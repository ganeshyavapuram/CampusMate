---
id: ADR-018
title: AI request handling with timeout, validation and fallback
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, ADR-008, ADR-010, ADR-024, US-016]
updated: 2026-10-17
---

# ADR-018 — AI request handling with timeout, validation and fallback

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Free AI models are slow, rate-limited and sometimes return malformed JSON. TC-08 requires a friendly error with no partial data saved. Without a common approach, each module would handle failures differently.

## Decision

Call the AI synchronously with a 60-second timeout and one retry, try configured fallback models in order, validate responses with Pydantic, and save results only inside a transaction after validation succeeds.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Synchronous call with timeout, retry, fallback and validation | Med | Low | Low | High |
| B — Background job queue (Celery or RQ with Redis) | High | Med | Low | Med |
| C — Synchronous call with no safeguards | Low | Low | Med | High |

**A — Synchronous call with timeout, retry, fallback and validation** (chosen)  
Pros: Simple flow; consistent errors; no partial saves.  
Cons: The student waits on a spinner during the call.

**B — Background job queue (Celery or RQ with Redis)**  
Pros: Requests return immediately; long jobs don't block.  
Cons: Needs Redis and a worker process, which free hosting doesn't provide well.

**C — Synchronous call with no safeguards**  
Pros: Least code.  
Cons: Hangs and half-saved data on failure.

## Consequences

**Good**
- Every AI feature fails the same, predictable way.
- No half-saved plans or quizzes.

**Neutral**
- One shared AI client module wraps all calls.

**Bad / accepted limitations**
- Requests can take up to about two minutes in the worst case (timeout plus retry).
- Fallback models may give lower-quality output.

## Rejected alternatives

A job queue is rejected because it needs infrastructure free hosts don't offer. No safeguards is rejected because it fails TC-08.

## Revisit triggers

Reopen if typical AI latency exceeds 30 seconds, or if the host starts cutting off long requests.

## How this is enforced

Tests with a mocked AI client: timeout, HTTP 429 and malformed JSON each return the expected error and write no rows.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
