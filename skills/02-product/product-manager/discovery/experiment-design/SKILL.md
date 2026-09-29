---
description: Designs a product experiment (A/B test, fake-door, painted-door, concierge or prototype test) from a hypothesis, with variants, randomization unit, primary and guardrail metrics, minimum detectable effect, sample size and duration, stop rules and a pre-committed decision rule. Use when a team wants to validate a hypothesis with real users, asks how to set up an A/B or fake-door test, or needs to check an experiment plan before launch.
related: hypothesis-statement, ab-test-analysis, assumption-mapping, metric-definition, funnel-analysis
prompt: Design an A/B test for our new pricing page layout; we get about 40,000 visitors a week and trial sign-up is 3.2%.
---

# Design a Product Experiment

## Purpose
Produce an experiment plan that can actually answer the hypothesis: the right test type, enough statistical power, clean measurement and a decision rule fixed before any data is seen.

## When to use
- A written hypothesis needs a test before engineering investment or rollout.
- A team plans an A/B test and needs sample size, duration and metrics set up correctly.
- Demand for a not-yet-built feature must be gauged (fake door, waitlist, concierge).
- An existing experiment plan must be reviewed for flaws before launch.

## When not to use
- There is no clear hypothesis yet. Use `hypothesis-statement` first.
- The experiment has run and results need interpreting. Use `ab-test-analysis`.
- The question is exploratory ("why do users churn?"). Use `problem-interview-script` or `research-plan`.

## Inputs
Required:
- The hypothesis (change, segment, expected behavior change) or enough to write one.
- Rough traffic or number of eligible users per week.

Optional, improves quality:
- Baseline rate/mean and variance of the primary metric; minimum effect worth acting on.
- Constraints: legal/consent rules, pricing fairness, sales commitments, engineering effort.
- Existing experimentation platform conventions (bucketing, exposure logging).

If the hypothesis or traffic is missing, ask for it. Never invent a baseline; if it is unknown, plan a baseline-measurement step first.

## Process
1. Restate the hypothesis and the decision the experiment informs; if the hypothesis is vague, sharpen it (segment, metric, threshold) and mark changes `[ASSUMPTION]`.
2. Choose the test type by the riskiest assumption and traffic: A/B or multivariate for optimizing existing flows with enough traffic; fake door / painted door for demand; concierge or Wizard-of-Oz for value delivery; moderated prototype test when traffic is too low.
3. Define variants (control and at most 1-2 treatments) and the single variable that differs; list what must stay identical.
4. Pick the randomization unit (user, account, session, region) to avoid contamination; use account level for B2B shared workspaces and when network effects exist.
5. Define the primary metric (one), secondary metrics and guardrails, each with formula, source and exposure definition (who counts as "in the experiment").
6. Calculate sample size from baseline, minimum detectable effect (MDE), significance (commonly alpha 0.05, two-sided) and power (commonly 0.8); convert to duration using eligible traffic and round up to full weeks to cover weekly cycles. If the duration exceeds what is acceptable, raise the MDE, change the metric, or switch test type.
7. Set stop rules: fixed horizon (no peeking) or a pre-declared sequential method; stop early only for guardrail breaches, bugs or sample-ratio mismatch.
8. Pre-commit the decision rule: ship / iterate / kill for each outcome, including "flat" results.
9. List validity threats and mitigations: novelty effects, seasonality, SRM, bot traffic, overlapping experiments, instrumentation gaps; for fake doors, plan the honest follow-up message to users.
10. Cover ethics and privacy: consent, no deceptive pricing to paying customers, personal data minimized in event logging.
11. Produce the plan with owners, launch checklist (QA of variants, event verification, A/A or SRM check) and open questions.
12. If the user's goal continues, suggest the next skill: `ab-test-analysis` once data is in, or `metric-definition` if the primary metric is not yet defined precisely.

## Output format
```markdown
# Experiment Plan: <name>
Hypothesis: <one sentence> · Decision owner: <name | [UNKNOWN]>

| Item | Value |
|---|---|
| Test type | <A/B / fake door / concierge / ...> – <why> |
| Variants | Control: ... / Treatment: ... |
| Randomization unit | <unit> – <why> |
| Eligible population | <segment, inclusion/exclusion> |
| Primary metric | <formula, source, exposure rule> |
| Guardrails | <metric – threshold> |
| Baseline / MDE | <value | [UNKNOWN]> / <value> |
| Alpha / power | <values> |
| Sample size per variant | <n> |
| Duration | <weeks> (<traffic assumption>) |
| Stop rules | ... |

## Decision Rule
| Outcome | Decision |
|---|---|
| Significant positive, guardrails OK | ... |
| Flat / inconclusive | ... |
| Negative or guardrail breach | ... |

## Validity Threats and Mitigations
- ...
## Launch Checklist
- [ ] Variants QA'd  - [ ] Events verified  - [ ] SRM check scheduled
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Only one variable differs between control and treatment.
- [ ] Sample size and duration are computed from stated inputs, and inputs not given are marked `[UNKNOWN]` or `[ASSUMPTION]`.
- [ ] Duration covers at least one full weekly cycle and is feasible with the stated traffic.
- [ ] The decision rule covers positive, flat and negative outcomes before launch.
- [ ] Guardrails and stop rules exist; peeking is excluded or a sequential method is named.
- [ ] Privacy, consent and fairness risks are addressed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Running an A/B test on too little traffic and reading noise as a result. Compute power first; switch to qualitative testing if the math does not work.
- Stopping the test the day it turns significant. Fix the horizon or use a sequential method declared in advance.
- Randomizing by session when users return several times. Randomize by the unit that experiences the change.
- Treating fake-door clicks as purchase intent without a follow-up step. Add a second commitment signal (waitlist, email, pre-order).

## Example
Input: "A/B test a new pricing page layout; about 40,000 visitors/week, trial sign-up 3.2%."

Excerpt of output:
- Test type: A/B, user-level randomization (cookie + logged-in ID).
- Primary metric: trial sign-ups / unique pricing page visitors; guardrail: paid conversion of trials at day 14.
- MDE 10% relative (3.2% to 3.52%), alpha 0.05 two-sided, power 0.8: about 49,000 per variant, so roughly 3 weeks with 2 variants.
- Decision rule: flat result means keep control and stop investing in layout; test the value messaging instead.
