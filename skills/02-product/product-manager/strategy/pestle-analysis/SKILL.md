---
name: pestle-analysis
description: "Runs a PESTLE analysis (political, economic, social, technological, legal, environmental) for a product, market entry or strategic decision, rating each factor by impact, likelihood and time horizon and translating the top factors into concrete product and business implications. Use when entering a new market or country, reviewing a strategy or roadmap, assessing regulatory or macro risk, or when someone asks for a PESTEL/PEST or \"external environment\" scan."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: strategy
  title: "Run a PESTLE analysis"
  related: "market-analysis, swot-analysis, porters-five-forces, product-strategy-one-pager, assumption-mapping"
  prompt: "Do a PESTLE analysis for launching our SME payroll SaaS in Germany next year."
---

# Run a PESTLE Analysis

## Purpose
Scan the macro environment around a product or decision and turn the few factors that really matter into implications, actions and signals to monitor, instead of a generic list of trends.

## When to use
- Evaluating entry into a new country, region or regulated segment.
- Refreshing product strategy or a multi-year roadmap.
- Assessing exposure to regulatory, economic or technology shifts before a major investment.

## When not to use
- The question is about competitors and industry profitability. Use `porters-five-forces` or `competitor-analysis`.
- Internal strengths and weaknesses must be combined with external factors. Use `swot-analysis` (PESTLE can feed its opportunities and threats).
- Market size and segments are needed. Use `market-analysis`.

## Inputs
Required:
- The subject: product or business, and the market/geography and decision the analysis supports.

Optional, improves quality:
- Time horizon, target segments, business model, known regulations, internal research or sources the user trusts.

If the subject or geography is missing, ask for it. Do not present current figures, laws or rates as facts unless the user supplies them or they are well-established; otherwise mark them `[VERIFY]` with the type of source to check.

## Process
1. Frame the scope: subject, geography, segment, decision to support and time horizon (for example 0-12 months, 1-3 years, 3+ years).
2. For each of the six dimensions, list 3-6 candidate factors specific to this product and market. Examples: Political (trade policy, public procurement, stability, government digitalization programs); Economic (interest and inflation dynamics, FX, labor cost, SME investment appetite); Social (demographics, work patterns, trust, language, digital literacy); Technological (platform shifts, infrastructure, AI, interoperability standards); Legal (data protection such as GDPR/KVKK, sector rules, employment, tax, e-invoicing, accessibility); Environmental (sustainability reporting, energy costs, customer ESG requirements).
3. Separate what is a sourced fact, what is general knowledge and what is inference; tag each factor `[FACT: source]`, `[VERIFY]` or `[ASSUMPTION]`.
4. Rate each factor: Impact on the subject (H/M/L), Likelihood or certainty (H/M/L), Direction (opportunity / threat / both) and Horizon.
5. Remove factors that are generic or have no plausible link to the decision. Keep a short "considered and dropped" list.
6. For the top 5-8 factors (High impact and at least Medium likelihood), write the concrete implication for product, pricing, go-to-market, operations or compliance.
7. Turn implications into actions: must-do (compliance, entry blockers), should-do (differentiators), and watch items with a leading indicator and a review trigger.
8. Note cross-factor interactions (for example a legal change that creates a technology requirement) and the key assumptions the conclusion depends on.
9. Summarize in 3-5 bullets: overall attractiveness or exposure, blocking factors and the next evidence to gather.
10. Suggest the next skill: `swot-analysis` to combine with internal capabilities, `porters-five-forces` for industry structure, or `assumption-mapping` to test the riskiest assumptions.

## Output format
```markdown
# PESTLE Analysis: <subject> – <geography> – <horizon>
**Decision supported:** <...>
**Summary:** <3-5 bullets>

| Dim. | Factor | Evidence tag | Direction | Impact | Likelihood | Horizon | Implication |
|---|---|---|---|---|---|---|---|
| L | <factor> | [VERIFY: official source type] | Threat | H | H | 0-12m | <...> |

## Priority Factors and Actions
| Factor | Action type (must / should / watch) | Action | Leading indicator | Owner |
|---|---|---|---|---|

## Interactions
- ...

## Considered and Dropped
- <factor> – <why>

## Assumptions and Items to Verify
- [ASSUMPTION] ...
- [VERIFY] <claim> – <where to check>
```

## Quality checklist
- [ ] Every factor is specific to this product and geography, not a generic trend.
- [ ] Laws, rates and figures are either sourced by the user or tagged `[VERIFY]`; none are invented.
- [ ] Each priority factor has an implication and a concrete action or indicator.
- [ ] Opportunities are captured as well as threats.
- [ ] The summary answers the decision the analysis supports.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Encyclopedic lists with no "so what". Each kept factor needs an implication, or it is dropped.
- Stating regulation or economic figures from memory as current facts. Tag and route to verification.
- Mixing up Legal and Political: Political is policy direction and stability; Legal is binding law and enforcement.

## Example
Input: "PESTLE for launching our SME payroll SaaS in Germany next year."

Excerpt of output:
| Dim. | Factor | Evidence tag | Direction | Impact | Likelihood | Horizon | Implication |
|---|---|---|---|---|---|---|---|
| L | Payroll data is personal and sensitive; GDPR plus works council expectations on employee data | [VERIFY: data protection authority and legal counsel] | Threat | H | H | 0-12m | EU data residency, DPA templates, audit logs before launch |
| S | Preference for German-language support and local accounting partners | [ASSUMPTION] | Both | M | H | 0-12m | Partner channel with tax advisors; localized onboarding |
| T | Mandatory e-invoicing and digital reporting interfaces | [VERIFY: current mandate and dates] | Opportunity | M | M | 1-3y | Offer certified interfaces as differentiator |
