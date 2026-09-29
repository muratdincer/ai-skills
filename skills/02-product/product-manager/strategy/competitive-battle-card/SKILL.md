---
description: Builds a one-page competitive battle card for sales and presales against a named competitor, covering when we win and lose, strengths and weaknesses on both sides, discovery and landmine questions, objection handling with proof points and quick-dismiss answers. Use when sales meets a competitor in deals, before a competitive pitch or RFP, when win/loss notes need to become field guidance, or when someone asks for a "battle card", "kill sheet" or "how do we beat X".
related: competitor-analysis, positioning-statement, pricing-analysis, rfp-response, elevator-pitch
prompt: Build a battle card for our sales team against VendorX; we keep losing mid-size deals to them on price but win when integrations matter.
---

# Build a Competitive Battle Card

## Purpose
Give a salesperson or presales engineer what they need in a live conversation against one competitor: where to steer, what to ask, how to answer objections, and what not to claim, on one page.

## When to use
- A competitor shows up repeatedly in deals or RFPs.
- Win/loss findings or analyst notes must become usable field guidance.
- A new competitor, release or pricing change requires a quick update of sales messaging.

## When not to use
- A broad market-level comparison of many competitors is needed. Use `competitor-analysis`.
- The core positioning of the product is not yet defined. Use `positioning-statement` first.
- A formal response to a specific tender is needed. Use `rfp-response`.

## Inputs
Required:
- The competitor's name and our product/offering.
- At least some evidence about deals against them (win/loss notes, sales feedback, public material the user provides).

Optional, improves quality:
- Target segment and typical buyer roles, pricing information, customer references, recent competitor releases.

If there is no evidence at all, say so, build the card as a hypothesis draft with every claim marked `[UNVERIFIED]`, and list the evidence to gather. Never invent competitor features, prices or customer names.

## Process
1. Fix the context: segment, deal size, buyer roles and the stage where the competitor usually appears.
2. Summarize the competitor in 2-3 lines: their positioning, typical pitch and who they sell best to.
3. From the evidence, list "we win when" and "we lose when" conditions (deal patterns, not features). These drive the whole card.
4. List our 3-5 differentiators that matter to the buyer, each with a proof point (reference, demo, metric, certification) or `[PROOF NEEDED]`.
5. List their real strengths honestly and how to reframe or neutralize each; list their weaknesses with evidence and a verification date or source.
6. Write discovery and landmine questions: neutral questions that make the buyer discover requirements where we are strong (for example "How will you handle updates to your e-invoice integration when regulations change?").
7. Write objection handling for the top 4-6 objections: acknowledge, reframe, prove, and a short quick-dismiss line.
8. Add pricing guidance only from supplied data: how to position total cost, not discount tactics you cannot back.
9. Add "don't say" rules: unverifiable claims, disparagement, legal/confidential information, outdated feature comparisons.
10. Add a freshness line (owner, sources, last-reviewed date as given by the user or `[TBD]`), then suggest `competitor-analysis` for a deeper market view, `pricing-analysis` if losses are price-driven, or `elevator-pitch` for talk tracks.

## Output format
```markdown
# Battle Card: <our product> vs <competitor>
**Segment:** <...> | **Owner:** <...> | **Last reviewed:** <date or TBD> | **Sources:** <...>

## In One Line
<why a buyer in this segment should choose us over them>

## We Win When / We Lose When
| We win when | We lose when |
|---|---|

## Our Differentiators (with proof)
1. <differentiator> – <proof or [PROOF NEEDED]>

## Their Strengths → Our Response
| Their strength | How to reframe / neutralize |
|---|---|

## Their Weaknesses (verified)
- <weakness> – <evidence / source>

## Discovery and Landmine Questions
1. ...

## Objection Handling
| Objection | Response (acknowledge → reframe → proof) | Quick dismiss |
|---|---|---|

## Pricing Guidance
## Don't Say
```

## Quality checklist
- [ ] Every claim about the competitor has a source or is marked `[UNVERIFIED]`; nothing is invented.
- [ ] "We win/lose when" are deal conditions derived from evidence, not feature lists.
- [ ] Their strengths are acknowledged honestly; no disparaging or legally risky wording.
- [ ] Landmine questions are neutral and useful to the buyer, not traps that sound like attacks.
- [ ] The card fits on one page and can be scanned during a call.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A feature checklist where we have every tick. Sales loses credibility the first time the buyer checks.
- Stale cards. Put owner, sources and review date on the card and remove claims older than the last competitor release.
- Answering price objections only with discounts. Reframe to total cost, risk and time to value using supplied evidence.

## Example
Input: "We lose mid-size deals to VendorX on price but win when integrations matter."

Excerpt of output:
| We win when | We lose when |
|---|---|
| Buyer has 3+ systems to integrate and an IT stakeholder in the room | Only a department buyer, single-use case, price is the first filter |

Objection: "VendorX is 30% cheaper." `[figure as reported by sales; verify]`
Weak response: "They are cheap because their product is bad."
Strong response: "That's fair for licence price. Let's compare the cost of the three integrations you listed; in our references those took [PROOF NEEDED: implementation days] with us." Quick dismiss: "Cheaper to buy, or cheaper to run?"
