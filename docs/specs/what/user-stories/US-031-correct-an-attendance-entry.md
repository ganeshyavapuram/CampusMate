---
id: US-031
title: Correct an attendance entry
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

# US-031 — Correct an attendance entry

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to fix or remove a wrong attendance entry,
so that my percentage stays accurate.

## Why this matters

Logging mistakes are inevitable, and a wrong entry gives a wrong warning. The synopsis has no way to correct one.

## Acceptance criteria

- [ ] Each subject's attendance history lists records newest first.
- [ ] The student can switch a record between present and absent.
- [ ] The student can delete a record.
- [ ] After any change the percentage, counts and warnings are recalculated.

## Out of scope

Edit history.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
