---
id: US-028
title: Flag overdue assignments
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020, ADR-029]
updated: 2026-10-17
---

# US-028 — Flag overdue assignments

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want overdue assignments to be clearly flagged,
so that I know which deadlines I've already missed.

## Why this matters

The synopsis reports list "overdue" assignments, but the status field only allows pending and completed. Missed deadlines need to be visible so the student can contact a tutor or catch up.

## Acceptance criteria

- [ ] A pending assignment whose due date is before today shows an "Overdue" label.
- [ ] The dashboard shows the number of overdue assignments.
- [ ] Completing an overdue assignment removes the label.
- [ ] Overdue is worked out from the due date and today's date; it is never stored as a status.

## Out of scope

Penalties or late-submission tracking.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
