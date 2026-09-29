---
description: Assesses a proposed AI or machine learning use case on business value, technical feasibility, data readiness, risk (privacy, fairness, safety, regulatory) and operating cost, and gives a scored go / pilot / no-go recommendation with the smallest next experiment. Use when someone proposes "let's use AI for X", when prioritizing a portfolio of AI ideas, or before funding an AI pilot.
related: ml-problem-framing, rag-design, privacy-impact-assessment, cost-benefit-analysis, decision-matrix
prompt: Assess this idea: use an LLM to draft first replies to all incoming customer complaints for our call center agents.
---

# Assess an AI Use Case

## Purpose
Decide early and on evidence whether an AI idea deserves investment, what shape it should take (rules, classical ML, generative AI, or no AI) and which risks must be controlled, before teams commit budget and data.

## When to use
- A business unit proposes an AI feature or automation.
- Several AI ideas compete for the same team or budget and need comparable scores.
- A pilot is about to start and needs explicit success and stop criteria.

## When not to use
- The use case is approved and needs technical framing of target, features and baseline. Use `ml-problem-framing`.
- A full financial business case is required. Use `cost-benefit-analysis` after this assessment.
- The main question is personal data processing. Use `privacy-impact-assessment`.

## Inputs
Required:
- The use case in the proposer's words: task, users, and the decision or output the AI would produce.

Optional, improves quality:
- Current process, volumes, error rates, costs and pain points.
- Available data (sources, labels, quality, ownership), regulatory context, risk appetite.
- Budget, timeline and team skills.

If the task or the affected users are unclear, ask one question at a time. Everything else becomes an open question; never invent volumes or savings.

## Process
1. Restate the use case: literal ask versus underlying need, the decision being automated or assisted, and who acts on the output.
2. Check whether AI is needed: could rules, search, a form change or a report solve most of it? Record the simplest alternative as the baseline.
3. Classify the AI pattern: classification/scoring, forecasting, extraction, generation/drafting, retrieval Q&A, agent/automation; and the autonomy level (suggest, human-approves, fully automated).
4. Assess value: pain today (time, cost, error, revenue, experience), who benefits, how it would be measured; express as ranges only if the input supports them, otherwise `[UNKNOWN]`.
5. Assess feasibility: task difficulty for current techniques, tolerance for error, latency needs, integration points, team skills.
6. Assess data readiness: availability, volume, labels or ground truth, quality, representativeness, access rights and legal basis for use.
7. Assess risk: impact of a wrong output on people, privacy (KVKK/GDPR), fairness, safety and harmful content, security (prompt injection, data leakage), regulatory classification (e.g. EU AI Act risk category), reputational exposure.
8. Estimate operating considerations qualitatively: inference cost drivers, monitoring and human review effort, vendor dependency.
9. Score value, feasibility, data readiness and risk on 1-5 with one-line evidence each; mark scores based on inference `[ASSUMPTION]`.
10. Recommend go, pilot or no-go; for a pilot define scope, success metric, stop criterion, human oversight and the smallest experiment that reduces the biggest uncertainty.
11. List open questions with owners; suggest `ml-problem-framing` or `rag-design` for a go/pilot, and `privacy-impact-assessment` when personal data is involved.

## Output format
```markdown
# AI Use Case Assessment: <name>
Proposer: <name/unit or [UNKNOWN]> · Pattern: <type> · Autonomy: <suggest / approve / automate>

## Use Case
- Literal ask: ...
- Underlying need: ...
- Non-AI baseline: ...

## Scorecard
| Dimension | Score (1-5) | Evidence | Confidence |
|---|---|---|---|
| Business value | | | |
| Technical feasibility | | | |
| Data readiness | | | |
| Risk (5 = low) | | | |

## Key Risks and Controls
| Risk | Impact | Control | Owner |
|---|---|---|---|

## Recommendation
<Go / Pilot / No-go> – <rationale>
Pilot: scope ..., success metric ..., stop criterion ..., human oversight ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
1. <question> — <owner>
```

## Quality checklist
- [ ] A non-AI baseline is considered and compared.
- [ ] Autonomy level and the impact of a wrong output are explicit.
- [ ] Data readiness covers labels, quality, access rights and legal basis.
- [ ] Every score has evidence; inferred scores are marked.
- [ ] No invented volumes, costs or savings.
- [ ] A pilot recommendation has success and stop criteria.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Solution-first thinking ("we need an LLM"). Start from the decision and the error tolerance, not the technology.
- Ignoring the cost of human review. If every output needs checking, the saving may vanish; estimate review effort.
- Treating a demo as feasibility evidence. A few good examples say nothing about the error rate on real, messy inputs.

## Example
Input: "LLM drafts first replies to all customer complaints for call center agents."

Excerpt of output:
- Autonomy: suggest; agent edits and sends. Wrong output impact: medium (tone, wrong promises), mitigated by human review.
- Data readiness 3: two years of complaints and replies exist; quality of historical replies unknown `[ASSUMPTION]`; contains personal data, must be masked for development.
- Recommendation: Pilot with one complaint category for 4 weeks; success = median handling time down without lower satisfaction score; stop if any draft makes an unauthorized compensation promise that reaches a customer.
