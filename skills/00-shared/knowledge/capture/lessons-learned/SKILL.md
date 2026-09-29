---
name: lessons-learned
description: "Captures lessons learned from a project, release, phase, incident or initiative as evidence-backed observations of what worked and what did not, their causes, and specific actions to keep or change, each with an owner and a place where it will be applied. Use at the end of a project or phase, after a release or major event, when preparing a closure report, or when someone asks to \"write up lessons learned\" from notes, retrospectives or timelines."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: knowledge
  area: capture
  title: "Capture lessons learned"
  related: "retrospective-facilitation, postmortem, project-closure-report, kb-article, action-item-extraction"
  prompt: "Write up lessons learned from our CRM migration project using these retro notes and the timeline."
---

# Capture Lessons Learned

## Purpose
Turn experience into reusable, actionable knowledge so the next team does not repeat the same mistakes and keeps what worked. A lesson counts only when it changes a practice, template, checklist or decision rule somewhere.

## When to use
- A project, phase, release or major initiative has ended or reached a milestone.
- Retrospective notes, a timeline or status reports exist and must be distilled for others.
- A closure report or portfolio review requires a lessons section.

## When not to use
- A single production incident needs a blameless causal analysis. Use `postmortem`.
- The team needs to run the reflection session itself. Use `retrospective-facilitation`.
- The goal is a formal end-of-project document covering scope, budget and handover. Use `project-closure-report`.

## Inputs
Required:
- Source material: retro notes, timeline, status reports, incident notes, or the user's own account.

Optional, improves quality:
- Original goals, success criteria, plan vs. actual (dates, scope, budget).
- Audience of the lessons (same team, other teams, management, portfolio office).
- Where lessons are stored and how they are reused (templates, checklists, knowledge base).

If no source material is given, ask the user for a short account of what happened, one focused question at a time (at most 5).

## Process
1. Establish context in three lines: what the effort was, its goals, and plan vs. actual on the dimensions the input supports. Mark missing figures `[UNKNOWN]`; never estimate them.
2. Extract raw observations from the source and tag each as "went well", "went badly" or "surprise". Keep the user's wording where it carries evidence.
3. Separate facts from interpretation: each observation cites its evidence (event, date, metric, document); anything inferred is marked `[ASSUMPTION]`.
4. Group observations into themes (for example planning, requirements, dependencies, technical, testing, communication, stakeholders, tooling, people). Merge duplicates.
5. For each significant theme, ask "why did this happen?" until you reach a cause the organization can act on (a process, decision rule, template, skill or structure), not a person. Keep the tone blameless.
6. Write each lesson as: context → what happened → cause → lesson (a generalizable rule) → action. A lesson that only restates the event ("testing was late") is not finished.
7. Define actions as keep, start, stop or change, each with an owner, a target (the template, checklist, process or team where it will be applied) and a due date or `[TBD]`.
8. Prioritize: mark the 3-5 lessons with the highest expected impact on future efforts; move minor observations to an appendix.
9. Check audience and privacy: remove personal blame, names in negative context and personal data; mask anything sensitive.
10. Fill the output template and list open questions.
11. If the goal continues, suggest the next skill: `kb-article` to publish a lesson for reuse, `action-item-extraction` to push actions into a tracker, or `project-closure-report` to include them in closure.

## Output format
```markdown
# Lessons Learned: <effort name>
Period: <start – end> · Audience: <who> · Sources: <retro notes, timeline, ...>

## Context
- Goal: ... · Plan vs. actual: <scope/time/budget or [UNKNOWN]>

## Top Lessons
### L1. <lesson as a rule, one sentence>
- Context / what happened: ... (evidence: ...)
- Cause: ... [ASSUMPTION if inferred]
- Action: <Keep/Start/Stop/Change> — <what> — owner: <name/role or TBD> — applied in: <template/process> — due: <date or TBD>

## What Worked (keep)
- ...

## Other Observations
- ...

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every lesson is a generalizable rule, not a restatement of an event.
- [ ] Every lesson has at least one action with owner and a concrete place where it will be applied.
- [ ] Observations cite evidence; inferences are labeled `[ASSUMPTION]`; no invented figures.
- [ ] Both what worked and what did not are captured.
- [ ] The text is blameless and contains no unnecessary personal data.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Lessons recorded, never learned": a document filed and forgotten. Attach each action to a template, checklist or process owner.
- Blaming people ("the vendor was incompetent"). Describe the condition that allowed the outcome, such as missing acceptance gates in the contract.
- Only listing negatives. What worked is equally valuable and easier to repeat.

## Example
Input: "Retro notes: data migration slipped 3 weeks, source data quality worse than expected, business key users joined testing late. Daily cutover calls worked well."

Weak lesson: "Data quality was bad."
Strong lesson: "L1. Profile source data before committing to migration dates." Cause: dates were set before any profiling `[ASSUMPTION: confirm with PM]`. Action: Change — add a data-profiling step and exit criterion to the migration plan template — owner: PMO `[TBD]`.
Keep: daily cutover calls during the final two weeks.
