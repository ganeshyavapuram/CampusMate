---
id: ADR-015
title: Text extraction from PDF and plain-text notes
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-005, ADR-014, US-017, US-023]
updated: 2026-10-17
---

# ADR-015 — Text extraction from PDF and plain-text notes

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Notes can be typed PDFs, scanned PDFs, photos or handwriting (§10). Most free OpenRouter models are text-only, so images can't simply be sent to the AI.

## Decision

Accept PDF and plain-text files, extract text with pypdf, and reject files with no extractable text; support images only if a free vision model is reliably available.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — pypdf for PDF plus plain text | Low | Low | Med | High |
| B — Free vision model for images | Med | Low | Low | High |
| C — Local OCR with Tesseract | Med | Low | Low | High |

**A — pypdf for PDF plus plain text** (chosen)  
Pros: Reliable for typed notes; no external service.  
Cons: No support for scans, photos or handwriting.

**B — Free vision model for images**  
Pros: Handles photos and some handwriting.  
Cons: Few free vision models; availability changes.

**C — Local OCR with Tesseract**  
Pros: Works offline for printed text.  
Cons: Extra system dependency; poor on handwriting.

## Consequences

**Good**
- Core upload flow works on day one.

**Neutral**
- Synopsis §10 must state that scanned and handwritten notes aren't supported.

**Bad / accepted limitations**
- Students who photograph handwritten notes, a common case, can't use AI Notes.

## Rejected alternatives

Tesseract is rejected because it adds a system dependency and handles handwriting badly. The vision-model option is deferred, not rejected.

## Revisit triggers

Reopen if a free vision model stays available on OpenRouter for a month, or if most test users upload photos.

## How this is enforced

Tests with fixture files: a typed PDF is accepted, a scanned PDF is rejected with the expected message.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
