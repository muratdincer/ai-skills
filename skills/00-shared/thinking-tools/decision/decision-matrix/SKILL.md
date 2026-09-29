---
name: decision-matrix
description: "Builds a weighted decision matrix that compares options against agreed, independent criteria with explicit weights, scoring scales and must-have knock-out rules, then tests how sensitive the result is to weights and uncertain scores. Use when choosing between three or more options (vendors, technologies, designs, candidates for investment), when a decision must be defensible to others, or when a group needs to converge."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "Build a weighted decision matrix"
  related: "trade-off-analysis, pros-cons, vendor-evaluation, technology-selection, decision-log"
  prompt: "Build a weighted decision matrix to choose between three message brokers for our order platform."
---

# Build a Weighted Decision Matrix

## Purpose
Turn a multi-option choice into a transparent, reproducible comparison, so the decision rests on explicit criteria and weights that stakeholders can challenge, rather than on whoever argues best.

## When to use
- Three or more options must be compared on several criteria.
- The decision will be audited, reviewed or questioned later.
- Stakeholders value different things and need a shared frame to converge.

## When not to use
- Only two options, or a yes/no choice, need a quick balanced view. Use `pros-cons`.
- The key question is what each option sacrifices rather than which scores highest. Use `trade-off-analysis`.
- The choice is a formal vendor procurement with RFP scoring rules. Use `vendor-evaluation`.

## Inputs
Required:
- The decision to make and the options (at least two; ideally three or more).

Optional, improves quality:
- Criteria and weights stakeholders already agreed.
- Facts per option (cost, capabilities, references, test results).
- Hard constraints (budget ceiling, regulation, compatibility).

If the decision or options are missing, ask for them. If criteria are missing, propose them and mark them `[PROPOSED — confirm]`.

## Process
1. State the decision as a question with its scope and decision owner ("Which broker will the order platform use for the next 3+ years?").
2. List must-have constraints as knock-out criteria (pass/fail). Options that fail are removed before scoring, with the reason recorded.
3. Define 4-8 scored criteria that are independent (no double counting), measurable or at least describable, and relevant to the goal. Include cost, risk and operability, not only features.
4. Assign weights summing to 100, with a one-line reason each. Weights come from stakeholders; proposed weights are marked `[PROPOSED]`.
5. Define the scoring scale (for example 1-5) with anchors per criterion ("5 = managed service with SLA; 1 = self-hosted, no in-house skills").
6. Score each option per criterion, citing the evidence. Unknown facts get a conservative score marked `[UNVERIFIED]`.
7. Compute weighted totals and rank; show the arithmetic.
8. Run sensitivity checks: swap the two highest weights, set each `[UNVERIFIED]` score to its plausible best and worst; note whether the winner changes.
9. Write the recommendation, the margin of victory, the conditions under which the ranking flips, and what the winner gives up.
10. List open questions and the facts that would most reduce uncertainty.
11. If the user's goal continues, suggest `decision-log` or `adr` to record the decision, or `trade-off-analysis` when the top options are close.

## Output format
```markdown
# Decision Matrix: <decision question>
Decision owner: <role or [UNKNOWN]> · Scale: 1-5 (anchors below)

## Knock-out Criteria
| Constraint | Option A | Option B | Option C |
|---|---|---|---|
| <must-have> | Pass | Pass | Fail – <reason> |

## Weighted Scores
| Criterion (weight) | Option A | Option B |
|---|---|---|
| <criterion> (30) | 4 – <evidence> | 3 – <evidence> [UNVERIFIED] |
| **Weighted total** | **x.xx** | **x.xx** |

## Scoring Anchors
- <criterion>: 5 = ..., 3 = ..., 1 = ...

## Sensitivity
- <change> -> winner <unchanged / changes to B>

## Recommendation
<option>, because ... Margin: ... It gives up: ... Ranking flips if: ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Knock-out criteria are applied before scoring.
- [ ] Criteria do not overlap; cost, risk and operability are represented.
- [ ] Weights sum to 100 and each has a reason; proposed weights are marked.
- [ ] Every score cites evidence or is marked `[UNVERIFIED]`; no facts are invented.
- [ ] Sensitivity analysis states whether the winner is robust.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Choosing weights after seeing scores to justify a favorite. Fix weights first, and state if they were changed.
- Counting the same benefit twice ("performance" and "throughput"). Merge overlapping criteria.
- Presenting a 0.1 difference as a clear win. Call it a tie and decide on the key trade-off.
- Scoring unknown capabilities optimistically. Unknown is a risk; score conservatively and flag it.

## Example
Input: "Choose between three message brokers for our order platform."

Excerpt of output:
| Criterion (weight) | Managed broker A | Self-hosted B | Streaming platform C |
|---|---|---|---|
| Ordering and delivery guarantees (25) | 4 | 4 | 5 |
| Operability with current team (25) | 5 – managed service | 2 – no in-house skills | 3 [UNVERIFIED] |
| Cost over 3 years (20) | 3 [PROPOSED estimate needed] | 4 | 2 |

Sensitivity: if operability weight drops to 10, C overtakes A; the recommendation depends on the team's operating capacity.
