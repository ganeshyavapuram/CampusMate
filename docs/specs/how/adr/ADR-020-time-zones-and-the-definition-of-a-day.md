---
id: ADR-020
title: Time zones and the definition of a day
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-012, ADR-019, US-013, US-035, US-027]
updated: 2026-10-18
---

# ADR-020 — Time zones and the definition of a day

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Streaks, due dates, today's classes, the daily suggestion and attendance all depend on what "today" is. A server in another region running on UTC would break streaks and mark assignments overdue early.

## Decision

Store timestamps in UTC, store each student's IANA time zone on User (detected from the browser), and compute "today" in that time zone.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — UTC storage plus per-user time zone | Med | Low | Low | High |
| B — Server local time | Low | Low | Med | Med |
| C — Client computes all dates | Med | Low | Med | Med |

**A — UTC storage plus per-user time zone** (chosen)  
Pros: Correct days wherever the server runs.  
Cons: Date logic must always use the helper.

**B — Server local time**  
Pros: Simplest.  
Cons: Wrong whenever the server is in another time zone.

**C — Client computes all dates**  
Pros: Uses the browser's time zone directly.  
Cons: Server-side rules like streaks can't be trusted.

## Consequences

**Good**
- Streaks and deadlines are right for every student.

**Neutral**
- User gains a time_zone column.

**Bad / accepted limitations**
- All date code must go through one helper, which is easy to forget.

## Rejected alternatives

Server local time is rejected because the host's region is unknown. Client-only dates are rejected because XP and streaks must be computed on the server.

## Revisit triggers

Reopen if students regularly travel across time zones and complain about streaks.

## How this is enforced

Helper today_for(user) used everywhere; tests freeze time near midnight in two time zones; a CI grep flags date.today() and naive datetime.now() in the backend.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
