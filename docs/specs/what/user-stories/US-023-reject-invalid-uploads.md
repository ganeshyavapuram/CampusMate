---
id: US-023
title: Reject invalid uploads
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-015, ADR-025]
updated: 2026-10-17
---

# US-023 — Reject invalid uploads

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want a clear message when I upload a file CampusMate can't use,
so that I know what to upload instead.

## Why this matters

Unsupported or oversized files would otherwise fail deep inside text extraction or the AI call, wasting the student's time and the AI quota.

## Acceptance criteria

- [ ] Uploading an unsupported type (for example .exe or .docx) is rejected with a message listing the allowed types (TC-07).
- [ ] Uploading a file over the size limit is rejected with a message stating the limit.
- [ ] Both checks are also enforced by the API: a direct request with an invalid file returns HTTP 400 or 422.
- [ ] No note is created and no AI request is made for a rejected file.

## Out of scope

Virus scanning.

## Evidence it exists today

Not built.

## Open questions

None.

## Discussion

_No discussion yet. Add notes below with your name and the date._
