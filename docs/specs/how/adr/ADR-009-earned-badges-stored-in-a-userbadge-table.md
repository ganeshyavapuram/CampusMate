---
id: ADR-009
title: Earned badges stored in a UserBadge table
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021, US-036, US-038]
updated: 2026-10-17
---

# ADR-009 — Earned badges stored in a UserBadge table

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The synopsis stores badges as a JSON list in GamificationRecord.badges. That breaks first normal form, which an examiner may question in an RDBMS-category project, and it can't record when a badge was earned.

## Decision

Replace the badges column with a UserBadge table (user_id, badge_code, earned_at) with a unique constraint on (user_id, badge_code); badge definitions stay in code.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — UserBadge table | Low | Low | High | Med |
| B — JSON list column (as in the synopsis) | Low | Low | High | Med |

**A — UserBadge table** (chosen)  
Pros: Normalised; earned dates stored; duplicates blocked by the database.  
Cons: One more table and ER diagram change.

**B — JSON list column (as in the synopsis)**  
Pros: No extra table.  
Cons: Not in first normal form; no earned date; duplicates possible.

## Consequences

**Good**
- The schema is fully normalised for badges.
- The profile can show when each badge was earned.

**Neutral**
- Badge definitions live in code, not the database.

**Bad / accepted limitations**
- The synopsis ER diagram, data dictionary and §4.6 must be updated.

## Rejected alternatives

The JSON column is rejected because it weakens the RDBMS design the project is assessed on.

## Revisit triggers

Reopen if badge definitions need to be edited without a code change.

## How this is enforced

Database unique constraint on (user_id, badge_code); a test awards the same badge twice and checks only one row exists.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
