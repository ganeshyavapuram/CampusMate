---
id: ADR-006
title: Database engine: SQLite for development, PostgreSQL for deployment
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-016, ADR-017]
updated: 2026-10-17
---

# ADR-006 — Database engine: SQLite for development, PostgreSQL for deployment

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The synopsis lists SQLite with PostgreSQL as an "alternative option", leaving the deployed database undecided. Free hosting platforms usually wipe their disk on each redeploy, which would delete a SQLite file and all student data.

## Decision

Use SQLite locally for development and tests, and a managed free PostgreSQL database for the deployed app, with all access through the ORM.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — SQLite in development, PostgreSQL in deployment | Med | Low | High | High |
| B — SQLite everywhere | Low | Low | High | High |
| C — PostgreSQL everywhere (Docker locally) | Med | Low | Med | High |

**A — SQLite in development, PostgreSQL in deployment** (chosen)  
Pros: Zero-setup local development; deployed data survives redeploys.  
Cons: Small dialect differences between the two engines.

**B — SQLite everywhere**  
Pros: Simplest possible setup.  
Cons: Data is lost on free hosts with ephemeral disks.

**C — PostgreSQL everywhere (Docker locally)**  
Pros: Identical behaviour in development and production.  
Cons: Docker adds another tool to learn during the learning phase.

## Consequences

**Good**
- Deployed data persists.
- Local development needs no database server.

**Neutral**
- One extra free service (for example Neon) to create and configure.

**Bad / accepted limitations**
- Bugs that appear only on PostgreSQL can slip through local testing.
- SQLite needs foreign keys enabled explicitly (ADR-023).

## Rejected alternatives

SQLite everywhere is rejected because free hosts lose the file. PostgreSQL everywhere is rejected for the extra Docker learning cost.

## Revisit triggers

Reopen if the chosen host offers a free persistent disk, or if the free PostgreSQL provider changes its limits (for example storage below 0.5 GB or expiring databases).

## How this is enforced

CI runs the test suite twice: on SQLite and on a PostgreSQL service container.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
