---
id: US-039
title: View weekly productivity report
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-029]
updated: 2026-10-17
---

# US-039 — View weekly productivity report

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a weekly report of my study time and assignment completion,
so that I can see whether I'm keeping up.

## Why this matters

Without a review of the week, plans drift unnoticed. The synopsis lists this report but no module or screen for it.

## Acceptance criteria

- [ ] The student can pick a week (Monday to Sunday); the current week is the default.
- [ ] The report shows, per subject, total minutes of completed sessions and the number of sessions completed out of planned.
- [ ] The report shows how many assignments were due that week and what percentage were completed.
- [ ] The figures match the underlying records exactly (checked against a test data set).
- [ ] The report can be downloaded as CSV and printed from the browser.

## Out of scope

Focus time (no timer exists), and trends across several weeks.

## Evidence it exists today

Not built.

## Open questions

Should "focus time" be removed from synopsis §5.5, since nothing records it?

## Discussion

_No discussion yet. Add notes below with your name and the date._
