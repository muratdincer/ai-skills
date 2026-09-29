---
name: porters-five-forces
description: "Analyzes an industry or market segment with Porter's five forces (rivalry, threat of new entrants, threat of substitutes, buyer power, supplier power), rates each force with its drivers and evidence, and derives what the structure means for profitability, positioning and product strategy. Use when assessing the attractiveness of a market or segment, preparing a strategy or entry decision, explaining margin pressure, or when someone asks for a five forces or industry structure analysis."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: strategy
  title: "Analyze Porter's five forces"
  related: "pestle-analysis, competitor-analysis, market-analysis, swot-analysis, pricing-analysis"
  prompt: "Run a five forces analysis for the mid-market field service management software segment in Turkey; we are deciding whether to enter it."
---

# Analyze Porter's Five Forces

## Purpose
Explain why a market segment is more or less profitable and defensible, and turn the strongest forces into strategic choices on positioning, pricing, lock-in and partnerships.

## When to use
- Deciding whether to enter, expand in or exit a market or segment.
- Explaining persistent price or margin pressure.
- Preparing product strategy where platform, channel or supplier dependencies matter.

## When not to use
- The need is a feature-by-feature comparison of named competitors. Use `competitor-analysis`.
- The need is a macro scan of regulation, economy and society. Use `pestle-analysis`.
- The need is to size the market. Use `market-analysis`.

## Inputs
Required:
- The industry or segment definition: what is sold, to whom, and in which geography.

Optional, improves quality:
- The user's own position (entrant or incumbent), known competitors, substitutes, key suppliers/platforms, pricing and switching data, market studies.

If the segment is undefined or too broad ("software"), ask one question to narrow it. Do not invent market shares, margins or counts; mark unknown values `[UNKNOWN]` and state which evidence would settle them.

## Process
1. Define the segment boundary precisely: product category, customer type, geography, and the point of view (entrant, incumbent, investor).
2. Rivalry: number and balance of competitors, growth rate, differentiation, fixed-cost intensity, exit barriers, price transparency.
3. Threat of new entrants: scale economies, network effects, switching costs, capital needs, access to channels, regulation/certification, incumbent retaliation, entry by adjacent platforms.
4. Threat of substitutes: other ways the customer does the job (spreadsheets, services, in-house build, doing nothing), relative price-performance and switching cost.
5. Buyer power: buyer concentration, purchase volume, price sensitivity, ability to backward-integrate, procurement sophistication, standardization of the offering.
6. Supplier power: concentration of critical inputs (cloud, app stores, data providers, specialist talent, integration partners), switching cost, forward-integration threat.
7. For each force, list the 2-4 strongest drivers with evidence tags `[FACT: source]`, `[ASSUMPTION]` or `[UNKNOWN]`, rate it Low/Medium/High and give a trend (rising/stable/falling). Consider complementors and regulators as modifiers, not a sixth force.
8. Synthesize: overall attractiveness for the stated point of view, and which forces cap profitability.
9. Derive strategic implications: where to position, how to raise switching costs or differentiation, which dependencies to mitigate, pricing stance, partnerships; each tied to a force.
10. List the evidence to gather to validate the weakest ratings, then suggest the next skill: `competitor-analysis` for named rivals, `pricing-analysis` for pricing moves, or `swot-analysis` to combine with internal capabilities.

## Output format
```markdown
# Five Forces: <segment> – <geography> – <point of view>
**Segment boundary:** <product, customer, geography>
**Overall attractiveness:** <Low/Medium/High> – <one-line reason>

| Force | Rating | Trend | Key drivers (evidence tag) |
|---|---|---|---|
| Rivalry | H | ↑ | <driver> [FACT: ...]; <driver> [ASSUMPTION] |
| New entrants | | | |
| Substitutes | | | |
| Buyer power | | | |
| Supplier power | | | |

## Strategic Implications
| # | Implication / move | Force addressed | Confidence |
|---|---|---|---|

## Evidence to Gather
- <question> – <source> – <which rating it would change>

## Assumptions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The segment boundary is specific enough that a different boundary would change the ratings.
- [ ] Every rating is backed by named drivers with evidence tags; no invented shares or margins.
- [ ] Substitutes include non-product alternatives (manual work, services, in-house, do nothing).
- [ ] Implications are tied to specific forces and are actionable for the stated point of view.
- [ ] Weakest ratings have a validation step.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Analyzing "the software industry". Too broad a boundary makes every force Medium and the output useless.
- Confusing rivalry with the full analysis. The biggest threat is often a substitute or a platform supplier.
- Static snapshot. Add the trend; a force that is Low today but rising drives the decision.

## Example
Input: "Five forces for mid-market field service management software in Turkey; we are deciding whether to enter."

Excerpt of output:
| Force | Rating | Trend | Key drivers |
|---|---|---|---|
| Substitutes | H | → | Spreadsheets plus messaging apps are "good enough" for many firms [ASSUMPTION]; ERP add-on modules [VERIFY which vendors bundle it] |
| Buyer power | M | ↑ | Fragmented buyers, but high price sensitivity and easy monthly switching [ASSUMPTION] |
| Supplier power | M | → | Dependence on mobile app stores and map/route APIs [FACT: product architecture] |

Implication: Compete on integration with local e-invoice and accounting systems to raise switching costs (addresses substitutes and buyer power). Confidence: Medium.
