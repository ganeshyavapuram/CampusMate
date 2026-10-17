---
id: ADR-028
title: Testing approach: pytest, Angular test runner and recorded AI responses
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-018, ADR-026, US-016]
updated: 2026-10-17
---

# ADR-028 — Testing approach: pytest, Angular test runner and recorded AI responses

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The final report needs unit, integration and system test reports (§5.4). Calling the real AI during tests would use up the free quota (§11.3) and make results unrepeatable.

## Decision

Use pytest with FastAPI's TestClient on a temporary SQLite database, replace Firebase verification with a test dependency, replay recorded AI responses, use Angular CLI's default test runner for the front end, and keep a manual system-test checklist.

## Options considered

| Option | Complexity | Cost | Team familiarity | Reversibility |
|---|---|---|---|---|
| A — pytest + TestClient + recorded AI responses + Angular CLI runner | Med | Low | Low | High |
| B — Tests against the live AI | Low | Med | Low | High |
| C — Manual testing only | Low | Low | High | High |

**A — pytest + TestClient + recorded AI responses + Angular CLI runner** (chosen)  
Pros: Fast, free, repeatable; maps onto the report's sections.  
Cons: Recorded responses can drift from real model output.

**B — Tests against the live AI**  
Pros: Always realistic.  
Cons: Uses quota; results change between runs.

**C — Manual testing only**  
Pros: No test code.  
Cons: No repeatable evidence for the report.

## Consequences

**Good**
- Tests run in CI on every push.
- Test results feed the report directly.

**Neutral**
- Recorded AI responses live in backend/tests/fixtures.

**Bad / accepted limitations**
- A few live AI checks are still needed before submission.

## Rejected alternatives

Live AI tests are rejected for quota and repeatability. Manual-only testing is rejected because the report requires documented test levels.

## Revisit triggers

Reopen if recorded responses no longer match the format the chosen models return.

## How this is enforced

GitHub Actions runs pytest and the Angular tests on every push; PR review checks each new route has at least one test.

## Amendments

_No amendments yet. Add each one as `### Amendment — YYYY-MM-DD: <what changed and why>`._

## Discussion

_No discussion yet. Add notes below with your name and the date._
