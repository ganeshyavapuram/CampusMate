---
id: ADR-016
title: Hosting on Firebase Hosting, Render and Neon
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-006, ADR-027, US-044]
updated: 2026-10-18
---

# ADR-016 — Hosting on Firebase Hosting, Render and Neon

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The synopsis doesn't say where the app runs, and it must be reachable by the evaluator at no cost. Without a decision, deployment is left to the last week, when free-tier surprises are hardest to fix.

## Decision

Host the Angular build on Firebase Hosting, the FastAPI back end on Render's free web service, and the database on Neon's free PostgreSQL.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Firebase Hosting + Render + Neon | Med | Low | Low | High |
| B — All on Render (static site, web service, Render PostgreSQL) | Low | Low | Low | High |
| C — Single VPS | High | Med | Low | Med |

**A — Firebase Hosting + Render + Neon** (chosen)  
Pros: All free; front end shares the Firebase project with authentication.  
Cons: Three services to configure; Render's free tier sleeps when idle.

**B — All on Render (static site, web service, Render PostgreSQL)**  
Pros: One dashboard.  
Cons: Render's free PostgreSQL databases expire after 30 days.

**C — Single VPS**  
Pros: Full control; no sleeping.  
Cons: Costs money and needs server administration.

## Consequences

**Good**
- Zero hosting cost.
- Each part can be redeployed independently.

**Neutral**
- Deployment steps are written in each folder's README.

**Bad / accepted limitations**
- The first request after about 15 minutes idle can take up to a minute while the back end wakes.
- Three accounts to manage.

## Rejected alternatives

All-on-Render is rejected because its free database expires. A VPS is rejected for cost and administration effort.

## Revisit triggers

Reopen if any provider removes or reduces its free tier, or if cold starts make the evaluation demo unreliable.

## How this is enforced

Deployment checklist in the README, plus a post-deploy smoke test that signs in and loads the dashboard. Open the app before the evaluation to wake the back end.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
