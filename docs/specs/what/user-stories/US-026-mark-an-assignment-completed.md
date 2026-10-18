---
id: US-026
title: Mark an assignment completed
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021]
updated: 2026-10-18
---

# US-026 — Mark an assignment completed

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to mark an assignment as completed,
so that I can see what's left and earn XP.

## Why this matters

Completion drives the pending list, the completion-rate report and XP. Students also need to undo an accidental completion.

## Acceptance criteria

- [ ] Marking an assignment completed sets its status to "completed" and records the completion time.
- [ ] The student is awarded assignment XP once (TC-04).
- [ ] A completed assignment can be reopened to "pending"; completing it again awards no extra XP.
- [ ] Completed assignments leave the pending lists and appear under a "Completed" filter.

## Out of scope

Partial completion or progress percentages.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
