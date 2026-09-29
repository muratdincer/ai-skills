---
name: task-breakdown
description: "Breaks a user story or work item into ordered, independently verifiable technical tasks with dependencies, relative estimates and a definition of done per task. Use when a developer or team picks up a story and needs an implementation plan, wants to parallelize work, or asks how to split a story into tasks or subtasks."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: design
  title: "Break a story into tasks"
  related: "user-story, story-splitting, technical-estimation, implement-from-story, technical-design-doc"
  prompt: "Break this story into technical tasks: As a customer I want to download my invoices as PDF from the order history page."
---

# Break a Story Into Tasks

## Purpose
Turn a story into a sequence of small technical tasks that each end in a verifiable, mergeable state, so the work can be tracked, shared between developers and finished without hidden work surfacing at the end.

## When to use
- A story is ready and the team is planning how to build it.
- Several developers need to work on one story in parallel.
- An estimate looks too large and the team wants to see where the effort is.

## When not to use
- The story itself is too big or mixes several user outcomes. Use `story-splitting` first.
- The approach is unclear or risky. Use `spike-report` or `technical-design-doc` first.
- Only an effort number is needed. Use `technical-estimation`.

## Inputs
Required:
- The story or work item with its acceptance criteria.

Optional, improves quality:
- Affected components or repositories, existing design doc, team conventions (estimate unit, task size limit).
- Known constraints: feature flag policy, release window, other teams involved.

If acceptance criteria are missing, ask for them or derive candidates and mark them `[ASSUMPTION]`.

## Process
1. Read the acceptance criteria and list the behaviors the system must show; each behavior needs at least one task that delivers and verifies it.
2. Identify touched layers and assets: contract/API, data schema, domain logic, UI, integrations, configuration, infrastructure, documentation.
3. Slice vertically where possible (one thin end-to-end path first), then widen. Avoid "all backend, then all frontend".
4. Add enabling tasks explicitly: schema migration, feature flag, contract stub or mock, test data, permissions, observability.
5. Make each task small enough to finish and merge in about a day (or the team's limit), with a clear done condition and an explicit verification step (the test, check or demo that proves it).
6. Order tasks by dependency and mark which can run in parallel. Put risky or unknown work first.
7. Add verification tasks that are not already inside other tasks: integration or end-to-end test, performance check, security review if personal data or auth is involved.
8. Add release tasks: flag rollout, documentation or changelog, removal of temporary code.
9. Give relative estimates in the team's unit; mark uncertain ones and do not invent hours if the team does not use them.
10. Check coverage: map every acceptance criterion to at least one task.
11. If the goal continues, suggest `technical-estimation` for a range estimate with assumptions or `implement-from-story` to start the first task.

## Output format
```markdown
# Task Breakdown: <story title>
Story: <id/link> · Assumptions: <list or none>

| # | Task | Done when | Depends on | Parallel? | Estimate |
|---|---|---|---|---|---|
| 1 | <verb + object> | <verifiable condition> | – | – | <unit> |

## Acceptance Criteria Coverage
| Criterion | Tasks |
|---|---|
| AC1 | 2, 4, 7 |

## Risks and Open Questions
- <risk or question> — <owner>
```

## Quality checklist
- [ ] Every acceptance criterion maps to at least one task.
- [ ] Each task starts with a verb and has a checkable "done when".
- [ ] No task is larger than the team's size limit; large ones are split.
- [ ] Migrations, flags, test data and cleanup tasks are explicit.
- [ ] The first tasks reduce the biggest risk or unknown.
- [ ] Estimates use the team's unit; none are fabricated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Layer-based splitting ("backend", "frontend", "tests") that delivers nothing verifiable until the end. Prefer thin vertical slices.
- Forgetting non-code work: config, permissions, dashboards, docs, flag removal. It is often a third of the effort.
- A "write tests" task at the end. Tests belong inside each task's done condition.

## Example
Input: "As a customer I want to download my invoices as PDF from the order history page. AC1: button per order. AC2: PDF matches the invoice layout. AC3: only own invoices."

Excerpt of output:
| # | Task | Done when | Depends on | Parallel? | Estimate |
|---|---|---|---|---|---|
| 1 | Spike PDF rendering option against layout sample | Sample PDF approved by PO | – | – | 1 |
| 2 | Add `GET /orders/{id}/invoice.pdf` behind flag with ownership check | Contract test + 403 test for other user's order pass | 1 | – | 2 |
| 3 | Add download button to order history row | UI test shows button only for invoiced orders | 2 (stub ok) | Yes | 1 |
