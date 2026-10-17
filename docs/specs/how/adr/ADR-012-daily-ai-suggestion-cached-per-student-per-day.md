---
id: ADR-012
title: Daily AI suggestion cached per student per day
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, ADR-020, US-009]
updated: 2026-10-17
---

# ADR-012 — Daily AI suggestion cached per student per day

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The dashboard shows a one-line AI suggestion (§5.1). Generating it on every page load would quickly exhaust the free request limit (§11.3). The synopsis has nowhere to store it.

## Decision

Store the suggestion in a DailySuggestion table with a unique (user_id, date) constraint; generate it on the first dashboard load of the student's day and reuse it after that.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — DailySuggestion table | Low | Low | High | High |
| B — In-memory cache | Low | Low | Med | High |
| C — Generate on every load | Low | High | High | High |

**A — DailySuggestion table** (chosen)  
Pros: At most one AI call per student per day; survives restarts.  
Cons: One more table.

**B — In-memory cache**  
Pros: No schema change.  
Cons: Lost on every restart, so free hosts that sleep would regenerate often.

**C — Generate on every load**  
Pros: Always fresh.  
Cons: Uses up the free AI quota.

## Consequences

**Good**
- Predictable AI usage for this feature.

**Neutral**
- A fixed fallback message is shown when generation fails.

**Bad / accepted limitations**
- The suggestion can't react to changes made later in the same day.
- The ER diagram needs a new table.

## Rejected alternatives

Per-load generation is rejected for quota reasons. An in-memory cache is rejected because free hosts restart often.

## Revisit triggers

Reopen if students want a fresh suggestion after completing work during the day.

## How this is enforced

Test: two dashboard loads on the same day trigger exactly one call to the mocked AI client.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
