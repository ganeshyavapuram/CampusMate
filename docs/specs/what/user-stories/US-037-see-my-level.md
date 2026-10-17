---
id: US-037
title: See my level
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-021]
updated: 2026-10-17
---

# US-037 — See my level

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a level based on my total XP,
so that I can see my long-term progress at a glance.

## Why this matters

The synopsis Profile screen shows a level, but there is no rule for calculating one. Without it the field can't be built or tested.

## Acceptance criteria

- [ ] Level = floor(XP / 100) + 1, so 0–99 XP is level 1 and 100–199 XP is level 2.
- [ ] The profile and dashboard show the current level.
- [ ] Progress towards the next level is shown, for example "40 / 100 XP".

## Out of scope

Rewards for reaching a level.

## Evidence it exists today

Not built.

## Open questions

Is a flat 100 XP per level right, or should each level need more XP than the last?

## Discussion

_No discussion yet. Add notes below with your name and the date._
