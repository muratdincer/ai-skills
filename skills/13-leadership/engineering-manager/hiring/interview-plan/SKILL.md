---
name: interview-plan
description: "Designs a structured interview loop for a role, mapping each competency to exactly the stages that assess it, with stage formats, durations, interviewer profiles, rubrics, candidate communication and decision rules that reduce bias. Use when opening a role, when an existing loop is slow, inconsistent or has low offer acceptance, or when interviewers assess overlapping things and miss others."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "Design an interview loop"
  related: "job-description, technical-interview-questions, interview-scorecard, candidate-debrief, career-ladder"
  prompt: "Design an interview loop for a mid-level frontend engineer. We can afford at most four hours of candidate time."
---

# Design an Interview Loop

## Purpose
Assess the competencies that predict success in the role consistently for every candidate, with minimal candidate time and interviewer overlap, and a clear decision rule.

## When to use
- A new role is opened or a role's level changes.
- The current loop produces inconsistent decisions, long cycle times or poor candidate feedback.
- Hiring volume grows and new interviewers need a standard structure.

## When not to use
- Writing the actual questions and rubrics for a technical stage. Use `technical-interview-questions`.
- Recording evidence after an interview. Use `interview-scorecard`.
- The posting text. Use `job-description`.

## Inputs
Required:
- Role, level and the 4-7 competencies that matter (or the job description to derive them from).

Optional, improves quality:
- Candidate time budget, remote or on-site, available interviewers and their training status.
- Current loop and its problems; legal or HR requirements; accessibility needs process.

If competencies are missing, derive a proposal from the job description and mark it `[ASSUMPTION]` for confirmation.

## Process
1. Confirm competencies and define what "meets bar" looks like for each at this level, in observable terms.
2. Build a competency × stage matrix; every competency is assessed in at least one stage, the critical ones in two, and no stage assesses more than three.
3. Choose formats that resemble the real work: pairing or practical exercise, system design discussion, code review exercise, structured behavioral interview. Avoid trivia and puzzles unrelated to the job.
4. Decide on take-home versus live exercise; cap unpaid take-home effort (e.g. 2-3 hours) and offer an alternative for candidates with constraints.
5. Keep total candidate time within budget; sequence stages so early stages screen for must-haves.
6. Assign interviewer profiles per stage (level, trained, diverse panel where possible); avoid the hiring manager being the only decision voice.
7. Standardize: same core questions per stage, rubric anchors per level, independent written scorecards before any discussion.
8. Define decision rules: what combination of scores leads to hire / no hire, who decides, how disagreements are resolved.
9. Plan candidate experience: what they are told in advance, accommodations offered, feedback timeline.
10. Define loop health metrics: time to decision, pass-through rate per stage, offer acceptance, interviewer calibration drift.
11. If the user's goal continues, suggest `technical-interview-questions` for stage questions, `interview-scorecard` for the scoring form, or `candidate-debrief` for the decision meeting.

## Output format
```markdown
# Interview Loop: <role, level>
Candidate time: <total> · Decision owner: <role>

## Competencies and Bar
| Competency | Meets bar at this level looks like |
|---|---|

## Stages
| # | Stage | Format | Duration | Competencies assessed | Interviewer profile |
|---|---|---|---|---|---|

## Coverage Matrix
| Competency | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
|---|---|---|---|---|

## Standardization and Bias Controls
- ...

## Decision Rule
- ...

## Candidate Communication
- ...

## Loop Health Metrics
- ...
```

## Quality checklist
- [ ] Every competency is covered; critical ones twice; no stage covers more than three.
- [ ] Formats resemble real work; no brainteasers.
- [ ] Total candidate time is within budget; take-home effort is capped.
- [ ] Scorecards are written independently before any debrief.
- [ ] Decision rule and owner are explicit.
- [ ] Accommodation and candidate communication are planned.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Culture fit" as a stage. It invites similarity bias; assess specific values-based behaviors instead.
- Five interviewers all asking about the same project. Use the coverage matrix to assign distinct focus areas.
- Adding stages when unsure. More stages rarely improve prediction but always slow hiring.

## Example
Input: "Mid-level frontend engineer, max four hours candidate time."

Excerpt of output:
| 1 | Recruiter screen | Call | 30 min | Motivation, logistics | Recruiter |
| 2 | Practical pairing | Build a small component in the candidate's preferred framework | 75 min | Frontend craft, testing | Two trained mid/senior engineers |
| 3 | Design & code review | Review a PR, discuss state and performance trade-offs | 60 min | Technical judgment, collaboration | Senior engineer |
| 4 | Behavioral | Structured questions | 45 min | Ownership, communication | Hiring manager + cross-functional partner |
