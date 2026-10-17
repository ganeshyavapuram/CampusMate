---
id: US-011
title: Save daily study hours
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020]
updated: 2026-10-17
---

# US-011 — Save daily study hours

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want my daily study hours to be saved,
so that I don't re-enter them every time I generate or adjust a plan.

## Why this matters

The planner needs available hours, but the synopsis schema has no column for them, so they would be lost after each generation. Re-entering them each time is tedious and invites inconsistent plans.

## Acceptance criteria

- [ ] The student can set daily study hours between 0.5 and 12, in steps of 0.5.
- [ ] Values outside that range are rejected with a message.
- [ ] The saved value pre-fills the planner form on later visits, including after signing out and back in.
- [ ] Changing the value does not alter the existing plan until the student regenerates it (US-015).

## Out of scope

Different hours for different weekdays.

## Evidence it exists today

Not built.

## Open questions

Do students need different hours on weekends and weekdays?

## Discussion

_No discussion yet. Add notes below with your name and the date._
