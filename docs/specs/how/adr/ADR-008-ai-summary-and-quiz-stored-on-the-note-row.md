---
id: ADR-008
title: AI summary and quiz stored on the Note row
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, US-017, US-018, US-019]
updated: 2026-10-17
---

# ADR-008 — AI summary and quiz stored on the Note row

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Each note has one current summary and one current quiz (§4.6 stores them as ai_summary and quiz_json). Quiz attempts are a separate concern because one quiz can be taken many times.

## Decision

Keep ai_summary and quiz_json as columns on Note, validated against a Pydantic schema before saving, and store attempts in a separate QuizAttempt table.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Columns on Note plus a QuizAttempt table | Low | Low | High | Med |
| B — Normalised Quiz, Question and Option tables | High | Low | High | Med |
| C — Separate Quiz table holding JSON | Med | Low | High | Med |

**A — Columns on Note plus a QuizAttempt table** (chosen)  
Pros: Simple reads and writes; regenerating replaces two columns.  
Cons: Individual questions can't be queried with SQL.

**B — Normalised Quiz, Question and Option tables**  
Pros: Fully relational; good for showing normal forms in the report.  
Cons: Many more tables and joins for little benefit.

**C — Separate Quiz table holding JSON**  
Pros: Allows several quiz versions per note.  
Cons: Extra table with no current need.

## Consequences

**Good**
- Fewer tables and simpler code for the AI Notes module.

**Neutral**
- QuizAttempt is a new table to add to the ER diagram.

**Bad / accepted limitations**
- quiz_json is not normalised, which the report must justify in an RDBMS project.
- Question-level analytics are not possible.

## Rejected alternatives

Normalised quiz tables are rejected as complexity without a user-facing benefit. A separate Quiz table is rejected because versioning is out of scope (US-022).

## Revisit triggers

Reopen if question-level statistics become a requirement, or if the Guide asks for a fully normalised schema.

## How this is enforced

Unit test: a malformed quiz JSON is rejected and the Note row is unchanged.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
