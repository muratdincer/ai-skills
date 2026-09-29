---
name: wip-policy
description: "Designs a board and its flow policies: columns that mirror the real workflow including wait states, work-in-progress limits per column or person, explicit entry and exit criteria, classes of service, blocked-item and aging rules, and a review cadence for adjusting the limits. Use when a team sets up or redesigns its board, has too much work started and little finished, or asks what WIP limits and pull rules to use."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Define WIP limits and flow policies"
  related: "cycle-time-analysis, working-agreement, definition-of-ready, definition-of-done, impediment-tracking"
  prompt: "We are 6 developers and 1 tester, everything is 'in progress' and nothing finishes. Help us define board columns and WIP limits."
---

# Define WIP Limits and Flow Policies

## Purpose
Make the team's workflow explicit and limit work in progress so that items finish faster and more predictably, with policies clear enough that anyone can tell whether an item may move and what to do when a limit is hit.

## When to use
- A team is creating or redesigning its board.
- Many items are started, few finish, and cycle time is rising.
- Handoffs (review, test, deployment) pile up and nobody knows when to stop starting new work.

## When not to use
- Measuring how long items take or finding the bottleneck from data. Use `cycle-time-analysis` first, then return here.
- Agreeing on general team norms (hours, communication, meetings). Use `working-agreement`.
- Defining what "ready" or "done" means for backlog items. Use `definition-of-ready` or `definition-of-done`.

## Inputs
Required:
- How work currently flows from idea to production (steps, handoffs) and the team composition by skill.

Optional, improves quality:
- Current board columns and a snapshot of item counts per column.
- Cycle time or throughput data, known bottlenecks.
- Work types and urgency levels (defects, expedite requests, fixed-date work).
- Organizational constraints (separate test team, release windows, approvals).

If the workflow is unknown, ask the user to walk through the last finished item step by step; use that as the first draft.

## Process
1. Map the actual workflow from the input, not the ideal one. Include wait states explicitly ("Ready for review", "Ready for test", "Awaiting deploy") so queue time becomes visible. Keep 4-8 columns.
2. Define the commitment point (where the team commits to finish an item) and the delivery point (where it counts as done). Cycle time is measured between them.
3. Write entry and exit criteria for every column as short, checkable statements. Link the first column's entry to `definition-of-ready` and the last exit to `definition-of-done` if they exist.
4. Set initial WIP limits: a common starting heuristic is roughly the number of people who can work in that state, minus pairing; for team-wide limits start near team size and tighten over time `[heuristic]`. Put limits on wait-state pairs (active + ready-for-next) to prevent hidden queues.
5. Define classes of service if work types differ: e.g. standard, fixed date, expedite (max 1 at a time, may exceed limits), intangible/improvement (reserved capacity). State what each may bypass.
6. Write pull rules: pull from right to left; finish or help before starting; when a column is at its limit, swarm on downstream work rather than start new items.
7. Write blocked and aging rules: how to mark blocked items, when blockers are escalated (e.g. same day in the daily sync, to `impediment-tracking` after 1-2 days), and an age threshold (e.g. above the P85 cycle time) that triggers a conversation.
8. Define what happens when a limit is breached: allowed only by explicit team agreement, recorded, and discussed at the next review, not silently.
9. Set a review cadence (e.g. every 2-4 weeks) and the signals used to adjust limits: cycle time percentiles, aging items, idle people, blocked counts. Change one limit at a time.
10. Mark every number and rule not given by the user as `[PROPOSAL]` for team agreement, and suggest `cycle-time-analysis` to validate the effect and `working-agreement` to record the policies with other team norms.

## Output format
```markdown
# Board and Flow Policies – <team>
Commitment point: <column> · Delivery point: <column> · Review cadence: <...>

| Column | Type (active/wait) | WIP limit | Entry criteria | Exit criteria |
|---|---|---|---|---|

## Classes of Service
| Class | When used | Policy (limit, bypass, priority) |
|---|---|---|

## Pull Rules
- ...

## Blocked and Aging Items
- Mark as blocked when ... ; escalate after ...
- Aging threshold: <n days> → <action>

## Limit Breaches
- ...

## Metrics to Watch and Adjustment Rule
- ...

## Open Questions / Proposals to Agree
- [PROPOSAL] ...
```

## Quality checklist
- [ ] Columns reflect the real workflow and make wait states visible.
- [ ] Every column has checkable entry and exit criteria.
- [ ] WIP limits are numbers with a stated rationale, not "keep WIP low".
- [ ] Expedite work has a hard cap so it cannot become the default lane.
- [ ] Blocked, aging and breach rules say who acts and when.
- [ ] Proposals not agreed by the team are marked `[PROPOSAL]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Setting limits so high they never bind. A limit that is never reached changes nothing; start tight enough to trigger conversations.
- Limiting only active columns. Work then piles up in "Done dev / Ready for test"; limit active and wait columns together.
- Per-person limits only. They optimize individual busyness, not flow; prefer column or team limits.

## Example
Input: 6 developers, 1 tester; columns To do / In progress / Done; 17 items in progress.

Excerpt of output:
| Column | Type | WIP limit | Exit criteria |
|---|---|---|---|
| Develop | active | 4 [PROPOSAL] | Code merged, unit tests green |
| Ready for test + Test | wait + active | 3 [PROPOSAL] | Acceptance criteria verified |
- Pull rule: when "Ready for test + Test" is at 3, developers pair on testing before starting new items.
- Weak policy: "Don't take too much work." Strong policy: "Do not pull into Develop while Develop has 4 items; help downstream first."
