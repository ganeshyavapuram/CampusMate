---
id: US-033
title: Get attendance warnings before it's too late
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-013, ADR-020]
updated: 2026-10-17
---

# US-033 — Get attendance warnings before it's too late

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a warning when my attendance is below 75% or when one more absence would take it there,
so that I can act while there's still time.

## Why this matters

Warning before a shortfall happens is what separates CampusMate from manual counting. The synopsis rule and its test cases currently disagree (see Open questions).

## Acceptance criteria

- [ ] A subject below 75% shows a "Below 75%" warning on the dashboard and attendance screen.
- [ ] A subject at or above 75% where one more absence would drop it below shows an "At risk" warning; for example, 18 of 24 is at risk because 18 of 25 is 72%.
- [ ] The two warnings look different and each has a text label.
- [ ] Once a class timetable exists (US-007), an at-risk subject shows the date of its next class.

## Out of scope

Warnings outside the app.

## Evidence it exists today

Not built.

## Open questions

The synopsis says to warn when the next absence would drop below 75%, but TC-05 expects no warning at 18 of 24. Should TC-05 be updated to expect an "At risk" warning?

## Discussion

_No discussion yet. Add notes below with your name and the date._
