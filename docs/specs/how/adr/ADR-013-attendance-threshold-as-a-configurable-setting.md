---
id: ADR-013
title: Attendance threshold as a configurable setting
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [US-030, US-032, US-033]
updated: 2026-10-17
---

# ADR-013 — Attendance threshold as a configurable setting

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Warnings use a 75% threshold (§5.3), but institutions differ. Floating-point maths on the formulas can give off-by-one results near the boundary.

## Decision

Read the threshold from server configuration (default 75%) and compute attendance counts with integer arithmetic.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Configurable setting, integer arithmetic | Low | Low | High | High |
| B — Per-subject threshold column | Med | Low | High | Med |
| C — Hard-coded 0.75 in the code | Low | Low | High | Med |

**A — Configurable setting, integer arithmetic** (chosen)  
Pros: One place to change; exact results.  
Cons: Same threshold for every subject.

**B — Per-subject threshold column**  
Pros: Flexible.  
Cons: Extra input for every subject with little demand.

**C — Hard-coded 0.75 in the code**  
Pros: Simplest.  
Cons: Literal repeated in several places; float rounding errors.

## Consequences

**Good**
- Exact, testable attendance figures.

**Neutral**
- The formulas are written as integer expressions (for example floor((4A − 3T) / 3)).

**Bad / accepted limitations**
- Students at institutions with other thresholds can't set their own.

## Rejected alternatives

Per-subject thresholds are rejected as unneeded for the first version. Hard-coding is rejected for maintainability and rounding errors.

## Revisit triggers

Reopen if students from institutions with other thresholds use the app.

## How this is enforced

Unit tests cover TC-05, TC-06 and boundary cases (0 classes, exactly 75%, one class below). CI grep fails on the literal 0.75 outside the settings module.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
