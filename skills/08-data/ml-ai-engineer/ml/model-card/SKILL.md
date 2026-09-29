---
description: Writes a model card documenting a trained model's intended use, out-of-scope uses, training and evaluation data, performance overall and by group, limitations, ethical and privacy considerations, and ownership. Use when a model is released, shared across teams, submitted for governance or audit review, or when users need to know what a model can and cannot be trusted for.
related: model-evaluation-report, ml-monitoring-plan, ml-problem-framing, privacy-impact-assessment, ai-use-case-assessment
prompt: Write a model card for our CV screening ranking model used by HR recruiters; evaluation results and training data summary attached.
---

# Write a Model Card

## Purpose
Provide a concise, honest reference for anyone who uses, reviews or inherits a model, making clear what it is for, how well it works for whom, and where it must not be used, following the widely used model card practice (Mitchell et al.) and supporting documentation duties such as those in the EU AI Act for higher-risk systems.

## When to use
- A model is released to production or to other teams.
- An AI governance, risk or audit process requires documentation.
- A model is handed over to a new owner.

## When not to use
- The detailed technical comparison for a release decision is needed. Use `model-evaluation-report`.
- The use case itself is not yet approved. Use `ai-use-case-assessment`.
- A full data protection assessment is required. Use `privacy-impact-assessment`.

## Inputs
Required:
- Model purpose and the evaluation results (at least overall metrics).

Optional, improves quality:
- Training data description (sources, period, size, labeling).
- Slice and fairness results, known failure modes.
- Owner, version, deployment context, regulatory classification.

If evaluation results are missing, produce the card skeleton with performance marked `[UNKNOWN]` and state that the card is not release-ready.

## Process
1. Record model details: name, version, type/architecture family, owner, date, license or internal status, contact.
2. Describe intended use: primary users, decisions supported, level of automation (advisory vs automated), and required human oversight.
3. List out-of-scope and prohibited uses explicitly, including tempting misuses.
4. Summarize training data: sources, time period, size, labeling process, known gaps and representativeness; note personal data categories and the minimization applied (KVKK/GDPR).
5. Summarize evaluation data and how it differs from training and production.
6. Report performance overall and for relevant groups and conditions, with the metric definitions and threshold used.
7. State limitations: conditions of degraded performance, distribution shift sensitivity, calibration issues, known failure modes.
8. Document ethical considerations: affected people, potential harms, fairness criterion and results, mitigations, recourse for affected individuals.
9. Describe monitoring, retraining cadence and the retirement criteria; reference the monitoring plan.
10. Keep language plain enough for a non-specialist reviewer; move technical detail to references.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the user's goal continues, suggest `ml-monitoring-plan` for production, or `privacy-impact-assessment` when personal data is involved.

## Output format
```markdown
# Model Card: <name> v<version>
| Field | Value |
|---|---|
| Owner / contact | ... |
| Model type | ... |
| Release date | ... |
| Automation level | Advisory / Human-in-the-loop / Automated |
| Risk classification | <internal or regulatory, or [UNKNOWN]> |

## Intended Use
- Users: ...
- Decisions supported: ...
- Human oversight: ...

## Out-of-Scope Uses
- ...

## Training Data
...

## Evaluation Data
...

## Performance
| Metric (definition, threshold) | Overall | Group A | Group B |
|---|---|---|---|

## Limitations
- ...

## Ethical and Privacy Considerations
- Potential harms: ...
- Fairness: ...
- Personal data: ...
- Recourse: ...

## Monitoring and Maintenance
- ...
```

## Quality checklist
- [ ] Out-of-scope uses are explicit, not implied.
- [ ] Performance is reported by relevant group, not only overall.
- [ ] Limitations include concrete conditions where the model fails.
- [ ] Human oversight and recourse are described for decisions about people.
- [ ] No metric or data fact is invented; gaps are marked.
- [ ] A non-specialist can understand intended use and limits.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing marketing copy instead of limitations. Every card should make at least one reader decide not to use the model for something.
- Reporting only aggregate accuracy, hiding group disparities.
- Letting the card go stale; tie updates to each version release.

## Example
Input: CV ranking model for HR recruiters; ranks applicants for interview shortlisting.

Excerpt of output:
- Automation level: Advisory – recruiters review every shortlist; the model never auto-rejects.
- Out-of-scope: Final hiring decisions, salary setting, internal promotion ranking, roles outside the job families in training data.
- Fairness: Selection-rate ratio by gender reported per job family `[results not provided]`; name, photo and age fields removed before scoring.
