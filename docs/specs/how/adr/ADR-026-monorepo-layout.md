---
id: ADR-026
title: Monorepo layout
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-016, ADR-028]
updated: 2026-10-17
---

# ADR-026 — Monorepo layout

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The CampusMate GitHub repository will hold the front end, back end and documentation. Without an agreed layout, files land in ad hoc places and deployment configuration gets confused.

## Decision

Use one repository with top-level frontend/, backend/ and docs/ folders, each with its own README.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Monorepo with frontend/, backend/, docs/ | Low | Low | High | High |
| B — Separate repositories | Med | Low | Med | Med |

**A — Monorepo with frontend/, backend/, docs/** (chosen)  
Pros: One history and one place to look; easy for the evaluator.  
Cons: Deployments must target subfolders.

**B — Separate repositories**  
Pros: Independent histories and deployments.  
Cons: Changes spanning both sides need two commits; harder to show as one project.

## Consequences

**Good**
- One commit history supports the authenticity requirement (§11.2).

**Neutral**
- CI jobs run per folder.

**Bad / accepted limitations**
- Hosts must be configured with the right root folder.

## Rejected alternatives

Separate repositories are rejected because they split the project's evidence trail.

## Revisit triggers

Reopen if the front end and back end end up owned by different people.

## How this is enforced

PR review checklist: new code goes under frontend/ or backend/, docs under docs/.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
