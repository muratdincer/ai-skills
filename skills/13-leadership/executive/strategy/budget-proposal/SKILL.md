---
description: Writes a technology budget proposal that separates investment (change) from run costs, ties each line to a business outcome, shows the cost of not funding, and offers funding scenarios with their consequences. Use when a technology leader must request or defend an annual or project budget, justify headcount, licenses or cloud spend, or present options to finance or the executive team.
related: technology-strategy, cost-benefit-analysis, cloud-cost-estimate, budget-plan, board-update
prompt: Draft our IT budget proposal for next year; run costs grow 12% from cloud and licenses, and we want funding for a data platform and 4 more engineers.
---

# Write a Budget Proposal

## Purpose
Give decision makers a budget request they can approve, reduce or reject knowingly: every line is justified, run and change costs are separated, and each funding scenario states what the organization gets and what it gives up.

## When to use
- Annual budgeting for a technology department or a major area.
- Requesting funding for a new initiative, headcount, licenses or infrastructure.
- Finance asks for cuts or scenarios and the consequences must be explicit.

## When not to use
- Detailed cost plan of an approved project. Use `budget-plan`.
- Deciding whether a single initiative pays off. Use `cost-benefit-analysis`.
- Estimating cloud cost of a specific design. Use `cloud-cost-estimate`.

## Inputs
Required:
- Current cost base or last year's actuals (at least by major category) and the proposed new spending items.

Optional, improves quality:
- Strategy and goals the budget supports; contract renewals and price changes; headcount plan.
- Finance rules: capex/opex treatment, currency, inflation assumptions, approval thresholds.
- Usage trends (users, transactions, data volume) that drive run costs.

If the cost base is missing, ask for it. Never invent amounts, rates or prices; mark gaps `[UNKNOWN]` and estimates `[ASSUMPTION]` with their basis.

## Process
1. Establish the baseline: last period's actuals by category (people, licenses/subscriptions, cloud/hosting, hardware, services/contractors, training) and known committed contracts.
2. Separate run (keep the lights on, including mandatory growth from usage, price and contract changes) from change (new investments); explain each run increase by its driver.
3. For each investment, state the business outcome, the goal it serves, the cost profile over time (one-off versus recurring, including follow-on run costs) and the earliest visible benefit.
4. State the cost and risk of not funding each item (compliance exposure, outage risk, missed revenue, rising maintenance), with evidence where available.
5. Identify savings and offsets: decommissioning, license consolidation, rightsizing, contract renegotiation; mark unconfirmed savings `[ASSUMPTION]`.
6. Build 2-3 scenarios (e.g. baseline, recommended, reduced) and say exactly which items move between them and what outcome is lost in each.
7. Apply finance conventions the user gave (capex/opex, currency, inflation); if unknown, list them as open questions rather than guessing.
8. Add risks and sensitivities: exchange rates, usage growth, hiring timing, vendor price changes.
9. Define how spend and outcomes will be tracked and reported during the period.
10. Write a one-page summary: total ask, change versus last period, recommended scenario, top three reasons.
11. If the user's goal continues, suggest `board-update` to present it, `cost-benefit-analysis` for a contested item, or `quarterly-planning` to phase the work.

## Output format
```markdown
# Budget Proposal <period>: <organization/area>

## Summary
- Total request: <amount> (<+/-x% vs last period>) – recommended scenario: <name>
- Top reasons: 1) ... 2) ... 3) ...

## Baseline (last period actuals)
| Category | Actual | Committed next period | Source |
|---|---|---|---|

## Run Costs
| Category | Next period | Change | Driver |
|---|---|---|---|

## Investments
| Item | Outcome / goal | One-off | Recurring | First benefit | Cost of not funding |
|---|---|---|---|---|---|

## Savings and Offsets
- ...

## Scenarios
| Scenario | Total | Included | Excluded | Consequence |
|---|---|---|---|---|

## Risks, Sensitivities, Assumptions
- [ASSUMPTION] ...

## Tracking and Reporting
- ...
```

## Quality checklist
- [ ] Run and change costs are separated, and every run increase has a driver.
- [ ] Every investment names an outcome, its follow-on run cost and the cost of not funding.
- [ ] Scenarios state what is lost, not just a lower number.
- [ ] No invented amounts, prices or savings; each figure has a source or an `[ASSUMPTION]` label.
- [ ] The summary fits on one page and states the recommended scenario.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Hiding the recurring cost of investments. A new platform adds licenses, cloud and people to next year's run budget; show it now.
- Percent-increase requests without drivers ("+10% for growth"). Finance cuts what is not explained.
- Presenting only one number. Without scenarios, the decision becomes an arbitrary cut.

## Example
Input: Run costs +12% from cloud and licenses; ask for a data platform and 4 engineers.

Excerpt of output:
- Run driver: cloud +`[UNKNOWN]` from transaction growth and a license renewal with price uplift `[confirm contract terms]`.
- Weak justification (avoid): "Data platform is strategic." Strong: "Data platform removes 3 manual monthly reports and enables the pricing goal; not funding keeps the regulatory report on spreadsheets (audit finding risk)."
- Reduced scenario: data platform phase 1 only, 2 engineers; consequence: pricing analytics slips 2 quarters `[ASSUMPTION]`.
