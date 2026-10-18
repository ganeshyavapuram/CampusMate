---
id: ADR-022
title: Privacy controls for notes sent to AI models
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, US-017]
updated: 2026-10-18
---

# ADR-022 — Privacy controls for notes sent to AI models

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Uploaded notes go to third-party models through OpenRouter, and some free model providers log or train on prompts. Students aren't told this anywhere in the synopsis.

## Decision

Use OpenRouter's privacy settings to exclude providers that train on or retain prompts where free options allow it, show a notice on the upload screen, and send only note text, never names or emails.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Privacy settings, notice and text-only prompts | Low | Low | Low | High |
| B — Any free model, no notice | Low | Low | High | High |
| C — Local model | High | Low | Low | Med |

**A — Privacy settings, notice and text-only prompts** (chosen)  
Pros: Students are informed; exposure is reduced.  
Cons: Fewer free models may be available.

**B — Any free model, no notice**  
Pros: Widest model choice.  
Cons: Students' notes may be used for training without their knowledge.

**C — Local model**  
Pros: Notes never leave the system.  
Cons: Can't run on free hosting (ADR-005).

## Consequences

**Good**
- Students know where their notes go.

**Neutral**
- The upload screen gains a one-line notice.

**Bad / accepted limitations**
- The free model list may shrink further.

## Rejected alternatives

Using any model without notice is rejected as unfair to students. A local model is rejected because it can't run on free hosting.

## Revisit triggers

Reopen if OpenRouter changes its privacy options, or if the university issues data-handling rules for student projects.

## How this is enforced

Unit test: the prompt builder's output never contains the user's name or email. PR review checks the configured models against OpenRouter's privacy filter.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
