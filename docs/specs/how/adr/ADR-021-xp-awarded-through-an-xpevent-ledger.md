---
id: ADR-021
title: XP awarded through an XpEvent ledger
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-009, US-034, US-026, US-013]
updated: 2026-10-18
---

# ADR-021 — XP awarded through an XpEvent ledger

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

XP is awarded when an assignment or session is completed (§5.3). A student who completes, reopens and completes an item again would earn XP twice. The synopsis also doesn't define what counts as streak activity.

## Decision

Record each award in an XpEvent table with a unique constraint on (user_id, source_type, source_id), and update xp_total only when a new row is inserted.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — XpEvent ledger with unique constraint | Med | Low | High | Med |
| B — xp_awarded flag on each assignment and session | Low | Low | High | Med |
| C — No protection | Low | Low | High | High |

**A — XpEvent ledger with unique constraint** (chosen)  
Pros: Exactly-once awards enforced by the database; audit trail.  
Cons: One more table.

**B — xp_awarded flag on each assignment and session**  
Pros: No new table.  
Cons: A flag per source table; no history.

**C — No protection**  
Pros: Nothing to build.  
Cons: XP can be farmed by toggling completion.

## Consequences

**Good**
- XP can't be awarded twice for the same item.
- Activity history supports streak calculation.

**Neutral**
- xp_total is a cached sum of XpEvent points.

**Bad / accepted limitations**
- Another table for the ER diagram and data dictionary.

## Rejected alternatives

Per-table flags are rejected because each new XP source would need its own flag. No protection is rejected because XP would be meaningless.

## Revisit triggers

Reopen if XP sources multiply enough that a general rules engine is needed.

## How this is enforced

Test: complete, reopen and complete an assignment; exactly one XpEvent row exists and xp_total rose once.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
