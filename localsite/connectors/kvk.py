"""KvK Handelsregister connector.

`KvKConnector` is the interface the pipeline depends on. `KvKApiConnector`
is the real implementation (needs KVK_API_KEY — stubbed until the key
arrives). `MockKvKConnector` is deterministic per handelsnaam so repeated
runs are reproducible and the pipeline runs end-to-end today.
"""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Protocol

import httpx


@dataclass(frozen=True)
class KvKRecord:
    kvk_number: str
    handelsnaam: str
    rechtsvorm: str
    sbi_code: str
    sbi_omschrijving: str
    inschrijfdatum: str  # ISO date
    nmi: bool
    status: str  # actief | opgeheven | faillissement | surseance


class KvKConnector(Protocol):
    def lookup(self, handelsnaam: str, postcode: str | None) -> KvKRecord | None:
        """Best-match Handelsregister record for a trade name near a postcode."""
        ...


class KvKApiConnector:
    """Real Handelsregister API (https://developers.kvk.nl).

    Flow once the key is live: GET /v2/zoeken?handelsnaam=..&postcode=..
    to resolve a kvkNummer, then GET /v1/basisprofielen/{kvkNummer} for
    rechtsvorm, SBI, materieleRegistratie.datumAanvang and
    nonMailingIndicator. Both behind `apikey` header.
    """

    BASE = "https://api.kvk.nl/api"

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ.get("KVK_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "KVK_API_KEY not set — use MockKvKConnector until the key arrives"
            )
        self._client = httpx.Client(headers={"apikey": self.api_key}, timeout=30)

    def lookup(self, handelsnaam: str, postcode: str | None) -> KvKRecord | None:
        raise NotImplementedError(
            "Wire up /v2/zoeken + /v1/basisprofielen when the API key arrives"
        )


# --- Mock -------------------------------------------------------------------

# OSM category -> plausible SBI. Fallback is generic retail.
_SBI_BY_CATEGORY: dict[str, tuple[str, str]] = {
    "bakery": ("4724", "Winkels in brood en banket"),
    "butcher": ("4722", "Winkels in vlees en vleeswaren"),
    "hairdresser": ("96021", "Haarverzorging"),
    "beauty": ("96022", "Schoonheidsverzorging"),
    "florist": ("47761", "Winkels in bloemen en planten"),
    "bicycle": ("47641", "Winkels in fietsen en bromfietsen"),
    "car_repair": ("45204", "Autoservicebedrijven"),
    "supermarket": ("4711", "Supermarkten"),
    "clothes": ("4771", "Winkels in kleding"),
    "optician": ("47782", "Winkels in optische artikelen"),
    "restaurant": ("5610", "Restaurants"),
    "cafe": ("5630", "Cafés"),
    "fast_food": ("56102", "Fastfoodrestaurants en snackbars"),
    "dentist": ("86231", "Praktijken van tandartsen"),
    "doctors": ("8621", "Praktijken van huisartsen"),
    "pharmacy": ("47731", "Apotheken"),
    "veterinary": ("75001", "Veterinaire diensten"),
    "physiotherapist": ("86919", "Paramedische praktijken"),
    "gym": ("93130", "Fitnesscentra"),
    "fitness_centre": ("93130", "Fitnesscentra"),
    "lawyer": ("69101", "Advocatenkantoren"),
    "accountant": ("69201", "Accountantskantoren"),
    "estate_agent": ("68311", "Bemiddeling bij handel in onroerend goed"),
    "notary": ("69102", "Notariskantoren"),
    "electrician": ("43210", "Elektrotechnische installatie"),
    "plumber": ("43221", "Loodgieterswerk"),
}
_SBI_FALLBACK = ("4778", "Overige detailhandel")

_RECHTSVORMEN = [
    # (rechtsvorm, cumulative weight out of 100) — roughly NL MKB reality
    ("Eenmanszaak", 48),
    ("Vennootschap onder firma", 62),
    ("Besloten vennootschap", 90),
    ("Naamloze vennootschap", 92),
    ("Stichting", 96),
    ("Maatschap", 100),
]

_STATUSES = [
    ("actief", 93),
    ("opgeheven", 97),
    ("faillissement", 99),
    ("surseance", 100),
]


def _pick(table: list[tuple[str, int]], roll: int) -> str:
    for value, ceiling in table:
        if roll < ceiling:
            return value
    return table[-1][0]


class MockKvKConnector:
    """Deterministic fake: same handelsnaam -> same record on every run."""

    def __init__(self, today: date | None = None):
        self.today = today or date.today()

    def lookup(self, handelsnaam: str, postcode: str | None) -> KvKRecord | None:
        digest = hashlib.sha256(handelsnaam.lower().encode()).digest()
        # independent byte streams for each attribute
        b = list(digest)

        if b[0] % 100 < 5:  # ~5% of OSM places have no KvK match
            return None

        rechtsvorm = _pick(_RECHTSVORMEN, b[1] % 100)
        status = _pick(_STATUSES, b[2] % 100)
        nmi = b[3] % 100 < 10  # ~10% opted out of direct marketing

        # ~8% registered within the last 12 months (F3 fodder);
        # the rest spread over 1..40 years back.
        if b[4] % 100 < 8:
            days_back = 30 + int.from_bytes(b[5:7], "big") % 330
        else:
            days_back = 365 + int.from_bytes(b[5:7], "big") % (365 * 39)
        inschrijfdatum = (self.today - timedelta(days=days_back)).isoformat()

        return KvKRecord(
            kvk_number=f"{17000000 + int.from_bytes(b[8:12], 'big') % 60000000:08d}",
            handelsnaam=handelsnaam,
            rechtsvorm=rechtsvorm,
            sbi_code=_SBI_FALLBACK[0],
            sbi_omschrijving=_SBI_FALLBACK[1],
            inschrijfdatum=inschrijfdatum,
            nmi=nmi,
            status=status,
        )

    def lookup_with_category(
        self, handelsnaam: str, postcode: str | None, category_value: str | None
    ) -> KvKRecord | None:
        """Like lookup(), but maps the OSM category to a plausible SBI code."""
        rec = self.lookup(handelsnaam, postcode)
        if rec is None or category_value not in _SBI_BY_CATEGORY:
            return rec
        sbi_code, sbi_oms = _SBI_BY_CATEGORY[category_value]
        return KvKRecord(
            **{**rec.__dict__, "sbi_code": sbi_code, "sbi_omschrijving": sbi_oms}
        )
