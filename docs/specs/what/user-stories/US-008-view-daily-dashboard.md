---
id: US-008
title: View daily dashboard
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011, ADR-012]
updated: 2026-10-18
---

# US-008 — View daily dashboard

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want one dashboard that shows today's classes, pending assignments, upcoming exams, attendance and my progress,
so that I can see what needs my attention without opening several apps.

## Why this matters

The core problem in the synopsis is fragmentation: deadlines in chat groups, timetables in calendar apps, attendance counted by hand. A single summary screen is the main reason a student would open CampusMate daily.

## Acceptance criteria

- [ ] The dashboard shows five sections: today's classes, pending assignments sorted by due date, upcoming exams, attendance percentage per subject, and XP with current streak.
- [ ] Pending assignments due today or tomorrow are visually highlighted (US-027).
- [ ] Subjects below or at risk of falling below the attendance threshold show a warning label (US-033).
- [ ] A section with no data shows a short explanation and a link to the screen where that data is added.
- [ ] The dashboard shows only the signed-in student's data.

## Out of scope

Customising, reordering or hiding dashboard sections.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
