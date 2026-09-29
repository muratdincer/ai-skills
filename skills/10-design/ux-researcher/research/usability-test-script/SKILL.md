---
description: Writes a moderated or unmoderated usability test script with intro and consent, warm-up, realistic task scenarios, neutral probes, observable success criteria, post-task and post-test measures and a debrief. Use when a prototype or live product must be tested with users, when someone asks for "test tasks" or a "moderator guide", or before a usability session is scheduled.
related: research-plan, screener-survey, research-synthesis, heuristic-evaluation, interview-question-set
prompt: Write a usability test script for our new checkout prototype; we want to see if first-time buyers can apply a discount code and pay by card.
---

# Write a Usability Test Script

## Purpose
Give the moderator (or unmoderated tool) a script that tests the riskiest parts of a design with realistic, non-leading tasks and observable success criteria, so results are comparable across participants and point to concrete design changes.

## When to use
- A prototype, beta or live flow needs evaluation with representative users.
- A research plan exists and the session guide must be written.
- A redesign must be benchmarked against the current version with the same tasks.

## When not to use
- The objectives, method and participants are not agreed yet. Use `research-plan`.
- The goal is to explore needs and behaviors, not to evaluate a design. Use `interview-question-set`.
- No users are available and an expert review is enough. Use `heuristic-evaluation`.

## Inputs
Required:
- What is being tested (flow, prototype or product area) and the research questions or risks it must answer.

Optional, improves quality:
- Research plan, target segment, prototype fidelity and its dead ends, session length, moderated or unmoderated format, benchmark metrics to reuse.

If the tested flow or its research questions are missing, ask for them in one short numbered batch. Other gaps become open questions in the script.

## Process
1. Restate the research questions and map each to at least one task; drop tasks that answer no question.
2. Pick 4-7 tasks for a 45-60 minute moderated session (fewer for unmoderated), ordered from low to high complexity, with the riskiest flows covered early enough not to be cut.
3. Write each task as a scenario with a goal and context, never with interface labels or steps ("You want to pay less using the code from your email", not "Click Apply coupon").
4. Define success per task observably: end state reached, critical errors, assists allowed, time limit; set "success / success with difficulty / fail" rules before the sessions.
5. Add neutral probes (what are you expecting here, what would you do next) and forbidden prompts; plan how to handle prototype dead ends and requests for help.
6. Choose measures: task completion, time on task, errors, a post-task single-ease question and a post-test standardized questionnaire (e.g. SUS) if benchmarking; keep the same wording across rounds.
7. Write the intro: purpose, "we are testing the design, not you", think-aloud instructions, recording and consent with data minimization; never capture more personal data than needed.
8. Add warm-up questions that confirm the screener profile and context, then the debrief: overall impressions, most difficult moment, expectations not met.
9. Build the timing plan and observer note grid (task, observation, quote, severity).
10. Mark every inference as `[ASSUMPTION]`, list open questions (prototype limits, test data, accounts), and suggest `screener-survey` for recruiting and `research-synthesis` after the sessions.

## Output format
```markdown
# Usability Test Script: <product / flow>
Format: <moderated remote / in person / unmoderated> · Length: <min> · Prototype: <fidelity, link TBD>

## Research Questions
- RQ1 ... → Tasks: T1, T3

## Introduction (≈5 min)
<purpose, not testing you, think aloud, recording and consent>

## Warm-up (≈5 min)
1. ...

## Tasks
### T1 <short name> (≈<min>)
- Scenario: "<goal and context, no UI labels>"
- Starting point / test data: ...
- Success: <end state> · Critical errors: ... · Time limit: ...
- Probes: ...
- Post-task: "Overall, how easy or difficult was this task?" (1-7)

## Post-test (≈5 min)
<questionnaire, closing questions>

## Debrief and Thanks
<incentive, next steps>

## Observer Grid
| Task | Outcome | Observation | Quote | Severity |
|---|---|---|---|---|

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Every task maps to a research question and every research question has a task.
- [ ] No task uses interface labels, step hints or leading wording.
- [ ] Success and failure rules are defined per task before the sessions.
- [ ] Timing adds up to the session length with buffer.
- [ ] Consent, recording and personal data handling are covered.
- [ ] Prototype limits and required test data are listed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Telling participants where to click in the task text. Describe the goal; let them find the path.
- Helping too early. Agree on an assist policy and count assisted completions separately.
- Changing task wording between rounds and then comparing metrics. Freeze the wording for benchmarks.

## Example
Input: "Test if first-time buyers can apply a discount code and pay by card."

Weak task: "Click 'Apply coupon' and enter SAVE10."
Strong task: "You got a 10% code in a welcome email. Buy the blue backpack for the lowest price you can and pay with the test card below."
- Success: order confirmation shown with discount applied, no assist. Critical error: paying full price without noticing.
- Probe: "What did you expect to happen when you pressed that?"
