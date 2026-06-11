# Expert Constructor Core — a constructor for grounded domain expert AI-chats

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/expert-constructor-core/README.md`](../../../Ru/3_Verticals/expert-constructor-core/README.md)

> **Part of the Real AGI portfolio.** This is a core-engine layer: a configurable platform that turns a body of documents into a grounded expert chat, with the domain plugged in by configuration rather than rebuilt each time — the infrastructure that verticals are assembled from. **Stage:** working prototype (runnable answer slice; self-learning designed but not yet in code).

Expert Constructor Core is a reusable expert-chat constructor. A knowledge owner feeds in documents; the system prepares them into promoted knowledge packages, retrieves the relevant context per question, and composes an answer grounded in those sources through a universal chat interface. The job it does is narrow and honest: take a corpus and a question, return an answer anchored in the corpus. It is built as five modules behind explicit contracts — Chat UI, Knowledge Base Setup, Retrieval Context Builder, Answer Core Runtime, and a Synthetic Traffic Console — so that any one of them can be replaced without touching the others.

## How it realizes the concept

It implements the *expert-assembly* and *retrieval/grounding* layers of the core, deliberately leaving the domain empty. A "vertical" here is meant to be **universal core + swappable knowledge package + profile**, which maps directly onto the corpus formula of core + domain + market. On the ladder it reaches a real **pipeline** (documents → knowledge package → retrieval pack → grounded answer) with the *first half* of an agent's feedback loop in place: every answer must emit a feedback event, and an eval benchmark exists. It stops short of a full agent — the loop's closure (behavior correction from accumulated experience) is designed but not yet implemented. Critically, it is an *expert that answers*, not a *mentor that leads*: mentor flows are explicitly excluded from the product boundary.

## What exists today

A runnable Answer Chat UI wired to the Answer Core Runtime; deterministic retrieval pack generation with cache/topic/staleness tests and an eval benchmark; Knowledge Base Setup able to publish a local package and access descriptor; versioned prompts and a project-level architecture guard. Self-learning, the live cross-module service seam, and the Synthetic Traffic Console runtime are specified but not built. No market segment or payer is fixed in the materials.

## Where it could go

*Hypothesis:* if the designed learning subsystem were closed (consequence → evaluation → rule update) and the answering profile swapped for a leading one — goal model, scenario fan, a guiding figure — this engine becomes the substrate on which Real AGI verticals are instantiated: one core, many domains, each entering as a knowledge package and profile.
