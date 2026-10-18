---
id: ADR-025
title: REST API conventions
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-003, ADR-011, US-023]
updated: 2026-10-18
---

# ADR-025 — REST API conventions

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Angular and FastAPI are written by the same team, but inconsistent paths and errors make client code and tests harder and look messy in the report.

## Decision

Prefix all routes with /api/v1, use plural resource names and standard HTTP methods, and return errors in FastAPI's {"detail": ...} format with fixed status codes.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Versioned REST with FastAPI's error format | Low | Low | Med | Med |
| B — GraphQL | High | Low | Low | Low |
| C — Ad hoc unversioned routes | Low | Low | Med | High |

**A — Versioned REST with FastAPI's error format** (chosen)  
Pros: Predictable for client and tests; matches FastAPI defaults.  
Cons: Some upfront discipline.

**B — GraphQL**  
Pros: Flexible queries.  
Cons: Another technology to learn.

**C — Ad hoc unversioned routes**  
Pros: No rules to follow.  
Cons: Inconsistent paths and errors.

## Consequences

**Good**
- Client error handling is uniform.

**Neutral**
- Status codes: 400/422 validation, 401 auth, 404 missing or not owned, 429 AI limit, 503 AI unavailable.

**Bad / accepted limitations**
- Changing the conventions later means changing every route.

## Rejected alternatives

GraphQL is rejected as unnecessary for this app. Ad hoc routes are rejected for inconsistency.

## Revisit triggers

Reopen if a second client (for example a mobile app) needs different data shapes.

## How this is enforced

Test asserts every route in the OpenAPI schema starts with /api/v1.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
