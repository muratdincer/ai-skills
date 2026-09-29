---
description: "Prioritizes test effort by assessing product risk items for likelihood and impact, producing a risk matrix, a test depth per item and an execution order. Use when time or people are limited, when deciding what to test first or how deeply, or when stakeholders need to see which risks are covered and which remain."
related: test-strategy, test-plan, regression-selection, risk-register, impact-analysis
prompt: "We have 5 test days for this release. Here are the 14 changes. Tell me what to test first and how deep."
---

# Prioritize Tests by Risk

## Purpose
Direct limited test time at the areas where failure is both likely and costly, and make residual risk explicit so that the release decision is informed rather than hopeful.

## When to use
- The test window is shorter than full coverage requires.
- A release contains many changes of different criticality.
- Stakeholders ask "what have we not tested and what could go wrong?".
- Building the risk section of a test strategy or test plan.

## When not to use
- You need to pick regression tests from a code change footprint. Use `regression-selection`.
- You are managing project delivery risks (people, schedule, budget). Use `risk-register`.
- You need a full testing approach for a product. Use `test-strategy`.

## Inputs
Required:
- List of features, changes, requirements or components to consider.

Optional, improves quality:
- Business criticality, usage volume, regulatory relevance per item.
- Change size, complexity, new technology, developer experience, defect history per area.
- Available test capacity (days, people).

If the list of items is missing, ask for it. Missing factor values are rated with `[ASSUMPTION]` and flagged for confirmation.

## Process
1. Normalize the input into risk items at a consistent granularity (feature or business flow, not individual test cases).
2. Agree on the scale: 1-5 or H/M/L for likelihood and impact, and write one-line definitions so ratings are comparable.
3. Rate likelihood from technical factors: complexity, amount of change, new or unfamiliar technology, integration count, defect history, time pressure.
4. Rate impact from business factors: financial loss, regulatory/legal exposure, number of affected users, data integrity, safety, reputation, workaround availability.
5. Compute risk score (likelihood x impact) and place items on a matrix. Break ties by impact.
6. Map score bands to test depth: e.g. 15-25 thorough (multiple techniques, negative and non-functional tests, independent review), 8-14 standard, 1-7 smoke or accept.
7. Choose techniques per high-risk item (boundary, decision table, state transition, exploratory charter, performance, security).
8. Sequence execution: highest risk first so that the earliest feedback addresses the costliest failures.
9. If capacity is given, fit depth to capacity; list what is reduced or dropped.
10. State residual risk: items tested lightly or not at all, and who must accept that.
11. Recommend re-assessment triggers (scope change, new defects clustering in one area).
12. If the user continues, suggest `test-plan` to schedule the focused effort or `regression-selection` to apply the ratings to a change.

## Output format
```markdown
# Risk-Based Test Prioritization: <release / scope>
Scale: Likelihood 1-5 (<definitions>) · Impact 1-5 (<definitions>)

| # | Risk item | Likelihood (why) | Impact (why) | Score | Depth | Techniques | Order |
|---|---|---|---|---|---|---|---|

## Risk Matrix
<5x5 grid or H/M/L grid listing item numbers>

## Capacity Fit
- Available: <days / people or [UNKNOWN]>
- Reduced or dropped: <items and reason>

## Residual Risk to Accept
| Item | Remaining risk | Acceptance owner |

## Re-assessment Triggers
- ...
```

## Quality checklist
- [ ] Every rating has a short reason; nothing is rated without justification.
- [ ] Likelihood and impact are rated independently (not both from "importance").
- [ ] Items are at a consistent granularity.
- [ ] Highest-risk items are first in execution order.
- [ ] Residual risk and its acceptance owner are explicit.
- [ ] Assumed ratings are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Rating everything high. Force a distribution; if more than a third is top band, recalibrate the scale.
- Ignoring impact of low-change areas that are business critical. Small changes in payment code still deserve depth.
- Treating the assessment as one-off. Re-rate when defects cluster or scope changes.

## Example
Input: "5 test days, 14 changes including new VAT calculation, logo change, export to PDF."

Excerpt of output:
| 1 | New VAT calculation | 4 (new rules, 3 rates) | 5 (legal, invoices) | 20 | Thorough | Decision table, boundary | 1 |
| 9 | Logo change | 1 | 1 | 1 | Smoke | Visual check | 14 |
- Residual risk: PDF export on older browsers not tested; accept by product owner `[TBD]`.
