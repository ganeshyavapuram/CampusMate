---
id: ADR-002
title: Angular with Angular Material for the front end
class: adr
category: build
facet: how
status: accepted
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-001, US-044]
updated: 2026-10-17
---

# ADR-002 — Angular with Angular Material for the front end

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The student is new to front-end frameworks and the schedule allows three weeks of learning (synopsis §9). Every screen needs forms, tables, dialogs and responsive layout. Hand-styling components would consume the time needed for the AI features.

## Decision

Build the UI in Angular using Angular Material components, adding custom styles only where Material has no suitable component.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — Angular + Angular Material | Med | Low | Low | Low |
| B — React + MUI | Med | Low | Low | Low |
| C — Plain HTML, CSS and JavaScript | High | Low | Med | Med |

**A — Angular + Angular Material** (chosen)  
Pros: Complete, accessible component set; built-in routing, forms and HTTP client; responsive layout support.  
Cons: Steeper learning curve than plain HTML; apps look like standard Material apps.

**B — React + MUI**  
Pros: Larger community and more tutorials.  
Cons: More decisions to make (router, forms, state); the synopsis already names Angular.

**C — Plain HTML, CSS and JavaScript**  
Pros: Nothing new to learn beyond the web basics.  
Cons: Routing, forms and responsive components must all be built by hand.

## Consequences

**Good**
- Ready-made dialogs, tables, date pickers and form validation.
- Consistent look across all screens with little design work.

**Neutral**
- Angular's structure (components, services, guards) shapes how the front end is organised.

**Bad / accepted limitations**
- The UI looks generic.
- Angular major versions arrive every six months and may need upgrade work.

## Rejected alternatives

React is rejected because the synopsis commits to Angular and switching gains nothing for this project. Plain HTML is rejected because it would mean building routing and components by hand.

## Revisit triggers

Reopen if the learning phase overruns by more than one week, or if an Angular Material release breaks a component the app depends on.

## How this is enforced

PR review checklist: prefer a Material component before writing a custom one. ng lint runs in CI.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
