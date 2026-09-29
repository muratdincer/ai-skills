---
name: interview-question-set
description: "Prepares a requirements interview guide tailored to a stakeholder type (executive, process owner, end user, IT/system owner, compliance), with opening, context, open, probing and validation questions, timing and follow-up prompts. Use before an elicitation interview or when asked 'what should I ask the users/managers in the interview?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Prepare interview questions"
  related: "interview-notes-analysis, request-clarification-questions, workshop-plan, stakeholder-identification, problem-interview-script"
  prompt: "Prepare a 45-minute interview for warehouse shift supervisors about how they handle stock discrepancies today."
---

# Prepare Interview Questions

## Purpose
Give the analyst a focused, timed interview guide that surfaces real needs, pains, rules and exceptions from a specific stakeholder type, instead of a wish list.

## When to use
- Before one-to-one or small-group elicitation interviews.
- Different stakeholder types need different angles on the same initiative.
- A previous interview produced vague or solution-only answers.

## When not to use
- You only need a few questions to clarify a single request. Use `request-clarification-questions`.
- You want to validate a product problem with external customers. Use `problem-interview-script`.
- Many participants must converge together. Use `workshop-plan`.

## Inputs
Required:
- The initiative or topic.
- The interviewee type or role.

Optional, improves quality:
- Duration, format (on-site, remote), what is already known, previous interview findings.
- Specific hypotheses or conflicts to test.

If the interviewee type is missing, ask; the questions depend on it.

## Process
1. Set 2-4 interview objectives: what you must know when you leave the room.
2. Adapt the angle to the stakeholder type: executives (goals, success, constraints, priorities), process owners (flow, rules, exceptions, KPIs), end users (tasks, pains, workarounds, tools), IT/system owners (interfaces, data, constraints, technical debt), compliance (obligations, controls, evidence).
3. Write an opening (purpose, confidentiality, recording consent, time) and a warm-up about their role.
4. Write open "tell me about" and "walk me through the last time" questions tied to real episodes.
5. For each open question add 2-3 probes: frequency, volume, exceptions, what happens when it goes wrong, who else is involved, how they know it worked.
6. Add validation questions that confirm current hypotheses without leading ("Some people told us X; how does that match your experience?").
7. Add a closing: priorities ("if only one thing changed..."), who else to talk to, documents or samples to share, follow-up consent.
8. Order each section as a funnel (pyramid): broad open context first, then narrower episode questions and probes, then closed confirmation questions last, so early answers are not anchored by your framing.
9. Timebox sections to fit the duration, mark must-ask questions, and remove any question that suggests a solution. Label hypotheses you bring in as `[ASSUMPTION]` in the interviewer notes, never in the question wording.
10. If the goal continues, suggest `interview-notes-analysis` for the notes afterwards, or `workshop-plan` when conflicting views need a joint session.

## Output format
```markdown
# Interview Guide: <initiative> – <stakeholder type>
Duration: <min> · Objectives: 1) ... 2) ...

## Opening (<min>)
- Purpose, confidentiality, recording consent

## Context (<min>)
1. ...

## Core topics (<min>)
| # | Question | Probes | Must-ask |
|---|---|---|---|

## Validation (<min>)
- ...

## Closing (<min>)
- Top priority · Who else · Documents/samples · Follow-up

## Artifacts to request
- ...
```

## Quality checklist
- [ ] Questions are open and anchored on real, recent episodes.
- [ ] No question proposes or presumes a solution.
- [ ] Each objective is covered by at least one must-ask question.
- [ ] The timeboxes add up to the duration with buffer.
- [ ] Recording consent and personal data handling are addressed in the opening.
- [ ] The angle clearly matches the stakeholder type.
- [ ] Each section runs as a funnel from broad open questions to narrow closed ones.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asking hypotheticals ("Would you use...?"). Ask what they did last time and why.
- Too many questions for the time. 8-12 core questions for 45 minutes is typical; probes matter more.
- Only interviewing managers. The people who do the work hold the exceptions and workarounds.

## Example
Input: "45-minute interview, warehouse shift supervisors, stock discrepancies."

Excerpt of output:
| # | Question | Probes | Must-ask |
|---|---|---|---|
| 1 | Walk me through the last stock discrepancy you handled. | How was it detected? Who did you involve? How long until resolved? | Yes |
| 2 | Which discrepancies do you not record, and why? | How often? What happens at month end? | Yes |
