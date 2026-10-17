---
id: US-019
title: Take a quiz and see my score
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-008]
updated: 2026-10-17
---

# US-019 — Take a quiz and see my score

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to answer the quiz in the app and see my score,
so that I know how well I understand the material.

## Why this matters

The synopsis describes an interactive quiz but stores no attempts, so a student gets no feedback or record of progress.

## Acceptance criteria

- [ ] The student can select one option per question and submit the quiz.
- [ ] Submitting with unanswered questions asks for confirmation; unanswered questions count as wrong.
- [ ] After submitting, the score is shown as "correct / total" and each question shows the correct answer.
- [ ] Each submitted attempt is saved with its score and date.

## Out of scope

Timed quizzes, sharing scores, and leaderboards (synopsis §8).

## Evidence it exists today

Not built.

## Open questions

Should completing a quiz award XP?

## Discussion

_No discussion yet. Add notes below with your name and the date._
