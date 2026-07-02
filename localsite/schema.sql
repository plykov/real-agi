-- LocalSite Agent — M1 Harvest schema
-- Compliance fields per CLAUDE.md + rubric §5. See README "Spec flags" for
-- deliberate deviations from the rubric §5 store-only list.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS businesses (
    id                INTEGER PRIMARY KEY,

    -- Identity. Spec says "keyed on KvK number", but harvest is OSM-first:
    -- rows exist before (and sometimes without) a KvK match. kvk_number is
    -- the UNIQUE natural key once known; (osm_type, osm_id) is the ingest key.
    kvk_number        TEXT UNIQUE,
    osm_type          TEXT NOT NULL CHECK (osm_type IN ('node','way','relation')),
    osm_id            INTEGER NOT NULL,

    handelsnaam       TEXT NOT NULL,
    category_key      TEXT,             -- shop | amenity | office | healthcare | craft
    category_value    TEXT,             -- hairdresser, restaurant, dentist, ...

    -- KvK enrichment (MockKvKConnector until API key arrives)
    rechtsvorm        TEXT,
    sbi_code          TEXT,
    sbi_omschrijving  TEXT,
    inschrijfdatum    TEXT,             -- ISO date; drives F3 and V-longevity
    nmi               INTEGER,          -- Non-Mailing-Indicator; drives F1
    kvk_status        TEXT,             -- actief | opgeheven | faillissement | surseance; drives F2

    -- Address & published contact (rubric §5 allowed set)
    straat            TEXT,
    huisnummer        TEXT,
    postcode          TEXT,
    plaats            TEXT,
    telefoon          TEXT,             -- published business phone only, never private mobiles
    website           TEXT,
    lat               REAL,
    lon               REAL,

    -- Scores (filled by M2 Qualify; columns exist so §5 "scores" live here)
    viability_score   INTEGER,
    gap_score         INTEGER,
    prospect_score    REAL,
    tier              TEXT CHECK (tier IN ('A','B','C') OR tier IS NULL),

    -- Compliance switchboard (CLAUDE.md hard rules — never bypass)
    channel           TEXT CHECK (channel IN ('call_allowed','print_or_walkin') OR channel IS NULL),
    lawful_basis      TEXT NOT NULL DEFAULT 'legitimate_interest',
    lia_ref           TEXT NOT NULL DEFAULT 'LIA-TILBURG-2026-001',
    art14_notified    INTEGER NOT NULL DEFAULT 0,

    pipeline_status   TEXT NOT NULL DEFAULT 'harvested'
                      CHECK (pipeline_status IN
                        ('harvested','active','excluded','nurture','archived')),
    exclusion_reason  TEXT,

    created_at        TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at        TEXT NOT NULL DEFAULT (datetime('now')),

    UNIQUE (osm_type, osm_id)
);

-- Append-only exclusion log: GDPR accountability trail.
-- NMI (F1) rows are NOT deleted: the record is retained as a suppression
-- entry (kvk_number + handelsnaam) so the business can never re-enter the
-- pipeline via a future harvest. Retention job (M2+) strips other fields.
CREATE TABLE IF NOT EXISTS exclusion_log (
    id           INTEGER PRIMARY KEY,
    business_id  INTEGER NOT NULL REFERENCES businesses(id),
    filter_code  TEXT NOT NULL,        -- F1..F6
    reason       TEXT NOT NULL,
    excluded_at  TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (business_id, filter_code)
);

-- F3 park: too young to score, re-check at month 13 (rubric §0 F3).
CREATE TABLE IF NOT EXISTS nurture_later (
    business_id  INTEGER PRIMARY KEY REFERENCES businesses(id),
    parked_at    TEXT NOT NULL DEFAULT (datetime('now')),
    recheck_on   TEXT NOT NULL         -- inschrijfdatum + 13 months
);

CREATE INDEX IF NOT EXISTS idx_businesses_status  ON businesses (pipeline_status);
CREATE INDEX IF NOT EXISTS idx_businesses_channel ON businesses (channel);
