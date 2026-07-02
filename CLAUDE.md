# LocalSite Agent — Project Context

Agent pipeline that finds local businesses with weak web presence (NL, Tilburg pilot), generates positioning + demo websites, and produces compliant outreach material for selling website subscriptions.

Owner: Pavel — enterprise sales background, building this as a side venture. Prefers ranked options, honest pushback, evidence-based decisions, concise output.

## Pipeline (5 stages)

1. **Harvest** — city-level business catalog. Sources: OpenStreetMap Overpass API (free, ODbL) + KvK Handelsregister API (authoritative; gives rechtsvorm, SBI, inschrijfdatum, NMI flag). NEVER scrape Google Maps (ToS). Store in SQLite keyed on KvK number.
2. **Qualify & enrich** — DNS/HTTP probe, SSL check, mobile responsiveness, PageSpeed Insights API, Google Business Profile signals (review count/rating/photos/hours), findability check. Score per `docs/qualification-rubric.md` — this file is authoritative for all scoring logic, hard filters, tiers, and retention rules.
3. **Position** — one Claude API call per qualified prospect producing a strict-JSON positioning brief. System prompt, schema, validation and orchestrator notes are in `docs/positioning-prompt.md` — authoritative, use verbatim. Pre-call: cheap Haiku-class review-theme extraction (themes only, never verbatim review text).
4. **Generate & deploy demo** — Astro + Tailwind from a component template library, populated from the positioning brief. Deploy to Cloudflare Pages via API (free tier).
5. **Proposition** — printed one-pager with QR to demo (primary channel), call scripts only for BV-tagged records. Subscription model: €0 setup, €59–99/month (hosting, maintenance, edits, one added-value service: GBP optimization, review-request QR flow, booking widget, NL/EN bilingual, quarterly web-presence report).

## Compliance hard rules (enforce in code, never bypass)

- **NMI**: KvK Non-Mailing-Indicator set → exclude from pipeline entirely, log exclusion reason.
- **Channel routing by rechtsvorm** (Telecommunicatiewet, incl. 1 Jul 2026 amendment):
  - BV/NV/rechtspersoon → `channel: call_allowed` (cold email still NO by default)
  - Eenmanszaak/VOF/natuurlijk persoon → `channel: print_or_walkin` — code must REFUSE to generate cold-call scripts or cold emails for these records
- **Demo sites**: `noindex` meta + password protection or unguessable URL. No scraped photos (copyright) — placeholders/licensed stock only. No cookies, no analytics, self-hosted fonts (no Google Fonts CDN) → no cookie banner needed, which is a selling point.
- **No verbatim review quotes** anywhere in generated artifacts; themes only.
- **GDPR**: lawful basis = legitimate interest; every record carries `lawful_basis`, `lia_ref`, `art14_notified` fields. Eenmanszaak business data = personal data. Store only fields listed in rubric §5; delete/anonymize archived records after 12 months.
- No health-outcome claims for zorg-verticals in generated copy.

## Tech decisions (made — don't relitigate without reason)

- Python 3.12 orchestrator, SQLite (single-city scale), httpx for probes
- Astro + Tailwind for demo sites; one template repo, per-prospect content injection
- Cloudflare Pages for hosting (API deploy, free tier)
- Claude API: `claude-sonnet-4-6` for positioning, Haiku-class for theme extraction
- Config in `.env` (KvK API key, Anthropic key, CF token); never commit secrets

## Build order

1. **M1 — Harvest**: Overpass + KvK connectors, SQLite schema (incl. compliance fields), one Tilburg postcode area end-to-end
2. **M2 — Qualify**: enrichment probes + rubric scorer; output tier distribution report → tune weights against real data before proceeding
3. **M3 — Position**: theme extractor + positioning call + JSON validation/banned-word scan
4. **M4 — Generate**: Astro template + injection + CF Pages deploy with noindex/password
5. **M5 — Proposition**: one-pager generator (per-prospect PDF with QR), BV-only call script generator

## Conventions

- Every pipeline stage idempotent and resumable; log exclusions with reasons (GDPR accountability)
- Human gate before Tier A demo deploy: check `differentiators[].evidence` only
- Dutch primary language in all customer-facing output
