---
name: cost-benefit-analysis
description: "Quantifies the costs and benefits of an initiative or of competing options over a defined horizon, separating one-off and recurring items, tangible and intangible benefits, and computes net benefit, ROI, payback period and optionally NPV with sensitivity on the key assumptions. Use when a business case, investment decision or option comparison needs numbers, or when asked 'is it worth it?' or 'what is the ROI?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: solution
  title: "Run a cost-benefit analysis"
  related: "feasibility-study, budget-proposal, cloud-cost-estimate, benefits-realization, decision-matrix"
  prompt: "Run a cost-benefit analysis for automating invoice matching: licence 40k/year, implementation 120k, it should save 3 FTE of manual work."
---

# Run a Cost-Benefit Analysis

## Purpose
Put an initiative's costs and benefits on one comparable, transparent basis so that decision makers see the net value, the payback and which assumptions the result depends on.

## When to use
- A business case or funding request needs financial justification.
- Two or more options must be compared on value, not only on price.
- A sponsor asks for ROI or payback before approving.

## When not to use
- Viability across non-financial dimensions is still open. Use `feasibility-study` first.
- You only need the cloud run-cost of an architecture. Use `cloud-cost-estimate`.
- Benefits have already been delivered and must be tracked. Use `benefits-realization`.

## Inputs
Required:
- The initiative or options, and the cost and benefit figures or drivers the user has (volumes, rates, FTE, licence prices).
- The evaluation horizon (e.g. 3 or 5 years); if absent, propose 3 years and mark `[ASSUMPTION]`.

Optional, improves quality:
- Discount rate or hurdle rate used by finance, currency, inflation assumption.
- Fully loaded cost per FTE, baseline volumes, growth forecast.
- Risk-adjustment policy, tax or depreciation treatment (defer to finance).

Never invent prices, salaries or volumes. If a figure is needed and missing, ask (at most 5 questions at once) or leave it as a named variable.

## Process
1. Define the base case (do nothing / status quo) and each option; all figures are incremental to the base case.
2. List costs: one-off (licences, implementation, migration, training, internal effort, parallel run) and recurring (subscriptions, support, infrastructure, additional staff, maintenance). Include decommissioning and exit costs.
3. List benefits: hard savings (cost avoided, FTE hours released, licences retired), revenue effects, risk reduction (expected loss avoided) and intangible benefits (kept qualitative).
4. Distinguish released capacity from cash savings: hours freed are only cash if headcount, overtime or contractor spend actually falls. Mark which applies.
5. Lay out a period table (year 0..N): costs, benefits, net, cumulative net. Show formulas or drivers for each line.
6. Compute: total net benefit, ROI = (total benefits − total costs) ÷ total costs, payback period (when cumulative net turns positive), and NPV if a discount rate was given.
7. Run sensitivity on the 2-3 assumptions with the biggest effect (e.g. adoption rate, savings per item, implementation cost +30%): show best, expected and worst case.
8. Add non-financial factors: strategic fit, compliance, customer experience, risks that numbers do not capture.
9. State the conclusion with its conditions ("positive if adoption exceeds X%") and list assumptions for finance to validate.
10. If the user wants to continue, suggest `budget-proposal` to request funding, `decision-matrix` to weigh financial and non-financial criteria, or `benefits-realization` to track the promised benefits.

## Output format
```markdown
# Cost-Benefit Analysis: <initiative>
Horizon: <N years> · Currency: <...> · Discount rate: <x% or not applied> · Base case: <...>

## Costs
| Item | Type (one-off/recurring) | Driver / formula | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|---|

## Benefits
| Item | Type (cash / capacity / risk / intangible) | Driver / formula | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|

## Result
| Metric | Expected | Worst | Best |
|---|---|---|---|
| Net benefit | | | |
| ROI | | | |
| Payback | | | |
| NPV (if rate given) | | | |

## Non-Financial Factors
- ...

## Conclusion and Conditions
...

## Assumptions to Validate
- [ASSUMPTION] ... — validate with: ...
```

## Quality checklist
- [ ] Every figure traces to the input or a stated driver; nothing is invented.
- [ ] One-off and recurring costs are both present, including internal effort and exit costs.
- [ ] Capacity benefits are not counted as cash unless the saving is realized.
- [ ] Arithmetic is correct: totals, ROI and payback match the period table.
- [ ] Sensitivity covers the assumptions that could flip the conclusion.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Counting freed FTE hours as savings when nobody leaves or is redeployed. Label it capacity and say how it will be used.
- Forgetting internal effort, parallel run and adoption ramp-up, which makes year 1 look unrealistically good.
- Presenting one number without sensitivity. Show which assumption breaks the case.

## Example
Input: "Licence 40k/year, implementation 120k, saves 3 FTE of manual matching."

Excerpt of output:
| Metric | Expected |
|---|---|
| 3-year cost | 120k + 3 × 40k = 240k |
| 3-year benefit | 3 FTE × fully loaded cost `[UNKNOWN]` × 3 years – ask finance for FTE cost |
| Break-even condition | Benefit ≥ 240k over 3 years, i.e. fully loaded cost per FTE ≥ ~26.7k/year, provided the 3 FTE are actually released |
