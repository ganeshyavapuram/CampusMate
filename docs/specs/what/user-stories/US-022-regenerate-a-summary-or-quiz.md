---
id: US-022
title: Regenerate a summary or quiz
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

# US-022 — Regenerate a summary or quiz

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to regenerate a note's summary or quiz,
so that I can get a better result when the first one is poor.

## Why this matters

AI output quality varies with the notes and the model (synopsis §10). Without regeneration, a poor summary or quiz is stuck there for good.

## Acceptance criteria

- [ ] The note screen has separate "Regenerate summary" and "Regenerate quiz" actions.
- [ ] The new output replaces the old one only after it is generated and validated successfully.
- [ ] If regeneration fails, the existing summary or quiz is unchanged.
- [ ] Each regeneration counts towards the daily AI request limit.
- [ ] Previous quiz attempts are kept after the quiz is regenerated.

## Out of scope

Keeping several versions of a summary or quiz side by side.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
