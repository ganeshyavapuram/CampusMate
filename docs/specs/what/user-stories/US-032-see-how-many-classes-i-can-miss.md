---
id: US-032
title: See how many classes I can miss
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-013]
updated: 2026-10-17
---

# US-032 — See how many classes I can miss

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to see how many more classes I can miss, or must attend, to stay at the required attendance,
so that I can plan absences safely.

## Why this matters

A percentage alone doesn't tell a student what to do next. Converting it into a count of classes is what makes attendance tracking useful.

## Acceptance criteria

- [ ] At or above 75%, the subject shows "You can miss N more classes", where N = floor((4A − 3T) / 3) for A attended out of T held.
- [ ] Below 75%, the subject shows "Attend the next N classes", where N = 3T − 4A.
- [ ] Examples: 20 of 24 shows "miss 2", 18 of 24 shows "miss 0", and 17 of 24 shows "attend 4".
- [ ] A subject with no records shows "No classes logged yet".

## Out of scope

Per-subject thresholds other than the configured one.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
