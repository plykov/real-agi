# Founder Pipeline — leading a founder from "I have a feeling" to a validated, fundable thesis

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/founder-pipeline/README.md`](../../../Ru/3_Verticals/founder-pipeline/README.md)

> **Part of the Real AGI portfolio.** The founder / business-launch vertical, and the portfolio's most complete single-project realization of *agent = pipeline + feedback + self-learning*. **Stage:** prototype (runnable, real synthetic runs with real cost; no live users or revenue yet).

A founder arrives with a half-formed, inarticulate idea. They do not need an answer; they need to be *led* from "I have a feeling" to "here is a validated, fundable thesis." The product is a chat system that takes the raw idea, enriches it through a guided dialogue into a structured, machine-readable idea profile, then hands that profile to a second pipeline — market, risk, and investment analysis producing a memo and report. It is for early-stage founders who today pay mentors, accelerators, and consultants, or settle for a plain LLM chat.

## How it realizes the concept

It uses the core's *scenario space* and *positioning* organs: turn a vague intent into a structured profile, then route it through analysis to locate where the idea actually stands. The pipeline is full and two-loop — a guided enrichment dialogue (with a security gate and intent router, a readiness gate, and a "marginal value" rule for when to stop asking) produces a handoff contract, which a second analyst pipeline consumes. Code steps hold the contract; model calls do the judgment — the "judgment vs. bookkeeping" split, made explicit. Above the product sits a designed learning contour: synthetic users run the system, an evaluator compares runs against golden references and proposes prompt improvements, gated by human review. This is the cleanest example in the portfolio of the offline "strong model designs, then exits" pattern.

## What exists today

A runnable prototype: the two-loop dialogue + analyst pipeline, a deterministic analyst pass with tests, versioned roles/criteria, a learning orchestrator with persisted cycles and proposals, and real synthetic runs with actual measured cost. Of all the cards it scores highest on the four gates. What is still ahead is the market stage: monetization (a SaaS funnel) is designed but not launched, and there are no live users or accumulated self-learning yet.

## Where it could go

*Hypothesis:* this is the same engine the [mentoring](../mentoring/README.md) vertical needs, already assembled for a different market. The universal machinery (the security→intent gateway, the enrichment-with-knowledge-status pattern, the readiness-gate / question-generator split, the synthetic user as a test reality, the learning orchestrator) is being deliberately lifted into [expert-constructor-core](../expert-constructor-core/README.md); Founder Pipeline is the first concrete vertical standing on top of it.
