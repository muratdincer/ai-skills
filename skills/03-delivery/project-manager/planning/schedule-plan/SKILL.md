---
name: schedule-plan
description: "Builds a project schedule by sequencing work packages with dependency types and lags, assigning durations, setting milestones, calculating the critical path and float, and adding schedule buffers. Use when a WBS and estimates exist and a baseline timeline, critical path or realistic end date must be produced or checked."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Build a project schedule"
  related: "wbs, estimation-three-point, dependency-map, resource-plan, release-planning"
  prompt: "Build a schedule from these work packages and durations and show me the critical path to the June go-live."
---

# Build a Project Schedule

## Purpose
Produce a realistic, dependency-driven timeline that shows the critical path, float and milestones, so that the end date is derived from the work rather than wished into the plan.

## When to use
- After the WBS and estimates exist, to create the schedule baseline.
- A fixed date is given and feasibility must be tested.
- A delay occurred and the impact on milestones must be recalculated.

## When not to use
- Release content planning across iterations. Use `release-planning`.
- Probabilistic date forecasting from throughput. Use `monte-carlo-forecast`.
- Only mapping who depends on whom. Use `dependency-map`.

## Inputs
Required:
- Work packages or activities with duration estimates.
- Known dependencies or enough description to infer them (inferred ones are marked `[ASSUMPTION]`).

Optional, improves quality:
- Start date, calendars and holidays, fixed milestones, resource constraints, three-point estimates.

If activities or durations are missing, ask for them. Do not invent durations.

## Process
1. Convert work packages into activities; keep one owner and a duration per activity.
2. Define dependencies with type (FS, SS, FF, SF) and lead/lag; prefer FS and justify others. Separate hard logic (technical) from soft logic (preference).
3. Add milestones (zero duration) for decisions, gates, external deliveries and go-live.
4. Apply calendars: working days, holidays, freeze periods, vendor lead times.
5. Run a forward and backward pass; compute early/late start and finish and total float.
6. Identify the critical path(s) and near-critical activities (float ≤ 5 working days, adjustable).
7. Check resource conflicts on the critical path; if levelling is needed, note the date impact.
8. Add explicit buffers (project or feeding buffers) instead of padding each task, sized from estimate uncertainty.
9. If a target date is missed, propose compression options: fast-tracking (risk) and crashing (cost), with trade-offs.
10. Produce the milestone table, critical path summary and key schedule risks.
11. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `resource-plan` to check the schedule against capacity, or `dependency-map` for external dependencies.

## Output format
```markdown
# Project Schedule: <project>
Start <date> | Calendar <working days, holidays> | Baseline v<x>
## Activities
| ID | Activity | Owner | Duration | Predecessors (type+lag) | ES | EF | LS | LF | Float |
## Milestones
| Milestone | Planned date | Type (gate/external/go-live) |
## Critical Path
<ID → ID → ID>, total duration <x>
## Near-Critical Activities
## Buffers
## Compression Options (if target missed)
| Option | Activities | Days gained | Cost / risk |
## Schedule Risks and Assumptions
```

## Quality checklist
- [ ] Every activity except start/finish has a predecessor and a successor (no dangling tasks).
- [ ] No hard-coded dates except true constraints, which are listed.
- [ ] Critical path is shown and explained.
- [ ] Inferred dependencies and durations are marked `[ASSUMPTION]`.
- [ ] Buffers are explicit, not hidden in activity durations.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Scheduling to a mandated date backwards and calling it a plan. Derive the date, then compare.
- Ignoring resource constraints, making the critical path look shorter than it is.
- Forgetting external lead times (procurement, security approvals, environment provisioning).

## Example
Input: "Design 10d, build 25d after design, test 15d after build, data migration 20d starting with build, go-live after test and migration."

Excerpt of output:
- Critical path: Design → Build → Test → Go-live = 50 working days.
- Migration float: 20 days (SS with Build, must finish before go-live).
- Risk: test environment provisioning lead time `[UNKNOWN]` sits on the critical path.
