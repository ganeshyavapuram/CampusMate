---
id: US-024
title: Add an assignment
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011]
updated: 2026-10-17
---

# US-024 — Add an assignment

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to add an assignment with its subject and due date,
so that I stop missing deadlines buried in chat groups.

## Why this matters

Assignment announcements arrive in messaging groups where they get buried (synopsis §2.3). Recording them in one place with due dates is the basis for reminders and reports.

## Acceptance criteria

- [ ] The student can add an assignment with a title of 1 to 150 characters, a subject and a due date.
- [ ] A due date before today is rejected with a message, and nothing is saved (TC-03).
- [ ] A new assignment has status "pending" and appears in the assignment list sorted by due date.
- [ ] It also appears in the dashboard's pending assignments.

## Out of scope

Attachments, submitting work to the university, and a due time of day.

## Evidence it exists today

Not built.

## Open questions

Do assignments need a description field, and a due time as well as a date?

## Discussion

_No discussion yet. Add notes below with your name and the date._
