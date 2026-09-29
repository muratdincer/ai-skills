---
name: product-vision
description: "Writes an inspiring, testable product vision statement and a vision board covering target group, needs, product, and business goals. Use when a new product or major pivot needs a shared north, when teams disagree on what the product is for, or when someone asks for a vision statement, vision board or \"why does this product exist\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: strategy
  title: "Write a product vision"
  related: "product-strategy-one-pager, positioning-statement, north-star-metric, persona, okr-definition"
  prompt: "Write a product vision and vision board for our self-service invoice portal for small business customers."
---

# Write a Product Vision

## Purpose
Produce a short vision statement and a vision board that state who the product serves, which need it addresses and what change it creates. A good vision stays stable for years, guides trade-offs and lets strategy, roadmap and OKRs be checked against it.

## When to use
- A new product, product line or major pivot is starting and teams need one shared direction.
- Stakeholders describe the product in conflicting ways or the roadmap reads like a feature list without a purpose.
- An existing vision is a slogan that cannot guide decisions and must be rewritten.

## When not to use
- You need where-to-play and how-to-win choices for the next 12-24 months. Use `product-strategy-one-pager`.
- You need market-facing differentiation copy. Use `positioning-statement`.
- You need measurable quarterly targets. Use `okr-definition`.

## Inputs
Required:
- The product or product idea and the problem space it addresses.

Optional, improves quality:
- Target users/customers and any research evidence (interviews, personas, data).
- Company mission and strategy, business goals, current state of the product.
- Competitors or alternatives users rely on today.

If the product or problem space is missing, ask for it. Everything else becomes an assumption or open question.

## Process
1. Restate the problem space in one line: whose life or work gets better, and in what situation.
2. Separate the vision (enduring change in the world) from the product (a means) and from goals (business benefit). Keep features out of the vision statement.
3. Identify the target group: primary segment first, secondary segments only if the product truly serves them. Mark unsupported segments `[ASSUMPTION]`.
4. Name the top 1-3 needs or jobs the product addresses; prefer evidence-backed needs and cite the source.
5. Describe the product in 3-5 differentiating characteristics, not a feature list.
6. State business goals the vision enables (revenue, retention, cost, strategic position) qualitatively; never invent figures.
7. Draft 2-3 alternative vision statements (one sentence, under ~25 words, plain language) and pick the one that best passes the checklist.
8. Test the statement: could a competitor say the same? Would it still hold in 3-5 years? Does it help say no to something? Revise until yes/no/yes.
9. Add the "what this vision rules out" list to make trade-offs explicit.
10. List assumptions to validate and open questions with owners.
11. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `product-strategy-one-pager` to decide how to reach the vision, or `north-star-metric` to measure progress toward it.

## Output format
```markdown
# Product Vision: <product>
**Vision statement:** <one sentence>

## Vision Board
| Target group | Needs | Product | Business goals |
|---|---|---|---|
| <primary / secondary segment> | <top needs, with evidence> | <3-5 differentiating traits> | <qualitative goals> |

## What This Vision Rules Out
- ...

## Alternatives Considered
1. <statement> — <why not chosen>

## Assumptions to Validate
- [ASSUMPTION] ... — <how to validate>

## Open Questions
1. <question> — <owner>
```

## Quality checklist
- [ ] The statement is one sentence, jargon-free and contains no feature names.
- [ ] Target group and need are specific enough to exclude someone.
- [ ] Needs are traced to evidence or marked `[ASSUMPTION]`.
- [ ] Business goals are qualitative or sourced; no invented numbers.
- [ ] "Rules out" list contains at least two real trade-offs.
- [ ] The vision can be read aloud in under 15 seconds.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing the mission of the whole company or a marketing tagline. Anchor on this product's users and the change it creates.
- Stuffing every stakeholder's wish into the statement. A vision that includes everything guides nothing.
- Mixing a time-bound target ("by 2027, 1M users") into the vision. Move targets into OKRs or strategy.

## Example
Input: "Self-service invoice portal for small business customers; today they call support to get copies and dispute charges."

Excerpt of output:
- Vision statement: Small business owners understand and settle every invoice on their own, without ever needing to call us.
- Needs: Find past invoices quickly; understand unexpected charges; dispute without waiting on hold (support call logs `[confirm volume]`).
- Rules out: Becoming a general accounting tool; serving enterprise procurement workflows.
