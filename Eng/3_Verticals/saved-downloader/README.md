# Saved Downloader — turning your saved posts into a personal domain expert that leads you to a plan

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/saved-downloader/README.md`](../../../Ru/3_Verticals/saved-downloader/README.md)

> **Part of the Real AGI portfolio.** The "personal expert from your own data" vertical — and the portfolio's clearest demonstration of "one architecture, many products" inside a single codebase. **Stage:** prototype, with a real user planning a real trip on it; the full journey partly built.

You have already curated an expertise — the hundreds of posts you saved on a topic. That latent corpus should become an expert that speaks "in your slice of the subject," and then *lead you* from a vague wish to a concrete plan. The product downloads your saved content, transcribes video, OCRs images, and assembles a topic database an LLM answers from as a narrow specialist; on top of that runs a product journey from eliciting wishes to a scenario compiler to a personal guide exported to a map. The first concrete vertical is travel planning, sold as a subscription — but the same engine could become any saved-domain navigator.

## How it realizes the concept

It uses *memory* (your saved corpus as the trajectory store) and *scenario space* (the route compiler). The pipeline is full and many-staged — download → transcribe → OCR → assemble a topic base → narrow-specialist answers → a journey from wishes to a scenario compiler to a guide — with code and model interleaved on the "judgment to the model, bookkeeping to the code" principle, contracts between steps, and a clean "source vs. derivative" split that lets the whole conveyor be rebuilt. All five agency signals are present: scenario fan, feedback, designed self-learning, a working prototype, and a mentor figure (the topic-expert chat that answers with links to the underlying posts). The one honest caveat: self-learning here means accumulation of corpus and taste profile, not yet a formal loop that labels the consequences of the system's own decisions.

## What exists today

A working prototype (v0.2.0 end-to-end) with a UI panel and a real topic database (a ~200-post base) that a live user actually used to plan a trip. The scenario compiler is partly implemented; the journey's first step (chat elicitation + cold deep-research) and last step (guide + map export) are designed but not yet built — so the full journey is less mature than the base pipeline.

## Where it could go

*Hypothesis:* the author frames travel as the *first* vertical of a general engine — "the architecture is one, the products differ" — which is exactly the corpus's thesis stated from inside a working prototype. Proven beyond travel (and with the consequence loop made formal), the same "expert from your data" core could be instantiated as a navigator for anything a person has curated.
