---
description: Cuts a product or feature scope down to the smallest release that tests the riskiest value assumption with real users, using an assumption-led cut, a must/later/never scope table, explicit quality floor, learning goals and exit criteria. Use when a scope is too big for the available time, when someone asks "what is our MVP", or when a team must decide what to leave out of a first release.
related: hypothesis-statement, story-mapping, prd-writing, assumption-mapping, release-planning
prompt: We have 8 weeks and a 40-item feature list for a field-service scheduling app; help me scope the MVP.
---

# Scope an MVP

## Purpose
Define the smallest coherent release that delivers real value to a specific user and produces the learning needed for the next investment decision, with a clear list of what is deliberately left out and why.

## When to use
- The wish list clearly exceeds the time, budget or team capacity.
- A new product or major feature needs a first release that validates demand or value.
- Stakeholders disagree about what the first release must contain.

## When not to use
- The team only needs to test a single assumption without building a product. Use `hypothesis-statement` and `experiment-design`.
- Scope is agreed and needs release slices across the user journey. Use `story-mapping` or `release-planning`.
- Requirements for an agreed scope must be written. Use `prd-writing`.

## Inputs
Required:
- The product or feature idea, the target user segment and the candidate feature list (or enough description to derive one).

Optional, improves quality:
- Time/capacity constraint, deadline reason, launch audience (internal, beta, public).
- Evidence and known risks; regulatory or contractual must-haves.
- Existing story map or PRD.

If the target user or feature list is missing, ask. Do not invent capacity or estimates; mark them `[TBD]`.

## Process
1. Name the single primary user and the one job the MVP must get done end to end; secondary users are deferred unless the job fails without them.
2. List the riskiest assumptions (value, usability, feasibility, viability) and choose the 1-3 the MVP must answer; state these as learning goals.
3. Map the minimum end-to-end flow for that job (typically 4-8 steps); every step needs at least a basic solution, even if manual (concierge, admin tool, spreadsheet).
4. Classify every candidate item as Must (the job fails or learning goal cannot be measured without it), Later (improves but is not needed to learn), Never/Not now (off strategy); record the one-line reason for each Must.
5. Challenge each Must: can it be manual, narrower (one platform, one region, one integration), or faked behind the scenes? Replace with the cheapest version that keeps the job working.
6. Keep non-negotiables separate: security, privacy (KVKK/GDPR if personal data), legal, accessibility baseline, data integrity. These are the quality floor, not optional scope.
7. Define instrumentation needed to measure the learning goals; an MVP without measurement does not count.
8. Check fit against capacity only with team-provided estimates; if the Must list still does not fit, cut scope further or narrow the audience, never the quality floor.
9. Set exit criteria: the signals that mean scale, iterate or stop, and the date or sample by which to decide.
10. List what is explicitly out, the risks of the cut, and communication points for stakeholders who lose items.
11. If the user's goal continues, suggest the next skill: `story-mapping` to slice the MVP into releasable increments, or `prd-writing` to specify it.

## Output format
```markdown
# MVP Scope: <product/feature>
Primary user: <segment> · Job: <job statement> · Audience: <internal/beta/public>

## Learning Goals
1. <assumption> – measured by <metric/signal>

## Minimum End-to-End Flow
| Step | MVP solution | Manual / narrowed? |
|---|---|---|

## Scope Decisions
| Item | Decision (Must/Later/Never) | Reason |
|---|---|---|

## Quality Floor (non-negotiable)
- ...

## Instrumentation
- ...

## Exit Criteria
| Signal | Threshold | Decision |
|---|---|---|

## Out of Scope, Risks and Stakeholder Notes
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] One primary user and one job are named; the flow covers that job end to end.
- [ ] Every Must has a reason tied to the job or a learning goal.
- [ ] Learning goals are measurable and instrumentation is planned.
- [ ] Security, privacy, legal and data-integrity items are in the quality floor, not cut.
- [ ] Exit criteria define scale / iterate / stop.
- [ ] Capacity fit relies only on provided estimates; missing ones are `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Building one layer at a time (all of the backend, no usable flow). Cut horizontally thin, vertically complete.
- Treating MVP as "version 1 with fewer features" and skipping learning goals. Without a question to answer, there is no signal to act on.
- Cutting quality instead of scope. A buggy MVP tests tolerance for bugs, not the value hypothesis.

## Example
Input: "8 weeks, 40-item list for a field-service scheduling app."

Excerpt of output:
- Primary user: dispatcher at a 10-30 technician company. Job: assign tomorrow's jobs to technicians and let them see their day.
- Learning goal: dispatchers plan the next day in the tool instead of the whiteboard for 4 consecutive weeks.
| Item | Decision | Reason |
|---|---|---|
| Route optimization | Later | Dispatcher orders jobs manually today; not needed to learn |
| Technician mobile day view | Must | Job fails if technicians cannot see assignments |
| Invoicing | Never (now) | Different job; existing accounting tool |
