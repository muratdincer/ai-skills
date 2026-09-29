---
name: monte-carlo-forecast
description: "Produces a probabilistic delivery forecast from historical throughput using Monte Carlo simulation: answers 'when will N items be done?' or 'how many items by date D?' with confidence levels (50/85/95%), accounts for backlog growth and splitting, and explains the method and caveats. Use when someone shares weekly or per-iteration throughput and asks for a release date, a scope forecast for a deadline, or the probability of hitting a commitment."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Forecast delivery with Monte Carlo"
  related: "velocity-analysis, cycle-time-analysis, release-planning, burndown-analysis, schedule-plan"
  prompt: "Our weekly throughput for the last 12 weeks: 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5. We have 38 items left. When can we be done with 85% confidence?"
---

# Forecast Delivery with Monte Carlo

## Purpose
Replace single-point dates with honest probability-based answers derived from the team's own delivery history, so stakeholders can choose a commitment level knowingly and see how scope growth changes the picture.

## When to use
- A release date or a deadline scope needs a forecast with explicit confidence.
- Stakeholders ask "what is the probability we hit date D?".
- Estimates in points are distrusted or unavailable, but item counts per period exist.

## When not to use
- Understanding trend and variability of past delivery. Use `velocity-analysis`.
- Forecasting a single item's duration. Use the percentiles from `cycle-time-analysis`.
- Building a task-level schedule with dependencies. Use `schedule-plan`.

## Inputs
Required:
- Throughput history: items finished per week (or per iteration), at least ~8 periods, from a period whose team and process resemble the future.
- The question: remaining item count (for "when") or a target date (for "how many").

Optional, improves quality:
- Expected backlog growth or split rate (e.g. items typically split into 1.3 pieces once started).
- Planned capacity changes (holidays, team changes) in the forecast window.
- Start date of the forecast.

If fewer than ~8 periods exist, forecast anyway but label the result `[LOW CONFIDENCE]`. Never invent throughput values; if data is missing, ask.

## Process
1. Validate the sample: same team, same definition of "finished", item sizes of similar kind (right-sized, not homogeneous). Remove periods broken by known one-off events only if the user confirms they will not recur; state removals.
2. Adjust the remaining scope: remaining × split factor + expected growth. If unknown, show the forecast for the raw count and for a `[ASSUMPTION]` growth band (e.g. +10-25%).
3. Describe the simulation: each trial draws a random period from the history (with replacement) repeatedly until the remaining scope is consumed ("when") or until the date is reached ("how many"). Run many trials (e.g. 10,000).
4. If you cannot execute code, produce the forecast by a transparent approximation: compute percentiles of the sampled sum via the bootstrap reasoning or give the calculation as a small script/spreadsheet formula for the user to run, and label the numbers `[APPROXIMATION]`. Never present made-up simulation output as run.
5. Report "when" results as percentiles of periods needed: 50%, 85%, 95%. Convert periods to calendar dates from the start date, accounting for known capacity gaps.
6. Report "how many" results inversely: the count achieved with at least 85% and 95% probability (the lower tail), plus 50%.
7. Add a sanity check: remaining ÷ median throughput should be near the 50% result; explain large differences.
8. Explain sensitivity: which factor moves the date most (growth, zero-throughput weeks, split rate) and what would change the forecast.
9. State the refresh rule: re-run the forecast every period with new data; a forecast is a snapshot, not a commitment.
10. Suggest `release-planning` to translate the chosen confidence into a plan or `velocity-analysis` if the history looks unstable.

## Output format
```markdown
# Monte Carlo Forecast – <team/release>
Question: <when will N items be done / how many by D>
History: <n periods, dates>, throughput <list> · Trials: <n> · Method: <simulated / [APPROXIMATION]>
Scope used: <raw> → <adjusted> (<split factor, growth [ASSUMPTION]>)

| Confidence | Periods needed / Items done | Calendar date |
|---|---|---|
| 50% | | |
| 85% | | |
| 95% | | |

Sanity check: <remaining ÷ median throughput = ...>
Sensitivity: <main drivers>
Caveats: <sample quality, capacity changes, [LOW CONFIDENCE] if applicable>
Refresh: <cadence>
```

## Quality checklist
- [ ] The answer is a set of confidence levels, never one date.
- [ ] The history period and its representativeness are stated.
- [ ] Scope growth or splitting is either included or explicitly excluded.
- [ ] It is clear whether numbers come from an executed simulation or an approximation.
- [ ] For "how many" questions, the lower tail is used for high confidence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reading the "how many" distribution from the wrong tail. 85% confidence means at least that many items in 85% of trials, which is a lower number than the median.
- Forecasting fixed scope while the backlog keeps growing. Include growth or the date will slip every week.
- Using history from a different team or process. The model is only as good as the sample's similarity to the future.

## Example
Input: weekly throughput 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5 (median 4); 38 items left; start Monday of week 1.

Excerpt of output:
- Sanity check: 38 ÷ 4 ≈ 9.5 weeks at the median.
- 50%: 10 weeks · 85%: 11-12 weeks · 95%: 13 weeks `[APPROXIMATION]` (script provided to confirm).
- With +20% growth `[ASSUMPTION]` (46 items): 85% moves to ~13-14 weeks.
- Weak statement: "We'll be done in 9 weeks." Strong: "85% likely within 12 weeks if scope stays at 38 items."
