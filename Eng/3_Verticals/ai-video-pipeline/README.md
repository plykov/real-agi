# AI Video Pipeline — an "automated film company" that grows a creator's channel

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/ai-video-pipeline/README.md`](../../../Ru/3_Verticals/ai-video-pipeline/README.md)

> **Part of the Real AGI portfolio.** The creator / expert-economy vertical, and the card closest to a real market: a defined creator-economy segment with a subscription model and content already shipped end-to-end. **Stage:** prototype, with real videos published through the full cycle; a live non-technical user testing it.

A creator's scarce input is the original act of creation; everything downstream — transcription, titling, descriptions, tags, captions, publishing, analytics — is leverage that should run itself. The product is, in the author's words, an "automated film company": a human makes the film, and AI agents do the rest, leading the creator from "I made the thing" to "the thing is distributed and growing." It is for the creator economy — channels and expert-led media — sold as a tiered subscription.

## How it realizes the concept

It uses the *reality model* (the channel and its audience as a system to be grown) and *positioning* (what to publish, where it stands). The roadmap states the loop verbatim — **pipeline → feedback → self-learning** — which is why it reads as a textbook instance of the formula. The pipeline is end-to-end and real: folder watcher → upload → audio extraction + transcription → summary and chapters → title/description/tags generation → human approval → publish + captions + verify, with a job tracker holding state idempotently. Code orchestrates; model calls handle the language-shaped steps. Feedback runs today as a human-in-the-loop approve/fix/reject cycle; the automatic closure (analytics steering what gets produced next) and a true scenario fan (A/B of hypotheses) are designed for a later stage, not yet in code. An "AI Producer" mentor chat — personal channel-strategy guidance — is partly built, which is what makes this a vertical and not just a pipeline.

## What exists today

A working prototype: the end-to-end pipeline (v2) with real videos published, a web interface, a tiered chat router with stateful scenarios, and a live user. A documented competitive analysis shows it covering the full task set where rival tools cover a fraction. Self-learning and the scenario fan exist as specification, not yet as code; there is no revenue data — pricing is strategy.

## Where it could go

*Hypothesis:* it is the most market-ready card and the closest to revenue stage. Closing the analytics→production loop and broadening the scenario fan would turn the AI Producer from a partly-built mentor into a full navigator that decides "what and why to publish next," while the pipeline handles "how to produce and distribute." Its reusable orchestration (job tracker, centralized retry, the hypothesis→publish→measure→correct loop) is also a plausible donor to the shared core.
