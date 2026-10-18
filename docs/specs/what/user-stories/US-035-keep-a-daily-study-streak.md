---
id: US-035
title: Keep a daily study streak
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020, ADR-021]
updated: 2026-10-18
---

# US-035 — Keep a daily study streak

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a streak that counts consecutive days of study activity,
so that I'm motivated not to break the chain.

## Why this matters

Streaks reward consistency, which matters more than intensity for students planning their own time. The synopsis doesn't define what counts as activity.

## Acceptance criteria

- [ ] Completing an assignment or a study session counts as activity for that day in the student's time zone.
- [ ] The first activity on a day after an active previous day increases the streak by 1; more activity on the same day doesn't increase it again.
- [ ] If a whole day passes without activity, the streak shows 0 until the next activity starts a new streak at 1.
- [ ] The current streak appears on the dashboard and profile.

## Out of scope

Streak freezes or repairs, and a longest-streak record.

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: Only completing an assignment or a study session counts towards the streak.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. No. Only completing an assignment or a study session counts as activity.
