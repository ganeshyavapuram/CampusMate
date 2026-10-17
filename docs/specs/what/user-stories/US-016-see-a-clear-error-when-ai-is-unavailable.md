---
id: US-016
title: See a clear error when AI is unavailable
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, ADR-024]
updated: 2026-10-17
---

# US-016 — See a clear error when AI is unavailable

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a clear message when an AI feature can't run,
so that I know what happened and that none of my data was damaged.

## Why this matters

Free AI models are rate-limited and can disappear without notice (synopsis §10). Without deliberate handling, students would see spinners that never end or half-saved plans and quizzes.

## Acceptance criteria

- [ ] When an AI request fails or times out, the student sees a message saying the AI service is unavailable and to try again later, within 70 seconds of starting the action.
- [ ] No study sessions, summaries, quizzes or suggestions are partially saved after a failure.
- [ ] The failed action can be retried from the same screen.
- [ ] When the student has reached the daily AI request limit, a different message says so and states when the limit resets.

## Out of scope

Queueing failed requests to run later, and offline AI.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
