---
description: Compares pricing models (flat, tiered, per-seat, usage-based, freemium, hybrid) against value metric, cost-to-serve, competitor anchors and willingness-to-pay signals, and recommends a model with price-test options. Use when launching a product, adding a paid tier, revisiting prices, or when someone asks how to price or package a product.
related: market-analysis, competitor-analysis, business-model-canvas, experiment-design, persona
prompt: Analyze pricing options for our API monitoring tool; today it is a flat 49 USD per month.
---

# Analyze Pricing Options

## Purpose
Recommend a pricing model and packaging grounded in the value metric customers care about, the cost to serve and real willingness-to-pay evidence, with the risks and tests needed before committing.

## When to use
- Pricing a new product or a new paid tier/add-on.
- Churn, low conversion or margin issues suggest prices or packaging are wrong.
- Moving between models, e.g. per-seat to usage-based.

## When not to use
- You need overall market sizing. Use `market-analysis`.
- You need to design the actual price test mechanics. Use `experiment-design`.
- You need a customer-facing price announcement. Use `release-announcement` or `announcement`.

## Inputs
Required:
- The product, target segments and current pricing (or "none yet").

Optional, improves quality:
- Cost-to-serve drivers, usage distribution, conversion and churn data.
- Competitor prices, win/loss reasons, WTP research (Van Westendorp, Gabor-Granger, conjoint, sales discounting data).
- Constraints: contracts, regulations, currency, taxes, channel partners.

If product or segment is missing, ask. Never invent prices, elasticities or WTP; mark `[UNKNOWN]` and propose how to measure.

## Process
1. Identify the value metric: the unit that grows with customer value (seats, transactions, monitored endpoints, revenue processed). Test it: easy to understand, predictable for the buyer, scales with value, measurable.
2. Map segments by value received and WTP signals; note who is overserved or underserved by current pricing.
3. List candidate models and evaluate each on value alignment, revenue predictability, sales friction, cost coverage and expansion potential.
4. Establish the price corridor: floor from cost-to-serve and target margin, ceiling from value delivered and alternatives, anchors from competitors (sourced, dated).
5. Design packaging: tiers by segment job, fences (limits or features) that separate tiers without crippling the entry tier.
6. Assess migration impact on existing customers: who pays more or less, grandfathering, communication.
7. Recommend a model and packaging, with the assumptions it depends on.
8. Propose validation: WTP survey, sales-led price test, new-customer-only rollout, or A/B where ethical and legal.
9. Define the metrics to watch: conversion, ARPA, expansion, churn, discount rate.
10. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `experiment-design` to validate the preferred option before rollout, or `competitor-analysis` if competitor price points are unverified.

## Output format
```markdown
# Pricing Analysis: <product>
## Current State and Problem
...
## Value Metric
Chosen: <metric> — rationale; rejected alternatives
## Model Comparison
| Model | Value alignment | Predictability | Friction | Cost coverage | Expansion |
|---|---|---|---|---|---|
## Price Corridor
Floor: ... · Ceiling: ... · Anchors (source, date): ...
## Recommended Packaging
| Tier | Target segment | Includes | Fence | Price |
|---|---|---|---|---|
## Migration Impact
...
## Validation Plan and Metrics
...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] A value metric is chosen and tested against the four criteria.
- [ ] Every price or WTP figure is sourced or marked `[ASSUMPTION]`/`[TBD]`.
- [ ] Existing-customer impact and grandfathering are addressed.
- [ ] Tier fences are based on segment needs, not arbitrary feature hiding.
- [ ] A validation step exists before a full rollout.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Pricing on cost-plus alone. Cost sets the floor; value sets the ceiling.
- Too many tiers or add-ons. Buyers should self-select a tier in seconds.
- Asking customers "would you pay X?" directly. Use structured WTP methods or behavior.

## Example
Input: "API monitoring tool, flat 49 USD/month for all customers."

Excerpt of output:
- Value metric: monitored endpoints; heavy users (>200 endpoints) get most value but pay the same `[confirm usage distribution]`.
- Recommendation: three tiers by endpoints with overage, flat price retained for existing customers for 12 months `[ASSUMPTION]`.
- Validation: apply to new sign-ups only for 6 weeks; watch trial-to-paid conversion and ARPA.
