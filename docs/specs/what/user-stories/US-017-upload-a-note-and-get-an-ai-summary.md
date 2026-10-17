---
id: US-017
title: Upload a note and get an AI summary
class: user-story
category: build
facet: what
status: draft
decides: what
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, ADR-014, ADR-015, ADR-022]
updated: 2026-10-17
---

# US-017 — Upload a note and get an AI summary

> **What this document is:** the capability we want and how we will know it works.
> **What this document is NOT:** how it is built. Implementation approach is the team's call — see `docs/specs/how/`.

## Story

As a student,
I want to upload my notes for a subject and get an AI summary,
so that I can revise the key points quickly.

## Why this matters

Students keep notes as scattered PDFs and photos with no summaries, so revision means rereading everything. Summaries generated from the student's own material are the second main AI feature.

## Acceptance criteria

- [ ] The upload screen requires choosing a subject and a file.
- [ ] The upload screen shows a one-line notice that notes are processed by an external AI service.
- [ ] PDF and plain-text files up to 10 MB are accepted.
- [ ] After a successful upload the AI summary is shown, and reopening the note later shows the same summary without a new AI request.
- [ ] A PDF with no extractable text is rejected with a message explaining it may be a scanned document.

## Out of scope

Images and handwritten notes (unless ADR-015 is amended), Word and PowerPoint files, and editing the summary.

## Evidence it exists today

Not built.

## Open questions

Is 10 MB the right size limit? Do students need Word (.docx) or PowerPoint (.pptx) support?

## Discussion

_No discussion yet. Add notes below with your name and the date._
