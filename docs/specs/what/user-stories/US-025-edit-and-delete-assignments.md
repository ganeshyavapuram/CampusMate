---
id: US-025
title: Edit and delete assignments
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021, ADR-023]
updated: 2026-10-17
---

# US-025 — Edit and delete assignments

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to edit or delete an assignment,
so that my list stays accurate when deadlines change or tasks are cancelled.

## Why this matters

Deadlines get extended and assignments get cancelled. The synopsis mentions CRUD but has no use case for changes, so mistakes would be permanent.

## Acceptance criteria

- [ ] The student can change an assignment's title, subject and due date.
- [ ] Changing the due date to a date before today is rejected; an existing past due date doesn't block editing other fields.
- [ ] The student can delete an assignment after confirming.
- [ ] Deleting a completed assignment doesn't remove XP already earned for it.

## Out of scope

Edit history.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
