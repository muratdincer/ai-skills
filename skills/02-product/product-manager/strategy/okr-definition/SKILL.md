---
description: Writes outcome-based objectives with 2-5 measurable key results each, including baselines, targets, measurement source and owner, and flags output-style or unmeasurable KRs. Use when a team plans a quarter or half-year, when strategy must be turned into measurable goals, or when someone asks to write or review OKRs.
related: product-strategy-one-pager, north-star-metric, kpi-definition, goal-setting, quarterly-planning
prompt: Write Q3 OKRs for our onboarding team based on the goal of getting new customers to value faster.
---

# Define OKRs

## Purpose
Translate strategy into a small set of qualitative objectives and quantitative key results that describe changes in customer or business behavior, so the team can choose its own work and know whether it succeeded.

## When to use
- Quarterly or half-year planning for a product team or product area.
- Strategy or bets exist but teams lack measurable goals.
- Draft OKRs exist and need review for outcome focus and measurability.

## When not to use
- You need ongoing health metrics rather than change goals. Use `kpi-definition`.
- You need the single value metric for the whole product. Use `north-star-metric`.
- You need individual performance goals. Use `goal-setting`.

## Inputs
Required:
- The strategic intent or problem the team should address, and the period.

Optional, improves quality:
- Product strategy, North Star and input metrics, current baselines.
- Team scope and capacity, higher-level OKRs to align with.
- Whether OKRs are committed or aspirational in this organization.

If the intent or period is missing, ask. Unknown baselines become `[UNKNOWN]` with a measurement action.

## Process
1. Restate the strategic intent and identify the customer or business behavior that must change.
2. Write 1-3 objectives: qualitative, inspiring, time-bound by the period, within the team's influence.
3. For each objective draft 2-5 key results as outcomes: "<metric> from <baseline> to <target> by <date>". Avoid "launch X" outputs; if a deliverable is unavoidable, move it to initiatives.
4. Add baseline, target, data source and owner per KR. Missing baseline: `[UNKNOWN]` and add "establish baseline in week 1-2".
5. Balance KRs: pair a growth KR with a quality or guardrail KR (e.g. activation up, support tickets per new account not up).
6. Classify each OKR as committed or aspirational and set the expected scoring (e.g. 0.7 is success for aspirational).
7. List candidate initiatives separately as hypotheses, not as KRs.
8. Check alignment upward (company/strategy) and sideways (dependencies on other teams).
9. Define the check-in cadence and how confidence will be tracked.
10. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `kpi-definition` to specify each KR's formula and source, or `north-star-metric` if the objectives lack a shared value metric.

## Output format
```markdown
# OKRs: <team> — <period>
**Strategic link:** <strategy/bet>

## Objective 1: <qualitative objective>
Type: Committed / Aspirational
| # | Key result | Baseline | Target | Source | Owner |
|---|---|---|---|---|---|
| KR1 | ... | ... | ... | ... | ... |
Guardrail: <metric that must not degrade>
Candidate initiatives: <hypotheses>

## Dependencies
- ...

## Check-in Cadence and Scoring
- ...

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every KR is an outcome with a number, a baseline (or `[UNKNOWN]`) and a date.
- [ ] No KR is a task, launch or deliverable.
- [ ] Each objective has at most 5 KRs and the team has at most 3 objectives.
- [ ] At least one guardrail protects quality or customer trust.
- [ ] Targets are not invented; unagreed targets are `[TBD]`.
- [ ] Each KR has a named data source and owner.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a roadmap as OKRs ("Release v2 onboarding"). Ask "what will change when it ships?" and measure that.
- Choosing metrics the team cannot influence within the period. Pick leading input metrics instead.
- Setting targets without a baseline. Plan a baseline measurement first.

## Example
Input: "Onboarding team, Q3, goal: new customers reach value faster."

Excerpt of output:
- Objective: New customers get to their first successful invoice effortlessly.
- KR1: Median time from signup to first sent invoice from `[UNKNOWN]` to `[TBD]` by end of Q3 (source: product analytics).
- KR2: Share of new accounts activated within 7 days from 38% to 50% `[confirm baseline]`.
- Guardrail: Onboarding-related support tickets per new account do not increase.
