---
id: ADR-023
title: Cascade deletes for subjects and accounts
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-014, US-003, US-005, US-021]
updated: 2026-10-17
---

# ADR-023 — Cascade deletes for subjects and accounts

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Assignment, StudySession, Note and Attendance all reference Subject, but the synopsis doesn't say what happens on delete. SQLite also ignores foreign keys unless they are turned on.

## Decision

Use ON DELETE CASCADE from Subject to its children and from User to everything, show a confirmation that states what will be removed, and enable foreign keys in SQLite.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Cascade delete with confirmation | Low | Low | High | Low |
| B — Soft delete (deleted_at column) | Med | Low | High | High |
| C — Block delete while children exist | Low | Low | High | High |

**A — Cascade delete with confirmation** (chosen)  
Pros: No orphaned rows; account deletion really removes data.  
Cons: Deletion is permanent.

**B — Soft delete (deleted_at column)**  
Pros: Deletions can be undone.  
Cons: Every query must filter deleted rows; account deletion wouldn't truly remove data.

**C — Block delete while children exist**  
Pros: Prevents accidents.  
Cons: Students must delete every child record by hand first.

## Consequences

**Good**
- No orphaned data.
- Account deletion meets privacy expectations.

**Neutral**
- Confirmation dialogs list the counts of records that will be deleted.

**Bad / accepted limitations**
- There is no undo.

## Rejected alternatives

Soft delete is rejected because deleted accounts must really remove data. Blocking deletes is rejected as tedious for students.

## Revisit triggers

Reopen if students accidentally delete subjects and ask for undo.

## How this is enforced

Test: PRAGMA foreign_keys is ON in SQLite connections; deleting a subject removes its child rows.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
