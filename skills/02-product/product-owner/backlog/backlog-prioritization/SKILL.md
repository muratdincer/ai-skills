---
name: backlog-prioritization
description: "Orders backlog items with an explicit, defensible method (WSJF, RICE, value/effort, MoSCoW or cost of delay) and produces a ranked list with scores, rationale, sensitivity notes and items to drop or defer. Use when a product owner must decide what comes next, stakeholders dispute priorities, or someone asks to rank, score or justify backlog order."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-owner
  area: backlog
  title: "Prioritize the backlog"
  related: "backlog-refinement, requirements-prioritization, portfolio-prioritization, roadmap, decision-matrix"
  prompt: "Prioritize these 12 backlog items with WSJF; effort estimates are in the table, value comes from sales and support feedback."
---

# Prioritize the Backlog

## Purpose
Produce a backlog order that stakeholders can inspect and challenge on its inputs rather than on opinions. The output shows which method was used, why, how each item scored and how stable the ranking is.

## When to use
- More candidate items exist than capacity in the next iteration/sprint, release or quarter.
- Several stakeholders push competing requests and the product owner needs a transparent basis.
- The order must be explained to leadership or to the team.

## When not to use
- Items are still vague or oversized. Use `backlog-refinement` first.
- Ranking whole projects or initiatives across a portfolio. Use `portfolio-prioritization`.
- Prioritizing requirements inside one requirements document. Use `requirements-prioritization`.

## Inputs
Required:
- The list of items to prioritize.
- The goal or outcome the order should serve (iteration goal, OKR, release theme). If missing, ask; without it scores are arbitrary.

Optional, improves quality:
- Effort or size estimates, reach/usage data, revenue or cost signals, deadlines, risk notes.
- Preferred method or organizational standard.
- Fixed constraints (regulatory dates, contractual commitments, dependencies).

## Process
1. Choose the method and state why: WSJF when cost of delay varies and deadlines matter; RICE when reach data exists; value/effort 2x2 for a quick first cut; MoSCoW for fixed-date scope negotiation. Use the organization's method if given.
2. Define each scoring dimension with a scale and anchors (e.g. 1, 2, 3, 5, 8, 13 relative to the smallest item) so scores are comparable.
3. Separate non-negotiables (legal deadlines, contractual, security fixes, hard dependencies) and place them first with a label; do not score them into the ranking.
4. Score each remaining item. Cite the evidence behind each score; where there is none, give a provisional score and mark it `[ASSUMPTION]`.
5. Compute the result (WSJF = cost of delay / job size; RICE = reach x impact x confidence / effort) and rank.
6. Check dependencies: an item cannot rank above something it depends on; adjust and note it.
7. Run a sensitivity check: which items change rank if one assumed score moves by one step? Flag them as "rank-sensitive".
8. Identify candidates to defer or drop (lowest scores, no link to the goal) and state the consequence of not doing them.
9. Summarize the top of the list against available capacity if known; otherwise present the cut line as `[TBD]`.
10. If the user's goal continues, suggest `backlog-refinement` to make the top items ready, or `roadmap` to reflect the new order in the plan.

## Output format
```markdown
# Backlog Prioritization: <product> – <date>
Goal served: <goal>
Method: <method> – <why chosen>
Scales: <dimension: anchors>

## Committed First (not scored)
- <item> – <reason: legal/contract/dependency/security>

## Ranked Items
| Rank | Item | <dim 1> | <dim 2> | <dim 3> | Size | Score | Evidence / assumption | Rank-sensitive |
|---|---|---|---|---|---|---|---|---|

## Cut Line
Capacity: <value or [TBD]> → items 1–<n> fit.

## Defer or Drop
- <item> – <consequence of not doing it>

## Decisions Needed
- <decision> – <who> – <by when>
```

## Quality checklist
- [ ] The chosen method and its scale anchors are stated.
- [ ] Every score has evidence or an `[ASSUMPTION]` marker.
- [ ] Mandatory items are separated, not hidden inside scores.
- [ ] No item ranks above an item it depends on.
- [ ] Rank-sensitive items are flagged.
- [ ] Monetary or usage figures appear only if given in the input.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- False precision: presenting WSJF 4.33 vs 4.25 as a real difference. Treat close scores as ties and decide on goal fit.
- Letting "Must" become 80% of MoSCoW scope. Keep Must under roughly 60% of capacity or the plan has no slack.
- Using effort as the only divisor with inflated value for pet items. Anchor value scores against a reference item stakeholders agree on.

## Example
Input: "Items A (export, size 3), B (SSO, size 8), C (GDPR deletion, legal deadline in Q3), D (dark mode, size 2). Goal: reduce churn of enterprise accounts."

Excerpt of output:
- Committed first: C – regulatory deadline, not scored.
| 1 | B SSO | BV 8 | TC 5 | RR 8 | 8 | 2.6 | Enterprise churn interviews cite SSO | Yes |
| 2 | A Export | 3 | 2 | 3 | 3 | 2.7 | Tie with B (2.6); B kept first for goal fit | No |
- Defer: D dark mode – no link to enterprise churn goal.
