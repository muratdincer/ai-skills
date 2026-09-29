---
name: capability-map
description: "Builds a hierarchical business capability map (levels 1-3) with maturity, strategic importance and a heatmap, and maps applications and owners to capabilities. Use when planning investments, rationalizing applications, scoping a transformation or aligning IT with business strategy, or when someone asks what the business does independent of org chart and systems."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: enterprise-architect
  area: strategy
  title: "Build a business capability map"
  related: "application-portfolio-assessment, target-state-architecture, value-stream-map, bounded-context-map, portfolio-prioritization"
  prompt: "Build a level-2 capability map for our retail bank with maturity and strategic importance, and highlight where to invest next year."
---

# Build a Business Capability Map

## Purpose
Describe what the business does as a stable hierarchy of capabilities, then overlay maturity, importance and application coverage so investment and rationalization decisions rest on a shared, structure-independent view.

## When to use
- Annual planning or a transformation needs a heatmap of where to invest.
- Application rationalization needs a business-facing anchor for overlaps and gaps.
- An M&A or reorganization needs a neutral model independent of org structure.
- Domain or service boundaries are being drawn and need a business reference.

## When not to use
- The need is end-to-end flow and waste. Use `value-stream-map`.
- Only the application inventory is being assessed. Use `application-portfolio-assessment`.
- Software-level domain boundaries are needed. Use `bounded-context-map`.

## Inputs
Required:
- Business scope (enterprise, business unit, product line) and industry.
- Strategy statement or top business goals.

Optional:
- Existing capability models or industry reference models (e.g., BIAN for banking, eTOM for telecom, APQC PCF).
- Application inventory with owners.
- Pain points from business stakeholders.

If scope or goals are missing, ask. Maturity and importance scores must come from stakeholders; draft them as `[ASSUMPTION]` otherwise.

## Process
1. Fix the scope and naming rules: capabilities are nouns or noun phrases ("Customer Onboarding", "Credit Risk Assessment"), not processes, departments or systems.
2. Draft level 1 (7-12 capabilities) split into strategic, core and supporting groups. Start from an industry reference model if one fits, then tailor.
3. Decompose to level 2 (and level 3 only where decisions need it). Apply MECE: no overlaps, no gaps; each child fully belongs to one parent.
4. Validate stability: a capability must survive a reorganization and a system replacement. Rename anything that encodes a team or product.
5. Define scoring scales before scoring: maturity 1-5 (ad hoc → optimized) across process, people, information and technology; strategic importance (differentiating / core / commodity).
6. Score each L2 capability with its evidence source; unscored items remain `[TBD]`.
7. Map applications and business owners to L2 capabilities. Flag duplicates (many apps per capability) and gaps (none).
8. Build the heatmap: high importance + low maturity = invest; commodity + high cost/duplication = rationalize or buy.
9. Derive 3-7 investment themes and link each to capabilities and business goals.
10. List open questions and validation sessions needed with business owners.
11. Label every maturity or heat rating not confirmed by a business owner as `[ASSUMPTION]`; if the goal continues, suggest `application-portfolio-assessment` or `target-state-architecture`.

## Output format
```markdown
# Capability Map – <scope>
Scales: Maturity 1-5 · Importance: Differentiating / Core / Commodity

## Level 1 Overview
| Group | L1 Capabilities |
|---|---|

## Level 2 Detail
| L1 | L2 Capability | Description (1 line) | Owner | Maturity | Importance | Applications | Heat |
|---|---|---|---|---|---|---|---|

## Heatmap Findings
- Invest: <capability> – <why>
- Rationalize: <capability> – <duplicate apps>
- Gap: <capability with no support>

## Investment Themes
| Theme | Capabilities | Business goal | Next step |

## Assumptions and Open Questions
```

## Quality checklist
- [ ] Names are business nouns; no department, process verb or product names.
- [ ] Each level is MECE; L1 has 7-12 items.
- [ ] Scales are defined before use and every score has a source or `[ASSUMPTION]`.
- [ ] Applications and owners are mapped; duplicates and gaps are flagged.
- [ ] Investment themes trace to both capabilities and goals.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mirroring the org chart. It breaks at the next reorganization; model what, not who.
- Going to level 4 everywhere. Detail only where a decision needs it.
- Scoring by the architect alone. Maturity without business validation is not credible.

## Example
Input: "Retail bank, goals: digital onboarding and lower cost-to-serve."

Excerpt of output:
| L1 | L2 | Maturity | Importance | Applications | Heat |
|---|---|---|---|---|---|
| Customer Management | Customer Onboarding | 2 `[ASSUMPTION]` | Differentiating | 3 (branch app, web form, CRM) | Invest + rationalize |
| Payments | Payment Execution | 4 `[ASSUMPTION]` | Core | 1 | Maintain |
