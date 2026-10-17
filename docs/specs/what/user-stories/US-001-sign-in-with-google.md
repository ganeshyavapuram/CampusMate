---
id: US-001
title: Sign in with Google
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-004, ADR-011]
updated: 2026-10-17
---

# US-001 — Sign in with Google

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to sign in with my Google account,
so that I can use CampusMate without creating another password.

## Why this matters

Students already manage accounts for portals, email and many apps, and a separate CampusMate password would add friction plus a reset flow to build and secure. Google sign-in gets a student to their dashboard in one step and gives the back end a verified identity for every request.

## Acceptance criteria

- [ ] The login screen shows a "Sign in with Google" button and a one-paragraph introduction to CampusMate.
- [ ] After a successful Google sign-in the student is taken to the dashboard (or to first-time setup, US-004, if they have no subjects).
- [ ] On a student's first sign-in exactly one User record and one GamificationRecord are created; signing in again creates no new records.
- [ ] A request to any protected API endpoint without a valid Firebase ID token returns HTTP 401 and no data (TC-01).
- [ ] If the student closes the Google pop-up without signing in, they remain on the login screen and no error page is shown.

## Out of scope

Email/password sign-in, other identity providers (Microsoft, GitHub, Apple), and any multi-factor authentication beyond what Google applies to the account.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
