---
name: iteration-planning
description: "Facilitates an iteration/sprint planning session end to end: calculates realistic capacity, confirms the iteration goal, selects work that fits and breaks it into tasks, and records risks and the resulting plan. Use when a team is about to start an iteration/sprint, when someone asks for a planning agenda or capacity calculation, or when past plans were routinely overcommitted."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Facilitate iteration planning"
  related: "iteration-goal, estimation-session, velocity-analysis, task-breakdown, definition-of-ready"
  prompt: "Help me run sprint planning for 6 developers over a 2-week sprint; one is on leave 3 days and we have a release freeze on the last day. Here are the top 12 backlog items."
---

# Facilitate Iteration Planning

## Purpose
Produce an iteration/sprint plan the team actually believes in: a goal, a selection sized to real capacity, a first task breakdown and visible risks, so the iteration starts with shared commitment rather than a wish list.

## When to use
- The team starts a new iteration/sprint and needs an agenda and a capacity-based selection.
- Recent iterations ended with large carry-over and planning needs to be reset.
- A new or re-formed team plans its first iteration.

## When not to use
- Only the one-line goal is needed. Use `iteration-goal`.
- Items are unclear or too large to plan. Use `backlog-refinement` or `story-splitting` first.
- The team works in continuous flow without iterations. Use `wip-policy` and `monte-carlo-forecast` for commitments.

## Inputs
Required:
- Ordered candidate backlog items (with sizes if the team estimates).
- Team members and availability for the iteration (length, leave, other duties).

Optional, improves quality:
- Throughput or velocity of the last 3-6 iterations.
- Draft iteration goal, product/release goal.
- Known events: releases, freezes, holidays, on-call rotation, dependencies on other teams.
- Definition of Ready and Definition of Done.

If candidates or availability are missing, ask for them (at most 5 focused questions). Everything else becomes an open question.

## Process
1. Confirm iteration length, dates and fixed events (freezes, releases, holidays). Mark any unconfirmed date `[TBD]`.
2. Compute capacity per person: working days minus leave minus recurring load (meetings, support, on-call). State the focus factor used and mark it `[ASSUMPTION]` unless the team supplied it.
3. Cross-check capacity with history: if past throughput/velocity is available, use the median of recent iterations as the ceiling and explain gaps between the two views. Never invent historical figures.
4. Confirm or draft the iteration goal with the product owner; if it is only a list of items, propose an outcome-based goal.
5. Check each candidate against the Definition of Ready; move items that fail it to a "not ready" list with the missing element.
6. Select items in backlog order until the capacity ceiling is reached, keeping a buffer for unplanned work (state the percentage and its basis). Flag items that serve the goal versus independent necessary work.
7. Break the top selected items into tasks of at most about one day each, with an owner candidate and an explicit "done" check per task; leave the rest for the first days if time is short.
8. Identify risks and dependencies: external teams, environments, skills concentrated in one person, unclear acceptance criteria.
9. Run a confidence vote (e.g. fist of five). If confidence is low, remove scope rather than stretch capacity, and record what was removed.
10. Write the plan in the output format, separating what the team stated from what you inferred.
11. If the user's goal continues, suggest `task-breakdown` for deeper decomposition, `estimation-session` for unsized items, or `iteration-review-prep` later in the iteration.

## Output format
```markdown
# Iteration Plan: <iteration name/number> (<start> – <end>)
**Goal:** <one sentence outcome>
**Confidence:** <vote result or [TBD]>

## Capacity
| Member | Available days | Recurring load | Net capacity |
|---|---|---|---|
| Total | | | <n> – focus factor <x> [ASSUMPTION] |
Historical reference: <median throughput/velocity or [UNKNOWN]>
Buffer for unplanned work: <%> – <basis>

## Selected Items
| # | Item | Size | Serves goal? | Owner candidate | Risk |
|---|---|---|---|---|---|

## Not Selected / Not Ready
- <item> – <reason: capacity / fails DoR: missing ...>

## Task Breakdown (top items)
- <item>: <task> – <done check>

## Risks and Dependencies
- [RISK] ... – <mitigation / owner>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- <question> – <who answers>
```

## Quality checklist
- [ ] Capacity is derived from stated availability, and every factor not supplied is marked `[ASSUMPTION]`.
- [ ] Selection does not exceed the capacity ceiling, and a buffer is explicit.
- [ ] The goal is an outcome, and each selected item is marked as serving it or not.
- [ ] Items failing the Definition of Ready are not silently included.
- [ ] Each task has a verifiable done check.
- [ ] No historical metrics, dates or names are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Planning at 100% capacity. Unplanned work always arrives; reserve a buffer based on the team's recent interrupt rate.
- Using velocity as a target. It is a planning input; pushing it up inflates estimates, not output.
- Assigning every task up front. Assign only what must be parallelized; let the team pull the rest.
- Accepting a goal that is a ticket list. It removes the basis for scope trade-offs mid-iteration.

## Example
Input: "6 devs, 10-day sprint, Ayşe on leave 3 days, release freeze on day 10, last velocities 34, 28, 31. Top items attached."

Excerpt of output:
- Capacity: 57 person-days minus ~1 day/person meetings and support = 51; focus factor 0.7 `[ASSUMPTION]` → ~36 ideal days. Historical median velocity 31 points → plan to about 28-31 points with a 10% buffer.
- Not ready: "Invoice PDF redesign" – no acceptance criteria.
- [RISK] Day-10 freeze: anything needing deployment must be done by day 9.
