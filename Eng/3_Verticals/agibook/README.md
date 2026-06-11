# AGIbook — a book stated through, and as, a self-improving writing pipeline

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/agibook/README.md`](../../../Ru/3_Verticals/agibook/README.md)

> **Part of the Real AGI portfolio.** Two things at once: it is the manuscript that articulates the concept (a philosophical essay-manifesto on intelligence, insight, and ontology), and it is the production machine that writes that manuscript — a reusable pipeline that turns a human's "lab dialogues with an AI" into a publishable book. **Stage:** working — eight chapters drafted, a first PDF assembled, a tested extractor, and a live essay line; the pipeline-as-product is real in mechanism but not yet sold.

In product terms, AGIbook is a disciplined assembly line for long-form authored text. Phase 0 collects raw dialogue and notes; Phase 1 derives a canon (voice, arc, terms, conventions); Phase 2 runs a per-chapter loop — writer drafts, editor flags, author reviews, a maintainer folds lessons back into the canon and into the agents' own prompts; later phases check arc consistency and assemble the volume. It is for an author-expert who wants their accumulated AI conversations to become a book without surrendering their voice to a ghostwriter.

## How it realizes the concept

It maps cleanly to **core + domain + market**, and reaches the *agent* rung of the ladder. The **domain** — producing long authored text with an AI — is codified as named obstacles: context decay, voice and term drift, invented citations, academic stiffness, the tell-tale "AI-ness" that blocks reading. The **feedback core** is the load-bearing part: each chapter's review becomes `learnings/`, which a maintainer turns into edits of the bible and of the agents' prompts, git-traced so you can see which rule appeared after which chapter. That decision → result → correction loop, running on live material, is exactly the figure the Real AGI core formalizes — making this pipeline a donor candidate for the core's self-learning mechanics. It stops short of a *vertical*: the end consumer is currently the author himself, not an external human led toward a life goal, and the writing runs one disciplined path rather than a fan of scenarios. The book's reader, separately, gets a static artifact, not guidance.

## What exists today

A reusable `framework/` layer cleanly separated from book-specific content; an extractor (a tested Python package, `parse → cluster → consolidate → bridges`); a chapter-bundle builder; writer/editor/consistency-checker/maintainer agents with versioned prompts; a working `learnings/` loop with quality metrics; chapters 1–8, a 63-page v1 PDF, and a 17-topic essay line. The pipeline has already iterated on itself: writer v5→v6, pipeline v1→v2.

## Where it could go

*Hypothesis:* the universal layer detaches from this one book and becomes a product for other authors — same machine, different voice, theme, and corpus. That would require what is currently missing: a worked market (segment, pricing, the paid alternative it displaces — ghostwriting and editorial services), and a shift of the end consumer from the author to an external client the pipeline guides. Speculatively, adding a scenario fan and a mentor figure that assesses an author's situation and recommends a path would push it from agent toward a full vertical.
