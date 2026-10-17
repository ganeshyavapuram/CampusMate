---
id: ADR-017
title: SQLAlchemy ORM with Alembic migrations
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-003, ADR-006]
updated: 2026-10-17
---

# ADR-017 — SQLAlchemy ORM with Alembic migrations

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

FastAPI has no database layer. The schema will change during development, and the same code must run on SQLite and PostgreSQL (ADR-006). Hand-edited schemas drift from the data dictionary.

## Decision

Use SQLAlchemy 2.0 for models and queries, and Alembic for versioned schema migrations.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — SQLAlchemy 2.0 + Alembic | Med | Low | Low | High |
| B — SQLModel + Alembic | Low | Low | Low | High |
| C — Raw SQL with database drivers | Low | Low | High | Med |

**A — SQLAlchemy 2.0 + Alembic** (chosen)  
Pros: Database-independent; widely documented; migration history.  
Cons: Two libraries to learn.

**B — SQLModel + Alembic**  
Pros: Combines Pydantic and SQLAlchemy models.  
Cons: Thinner documentation, especially for migrations.

**C — Raw SQL with database drivers**  
Pros: Uses the student's existing SQL knowledge directly.  
Cons: Separate SQL for SQLite and PostgreSQL; manual schema changes.

## Consequences

**Good**
- One codebase for both engines.
- Migration history doubles as evidence of original work.

**Neutral**
- Key queries can be shown as SQL in the report using SQLAlchemy's query output.

**Bad / accepted limitations**
- ORM learning time.
- Generated SQL is less visible than hand-written SQL.

## Rejected alternatives

Raw SQL is rejected because it ties the code to one engine. SQLModel is rejected for its thinner migration documentation.

## Revisit triggers

Reopen if ORM complexity blocks progress for more than a week.

## How this is enforced

CI runs "alembic check" and fails if the models have changes without a migration.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
