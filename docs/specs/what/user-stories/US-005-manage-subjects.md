---
id: US-005
title: Manage subjects
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011, ADR-023]
updated: 2026-10-17
---

# US-005 — Manage subjects

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to add, rename and delete my subjects,
so that my assignments, notes, plans and attendance are organised by subject.

## Why this matters

Subject is the root of the data model: assignments, sessions, notes and attendance all belong to one. The synopsis has no way to create or change subjects outside the planner form, so a student who mistypes a subject or drops a course is stuck.

## Acceptance criteria

- [ ] The student can add a subject with a name of 1 to 100 characters.
- [ ] Adding a second subject with the same name (ignoring case) is rejected with a message.
- [ ] The student can rename a subject, and the new name appears everywhere it is used.
- [ ] Deleting a subject shows a confirmation that states how many assignments, notes, study sessions and attendance records will also be removed.
- [ ] After confirming, the subject and all those records are gone, and none of them appear on any screen or report.

## Out of scope

A shared subject catalogue, semesters, and archiving subjects instead of deleting them.

## Evidence it exists today

Not built.

## Open questions

Should subjects be archived at the end of a semester rather than deleted, so old attendance and notes stay available?

## Discussion

_No discussion yet. Add notes below with your name and the date._
