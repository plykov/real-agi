# AI-Test01 — Idea Intake: a smart admission interview for raw founder ideas

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/ai-test01/README.md`](../../../Ru/3_Verticals/ai-test01/README.md)

> **Part of the Real AGI portfolio.** A founder / business-launch family member — and a notable source of candidate *core* machinery: a reusable intake layer, a Learning Orchestrator, and a Synthetic User Lab. Sibling and earlier line to [founder-pipeline](../founder-pipeline/README.md). **Stage:** working local prototype (real model calls; no auth, payments, or production deployment).

Idea Intake takes a founder's raw, unstructured idea, runs a clarifying dialogue, and gradually assembles a structured idea profile for a downstream analytical pipeline. It does not answer the founder and it does not produce the final analysis; it *leads* — a stage-aware expert that reads the current state of the profile and decides what the person needs next. The end consumer is mixed: a human founder, plus a downstream agent/code that receives a machine handoff. It is explicitly framed in-repo as a "Founder Mentor Pipeline."

## How it realizes the concept

It maps cleanly onto core + domain + market. **Domain:** packaging and enrichment of an entrepreneurial idea — section methodology, hypotheses-vs-facts, and the specific failure mode of intake collapsing into a premature spec, pricing grid, or ICP workshop. **Market:** founders at the idea stage (a commercial interface with funnels and pricing is designed but unsold), plus an adjacent agent-QA / synthetic-traffic line.

Several components look like *core* machinery rather than domain code. The **idea intake layer** (raw material → enrichment → section patch → readiness gate → next-question-or-handoff) resembles the navigator's reality-model and positioning layers. The **Learning Orchestrator** — runs compared to golden sessions, attribution, draft prompt/role improvements, and a check on whether the next run improved — is the closest analog in the portfolio to the core's signature: learning from labeled consequences of its own decisions. The **Synthetic User Lab** acts as a generator of training traffic. On the ladder this sits at *agent* (pipeline + feedback + partial self-learning) and a strong *vertical* candidate — though not yet on the shared Real AGI core.

## What exists today

Built: chat-first UI, a local store, real model calls, versioned editable prompts, the two-phase enrichment pipeline, readiness gate, terminal handoff, a human-readable idea document, multiple dialogue depths, a budgeted synthetic runner, and the learning loop persisting cycles, evaluations, and draft proposals with cost accounting. Not built: automatic prompt mutation (proposals stay draft), real users/revenue, production auth/payments.

## Where it could go

*Hypothesis:* the Learning Orchestrator and Synthetic User Lab are extracted as domain-agnostic infrastructure — "self-improvement infrastructure for many expert-agent products" — feeding the Real AGI core directly. Migration into [expert-constructor-core](../expert-constructor-core/README.md) and [founder-pipeline](../founder-pipeline/README.md) has already begun; this folder is now a legacy mixed repo from which the durable pieces are being lifted.
