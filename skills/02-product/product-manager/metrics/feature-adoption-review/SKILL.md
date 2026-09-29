---
description: Reviews a shipped feature's adoption, retention and outcome against the goals set before launch, using a reach-activation-retention-outcome breakdown, segment cuts and qualitative signals, and ends with a keep, iterate, promote or retire recommendation. Use some weeks after a release, in a post-launch review, or when someone asks "is anyone using this feature and did it work".
related: kpi-definition, funnel-analysis, feedback-synthesis, benefits-realization, product-sunset-plan
prompt: Review adoption of the bulk-edit feature we shipped 8 weeks ago; here are usage numbers and support tickets.
---

# Review Feature Adoption

## Purpose
Judge whether a shipped feature reached the intended users, became a habit and moved the outcome it was built for, and turn the evidence into a clear decision instead of a usage chart nobody acts on.

## When to use
- A feature has been live long enough for the target users to encounter it several times (depends on usage frequency).
- A post-launch or quarterly review needs evidence on what shipped features delivered.
- The team debates whether to invest more in, change or remove a feature.

## When not to use
- The feature is not live yet and success measures must be set. Use `kpi-definition`.
- The question is where users drop in a multi-step flow. Use `funnel-analysis`.
- The decision to remove is already made and needs execution. Use `product-sunset-plan`.

## Inputs
Required:
- The feature, its target users and intended outcome, and the usage data available (counts, rates or raw events for a period).

Optional, improves quality:
- Pre-launch goals or hypothesis, rollout dates and exposure (flags, segments).
- Segment breakdowns, retention cohorts, outcome metric trend, feedback, support tickets.

If usage data or the intended outcome is missing, ask. Never fabricate numbers; compute only from given data and show calculations.

## Process
1. Restate the feature's target users, intended job and the success criteria set before launch; if none existed, reconstruct candidates and mark them `[ASSUMPTION]` (post-hoc goals are weaker evidence).
2. Define the eligible population: users who could use the feature (right plan, platform, role, exposed by rollout). Adoption rates use this as denominator, not all users.
3. Break adoption into stages: reach/awareness (saw or opened), activation (completed the core action once), repeat use/retention (used again within the expected frequency), and depth (share of relevant tasks done with the feature).
4. Compute each stage from the data, with period and cohort stated; show the arithmetic and mark missing stages `[TBD]` with the instrumentation needed.
5. Segment by user type, plan, platform and cohort (launch week vs later); look for a segment where the feature works well and one where it fails.
6. Assess outcome: did the intended metric move for adopters versus comparable non-adopters or the pre-launch trend? State the confounders (seasonality, other releases, self-selection) and avoid causal claims without a controlled comparison.
7. Add qualitative evidence: feedback themes, support tickets, sales/CS notes; tie each to a stage where it explains a gap.
8. Diagnose the main bottleneck: discoverability, value, usability, performance/reliability or fit to the wrong segment.
9. Recommend one decision with rationale: keep as is, iterate (named bottleneck + next test), promote (invest in discovery/rollout), or retire. Include cost of keeping (maintenance, complexity) if known.
10. Mark inferences `[ASSUMPTION]`. If the user's goal continues, suggest the next skill: `experiment-design` or `hypothesis-statement` for an iteration, `feedback-synthesis` for deeper qualitative work, or `product-sunset-plan` if retiring.

## Output format
```markdown
# Feature Adoption Review: <feature> · live since <date> · period <...>
Target users: <...> · Intended outcome: <...> · Pre-launch goal: <... or [ASSUMPTION]>

## Eligible Population
<definition and count>

## Adoption Stages
| Stage | Definition | Value | Goal | Status |
|---|---|---|---|---|
| Reach | | | | |
| Activation | | | | |
| Retention | | | | |
| Depth | | | | |

## Segments
| Segment | Activation | Retention | Note |
|---|---|---|---|

## Outcome Impact
- Observed: ... · Comparison basis: ... · Confounders: ...

## Qualitative Signals
- ...

## Diagnosis and Decision
- Bottleneck: ... · Decision: <keep/iterate/promote/retire> – rationale
- Next steps: ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Adoption rates use the eligible population as the denominator.
- [ ] Reach, activation, retention and depth are separated; missing ones are `[TBD]`.
- [ ] All numbers come from the given data with visible arithmetic.
- [ ] Outcome claims name the comparison basis and confounders; no unsupported causality.
- [ ] Post-hoc goals are labeled `[ASSUMPTION]`.
- [ ] The review ends with one decision and concrete next steps.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting "30% of users tried it" as success. One-time trial is curiosity; retention and outcome show value.
- Dividing by all users when only admins or one plan could use the feature. Always define eligibility.
- Treating adopters' better results as caused by the feature. Power users adopt everything first; compare like with like.

## Example
Input: "Bulk-edit shipped 8 weeks ago. Eligible: 5,000 admins; 2,600 opened it, 1,300 completed a bulk edit, 390 used it again in 4 weeks. 14 support tickets about undo."

Excerpt of output:
| Stage | Value | Status |
|---|---|---|
| Reach | 2,600 / 5,000 = 52% | Goal `[ASSUMPTION]` |
| Activation | 1,300 / 5,000 = 26% (50% of reach) | – |
| Retention | 390 / 1,300 = 30% repeat in 4 weeks | Weak |
- Diagnosis `[ASSUMPTION]`: value is there for first use, but fear of irreversible changes (undo tickets) suppresses repeat use.
- Decision: iterate – add preview and undo, re-measure retention for the next cohort.
