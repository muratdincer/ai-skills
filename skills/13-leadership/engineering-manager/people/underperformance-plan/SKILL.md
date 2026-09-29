---
name: underperformance-plan
description: "Drafts a fair, evidence-based performance improvement plan (PIP) with specific expectation gaps, measurable success criteria, the support provided, milestone reviews and clearly stated consequences, ready for HR review. Use when informal feedback has not resolved a sustained performance gap, or when a manager needs to check whether a situation is ready for a formal plan."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Write a performance improvement plan"
  related: "performance-review, feedback-sbi, one-on-one-notes, bad-news-delivery, goal-setting"
  prompt: "Draft a 60-day improvement plan for a developer whose PRs repeatedly fail review and who missed three sprint commitments despite feedback since April."
---

# Write a Performance Improvement Plan

## Purpose
Give the person a genuine, clearly structured chance to succeed: what is expected, how it will be measured, what help they get and what happens at the end, all grounded in documented evidence.

## When to use
- A gap against role expectations has persisted after documented informal feedback.
- HR or policy requires a written plan before further steps.
- A manager wants to test whether evidence and prior feedback are sufficient to start a formal plan.

## When not to use
- The issue has not been raised informally yet. Start with `feedback-sbi` and `one-on-one-notes`.
- The problem is misconduct or a policy breach; that follows the HR/disciplinary process, not a PIP.
- Regular review writing. Use `performance-review`.

## Inputs
Required:
- The role and level expectations, dated examples of the gap, and records of prior feedback given.

Optional, improves quality:
- The organization's PIP template, legal/HR constraints, standard duration.
- Context that may explain the gap: workload, unclear requirements, tooling, team changes, health or personal circumstances disclosed to HR.

If there is no record of prior feedback, state that a formal plan is premature and recommend documented feedback first. This skill does not replace HR or legal advice; recommend HR review before sharing.

## Process
1. Readiness check: expectations were clear, feedback was given and documented, reasonable time passed, and systemic causes (unclear scope, overload, missing onboarding, tooling) were ruled out or addressed.
2. Check whether accommodation or support needs might be involved; if so, route through HR before proceeding and do not speculate about causes.
3. Define 2-4 specific gap areas. For each: the expectation, dated examples of current behavior, impact.
4. Write measurable success criteria for each area that an average performer at this level would meet, not a higher bar.
5. List the support: mentor or pair, clarified priorities, training, reduced context switching, weekly check-ins.
6. Set duration (commonly 30-90 days per local policy) and milestone reviews with dates.
7. State consequences neutrally and per policy for both success and not meeting criteria.
8. Language pass: behavioral, non-judgmental, no personality labels, no references to protected characteristics, leave or personal life.
9. Consistency pass: are expectations and treatment the same as for others at the same level who had similar gaps?
10. Add a review log section for weekly evidence and mark every unknown `[TBD]` or `[UNKNOWN]`.
11. If the user's goal continues, suggest `bad-news-delivery` to prepare the conversation, or `one-on-one-notes` to log weekly check-ins.

## Output format
```markdown
# Performance Improvement Plan: <name> [draft – HR review required]
Role / level: <role> · Manager: <name> · Start: <date> · End: <date> · Duration: <days>

## Background
- Prior feedback: <dates, channel, summary>

## Expectation Gaps and Success Criteria
| Area | Expectation | Current (dated examples) | Success criteria by end | Measure |
|---|---|---|---|---|

## Support Provided
- ...

## Milestone Reviews
| Date | Focus | Outcome |
|---|---|---|

## Outcomes
- If criteria are met: ...
- If criteria are not met: <per policy>

## Review Log
| Week | Evidence | Progress (on track / at risk) | Notes |
|---|---|---|---|
```

## Quality checklist
- [ ] Prior documented feedback exists; otherwise the plan is flagged as premature.
- [ ] Every gap has dated, observable examples.
- [ ] Success criteria are measurable and match the level, not a higher bar.
- [ ] Concrete support is listed, with who provides it.
- [ ] Consequences are neutral and policy-based; HR review is flagged.
- [ ] No labels, speculation about causes, or personal/health details.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using a PIP as a paper trail for a decision already made. If there is no genuine chance to succeed, raise this with HR instead.
- Vague criteria ("improve communication"). Specify observable behavior and frequency.
- Surprise. Nothing in the plan should be heard for the first time in the PIP meeting.

## Example
Input: "PRs repeatedly fail review; missed three sprint commitments since April; feedback given in April and June 1:1s."

Excerpt of output:
| Code quality | PRs pass review with only minor comments | 7 of 9 PRs in May-June needed major rework (review history) | ≥ 80% of PRs merged after at most one round of minor comments `[confirm with team norm]` | PR review history |
- Support: Weekly pairing with tech lead; tickets refined with acceptance criteria before start.
