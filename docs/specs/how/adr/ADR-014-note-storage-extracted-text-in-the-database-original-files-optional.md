---
id: ADR-014
title: Note storage: extracted text in the database, original files optional
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-015, ADR-016, ADR-023, US-017, US-021]
updated: 2026-10-18
---

# ADR-014 — Note storage: extracted text in the database, original files optional

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Note.file_url points to an uploaded file, but the synopsis never says where files live. Firebase Storage now requires the pay-as-you-go Blaze plan for new projects, and free back-end hosts wipe their disks on redeploy.

## Decision

Extract the text at upload, store it in a new Note.extracted_text column, and generate summaries and quizzes from it; keep original files on local disk in development only.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Extracted text in the database; files optional | Low | Low | High | High |
| B — Firebase Storage | Low | Med | Low | Med |
| C — File bytes in a database BLOB column | Low | Low | High | Med |
| D — Supabase Storage free tier | Med | Low | Low | High |

**A — Extracted text in the database; files optional** (chosen)  
Pros: No paid storage; summaries can be regenerated without the file.  
Cons: Original files can't be downloaded in the deployed app.

**B — Firebase Storage**  
Pros: Same project as authentication.  
Cons: Requires a billing account for new projects.

**C — File bytes in a database BLOB column**  
Pros: Everything in one place.  
Cons: Bloats the database and free database storage limits.

**D — Supabase Storage free tier**  
Pros: Free object storage with download links.  
Cons: Another external service and key to manage.

## Consequences

**Good**
- No paid service is needed.
- Regeneration doesn't depend on the file.

**Neutral**
- file_url becomes optional.

**Bad / accepted limitations**
- Students can't re-download the original file from the deployed app.

## Rejected alternatives

Firebase Storage is rejected because it needs billing. BLOB storage is rejected for database size. Supabase Storage is kept as the upgrade path if downloads are required.

## Revisit triggers

Reopen if the Guide requires original files to be downloadable, or if Firebase Storage becomes free again for new projects.

## How this is enforced

Integration test: after upload, extracted_text is non-empty and no file is written outside the configured upload folder.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
