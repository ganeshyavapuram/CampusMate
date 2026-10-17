---
id: US-006
title: Set exam dates and weak subjects
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-010]
updated: 2026-10-17
---

# US-006 — Set exam dates and weak subjects

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to set each subject's exam date and mark subjects I find difficult,
so that my study plan and dashboard focus on what is coming up and what I struggle with.

## Why this matters

Exam dates and weak areas are the main inputs to the planner, yet the synopsis only collects them inside the planner form. Students revise poorly when difficult subjects get the same time as easy ones.

## Acceptance criteria

- [ ] The student can set, change and clear an exam date for each subject.
- [ ] An exam date before today is rejected with a message.
- [ ] The student can toggle a subject's weak flag, and weak subjects show a visible "Weak" label in the subject list and planner form.
- [ ] The dashboard's "Upcoming exams" section lists subjects with an exam in the next 30 days, soonest first, with the number of days remaining.

## Out of scope

More than one exam per subject (mid-term and final), and exam times or venues.

## Evidence it exists today

Not built.

## Open questions

Do any subjects need more than one exam date, for example a practical and a theory exam?

## Discussion

_No discussion yet. Add notes below with your name and the date._
