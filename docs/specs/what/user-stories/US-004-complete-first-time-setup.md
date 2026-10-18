---
id: US-004
title: Complete first-time setup
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020]
updated: 2026-10-18
---

# US-004 — Complete first-time setup

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a short setup on my first visit that asks for my subjects and daily study hours,
so that the app is useful on day one instead of showing empty screens.

## Why this matters

Every CampusMate feature hangs off a subject, so a new student who lands on an empty dashboard has nothing to act on and may leave. A guided setup gets the minimum data in place in under two minutes.

## Acceptance criteria

- [ ] A signed-in student with zero subjects is shown the setup screen instead of the dashboard.
- [ ] Setup collects at least one subject name, an optional exam date and weak-subject flag per subject, and daily study hours.
- [ ] The student's time zone is detected from the browser and saved without asking.
- [ ] The "Finish" button stays disabled until at least one subject has a name.
- [ ] After finishing, the dashboard lists the subjects entered, and setup is not shown again while the student has at least one subject.

## Out of scope

Entering the class timetable during setup (done later in US-007), and importing subjects from a university portal.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
