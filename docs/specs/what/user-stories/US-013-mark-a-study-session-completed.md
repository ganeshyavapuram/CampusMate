---
id: US-013
title: Mark a study session completed
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021, ADR-020]
updated: 2026-10-18
---

# US-013 — Mark a study session completed

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to mark a study session as completed,
so that my progress is tracked and I earn XP for studying.

## Why this matters

Gamification awards XP when a session is finished, and the productivity report counts study hours, but the synopsis has no way to record completion. Without it the planner has no feedback and rewards never trigger.

## Acceptance criteria

- [ ] A planned session dated today or earlier can be marked completed; a future-dated session cannot.
- [ ] The session's status changes to "completed" on the timetable and in the weekly report.
- [ ] The student is awarded session XP once; marking it again or reopening and re-completing it awards nothing more.
- [ ] Completing a session counts as activity for today's streak.
- [ ] A planned session dated before today shows a "Not marked" label, and the dashboard lists it with buttons to mark it completed or missed.

## Out of scope

A study timer, and recording actual minutes studied when they differ from the planned duration.

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: Past planned sessions aren't changed automatically; they show "Not marked" and the dashboard prompts the student.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. Don't change the status automatically. A planned session from a past date shows "Not marked", and the dashboard asks the student to mark it completed or missed.
