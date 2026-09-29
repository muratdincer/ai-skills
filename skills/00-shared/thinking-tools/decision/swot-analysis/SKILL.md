---
description: Runs a SWOT analysis for a clearly scoped subject (product, team, platform, initiative, business unit) against a stated objective, keeping internal strengths and weaknesses separate from external opportunities and threats, backing each item with evidence and converting the result into TOWS strategies and prioritized actions. Use for strategy or planning sessions, before a major investment, when entering a market, or when someone asks for a SWOT.
related: competitor-analysis, product-strategy-one-pager, technology-strategy, assumption-mapping, risk-register
prompt: Do a SWOT analysis for our internal data platform team ahead of next year's planning.
---

# Run a SWOT Analysis

## Purpose
Give decision makers an evidence-based picture of where the subject stands relative to its objective, and translate that picture into concrete strategic options instead of four lists that nobody acts on.

## When to use
- Annual or strategic planning for a product, platform, team or business unit.
- Assessing readiness before an investment, market entry, reorganization or major change.
- Stakeholders need a shared starting point before choosing a direction.

## When not to use
- A specific choice between options is needed. Use `decision-matrix` or `trade-off-analysis`.
- The focus is only on competitors. Use `competitor-analysis`.
- The focus is only on delivery risks of an existing plan. Use `pre-mortem` or `risk-register`.

## Inputs
Required:
- The subject and the objective the SWOT serves (for example "grow self-service analytics adoption next year").

Optional, improves quality:
- Performance data, customer or user feedback, capability inventory, costs.
- Market, technology, regulatory or organizational trends.
- Previous SWOT or strategy documents.

If the objective is missing, ask for it; a SWOT without an objective produces generic lists.

## Process
1. Define scope and objective in one line each, and the time horizon.
2. Strengths: internal attributes the subject controls that help reach the objective, ideally ones that are hard for others to copy.
3. Weaknesses: internal attributes that hinder the objective, including capability, process, technical debt and cost positions.
4. Opportunities: external conditions (market, users, technology, regulation, organization beyond the subject's control) the subject could exploit.
5. Threats: external conditions that could hurt the subject regardless of its actions.
6. Test placement: if the subject can change it directly, it is internal (S/W); if not, external (O/T). Move misplaced items.
7. Make each item specific and evidenced ("median query time 40 s on the shared cluster" not "slow"); tag unsupported items `[ASSUMPTION]`.
8. Limit each quadrant to the 3-6 items that matter most for the objective; rank them.
9. Build a TOWS matrix: SO (use strengths to capture opportunities), WO (fix weaknesses to capture opportunities), ST (use strengths to reduce threats), WT (minimize weaknesses to avoid threats).
10. Select 3-5 priority actions with owner role, horizon and success signal; note what needs validation first.
11. If the user's goal continues, suggest `product-strategy-one-pager` or `technology-strategy` to turn actions into strategy, or `assumption-mapping` to validate the key items.

## Output format
```markdown
# SWOT: <subject>
**Objective:** ... **Horizon:** ...

| | Helpful | Harmful |
|---|---|---|
| **Internal** | **Strengths** 1. <item – evidence> | **Weaknesses** 1. ... |
| **External** | **Opportunities** 1. ... | **Threats** 1. ... |

## TOWS Strategies
| | Opportunities | Threats |
|---|---|---|
| **Strengths** | SO: ... | ST: ... |
| **Weaknesses** | WO: ... | WT: ... |

## Priority Actions
| # | Action | Strategy type | Owner (role) | Horizon | Success signal |
|---|---|---|---|---|---|

## Assumptions and Items to Validate
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The objective is stated and every item is relevant to it.
- [ ] Internal and external items are correctly placed (controllable = internal).
- [ ] Items are specific and evidenced or tagged `[ASSUMPTION]`.
- [ ] Each quadrant is ranked and limited to what matters.
- [ ] TOWS strategies lead to actions with owners and success signals.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing opportunities as things the team wants to do ("build a new API"). Those are actions; opportunities are external conditions.
- Vague items ("good team", "competition"). State what makes the team good and which competitor does what.
- Stopping at the four quadrants. The value is in the TOWS strategies and actions.

## Example
Input: "SWOT for our internal data platform team ahead of next year's planning."

Excerpt of output:
- Objective: double the number of business teams using self-service analytics within 12 months.
- Strength: curated finance and sales data sets already trusted by controllers `[ASSUMPTION — confirm usage data]`.
- Weakness: median query time around 40 s on the shared cluster (monitoring data).
- Opportunity: company-wide reporting consolidation mandated for next year.
- Threat: business units buying their own BI tools and building shadow data stores.
- WO action: fund cluster isolation for self-service workloads before the consolidation starts; success signal: median query time under [TBD] seconds.
