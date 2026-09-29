---
description: "Interprets burndown and burnup charts or their underlying daily data for an iteration or release: reads the shape, separates progress from scope change, detects patterns such as late drops, flat lines and scope creep, and flags risks with recommended actions. Use when someone shares a burndown/burnup chart, daily remaining-work numbers or asks whether an iteration or release is on track."
related: "velocity-analysis, monte-carlo-forecast, daily-sync-summary, iteration-planning, project-status-report"
prompt: "Day 7 of 10 in our sprint. Remaining points by day: 40, 40, 38, 38, 38, 35, 35. Two stories were added on day 4. Are we going to make it?"
---

# Read Burndown/Burnup Charts

## Purpose
Explain what a burndown or burnup actually says about the likelihood of reaching the iteration or release goal, distinguish real progress from scope movement, and turn the reading into concrete actions early enough to matter.

## When to use
- Mid-iteration or mid-release check: "are we on track?".
- A chart has an unusual shape (flat, stepped, rising) and someone wants an interpretation.
- Preparing a status message that needs an evidence-based progress statement.

## When not to use
- Analyzing delivery rate across many iterations. Use `velocity-analysis`.
- Forecasting a completion date with probabilities. Use `monte-carlo-forecast`.
- Diagnosing why individual items take long. Use `cycle-time-analysis`.

## Inputs
Required:
- The chart or the daily/periodic series of remaining work (burndown) or completed and total scope (burnup), plus the period length and current day.

Optional, improves quality:
- Scope changes with dates, the iteration/release goal.
- Unit (points, items, hours) and whether items count only when fully done.
- Known events (holidays, incidents, blocked items).

If the data or current day is missing, ask. Do not read values off an image you cannot see clearly; ask for the numbers.

## Process
1. Restate the data as a table per day/period: remaining (or done), total scope, ideal line value. Note the unit and counting rule.
2. Separate scope change from progress: for each period, completed = previous remaining − current remaining + scope added. Show scope changes explicitly; prefer a burnup view when scope moves.
3. Compare actual to ideal: gap in units and as a percentage of the original commitment at the current day.
4. Identify the pattern and its usual causes:
   - Flat for several days: work not finishing, large items, blocked work, or board not updated.
   - Late cliff: items too large or done only at the end; testing batched.
   - Rising line: scope added faster than completed.
   - Steady but above ideal: overcommitment or underestimation.
   - Ahead of ideal early: possible under-commitment or easy items first.
5. Project the finish: using the average completion rate of the last few periods, estimate remaining at the end. Present it as a range and label it `[PROJECTION]`.
6. Assess goal risk: will the goal-critical items finish even if not all items do? Use the goal, not the total, as the yardstick.
7. List 2-4 actions sized to the time left: swarm on the oldest item, split or drop scope with the product owner, remove a blocker, stop starting new items.
8. Note data-quality issues (hours re-estimated daily, partial credit, stale board) that make the chart unreliable.
9. If the user's goal continues, suggest `daily-sync-summary` to address blockers with the team or `velocity-analysis` / `monte-carlo-forecast` for release-level forecasting.

## Output format
```markdown
# Burndown Reading – <iteration/release>, day <n> of <m>
Unit: <...> · Goal: <goal or [UNKNOWN]>

| Day | Remaining | Scope | Ideal | Completed that day | Scope added |
|---|---|---|---|---|---|

**Status:** On track / At risk / Off track
**Pattern:** <name> – <evidence>
**Projection at end:** <range> remaining [PROJECTION]
**Goal risk:** <which goal-critical items are at risk>

## Actions
1. <action> – <owner role> – <by when>

## Data Caveats
- ...
```

## Quality checklist
- [ ] Scope change and completed work are shown separately.
- [ ] The status is based on the gap to ideal and the projection, with numbers shown.
- [ ] The pattern is named with evidence and plausible causes, and inferred causes are labeled.
- [ ] Goal risk is assessed separately from total scope.
- [ ] Actions are feasible in the remaining time.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reading a flat line as "no work done". It often means work is in progress but not finished; check items in progress and their age.
- Hiding scope creep inside a burndown. When scope moves, switch to a burnup so it becomes visible.
- Treating the ideal line as a target. It is a reference; deviation is information, not failure.

## Example
Input: 10-day sprint, day 7; remaining 40, 40, 38, 38, 38, 35, 35; two stories (+5) added on day 4.

Excerpt of output:
- Completed so far: 40 + 5 − 35 = 10 points in 7 days (~1.4/day). Ideal remaining at day 7: 12.
- Pattern: mostly flat with scope added – work not finishing plus scope creep.
- Projection: ~31 points remaining at day 10 `[PROJECTION]` → Off track.
- Action: with the product owner, agree today which goal-critical stories remain and move the day-4 additions out.
