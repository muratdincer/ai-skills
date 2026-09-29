---
name: candidate-debrief
description: "Consolidates interview scorecards into a structured debrief summary with a competency coverage matrix, conflicting signals, resolved and unresolved questions, and a documented hire decision with level. Use when preparing or running a candidate debrief, when interviewers disagree, or when a hiring decision must be recorded with its evidence and rationale."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "Summarize a candidate debrief"
  related: "interview-scorecard, interview-plan, decision-log, onboarding-plan-30-60-90, bias-check"
  prompt: "Summarize the debrief for candidate B from these four scorecards and give me a decision draft for the senior level."
---

# Summarize a Candidate Debrief

## Purpose
Turn independent scorecards into one evidence-based decision: which competencies are covered, where signals conflict, what was resolved in discussion, and why the final hire/no-hire and level were chosen.

## When to use
- All scorecards for a candidate are submitted and the debrief is about to happen or just happened.
- Interviewers disagree strongly or scored the same competency differently.
- The decision and level need a written rationale for the hiring committee, the candidate feedback or later audit.

## When not to use
- Individual scorecards are still missing evidence. Use `interview-scorecard` first.
- The loop itself needs redesign after repeated weak signals. Use `interview-plan`.

## Inputs
Required:
- All submitted scorecards for the candidate (scores, evidence, recommendations) and the target level.

Optional, improves quality:
- Loop design (which stage owns which competency), level definitions, debrief discussion notes.
- Hiring bar policy (e.g. any strong no blocks, who decides).

If scorecards are missing for any stage, list the gap and do not infer that stage's outcome.

## Process
1. Confirm every scorecard was submitted before discussion; flag any written or changed after the debrief started.
2. Build a coverage matrix: competency × stage with score and one-line evidence; mark competencies with no or weak signal.
3. Identify conflicts (same competency, different scores) and state the evidence behind each side, not the interviewer's seniority.
4. Separate evidence from impressions: remove or flag statements without behavior, and non-job-related remarks; label any conclusion you draw beyond the scorecards `[ASSUMPTION]` and move it to open questions.
5. Record what the discussion resolved (new evidence, clarified rubric reading) and what stays unresolved.
6. Assess against the level bar, not against other candidates in the pipeline; if the evidence fits a different level, state which and why.
7. Apply the organization's decision rule (e.g. hiring manager decides, strong no requires rebuttal evidence); state which rule was used.
8. Run a bias pass: halo from one strong stage, affinity/similarity, pedigree, "culture fit" without defined values, groupthink after the first speaker.
9. Draft the decision, level, conditions or risks for onboarding, and a factual, respectful feedback outline for the candidate.
10. Minimize candidate personal data and note retention per policy (KVKK/GDPR).
11. If the user's goal continues, suggest `onboarding-plan-30-60-90` for a hire, `decision-log` to record the decision, or `interview-plan` if the loop showed gaps.

## Output format
```markdown
# Debrief: <candidate ID> – <role> – <target level> – <date>
Decision rule: <rule> · Decider: <role>

## Coverage Matrix
| Competency | Stage / interviewer | Score | Key evidence |
|---|---|---|---|

## Conflicting Signals
- <competency>: <side A evidence> vs <side B evidence> → <resolved / unresolved>

## Signal Gaps
- ...

## Decision
Hire / No hire – Level: <level> – Rationale: <3-5 sentences tied to evidence>
Risks / onboarding focus: ...

## Candidate Feedback Outline
- ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Every competency in the loop appears in the matrix with evidence or a flagged gap.
- [ ] Conflicts are resolved by evidence, not by seniority or majority vote alone.
- [ ] Decision is assessed against the level bar, not against other candidates.
- [ ] No non-job-related remarks or undefined "fit" arguments remain.
- [ ] The decision rule and decider are stated.
- [ ] Candidate feedback is factual and contains no internal scoring details or personal remarks.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Letting the first or most senior speaker anchor everyone. Read scorecards silently first, then discuss.
- Averaging scores. A missing must-have competency is not offset by excellence elsewhere unless the level definition says so.
- Down-levelling to hire "safely" without evidence for the lower level's bar. State the evidence for the chosen level.

## Example
Input: 4 scorecards, target Senior. Design Strong yes, coding Yes, collaboration Yes, operability No ("did not mention monitoring").

Excerpt of output:
- Conflict: Operability No (system design, hint needed) vs Yes (coding stage, added structured logging unprompted) → resolved as Yes-with-gap after comparing evidence.
- Weak rationale (avoid): "Everyone liked her, strong hire."
- Strong rationale: "Meets Senior bar on design and trade-offs (outbox choice with failure analysis); operability evidence mixed; onboarding focus: on-call shadowing in first 30 days."
