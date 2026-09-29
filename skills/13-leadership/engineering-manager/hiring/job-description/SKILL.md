---
description: Writes an inclusive, accurate job description for a software role with the role mission, first-year outcomes, responsibilities, must-have versus nice-to-have requirements, team context and practical details, and checks it for biased or exclusionary language. Use when opening a new position, rewriting an outdated posting, or when a posting attracts the wrong candidates or too few diverse applicants.
related: role-definition, interview-plan, career-ladder, onboarding-plan-30-60-90, tone-rewrite
prompt: Write a job description for a Senior Data Engineer in our Istanbul platform team, hybrid, working on streaming pipelines with Kafka and Spark.
---

# Write a Job Description

## Purpose
Attract the right candidates and let them self-select accurately by describing what the role achieves, what it really requires and what working here is like, in language that does not exclude qualified people.

## When to use
- A new position is approved and needs a public posting.
- An existing posting is outdated or brings mismatched applicants.
- Hiring aims to widen the candidate pool and the text needs an inclusivity review.

## When not to use
- Internal responsibilities and decision rights of a role. Use `role-definition`.
- Designing the interview stages. Use `interview-plan`.
- Level expectations for existing staff. Use `career-ladder`.

## Inputs
Required:
- Role title and level, team and what the role must achieve, key technologies or domain.

Optional, improves quality:
- Location, work model (on-site/hybrid/remote), employment type, salary range (if disclosed), benefits.
- Team size and structure, reporting line, product context.
- Company boilerplate and equal opportunity statement.
- Local legal requirements for postings.

If the role's purpose or level is unclear, ask; do not invent compensation, benefits or company facts, mark them `[TBD]`.

## Process
1. Write a 2-3 sentence mission: why the role exists and what success looks like after about a year.
2. List 4-6 outcomes or responsibilities as verbs with context ("design and operate streaming pipelines for order events"), not a task dump.
3. Separate must-have from nice-to-have. Keep must-haves to 4-6 items that are truly required on day one.
4. Express experience as capabilities, not years where possible ("has operated production data pipelines at scale" instead of "8+ years").
5. Remove requirements that act as proxies (specific universities, degree when not needed, "native speaker" when professional fluency suffices, age-coded words like "young, dynamic").
6. Language pass: replace gender-coded or exclusionary terms (rockstar, ninja, aggressive, dominant, "guys"), use "you" and gender-neutral language; in Turkish avoid gendered role titles.
7. Describe the team, the tech environment and the way of working honestly, including on-call or travel if applicable.
8. Add practicals: location, work model, employment type, salary range if allowed, accommodations statement, how to apply, process steps.
9. Add an equal opportunity and accommodation line consistent with local law and the organization's policy.
10. Check length (400-700 words) and readability; mark unknown facts `[TBD]`.
11. If the user's goal continues, suggest `interview-plan` to design the loop against the same requirements, or `onboarding-plan-30-60-90` for the new hire.

## Output format
```markdown
# <Title> (<level>) – <team>
Location / model: <...> · Type: <...> · Salary: <range or [TBD]>

## Why This Role Exists
<mission, 2-3 sentences>

## What You Will Do
- ...

## What You Bring (must-have)
- ...

## Nice to Have
- ...

## The Team and How We Work
- ...

## What We Offer
- ...

## Hiring Process
<steps, approximate duration>

<Equal opportunity and accommodation statement>
```

## Quality checklist
- [ ] Mission states outcomes, not just duties.
- [ ] Must-haves are at most six and genuinely required on day one.
- [ ] No gender-coded, age-coded or exclusionary language; no unnecessary degree or years requirements.
- [ ] On-call, travel and work model are stated honestly.
- [ ] No invented salary, benefits or company claims; unknowns marked `[TBD]`.
- [ ] Hiring process steps are listed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Wish lists of 15 technologies. They deter qualified candidates who apply only when meeting all criteria. Move extras to nice-to-have.
- Copying the internal ladder text. Candidates need outcomes and context, not calibration language.
- Promising culture traits the team cannot demonstrate. Describe concrete practices instead.

## Example
Input: "Senior Data Engineer, Istanbul platform team, hybrid, streaming with Kafka and Spark."

Excerpt of output:
- Why this role exists: Our platform team turns order and payment events into reliable, near-real-time data for product and finance. You will own key streaming pipelines and raise the bar for data quality across the platform.
- Must-have: Designed and operated production streaming pipelines (e.g. Kafka with Spark or Flink).
- Salary: `[TBD – confirm if range can be published]`
