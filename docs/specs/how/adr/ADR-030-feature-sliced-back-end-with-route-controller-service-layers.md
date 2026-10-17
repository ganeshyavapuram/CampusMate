---
id: ADR-030
title: Feature-sliced back end with route, controller and service layers
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-003, ADR-011, ADR-017, ADR-018, ADR-026, ADR-031]
updated: 2026-10-17
---

# ADR-030 — Feature-sliced back end with route, controller and service layers

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The FastAPI back end will hold eight features (auth, subjects, assignments, attendance, planner, notes, dashboard, gamification) built by a team still learning FastAPI. Without an agreed layout, HTTP handling, business rules and database code end up mixed in the same functions, every feature is organised differently, and a bug report doesn't point to a file. The Notion tasks were written before any layout existed, so their file paths need one fixed target. The full layout is in [folder-structure.md](../../../folder-structure.md).

## Decision

Organise `backend/api/` as one folder per feature, each split into `<feature>_route.py`, `<feature>_controller.py`, `<feature>_service.py` and `<feature>_schemas.py`, with pure-logic files (`*_calculations.py`, `*_rules.py`, `*_validation.py`, `*_prompts.py`) beside them. Shared wiring lives in `app/`, `core/`, `db/` and `utils/`, and tests mirror the feature folders under `tests/api/<feature>/`.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Feature folders with route, controller and service layers | Med | Low | Med | Med |
| B — Layer folders (all routes in `routes/`, all services in `services/`) | Low | Low | Med | Med |
| C — One file per feature with everything in it | Low | Low | High | High |

**A — Feature folders with route, controller and service layers** (chosen)  
Pros: Everything for a feature is in one folder; each layer has one job, so bugs map to a file; pure rules can be unit tested without a database or HTTP.  
Cons: More files per feature; the controller layer adds a step FastAPI tutorials usually skip.

**B — Layer folders (all routes in `routes/`, all services in `services/`)**  
Pros: Common in tutorials; fewer folders.  
Cons: One feature's code is spread across several folders; harder to see what a feature contains.

**C — One file per feature with everything in it**  
Pros: Fastest to start.  
Cons: Files grow into hundreds of lines mixing HTTP, rules and SQL; hard to test the rules on their own.

## Consequences

**Good**
- A symptom points to a layer: wrong status code means the controller, wrong data means the service (see "Where to look when something breaks").
- Attendance maths, gamification rules and AI-output validation are pure functions with fast unit tests.
- Back-end feature names match the front end and `test-cases/` folders.

**Neutral**
- Notion task paths are redirected through the table in `folder-structure.md`.
- Adding a feature means creating its folder and adding one line to `app/router/api_router.py`.

**Bad / accepted limitations**
- About five files per feature, some of them very small.
- The controller layer is extra code that only maps errors to HTTP responses.
- Features that need shared logic must go through `core/` or `utils/`, or through the two allowed cross-feature calls.

## Rejected alternatives

Layer folders are rejected because a feature's code would be spread across the project. One file per feature is rejected because it mixes HTTP, rules and database code, which makes testing the rules hard.

## Revisit triggers

Reopen if a feature regularly needs another feature's service beyond the two allowed exceptions (`get_current_user` and `gamification_service`), if a whole layer stays empty for most features, or if the layout is clearly slowing the team down by the end of the core-modules phase.

## How this is enforced

PR review checklist: files sit in the right feature folder and follow the naming rule; only controllers raise `HTTPException`; services never import routes or controllers; only `utils/ai_client.py` calls OpenRouter; models live in `db/models/`. A CI step fails if `HTTPException` appears in a `*_service.py` file or `openrouter` appears outside `utils/ai_client.py`.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
