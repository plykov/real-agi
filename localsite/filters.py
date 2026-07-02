"""Hard filters F1–F4 and channel routing (rubric §0 / §0b).

F5 (recent redesign) and F6 (paid ads) need web probes and belong to M2.
The channel switch is Telecommunicatiewet compliance — as of 1 Jul 2026
(in force) cold calls/emails to natuurlijke personen are prohibited.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta

# Rechtsvormen that are rechtspersonen -> B2B telemarketing permitted.
_RECHTSPERSOON = {
    "besloten vennootschap", "bv",
    "naamloze vennootschap", "nv",
    "stichting", "vereniging", "coöperatie", "cooperatie",
    "onderlinge waarborgmaatschappij",
}

# Natuurlijke personen (or partnerships thereof) -> print/walk-in only.
_NATUURLIJK_PERSOON = {
    "eenmanszaak",
    "vennootschap onder firma", "vof",
    "maatschap",
    "commanditaire vennootschap", "cv",
}

# NL franchise / formule brands for F4, matched on word boundaries
# (plain substring match flags "De Ketting" for "ing").
# Deliberately conservative: only names that are unambiguously chains.
FRANCHISE_NAMES = {
    "albert heijn", "jumbo", "aldi", "lidl", "plus", "spar", "coop",
    "hema", "action", "blokker", "zeeman", "wibra", "kruidvat", "etos",
    "trekpleister", "primera", "bruna", "gall & gall", "gall en gall",
    "mcdonald", "burger king", "kfc", "subway", "domino", "new york pizza",
    "kwalitaria", "bakker bart", "multivlaai", "bakkerij bart",
    "anytime fitness", "basic-fit", "basic fit", "fit for free",
    "pearle", "specsavers", "hans anders", "eyewish",
    "kwik-fit", "kwikfit", "profile", "halfords",
    "shell", "bp", "esso", "texaco", "tango", "tinq",
    "ing", "rabobank", "abn amro", "sns",
}

MAX_SAME_NAME_LOCATIONS = 3  # F4: >3 locations same handelsnaam = formule


@dataclass(frozen=True)
class FilterResult:
    passed: bool
    filter_code: str | None = None  # F1..F4
    reason: str | None = None
    park_nurture: bool = False      # F3 parks instead of excluding


def route_channel(rechtsvorm: str | None) -> str:
    """Rubric §0b. Unknown rechtsvorm defaults to the restrictive channel:
    without KvK confirmation we must assume natuurlijk persoon."""
    if rechtsvorm is None:
        return "print_or_walkin"
    rv = rechtsvorm.strip().lower()
    if rv in _RECHTSPERSOON:
        return "call_allowed"
    if rv in _NATUURLIJK_PERSOON:
        return "print_or_walkin"
    return "print_or_walkin"


def assert_channel_allows(channel: str, artifact: str) -> None:
    """The in-code refusal demanded by CLAUDE.md / rubric §0b.

    M3/M5 generators MUST call this before producing call scripts or
    cold-email copy. Raises — does not warn — for print_or_walkin records.
    """
    if artifact in ("call_script", "cold_email") and channel != "call_allowed":
        raise PermissionError(
            f"Refusing to generate {artifact!r} for channel {channel!r}: "
            "Telecommunicatiewet prohibits cold outreach to natuurlijke personen "
            "(rubric §0b). This check is deliberate — do not bypass."
        )
    if artifact == "cold_email":
        # Even for rechtspersonen, cold email is NO by default (CLAUDE.md):
        # only allowed when an address is published expressly for offers.
        raise PermissionError(
            "Cold email is disabled by default for all records (CLAUDE.md "
            "channel rules); requires an address published expressly for offers."
        )


def apply_hard_filters(
    handelsnaam: str,
    nmi: bool | None,
    kvk_status: str | None,
    inschrijfdatum: str | None,  # ISO date
    same_name_locations: int,
    today: date,
) -> FilterResult:
    """F1–F4 in rubric order. First hit wins. None values (no KvK match)
    pass F1–F3 unchecked — the record stays 'harvested' and is re-filtered
    once real KvK data lands."""

    # F1 — NMI: legal opt-out from direct marketing.
    if nmi:
        return FilterResult(False, "F1", "Non-Mailing-Indicator set (KvK)")

    # F2 — not an active business.
    if kvk_status is not None and kvk_status != "actief":
        return FilterResult(False, "F2", f"KvK status '{kvk_status}' ≠ actief")

    # F3 — younger than 12 months: park, don't drop.
    if inschrijfdatum is not None:
        registered = date.fromisoformat(inschrijfdatum)
        if registered > today - timedelta(days=365):
            return FilterResult(
                False, "F3",
                f"Registered {inschrijfdatum} (<12 months) — nurture-later, "
                "re-check at month 13",
                park_nurture=True,
            )

    # F4 — chain / franchise / formule.
    name_lower = handelsnaam.lower()
    for brand in FRANCHISE_NAMES:
        if re.search(rf"(?<!\w){re.escape(brand)}(?!\w)", name_lower):
            return FilterResult(
                False, "F4", f"Franchise brand match: '{brand}' — HQ decides website"
            )
    if same_name_locations > MAX_SAME_NAME_LOCATIONS:
        return FilterResult(
            False, "F4",
            f"{same_name_locations} locations share handelsnaam — formule",
        )

    return FilterResult(True)


def nurture_recheck_date(inschrijfdatum: str) -> str:
    """Month 13 after registration (rubric F3)."""
    registered = date.fromisoformat(inschrijfdatum)
    return (registered + timedelta(days=395)).isoformat()
