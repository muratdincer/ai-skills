---
description: Completes a Business Model Canvas or Lean Canvas for a product idea, separating evidence from assumptions and ranking the riskiest assumptions to test first. Use when a new idea, venture or product line needs its business logic laid out, when comparing business model options, or when someone asks for a business model or lean canvas.
related: market-analysis, pricing-analysis, assumption-mapping, hypothesis-statement, product-vision
prompt: Fill a lean canvas for a marketplace that connects freelance accountants with small e-commerce sellers.
---

# Fill a Business/Lean Canvas

## Purpose
Lay out on one page how an idea creates, delivers and captures value, and make visible which blocks rest on evidence and which are guesses. The riskiest guesses become the next experiments.

## When to use
- Early shaping of a new product, venture or internal business line.
- Comparing two or more business model options for the same idea.
- Reviewing an existing product's model after a market or cost change.

## When not to use
- You need market sizing detail. Use `market-analysis`.
- You need a full price model comparison. Use `pricing-analysis`.
- The idea is already validated and needs requirements. Use `prd-writing`.

## Inputs
Required:
- The idea: who it serves and what it offers.

Optional, improves quality:
- Canvas preference (Business Model Canvas for established or partner-heavy models, Lean Canvas for early-stage or uncertain problems).
- Research, early traction, cost data, partner options.

If the idea is missing, ask. If no canvas is specified, choose Lean Canvas for pre-product-market-fit ideas and say why.

## Process
1. Choose the canvas and state the reason.
2. Fill customer segments first, naming early adopters specifically.
3. Fill problem (Lean) or value propositions (BMC): top 3 problems and existing alternatives; the value proposition must tie to a problem.
4. Fill solution / key activities, channels and customer relationships.
5. Fill revenue streams and cost structure with models and drivers, not invented figures. Use `[ASSUMPTION]` for price points.
6. Fill key metrics (Lean) or key resources and partners (BMC); for Lean, fill unfair advantage honestly, "none yet" is valid.
7. Tag every entry as E (evidence, cite source) or A (assumption).
8. Check internal consistency: channel fits segment, revenue model fits relationship type, costs support the activities.
9. Rank assumptions by risk (impact if wrong x uncertainty) and propose a cheap test for the top 3.
10. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `assumption-mapping` or `hypothesis-statement` for the riskiest blocks, or `pricing-analysis` if revenue streams are the open question.

## Output format
```markdown
# <Lean Canvas | Business Model Canvas>: <idea>
Canvas choice: <reason>

| Block | Content | E/A | Source / note |
|---|---|---|---|
| Customer segments (early adopters) | ... | ... | ... |
| Problem / existing alternatives | ... | ... | ... |
| Unique value proposition | ... | ... | ... |
| Solution | ... | ... | ... |
| Channels | ... | ... | ... |
| Revenue streams | ... | ... | ... |
| Cost structure | ... | ... | ... |
| Key metrics | ... | ... | ... |
| Unfair advantage | ... | ... | ... |

## Consistency Notes
- ...

## Riskiest Assumptions and Tests
| # | Assumption | Risk | Cheapest test | Success signal |
|---|---|---|---|---|
```

## Quality checklist
- [ ] Every block is tagged evidence or assumption.
- [ ] Early adopters are specific enough to find and contact.
- [ ] Revenue and cost blocks name models and drivers, no invented numbers.
- [ ] The value proposition maps to a stated problem.
- [ ] The top 3 risky assumptions each have a test and a success signal.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Filling every block with confident text. A canvas without assumptions flagged hides risk.
- Listing "everyone" as the segment. Two-sided markets need both sides as separate segments.
- Claiming an unfair advantage that is really a feature. Features can be copied.

## Example
Input: "Marketplace connecting freelance accountants with small e-commerce sellers."

Excerpt of output:
- Segments: sellers on marketplaces with <10 staff doing their own bookkeeping (A); freelance accountants with spare capacity (A).
- Revenue: commission on first-year engagement `[ASSUMPTION]` vs seller subscription — to be tested.
- Riskiest assumption: sellers trust a platform-matched accountant; test: concierge matching for 10 sellers, success = 6 sign engagement.
