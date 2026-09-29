---
description: Builds a program roadmap that sequences the work of several teams or projects toward shared outcomes, showing cross-team milestones, integration points, decision gates and the critical path, with confidence levels instead of false precision. Use when a program spans multiple teams or vendors, when leadership needs one view of how parallel workstreams converge, or when someone asks for a program-level plan, timeline or integrated roadmap.
related: cross-team-dependency-board, portfolio-prioritization, roadmap, release-planning, schedule-plan
prompt: Build a program roadmap for our core banking migration: 5 teams, a vendor, and a regulatory go-live in Q4.
---

# Build a Program Roadmap

## Purpose
Give sponsors and team leads a single, honest view of how multiple workstreams move toward the program outcome: what each delivers when, where they must meet, which gates decide continuation, and how confident the dates are.

## When to use
- A program spans several teams, projects or vendors that must deliver together.
- A fixed external date (regulatory, contractual, market event) must be met by converging workstreams.
- Leadership or the steering committee needs one integrated timeline instead of separate team plans.

## When not to use
- One product team plans its own releases. Use `roadmap` or `release-planning`.
- Detailed task scheduling for a single project is needed. Use `schedule-plan`.
- The main need is negotiating and tracking specific dependencies. Use `cross-team-dependency-board`.

## Inputs
Required:
- The program goal or outcome and any fixed dates.
- The workstreams or teams involved and what each is expected to deliver.

Optional, improves quality:
- Team plans, capacity, forecasts or throughput data.
- Known dependencies, shared environments, vendor contracts and lead times.
- Governance gates, release windows, freeze periods, business calendars.
- Risks and assumptions already logged.

If the goal or workstreams are missing, ask. Unknown dates stay `[TBD]`; never invent them.

## Process
1. State the program outcome and success measures, plus fixed constraints (external deadlines, freeze periods, budget horizons). Label inferred items `[ASSUMPTION]`.
2. Define workstreams (swimlanes) and their owners. Each workstream's deliverables should be outcome-oriented increments, not activity lists.
3. Choose the time granularity that matches certainty: months or quarters for the far horizon, iterations or weeks for the next period. Use Now/Next/Later bands if dates are genuinely uncertain.
4. Place each workstream's major deliverables with a confidence level (High/Medium/Low) and the basis for the date (team forecast, vendor commitment, estimate, target).
5. Identify integration points: where one workstream's output is another's input, shared environments, end-to-end tests, data migrations, cutover rehearsals. Give each an ID, a date and both owners.
6. Define program milestones and decision gates (e.g. design complete, integration test entry, go/no-go) with explicit entry criteria.
7. Trace the critical path through dependencies and integration points to the fixed date; compute or estimate float and name where there is none.
8. Stress-test against capacity and calendars: overlapping peaks on shared teams, holiday and freeze periods, vendor lead times. Record conflicts rather than hiding them.
9. List top risks to the roadmap with owner and mitigation, and the assumptions the dates rest on.
10. Set the update rhythm and ownership: who updates which lane, how often, and what change needs steering approval.
11. If the goal continues, suggest `cross-team-dependency-board` to manage dependencies, `steering-committee-pack` to present it, or `governance-framework` to define the gates.

## Output format
```markdown
# Program Roadmap: <program> — v<n> (<date>)
Outcome: <goal + measures> · Fixed dates: <list>

## Timeline
| Workstream / owner | <period 1> | <period 2> | <period 3> | <period 4> |
|---|---|---|---|---|
| <team A> | <deliverable> (H) | ... | ... | ... |
| Program milestones | ◆ M1 <name> | ... | ◆ Gate G2 | ◆ Go-live |

## Integration Points
| ID | From → To | What is exchanged / tested | Date | Owners | Confidence |
|---|---|---|---|---|---|

## Milestones and Gates
| ID | Milestone / gate | Entry criteria | Date | Decision owner |
|---|---|---|---|---|

## Critical Path
<chain> · Float: <value or none>

## Capacity and Calendar Conflicts
## Risks and Assumptions
- [RISK] ... — owner — mitigation
- [ASSUMPTION] ...
## Update Rhythm and Change Control
```

## Quality checklist
- [ ] Every deliverable and integration point has an owner, a date or `[TBD]`, and a confidence level with its basis.
- [ ] Integration points name both sides and what is exchanged or tested.
- [ ] Gates have explicit entry criteria and a decision owner.
- [ ] The critical path to each fixed date is shown with float or its absence.
- [ ] Capacity and calendar conflicts are recorded, not smoothed over.
- [ ] No invented dates; inferences are labeled and listed as assumptions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Stitching team plans together without integration points. The risk of a program lives between teams; make every handoff explicit.
- Showing far-future dates with the same precision as next month. Use coarser bands and confidence levels further out.
- Putting integration and end-to-end testing at the very end. Plan early integration milestones so problems surface while there is still float.

## Example
Input: "Core banking migration: 5 teams + vendor, regulatory go-live in Q4."

Excerpt of output:
| ID | From → To | What is exchanged / tested | Date | Confidence |
|---|---|---|---|---|
| IP-03 | Vendor core → Payments team | Payment API on test environment | end of Q2 `[TBD]` | Low (vendor commitment not signed) |
| IP-05 | Data team → All | Full migration rehearsal #1 | mid Q3 | Medium |

Critical path: vendor API (IP-03) → payments integration → E2E test → go/no-go. Float: about 3 weeks `[ASSUMPTION]`; any vendor slip beyond that threatens the regulatory date.
