# LocalSite Agent — M1 Harvest

Pipeline stage 1: harvest local businesses (Tilburg pilot) from OpenStreetMap
Overpass + KvK Handelsregister into SQLite, apply hard filters F1–F4 and
Telecommunicatiewet channel routing. See `CLAUDE.md` and `docs/` for the
authoritative specs.

## Run

```bash
pip install -r requirements.txt          # httpx only

# Live (needs egress to overpass-api.de):
python run_harvest.py --postcode 5038 --db localsite.db

# Offline / sandbox (synthetic fixture, clearly labeled):
python run_harvest.py --postcode 5038 --db localsite.db \
    --fixture fixtures/overpass_5038_synthetic.json
```

Idempotent: re-running upserts on `(osm_type, osm_id)`, skips already-enriched
rows, and never duplicates exclusion-log entries.

## Layout

- `localsite/schema.sql` — SQLite schema incl. compliance fields
- `localsite/connectors/overpass.py` — live Overpass query (shop/amenity/office/healthcare/craft, named, one postcode area) + fixture mode
- `localsite/connectors/kvk.py` — `KvKConnector` interface; `KvKApiConnector` stub (awaits `KVK_API_KEY`); deterministic `MockKvKConnector`
- `localsite/filters.py` — F1–F4, channel routing, and `assert_channel_allows()` — the in-code refusal M3/M5 generators must call before producing call scripts / cold emails
- `localsite/harvest.py` — orchestrator; `run_harvest.py` — CLI
- `scripts/make_fixture.py` — regenerates the synthetic fixture

## Spec flags (deliberate deviations & gaps — decide, don't let them rot)

1. **Rubric §5 "store only" list vs. what the pipeline needs.** §5 forbids
   storing anything beyond kvk/handelsnaam/rechtsvorm/SBI/address/phone/
   website/scores/exclusion_reason — but F1 needs `nmi`, F2 needs
   `kvk_status`, F3 + V-longevity need `inschrijfdatum`, §0b needs `channel`,
   and M2 will need staff size. These are stored anyway (pipeline can't run
   otherwise); the §5 list should be amended to include them, or the
   retention job must strip them at archive time.
2. **"Keyed on KvK number" (CLAUDE.md) vs. OSM-first harvest.** OSM records
   arrive without a KvK number (and ~5% never match). Schema uses a surrogate
   PK, `(osm_type, osm_id)` as ingest key, and `kvk_number` as UNIQUE
   nullable natural key.
3. **Unknown rechtsvorm → `print_or_walkin`.** Neither spec says what to do
   when KvK data is missing; defaulting to the restrictive channel is the
   only defensible reading. KvK-unmatched records stay `harvested` (not
   `active`) until real data lands.
4. **F1 "drop from pipeline entirely" vs. GDPR suppression.** NMI records are
   status `excluded` but the row (kvk_number + handelsnaam) is retained as a
   suppression entry — deleting it entirely would let the business re-enter
   on the next harvest, which is the worse compliance failure.
5. **F3 sits under "hard filters (exclude before scoring)" but says "park in
   nurture-later".** Implemented as park: status `nurture`, logged as F3 in
   the exclusion log, recheck date = registration + 13 months.
6. **F4 ">3 locations same handelsnaam" is untestable inside one postcode
   area.** A national chain with one shop in 5038 is caught only by the
   brand list; the location count becomes meaningful once harvest covers
   more of Tilburg.
7. **Environment**: sandbox blocks `overpass-api.de` (egress policy) —
   hence the fixture mode; and sandbox Python is 3.11, spec says 3.12
   (code runs on both).
