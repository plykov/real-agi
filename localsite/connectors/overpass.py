"""Overpass API connector — OSM business harvest for one postcode area.

ODbL attribution applies to stored OSM-derived data. Never Google Maps.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import httpx

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

# One query, three element classes. `nwr` covers nodes/ways/relations;
# `out center` gives ways/relations a representative lat/lon. Requiring
# "name" drops unnamed infrastructure (benches, vending machines).
QUERY_TEMPLATE = """
[out:json][timeout:90];
area["name"="{city}"]["boundary"="administrative"]["admin_level"="8"]->.city;
(
  nwr(area.city)["addr:postcode"~"^{postcode4}"]["name"]["shop"];
  nwr(area.city)["addr:postcode"~"^{postcode4}"]["name"]["amenity"];
  nwr(area.city)["addr:postcode"~"^{postcode4}"]["name"]["office"];
  nwr(area.city)["addr:postcode"~"^{postcode4}"]["name"]["healthcare"];
  nwr(area.city)["addr:postcode"~"^{postcode4}"]["name"]["craft"];
);
out center tags;
"""

# Element classes we treat as businesses, in priority order when several
# tags coexist (a dentist can carry both amenity=dentist and healthcare=*).
CATEGORY_KEYS = ("shop", "amenity", "office", "healthcare", "craft")

# amenity=* is a grab-bag; keep only commercial values.
AMENITY_ALLOW = {
    "restaurant", "cafe", "bar", "pub", "fast_food", "ice_cream",
    "dentist", "doctors", "clinic", "pharmacy", "veterinary",
    "driving_school", "car_rental", "car_wash", "fuel",
    "bank", "bureau_de_change", "gym", "fitness_centre",
}


def fetch_elements(
    postcode4: str,
    city: str = "Tilburg",
    fixture: str | Path | None = None,
    max_retries: int = 3,
) -> list[dict]:
    """Return raw Overpass elements, live or from a fixture file."""
    if fixture is not None:
        payload = json.loads(Path(fixture).read_text())
    else:
        query = QUERY_TEMPLATE.format(city=city, postcode4=postcode4)
        for attempt in range(max_retries):
            try:
                resp = httpx.post(OVERPASS_URL, data={"data": query}, timeout=120)
                resp.raise_for_status()
                payload = resp.json()
                break
            except httpx.HTTPError:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** (attempt + 1))  # be polite to a free API
    return payload.get("elements", [])


def parse_element(el: dict) -> dict | None:
    """Overpass element -> flat place dict for db.upsert_place, or None to skip."""
    tags = el.get("tags", {})
    name = tags.get("name")
    if not name:
        return None

    category_key = category_value = None
    for key in CATEGORY_KEYS:
        if key in tags:
            category_key, category_value = key, tags[key]
            break
    if category_key is None:
        return None
    if category_key == "amenity" and category_value not in AMENITY_ALLOW:
        return None

    lat = el.get("lat") or el.get("center", {}).get("lat")
    lon = el.get("lon") or el.get("center", {}).get("lon")

    return {
        "osm_type": el["type"],
        "osm_id": el["id"],
        "handelsnaam": name,
        "category_key": category_key,
        "category_value": category_value,
        "straat": tags.get("addr:street"),
        "huisnummer": tags.get("addr:housenumber"),
        "postcode": tags.get("addr:postcode"),
        "plaats": tags.get("addr:city", "Tilburg"),
        "telefoon": tags.get("phone") or tags.get("contact:phone"),
        "website": tags.get("website") or tags.get("contact:website"),
        "lat": lat,
        "lon": lon,
    }
