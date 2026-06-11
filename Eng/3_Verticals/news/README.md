# News — author's news-digest pipeline (curate → comment → publish)

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/news/README.md`](../../../Ru/3_Verticals/news/README.md)

> **Part of the Real AGI portfolio.** A content-production pipeline: it ingests human-curated articles, generates author-voiced commentary, and distributes a finished digest across social platforms. It sits one rung below an agent on the ladder — a multi-step pipeline toward a goal, but without a feedback loop or self-learning. **Stage:** working production (Docker/VPS, live published digests).

The author curates news by hand — sharing articles from a reader app into a bot (or a browser extension / mobile shortcut). When enough articles accumulate, a queue manager fires a two-phase generation: an LLM writes a sardonic, voice-preserving comment per article, then assembles them into a formatted digest with hashtags and a course mention. From a dashboard, the author publishes to social platforms with one button. It removes the production drudgery of running a news channel — built for authors, bloggers, and experts who maintain a media presence and a funnel to their courses.

## How it realizes the concept

This is the "executive hand," not the navigator. The pipeline does *production and delivery* — judgment is narrowly scoped (comment one article) and bookkeeping (queueing, dedup, assembly, publishing) is deterministic code, exactly the component-pattern the corpus argues for. But the human here is the operator-beneficiary of a fixed cycle, not a *led* client: the system doesn't model the author's situation, fan out scenarios, or recommend a strategy. It executes one path well. On the particular→general path it is a clean instance of "expert that produces," still short of "expert that leads."

## What exists today

Production-deployed: a store, a queue manager, two-phase generation with externalized style prompts, multi-platform publishers, an authenticated dashboard with human-in-the-loop approval, and hard-won platform knowledge (shadow-ban research, length limits, rate-limit retries). Image and video pipelines are described as in-development; readiness unverified.

## Where it could go

*Hypothesis:* the missing rungs to "agent": close the loop by collecting publication metrics (reach, reactions) and letting them steer topic and tone of the next digest (feedback), accumulate experience across runs (self-learning), and add a leading layer that advises the author on presence strategy rather than only executing — at which point the navigator core could decide "what and why to publish" while this pipeline handles "how to produce and deliver."
