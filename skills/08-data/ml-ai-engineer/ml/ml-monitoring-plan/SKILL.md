---
name: ml-monitoring-plan
description: "Produces a production monitoring plan for a machine learning model covering data and prediction drift, performance decay with delayed labels, data quality, operational health, alert thresholds, owners and retraining triggers. Use when a model is about to go live, after an incident caused by silent model degradation, or when someone asks how to know if a model is still working."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: ml-ai-engineer
  area: ml
  title: "Plan model monitoring"
  related: "model-evaluation-report, model-card, alert-design, observability-plan, feature-engineering-plan"
  prompt: "Write a monitoring plan for our churn model; it scores all customers nightly and we only learn true churn 60 days later."
---

# Plan Model Monitoring

## Purpose
Define what to measure, how often, against which baseline and who acts, so model degradation is detected before the business notices it and retraining happens for a reason rather than on a whim.

## When to use
- A model is moving to production or from shadow to live traffic.
- A model underperformed silently and the team needs detection in place.
- Retraining is done on a fixed calendar and the team wants evidence-based triggers.

## When not to use
- The model is not yet evaluated offline. Use `model-evaluation-report` first.
- The need is infrastructure/service monitoring without model concerns. Use `observability-plan` or `alert-design`.

## Inputs
Required:
- Model purpose, prediction type (class, score, ranking, regression, generative) and serving mode (batch, online, streaming).
- How and when ground-truth labels become available (or that they never do).

Optional, improves quality:
- Offline evaluation results and the training data window (the reference baseline).
- Key features and slices, business KPI the model influences, SLOs of the serving path.
- Existing monitoring stack and on-call structure.

If label availability is unknown, ask; it decides the whole design. Everything else becomes an open question.

## Process
1. Describe the serving context: volume, cadence, latency budget, consumers of predictions, and actions taken on them.
2. Fix the reference baseline: training or validation window, and the statistics to store per feature and for predictions.
3. Define data quality checks at input: schema, null rate, range, category cardinality, freshness; set these as blocking or warning.
4. Define drift monitors: per-feature distribution shift (PSI, KS or Jensen-Shannon; chi-square for categoricals) and prediction distribution shift; prioritize by feature importance so noise from minor features does not page anyone.
5. Define performance monitors on labels: the offline metric, computed per slice, with the label delay stated. When labels are delayed, add leading proxies (prediction drift, business proxy, small human-labeled sample).
6. Add business and fairness monitors: the KPI the model moves, and metric gaps between protected or key segments.
7. Add operational monitors: latency percentiles, error and timeout rate, fallback rate, throughput, cost per prediction.
8. Set thresholds and windows per monitor with a warning and a critical level; mark unvalidated thresholds `[ASSUMPTION]` and plan a calibration period.
9. Map each alert to an owner and a runbook action: investigate, roll back to previous model, switch to fallback rule, or retrain.
10. Define retraining triggers (performance below floor, sustained drift, scheduled refresh with maximum age) and the gate a retrained model must pass before promotion.
11. Specify dashboards, review cadence and log retention; mask personal data in logged features and predictions.
12. Mark every inference as `[ASSUMPTION]` and list open questions. If the user's goal continues, suggest `alert-design` to tune alerts or `model-card` to document monitoring commitments.

## Output format
```markdown
# Model Monitoring Plan: <model name, version>
Serving: <batch/online> · Volume: <n/period> · Label delay: <duration or none> · Owner: <team>

## Baseline
<window, stored statistics>

## Monitors
| # | Layer | Signal | Method / metric | Window | Warning | Critical | Owner | Action |
|---|---|---|---|---|---|---|---|---|
| 1 | Data quality | <feature null rate> | <rule> | <daily> | <x> | <y> | <team> | <block batch / alert> |
| 2 | Drift | <top-k features> | <PSI> | <weekly> | <0.1> | <0.25> | ... | ... |
| 3 | Performance | <metric per slice> | ... | ... | ... | ... | ... | ... |
| 4 | Business / fairness | ... | ... | ... | ... | ... | ... | ... |
| 5 | Operational | <p95 latency> | ... | ... | ... | ... | ... | ... |

## Retraining Triggers and Promotion Gate
- Triggers: ...
- Gate: <offline metric ≥ current model, slice checks, shadow period>

## Fallback and Rollback
<previous version / rule-based fallback, who decides>

## Privacy and Retention
<what is logged, masking, retention period>

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Label delay is stated and leading indicators cover the gap.
- [ ] Every monitor has a threshold, window, owner and concrete action.
- [ ] Drift monitoring is prioritized by feature importance, not applied blindly to all features.
- [ ] Performance and fairness are tracked per slice, not only in aggregate.
- [ ] Retraining has explicit triggers and a promotion gate.
- [ ] Logged personal data is minimized or masked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Alerting on drift alone. Drift without performance impact often needs no action; pair it with performance or business signals.
- Retraining automatically without a gate. A retrained model on corrupted data can be worse; always compare to the champion first.
- Ignoring feedback loops. If the model's actions change future labels (e.g. retention offers), note it and keep a holdout group.

## Example
Input: "Churn model, nightly batch over all customers, true churn known after 60 days."

Excerpt of output:
- Performance: AUC and precision@top-10% per tenure slice, computed monthly on the cohort scored 60 days earlier.
- Leading proxy: weekly PSI on score distribution (warning 0.1, critical 0.25 `[ASSUMPTION: calibrate in first 8 weeks]`).
- Feedback loop: customers who receive a retention offer are excluded from label evaluation; a 5% random holdout gets no offer `[ASSUMPTION]`.
