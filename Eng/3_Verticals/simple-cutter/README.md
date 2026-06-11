# Simple Cutter — automated post-production for recorded talks

> **Up:** [Verticals — the portfolio](../README.md) · **Russian counterpart:** [`Ru/3_Verticals/simple-cutter/README.md`](../../../Ru/3_Verticals/simple-cutter/README.md)

> **Part of the Real AGI portfolio.** A small single-purpose utility in the creator/production toolchain: it turns a raw screen-recording into a clean video plus a usable transcript, unattended. **Stage:** working prototype (deployed as a personal macOS daemon; built for the author's own use, no paying users).

Simple Cutter watches a folder for new recordings and, on its own, does the tedious post-production: trims the leading silence, crops the black bars, extracts audio, transcribes it, and runs the transcript through a text-cleanup step that removes filler and adds structure. The finished artifacts land next to the original; the system posts a notification when it's done. The job it removes is "manually editing and transcribing my own recorded lectures and calls."

## How it realizes the concept

Honestly, this sits low on the ladder. It is a **multi-step pipeline aimed at a clear result** — not an agent and not a vertical. It mixes deterministic steps (silence detection, smart cut, crop) with model calls (transcription, the text-cleanup stage), which is exactly the "pipeline of reliable steps" pattern the core relies on. But it has no scenario fan-out, no feedback on output quality, and no memory between runs: each file produces a one-off artifact, with no figure that leads the user toward a goal. Its natural place in the larger concept is as one *tool-step* — "prepare the transcript of this meeting" — inside a bigger agent, not as a navigator itself.

## What exists today

A working pipeline on macOS: a polling watcher, a frame-accurate smart cut, recorder-specific crop geometry, transcription with chunking for files over the API size limit, and a menu-bar control. It runs as a background daemon with start/stop and logs.

## Where it could go

*Speculative:* it most likely **stays a utility** — and that is a legitimate outcome. The plausible upgrade is not to grow it into an agent but to **fold it into the creator pipeline** as a reusable transcript/video step, with quality feedback (did the cut and cleanup actually land?) accumulating into the shared core rather than living in this tool. As raw material, its value to the corpus is the abstracted pattern, not the tool itself.
