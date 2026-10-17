---
id: ADR-029
title: Reports computed on request with CSV export
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-017, US-039, US-040, US-041, US-042]
updated: 2026-10-17
---

# ADR-029 — Reports computed on request with CSV export

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

Section 5.5 lists four reports but no module, storage or export format. Precomputed reports can go stale; generating PDFs on the server adds libraries.

## Decision

Compute each report on request with SQL aggregate queries, show it on screen, offer CSV download, and rely on the browser's print-to-PDF.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — On-request SQL aggregates, CSV and browser print | Low | Low | High | High |
| B — Precomputed snapshot tables | Med | Low | High | Med |
| C — Server-side PDF generation (ReportLab or WeasyPrint) | Med | Low | Low | High |

**A — On-request SQL aggregates, CSV and browser print** (chosen)  
Pros: Always up to date; good SQL showcase; no extra libraries.  
Cons: No historical snapshots.

**B — Precomputed snapshot tables**  
Pros: Fast and keeps history.  
Cons: Snapshots go stale and need a scheduler.

**C — Server-side PDF generation (ReportLab or WeasyPrint)**  
Pros: Polished printable output.  
Cons: More libraries and layout work.

## Consequences

**Good**
- Reports always match the live data.
- Aggregate queries demonstrate SQL skills for the report.

**Neutral**
- A Reports module and screen must be added to synopsis §5.1 and §5.6.

**Bad / accepted limitations**
- Past weeks can't be compared unless re-computed.
- Printed output is only as good as the browser's print styling.

## Rejected alternatives

Snapshot tables are rejected because they need a scheduler. Server-side PDFs are rejected as extra work for little gain.

## Revisit triggers

Reopen if the Guide requires formatted PDF reports, or if report queries exceed one second.

## How this is enforced

Tests compare each report's figures with a fixed fixture data set.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
