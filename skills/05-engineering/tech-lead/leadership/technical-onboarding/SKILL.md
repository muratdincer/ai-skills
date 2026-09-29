---
name: technical-onboarding
description: "Builds a technical onboarding plan for a developer joining a team: environment setup with verification, a guided codebase and architecture tour, ways of working, a sequence of progressively harder first work items, key contacts and checkpoints, adapted to the person's experience and role. Use when a new or transferring developer starts, when a tech lead must prepare the first weeks for a newcomer, or when an existing onboarding path is too slow and needs restructuring."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: tech-lead
  area: leadership
  title: "Onboard a developer"
  related: "onboarding-plan-30-60-90, readme-writing, legacy-code-comprehension, coding-standards, onboarding-guide"
  prompt: "A mid-level backend developer joins our payments team on Monday. Prepare a technical onboarding plan for the first two weeks, including setup and first tickets."
---

# Onboard a Developer

## Purpose
Get a new developer to a first meaningful, reviewed change in production quickly and safely, and build the mental model of the system they need to work independently. Good onboarding reduces time to productivity and the load on the rest of the team.

## When to use
- A developer joins the team, from outside or from another team.
- A tech lead needs a concrete plan for the first one to two weeks.
- Onboarding feedback says setup takes days or newcomers stay dependent for too long.

## When not to use
- The plan covers the whole role over three months, including non-technical goals. Use `onboarding-plan-30-60-90`.
- The need is general documentation for the repository. Use `readme-writing`.
- The organization-wide onboarding guide (HR, tools, policies) is the subject. Use `onboarding-guide`.

## Inputs
Required:
- Team and system context (what the team owns, main technologies) and the newcomer's role and experience level.

Optional, improves quality:
- Repositories, architecture docs, setup instructions, coding standards, definition of done.
- Candidate first work items, the buddy/mentor, access request process, security training requirements.
- Start date and planned absences.

If the team context or the newcomer's level is missing, ask. Ask at most five questions; everything else is marked `[TBD]` in the plan.

## Process
1. Define the target for the period: e.g., "first reviewed change merged and deployed by day 5, owns a small feature by end of week 2". Adapt to experience level and domain complexity.
2. List access and accounts needed on day 1 (source control, pipeline, environments, observability, ticketing, chat channels), who grants each and lead time; request before the start date. Never write credentials into the plan.
3. Write environment setup as verifiable steps: each ends with a check ("tests pass locally", "service responds on health endpoint"). Record gaps found during setup as documentation fixes.
4. Plan the architecture tour: context and container view of the system (C4 levels 1-2), main data flows, the most important domain concepts and glossary, and where the risky or legacy areas are.
5. Plan the codebase tour: repository layout, how a request flows through the code, testing approach, build and release path, feature flags, logging and dashboards.
6. Explain ways of working: branching and review rules, definition of done, on-call expectations, meeting rhythm, how decisions are recorded.
7. Select first work items in increasing difficulty: (a) a documentation or setup fix, (b) a small, well-bounded bug or change with tests, (c) a feature slice touching more of the system. Each has a done criterion and a named reviewer.
8. Assign a buddy and list key contacts (product, architecture, operations, security) with what to ask whom.
9. Schedule checkpoints (end of day 1, end of week 1, end of week 2) with questions to assess progress and adjust.
10. Mark every assumption about tools, people and dates `[ASSUMPTION]` or `[TBD]`, and if the goal continues suggest `onboarding-plan-30-60-90` for the longer horizon, `readme-writing` for setup gaps found, or `legacy-code-comprehension` for complex areas.

## Output format
```markdown
# Technical Onboarding: <name/role> · <team>
Start: <date> · Buddy: <name or [TBD]> · Target: <measurable goal for the period>

## Before Day 1 (Access)
| Access | Granted by | Lead time | Status |
|---|---|---|---|

## Environment Setup
1. <step> — Verify: <check>

## Architecture and Codebase Tour
| Session | Content | Material | Host |
|---|---|---|---|

## Ways of Working
- ...

## First Work Items
| # | Item | Why this one | Done when | Reviewer |
|---|---|---|---|---|

## Contacts
| Topic | Person/role |
|---|---|

## Checkpoints
| When | Questions | Adjust if |
|---|---|---|
```

## Quality checklist
- [ ] The plan has a measurable target (e.g., first change merged and deployed by a given day).
- [ ] Every setup step ends with a verification check.
- [ ] First work items increase in difficulty and each has a done criterion and reviewer.
- [ ] Access requests are listed with owners and lead times; no credentials appear in the plan.
- [ ] Names, dates and tools not given by the user are marked `[TBD]` or `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Days of reading documentation before touching code. Pair reading with a small real change early.
- A first ticket that is urgent or on the critical path; the newcomer gets stuck under pressure. Choose bounded, non-urgent work.
- Leaving access requests to day 1, which blocks the first week. Request them before the start date.

## Example
Input: "Mid-level backend developer joins payments team Monday; .NET services, message broker, Kubernetes."

Excerpt of output:
- Target: first reviewed change deployed to production by day 5; owns a small refund-report feature by end of week 2.
| # | Item | Why this one | Done when | Reviewer |
|---|---|---|---|---|
| 1 | Fix outdated steps in the local setup guide | Uses setup pain as input | Guide updated and merged | Buddy |
| 2 | Add missing validation for refund amount with tests | Small, touches API and domain | Merged, deployed, alert-free for 24 h | Tech lead |
