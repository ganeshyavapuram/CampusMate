---
id: ADR-019
title: In-app deadline reminders
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-020, US-029, US-027, US-028]
updated: 2026-10-17
---

# ADR-019 — In-app deadline reminders

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The synopsis promises deadline reminders and "queues of reminder events" (§5.2) but no delivery mechanism. Email or push would need a scheduler and a mail or messaging service.

## Decision

Show reminders only inside the app, computed from due dates each time a page loads; no background scheduler.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — In-app reminders computed on load | Low | Low | High | High |
| B — Email reminders via a scheduler (APScheduler + email service) | Med | Low | Low | High |
| C — Web push via Firebase Cloud Messaging | High | Low | Low | High |

**A — In-app reminders computed on load** (chosen)  
Pros: No infrastructure; always accurate.  
Cons: No reminder unless the student opens the app.

**B — Email reminders via a scheduler (APScheduler + email service)**  
Pros: Reaches students outside the app.  
Cons: Needs a scheduler that keeps running on sleeping free hosts and an email provider.

**C — Web push via Firebase Cloud Messaging**  
Pros: Notifications on phone and desktop.  
Cons: Service workers and permission prompts add complexity.

## Consequences

**Good**
- Nothing extra to host or monitor.

**Neutral**
- Synopsis §5.2 wording about reminder queues needs updating.

**Bad / accepted limitations**
- Students who don't open the app get no reminder.

## Rejected alternatives

Email and push are deferred to Future Scope because free hosts sleep and can't run a reliable scheduler.

## Revisit triggers

Reopen if the Guide requires reminders outside the app, or if hosting moves to an always-on server.

## How this is enforced

Judgement call in PR review, plus unit tests for the due-soon and overdue queries.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
