---
id: US-034
title: Earn XP for study activity
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021]
updated: 2026-10-18
---

# US-034 — Earn XP for study activity

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to earn XP when I complete assignments and study sessions,
so that I feel rewarded for steady work.

## Why this matters

Distance learners lack the routine of daily classes, and light rewards encourage consistent habits (synopsis §2.4). XP is the base of streaks, levels and badges.

## Acceptance criteria

- [ ] Completing an assignment awards 20 XP and completing a study session awards 10 XP.
- [ ] The XP total on the dashboard and profile updates straight after the action.
- [ ] Each assignment or session awards XP at most once, even if reopened and completed again.
- [ ] Reopening a completed item doesn't remove XP.

## Out of scope

Spending XP, and XP for uploading notes or logging attendance.

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: 20 XP per completed assignment, 10 XP per completed study session, none for quizzes.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. Keep 20 XP per assignment and 10 XP per study session, with no XP for quizzes (see US-019).
