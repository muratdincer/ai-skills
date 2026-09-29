---
description: "Splits a large user story or work item into thin, independently valuable vertical slices using named patterns (workflow step, business rule, data variation, interface, operation, happy/unhappy path, spike) and shows acceptance criteria and a suggested order for each slice. Use when a story is too big for one iteration/sprint, estimates are wide, or someone asks to break down, slice or split a story."
related: "epic-breakdown, invest-check, backlog-refinement, acceptance-criteria, user-story"
prompt: "This story is 21 points and nobody trusts the estimate: 'As a customer I want to pay my invoice online.' Split it."
---

# Split Large Stories

## Purpose
Turn one oversized item into several small slices, each delivering observable value end to end, so the team can finish, test and get feedback within short cycles and reduce estimation risk.

## When to use
- A story cannot plausibly be finished within one iteration/sprint or a few days of flow.
- The team's estimates for an item diverge widely or hide "we'll see" work.
- A story mixes several user roles, rules or channels.
- Early feedback is needed before the full feature is built.

## When not to use
- The input is an epic or feature needing a first-level breakdown into many stories. Use `epic-breakdown` or `story-mapping`.
- The story is small but badly written. Use `user-story` or `invest-check`.
- Only technical tasks are needed for a ready story. Use `task-breakdown`.

## Inputs
Required:
- The story or item text, with any acceptance criteria.

Optional, improves quality:
- Current estimate and team's typical story size.
- Business rules, user roles, channels, data variants involved.
- Known technical risks or unknowns.

If the story text is missing, ask for it.

## Process
1. Restate the story's core value in one line and list the acceptance criteria, rules, roles, channels and data variants it implicitly contains.
2. Identify the unknowns; if a major technical or domain question blocks sizing, propose a timeboxed spike slice with a concrete question and exit criterion.
3. Try the patterns in this order and keep the ones that yield meaningful slices:
   - Workflow steps (do the simplest end-to-end path first, enrich later).
   - Business rule variations (one rule per slice).
   - Happy path vs error/exception handling.
   - Data variations (one data type, currency, file format at a time).
   - Interface/channel (web first, then mobile, then API).
   - Operations (create/read/update/delete separately).
   - Defer performance or scale ("works for 100 records" before "for 1M").
4. Reject horizontal slices (UI only, database only, "backend story"); each slice must be demonstrable to a user or testable through an interface.
5. Write each slice as a story with 2-5 acceptance criteria. Make sure the original acceptance criteria are all covered by the union of the slices.
6. Check each slice against INVEST, especially Independent, Valuable and Small; note deliberate dependencies.
7. Propose an order: the slice that tests the riskiest assumption or delivers the walking skeleton first.
8. Name slices that could be dropped entirely if feedback shows low value.
9. If the user's goal continues, suggest `invest-check` to validate each slice and `acceptance-criteria` to write criteria for the retained slices.

## Output format
```markdown
# Story Split: <original story title>
Original: <story text>
Core value: <one line>
Patterns used: <pattern list>

| # | Slice | Pattern | Acceptance criteria (short) | Depends on | Could drop? |
|---|---|---|---|---|---|
| 1 | <story> | <pattern> | <AC1; AC2> | – | No |

## Spike (if needed)
- Question: <what must be learned>
- Timebox: <duration>
- Exit: <evidence that answers it>

## Coverage Check
| Original AC | Covered by slice |
|---|---|

## Suggested Order and Rationale
1. <slice> – <why first>
```

## Quality checklist
- [ ] Every slice is vertical and delivers something a user or tester can observe.
- [ ] All original acceptance criteria map to at least one slice.
- [ ] The first slice is a thin end-to-end path, not a component.
- [ ] Spikes have a question, a timebox and an exit criterion.
- [ ] No estimates are invented; sizing is left to the team or marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Splitting by layer or by team ("frontend story", "API story"). This defers value and integration risk; slice by behavior instead.
- Creating a "part 2: polish" slice that is really unfinished work. Each slice must meet the Definition of Done on its own.
- Splitting so finely that slices have no user value (e.g. "add a field"). Merge back to the smallest valuable behavior.

## Example
Input: "As a customer I want to pay my invoice online."

Excerpt of output:
| 1 | Pay a single invoice in full by card | Workflow (simplest path) | Payment confirmed; invoice marked paid | – | No |
| 2 | Handle declined card with retry | Happy/unhappy path | Clear error; no duplicate charge | 1 | No |
| 3 | Pay multiple invoices at once | Data variation | Total shown; each invoice marked | 1 | Yes |
| 4 | Pay by bank transfer | Rule/channel variation | Reference number generated | 1 | Yes |
- Spike: Does the payment provider support 3-D Secure in our checkout flow? Timebox 2 days.
