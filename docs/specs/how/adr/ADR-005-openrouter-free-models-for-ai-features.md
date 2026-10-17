---
id: ADR-005
title: OpenRouter free models for AI features
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, ADR-022, ADR-024, US-009, US-010, US-017]
updated: 2026-10-17
---

# ADR-005 — OpenRouter free models for AI features

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Summaries, quizzes, timetables and the daily suggestion need a generative AI service at no cost (synopsis §2.7). Free models can be rate-limited, changed or withdrawn without notice. Calling an AI from the browser would expose the API key.

## Decision

Call OpenRouter's free models from the FastAPI back end only, with the API key in a server environment variable and the model names in configuration.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — OpenRouter free models, server-side | Low | Low | Low | High |
| B — A single provider's free tier (for example Google Gemini API) | Low | Low | Low | Med |
| C — Local model with Ollama | Med | Low | Low | Med |

**A — OpenRouter free models, server-side** (chosen)  
Pros: No cost; one API for many models; changing models is a config change.  
Cons: Low daily request limits on free accounts; model availability changes.

**B — A single provider's free tier (for example Google Gemini API)**  
Pros: More stable model; generous free tier.  
Cons: Tied to one vendor's terms; free-tier data may be used for training.

**C — Local model with Ollama**  
Pros: No limits or data sharing.  
Cons: Needs a powerful machine; can't run on free hosting.

## Consequences

**Good**
- Zero AI cost.
- Swapping models needs no code change.

**Neutral**
- All AI calls go through one back-end client module.

**Bad / accepted limitations**
- Daily request limits cap how much students can use AI features.
- Output quality varies between models.
- Student notes leave the system (ADR-022).

## Rejected alternatives

A local model is rejected because it can't run on free hosting. A single-provider free tier is kept as the first fallback if OpenRouter's free limits become unusable.

## Revisit triggers

Reopen if free models are withdrawn more than twice during development, if daily limits fall below what testing needs, or if summary quality fails the Guide's review.

## How this is enforced

CI step fails if "openrouter" appears under frontend/. A settings test checks that the API key and model names are read from the environment.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
