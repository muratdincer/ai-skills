---
description: Structures a market analysis with TAM/SAM/SOM sizing (top-down and bottom-up, with every figure sourced or marked as assumption), segments, trends, drivers and barriers. Use when evaluating a new market, product idea or expansion, when a business case needs market size, or when someone asks how big a market is or which segment to target.
related: competitor-analysis, business-model-canvas, product-strategy-one-pager, persona, pricing-analysis
prompt: Do a market analysis for a scheduling SaaS for independent physiotherapy clinics in Turkey.
---

# Analyze a Market

## Purpose
Give decision makers a transparent view of a market's size, structure and dynamics so they can decide whether and where to play. Transparency of sources and assumptions matters more than a big number.

## When to use
- Evaluating a new product, market entry or geographic expansion.
- A business case, strategy or investment decision needs market sizing.
- Choosing a beachhead segment among several candidates.

## When not to use
- The question is how specific rivals compare. Use `competitor-analysis`.
- You need the business model logic of one idea. Use `business-model-canvas`.
- You need price levels and models. Use `pricing-analysis`.

## Inputs
Required:
- The product or offering and the market/geography to analyze.

Optional, improves quality:
- Available data: industry reports, public statistics, internal sales data, customer counts.
- Target price or revenue per customer, business model.
- Decision the analysis supports.

If product or geography is missing, ask. Never fill missing data with invented numbers; mark `[UNKNOWN]` and state how to obtain it.

## Process
1. Define the market boundary: the customer, the need and the geography; list what is excluded.
2. Segment the market by attributes that change buying behavior (size, vertical, maturity, channel, regulation), not by demographics alone.
3. Size TAM bottom-up where possible: number of potential customers x annual value per customer. Show the formula and cite each input.
4. Cross-check with a top-down estimate from a published source; explain gaps greater than ~2x.
5. Derive SAM (reachable with current product, channel, language, regulation) and SOM (realistically capturable in the horizon, based on capacity and comparable adoption). Label every factor.
6. Describe trends and drivers (technology, regulation, behavior, economics) and barriers (switching costs, incumbents, compliance).
7. Score candidate segments on attractiveness (size, growth, pain, willingness to pay, accessibility) and fit (capability, advantage).
8. State confidence (High/Medium/Low) for each figure and the key sensitivity (which input moves the result most).
9. Recommend a focus segment and the evidence still needed.

## Output format
```markdown
# Market Analysis: <offering> — <geography>
## Market Definition
<customer, need, geography; exclusions>

## Sizing
| Level | Formula | Inputs (source) | Value | Confidence |
|---|---|---|---|---|
| TAM | ... | ... | ... | H/M/L |
| SAM | ... | ... | ... | ... |
| SOM | ... | ... | ... | ... |
Top-down cross-check: ...
Key sensitivity: ...

## Segments
| Segment | Attractiveness | Fit | Notes |
|---|---|---|---|

## Trends, Drivers and Barriers
- ...

## Recommendation and Evidence Gaps
- ...
```

## Quality checklist
- [ ] Every number has a source or is marked `[ASSUMPTION]`/`[UNKNOWN]`.
- [ ] Sizing formulas are shown, not just results.
- [ ] Bottom-up and top-down estimates are compared.
- [ ] SOM reflects realistic capacity and adoption, not "1% of TAM".
- [ ] Segments are defined by buying behavior.
- [ ] A clear recommendation and remaining evidence gaps are stated.

## Common pitfalls
- Presenting a top-down TAM from a report as the opportunity. Buyers who cannot be reached or served are not your market.
- Mixing currencies, years or units across sources. Normalize and state the base year.
- Hiding assumptions in a spreadsheet. Put the drivers in the document.

## Example
Input: "Scheduling SaaS for independent physiotherapy clinics in Turkey."

Excerpt of output:
- TAM formula: number of independent physiotherapy clinics `[UNKNOWN – source: ministry/association registry]` x annual subscription `[ASSUMPTION: from pricing test]`.
- SAM: clinics with online booking readiness and Turkish-language support; excludes hospital chains.
- Key sensitivity: clinic count; confidence Low until registry data is obtained.
