#!/usr/bin/env python3
"""Generate a SYNTHETIC Overpass-shaped fixture for postcode area 5038.

All business names, addresses and contact details below are invented.
This exists only because the dev sandbox blocks overpass-api.de; the live
connector produces the same element shape. Regenerate with:
    python scripts/make_fixture.py
"""

import json
import random
from pathlib import Path

random.seed(5038)  # reproducible

STREETS = [
    ("Bredaseweg", "5038"), ("Noordstraat", "5038"), ("Nieuwlandstraat", "5038"),
    ("Schouwburgring", "5038"), ("Willem II-straat", "5038"),
    ("Stationsstraat", "5038"), ("Heuvelring", "5038"), ("Tuinstraat", "5038"),
]

# (name, category_key, category_value, has_website, has_phone)
BUSINESSES = [
    # -- shops --
    ("Bakkerij De Korenschoof", "shop", "bakery", False, True),
    ("Slagerij van den Broek", "shop", "butcher", False, True),
    ("Kapsalon Knip & Klaar", "shop", "hairdresser", False, False),
    ("Haarstudio Meike", "shop", "hairdresser", True, True),
    ("Bloemsierkunst 't Boeketje", "shop", "florist", False, True),
    ("Tweewielers Peeters", "shop", "bicycle", True, True),
    ("Rijwielhandel De Ketting", "shop", "bicycle", False, True),
    ("Albert Heijn", "shop", "supermarket", True, True),           # F4
    ("Jumbo Verstappen", "shop", "supermarket", True, True),        # F4
    ("Kruidvat", "shop", "chemist", True, False),                   # F4
    ("Boekhandel Livius", "shop", "books", True, True),
    ("Kledingzaak Mode van Mari", "shop", "clothes", False, True),
    ("Zeeman", "shop", "clothes", True, False),                     # F4
    ("Juwelier Goudappel", "shop", "jewelry", True, True),
    ("Optiek Helder Zicht", "shop", "optician", True, True),
    ("Hans Anders", "shop", "optician", True, True),                # F4
    ("Dierenspeciaalzaak Vachtje", "shop", "pet", False, True),
    ("Wijnhandel Bacchus Tilburg", "shop", "alcohol", True, True),
    ("Schoenmakerij Zolen & Hakken", "shop", "shoe_repair", False, False),
    ("Fotostudio Lichtbeeld", "shop", "photo", True, True),
    ("IJzerwaren Gebr. Smulders", "shop", "hardware", False, True),
    ("Kaashandel De Zuivelhoeve Tilburg", "shop", "cheese", False, True),
    ("Autobedrijf Van Gorp", "shop", "car_repair", True, True),
    ("Garage De Cilinder", "shop", "car_repair", False, True),
    ("Kwik-Fit", "shop", "car_repair", True, True),                 # F4
    ("Naaimachinehuis Steek Vast", "shop", "sewing", False, False),
    ("Speelgoedwinkel De Blokkendoos", "shop", "toys", False, True),
    ("Delicatessen Puur & Eerlijk", "shop", "deli", True, True),
    ("Muziekhandel Fortissimo", "shop", "musical_instrument", True, True),
    ("Tabak & Gemak Centrum", "shop", "tobacco", False, True),
    # -- amenities (commercial) --
    ("Restaurant De Gouden Lepel", "amenity", "restaurant", True, True),
    ("Eetcafé Bij Tante Toos", "amenity", "restaurant", False, True),
    ("Bistro Noordhoek", "amenity", "restaurant", True, True),
    ("Pizzeria La Fontana", "amenity", "restaurant", False, True),
    ("Domino's Pizza", "amenity", "fast_food", True, True),         # F4
    ("Cafetaria 't Pleintje", "amenity", "fast_food", False, True),
    ("Snackbar De Smulhoek", "amenity", "fast_food", False, False),
    ("Café De Boekanier", "amenity", "cafe", False, True),
    ("Koffiehuis Bonen & Zo", "amenity", "cafe", True, True),
    ("Grand Café Wilhelmina", "amenity", "cafe", True, True),
    ("Tandartspraktijk Molenaar", "amenity", "dentist", True, True),
    ("Tandartsen aan de Ring", "amenity", "dentist", True, True),
    ("Huisartsenpraktijk Centrum-West", "amenity", "doctors", True, True),
    ("Apotheek De Vijzel", "amenity", "pharmacy", True, True),
    ("Dierenkliniek Beestenboel", "amenity", "veterinary", True, True),
    ("Sportschool IJzersterk", "amenity", "gym", False, True),
    ("Basic-Fit", "amenity", "gym", True, False),                   # F4
    ("Autorijschool De Groene Kaart", "amenity", "driving_school", False, True),
    # -- healthcare --
    ("Fysiotherapie Corpus Tilburg", "healthcare", "physiotherapist", False, True),
    ("Praktijk voor Fysiotherapie Rugsteun", "healthcare", "physiotherapist", True, True),
    ("Podotherapie Voetenwerk", "healthcare", "podiatrist", False, True),
    # -- offices --
    ("Advocatenkantoor Hendrickx & Partners", "office", "lawyer", True, True),
    ("Notariskantoor Van der Zanden", "office", "notary", True, True),
    ("Administratiekantoor Cijfers op Orde", "office", "accountant", False, True),
    ("Accountants Brabant Zuid", "office", "accountant", True, True),
    ("Makelaardij Huis & Haard Tilburg", "office", "estate_agent", True, True),
    ("Assurantiekantoor De Polder", "office", "insurance", False, True),
    ("Uitzendbureau WerkDirect", "office", "employment_agency", True, True),
    # -- crafts --
    ("Installatiebedrijf Warmtebron", "craft", "plumber", False, True),
    ("Elektro Van Riel", "craft", "electrician", False, True),
    ("Schildersbedrijf Kleurrijk", "craft", "painter", True, True),
]


def main() -> None:
    elements = []
    for i, (name, key, value, has_web, has_phone) in enumerate(BUSINESSES):
        street, pc4 = random.choice(STREETS)
        letters = random.choice(["AB", "CD", "EK", "GM", "JN", "LP"])
        slug = (
            name.lower()
            .replace(" ", "")
            .replace("'", "")
            .replace("&", "en")
            .replace("é", "e")
        )[:24]
        tags = {
            "name": name,
            key: value,
            "addr:street": street,
            "addr:housenumber": str(random.randint(1, 180)),
            "addr:postcode": f"{pc4} {letters}",
            "addr:city": "Tilburg",
        }
        if has_phone:
            tags["phone"] = f"+3113{random.randint(4000000, 5999999)}"
        if has_web:
            tags["website"] = f"https://www.{slug}.nl"
        elements.append(
            {
                "type": "node",
                "id": 9_900_000_000 + i,  # synthetic-range ids
                "lat": round(51.556 + random.uniform(-0.008, 0.008), 6),
                "lon": round(5.078 + random.uniform(-0.010, 0.010), 6),
                "tags": tags,
            }
        )

    out = Path(__file__).parent.parent / "fixtures" / "overpass_5038_synthetic.json"
    out.write_text(
        json.dumps(
            {
                "version": 0.6,
                "generator": "SYNTHETIC-FIXTURE (not real OSM data)",
                "elements": elements,
            },
            indent=1,
            ensure_ascii=False,
        )
    )
    print(f"Wrote {len(elements)} synthetic elements to {out}")


if __name__ == "__main__":
    main()
