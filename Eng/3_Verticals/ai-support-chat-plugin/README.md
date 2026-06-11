# AI Support Chat Plugin — a knowledge-bound support assistant that diagnoses rather than guesses

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/ai-support-chat-plugin/README.md`](../../../Ru/3_Verticals/ai-support-chat-plugin/README.md)

> **Part of the Real AGI portfolio.** An early but fully-built agent (pipeline + feedback + self-learning) that applies the "expert that leads, not just answers" pattern to one narrow domain — customer support — on one platform, WordPress. **Stage:** working public release (v2.1.1, GPLv2), no usage/revenue data yet.

A WordPress plugin that adds a support chatbot answering strictly from the site owner's curated knowledge base — no hallucinations, no off-topic drift. Instead of handing a user a single canned reply, it classifies each question, serves a verified answer for simple cases (T1) or walks the user through a multi-turn troubleshooting scenario for complex ones (T2), where each answer determines the next step. When it cannot resolve the issue, it escalates to a human rather than improvising. It ships with an analytics dashboard, a 4-parameter feedback system, and an admin AI helper. It is for small and mid-size site owners — e-commerce, edtech, SMB — who today pay for live operators or SaaS chat tools.

## How it realizes the concept

This is a genuine agent in the ladder's sense, scoped to one vertical. The pipeline is real: context builder → LLM router → tiered answer or branching scenario → escalation. Feedback closes a loop — user replies steer the next step, and ratings plus dialog history flow into analytics. Self-learning exists with a human in the loop: the model analyzes accumulated dialogs and *proposes* new knowledge-base entries, which an admin approves or rejects. The domain (support cases) and market (WordPress SMB) are clearly present. Honestly, though, it stops short of the full Real AGI vertical: guidance is transactional — "solve this one problem" — not long-term steering toward a person's goal, and there is no mentor figure. It corrects its knowledge base, not its decision policy.

## What exists today

A working, security-audited public plugin: T1/T2 routing, 6-layer contextual memory, escalation, feedback, analytics with AI analysis, the proposals self-learning loop, SQLite/Supabase storage, and a multi-domain field (support/admin). A fuller premium edition lives in a separate private repo.

## Where it could go

*Speculative.* The engine — memory, scenarios, feedback, self-learning, storage abstraction — is domain-agnostic; lifted out of the WordPress shell, it could become an early candidate component for the shared core, with the support knowledge base swapped for any vertical's knowledge base.
