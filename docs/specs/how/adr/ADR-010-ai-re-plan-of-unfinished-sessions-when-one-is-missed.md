---
id: ADR-010
title: AI re-plan of unfinished sessions when one is missed
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, ADR-024, US-014, US-015]
updated: 2026-10-17
---

# ADR-010 — AI re-plan of unfinished sessions when one is missed

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

When a student misses a session, the remaining plan must adjust (synopsis §5.3). A failed re-plan must not leave the student with no plan or half a plan.

## Decision

On "mark missed", ask the AI for a new plan and replace only planned sessions dated today or later, inside one database transaction.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — AI re-plan of unfinished sessions | Med | Med | Low | High |
| B — Rule-based shift to the next free day | Med | Low | Med | High |
| C — No automatic re-plan | Low | Low | High | High |

**A — AI re-plan of unfinished sessions** (chosen)  
Pros: Plan stays realistic and balanced across subjects.  
Cons: Uses an AI request each time; results vary.

**B — Rule-based shift to the next free day**  
Pros: No AI cost; predictable.  
Cons: Can overload days near exams; less balanced.

**C — No automatic re-plan**  
Pros: Nothing to build.  
Cons: Plans go stale after the first missed day.

## Consequences

**Good**
- Plans adapt to missed days.
- History of completed and missed sessions is kept for reports.

**Neutral**
- Each re-plan counts against the daily AI limit (ADR-024).

**Bad / accepted limitations**
- The new plan can differ noticeably from the old one.
- A re-plan takes as long as an AI call.

## Rejected alternatives

No re-plan is rejected because it makes the planner useless after one missed day. The rule-based shift is kept as the fallback if AI quota becomes the bottleneck.

## Revisit triggers

Reopen if re-plans account for more than half of all AI requests in testing, or if students find the reshuffled plans confusing.

## How this is enforced

Integration test: with the AI mocked to fail, marking a session missed leaves all planned sessions unchanged.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
