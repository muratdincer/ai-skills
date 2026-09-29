---
description: Decomposes an epic into thin, vertical, independently valuable stories with a specific persona, a real outcome and a walking-skeleton first slice, ordered by value, risk and dependency. Use when an epic, initiative or large feature must become backlog items, when stories keep coming out as layers (UI/API/DB) or technical tasks, or when a team asks "how do we split this epic".
related: story-splitting, user-story, acceptance-criteria, story-mapping, invest-check
prompt: Break this epic into stories: "Self-service contract renewal for SME customers in the customer portal".
---

# Break an Epic Into Stories

## Purpose
Turn one epic into a set of thin vertical slices, each delivering observable value to a named user, so the team can ship, learn and reorder early instead of integrating everything at the end.

## When to use
- An epic or initiative is approved and must enter the backlog as workable items.
- Existing breakdowns are horizontal (frontend story, backend story, database story) or mostly technical tasks.
- A release needs a first slice that proves the end-to-end path early.

## When not to use
- A single story is too big and only needs splitting. Use `story-splitting`.
- The whole user journey and release slices must be laid out for several epics. Use `story-mapping`.
- Individual stories need detailed conditions of satisfaction. Use `acceptance-criteria`.

## Inputs
Required:
- The epic: goal, target users and the outcome it should move (or a PRD/feature brief containing them).

Optional, improves quality:
- Business rules, flows, screens, integrations, NFRs, known constraints.
- Team conventions for story format and size; existing related stories.

If the epic's users or goal are missing, ask (at most 3 focused questions). Do not invent business rules; list them as open questions.

## Process
1. Restate the epic as outcome + primary persona + scope boundary. Name specific personas (e.g. "SME account admin"), never "a user"; if persona is not given, propose one and mark `[ASSUMPTION]`.
2. Walk the end-to-end flow the epic enables (trigger, steps, completion) and note the business rules, data and integrations touched at each step.
3. Define the walking skeleton: the thinnest path through every step that a real persona can complete, using the simplest rule, one data variant and the happy path.
4. Grow slices from the skeleton along split axes: workflow steps, rule variations, data variants, interfaces/channels, error and edge paths, performance/quality levels. Each slice must cross all needed layers.
5. Write each story as "As a <specific persona>, I want <capability>, so that <real outcome>". The "so that" states a benefit, not a restatement of the want.
6. Separate technical work: pure technical tasks (set up queue, migrate schema) are tasks under a story or enablers with a stated reason, not user stories. Unknowns large enough to block estimation become time-boxed spikes.
7. Draft 2-4 acceptance scenarios per story in Given/When/Then; one When and one Then per scenario. If a story needs many Whens or Thens, split it.
8. Check every story against INVEST; flag dependencies explicitly and prefer reordering or splitting over coupling.
9. Order stories: skeleton first, then highest value or highest risk reduction, respecting hard dependencies. Mark which stories together form a releasable increment.
10. Check coverage: every rule, data variant and NFR from step 2 lands in a story, an explicit "out of scope", or an open question. Label inferred rules `[ASSUMPTION]`.
11. If the user's goal continues, suggest the next skill: `acceptance-criteria` to detail stories, `story-splitting` for any still-large item, or `story-mapping` to plan releases across epics.

## Output format
```markdown
# Epic Breakdown: <epic name>
Outcome: <metric/behaviour to move> · Primary persona: <persona> · Boundary: <in / out>

## End-to-End Flow
<step 1> → <step 2> → ... (rules / data / integrations noted per step)

## Stories
| # | Story (As a / I want / so that) | Slice type | Key scenarios | Depends on | Size signal |
|---|---|---|---|---|---|
| 1 | <walking skeleton> | Skeleton | ... | – | S/M/L or [TBD] |

## Enablers, Tasks and Spikes
| Item | Type | Reason / linked story | Time-box |
|---|---|---|---|

## Suggested Order and Release Increments
- Increment 1: #1, #2 – <what a user can now do>

## Coverage and Out of Scope
- Rules/NFRs covered: ... · Explicitly out: ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every story names a specific persona and a "so that" that states a real outcome.
- [ ] Every story is vertical (usable by the persona); no story is a layer or a pure technical task.
- [ ] The first story is a walking skeleton that completes the end-to-end flow.
- [ ] Each scenario has one When and one Then; multi-behaviour stories were split.
- [ ] Every rule, variant and NFR from the flow is mapped to a story, out of scope or an open question.
- [ ] Sizes come from the team or are `[TBD]`; nothing is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
| Pitfall | Fix |
|---|---|
| Splitting by layer (UI, API, DB) | Split by workflow, rule or data so each slice crosses layers |
| "As a user..." | Name the persona whose behaviour changes |
| "so that I can renew" (repeats the want) | State the benefit: "so that service is not interrupted" |
| Gold-plating the first slice | Keep the skeleton to happy path, one rule, one variant |

## Example
Input: "Self-service contract renewal for SME customers in the customer portal."

Weak: "As a user, I want a renewal page, so that I can renew." / "Build renewal API."

Strong excerpt:
| # | Story | Slice type |
|---|---|---|
| 1 | As an SME account admin, I want to renew my current contract unchanged with one confirmation, so that service continues without calling sales | Skeleton |
| 2 | As an SME account admin, I want to change the seat count during renewal, so that I pay only for active staff | Data variant |
| 3 | As an SME account admin, I want to be told why renewal is blocked for overdue invoices, so that I can resolve it myself | Rule / error path |
- Enabler: expose contract end dates from billing to the portal (linked to #1).
- Open question: may renewal change the price plan, or only quantities?
