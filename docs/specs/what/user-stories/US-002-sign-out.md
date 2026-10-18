---
id: US-002
title: Sign out
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-004]
updated: 2026-10-18
---

# US-002 — Sign out

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to sign out of CampusMate,
so that my data is safe when I use a shared or public computer.

## Why this matters

Distance-learning students often use shared family computers or study-centre machines. Without a visible sign-out, the next person at that browser can see the student's notes, attendance and plans.

## Acceptance criteria

- [ ] A "Sign out" control is reachable from every screen after sign-in (header or profile menu).
- [ ] Selecting it returns the student to the login screen.
- [ ] After signing out, pressing the browser Back button does not display any previously loaded student data.
- [ ] After signing out, the front end holds no Firebase ID token, and the next API call from that browser is rejected with HTTP 401 until the student signs in again.

## Out of scope

Signing out of all devices at once, and revoking Firebase tokens server-side before they expire.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
