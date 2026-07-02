# Stage 2 — Prospect Qualification Rubric
**Web Presence Gap engine · v1.0 · NL market (Tilburg pilot)**

Core logic: `Prospect Score = (Viability × Gap) / 100`

Multiplicative, not additive — deliberately. A thriving business with a great website (high V, zero G) scores near zero. A dying business with no website (zero V, high G) also scores near zero. You only pitch where **money meets neglect**.

---

## 0. Hard filters (exclude before scoring)

| # | Filter | Source | Rationale |
|---|--------|--------|-----------|
| F1 | Non-Mailing-Indicator (NMI) set | KvK | Legal: they opted out of direct marketing. Drop from pipeline, log exclusion. |
| F2 | Status ≠ actief (faillissement, surseance, opgeheven) | KvK | No revenue to sell to. |
| F3 | Registered < 12 months ago | KvK inschrijfdatum | Too unstable; no review history to position on. Park in a "nurture-later" table, re-check at month 13. |
| F4 | Chain / franchise / formule | Brand-name match against franchise list + >3 locations same handelsnaam | Website decided at HQ; local owner can't buy. |
| F5 | Website redesigned within ~18 months | Wayback Machine diff, copyright year, agency credit in footer | Just spent the budget; you're pitching against a fresh sunk cost. |
| F6 | Actively running paid ads | Meta Ad Library check (free API) | Marketing-mature; they have an agency. Different pitch, different pipeline — exclude from v1. |

## 0b. Channel routing (not a filter — a compliance switch)

Read `rechtsvorm` from KvK and tag every surviving record:

- **BV / NV / rechtspersoon** → `channel: call_allowed` (B2B telemarketing to rechtspersonen remains permitted; email only if an address is published expressly for commercial offers — rare, default to no)
- **Eenmanszaak / VOF / natuurlijk persoon** → `channel: print_or_walkin` (as of 1 Jul 2026 no cold calls, no cold email; personal data rules apply — set Art. 14 notice flag for first contact)

The agent must refuse to generate call scripts or cold emails for `print_or_walkin` records. Build the refusal into the pipeline, not into your memory.

---

## 1. Viability score (V, 0–100) — "is there money here?"

| Signal | Weight | Scoring | Source |
|---|---|---|---|
| Review volume | 25 | 0 revs = 0 · 1–14 = 8 · 15–49 = 15 · 50–149 = 22 · ≥150 = 25 | Google Business Profile (GBP) |
| Rating quality | 15 | 4.2–4.8 = 15 · 3.8–4.1 = 10 · ≥4.9 with <20 revs = 6 (noise) · <3.8 = 3 | GBP |
| Longevity | 15 | 3–7 yrs = 10 · 8–19 yrs = 15 · ≥20 yrs = 13 (succession risk) · <3 = 4 | KvK inschrijfdatum |
| Vertical ticket size | 20 | Tier 1 = 20: tandarts, fysio, garage, installateur, advocaat, notaris, accountant, kliniek · Tier 2 = 13: kapper, restaurant, bakker, sportschool, dierenarts · Tier 3 = 6: snackbar, kiosk, tweedehands | SBI code (KvK) |
| Staff size band | 15 | 2–9 wp = 15 · 10–49 = 12 (may have internal marketing) · 1 = 8 · 0/unknown = 4 | KvK |
| Physical premises | 10 | Street-level commercial address = 10 · office/praktijk = 8 · residential/postbus = 2 | KvK adres + OSM tag |

**Why the ≥4.9 penalty:** a 5.0 with 12 reviews is statistically friends-and-family; a 4.5 with 200 reviews is a real customer engine. Volume × quality beats quality alone.

**Why ≥20 yrs scores lower than 8–19:** strong business, but elevated odds the owner is 60+ and web-indifferent or exit-minded. Still pitchable — the site becomes "sale-readiness" positioning — but conversion is lower.

## 2. Gap score (G, 0–100) — "how badly do they need you?"

| Signal | Weight | Scoring | Source |
|---|---|---|---|
| Website existence | 30 | None/parked domain = 30 · Facebook-page-only = 26 · directory listing only (e.g. Telefoonboek) = 24 · has real site = 0, continue below | DNS + HTTP probe |
| Technical quality (only if site exists) | 20 | No SSL = +8 · not mobile responsive = +7 · PageSpeed mobile <40 = +5 | HTTP probe, PSI API |
| Content staleness | 15 | Copyright/date ≥3 yrs stale = +6 · dead links or "under construction" = +5 · no visible services/prices = +4 | Crawler |
| Conversion machinery | 15 | No contact form = +5 · no booking/appointment path in a bookable vertical = +7 · no click-to-call on mobile = +3 | Crawler |
| GBP hygiene | 12 | Missing hours = +3 · <3 photos = +3 · owner never replies to reviews = +3 · unclaimed profile = +3 | GBP |
| Findability | 8 | Not ranking top-3 for "{handelsnaam} {stad}" = +8 | 1 search per record |

## 3. Tiers and pipeline action

| Prospect Score | Tier | Action |
|---|---|---|
| ≥ 55 | **A** | Generate full demo site + positioning brief + printed one-pager. Walk-in / mail this week. |
| 35–54 | **B** | Positioning brief + single mock homepage screenshot (cheaper than full demo). Batch outreach. |
| 20–34 | **C** | Hold. Re-score quarterly (sites decay; scores rise). |
| < 20 | — | Archive with exclusion reason (audit trail for GDPR accountability). |

## 4. Worked example

*Fysiopraktijk, Tilburg-West. Eenmanszaak, 2011, 3 medewerkers, GBP 4.6★/138 reviews, no website, claimed GBP but 2 photos and no review replies.*

- V = 22 (reviews) + 15 (rating) + 15 (longevity) + 20 (Tier 1) + 15 (staff) + 8 (praktijk) = **95**
- G = 30 (no site) + 3 + 3 (GBP hygiene) + 8 (findability) = **44**
- **PS = 95 × 44 / 100 = 41.8 → Tier B**, channel `print_or_walkin`

Counter-intuitive but correct: no website ≠ automatic Tier A. A 4.6★ practice with 138 reviews is *already winning without a site* — your pitch there is capacity/pricing power ("stop competing on availability, start converting searchers before they call your competitor"), and Tier B effort matches realistic urgency. The Tier A archetype is high-V *plus* a broken site actively costing them: garage with a dead SSL cert and no booking path.

## 5. Data & retention policy (enforce in code)

- Store only: KvK number, handelsnaam, rechtsvorm, SBI, address, published business phone, website URL, scores, exclusion reason. **No** private mobile numbers, no owner names unless legally required for contact records after engagement.
- Retention: C-tier and archived records → delete raw personal data after 12 months, keep only anonymized score stats.
- Every record carries `lawful_basis: legitimate_interest`, `lia_ref:` pointing to your written Legitimate Interest Assessment, and `art14_notified: bool`.
