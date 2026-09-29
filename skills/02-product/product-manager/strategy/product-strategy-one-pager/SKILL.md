---
name: product-strategy-one-pager
description: "Writes a one-page product strategy that states the diagnosis, where to play, how to win, the few strategic bets and explicit non-goals, linked to vision and outcome metrics. Use when a product needs a strategy for the next 12-24 months, when a roadmap lacks a rationale, or when leadership asks \"what is our product strategy\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: strategy
  title: "Write a product strategy one-pager"
  related: "product-vision, market-analysis, competitor-analysis, okr-definition, roadmap"
  prompt: "Draft a product strategy one-pager for our B2B field service app for the next 18 months."
---

# Write a Product Strategy One-Pager

## Purpose
Condense a product's strategic choices onto one page: what challenge it faces, where it will compete, why it will win there, which bets it makes and what it deliberately will not do. This gives teams a filter for roadmap and prioritization decisions.

## When to use
- Annual or half-year planning, or before building a roadmap.
- A roadmap exists but nobody can explain why these items and not others.
- A new leader, market shift or competitor move requires the strategy to be restated.

## When not to use
- The long-term purpose itself is unclear. Use `product-vision` first.
- You need measurable quarterly targets from this strategy. Use `okr-definition`.
- You need the sequenced plan of initiatives. Use `roadmap`.

## Inputs
Required:
- Product, its current situation (users, traction, main problems) and the strategy horizon.

Optional, improves quality:
- Vision, company strategy and constraints (budget, headcount, regulation).
- Market and competitor analysis, customer research, key metrics.
- Previous strategy and what happened to it.

If the product situation or horizon is missing, ask for it.

## Process
1. Write the diagnosis: the one or two critical challenges or opportunities, grounded in evidence. A strategy without a diagnosis is a wish list.
2. Define where to play: target segments, use cases, geographies and channels, and which ones are excluded.
3. Define how to win: the advantage that is hard to copy (data, distribution, integration depth, cost, experience). Check it against competitors.
4. Choose 2-4 strategic bets: each with the rationale, the outcome it should move and the signal that would prove it wrong.
5. Write non-goals: attractive things you will not do in this horizon and why.
6. Link each bet to an outcome metric (North Star or input metric); mark targets `[TBD]` if not agreed.
7. List capabilities or investments needed (team skills, platform work, partnerships) and key risks.
8. Check coherence: bets support how-to-win; non-goals do not contradict bets; the whole fits available capacity.
9. Keep it to one page; move detail to appendices or linked documents.
10. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `okr-definition` to turn the bets into measurable goals, or `roadmap` to sequence them.

## Output format
```markdown
# Product Strategy: <product> (<horizon>)
**Vision link:** <one line>

## Diagnosis
<critical challenge/opportunity with evidence>

## Where to Play
- Focus: ...
- Excluded: ...

## How to Win
<differentiating advantage and why it is defensible>

## Strategic Bets
| Bet | Rationale | Outcome metric | Kill signal |
|---|---|---|---|

## Non-Goals
- <thing> — <why not now>

## Required Capabilities and Risks
- ...

## Open Questions
1. <question> — <owner>
```

## Quality checklist
- [ ] The diagnosis names a real challenge and cites evidence or marks `[ASSUMPTION]`.
- [ ] Where-to-play explicitly excludes at least one attractive segment or use case.
- [ ] Each bet has an outcome metric and a kill signal.
- [ ] Non-goals are things someone actually wants, not straw men.
- [ ] No invented market sizes, revenue or targets.
- [ ] It fits on one page.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing goals ("grow revenue 30%") and calling it strategy. Strategy is the choice of how, given a diagnosis.
- Listing features as bets. A bet is a hypothesis about value and advantage; features come later.
- Leaving non-goals empty. Without them teams cannot say no.

## Example
Input: "B2B field service app, strong with mid-size HVAC firms, losing deals to all-in-one suites, 18-month horizon."

Excerpt of output:
- Diagnosis: Buyers increasingly consolidate tools; our standalone scheduling loses when finance and CRM are bundled `[confirm win/loss data]`.
- Where to play: Mid-size trade service firms (HVAC, plumbing); excluded: enterprise utilities.
- Bet: Deep accounting integrations instead of building our own invoicing — outcome: win rate vs suites — kill signal: no win-rate change after two quarters.
