---
id: US-015
title: Regenerate the study plan
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-010, ADR-018]
updated: 2026-10-17
---

# US-015 — Regenerate the study plan

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to regenerate my plan after my exam dates, subjects or study hours change,
so that my plan always matches my current situation.

## Why this matters

Exam dates move and subjects get added mid-semester. Without regeneration the only option is to live with a plan built on old inputs.

## Acceptance criteria

- [ ] A "Regenerate plan" action is available on the timetable screen.
- [ ] Before regenerating, a confirmation states how many planned sessions will be replaced.
- [ ] Only planned sessions dated today or later are replaced; completed and missed sessions stay.
- [ ] The new plan uses the current subjects, exam dates, weak flags and daily hours.
- [ ] If generation fails, the existing plan is left exactly as it was.

## Out of scope

Keeping a history of previous plans, and comparing plans side by side.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
