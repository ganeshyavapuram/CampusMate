---
id: US-009
title: Get a daily AI study suggestion
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-012, ADR-018, ADR-020]
updated: 2026-10-18
---

# US-009 — Get a daily AI study suggestion

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want one short AI study suggestion on my dashboard each day,
so that I know what to focus on today without planning it myself.

## Why this matters

Students with limited supervision often start a study session unsure what to prioritise. A single, specific suggestion based on their exams, deadlines and attendance turns the stored data into a next action.

## Acceptance criteria

- [ ] The dashboard shows a one-sentence suggestion that names at least one of the student's subjects or assignments.
- [ ] Reloading the dashboard on the same day (in the student's time zone) shows the same suggestion and makes no new AI request.
- [ ] The first dashboard load on the next day shows a newly generated suggestion.
- [ ] If the AI service fails, a fixed fallback message is shown instead, no error page appears, and generation is retried on the next load.

## Out of scope

Chatting with the AI, more than one suggestion per day, and a button to regenerate the suggestion.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
