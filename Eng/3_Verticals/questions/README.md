# Questions — a structured intake engine that builds a reality model from people

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/questions/README.md`](../../../Ru/3_Verticals/questions/README.md)

> **Part of the Real AGI portfolio.** This is the *intake / diagnostic* step that feeds a navigator's reality model — a conversational questionnaire that converts what people know, do, and fear into structured data. It does not lead anyone yet; it collects the ground truth that leading would require. **Stage:** working product (deployed, tested), single client.

Questions is a survey application built to assess an organization's readiness for AI adoption. Anonymous respondents move through two-stage questionnaires in a one-question-at-a-time, conversational format — a diagnostic stage and an execution stage — with autosave, retry on flaky networks, and session restore. Answers consolidate into a database that an analyst uses to size and design a training program and proposal.

It was built from a concrete need: diagnosing the AI maturity of a corporate client across departments, roles, current adoption, and compliance limits — instead of guessing from interviews and generic forms.

## How it realizes the concept

The navigator's core begins with a *reality model*: an accurate picture of where the user actually stands. Questions is precisely that first step, instantiated for organizations rather than individuals — a systematic mechanism for eliciting current state, deficits, and constraints. On the ladder it sits low and honestly so: a clean **pipeline** (start session → answer with autosave → complete → consolidate → export), not yet an agent. There is no scenario fan, no feedback loop between stages, no self-learning, and no figure that leads. It captures inputs; it does not yet decide or recommend.

## What exists today

A production system: a single-page front end, a serverless backend, versioned questionnaire config, token-based anonymous sessions, autosave with retry, an admin dashboard with CSV export, and unit/integration/e2e tests. Built and deployed for one client.

## Where it could go

*Hypothesis:* the reusable part is the diagnostic engine, not the client-specific content. It could become the intake front-end of a "corporate AI transformation" vertical — where stage-one results shape stage two (a feedback loop), collected diagnostics feed an automated analysis-and-recommendation step, and experience accumulates across clients. That trajectory is the path from collector to navigator; today only the collector exists.
