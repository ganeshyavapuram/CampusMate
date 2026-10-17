---
id: ADR-001
title: Three-tier web architecture
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-002, ADR-003, ADR-005, US-008]
updated: 2026-10-17
---

# ADR-001 — Three-tier web architecture

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

CampusMate needs a browser UI, business logic (planner rules, attendance maths, gamification), relational storage and calls to two external services (Firebase, OpenRouter). The OpenRouter key must never reach the browser. Without a fixed structure, logic would drift between client and server and the DFDs in the synopsis would stop matching the code.

## Decision

Build an Angular single-page front end, a FastAPI back end that holds all business logic and external API calls, and a relational database.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Three-tier: Angular + FastAPI + relational DB | Med | Low | Low | Med |
| B — Django full-stack with server-rendered pages | Low | Low | Low | Low |
| C — Firebase-only backend-as-a-service, logic in the browser | Low | Med | Low | Low |

**A — Three-tier: Angular + FastAPI + relational DB** (chosen)  
Pros: Matches the synopsis architecture and DFDs; keeps the API key server-side; front end and back end can be tested separately.  
Cons: Two languages and two codebases to learn within the 3-week learning phase.

**B — Django full-stack with server-rendered pages**  
Pros: One language and one codebase; built-in admin and ORM.  
Cons: Contradicts the synopsis's chosen stack; less interactive UI for quizzes and the timetable.

**C — Firebase-only backend-as-a-service, logic in the browser**  
Pros: No server to host; real-time data out of the box.  
Cons: Firestore is not relational, which undermines the project's RDBMS category; the AI key would need extra cloud functions to stay secret.

## Consequences

**Good**
- The OpenRouter key and all business rules stay on the server.
- Each tier maps directly onto the synopsis's architecture diagram and DFD processes.

**Neutral**
- Two deployable units (front end and back end) instead of one.

**Bad / accepted limitations**
- Two languages (TypeScript and Python) to learn in parallel.
- Cross-origin requests need CORS configuration and token passing on every call.

## Rejected alternatives

A Firebase-only design is rejected because the project is registered under the RDBMS category and needs a relational schema. Django is rejected because the synopsis commits to Angular and FastAPI.

## Revisit triggers

Reopen if the Angular learning phase overruns by more than one week, or if the Project Guide asks for a simpler single-codebase design.

## How this is enforced

PR review checklist: no database access or OpenRouter calls in frontend/. A CI step fails if the string "openrouter" appears anywhere under frontend/.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
