---
name: north-star-metric
description: "Selects a North Star metric that captures the value customers get from the product and links it to revenue, then decomposes it into a tree of 3-5 controllable input metrics with owners and counter-metrics. Use when a product team lacks a shared value metric, when teams optimize conflicting numbers, or when someone asks \"what should our North Star be\" or wants a metric tree for a product."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: metrics
  title: "Define a North Star metric"
  related: "kpi-definition, okr-definition, metric-definition, product-strategy-one-pager, funnel-analysis"
  prompt: "Define a North Star metric and input metric tree for our B2B invoicing SaaS for small businesses."
---

# Define a North Star Metric

## Purpose
Give the product one metric that expresses delivered customer value and leads sustainable revenue, plus the input metrics teams can actually move, so roadmap and team goals align around value rather than activity.

## When to use
- Teams or squads optimize different numbers and trade-offs are argued without a shared yardstick.
- A new product or strategy needs a value metric before OKRs or KPIs are set.
- The current "North Star" is revenue, sign-ups or another output that teams cannot influence directly.

## When not to use
- Operational KPIs with formula, source and owner must be specified. Use `kpi-definition`.
- Quarterly goals are needed. Use `okr-definition` (the North Star and inputs feed it).
- A single metric needs a precise technical definition for data teams. Use `metric-definition`.

## Inputs
Required:
- Product description, primary customer segment and business model (how the product makes money).

Optional, improves quality:
- Current metrics and available data, strategy, known "aha" moment or core value action.
- Team structure (to assign input metrics).

If the business model or core customer is missing, ask. Do not invent baselines or targets; mark them `[TBD]`.

## Process
1. Classify the value game: attention (time in product), transaction (completed exchanges) or productivity (work done efficiently). This shapes candidate metrics.
2. State the core value moment in one sentence: when does the customer get the value they came for? Separate what the user said from what you infer `[ASSUMPTION]`.
3. Generate 3-5 candidate metrics of the form "<count/rate of> <value action> by <qualified customer> per <period>" (e.g. "invoices paid on time per active business per month").
4. Score candidates against criteria: expresses customer value, leads revenue, measurable with existing or feasible data, understandable by everyone, movable by product work, hard to game. Pick one; record why the others lost.
5. Define it precisely: formula, qualification rules (what counts as active/valid), time window, segment scope and data source or `[TBD]`.
6. Decompose into 3-5 input metrics that multiply or add up to the North Star (breadth: how many customers; depth: how much each; frequency: how often; efficiency/quality: how well). Each must be controllable by a team.
7. Add 1-2 counter-metrics (guardrails) that expose gaming or harm: quality, customer trust, support load, churn.
8. Assign an owner team per input metric and a review cadence; note known leading-lag relationships as hypotheses to validate.
9. List risks: lagging behaviour, seasonality, data gaps, segments where the metric misleads.
10. If the user's goal continues, suggest the next skill: `okr-definition` to set goals on input metrics, `kpi-definition` for operational tracking, or `metric-definition` for a data-level spec.

## Output format
```markdown
# North Star Metric: <product>
Value game: <attention/transaction/productivity> · Core value moment: <sentence>

## North Star
- Metric: <name>
- Formula: <...> · Qualified when: <...> · Window: <...> · Source: <... or [TBD]>
- Why it reflects value / leads revenue: <...>

## Candidates Considered
| Candidate | Value | Revenue link | Measurable | Movable | Gaming risk | Verdict |
|---|---|---|---|---|---|---|

## Input Metric Tree
North Star
├── Breadth: <metric> – owner <team>
├── Depth: <metric> – owner <team>
├── Frequency: <metric> – owner <team>
└── Quality: <metric> – owner <team>

## Counter-Metrics
- <metric> – guards against <...>

## Risks, Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The North Star measures customer value delivered, not revenue, sign-ups or raw activity.
- [ ] The formula, qualification rule and time window are unambiguous.
- [ ] Each input metric is controllable by a named team and logically drives the North Star.
- [ ] At least one counter-metric guards against gaming.
- [ ] No baseline or target is invented; missing data is `[TBD]`.
- [ ] Rejected candidates are listed with reasons.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Picking a vanity metric (registered users, page views) that grows without value delivered. Require a value action and a qualified customer.
- Choosing revenue as North Star. Revenue lags value; keep it as the business outcome the North Star should predict.
- Input metrics nobody owns. Map each to a team or it will not move.

## Example
Input: "B2B invoicing SaaS for small businesses."

Weak: "Monthly active users."
Strong excerpt:
- Value game: productivity. Core value moment `[ASSUMPTION]`: a business gets paid for an invoice sent through the product.
- North Star: invoices paid within terms per active business per month.
- Inputs: businesses sending ≥1 invoice/month (breadth); invoices per business (depth); share with online payment link (efficiency); % reminders automated (quality).
- Counter-metric: customer complaints about reminder emails per 1,000 invoices.
