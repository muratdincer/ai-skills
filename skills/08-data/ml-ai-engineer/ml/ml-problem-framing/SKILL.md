---
name: ml-problem-framing
description: "Frames a business need as a machine learning problem - decision supported, prediction target and label, unit and timing of prediction, features available at prediction time, success metrics (offline and business), baseline, data feasibility and go/no-go. Use when someone proposes \"let's use ML/AI to predict X\", before any data work or model selection starts."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: ml-ai-engineer
  area: ml
  title: "Frame an ML problem"
  related: "ai-use-case-assessment, feature-engineering-plan, model-evaluation-report, analysis-plan, problem-statement"
  prompt: "Frame this as an ML problem: the collections team wants to predict which customers will not pay their invoice on time so they can call them earlier."
---

# Frame an ML Problem

## Purpose
Turn a vague "use ML for X" idea into a precise, testable problem definition with a label, a decision, a baseline and success criteria, so the team knows whether ML is justified and what "good enough" means before investing in modeling.

## When to use
- A business team asks for a prediction, classification, ranking or forecasting capability.
- A data science project is being kicked off or re-scoped.
- A model exists but nobody agrees what it is optimizing.

## When not to use
- The question is whether an AI initiative is worth doing at all across value, risk and readiness. Use `ai-use-case-assessment`.
- The problem is generative (text, summaries, chat). Use `prompt-design` or `rag-design`.
- The need is a one-off explanatory analysis. Use `analysis-plan`.

## Inputs
Required:
- The business need and the decision or process the prediction would change.

Optional, improves quality:
- Available data sources and history length.
- Current process and its performance (the implicit baseline).
- Cost of errors, volume, latency and regulatory constraints.

If the decision or process is missing, ask; ML without a decision is not framed.

## Process
1. Write the decision: who acts, on what, when, and what they do differently with a prediction.
2. Define the target precisely: entity, event, observation window and label rule (e.g. "invoice paid > 15 days after due date"). Note label delay and label noise.
3. Define the prediction point: when the model is called and what data is available at that moment; this defines the leakage boundary.
4. Choose the ML task type (binary/multiclass classification, regression, ranking, forecasting, anomaly detection) and justify it from the decision.
5. Define a non-ML baseline (current rule, heuristic, last-period value) and the metric it achieves or `[UNKNOWN]`.
6. Define success: offline metric aligned to the decision (e.g. precision at top-k capacity, recall at fixed precision, MAE, calibration), and the business KPI with target. Write the cost of false positives vs false negatives.
7. Assess feasibility: label volume and class balance, history length versus seasonality, feature availability, data access and privacy constraints (KVKK/GDPR, lawful basis, sensitive attributes).
8. Identify risks: feedback loops (model actions change future labels), fairness on protected groups, concept drift, explainability requirements, automation of adverse decisions.
9. Define deployment shape: batch vs real-time, latency, volume, human-in-the-loop, fallback when the model is unavailable.
10. Give a go / no-go / do-a-spike recommendation with the smallest experiment that would reduce uncertainty.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the user's goal continues, suggest `feature-engineering-plan` on a go decision, or `ai-use-case-assessment` if the business case is still open.

## Output format
```markdown
# ML Problem Frame: <name>
| Field | Value |
|---|---|
| Decision supported | <who does what when> |
| Task type | ... |
| Prediction point | <trigger, data cutoff> |
| Target / label | <precise rule, window> |
| Unit of prediction | ... |

## Baseline
<current approach and its performance or [UNKNOWN]>

## Success Criteria
- Offline: <metric, threshold>
- Business: <KPI, target or [TBD]>
- Error costs: FP = ..., FN = ...

## Feasibility
| Aspect | Status | Notes |
|---|---|---|
| Label volume / balance | ... | ... |
| Feature availability at prediction time | ... | ... |
| Data access / privacy | ... | ... |

## Risks
- ...

## Deployment Shape
<batch/real-time, latency, human review, fallback>

## Recommendation
Go / No-go / Spike: <smallest next experiment>

## Open Questions
1. ...
```

## Quality checklist
- [ ] The prediction is tied to a concrete action and actor.
- [ ] The label rule is precise and computable from historic data.
- [ ] Only data available at prediction time is assumed as input.
- [ ] A non-ML baseline is defined.
- [ ] The offline metric reflects the business error costs and capacity.
- [ ] Privacy, fairness and feedback-loop risks are addressed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Optimizing accuracy on imbalanced classes. Use metrics tied to capacity (precision@k) and cost.
- Framing a label that is only known long after the decision is needed without accounting for label delay.
- Skipping the baseline; many "ML wins" are beaten by a simple rule.

## Example
Input: "Collections wants to predict which customers will not pay on time so they can call earlier."

Excerpt of output:
- Decision: Each morning, the collections team calls the top N open invoices ranked by risk, 7 days before due date.
- Label: Invoice paid more than 15 days after due date or unpaid at day 45 `[confirm threshold with finance]`.
- Offline metric: Precision at N = daily call capacity `[UNKNOWN]`; baseline = current rule "customers late last quarter".
- Risk: Calls change payment behavior, so future labels are influenced by the model; keep a random holdout.
