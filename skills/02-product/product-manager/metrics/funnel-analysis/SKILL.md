---
description: Analyzes a conversion funnel step by step, computing step and cumulative conversion, locating the biggest absolute drop-offs, segmenting them, separating data artefacts from real behaviour and turning findings into ranked, testable improvement hypotheses. Use when given funnel numbers or event data for sign-up, onboarding, checkout or activation, or when someone asks "where are we losing users and why".
related: experiment-design, hypothesis-statement, customer-journey-map, north-star-metric, data-exploration
prompt: Here are our sign-up funnel numbers for last month by step and device; find where we lose users and what to try.
---

# Analyze a Funnel

## Purpose
Find where and for whom users drop out of a defined journey, distinguish real behaviour from measurement problems, and produce a short, ranked list of hypotheses that can be tested, instead of a chart with no decision.

## When to use
- Step counts or event data exist for sign-up, onboarding, activation, checkout or upgrade.
- A conversion KPI fell or stagnates and the team needs to know where to look.
- Before choosing which experiment to run on a flow.

## When not to use
- There is no data yet and the team needs to understand the qualitative experience. Use `customer-journey-map` or `research-synthesis`.
- An experiment result must be evaluated. Use `ab-test-analysis`.
- The data is unknown and must first be profiled. Use `data-exploration`.

## Inputs
Required:
- Funnel definition (ordered steps and what event marks each) and counts per step for a period, or raw data to derive them.

Optional, improves quality:
- Segment breakdowns (device, channel, country, new/returning, plan), prior periods.
- Time between steps, qualitative feedback, recent releases or campaigns.

If step definitions or counts are missing, ask. Never fabricate numbers; compute only from the data given and show calculations.

## Process
1. Confirm the funnel definition: entry event, each step's event, ordering (strict or any order), conversion window, and unit (user, session, account). Note if steps are user-level versus session-level mixes.
2. Validate data before interpreting: step counts should not increase down the funnel (unless steps are unordered), period and filters match, bot/test traffic excluded, tracking changes near the period. Flag suspected artefacts separately.
3. Compute step conversion (step n ÷ step n-1), cumulative conversion (step n ÷ entry) and absolute users lost per step. Show the arithmetic.
4. Rank drop-offs by absolute users lost and by distance from any given benchmark or prior period; the biggest percentage drop is not always the biggest opportunity.
5. Segment the top 2-3 drop-offs (device, channel, new/returning, geography, plan). Look for segments with much worse conversion or large volume shifts (mix effects).
6. If timing data exists, examine time-to-convert: long gaps suggest friction or external dependencies (email verification, document upload, approval).
7. Combine with qualitative signals (feedback, session notes, support tickets) when provided; mark every causal explanation `[ASSUMPTION]` unless evidence supports it.
8. Write hypotheses per drop-off: "Because <evidence>, we believe <change> for <segment> will raise <step conversion>". Rank by impact (users affected × plausible lift), confidence and effort.
9. Recommend next actions: instrumentation fixes first if data is doubtful, then the top 1-3 experiments or quick fixes, with the metric and guardrail for each.
10. If the user's goal continues, suggest the next skill: `hypothesis-statement` to sharpen the top hypothesis, `experiment-design` to test it, or `customer-journey-map` to investigate qualitatively.

## Output format
```markdown
# Funnel Analysis: <funnel> · <period> · unit: <user/session/account>

## Data Checks
- ... (artefacts flagged, exclusions applied)

## Funnel
| Step | Count | Step conversion | Cumulative | Users lost |
|---|---|---|---|---|

## Biggest Drop-Offs
1. <step> – <users lost>, <conversion vs prior/benchmark> – segments: <...>

## Segment Findings
| Segment | Step | Conversion | vs overall | Volume |
|---|---|---|---|---|

## Hypotheses (ranked)
| # | Hypothesis | Evidence | Impact | Confidence | Effort |
|---|---|---|---|---|---|

## Recommended Next Actions
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Funnel unit, ordering and conversion window are stated.
- [ ] Data validity checks were done and artefacts are separated from behaviour.
- [ ] All numbers are computed from the given data with visible arithmetic; nothing is invented.
- [ ] Drop-offs are ranked by absolute impact, not only percentage.
- [ ] Every causal explanation is labeled `[ASSUMPTION]` or backed by cited evidence.
- [ ] Each recommended action has a success metric and a guardrail.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Comparing periods with different traffic mix and calling it a conversion change. Segment before concluding.
- Mixing session and user counts across steps. Use one unit throughout.
- Jumping from a drop-off to a redesign. The output is hypotheses to test, not a verdict.

## Example
Input: "Sign-up funnel last month: landing 40,000 → form start 12,000 → form submit 7,200 → email verified 4,300 → first project 2,150; mobile vs desktop split given."

Excerpt of output:
| Step | Count | Step conv. | Cumulative | Lost |
|---|---|---|---|---|
| Email verified | 4,300 | 59.7% | 10.8% | 2,900 |
| First project | 2,150 | 50.0% | 5.4% | 2,150 |
- Largest loss after entry is landing → form start (28,000), but it mixes intent; the biggest controllable loss is submit → verified (2,900).
- Hypothesis `[ASSUMPTION]`: mobile users leave the app to check email and do not return; allowing a deferred verification for mobile users will raise submit → first project.
