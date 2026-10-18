---
id: ADR-027
title: Secrets and configuration through environment variables
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-004, ADR-005, ADR-016]
updated: 2026-10-18
---

# ADR-027 — Secrets and configuration through environment variables

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The app needs an OpenRouter key, Firebase service account, database URL and CORS origins. The repository is on GitHub, so any committed secret is exposed.

## Decision

Load configuration from environment variables with pydantic-settings, use a git-ignored .env locally, commit a .env.example, and allow only the front-end origin in CORS.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Environment variables with pydantic-settings | Low | Low | Low | High |
| B — Committed config file | Low | Low | High | Low |
| C — Cloud secret manager | High | Low | Low | Med |

**A — Environment variables with pydantic-settings** (chosen)  
Pros: Standard approach; validated at startup.  
Cons: Every environment must be configured by hand.

**B — Committed config file**  
Pros: Simple.  
Cons: Leaks secrets on GitHub.

**C — Cloud secret manager**  
Pros: Centralised secrets with rotation.  
Cons: Overkill and may need billing.

## Consequences

**Good**
- No secrets in the repository.
- The app refuses to start when a required setting is missing.

**Neutral**
- .env.example documents every setting.

**Bad / accepted limitations**
- Each host's environment must be set up manually.

## Rejected alternatives

A committed config file is rejected because it leaks secrets. A secret manager is rejected as overkill.

## Revisit triggers

Reopen if a secret is ever committed (rotate it immediately), or if more than one environment besides local and production is added.

## How this is enforced

.env is in .gitignore; gitleaks runs in CI; a startup test fails when a required variable is missing.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Approved.
