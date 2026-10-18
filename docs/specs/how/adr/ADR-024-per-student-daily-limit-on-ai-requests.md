---
id: ADR-024
title: Per-student daily limit on AI requests
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, ADR-018, US-016]
updated: 2026-10-18
---

# ADR-024 — Per-student daily limit on AI requests

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The free OpenRouter quota is shared by all students. One student repeatedly regenerating quizzes could use it up for everyone.

## Decision

Count each student's AI requests per day in the database and refuse further requests above a configured limit (default 20) with HTTP 429 and a reset time.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Daily counter per student in the database | Low | Low | High | High |
| B — Per-minute rate limiting in memory (slowapi) | Low | Low | Low | High |
| C — No limit | Low | Low | High | High |

**A — Daily counter per student in the database** (chosen)  
Pros: Fair share; survives restarts.  
Cons: Heavy users may hit the limit.

**B — Per-minute rate limiting in memory (slowapi)**  
Pros: Stops bursts.  
Cons: Doesn't cap daily usage; resets on restart.

**C — No limit**  
Pros: Nothing to build.  
Cons: One student can exhaust the shared quota.

## Consequences

**Good**
- The shared quota is protected.

**Neutral**
- The limit is a config setting.

**Bad / accepted limitations**
- Students preparing for exams may hit the limit.

## Rejected alternatives

No limit is rejected for fairness. In-memory limiting is rejected because it doesn't cap daily usage.

## Revisit triggers

Reopen if paid credits raise the quota, or if more than 10% of active students hit the limit in a week.

## How this is enforced

Test: the 21st AI request in one day returns HTTP 429 with the reset time.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
