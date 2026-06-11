# Course Producer — content-production engine that turns an expert's raw material into a deployed course

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/course-producer/README.md`](../../../Ru/3_Verticals/course-producer/README.md)

> **Part of the Real AGI portfolio.** Part of the creator / expert-economy family — the *production* side of turning expertise into courses (its sibling, [course-distributor](../course-distributor/README.md), is the distribution side). **Stage:** working internal tool; multi-stage pipeline running against live and test sites, monetization deferred.

Course Producer takes a raw input — a brief, a bare topic, a 1–3 hour lecture transcript, or a draft — and runs it through staged pipelines that emit a finished course: lessons, quizzes, exercises, a thesaurus, and a landing page, laid into a WordPress (LMS) design template and deployed without manual layout work. The author frames it as "a specialized agent for producing structured content." Its direct user, today, is the author himself: produce a publishable course on a topic in about an hour, without opening the code.

## How it realizes the concept

On the ladder — utility → pipeline → agent → vertical — Producer sits firmly at *agent*, reaching toward vertical. It is a genuine multi-step pipeline (intake → research → structuring → writing → enrichment → review → bundle → two-layer verify/auto-fix → deploy) with a fan of scenarios for different input classes, a feedback loop inside each run, and a self-learning loop that is designed but only partly built. Its domain knowledge — instructional design, a lesson standard, quiz and thesaurus specs — is the *domain* layer of the creator/expert-economy vertical. What it does *not* yet have is the navigator's defining figure: it produces an artifact, it does not *lead* a learner (or even the author-client) toward a goal. The market layer is also undefined. So it is a strong agent and a candidate vertical, not a complete one — honestly, the production half of a vertical whose other half is distribution.

## What exists today

A sizeable, working repo: several pipelines routed by input size, per-section LLM generation, a 28-point review loop, content/deploy verification with auto-fix, a SQLite registry, and live deploys to a production and a test site. Early self-learning steps (capture, classify, localize feedback) run; the later steps (prompt auto-diff, A/B eval, edit acceptance) are designed, still TODO.

## Where it could go

*Hypothesis:* if a leading figure were added — the pipeline guiding an author-client from idea to a working, earning school — and a paying segment defined, Producer becomes a real expert-economy vertical. Its reusable machinery (input-routing, layered quality control, the self-learning loop) is also a plausible donor to the shared core.
