---
id: US-007
title: Enter weekly class timetable
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

# US-007 — Enter weekly class timetable

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to enter my weekly class timetable,
so that the dashboard shows today's classes and attendance can warn me based on the classes still to come.

## Why this matters

The synopsis shows "today's classes" on the dashboard but never collects the timetable, so that section would always be empty. Students currently keep timetables in a separate calendar app that knows nothing about attendance.

## Acceptance criteria

- [ ] The student can add a class slot with a subject, weekday, start time and end time.
- [ ] A slot whose end time is not after its start time is rejected with a message.
- [ ] A slot overlapping another slot on the same weekday is rejected with a message naming the conflicting class.
- [ ] The student can edit and delete slots.
- [ ] The dashboard's "Today's classes" section lists today's slots in start-time order, using the student's time zone.
- [ ] Attendance percentages and warnings use only logged attendance records, never classes predicted from the timetable.

## Out of scope

One-off changes (cancelled or extra classes, holidays), non-weekly patterns, and importing a timetable from a university portal (synopsis §10).

## Evidence it exists today

Not built.

## Open questions

Resolved 2026-10-18: Holidays aren't modelled; warnings use logged attendance only, and the timetable is used for today's classes and the next class date.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.

- **Review, 2026-10-18:** Recommendation accepted. Don't model holidays. Attendance warnings use only classes the student has logged; the timetable only shows today's classes and the next class date.
