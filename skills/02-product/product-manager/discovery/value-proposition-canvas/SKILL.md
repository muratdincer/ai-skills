---
description: Fills a value proposition canvas for one customer segment, mapping customer jobs, pains and gains to products and services, pain relievers and gain creators, ranks them by importance, checks problem-solution fit and lists the assumptions to test. Use when defining or sharpening a value proposition, checking whether a product idea addresses real pains, preparing positioning or discovery work, or when someone asks for a "value proposition canvas" or "fit" analysis.
related: jobs-to-be-done, persona, positioning-statement, business-model-canvas, hypothesis-statement
prompt: Fill a value proposition canvas for our expense app for field sales reps at mid-size distributors.
---

# Fill a Value Proposition Canvas

## Purpose
Make explicit which customer jobs, pains and gains a product addresses and how, so the team can see where fit is strong, where it is claimed but unproven, and what to test next.

## When to use
- A new product or feature idea needs a clear value proposition for a specific segment.
- An existing product's messaging is feature-led and needs to connect to customer outcomes.
- Discovery findings (interviews, support tickets) must be linked to product decisions.

## When not to use
- The customer's jobs themselves are not yet understood. Use `jobs-to-be-done` first.
- The whole business (channels, revenue, cost) must be designed. Use `business-model-canvas`.
- A one-sentence market positioning is needed. Use `positioning-statement`.

## Inputs
Required:
- One customer segment (specific role and context) and the product or idea.

Optional, improves quality:
- Research evidence: interview notes, survey results, support data, win/loss notes, analytics.
- Competing alternatives the segment uses today.

If more than one segment is given, ask which to start with; build one canvas per segment. If there is no research evidence, build the canvas as hypotheses and label every item `[ASSUMPTION]`.

## Process
1. Define the segment precisely (role, context, situation) and the product scope under review.
2. Customer jobs: list functional, social and emotional jobs, plus supporting jobs (buying, learning, maintaining). Phrase each as a verb + object + context, without the product.
3. Pains: undesired outcomes, obstacles and risks around the jobs. Make them concrete ("reps retype receipts at night, ~30 min/week `[ASSUMPTION]`"), not vague ("it's slow").
4. Gains: required, expected, desired and unexpected outcomes. Make them measurable where possible.
5. Rank jobs, pains and gains by importance and severity for this segment, and tag each with evidence: `[EVIDENCE: source]` or `[ASSUMPTION]`.
6. Products and services: list what the offering includes (features, service, support, integrations), without marketing wording.
7. Pain relievers: for each top-ranked pain, state how the offering relieves it; gain creators: for each top-ranked gain, state how it creates it. Draw explicit links (pain ↔ reliever, gain ↔ creator).
8. Assess fit: mark each top pain/gain as addressed, partially addressed or not addressed; flag features that map to no job, pain or gain.
9. Compare with the current alternative (including doing nothing): why would the segment switch?
10. List the riskiest assumptions behind the fit with a cheap test for each, write a one-sentence value proposition, and suggest `hypothesis-statement` to formalize tests, `positioning-statement` for messaging or `business-model-canvas` for the wider model.

## Output format
```markdown
# Value Proposition Canvas: <product> for <segment>

## Customer Profile
| Type | Item | Rank | Evidence |
|---|---|---|---|
| Job (functional) | ... | 1 | [EVIDENCE: 6/8 interviews] |
| Pain | ... | 1 | [ASSUMPTION] |
| Gain | ... | 2 | ... |

## Value Map
| Products & services | Pain relievers (→ pain) | Gain creators (→ gain) |
|---|---|---|

## Fit Assessment
| Top pain / gain | Addressed? (Yes / Partly / No) | How | Gap |
|---|---|---|---|
- Features with no link: ...
- Why switch from current alternative: ...

## Value Proposition (one sentence)
For <segment> who <job>, <product> <relieves top pain / creates top gain>, unlike <alternative>.

## Riskiest Assumptions and Tests
| Assumption | Test | Success signal |
|---|---|---|
```

## Quality checklist
- [ ] The canvas covers exactly one specific segment.
- [ ] Jobs, pains and gains are written from the customer's view and do not mention the product.
- [ ] Every item is tagged with evidence or `[ASSUMPTION]`, and items are ranked.
- [ ] Each top pain and gain has an explicit link or is marked as a gap; unlinked features are called out.
- [ ] Riskiest assumptions each have a concrete, cheap test.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Starting from the value map and reverse-engineering pains to fit the features. Fill the customer profile first.
- Generic pains ("wants efficiency"). Write the specific situation, frequency and consequence.
- Mixing segments; a CFO and a field rep have different jobs. One canvas per segment.

## Example
Input: "Expense app for field sales reps at mid-size distributors."

Excerpt of output:
Weak pain: "Expense reporting is annoying."
Strong pain: "Rep loses paper fuel receipts on multi-day routes and pays out of pocket when they cannot be reimbursed" – Rank 1 – `[ASSUMPTION: validate in 5 rep interviews]`.
| Top pain / gain | Addressed? | How | Gap |
|---|---|---|---|
| Lost receipts → unreimbursed cost | Yes | Photo capture at the pump, offline sync | None if OCR works on thermal paper `[test]` |
| Reimbursement within a week | Partly | Faster submission | Approval speed depends on managers, not the app |
