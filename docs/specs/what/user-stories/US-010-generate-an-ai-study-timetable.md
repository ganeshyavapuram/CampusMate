---
id: US-010
title: Generate an AI study timetable
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, ADR-010, ADR-018, ADR-024]
updated: 2026-10-18
---

# US-010 — Generate an AI study timetable

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want an AI-generated study timetable based on my subjects, weak areas, exam dates and daily study hours,
so that I have a realistic revision plan without building one by hand.

## Why this matters

Calendar apps know nothing about exams or weak subjects, so students either plan revision by hand or not at all. Planning is where students with no day-to-day supervision struggle most, and it is the main AI feature of CampusMate.

## Acceptance criteria

- [ ] The planner form is pre-filled with the student's subjects, weak flags, exam dates and saved daily study hours.
- [ ] Generating a plan creates study sessions with status "planned" from today up to the latest exam date.
- [ ] No day's planned sessions add up to more than the student's daily study hours.
- [ ] No session for a subject is scheduled after that subject's exam date.
- [ ] Every subject with a future exam date has at least one session.
- [ ] If the AI response breaks any of these rules or the AI is unavailable, a clear error is shown and no sessions are saved (TC-08).
- [ ] Each weak subject's total planned minutes are at least 1.5 times those of every non-weak subject whose exam date is the same or later.

## Out of scope

Time-of-day scheduling (sessions are dated, not timed), avoiding class times, manual drag-and-drop editing, and syncing to Google Calendar.

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: Weak subjects get at least 1.5 times the minutes of non-weak subjects with the same or a later exam date.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. Use a 1.5× rule: each weak subject gets at least 1.5 times the total minutes of every non-weak subject with the same or a later exam date.
