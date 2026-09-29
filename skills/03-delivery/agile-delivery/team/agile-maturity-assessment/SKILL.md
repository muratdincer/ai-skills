---
description: "Assesses a team's or unit's agile maturity in a methodology-neutral way: scores practice areas (customer value and product ownership, planning and forecasting, flow and delivery, technical practices, quality, continuous improvement, team autonomy, stakeholder collaboration) on a 1-5 evidence-based scale, identifies constraints rather than averaging, and proposes the next 2-3 improvements with observable outcomes. Use when a leader or coach asks how agile a team really is, needs a baseline before a transformation, or wants to decide what to improve next."
related: "team-health-check, retrospective-facilitation, wip-policy, engineering-metrics-review, current-state-assessment"
prompt: "Assess our team's agile maturity. We do two-week iterations, releases are quarterly, the product owner is part-time, and there is no test automation."
---

# Assess Agile Maturity

## Purpose
Give an evidence-based picture of how well a team's ways of working deliver value frequently, safely and adaptively, and point to the few improvements that will unlock the most, rather than a ceremony checklist or a vanity score.

## When to use
- A baseline is needed before or during an agile transformation.
- A leader or coach asks "where are we and what next?" for a team or group of teams.
- Periodic reassessment to see whether improvements took hold.

## When not to use
- Measuring team morale and perceived health. Use `team-health-check`.
- Analyzing delivery metrics in depth. Use `engineering-metrics-review`.
- Assessing a client's whole IT organization in a consulting context. Use `current-state-assessment`.

## Inputs
Required:
- A description of how the team works today (planning, delivery and release cadence, roles, quality practices, feedback loops), or answers to an assessment questionnaire.

Optional, improves quality:
- Metrics: deployment frequency, lead time for changes, change failure rate, recovery time (DORA), cycle time, escaped defects.
- Artifacts: backlog, board snapshot, definition of done, retrospective actions.
- Goals of the assessment and any maturity model the organization already uses.

If the description is thin, ask up to 5 targeted questions (release frequency, who decides priorities, how quality is assured, how often users give feedback, what changed after the last retrospective). Score unanswered areas `[INSUFFICIENT EVIDENCE]`, never guess.

## Process
1. Confirm scope (one team, several teams, a department) and purpose (baseline, improvement planning, reassessment). State that the result is not a performance rating.
2. Use practice areas independent of any framework: customer value and product ownership; planning and forecasting; flow and delivery; technical practices (integration, automation, deployment); quality built in; continuous improvement; team autonomy and roles; stakeholder collaboration and feedback.
3. Define a 1-5 scale with observable anchors per area (1 = ad hoc, 3 = consistent within the team, 5 = continuously optimized and measured). Write the anchors before scoring.
4. Score each area only from evidence in the input; cite it. Mark statements that are claims without evidence as `[CLAIMED]` and areas without information as `[INSUFFICIENT EVIDENCE]`.
5. Cross-check with outcomes: if DORA or flow metrics are available, compare them with the practice scores; a high practice score with poor outcomes means the practice is ritual, not effective.
6. Identify the constraint: the lowest area that limits the others (e.g. quarterly releases cap feedback loops regardless of iteration planning). Do not average areas into one headline score.
7. Propose the next 2-3 improvements targeting the constraint, each with an observable outcome, a first experiment and a check interval (e.g. "deploy to production at least every 2 weeks within 3 months").
8. List what not to do yet (improvements that depend on the constraint being solved first).
9. Define how to reassess: same areas and anchors, evidence to collect, date. Suggest `team-health-check` for the human side, `wip-policy` or `retrospective-facilitation` to start the chosen improvements.

## Output format
```markdown
# Agile Maturity Assessment – <team/unit>, <date>
Purpose: <...> · Evidence used: <description, metrics, artifacts>

| Practice area | Score (1-5) | Evidence | Gap to next level |
|---|---|---|---|

Outcome metrics (if available): <deployment frequency, lead time, change failure rate, recovery time, cycle time>

## Main Constraint
<area> – <why it limits the others>

## Next Improvements (2-3)
| Improvement | Observable outcome | First experiment | Check after |
|---|---|---|---|

## Not Yet
- ...

## Evidence Gaps and Open Questions
- ...

## Reassessment
<date, same anchors>
```

## Quality checklist
- [ ] Every score cites evidence, or is marked `[CLAIMED]` / `[INSUFFICIENT EVIDENCE]`.
- [ ] The scale anchors are observable and written before scoring.
- [ ] No specific framework is assumed as the target state.
- [ ] Practices are cross-checked with outcomes where metrics exist.
- [ ] A single constraint is named instead of an averaged overall score.
- [ ] Improvements have observable outcomes and a check interval.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Scoring ceremonies instead of outcomes ("they hold retrospectives" is not maturity if nothing changes).
- Recommending a full framework rollout. Target the constraint with a small experiment instead.
- Comparing teams by score. Context differs; use scores to guide each team's own next step.

## Example
Input: two-week iterations, quarterly releases, part-time product owner, no test automation.

Excerpt of output:
| Practice area | Score | Evidence |
|---|---|---|
| Planning and forecasting | 3 | Iterations planned consistently [CLAIMED] |
| Flow and delivery | 1 | Releases quarterly |
| Technical practices | 1 | No test automation |
- Main constraint: release and test automation – feedback from users arrives every 3 months regardless of iteration cadence.
- Improvement: automate regression for the top 5 user journeys and release to a pilot group every 2 weeks; check after 3 months.
