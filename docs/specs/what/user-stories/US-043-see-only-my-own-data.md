---
id: US-043
title: See only my own data
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011, ADR-007]
updated: 2026-10-17
---

# US-043 — See only my own data

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to be certain that no other student can see or change my data,
so that my notes and records stay private.

## Why this matters

Notes, attendance and plans are personal. A single missing ownership check would expose one student's data to another.

## Acceptance criteria

- [ ] For every API resource, requesting another student's record by its id returns HTTP 404 (automated test with two users).
- [ ] Every list endpoint returns only the signed-in student's records.
- [ ] No endpoint accepts a user id from the client; the user always comes from the verified token.

## Out of scope

Sharing data with other students or tutors.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
