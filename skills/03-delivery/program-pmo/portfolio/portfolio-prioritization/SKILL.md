---
description: Prioritizes a portfolio of projects or initiatives by scoring them on value, strategic fit, risk and effort, checking the ranked list against real capacity and dependencies, and producing a funded / queued / stopped recommendation with rationale. Use when there are more initiatives than capacity, during annual or quarterly portfolio planning, when a new demand must be slotted in, or when leadership asks "what should we fund or stop".
related: decision-matrix, cost-benefit-analysis, okr-definition, program-roadmap, steering-committee-pack
prompt: Prioritize these 12 initiatives for next year; we have roughly 6 delivery teams and the strategy is to grow digital sales and cut operating cost.
---

# Prioritize a Project Portfolio

## Purpose
Turn a list of competing initiatives into a transparent, capacity-feasible ranking with a clear fund, queue or stop decision for each, so that leadership commits the organization's limited delivery capacity to the work that best serves strategy.

## When to use
- Annual or quarterly portfolio planning with more demand than capacity.
- A significant new initiative must be inserted and something has to move.
- The portfolio has grown by accretion and needs a stop/continue review.

## When not to use
- The items are features or backlog items inside one product. Use `backlog-prioritization` or `requirements-prioritization`.
- One initiative's business case is being built. Use `cost-benefit-analysis` or `feasibility-study`.
- Only a single choice between a few options is needed. Use `decision-matrix`.

## Inputs
Required:
- The list of initiatives with a short description of each.
- The strategic objectives the portfolio must serve (or permission to infer them, labeled).

Optional, improves quality:
- Estimates of value, cost/effort, duration, and which teams or skills each needs.
- Available capacity by team or skill for the planning period.
- Mandatory items (regulatory, contractual, end-of-support), dependencies, in-flight status and sunk cost.
- The organization's existing scoring model or weights.

If the list or objectives are missing, ask. Mark missing estimates `[UNKNOWN]` and keep them visible rather than scoring them as zero.

## Process
1. Normalize the list: one line per initiative with owner, objective served, stage (idea, approved, in flight) and a one-line outcome. Merge duplicates and split bundles that hide separable scopes.
2. Separate mandatory items (regulatory, contractual, security, end-of-support) from discretionary ones; mandatory items consume capacity first but still get sized.
3. Agree scoring criteria and weights with the user, or propose a default and label it `[ASSUMPTION]`: business value, strategic fit, time criticality, risk reduction/opportunity enablement, delivery risk (inverse), effort/cost. Define a 1-5 anchor for each score so ratings are comparable.
4. Score each initiative, citing the evidence or estimate behind each score. Mark scores based on inference `[ASSUMPTION]` and confidence Low/Medium/High.
5. Compute a weighted score and, where effort is known, a value-to-effort ratio (e.g. WSJF-style cost of delay divided by size). Keep the formula visible.
6. Check sensitivity: would the top and cut-line positions change if one weight changed moderately or low-confidence scores moved by one point? Flag unstable rankings.
7. Fit to capacity: fill available capacity per team/skill in rank order, respecting dependencies and in-flight commitments. Draw the cut line where capacity ends, not where scores end.
8. Assign a decision to each item: Fund now, Queue (with trigger to start), Rescope, Stop/Do not start. Ignore sunk cost when recommending stops; state the exit cost instead.
9. Summarize trade-offs: what the organization explicitly will not do, and which objectives are under-served by the result.
10. List assumptions, data gaps and decisions needed from the portfolio owner or board.
11. If the goal continues, suggest `program-roadmap` to sequence funded work, `steering-committee-pack` to take decisions to the board, or `benefits-realization` to set up benefit tracking.

## Output format
```markdown
# Portfolio Prioritization: <portfolio> — <period>
Objectives: <list> · Capacity: <teams/FTE/budget or [UNKNOWN]>

## Scoring Model
| Criterion | Weight | 1 = | 5 = |
|---|---|---|---|

## Ranked Portfolio
| Rank | Initiative | Mandatory | Value | Fit | Time crit. | Risk red. | Delivery risk | Effort | Weighted | Confidence | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Capacity Fit
| Team / skill | Available | Demand (funded) | Gap |
|---|---|---|---|
Cut line after: <initiative>

## Sensitivity Notes
## Trade-offs (what we will not do)
## Assumptions and Data Gaps
- [ASSUMPTION] ...
## Decisions Needed
1. <decision> — <by whom> — <by when>
```

## Quality checklist
- [ ] Scoring anchors and weights are explicit and agreed or labeled `[ASSUMPTION]`.
- [ ] Every score has evidence or an assumption and a confidence level; missing data is `[UNKNOWN]`, not zero.
- [ ] Mandatory items are separated and sized.
- [ ] The cut line is based on capacity and dependencies, not on score alone.
- [ ] Every initiative has a decision, and stops are justified without sunk-cost reasoning.
- [ ] Sensitivity of the cut line is stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating the weighted score as the answer. Scores inform a decision; capacity, dependencies and risk balance decide it.
- Funding everything at partial capacity. Starting more than capacity allows extends every lead time; queue instead.
- Letting the loudest sponsor set the inputs. Use anchored scales and ask for evidence behind high ratings.

## Example
Input: "12 initiatives, 6 teams, objectives: grow digital sales, cut operating cost."

Excerpt of output:
| Rank | Initiative | Mandatory | Weighted | Confidence | Decision |
|---|---|---|---|---|---|
| — | e-Invoice regulation update | Yes | n/a | High | Fund now (2 teams, Q1) |
| 1 | Mobile checkout redesign | No | 4.3 | Medium | Fund now |
| 2 | Warehouse slotting automation | No | 4.1 | Low `[ASSUMPTION: savings estimate unvalidated]` | Fund now, gate after discovery |
| 6 | Loyalty app v2 | No | 3.2 | Medium | Queue: start when checkout team frees up |

Sensitivity: ranks 5-7 swap if strategic-fit weight moves from 25% to 20%; decide the cut line explicitly with the board.
