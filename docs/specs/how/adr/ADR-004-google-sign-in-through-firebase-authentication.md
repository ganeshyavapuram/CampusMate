---
id: ADR-004
title: Google sign-in through Firebase Authentication
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-011, ADR-027, US-001, US-002]
updated: 2026-10-17
---

# ADR-004 — Google sign-in through Firebase Authentication

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The app needs sign-in without spending development time on password hashing, reset emails and token issuing. Building custom auth would take time from the core modules and add security risk.

## Decision

Use Firebase Authentication with Google as the only sign-in method; the back end verifies the Firebase ID token on every protected request.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Firebase Authentication, Google only | Low | Low | Low | Med |
| B — Firebase Authentication, Google plus email/password | Med | Low | Low | Med |
| C — Custom JWT auth in FastAPI | High | Low | Low | Low |

**A — Firebase Authentication, Google only** (chosen)  
Pros: No passwords stored; one-click sign-in; free tier is ample.  
Cons: Students without a Google account can't sign in.

**B — Firebase Authentication, Google plus email/password**  
Pros: Works for students without Google accounts.  
Cons: Needs password reset and email verification screens.

**C — Custom JWT auth in FastAPI**  
Pros: No external dependency.  
Cons: Password storage, resets and token handling must be built and secured by hand.

## Consequences

**Good**
- CampusMate never stores a password.
- Every request carries a verified identity.

**Neutral**
- User records are created on first sign-in rather than at registration.

**Bad / accepted limitations**
- Students without a Google account are excluded.
- Tokens stay valid for up to one hour after sign-out.
- The back end depends on Firebase's public keys being reachable.

## Rejected alternatives

Custom JWT auth is rejected as rebuilding a solved problem (synopsis §11.1). Email/password is deferred to keep the first version small.

## Revisit triggers

Reopen if the Guide or evaluator can't use a Google account, or if Firebase Authentication's free-tier limits change.

## How this is enforced

Automated test: every protected route returns HTTP 401 without a token (TC-01), generated from the app's route list so new routes are covered.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
