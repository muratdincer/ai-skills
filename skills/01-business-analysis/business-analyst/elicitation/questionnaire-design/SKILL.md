---
name: questionnaire-design
description: "Designs an unbiased requirements questionnaire for a large or distributed audience: objectives, target population, question types and wording free of leading or double-barreled items, logic/branching, pilot plan, privacy notice and analysis plan. Use when many users or sites must be asked the same things, or when asked to 'create a survey to gather requirements'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Design a questionnaire"
  related: "interview-question-set, screener-survey, feedback-synthesis, research-plan, data-classification"
  prompt: "Design a survey for 400 branch employees to find out which tasks in the current loan application screen take the most time."
---

# Design a Questionnaire

## Purpose
Collect comparable requirements evidence from many people at low cost, with questions that measure what the analysis actually needs and do not bias the answers.

## When to use
- Many users, branches or sites are affected and interviews cannot cover them.
- You need to quantify how widespread a pain, practice or need is.
- You want to validate interview findings at scale.

## When not to use
- You need depth, stories and reasons from a few people. Use `interview-question-set`.
- You are recruiting participants for user research. Use `screener-survey`.

## Inputs
Required:
- The decision or analysis question the survey supports.
- The target population.

Optional, improves quality:
- Interview findings or hypotheses to test, available survey tooling constraints, languages, deadline.

If the decision the survey supports is missing, ask; otherwise questions drift into "nice to know".

## Process
1. Write 2-5 information objectives and, for each, how the answer will be used (decision, threshold, comparison).
2. Define the population and segments you need to compare (role, site, experience); add only the demographic questions that serve these comparisons.
3. Draft questions per objective. Prefer behavior and frequency ("In the last week, how many times...") over opinions and hypotheticals.
4. Choose types deliberately: single/multiple choice with "Other (specify)" and "Not applicable", rating scales with labelled points, ranking (max 5-7 items), few open text fields.
5. Remove bias: no leading or loaded wording, one topic per question, balanced scales, neutral order, avoid jargon, randomize option order where sensible.
6. Order as a funnel (pyramid): easy, general behavior questions first, then specific and sensitive ones, demographics last; add branching so respondents only see relevant questions; keep completion time at about 5-10 minutes.
7. Write the intro: purpose, time needed, anonymity or not, data use and retention (KVKK/GDPR notice); collect no personal data you do not need.
8. Pilot with 3-5 people from the population before sending: check understanding, time and branching, then revise. Do not launch an unpiloted questionnaire.
9. Define the analysis plan: metrics per question, segment cuts, minimum response count for reliable conclusions `[ASSUMPTION until agreed]`. Hypotheses carried over from interviews are labeled as such, not stated as findings.
10. If the goal continues, suggest `feedback-synthesis` to analyze the responses, or `interview-question-set` to follow up on surprising results in depth.

## Output format
```markdown
# Questionnaire: <topic>
Audience: <population> · Target time: <min> · Anonymous: <yes/no>

## Objectives
| # | Information objective | Used for |

## Introduction text
...

## Questions
| # | Objective | Question | Type | Options / scale | Branching |
|---|---|---|---|---|---|

## Pilot plan
- ...

## Analysis plan
- ...
```

## Quality checklist
- [ ] Every question maps to an objective; none is "nice to know".
- [ ] No leading, loaded or double-barreled questions.
- [ ] Scales are balanced and labelled; "Not applicable" exists where needed.
- [ ] Estimated completion time is 10 minutes or less.
- [ ] Privacy notice is present and personal data is minimized.
- [ ] A pilot and an analysis plan are defined.
- [ ] Questions run as a funnel from general to specific, with demographics at the end.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asking users to design the solution ("Which features do you want?"). Ask about tasks, frequency and pain instead.
- Treating a low response rate as representative. Report response rate per segment.
- Changing questions after launch. Pilot first; changes break comparability.

## Example
Input: "400 branch employees; which steps in the loan application screen take the most time."

Excerpt of output:
| # | Objective | Question | Type | Options / scale |
|---|---|---|---|---|
| 3 | Time drivers | In your last 5 loan applications, which step took the longest? | Single choice | Customer search / Income entry / Document upload / Credit check / Other (specify) |
| 4 | Frequency | How often do you re-enter data that already exists in another system? | Scale | Never / Rarely / Sometimes / Often / Every application |
