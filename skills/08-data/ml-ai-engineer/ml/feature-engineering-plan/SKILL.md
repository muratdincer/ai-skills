---
description: Plans the features for a predictive model - candidate features by hypothesis, source and availability at prediction time, point-in-time correctness, leakage checks, transformations, encoding, missing-value strategy and validation approach. Use after the ML problem is framed and before model training, or when a model performs suspiciously well and leakage is suspected.
related: ml-problem-framing, data-exploration, model-evaluation-report, source-to-target-mapping, data-quality-rules
prompt: Plan feature engineering for a churn model on a telecom subscription base; prediction is made monthly for the next 60 days.
---

# Plan Feature Engineering

## Purpose
Design a feature set that is predictive, available at prediction time, free of leakage and reproducible in production, so offline results survive deployment.

## When to use
- An ML problem is framed and the team needs a feature backlog.
- Offline metrics look too good to be true.
- Features must be moved from notebooks to a feature pipeline or store.

## When not to use
- The target, prediction point or success metric is not defined yet. Use `ml-problem-framing`.
- The raw data is not yet understood. Use `data-exploration`.
- The task is evaluating a trained model. Use `model-evaluation-report`.

## Inputs
Required:
- The problem frame: target/label rule, prediction point and unit of prediction.
- Available data sources (tables and key fields).

Optional, improves quality:
- Domain knowledge of drivers, existing features, serving constraints (latency, batch vs online).

If the prediction point is missing, ask; leakage cannot be assessed without it.

## Process
1. Restate the prediction point and the label window; draw the timeline (feature window → cutoff → label window).
2. Brainstorm candidate features from domain hypotheses, grouped by family: recency/frequency/monetary, trend and change, behavior/usage, relationship/tenure, context (calendar, region), interactions.
3. For each feature, record source, aggregation window, freshness at serving time and point-in-time retrieval method (as-of joins, snapshot tables, event-time filtering).
4. Run leakage checks: uses data after cutoff? proxies of the label (e.g. "cancellation reason", collections flags)? target-derived encodings computed on the full set? duplicates across train/test for the same entity?
5. Define transformations: log/Box-Cox for skew, ratios, binning, time-since features, rolling statistics; note which models need scaling.
6. Define categorical encoding (one-hot, frequency, target encoding with out-of-fold computation), high-cardinality handling and unseen-category policy.
7. Define missing-value strategy per feature: meaningful missing indicator, imputation rule computed on training data only.
8. Flag sensitive or protected attributes and their proxies (postcode, name-derived gender); decide exclusion or fairness monitoring (KVKK/GDPR).
9. Define validation: time-based split mirroring production, group split by entity, ablation of feature families, importance and stability checks across time slices.
10. Define production parity: same code path for training and serving, feature tests, and monitoring of feature distributions.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the user's goal continues, suggest `model-evaluation-report` once a model is trained, or `data-quality-rules` for feature pipeline checks.

## Output format
```markdown
# Feature Engineering Plan: <model>
Prediction point: ... | Feature window: ... | Label window: ... | Unit: ...

## Candidate Features
| # | Feature | Family | Hypothesis | Source | Window | Available at cutoff? | Leakage risk |
|---|---|---|---|---|---|---|---|

## Transformations and Encoding
| Feature | Transform / encoding | Fit on | Notes |
|---|---|---|---|

## Missing Values
| Feature | Strategy | Indicator? |
|---|---|---|

## Excluded Features
- <feature> – <reason: leakage / sensitive / unavailable online>

## Validation Approach
- Split: ...
- Ablations: ...

## Production Parity and Monitoring
- ...

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every feature is computable using only data before the cutoff.
- [ ] Label proxies and post-outcome fields are explicitly excluded.
- [ ] Encoders and imputers are fit on training folds only.
- [ ] Validation split mirrors how the model is used in time.
- [ ] Sensitive attributes and proxies are addressed.
- [ ] Serving availability and latency are checked per feature.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using the current snapshot of a slowly changing table instead of the as-of value, which leaks the future.
- Random row splits when the same customer appears in train and test.
- Target encoding on the full dataset, inflating offline metrics.

## Example
Input: Telecom churn, monthly prediction for the next 60 days; sources: usage CDR aggregates, billing, support tickets, contract table.

Excerpt of output:
| # | Feature | Family | Available at cutoff? | Leakage risk |
|---|---|---|---|---|
| 3 | Data usage change last 30d vs prior 90d | Trend | Yes | Low |
| 7 | Contract end within 60 days | Relationship | Yes | Low |
| 9 | Port-out request flag | Behavior | No – arrives with churn | High → excluded |
