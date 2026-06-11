# essays-claude — a self-learning agent organization: the core's "learn from consequences" loop, running

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/essays-claude/README.md`](../../../Ru/3_Verticals/essays-claude/README.md)

> **Part of the Real AGI portfolio.** A core-engine layer: the place where the decision → result → correction loop is not just designed but *running* on real benchmarked runs. This is the portfolio's most concrete realization of the core's self-learning organ. **Stage:** prototype (40+ recorded runs across two runtimes; the product-facing contour designed, not yet delivered to live users).

essays-claude is an experimental ground where an autonomous multi-agent "organization" is built: an observer (a CEO-style agent) drives two independent runtime sandboxes through a canonical series of benchmark tasks and accumulates the lessons in a shared core. Its goal is a production-ready agent organization that takes a real task and carries it to a result without a human. Two multi-step loops run: an experimental loop (golden task → launch brief → autonomous run → status/scorecard → carry lessons into core) and a designed product loop (project request → intent normalization → product brief → engineering spec → task graph → execution).

## How it realizes the concept

Almost the entire project *is* universal machinery — that is its content: a pipeline engine (execution plane, orchestrator, continuous loop), a memory/state layer, scenarios and control tasks (golden tasks), feedback (scorecards, findings), and self-learning (methodology plus real learning traces). The domain it is scoped to — autonomous software development — is deliberately just a test arena; the mechanisms (leading through directives, evaluating the consequences of decisions, correcting) carry to any vertical. The decision → result → correction loop is present and concrete: a directive launches a run, a scorecard evaluates it, lessons edit the core and the contracts, the next wave tests the fix. The documented domain obstacles are the honest ones of autonomy — runtimes stalling between runs, infinite redispatch loops, hanging without progress, the absence of an honest terminal failure, stopping at the first friction instead of routing around it.

## What exists today

A working prototype: dozens of real runs across two runtimes, a passed benchmark suite, and the autonomy infrastructure (continuous loop, heartbeat, observer↔runtime protocol, retry budgets, honest failure states). What is not done: the product-facing contour that would lead a non-developer human from intent to a delivered app is designed but not yet running on live users; and the business layer (who pays, price, go-to-market) is absent by intent — this is a core experiment, not a vertical.

## Where it could go

*Hypothesis:* essays-claude is one of the three scattered pieces of the core — self-learning — proven on 40+ real runs. Fused with long-term memory ([MaaS](../maas/README.md)) and the scenario/anti-paralysis loop ([autonomy-hub](../autonomy-hub/README.md)) into a single engine, it supplies the part the corpus calls the hardest: a system that evaluates the consequences of its own decisions and changes itself. Carried to live users, its product contour would also spin off a class-A vertical of its own — an autonomous dev-organization for non-developers.
