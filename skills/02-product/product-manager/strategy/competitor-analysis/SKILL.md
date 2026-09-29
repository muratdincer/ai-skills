---
description: Compares direct, indirect and substitute competitors on target segment, jobs served, features, pricing and positioning, then identifies gaps, threats and differentiation opportunities with dated sources. Use when entering a market, planning strategy or positioning, preparing for sales losses, or when someone asks how a product stacks up against rivals.
related: market-analysis, positioning-statement, pricing-analysis, product-strategy-one-pager, swot-analysis
prompt: Compare our expense management app with the main competitors used by Turkish SMEs and show where we can differentiate.
---

# Analyze Competitors

## Purpose
Show, with evidence, how the product compares with the alternatives customers actually consider, and turn the comparison into decisions: where to differentiate, where parity is enough and where not to compete.

## When to use
- Strategy, positioning or roadmap planning.
- Repeated losses or churn to a specific rival.
- Entering a new segment or preparing sales battlecards.

## When not to use
- You need overall market size and segments. Use `market-analysis`.
- You need the final positioning statement. Use `positioning-statement`.
- You need a generic strengths/weaknesses view of your own situation. Use `swot-analysis`.

## Inputs
Required:
- Your product and target segment; at least the names of competitors or the problem space to search in.

Optional, improves quality:
- Win/loss notes, sales feedback, customer interviews, reviews.
- Public pricing pages, product docs, analyst notes (with access dates).

If your product or segment is missing, ask. Do not state competitor facts you cannot source; mark them `[UNVERIFIED]` with a date.

## Process
1. List competitors in three rings: direct (same job, same segment), indirect (same job, different approach) and substitutes (spreadsheets, agencies, doing nothing).
2. Pick 3-6 to analyze in depth, based on how often customers consider them.
3. For each, capture: target segment, core job, key capabilities, pricing model and entry price, go-to-market, positioning claim, notable strengths and weaknesses. Note source and access date.
4. Build a comparison on capabilities that matter to the target segment's buying criteria, not on every feature. Rate as Better / Parity / Worse / Absent.
5. Map positioning on two axes relevant to buyers (e.g. depth vs ease, price vs breadth).
6. Identify gaps: needs no one serves well, and segments underserved.
7. Identify threats: where rivals are moving (recent launches, pricing changes, funding) and what it means.
8. Recommend: differentiate on 1-2 areas, match parity on table stakes, deliberately ignore others.
9. List evidence gaps and how to close them (win/loss interviews, trial sign-ups).
10. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `positioning-statement` to turn the gaps into a differentiated position, or `pricing-analysis` if price is the main battleground.

## Output format
```markdown
# Competitor Analysis: <product> — <segment> (as of <date>)
## Competitive Set
| Ring | Competitor | Why considered |
|---|---|---|

## Profiles
### <Competitor>
Segment · Core job · Pricing · GTM · Positioning · Strengths · Weaknesses · Sources (date)

## Comparison on Buying Criteria
| Criterion | Us | A | B | C |
|---|---|---|---|---|

## Positioning Map
<axes and placement>

## Gaps, Threats and Recommendations
- Differentiate on: ...
- Parity needed: ...
- Do not compete on: ...

## Evidence Gaps
- ...
```

## Quality checklist
- [ ] Substitutes, including "do nothing", are considered.
- [ ] Every competitor fact has a source and date or is `[UNVERIFIED]`.
- [ ] Comparison criteria come from buyer priorities, not your feature list.
- [ ] The analysis ends with explicit differentiate/parity/ignore choices.
- [ ] Tone is factual; no disparaging claims.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Feature-count tables that make you look good but ignore what buyers value. Weight by buying criteria.
- Treating the analysis as permanent. Date it and schedule a refresh.
- Copying competitors' roadmaps. Use gaps to sharpen your own strategy.

## Example
Input: "Our expense app vs main competitors for Turkish SMEs."

Excerpt of output:
- Substitute: Excel plus WhatsApp photos of receipts — free, familiar, no approval trail.
- Criterion "e-Archive invoice matching": Us Better; A Parity; B Absent `[UNVERIFIED, pricing page 2026-09]`.
- Recommendation: Differentiate on accountant collaboration; parity on OCR; do not compete on corporate card issuing.
