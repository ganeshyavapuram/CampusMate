---
id: US-018
title: Generate a quiz from a note
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-008, ADR-018]
updated: 2026-10-17
---

# US-018 — Generate a quiz from a note

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a multiple-choice quiz generated from each note I upload,
so that I can test myself on my own material.

## Why this matters

Self-testing is more effective than rereading, but writing questions takes time students don't have. General chatbots can do it but aren't linked to the student's notes or progress.

## Acceptance criteria

- [ ] Each successfully processed note has a quiz of 5 to 10 multiple-choice questions.
- [ ] Every question has exactly four options and exactly one correct answer.
- [ ] The quiz is saved with the note and shown again without a new AI request.
- [ ] A quiz response that doesn't meet these rules is rejected and nothing is saved (US-016).

## Out of scope

True/false, fill-in-the-blank or short-answer questions, and choosing difficulty.

## Evidence it exists today

Not built.

## Open questions

Should the student choose the number of questions, or is a fixed number fine?

## Discussion

_No discussion yet. Add notes below with your name and the date._
