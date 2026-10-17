---
id: ADR-011
title: Per-user data isolation in a shared dependency
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-004, ADR-007, US-043]
updated: 2026-10-17
---

# ADR-011 — Per-user data isolation in a shared dependency

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Students must see only their own data (synopsis §5.7), but the synopsis doesn't say how. If each route filters by hand, one forgotten filter exposes another student's notes or attendance.

## Decision

A single FastAPI dependency returns the verified current user, and all data access goes through functions that filter by that user via Subject.user_id; other users' records return HTTP 404.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Central dependency plus ownership-filtered data functions | Med | Low | Low | Med |
| B — PostgreSQL row-level security | High | Low | Low | Med |
| C — Manual checks in each route | Low | Low | Med | High |

**A — Central dependency plus ownership-filtered data functions** (chosen)  
Pros: One place to review; easy to test.  
Cons: Every query on child tables joins to Subject.

**B — PostgreSQL row-level security**  
Pros: Enforced by the database itself.  
Cons: Not available on SQLite; hard to learn.

**C — Manual checks in each route**  
Pros: Simple to start.  
Cons: Easy to forget one check.

## Consequences

**Good**
- Isolation can be tested in one suite.
- HTTP 404 doesn't reveal that another student's record exists.

**Neutral**
- Routes never receive a user id from the client.

**Bad / accepted limitations**
- Extra joins on every child-table query.

## Rejected alternatives

Row-level security is rejected because it doesn't work on SQLite (ADR-006). Manual per-route checks are rejected as error-prone.

## Revisit triggers

Reopen if sharing between students (for example study groups) is added.

## How this is enforced

Automated two-user test for every resource endpoint: user B requesting user A's record gets HTTP 404.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
