---
name: cycle-time-analysis
description: "Analyzes cycle time and lead time from work item start/finish dates: computes percentiles, reads the distribution, finds bottleneck states from time-in-state data, flags aging work in progress against the historical percentiles and proposes a service level expectation. Use when someone shares item start/end dates or board state history and asks how long work takes, where it waits or which items are at risk of getting stuck."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Analyze cycle/lead time"
  related: "wip-policy, monte-carlo-forecast, velocity-analysis, value-stream-map, engineering-metrics-review"
  prompt: "Here are 40 finished items with start and done dates and 9 items in progress with their start dates. How long does our work take and what is stuck?"
---

# Analyze Cycle/Lead Time

## Purpose
Turn raw item timestamps into a truthful picture of how long work takes, where it waits and which in-progress items are drifting, so the team can make percentile-based commitments and act on aging work before it becomes late.

## When to use
- The team or a stakeholder asks "how long does a typical item take?" or wants a service level expectation (SLE).
- Delivery feels slow and the team wants to know which state or handoff causes the delay.
- A regular flow review needs an aging-WIP check.

## When not to use
- Forecasting how many items or which date for a batch of work. Use `monte-carlo-forecast`.
- Analyzing points delivered per iteration. Use `velocity-analysis`.
- Mapping the end-to-end process including non-team steps. Use `value-stream-map`.

## Inputs
Required:
- For finished items: start date and finish date (or state transition history). At least ~15 items; state the definitions of "start" and "finish" used.

Optional, improves quality:
- Time-in-state history per item (e.g. analysis, development, review, test, waiting for deployment).
- Currently in-progress items with start date and current state.
- Item type, class of service, size, blocked periods.
- Created date, to compute lead time (created → done) in addition to cycle time (started → done).

If start/finish definitions are unclear, ask one question to settle them; without them numbers are not comparable. With fewer than ~15 items mark every percentile `[LOW CONFIDENCE]`.

## Process
1. Fix the definitions: cycle time = start of active work to done; lead time = request created/committed to done. Choose day-counting (calendar days, inclusive: same-day finish = 1) and state it.
2. Clean the data: remove items with missing dates, flag negative or zero-duration anomalies, separate cancelled items, and note reopened items. Report how many were excluded and why.
3. Compute the distribution: count, median (P50), P70, P85, P95, min, max. Show the calculation method (nearest-rank on sorted values). Do not use the mean as the headline; cycle time is right-skewed.
4. Read the shape: long tail (a few items take much longer), bimodal (two kinds of work mixed; split by type), or tight. If types differ, compute percentiles per type or class of service.
5. Find bottlenecks from time-in-state: total and median time per state, split into active states and wait states (queues, "ready for review", "waiting for deploy"). Compute flow efficiency = active time / total time when both are available; label it `[ESTIMATE]` if wait states are not modeled on the board.
6. Check aging WIP: for each in-progress item compute age so far and compare with P50/P85 of finished items. Flag items above P85 as "at risk" and above P95 as "stuck".
7. Look for trends: compare the last 4-6 weeks with the earlier period; a rising P85 often signals growing WIP or batch size.
8. Propose an SLE: "85% of <type> items finish within N days", based on P85, with the sample period.
9. Recommend 2-4 actions tied to evidence: swarm on the oldest items, limit WIP in the bottleneck state (`wip-policy`), split large items, remove a handoff or queue.
10. Hand off: suggest `wip-policy` to act on bottlenecks and `monte-carlo-forecast` for delivery forecasts; list open data questions.

## Output format
```markdown
# Cycle/Lead Time Analysis – <team>, <period>
Definitions: start = <...>, finish = <...>, calendar days inclusive
Sample: <n> finished items (<excluded n> excluded: <reasons>)

## Distribution
| Metric | Cycle time | Lead time |
|---|---|---|
| P50 / P70 / P85 / P95 | | |
| Min / Max | | |
Shape: <tight / long tail / bimodal> – <evidence>

## Time in State
| State | Type (active/wait) | Median days | Share of total |
|---|---|---|---|
Flow efficiency: <x%> [ESTIMATE if applicable]
Bottleneck: <state> – <evidence>

## Aging WIP
| Item | State | Age (days) | vs P85 | Flag |
|---|---|---|---|---|

## Service Level Expectation
<85% of <type> items finish within N days (sample period)>

## Actions
1. <action> – <evidence> – <owner role>

## Data Caveats and Open Questions
- ...
```

## Quality checklist
- [ ] Start/finish definitions and day-counting rule are stated.
- [ ] Percentiles are headline metrics; the mean is not used as the typical value.
- [ ] Excluded or anomalous items are counted and explained.
- [ ] Every in-progress item is compared with the historical percentiles.
- [ ] Bottleneck claims are backed by time-in-state data or labeled `[INFERENCE]`.
- [ ] Individual performance is not ranked; the analysis is about the system of work.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mixing work types (defects, features, support) in one distribution. Split them when the shape is bimodal.
- Looking only at finished items. Aging WIP is the leading indicator; finished-item percentiles lag.
- Treating the board's states as the real process. If waiting is hidden inside "In progress", flow efficiency is overstated; say so.

## Example
Input: 40 finished items, cycle times sorted: 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, ... 14, 18, 27; 9 items in progress.

Excerpt of output:
- P50 = 4 days, P85 = 11 days, P95 = 18 days; long tail driven by 3 items blocked on an external API `[stated]`.
- Bottleneck: "Ready for review" median 2.5 days, 38% of total time – wait state.
- Aging WIP: ITEM-212 in Test for 14 days (> P85) → at risk; swarm today.
- SLE: 85% of stories finish within 11 days (sample: last 12 weeks).
