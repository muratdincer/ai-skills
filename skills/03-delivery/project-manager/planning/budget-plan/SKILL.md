---
description: Builds a project budget with a cost breakdown by WBS and cost category, separation of capex and opex where relevant, contingency and management reserves, and a time-phased cash flow that becomes the cost baseline. Use when a project needs a budget for approval, a cost baseline for tracking, or a re-forecast after scope or schedule changes.
related: wbs, resource-plan, estimation-three-point, earned-value-analysis, cloud-cost-estimate
prompt: Build a project budget from this resource plan and vendor quotes, with contingency and monthly cash flow.
---

# Build a Project Budget

## Purpose
Produce a traceable, time-phased budget that sponsors can approve and the project can track against, with explicit reserves for known and unknown risks.

## When to use
- Preparing the budget for charter approval or an investment gate.
- Establishing a cost baseline for earned value tracking.
- Re-forecasting after a change request or major risk event.

## When not to use
- Deciding whether the investment is worthwhile. Use `cost-benefit-analysis`.
- Department-level annual budget requests. Use `budget-proposal`.
- Cloud run-cost estimation of an architecture. Use `cloud-cost-estimate`.

## Inputs
Required:
- WBS or scope, and the resource plan or effort estimates.
- Rates or costs, or confirmation that they will be supplied (never assume rates).

Optional, improves quality:
- Vendor quotes, licence and infrastructure costs, travel, training.
- Organizational rules for capex/opex, currency, inflation, contingency policy.

If no cost basis is given, produce the structure with `[UNKNOWN]` values and a list of the rates needed.

## Process
1. Define cost categories: internal labour, external labour/vendors, software licences, hardware/infrastructure, cloud, training, travel, other.
2. Estimate cost per WBS package: effort × rate for labour; quotes for purchases. Show the formula or source for each line.
3. Classify each line as capex or opex according to organizational policy if required; mark `[CONFIRM WITH FINANCE]` when unsure.
4. Sum to the base estimate.
5. Add contingency reserve for identified risks (from the risk register expected monetary value or from three-point ranges). State the method.
6. Add management reserve for unknown unknowns only if organizational policy uses it; note it is outside the cost baseline.
7. Time-phase costs by month using the schedule and payment terms to produce cash flow and the cumulative baseline (S-curve data).
8. Include recurring costs that start at go-live if the approval requires total cost of ownership, clearly separated from project cost.
9. List assumptions, exclusions (e.g. taxes, internal overhead) and the currency and price basis date.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `earned-value-analysis` to track actuals against this baseline, or `resource-plan` if staffing costs are still open.

## Output format
```markdown
# Project Budget: <project>
Currency <x> | Price basis <date> | Version <x>
## Cost Breakdown
| WBS ID | Item | Category | Capex/Opex | Quantity × rate / source | Cost |
## Summary
| Line | Amount |
| Base estimate | |
| Contingency reserve (method) | |
| Cost baseline | |
| Management reserve (if used) | |
| Total budget | |
## Cash Flow
| Month | Planned spend | Cumulative |
## Post-Go-Live Recurring Costs (if required)
## Assumptions, Exclusions, Open Questions
```

## Quality checklist
- [ ] Every line has a formula or source; no unexplained numbers.
- [ ] No rate or price is invented; gaps are `[UNKNOWN]`.
- [ ] Contingency method is stated and linked to risks or ranges.
- [ ] Cash flow totals equal the cost baseline.
- [ ] Project cost and recurring run cost are separated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Hiding contingency inside line items, which makes variance analysis meaningless.
- Forgetting internal labour because it is not an invoice; sponsors then underestimate total cost.
- Phasing cost evenly instead of following the schedule and payment milestones.

## Example
Input: "3 developers for 6 months at internal rate [to be provided], vendor fixed price 120k in two milestones."

Excerpt of output:
| 1.2 | Development (internal) | Internal labour | Capex `[CONFIRM WITH FINANCE]` | 18 person-months × `[UNKNOWN]` | `[UNKNOWN]` |
| 1.3 | Vendor integration | External | Capex | Fixed price quote | 120,000 |
- Cash flow: vendor 50% at M3 acceptance, 50% at M6 `[ASSUMPTION: confirm payment terms]`.
