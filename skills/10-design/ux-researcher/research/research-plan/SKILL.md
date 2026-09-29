---
description: Writes a user research plan with the decision it informs, research objectives and questions, method choice and rationale, participant criteria and sample, logistics, ethics and consent, timeline and deliverables. Use when a team wants to "talk to users", validate a concept, understand a behavior or evaluate a design, and before recruiting participants or booking sessions.
related: screener-survey, usability-test-script, interview-question-set, research-synthesis, hypothesis-statement
prompt: Write a research plan to understand why small business owners abandon our invoicing app during the first week.
---

# Write a Research Plan

## Purpose
Align the team on what decision the research serves, what must be learned, and how, so the study produces evidence that changes a decision instead of interesting but unusable anecdotes.

## When to use
- A product or design decision depends on unknown user needs, behaviors or reactions.
- A concept, prototype or live product needs evaluation with users.
- Stakeholders request research and the scope, method and budget must be agreed.

## When not to use
- The plan exists and only the session script is needed. Use `usability-test-script` or `interview-question-set`.
- Data is already collected and needs analysis. Use `research-synthesis`.

## Inputs
Required:
- The business or product question and the decision that depends on it.

Optional, improves quality:
- Existing knowledge: analytics, support tickets, previous studies, personas.
- Target users and segments, constraints (budget, dates, incentives, access to users), stage of the product.

If the decision behind the research is unclear, ask for it first; without it the plan cannot prioritize. Other gaps become open questions.

## Process
1. State the decision the research informs, who makes it and by when; if no decision depends on it, say so and propose descoping.
2. Summarize what is already known and the evidence behind it, and separate assumptions to test from open unknowns.
3. Write 2-4 research objectives and, under each, specific research questions (what we want to learn, not questions to ask participants).
4. Choose the method by question type: generative (interviews, contextual inquiry, diary study) for needs and behavior; evaluative (moderated or unmoderated usability tests, concept tests) for designs; quantitative (survey, analytics, A/B) for how many. Justify the choice and state its limits.
5. Define participants: segments, inclusion and exclusion criteria, sample size per segment with rationale (e.g. 5-8 per segment for qualitative saturation, larger for surveys), accessibility and diversity coverage.
6. Plan recruitment and logistics: channel, screener, incentives, session length, remote or in person, tools category, note-takers and observers.
7. Address ethics and privacy: informed consent, recording permission, data minimization and masking, storage and retention, KVKK/GDPR basis, handling of vulnerable participants.
8. Define analysis approach and deliverables: synthesis method, format (findings report, highlight clips, updated journey), and how results reach the decision maker.
9. Build the timeline with milestones (plan sign-off, recruiting, fieldwork, synthesis, readout) and mark unconfirmed dates `[TBD]`.
10. List risks (recruiting difficulty, bias, stakeholder expectations) with mitigations.
11. Mark inferences `[ASSUMPTION]`, list open questions, and suggest `screener-survey` for recruiting and `usability-test-script` or `interview-question-set` for sessions.

## Output format
```markdown
# Research Plan: <study name>
Owner: <researcher> · Stakeholders: <names/roles> · Status: <draft/approved>

## Decision and Background
- Decision: <what, who, by when>
- Known: <evidence>
- Assumptions to test: ...

## Objectives and Research Questions
1. Objective: ...
   - RQ1.1 ...

## Method
<method, rationale, limitations>

## Participants
| Segment | Criteria | Exclusions | Sample | Rationale |
|---|---|---|---|---|

## Recruitment and Logistics
<channel, incentive, session format and length, roles>

## Ethics and Privacy
<consent, recording, masking, retention, legal basis>

## Analysis and Deliverables
<synthesis approach, outputs, readout audience>

## Timeline
| Milestone | Date | Owner |
|---|---|---|

## Risks and Open Questions
- ...
```

## Quality checklist
- [ ] The plan names the decision it informs and its deadline.
- [ ] Research questions are learning goals, not interview questions or leading statements.
- [ ] The method matches the question type and its limits are stated.
- [ ] Participant criteria are behavioral and sample sizes are justified.
- [ ] Consent, recording and personal data handling are covered.
- [ ] Unconfirmed dates, budgets and numbers are marked, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using qualitative interviews to answer "how many" questions. Pair them with a survey or analytics.
- Recruiting by demographics only. Screen for the behavior that matters (e.g. "sent at least 3 invoices last month").
- Planning research after the decision is already made. Tie the timeline to the decision date.

## Example
Input: "Why do small business owners abandon our invoicing app in the first week?"

Excerpt of output:
- Decision: Which two onboarding problems to fix next quarter; product lead, before planning `[TBD: date]`.
- RQ1.1: What were users trying to accomplish in their first session, and what stopped them?
- Method: 10 remote interviews with recent churners plus funnel analysis of first-week events; interviews explain why, funnel shows where and how many.
- Criteria: signed up in the last 30 days, created at most one invoice, owns a business with fewer than 10 employees.
