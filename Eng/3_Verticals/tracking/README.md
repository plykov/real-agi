# Tracking — the navigator turned on itself: ranking where to invest the scarcest resource, time

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/tracking/README.md`](../../../Ru/3_Verticals/tracking/README.md)

> **Part of the Real AGI portfolio.** The concept pointed at the author's own project portfolio — a strategic navigator that ranks bets by where time should go. This very portfolio analysis is the manual version of what tracking automates. **Stage:** working (real API calls, persistent store, used on the author's own portfolio); a personal tool, not yet a market product.

A founder with more ideas than time needs a navigator for the highest-stakes decision of all — *which trajectory to invest the scarcest resource, time, into*. The tool began as a project tracker and utility launcher, but in code it grew into a strategic decision-support system: it takes every project in the workspace, turns raw ideas into pre-project dossiers, runs web market research over them, scores each with an AI analyst on nine strategic criteria, and assembles a ranked leaderboard with a kill/continue verdict and a first-signal deadline. The mentor figure here leads the author through his own portfolio — not "what is this project," but "where should you actually go next, and why."

## How it realizes the concept

It uses all three core organs, applied to the project space itself. *Reality model:* every project as an element with state. *Scenario space:* each raw idea expanded into a dossier with market research. *Positioning:* an AI analyst scores each on weighted strategic criteria and a deterministic code step folds the scores into a composite focus rank with a veto cap on vendor-capture risk — judgment to the model, bookkeeping to the code. The pipeline is full (ideas → dossiers → research → scoring → ranking) and the leading function is explicit in the prompts ("assign a horizon, a first-signal deadline, a kill/continue rule"). What it lacks is the closed consequence loop: bet outcomes are not yet labeled and fed back to recalibrate the criteria weights — those are still set by hand.

## What exists today

A working tool with real model calls (with web search), a persistent store, and a live UI, used on the author's own portfolio. The README still describes only the older tracker-and-launcher layer; the strategic engine lives in the code, built later. Missing for a full vertical: a market beyond the author (it is a personal strategy tool) and self-learning across decisions.

## Where it could go

*Hypothesis:* it is the architecture's self-demonstration. The corpus says the navigator helps a person hold a productive vector across the dimensions of a life; tracking is that navigator pointed at the dimension "which of my bets deserves my time." Add a business wrapper and the consequence loop, and a working personal navigator becomes a vertical — a strategic co-pilot for any solo founder choosing where to bet.
