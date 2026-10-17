---
id: ADR-007
title: UUID primary keys
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011, US-043]
updated: 2026-10-17
---

# ADR-007 — UUID primary keys

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The data dictionary (§4.7) uses UUID primary keys without stating why. IDs appear in API URLs such as /api/v1/notes/{id}. Sequential integers would reveal record counts and make other students' IDs easy to guess.

## Decision

Use application-generated version 4 UUIDs as the primary key of every table.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — UUID v4 primary keys | Low | Low | Med | Low |
| B — Auto-increment integers | Low | Low | High | Low |
| C — Integer key plus a separate public UUID | Med | Low | Med | Low |

**A — UUID v4 primary keys** (chosen)  
Pros: IDs reveal nothing and can't be guessed; can be created before insert.  
Cons: Larger keys; hard to read in test data.

**B — Auto-increment integers**  
Pros: Simple and readable; familiar from SQL coursework.  
Cons: Guessable IDs in URLs.

**C — Integer key plus a separate public UUID**  
Pros: Fast joins with unguessable public IDs.  
Cons: Two identifiers per row to keep straight.

## Consequences

**Good**
- Unguessable IDs in every URL.

**Neutral**
- Test fixtures need fixed UUIDs to stay readable.

**Bad / accepted limitations**
- Larger indexes and less readable debugging output.
- UUIDs don't replace ownership checks (ADR-011).

## Rejected alternatives

Auto-increment keys are rejected because they are guessable in URLs. Dual keys add complexity this project doesn't need.

## Revisit triggers

Reopen only if query performance becomes a measurable problem, which is unlikely at this scale.

## How this is enforced

A shared model base class defines the id column; PR review rejects tables that don't use it.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
