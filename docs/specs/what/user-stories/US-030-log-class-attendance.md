---
id: US-030
title: Log class attendance
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-013]
updated: 2026-10-18
---

# US-030 — Log class attendance

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to record whether I attended each class,
so that I always know my attendance percentage.

## Why this matters

Students count attendance by hand and notice shortfalls too late (synopsis §2.3). Logging each class is the input for all attendance warnings.

## Acceptance criteria

- [ ] The student can record present or absent for a subject on a date, defaulting to today.
- [ ] A future date is rejected.
- [ ] Only one record is allowed per subject per date; logging the same date again offers to edit the existing record.
- [ ] The subject's percentage updates immediately, shown to one decimal place: 18 of 24 shows 75.0% (TC-05), and 17 of 24 shows 70.8% (TC-06).

## Out of scope

Syncing with university attendance systems, and partial or late attendance.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
