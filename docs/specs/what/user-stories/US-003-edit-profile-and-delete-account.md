---
id: US-003
title: Edit profile and delete account
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-023, ADR-014]
updated: 2026-10-17
---

# US-003 — Edit profile and delete account

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to change my display name and to delete my account with all its data,
so that I control how I appear and what CampusMate keeps about me.

## Why this matters

The display name comes from Google and may not be what the student wants shown. A student who stops using the app has no way today to remove their notes, attendance and plans, which is a privacy gap once notes have been uploaded.

## Acceptance criteria

- [ ] The profile screen lets the student change their display name; names of 1 to 100 characters are saved, and an empty name is rejected with a message.
- [ ] "Delete account" opens a confirmation dialog stating that all subjects, assignments, study sessions, notes, quiz attempts, attendance and rewards will be permanently removed.
- [ ] After confirmation, no rows belonging to that user remain in any table, any stored note files are removed, and the student is signed out.
- [ ] Signing in again with the same Google account afterwards starts as a brand-new user with no data.

## Out of scope

Exporting data before deletion, an undo or grace period, and deleting the Google account itself.

## Evidence it exists today

Not built.

## Open questions

Should deletion wait for a grace period (for example 7 days) so an accidental deletion can be reversed?

## Discussion

_No discussion yet. Add notes below with your name and the date._
