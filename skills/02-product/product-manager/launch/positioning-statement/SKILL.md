---
description: Writes a product or feature positioning statement in the For/Who/Is a/That/Unlike/Our product format, grounded in a specific target segment, a real alternative and a provable differentiator, plus the proof points and messaging guardrails that follow from it. Use when launching a product or major feature, when sales and marketing describe the product inconsistently, or when someone asks "how do we position this" or "what makes us different".
related: value-proposition-canvas, competitor-analysis, persona, go-to-market-plan, elevator-pitch
prompt: Write a positioning statement for our new invoice-matching module aimed at mid-size manufacturers' finance teams.
---

# Write a Positioning Statement

## Purpose
Produce a short, testable statement of who the product is for, what problem it solves, what category it competes in and why it beats the alternative the customer would otherwise choose, so that every launch message, sales pitch and roadmap argument starts from the same claim.

## When to use
- A new product, module or major feature is about to be launched.
- Sales, marketing and product describe the offering differently and deals are lost to confusion.
- The product is being repositioned for a new segment or after a competitor move.

## When not to use
- Customer jobs, pains and gains are not yet understood. Use `value-proposition-canvas` or `jobs-to-be-done` first.
- The need is the full launch plan (channels, timing, enablement). Use `go-to-market-plan`.
- A 30-second spoken pitch is needed. Use `elevator-pitch`, feeding it this statement.

## Inputs
Required:
- The product or feature and what it does.
- The intended target customer or segment (even if rough).

Optional, improves quality:
- Customer research, win/loss notes, reviews, support themes.
- Main competitors or the current workaround (spreadsheets, manual work, doing nothing).
- Evidence: metrics, case results, certifications, benchmarks.
- Brand or messaging guidelines.

If the product or target segment is missing, ask. If the alternative is unknown, propose candidates as `[ASSUMPTION]` and list them as open questions.

## Process
1. Narrow the target: one segment defined by role, context and trigger situation (e.g. "finance teams at mid-size manufacturers closing month-end with 3-way matching"), not a demographic or "everyone". If several segments exist, write one statement per segment.
2. State the need in the customer's words: the costly, frequent problem or job the segment has. Use evidence from inputs; mark inferences `[ASSUMPTION]`.
3. Choose the frame of reference (market category) the customer already understands. It sets expectations and the competitive set, so pick deliberately; note if you are creating a new category and why.
4. Identify the real alternative the customer would use instead: a named competitor, an adjacent tool, an internal build, manual work or inaction.
5. List candidate differentiators and keep only those that are important to the segment, unique or clearly better versus that alternative, and provable. Drop parity features.
6. Attach proof points to each kept differentiator. If no evidence exists, mark `[NEEDS PROOF]` rather than inventing numbers.
7. Assemble the statement: For <target> who <need>, <product> is a <category> that <key benefit>. Unlike <alternative>, our product <primary differentiator>.
8. Derive messaging guardrails: three message pillars, words to use and avoid, claims not allowed without proof.
9. Stress-test: could a competitor sign the same sentence? Would a target customer recognize their problem? Is the benefit an outcome rather than a feature? Revise until each answer supports the statement.
10. List assumptions and open questions, and suggest how to validate (customer interviews, message testing, win/loss review).
11. If the goal continues, suggest `go-to-market-plan` for launch planning, `elevator-pitch` for spoken form, or `release-announcement` for the launch message.

## Output format
```markdown
# Positioning: <product / feature> — <segment>

## Positioning Statement
For <target segment>
who <need / problem>,
<product> is a <market category>
that <key benefit (outcome)>.
Unlike <primary alternative>,
our product <primary differentiator>.

## Building Blocks
| Element | Content | Evidence / source |
|---|---|---|
| Target | ... | ... |
| Need | ... | ... |
| Category | ... | ... |
| Key benefit | ... | ... |
| Alternative | ... | ... |
| Differentiator | ... | <proof or [NEEDS PROOF]> |

## Message Pillars
1. <pillar> — proof: ...
## Words to Use / Avoid
## Assumptions and Open Questions
- [ASSUMPTION] ...
## Validation Plan
```

## Quality checklist
- [ ] The target is a specific segment with a situation, not "businesses" or "users".
- [ ] The key benefit is an outcome the customer values, not a feature list.
- [ ] The alternative is what the customer would really do instead, including a workaround or inaction.
- [ ] A competitor could not credibly sign the same statement.
- [ ] Every differentiator has a proof point or is marked `[NEEDS PROOF]`; no invented metrics.
- [ ] Inferences are labeled and listed under assumptions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Targeting everyone to avoid losing anyone. Broad positioning makes the benefit generic; pick the segment where you win most clearly.
- Using superlatives ("best-in-class", "seamless", "AI-powered") as differentiators. Replace them with a specific, verifiable difference.
- Choosing a category the customer does not recognize. An unfamiliar category forces education before any benefit lands.

## Example
Input: "Invoice-matching module for mid-size manufacturers' finance teams."

Weak: "For businesses who want efficiency, InvoiceX is an innovative AI-powered solution that streamlines finance. Unlike others, it is easy to use."

Strong (excerpt): "For finance teams at mid-size manufacturers who lose days each month-end reconciling supplier invoices against orders and receipts, InvoiceX is an accounts-payable automation module that matches invoices automatically and routes only the exceptions to people. Unlike spreadsheet-based matching, our product reads goods receipts directly from the ERP, so mismatches surface before the close `[NEEDS PROOF: match-rate data from pilot]`."
