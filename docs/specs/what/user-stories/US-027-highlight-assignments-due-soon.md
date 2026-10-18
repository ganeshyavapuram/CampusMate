---
id: US-027
title: Highlight assignments due soon
class: user-story
category: build
facet: what
status: approved
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020]
updated: 2026-10-18
---

# US-027 — Highlight assignments due soon

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want assignments due today or tomorrow to stand out,
so that I notice urgent work before it's too late.

## Why this matters

A sorted list still hides urgent items among routine ones. The synopsis flags assignments due within 24 hours.

## Acceptance criteria

- [ ] Pending assignments due today or tomorrow (in the student's time zone) show a "Due soon" label on the dashboard and the assignment list.
- [ ] Completed assignments never show the label.
- [ ] The label disappears once the due date has passed and the assignment becomes overdue (US-028).

## Out of scope

Configurable warning windows.

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: "Due soon" means due today or tomorrow in the student's time zone.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. Yes. Without due times, "due today or tomorrow" is the clearest rule.
