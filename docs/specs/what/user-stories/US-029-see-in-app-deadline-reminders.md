---
id: US-029
title: See in-app deadline reminders
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-019]
updated: 2026-10-17
---

# US-029 — See in-app deadline reminders

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want reminders inside the app for assignments that are due soon or overdue,
so that I'm reminded every time I open CampusMate.

## Why this matters

The synopsis promises deadline reminders but never says how they reach the student. In-app reminders need no extra infrastructure.

## Acceptance criteria

- [ ] A notification indicator in the header shows the number of pending assignments that are due soon or overdue.
- [ ] Opening it lists those assignments, each linking to its detail.
- [ ] The count updates as soon as an assignment is completed.
- [ ] No emails or push notifications are sent.

## Out of scope

Email, SMS and push notifications.

## Evidence it exists today

Not built.

## Open questions

Is in-app reminding enough for the guide, or are email reminders expected?

## Discussion

_No discussion yet. Add notes below with your name and the date._
