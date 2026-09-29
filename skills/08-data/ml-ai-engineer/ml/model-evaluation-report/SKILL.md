---
name: model-evaluation-report
description: "Writes a model evaluation report that compares a candidate model against baseline and incumbent - overall metrics with uncertainty, threshold choice, calibration, slice performance, error analysis, fairness and a release recommendation. Use when a model is trained and must be approved for deployment, compared with alternatives, or reviewed after a performance complaint."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: ml-ai-engineer
  area: ml
  title: "Write a model evaluation report"
  related: "ml-problem-framing, model-card, ml-monitoring-plan, feature-engineering-plan, llm-eval-set"
  prompt: "Write a model evaluation report for our fraud model v3 vs v2; here are the test-set metrics, confusion matrices and slice results by channel and country."
---

# Write a Model Evaluation Report

## Purpose
Give decision makers an honest, reproducible picture of how a model performs, where it fails and whether it is better than what exists, so the release decision is based on evidence rather than a single headline metric.

## When to use
- A new or retrained model is a release candidate.
- Several model variants must be compared.
- Users report poor predictions and the model needs re-evaluation.

## When not to use
- The problem, label and success metric are not defined. Use `ml-problem-framing`.
- The model is an LLM feature evaluated with rubrics. Use `llm-eval-set`.
- A public-facing summary of use and limits is needed. Use `model-card`.

## Inputs
Required:
- Evaluation results for the candidate (metrics, confusion matrix or predictions summary) and the comparison point (baseline or incumbent).

Optional, improves quality:
- Evaluation data description (period, size, split method).
- Slice results, calibration data, latency and cost measurements.
- Business thresholds and error costs.

If there is no comparison point, state that the recommendation is limited and ask for the baseline. Never invent metric values.

## Process
1. Describe the evaluation setup: data period, split (time-based, grouped), size, label definition and any difference from production distribution.
2. Report primary and secondary metrics for candidate, incumbent and baseline side by side, with confidence intervals (bootstrap) or at least sample sizes.
3. Choose and justify the operating threshold from business constraints (capacity, cost of FP/FN, target precision/recall); show the metrics at that threshold, not only threshold-free AUC.
4. Check calibration (reliability curve, Brier score, expected calibration error) if scores are used as probabilities.
5. Evaluate slices: key segments (channel, region, product, new vs existing entities), rare but critical cases, and data-quality strata. Flag slices where the candidate is worse than the incumbent.
6. Do error analysis: sample false positives and false negatives, cluster their causes (label noise, missing features, distribution shift), and propose fixes.
7. Assess fairness where decisions affect people: compare error rates across protected or proxy groups, state the fairness criterion used and its trade-offs.
8. Assess robustness and operational fit: stability across time slices, sensitivity to missing features, latency, memory, inference cost.
9. Check for leakage signals: suspiciously high metrics, dominant single features, performance drop on the most recent slice.
10. Recommend: release, release with conditions (shadow, canary, limited segment), or reject; list conditions and monitoring requirements.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the user's goal continues, suggest `model-card` to document the released model and `ml-monitoring-plan` for the release conditions.

## Output format
```markdown
# Model Evaluation: <model> v<x> vs <comparison>
| Field | Value |
|---|---|
| Task / label | ... |
| Evaluation data | <period, n, split> |
| Operating threshold | <value, rationale> |
| Recommendation | Release / Conditional / Reject |

## Overall Metrics
| Metric | Baseline | Incumbent | Candidate | 95% CI (candidate) |
|---|---|---|---|---|

## Calibration
...

## Slice Performance
| Slice | n | Incumbent | Candidate | Δ | Flag |
|---|---|---|---|---|---|

## Error Analysis
| Error cluster | Share of errors | Likely cause | Proposed fix |
|---|---|---|---|

## Fairness
<criterion, groups, results, trade-off>

## Robustness and Operations
- Stability over time: ...
- Latency / cost: ...

## Conditions and Monitoring
- ...

## Limitations
- ...
```

## Quality checklist
- [ ] Candidate is compared with a baseline and/or incumbent on the same data.
- [ ] Metrics are shown at the chosen operating threshold with uncertainty or n.
- [ ] Slices where the candidate regresses are explicitly flagged.
- [ ] Error analysis gives causes, not just counts.
- [ ] Fairness is assessed or the reason it is not applicable is stated.
- [ ] All numbers come from the provided results.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting only AUC while the business uses a fixed threshold. Report precision/recall at that threshold.
- Averages hiding regressions in small but critical slices.
- Evaluating on a random split when production scores future data.

## Example
Input: Fraud v3 vs v2; PR-AUC 0.61 vs 0.57 on last 8 weeks (time split); at review capacity threshold, precision 0.42 vs 0.39, recall 0.55 vs 0.51; card-not-present slice recall drops 0.62 → 0.58.

Excerpt of output:
- Recommendation: Conditional release – shadow for 2 weeks, then canary; block full rollout until the card-not-present regression is explained.
- Slice flag: Card-not-present recall -0.04 while overall recall +0.04; error sample shows new merchant category codes missing from training `[confirm]`.
