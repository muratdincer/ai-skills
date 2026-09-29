---
description: Defines product KPIs as an unambiguous KPI sheet with name, purpose, formula, inclusion rules, data source, baseline, target, thresholds, owner, cadence and the decision each KPI informs. Use when a product, feature or team needs a KPI set, when existing KPIs are vague or disputed, or when someone asks "which KPIs should we track and how exactly are they calculated".
related: north-star-metric, metric-definition, okr-definition, dashboard-spec, feature-adoption-review
prompt: Define the KPIs for our new mobile self check-in feature at hotels.
---

# Define KPIs

## Purpose
Produce a small set of KPIs that everyone calculates the same way, that have an owner and a review rhythm, and that each drive a known decision, so reviews discuss what to do rather than whose number is right.

## When to use
- A product, feature or team is launching and needs agreed performance indicators.
- Existing KPIs are disputed ("which active users?"), untracked or have no owner.
- A dashboard or management report must be specified and the KPIs behind it are unclear.

## When not to use
- The product has no shared value metric yet. Use `north-star-metric` first.
- Time-bound goals with ambition levels are needed. Use `okr-definition`.
- A data engineer needs a full event/SQL-level specification of one metric. Use `metric-definition`.

## Inputs
Required:
- The product/feature/team, its goal or the decisions the KPIs should support.

Optional, improves quality:
- Existing metrics, analytics events and data sources; North Star or OKRs.
- Baselines, benchmarks, SLAs or contractual targets; reporting audience.

If the goal is missing, ask. Do not invent baselines or targets; mark them `[TBD]` with how to obtain them.

## Process
1. List the decisions the KPIs must inform (e.g. "expand to more hotels", "invest in onboarding") and the audience; a KPI that informs no decision is dropped or moved to diagnostics.
2. Cover the value chain with a balanced set of 4-8 KPIs: outcome (value/business), behaviour (adoption, engagement), quality/health (errors, latency, support load) and at least one guardrail.
3. For each KPI write a precise definition: formula with numerator and denominator, unit, inclusion/exclusion rules (test accounts, internal users, cancellations), time window and aggregation (daily, rolling 28 days).
4. Name the data source and event/field, or mark `[TBD]` and note the instrumentation needed. Flag KPIs requiring personal data and apply minimization (aggregate, pseudonymize; KVKK/GDPR).
5. Classify each KPI as leading or lagging and note the expected relationship between them as a hypothesis.
6. Record baseline (given or `[TBD]` with measurement plan), target (given or `[TBD]`), and red/amber/green thresholds with the action each state triggers.
7. Assign one accountable owner (role) per KPI and a review cadence matching how fast it can move.
8. Check the set for conflicts and gaming: which KPI could be improved while harming another? Add or pair a counter-metric where needed.
9. Mark every inferred definition or relationship `[ASSUMPTION]` and list open questions for data owners.
10. If the user's goal continues, suggest the next skill: `dashboard-spec` to visualize the set, `metric-definition` for a data-level spec, or `okr-definition` to set time-bound goals.

## Output format
```markdown
# KPI Sheet: <product / feature / team>
Decisions supported: <...> · Audience: <...>

| KPI | Type (outcome/behaviour/quality/guardrail) | Leading/lagging | Formula | Inclusion rules | Window | Source | Baseline | Target | R/A/G thresholds → action | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|---|---|---|

## KPI Details
### <KPI name>
- Purpose / decision it informs: ...
- Definition notes and edge cases: ...
- Data and privacy: ...

## Conflicts and Counter-Metrics
- ...

## Instrumentation Gaps
- ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every KPI informs a named decision and has one accountable owner.
- [ ] Every formula states numerator, denominator, inclusion rules and time window.
- [ ] The set mixes outcome, behaviour and quality KPIs and has at least one guardrail.
- [ ] Baselines and targets are given or `[TBD]` with a way to obtain them; none are invented.
- [ ] Personal data use is minimized and flagged.
- [ ] Thresholds map to concrete actions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Active users" without defining active. Specify the qualifying action and window.
- Too many KPIs. More than ~8 per audience dilutes attention; move the rest to diagnostics.
- Targets without baselines. Measure first, then set the target, or state the target as a hypothesis.

## Example
Input: "KPIs for our new mobile self check-in feature at hotels."

Excerpt of output:
| KPI | Type | Formula | Target | Owner |
|---|---|---|---|---|
| Self check-in rate | Outcome | Stays checked in via app ÷ eligible stays (excl. group bookings) per week | `[TBD]` after 4-week baseline | Product manager, guest app |
| Median time to room key | Behaviour | Median minutes from arrival geofence to digital key issued | `[TBD]` | Product manager |
| Check-in failure rate | Quality | Failed app check-ins ÷ attempts | Red above threshold `[TBD]` → incident review | Engineering lead |
| Front desk escalations | Guardrail | App check-ins needing desk help ÷ app check-ins | `[TBD]` | Hotel operations |
- Open question: Are identity checks for foreign guests (legal requirement) possible in-app, or do they force desk visits?
