---
id: US-014
title: Mark a session missed and reschedule
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-010, ADR-018, ADR-024]
updated: 2026-10-18
---

# US-014 — Mark a session missed and reschedule

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to mark a session as missed and have my remaining plan rescheduled,
so that one bad day doesn't leave my whole plan out of date.

## Why this matters

Static timetables break the first time a student misses a day, and students then abandon them. Rescheduling automatically keeps the plan realistic.

## Acceptance criteria

- [ ] Marking a session missed sets its status to "missed".
- [ ] The remaining planned sessions dated today or later are replaced by a newly generated plan that meets the rules in US-010.
- [ ] Completed and missed sessions are not changed.
- [ ] The missed session's subject appears at least once in the new plan before its exam date.
- [ ] If rescheduling fails, the session stays marked missed, the previous planned sessions are unchanged, and a "Try again" action is shown.

## Out of scope

Rescheduling without the AI, and moving a single session by hand.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
