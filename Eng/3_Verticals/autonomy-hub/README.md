# Autonomy Hub — the anti-paralysis engine, specified before it is built

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/autonomy-hub/README.md`](../../../Ru/3_Verticals/autonomy-hub/README.md)

> **Part of the Real AGI portfolio.** This is a core-engine layer: the scenario / anti-paralysis loop that keeps a project moving through deficits and blockers instead of stalling. **Stage:** design-stage — a control plane plus a near-complete kernel specification; the kernel's own runtime is not yet implemented.

Autonomy Hub is a control plane for designing an "autonomy kernel": the architecture of an agent that *carries a project through obstacles without freezing*. It consolidates definitions, a staged build plan, an engineering kernel spec, research on adjacent open-source systems, and registries of related projects. The central design move is deliberate: *the model is a resource, not the whole agent* — the kernel is an architecture above the model, in which judgment goes to the model and bookkeeping (state, journal, status, modes) goes to deterministic code.

## How it realizes the concept

The hub's primitives map almost one-to-one onto the navigator core. Its working unit is `project` as a first-class entity; its loop is `project → deficits → blockers → unblock-step → continuation`. That is the productive-vector cycle stated in engineering terms: the **resource field** (covered knowledge, tools, access) is the reality model; the activity modes plus alternative unblock strategies are the scenario fan; choosing and verifying an unblock-step is selecting the productive vector. The execution contract is explicit — a blocker-handling contract with attempt-counting and strategy-switching on repeated failure — and the governing metric is honest and modest: *better a weak continuation than a stop*. On the ladder this is squarely the agent layer (pipeline + feedback + designed self-learning); it has no domain and no consumer-facing role, by intent.

## What exists today

A working orchestrator launches and resumes agent runtimes with run traces — but that is a local copy of an adjacent lab, not the kernel. The kernel itself exists as specification: definitions, glossary, stage plan, anti-paralysis test scenarios, and an external-memory-service requirements doc. No prototype of the kernel runs yet; no market materials exist.

## Where it could go

*Speculative.* If the spec becomes entities and tests, this layer is the most direct candidate for the assembled core's control loop — the part that decides, fails, and corrects. Fused with an external memory service ([MaaS](../maas/README.md)) for blocker/decision history and a self-learning post-mortem cycle ([essays-claude](../essays-claude/README.md)), it would become the single engine onto which Real AGI's verticals attach as "kernel + domain base."
