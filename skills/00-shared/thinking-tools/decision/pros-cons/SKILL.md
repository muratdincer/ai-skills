---
description: Produces a balanced pros and cons analysis for one proposal or a small set of options, weighing each point by impact and likelihood, separating facts from opinions, including the do-nothing baseline and ending with a clear, conditional recommendation. Use for quick decisions, yes/no proposals, or when someone asks for the advantages and disadvantages of an approach before committing.
related: decision-matrix, trade-off-analysis, bias-check, pre-mortem, decision-log
prompt: Give me the pros and cons of moving our weekly release to on-demand releases, and a recommendation.
---

# List Pros and Cons

## Purpose
Give a decision maker an honest, weighted view of what an option brings and costs compared with the status quo, and a recommendation that states what it depends on.

## When to use
- A yes/no proposal or a choice between two or three options needs a quick, fair assessment.
- Someone asks "should we...?" and the answer depends on context.
- A proposal is being championed and needs a balanced counterweight before approval.

## When not to use
- Many options must be scored on several criteria. Use `decision-matrix`.
- The core tension between two qualities (speed vs. safety) must be made explicit. Use `trade-off-analysis`.
- The main worry is how an adopted plan could fail. Use `pre-mortem`.

## Inputs
Required:
- The proposal or options, and the context of the decision (goal or problem it addresses).

Optional, improves quality:
- Constraints, stakeholders, timeline, cost figures, data from past experience.
- The decision maker's priorities or risk appetite.

If the goal behind the proposal is unclear, ask one question about it; pros and cons cannot be weighed without a goal.

## Process
1. Restate the decision, the goal it serves and the baseline: what happens if nothing changes.
2. List pros per option relative to the baseline, from the perspectives of users, team, operations, finance and risk/compliance.
3. List cons the same way, with equal effort; include transition costs (migration, training, dual running) and opportunity cost.
4. Rewrite each point as a concrete effect ("fewer changes per release, so smaller blast radius"), not a label ("less risk").
5. Tag each point as Fact (with source), Expectation (reasoned) or Opinion (stated by someone), and label your own inferences.
6. Weigh each point: impact High/Medium/Low and likelihood High/Medium/Low. Remove or merge trivial and duplicate points.
7. Identify mitigations for the heaviest cons and conditions that would amplify the key pros.
8. Check balance: if one column is much longer, look deliberately for what is missing on the other side.
9. Write the recommendation: go / no-go / go with conditions / defer until <evidence>, with the two or three points that decided it.
10. List open questions and the signals to monitor after the decision.
11. If the user's goal continues, suggest `decision-matrix` if more options appear, `pre-mortem` before execution, or `decision-log` to record the outcome.

## Output format
```markdown
# Pros and Cons: <decision>
**Goal:** ... **Baseline (do nothing):** ...

## Option: <name>
| Pros | Type | Impact | Likelihood |
|---|---|---|---|
| <concrete effect> | Fact – <source> / Expectation / Opinion | H/M/L | H/M/L |

| Cons | Type | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Recommendation
<go / no-go / go with conditions / defer>, because <deciding points>.
Conditions: ...

## Signals to Monitor
- ...

## Open Questions and Assumptions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The do-nothing baseline is stated and points are relative to it.
- [ ] Pros and cons received equal effort; transition and opportunity costs are included.
- [ ] Every point is a concrete effect with a type tag; inferences are labeled.
- [ ] The recommendation names the deciding points and its conditions.
- [ ] No figures are invented; missing ones are `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Counting items instead of weighing them. One high-impact con can outweigh five minor pros.
- Comparing the proposal with an idealized alternative instead of the real baseline.
- Leaving out transition cost because it is temporary. It often decides whether the change happens at all.

## Example
Input: "Should we move from weekly releases to on-demand releases?"

Weak: "Pro: faster. Con: risky. Recommendation: do it."

Strong excerpt:
| Pros | Type | Impact | Likelihood |
|---|---|---|---|
| Fixes reach customers in hours instead of up to 7 days. | Expectation | H | H |
| Smaller change sets make rollback decisions simpler. | Expectation | M | H |

| Cons | Type | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| Manual regression suite (about 2 days per run) cannot keep up. | Fact – team estimate | H | H | Automate the critical-path suite first |

Recommendation: go with conditions, once the critical-path regression suite runs automatically; until then, keep weekly releases with an expedited path for fixes.
