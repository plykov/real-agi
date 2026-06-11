# Course Distributor — the publishing engine that puts finished courses on live platforms

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/course-distributor/README.md`](../../../Ru/3_Verticals/course-distributor/README.md)

> **Part of the Real AGI portfolio.** A node in the creator / expert-economy family — the distribution side of course production, sibling to [course-producer](../course-producer/README.md) (which builds the content this engine ships). **Stage:** working, with real production deploys; an internal tool, no external market yet.

Course Distributor takes a finished markdown course bundle — handed off from its sibling, course-producer — and publishes it correctly onto live platforms: WordPress (an LMS plus access control) and GitHub (free courses routed to a public repo, paid to a private one). It deliberately does not write or edit content. Its job is everything *after* authoring: convert markdown to HTML, stage, test, deploy to production, verify, and record the result. The user is the operator of a course marketplace who needs each lesson to land on the live site without breaking it.

## How it realizes the concept

This is a genuine multi-step **pipeline with feedback**, not a single utility, and it sits one rung below an agent-vertical. A three-layer architecture — intelligence (the agent as orchestrator) over deterministic actions (scripts) over a fixed protocol (the single sanctioned "deploy canon") — separates judgment from bookkeeping. It learns *between* runs through an institutionalized incident-to-rule loop: every production regression becomes a documented trap and a hard prohibition that constrains the next deploy. What it lacks, by design, is the navigator figure: it has no client with a goal whom it leads. It is the *executing organ* a learning vertical would use — the channel that delivers whatever a mentor-core prescribes — not the mentor itself.

## What exists today

A working engine with real production deploys (reference lessons published to a live site; baseline snapshots captured). Built: the deploy canon, markdown→HTML rendering, WordPress and GitHub deploy paths, reverse WP→markdown export, cross-platform link verification, before/after snapshots with sanity checks, and a documented model of the LMS's awkward quiz internals.

## Where it could go

*Hypothesis:* generalized from one site to a platform-agnostic publishing layer — a reusable distribution module that any Real AGI vertical could call to deliver assigned content across LMS targets. The domain-specific WordPress mechanics would need extracting into a stable contract before that universal engine exists.
