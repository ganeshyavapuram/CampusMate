---
id: ADR-002
title: Angular with Angular Material for the front end
class: adr
category: build
facet: how
status: proposed
decides: how
owner: Ganesh Yavapuram, Hemanjini Peddireddy
provenance: team
related: [ADR-001, US-044]
updated: 2026-10-18
---

# ADR-002 — Angular with Angular Material for the front end

> **What this document is:** one architectural decision, and what it costs.
> **What this document is NOT:** a description of the system as built (that is `how/architecture.md`), or the reasoning that led here (that is a `design-note`).

**Deciders:** Ganesh Yavapuram, Hemanjini Peddireddy

## Context

The student is new to front-end frameworks and the schedule allows three weeks of learning (synopsis §9). Every screen needs forms, tables, dialogs and responsive layout. Hand-styling components would consume the time needed for the AI features.

## Decision

Build the UI in Angular using Angular Material components for behaviour and accessibility, restyled with a custom CampusMate theme and purposeful motion so the app has a bold, modern look rather than the default Material one (see the 2026-10-18 amendment).

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
- A distinctive, animated look that students enjoy using, without giving up Material's accessibility.

**Neutral**
- Angular's structure (components, services, guards) shapes how the front end is organised.

**Bad / accepted limitations**
- Custom theming and animation add design and build time (about 3–4 days, inside the interface-polish week).
- Most of the reference components are written for React, so effects must be rebuilt in Angular rather than copied.
- Angular major versions arrive every six months and may need upgrade work.

## Rejected alternatives

React is rejected because the synopsis commits to Angular and switching gains nothing for this project. Plain HTML is rejected because it would mean building routing and components by hand.

## Revisit triggers

Reopen if the learning phase overruns by more than one week, or if an Angular Material release breaks a component the app depends on.

## How this is enforced

PR review checklist: prefer a Material component before writing a custom one; colours, shapes and type come from the shared theme tokens; every animation is checked with reduced motion turned on; no React component code is copied in. ng lint runs in CI.

## Amendments

### Amendment — 2026-10-18: Gen Z look with motion, on top of Angular Material

Requested in review: a bold, modern ("Gen Z") look with noticeable animation, using the reference sites listed in the Discussion.

- **Base stays the same.** Angular Material still provides forms, dialogs, tables, keyboard support and accessibility.
- **Custom theme.** Replace the default Material look with a CampusMate theme: brand colours, larger corner radii, expressive display type and playful empty states, defined once as theme tokens in `frontend/campusmate-web/src/app/shared/` (ADR-031).
- **Motion.** Use Angular's built-in enter/leave animations and CSS transitions for page changes, list items, dialogs and buttons. Use the framework-agnostic `motion` library only for richer moments: the onboarding flow (US-004), an expandable toolbar and the AI loading state (US-016).
- **References are inspiration, not code.** Motion Primitives, SmoothUI, 21st.dev and Watermelon UI are React component libraries, so their effects are rebuilt in Angular. Uiverse snippets are plain HTML and CSS and can be adapted. Dribbble, Mobbin, Behance, Godly, Kira Learning and awesome-design-md are for layout and style ideas. Check the licence of Unblast Mono icons before using them.
- **Limits.** Interaction animations stay at or under 300 ms so the app feels fast on low-end phones (US-044), and every animation has a reduced or switched-off version when the device asks for reduced motion.
- **Order.** Theme and motion are built after the core modules work, in the interface-polish week (synopsis §9, §11.2). If that week overruns, keep the theme and drop the advanced motion.

## Discussion

_No discussion yet. Add notes below with your name and the date._

- **Review, 2026-10-18:** Needs changes. Along with them use there wensite for the UI suggestions and animatations i nneed the asthetic GEN Z style cool animations that reflect in the app
  - <https://ui.watermelon.sh/animated-components/onboarding-screen>
  - <https://dribbble.com/search/oboarding>
  - <https://motion-primitives.com/docs/toolbar-expandable>
  - <https://smoothui.dev/docs/components/motion-loader>
  - <https://github.com/voltagent/awesome-design-md>
  - <https://unblast.com/icons/mono/>
  - <https://mobbin.com/discover/apps/ios/latest>
  - <https://www.behance.net/>
  - <https://21st.dev/community/components>
  - <https://godly.design/website/kira-learning/>
  - <https://www.kira-learning.com/2.0-launch>
  - <https://uiverse.io/cards>
