"""M1 Harvest orchestrator: Overpass -> SQLite -> KvK enrich -> F1–F4 -> channel.

Idempotent: re-runs upsert on (osm_type, osm_id), skip already-enriched
rows, and never duplicate exclusion-log entries.
"""

from __future__ import annotations

import sqlite3
from collections import Counter
from datetime import date
from pathlib import Path

from . import db
from .connectors import overpass
from .connectors.kvk import MockKvKConnector
from .filters import (
    apply_hard_filters,
    nurture_recheck_date,
    route_channel,
)


def run(
    db_path: str | Path,
    postcode4: str = "5038",
    city: str = "Tilburg",
    fixture: str | Path | None = None,
    today: date | None = None,
) -> dict:
    today = today or date.today()
    conn = db.connect(db_path)

    # 1. Harvest from Overpass (live or fixture)
    elements = overpass.fetch_elements(postcode4, city=city, fixture=fixture)
    harvested = 0
    for el in elements:
        place = overpass.parse_element(el)
        if place is None:
            continue
        db.upsert_place(conn, place)
        harvested += 1
    conn.commit()

    # 2. KvK enrichment (mock until API key). Skip rows already enriched.
    kvk = MockKvKConnector(today=today)
    rows = conn.execute(
        """SELECT id, handelsnaam, postcode, category_value FROM businesses
           WHERE kvk_number IS NULL AND pipeline_status = 'harvested'"""
    ).fetchall()
    kvk_matched = kvk_unmatched = 0
    for row in rows:
        rec = kvk.lookup_with_category(
            row["handelsnaam"], row["postcode"], row["category_value"]
        )
        if rec is None:
            kvk_unmatched += 1
            continue
        try:
            conn.execute(
                """UPDATE businesses SET
                       kvk_number = ?, rechtsvorm = ?, sbi_code = ?,
                       sbi_omschrijving = ?, inschrijfdatum = ?, nmi = ?,
                       kvk_status = ?, updated_at = datetime('now')
                   WHERE id = ?""",
                (
                    rec.kvk_number, rec.rechtsvorm, rec.sbi_code,
                    rec.sbi_omschrijving, rec.inschrijfdatum, int(rec.nmi),
                    rec.status, row["id"],
                ),
            )
            kvk_matched += 1
        except sqlite3.IntegrityError:
            # Two OSM places resolved to one KvK number (multi-entrance
            # premises). Keep the first; the duplicate stays unenriched.
            kvk_unmatched += 1
    conn.commit()

    # 3. Hard filters F1–F4 + channel routing on every non-archived record.
    name_counts = Counter(
        r["handelsnaam"].lower()
        for r in conn.execute("SELECT handelsnaam FROM businesses").fetchall()
    )
    rows = conn.execute(
        """SELECT id, handelsnaam, nmi, kvk_status, inschrijfdatum, rechtsvorm
           FROM businesses WHERE pipeline_status != 'archived'"""
    ).fetchall()

    exclusions: Counter[str] = Counter()
    channels: Counter[str] = Counter()
    active = nurtured = 0

    for row in rows:
        result = apply_hard_filters(
            handelsnaam=row["handelsnaam"],
            nmi=None if row["nmi"] is None else bool(row["nmi"]),
            kvk_status=row["kvk_status"],
            inschrijfdatum=row["inschrijfdatum"],
            same_name_locations=name_counts[row["handelsnaam"].lower()],
            today=today,
        )
        channel = route_channel(row["rechtsvorm"])

        if result.passed:
            conn.execute(
                """UPDATE businesses SET pipeline_status = 'active',
                       channel = ?, exclusion_reason = NULL,
                       updated_at = datetime('now')
                   WHERE id = ?""",
                (channel, row["id"]),
            )
            channels[channel] += 1
            active += 1
        elif result.park_nurture:
            conn.execute(
                """UPDATE businesses SET pipeline_status = 'nurture',
                       channel = ?, exclusion_reason = ?,
                       updated_at = datetime('now')
                   WHERE id = ?""",
                (channel, result.reason, row["id"]),
            )
            db.log_exclusion(conn, row["id"], result.filter_code, result.reason)
            db.park_nurture(
                conn, row["id"], nurture_recheck_date(row["inschrijfdatum"])
            )
            exclusions[result.filter_code] += 1
            nurtured += 1
        else:
            conn.execute(
                """UPDATE businesses SET pipeline_status = 'excluded',
                       channel = NULL, exclusion_reason = ?,
                       updated_at = datetime('now')
                   WHERE id = ?""",
                (result.reason, row["id"]),
            )
            db.log_exclusion(conn, row["id"], result.filter_code, result.reason)
            exclusions[result.filter_code] += 1
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM businesses").fetchone()[0]
    report = {
        "source": "fixture" if fixture else "overpass_live",
        "postcode_area": postcode4,
        "harvested_this_run": harvested,
        "total_records": total,
        "kvk_matched": kvk_matched,
        "kvk_unmatched": kvk_unmatched,
        "active": active,
        "nurture": nurtured,
        "exclusions": dict(sorted(exclusions.items())),
        "channel_split": dict(sorted(channels.items())),
    }
    conn.close()
    return report
