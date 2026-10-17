---
id: ADR-031
title: Feature-sliced front end with core, shared and features
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-002, ADR-004, ADR-026, ADR-030]
updated: 2026-10-17
---

# ADR-031 — Feature-sliced front end with core, shared and features

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The Angular app will have about ten screens across eight features, and the team is new to Angular (ADR-002). Sign-in, the token interceptor and the page shell are needed by every screen, while each feature has its own pages, components and API service. Without a rule for where code goes, features import from each other, the first bundle grows to include every screen, and shared code ends up copied. The full layout is in [folder-structure.md](../../../folder-structure.md).

## Decision

Organise `src/app/` into `core/` (app-wide singletons: auth service, guard and interceptor, HTTP helpers, layout shell), `shared/` (reusable components, models and utilities that know nothing about any feature) and `features/<feature>/` (each with `pages/`, `components/`, `services/`, `models/` and its own lazy-loaded `<feature>.routes.ts`), using the same feature names as the back end.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — core / shared / features, lazy-loaded features | Med | Low | Low | Med |
| B — Folders by file type (`components/`, `services/`, `pages/`) | Low | Low | Med | Med |
| C — Flat `app/` folder with everything side by side | Low | Low | High | High |

**A — core / shared / features, lazy-loaded features** (chosen)  
Pros: Each feature is self-contained and loads only when opened; clear home for app-wide code; mirrors the back-end folders.  
Cons: More folders to navigate; lazy routes and standalone components are new concepts for the team.

**B — Folders by file type (`components/`, `services/`, `pages/`)**  
Pros: Simple to explain.  
Cons: One feature's files spread across many folders; no natural boundary for lazy loading.

**C — Flat `app/` folder with everything side by side**  
Pros: Matches the Angular CLI's starting point.  
Cons: Becomes unmanageable beyond a handful of screens.

## Consequences

**Good**
- The first page load includes only `core/`, the shell and the login page; each feature downloads when first opened.
- A screen problem points to one feature folder (its `pages/` and `services/`).
- Front-end, back-end and `test-cases/` folders share feature names, and `*.spec.ts` tests sit beside the code they test.

**Neutral**
- The "Rewards" feature is `features/profile/` on the front end but `api/gamification/` on the back end, which the mapping table in `folder-structure.md` records.

**Bad / accepted limitations**
- More boilerplate per feature (a routes file and several subfolders).
- Code two features both need must be moved into `shared/` rather than imported directly, which takes discipline.
- The layout is not what the Angular CLI generates, so new files must be placed by hand.

## Rejected alternatives

Folders by file type are rejected because they split each feature and give no boundary for lazy loading. A flat folder is rejected because it won't scale past a few screens.

## Revisit triggers

Reopen if `shared/` grows to hold feature-specific logic, if two features keep needing each other's components, or if lazy loading causes noticeable delays when opening screens on a phone.

## How this is enforced

PR review checklist: no import from one `features/` folder into another; `core/` and `shared/` never import from `features/`; every feature has its own routes file loaded with `loadChildren` or `loadComponent` in `app.routes.ts`. An ESLint import-restriction rule enforces the first two checks once linting is set up.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
