# MaaS — Memory as a Service: the core's long-term memory, built as standalone infrastructure

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/maas/README.md`](../../../Ru/3_Verticals/maas/README.md)

> **Part of the Real AGI portfolio.** A core-engine layer: the long-term semantic memory the navigator needs, built as a reusable service rather than as part of any one vertical. Two of the three terms of *agent = pipeline + feedback + self-learning* — memory and self-learning — live here. **Stage:** prototype (MVP working end-to-end; the self-learning subsystem largely designed, not yet built).

MaaS is an event-driven long-term memory system for LLMs: it remembers the context of past dialogues and folds it into new answers, solving the "every conversation starts from a blank slate" problem. A query runs through an explicit state machine — analyze whether memory is needed and extract semantic keys, assemble relevant memories into context, generate the answer, log the dialogue — while a background archivist periodically compresses raw logs into tagged, summarized memory records. Its direct consumer is code (a REST API for developers building AI assistants); a human appears only as the eventual end of the chat.

## How it realizes the concept

This is almost entirely universal machinery — which is exactly why it is core, not a vertical: it has no domain (memory works over any dialogue) and it does not lead a human to a goal. What it contributes to the core is foundational: the four-layer trajectory memory the corpus's first essay describes, an event-driven pipeline engine with hot-swappable prompts, and a designed self-learning contour (sensor → analyst → teacher → tuner) with metrics, golden datasets, and experiments. The conceptual materials position MaaS explicitly as the memory subsystem of an "AI expert/mentor" — a designed fragment of the super-mentor architecture. On the ladder, the runtime is a working single pipeline; the feedback/self-learning loop is specified but its agents are still empty folders.

## What exists today

A working MVP: the end-to-end query pipeline, a user emulator, and an analyzer, on a Node/TypeScript + Postgres + LLM stack. A three-tier business model is described (SaaS memory, self-hosted license, an extended self-learning package). What is not built: the self-learning roles (analyst, teacher, tuner, manager) exist as documentation and empty scaffolding; there is no live user or revenue data; and a known weak spot — the model not always using retrieved memories — is flagged but unresolved.

## Where it could go

*Hypothesis:* MaaS is one of the three scattered pieces of the core — memory — that the portfolio finds built but never yet assembled. Fused with the scenario/anti-paralysis loop ([autonomy-hub](../autonomy-hub/README.md)) and the self-learning loop ([essays-claude](../essays-claude/README.md)) into one engine — one memory feeding one scenario engine that learns from its own logged consequences — it becomes part of "the project where the core itself is realized." On paper that assembly is the center of the corpus; in the portfolio it is the one thing not yet built.
