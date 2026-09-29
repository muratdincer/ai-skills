---
name: interview-scorecard
description: "Turns an interviewer's raw notes into a scorecard with verbatim evidence per competency, a rubric-based score, and an independent hire recommendation with rationale. Use right after an interview, when notes must be written up before the debrief, or when checking a scorecard for missing evidence, bias or impressions presented as facts."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "Write an interview scorecard"
  related: "technical-interview-questions, candidate-debrief, interview-plan, bias-check"
  prompt: "Here are my notes from the system design interview with candidate B. Turn them into a scorecard against our senior rubric."
---

# Write an Interview Scorecard

## Purpose
Record what the candidate actually said and did, mapped to the competencies this stage owns, so the hiring decision rests on comparable evidence rather than the interviewer's overall impression.

## When to use
- An interview just finished and notes must become a scorecard before the debrief.
- A submitted scorecard contains only adjectives ("smart", "not senior enough") and needs evidence.
- A hiring manager wants to check scorecards for consistency with the rubric.

## When not to use
- Questions and rubric for the stage do not exist yet. Use `technical-interview-questions`.
- Combining several scorecards into a decision. Use `candidate-debrief`.
- Designing which stages assess which competencies. Use `interview-plan`.

## Inputs
Required:
- The interviewer's notes (as close to verbatim as available) and the competencies assigned to this stage.

Optional, improves quality:
- The stage rubric with level anchors, the target level, the question asked and hints given.
- The organization's recommendation scale (e.g. strong no to strong yes).

If the assigned competencies are missing, ask for them. If there is no rubric, use a four-point scale with generic anchors and mark it `[ASSUMPTION]`.

## Process
1. Write the scorecard independently: do not read other interviewers' feedback or the debrief channel first (anchoring).
2. Extract observations from the notes as behaviors and quotes with approximate time, separating what the candidate did from the interviewer's interpretation.
3. Map each observation to one assigned competency; park observations about competencies owned by other stages in a short "other signals" line.
4. Score each competency against the rubric anchor it matches best, citing the evidence; if evidence is insufficient, record "not enough signal" instead of guessing.
5. Note hints given and how they changed the outcome, per the stage's hint policy.
6. Remove or flag non-job-related content: appearance, accent, age, family, nationality, pedigree, "culture fit" without a defined value, and comments on nervousness.
7. Write the overall recommendation on the organization's scale with a 2-4 sentence rationale that names the strongest supporting and strongest counter evidence.
8. List what the next interviewers or the debrief should probe, framed as open questions.
9. Minimize personal data: keep only what the decision needs, and remind the user of the retention rules for candidate data (KVKK/GDPR).
10. If the user's goal continues, suggest `candidate-debrief` once all scorecards are in, or `bias-check` for a second review of the wording.

## Output format
```markdown
# Scorecard: <candidate ID> – <stage> – <interviewer> – <date>
Target level: <level> · Question: <title> · Hints given: <list or none>

## Evidence by Competency
| Competency | Evidence (behavior / quote, time) | Rubric anchor | Score |
|---|---|---|---|

## Other Signals (not scored here)
- ...

## Recommendation
<Strong no / No / Yes / Strong yes> – <rationale with strongest for and against>

## Probe Next
- ...

## Notes on Data Handling
- Personal data minimized; retention per policy [TBD].
```

## Quality checklist
- [ ] Every score cites at least one concrete behavior or quote.
- [ ] Only competencies assigned to this stage are scored; gaps say "not enough signal".
- [ ] No references to appearance, accent, age, family, origin, pedigree or undefined "fit".
- [ ] Interpretations are labeled as such and separated from observations.
- [ ] Recommendation rationale names counter-evidence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Deciding first, then selecting evidence. Fill the evidence column before choosing a score or recommendation.
- Penalizing a different but valid approach. Score against the rubric, not against the interviewer's own solution.
- Treating "not enough signal" as a no. Flag it for the debrief instead.

## Example
Input notes: "Seemed nervous. Asked about scale first. Picked outbox pattern, explained why vs dual write. Didn't cover monitoring until prompted."

Excerpt of output:
- Weak entry (avoid): "Nervous, decent design, probably mid-level."
- Strong entry: Trade-offs – "Compared outbox with dual write and chose outbox because a crash between writes loses events" (min 22) – anchor Yes.
- Operability – mentioned alerting only after hint at min 45 – anchor No (hint reduces score per policy).
- Removed: "seemed nervous" (not job-related).
