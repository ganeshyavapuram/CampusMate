---
id: ADR-003
title: Python with FastAPI for the back end
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-001, ADR-017, ADR-018]
updated: 2026-10-17
---

# ADR-003 — Python with FastAPI for the back end

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The back end must expose a REST API, validate every request (synopsis §5.7), verify Firebase tokens, extract text from PDFs and call OpenRouter, often waiting tens of seconds. The synopsis names FastAPI but gives no reason, which an evaluator may ask about.

## Decision

Build the back end in Python 3.11+ with FastAPI, using Pydantic models for all request and response bodies.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — FastAPI | Low | Low | Low | Med |
| B — Django REST Framework | Med | Low | Low | Low |
| C — Flask | Low | Low | Low | Med |

**A — FastAPI** (chosen)  
Pros: Request validation from Pydantic models; async support for slow AI calls; automatic OpenAPI docs for testing.  
Cons: No built-in database layer or admin panel.

**B — Django REST Framework**  
Pros: Built-in ORM, migrations and admin.  
Cons: More concepts to learn; heavier than needed for a JSON API.

**C — Flask**  
Pros: Very small and simple.  
Cons: No built-in validation or async; more glue code.

## Consequences

**Good**
- Invalid requests are rejected with HTTP 422 before any handler runs.
- Interactive API docs at /docs speed up manual testing.

**Neutral**
- Python's PDF libraries (ADR-015) are available directly.

**Bad / accepted limitations**
- The database layer must be chosen separately (ADR-017).
- Async and sync code must not be mixed carelessly, or the server blocks during AI calls.

## Rejected alternatives

Django REST Framework is rejected as heavier than needed. Flask is rejected because it lacks the validation the synopsis's security section relies on.

## Revisit triggers

Reopen if a needed library has no FastAPI-compatible equivalent.

## How this is enforced

PR review checklist: every route declares Pydantic request and response models. Tests assert HTTP 422 for invalid bodies.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
