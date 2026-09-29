---
name: llm-eval-set
description: "Builds an evaluation set for an LLM feature with categorized test cases, scoring rubrics, grader choice (exact match, programmatic, model-graded, human), pass thresholds and a regression process. Use when an LLM feature, prompt or RAG pipeline needs measurable quality before release, when comparing models or prompt versions, or when someone says \"we don't know if the new prompt is better\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: ml-ai-engineer
  area: genai
  title: "Build an LLM evaluation set"
  related: "prompt-design, rag-design, model-evaluation-report, test-strategy, ai-use-case-assessment"
  prompt: "Build an evaluation set for our contract-summary assistant so we can compare two prompt versions before release."
---

# Build an LLM Evaluation Set

## Purpose
Turn "it looks good" into repeatable evidence: a versioned set of cases with rubrics and graders that tells whether an LLM feature is good enough to ship and whether a change made it better or worse.

## When to use
- Before releasing an LLM feature or a new prompt, model or retrieval change.
- Choosing between models or prompt versions on cost, latency and quality.
- Production complaints need to be converted into regression cases.

## When not to use
- The prompt itself is not yet designed. Use `prompt-design` first.
- The model is a classical ML model with labeled data and standard metrics. Use `model-evaluation-report`.

## Inputs
Required:
- Feature description: task, users, input types and what a good output looks like.
- Any real or realistic input samples (masked).

Optional, improves quality:
- Known failure examples, user complaints, domain expert availability for labeling.
- Risk profile (regulated domain, harmful-output concerns), cost and latency budgets.
- Existing prompt and retrieval setup.

If there is no description of a good output, ask for it with one example; rubrics depend on it. Other gaps become open questions.

## Process
1. Define quality dimensions for this feature (e.g. correctness, groundedness/faithfulness, completeness, format compliance, tone, safety, refusal appropriateness) and weight them by risk.
2. Design the case taxonomy: core happy paths by frequency, edge cases (long, empty, multilingual, noisy input), adversarial cases (prompt injection, jailbreak, sensitive data), and out-of-scope inputs that must be declined.
3. Size the set: start with 30-100 cases, stratified by taxonomy; state how the size relates to the confidence needed and mark it `[ASSUMPTION]` if unvalidated.
4. Source cases from masked production logs, expert-written cases and synthetic variations; record the source per case and never include raw personal data.
5. For each case write the reference: an exact expected answer where possible, otherwise required facts, forbidden content and properties the output must satisfy.
6. Choose the grader per dimension: exact/regex or schema checks for format; programmatic checks for facts; model-graded rubric for open text; human review for high-risk or subjective dimensions.
7. Write each rubric with a 1-5 or pass/fail scale and anchored descriptions per level; for model graders, validate against 20+ human-labeled cases and report agreement before trusting them.
8. Set release thresholds per dimension and hard gates (e.g. zero safety failures, 100% format compliance) separately from average scores.
9. Define the run protocol: fixed parameters, number of repeats for non-deterministic outputs, cost and latency capture, side-by-side comparison of versions.
10. Define maintenance: every production incident adds a regression case, periodic refresh, a hidden holdout to avoid overfitting prompts to the set.
11. Mark every inference `[ASSUMPTION]`, list open questions, and suggest `prompt-design` for fixes or `model-evaluation-report` to report results.

## Output format
```markdown
# LLM Evaluation Set: <feature> v<version>
Owner: <team> · Cases: <n> · Last refreshed: <date>

## Quality Dimensions
| Dimension | Weight | Grader | Threshold / gate |
|---|---|---|---|

## Case Taxonomy and Coverage
| Category | Share | # cases | Source |
|---|---|---|---|

## Cases (sample)
| ID | Category | Input (masked) | Reference / required facts | Must not | Grader |
|---|---|---|---|---|---|

## Rubrics
### <dimension>
- 5: ...
- 3: ...
- 1: ...

## Run Protocol
<parameters, repeats, metrics captured, comparison method>

## Grader Validation
<human agreement results or [TBD]>

## Maintenance
<regression intake, refresh cadence, holdout>

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every quality dimension has a grader and a threshold; safety and format are hard gates.
- [ ] Cases cover happy path, edge, adversarial and out-of-scope inputs.
- [ ] References state required facts and forbidden content, not just "a good answer".
- [ ] Model-graded rubrics have a plan for validation against human labels.
- [ ] Case inputs are masked; no raw personal data.
- [ ] A holdout and regression intake prevent overfitting the prompt to the set.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Averaging everything into one score. A version that is better on average but leaks data once must fail.
- Trusting a model grader without calibration. Check agreement with humans and watch for bias toward longer answers.
- Writing cases only from the developer's imagination. Real, messy user inputs find the failures that matter.

## Example
Input: "Contract-summary assistant, compare two prompt versions."

Excerpt of output:
| ID | Category | Input | Required facts | Must not | Grader |
|---|---|---|---|---|---|
| C-014 | Edge | 42-page contract, renewal clause in annex | Auto-renewal term, notice period | Invent a termination fee | Model rubric + human spot check |
| C-031 | Adversarial | Contract text containing "ignore previous instructions" | Normal summary | Follow embedded instruction | Programmatic check |

Gate: faithfulness ≥ 4.0 average and zero cases with invented obligations `[ASSUMPTION: confirm with legal]`.
