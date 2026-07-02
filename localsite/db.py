"""SQLite access layer. Single-city scale; no ORM."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def connect(db_path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA_PATH.read_text())
    return conn


def upsert_place(conn: sqlite3.Connection, place: dict) -> int:
    """Idempotent ingest keyed on (osm_type, osm_id). Returns business id.

    Only harvest-owned columns are touched on conflict; KvK enrichment,
    scores, and compliance state set by later steps are preserved.
    """
    cur = conn.execute(
        """
        INSERT INTO businesses (
            osm_type, osm_id, handelsnaam, category_key, category_value,
            straat, huisnummer, postcode, plaats, telefoon, website, lat, lon
        ) VALUES (
            :osm_type, :osm_id, :handelsnaam, :category_key, :category_value,
            :straat, :huisnummer, :postcode, :plaats, :telefoon, :website, :lat, :lon
        )
        ON CONFLICT (osm_type, osm_id) DO UPDATE SET
            handelsnaam    = excluded.handelsnaam,
            category_key   = excluded.category_key,
            category_value = excluded.category_value,
            straat         = excluded.straat,
            huisnummer     = excluded.huisnummer,
            postcode       = excluded.postcode,
            plaats         = excluded.plaats,
            telefoon       = excluded.telefoon,
            website        = excluded.website,
            lat            = excluded.lat,
            lon            = excluded.lon,
            updated_at     = datetime('now')
        RETURNING id
        """,
        place,
    )
    return cur.fetchone()[0]


def log_exclusion(
    conn: sqlite3.Connection, business_id: int, filter_code: str, reason: str
) -> None:
    conn.execute(
        """
        INSERT INTO exclusion_log (business_id, filter_code, reason)
        VALUES (?, ?, ?)
        ON CONFLICT (business_id, filter_code) DO NOTHING
        """,
        (business_id, filter_code, reason),
    )


def park_nurture(conn: sqlite3.Connection, business_id: int, recheck_on: str) -> None:
    conn.execute(
        """
        INSERT INTO nurture_later (business_id, recheck_on)
        VALUES (?, ?)
        ON CONFLICT (business_id) DO UPDATE SET recheck_on = excluded.recheck_on
        """,
        (business_id, recheck_on),
    )
