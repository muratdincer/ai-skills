---
name: screener-survey
description: "Writes a participant screener that recruits the right users for a study, with behavioral inclusion and exclusion criteria, non-leading questions that hide the qualifying answer, quotas per segment, disqualification logic and consent. Use before recruiting for interviews, usability tests or diary studies, or when someone asks \"who should we talk to\" or \"write a recruitment survey\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 10-design
  role: ux-researcher
  area: research
  title: "Write a participant screener"
  related: "research-plan, usability-test-script, questionnaire-design, persona, interview-question-set"
  prompt: "Write a screener to recruit 8 small business owners who send invoices at least monthly and tried a competitor app in the last year."
---

# Write a Participant Screener

## Purpose
Recruit participants whose behavior matches the research questions, while filtering out professional testers, insiders and people who guess the "right" answers, so session time is spent with the users who matter.

## When to use
- A research plan defines target segments and recruiting is about to start.
- A recruiting agency or panel needs screening criteria and questions.
- Previous sessions included wrong-fit participants and screening must be tightened.

## When not to use
- The goal is to measure attitudes or behaviors at scale, not to recruit. Use `questionnaire-design`.
- Segments and study goals are undefined. Use `research-plan`.

## Inputs
Required:
- The study goal and the target participant profile (who, what behavior, what context).

Optional, improves quality:
- Research plan, sample size and segment quotas, recruiting channel (customer list, panel, agency, intercept), incentive, session format and dates, markets and languages.

If the target profile is missing, ask for it in one short numbered batch (who, key behavior, must-exclude groups). Other gaps become open questions.

## Process
1. Translate the target profile into behavioral criteria (frequency, recency, tools used, role in the decision) rather than demographics or self-labels; add demographics only for diversity quotas.
2. Define exclusions: employees and relatives of the company and competitors, market research or UX professionals, recent study participants (e.g. last 6 months), people outside the legal or market scope.
3. Set quotas per segment and the mix needed (e.g. new vs. experienced, device, accessibility needs); state total recruits including 20-25% over-recruit for no-shows `[ASSUMPTION]` if not given.
4. Order questions from broad to specific: exclusion questions first, then qualifying behaviors, then quotas, then logistics; put the cheapest disqualifiers first.
5. Write questions that do not reveal the target: multiple choice with distractor options, frequency ranges that do not hint at the cut-off, "none of the above" on every list.
6. Mark each answer with the rule it triggers (Qualify, Terminate, Quota: segment X, Flag for review) and define the scoring logic.
7. Add one open-ended articulation question to check that the respondent can express thoughts, with explicit review criteria.
8. Add logistics and consent: availability, device and connectivity for remote sessions, recording consent, data use and retention; collect only the personal data needed to schedule, and keep screener data separate from session notes.
9. Estimate length (aim for under 5 minutes, 8-12 questions) and pilot it with 2-3 people to catch leading wording and broken logic.
10. List assumptions and open questions, and suggest `usability-test-script` or `interview-question-set` for the sessions.

## Output format
```markdown
# Screener: <study>
Target: <n participants> · Segments/quotas: <...> · Channel: <...> · Incentive: <[TBD]>

## Criteria
- Include: ...
- Exclude: ...
- Quotas: | Segment | Target | Min | Max |

## Questions
**Q1. <question>** (single choice)
- a) ... → Terminate
- b) ... → Continue
- c) None of the above → Terminate

**Q2. <question>** (multiple choice)
- ... → Qualify if <rule>

**Q9. <articulation question>** (open) → Review: <criteria>

## Logistics and Consent
<availability, device, recording consent, data retention>

## Scoring Logic
<which combinations qualify; quota assignment>

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Criteria are behavioral and each maps to the research questions.
- [ ] No question reveals the qualifying answer; every list has a neutral exit option.
- [ ] Every answer option has an explicit rule (Qualify, Terminate, Quota, Flag).
- [ ] Standard exclusions (insiders, UX/market research professionals, recent participants) are included.
- [ ] Personal data collected is limited to what scheduling and consent require.
- [ ] Length is under about 5 minutes and a pilot step is planned.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Yes/no qualifiers ("Do you use invoicing software?"). Respondents answer yes; use options and frequency ranges.
- Screening on self-identity ("Are you a power user?"). Ask for concrete recent behavior instead.
- Forgetting quotas, so all recruits come from the easiest segment. Track quotas during recruiting.

## Example
Input: "8 small business owners who invoice at least monthly and tried a competitor in the last year."

Weak: "Do you send invoices every month? Yes / No"
Strong: "In the past 3 months, about how many invoices did your business send? a) None → Terminate b) 1-2 → Terminate c) 3-10 → Continue d) More than 10 → Continue"
- Q4: "Which of these tools have you used for invoicing in the last 12 months?" (list with our product, 3 competitors, spreadsheet, other, none) → Qualify if any competitor selected.
