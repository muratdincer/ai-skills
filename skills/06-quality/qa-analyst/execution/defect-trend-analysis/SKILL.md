---
description: "Analyzes defect data over time to expose density, escape (leakage) rate, reopen rate, ageing and root-cause categories, separating real quality signals from reporting noise and ending with evidence-backed improvement actions. Use when a team asks why quality is dropping, prepares a retrospective or quality review, needs to explain production escapes, or has a defect export and wants the trends interpreted."
related: bug-triage, test-summary-report, five-whys, engineering-metrics-review, code-quality-report
prompt: "Here is our defect export for the last 6 releases. Analyze the trends: where are bugs coming from, how many escape to production, and what should we change?"
---

# Analyze Defect Trends

## Purpose
Turn a defect log into a small set of trustworthy trend findings (where defects are introduced, where they are caught, where they escape) and targeted improvement actions, so the team fixes the process that produces defects rather than only the defects.

## When to use
- A quality review, retrospective or steering meeting needs a data-backed view of defects across releases or iterations.
- Production escapes or customer-reported bugs have increased and the team needs to know why.
- Management asks whether quality is improving, and the answer must be defended with numbers.

## When not to use
- Individual bugs need a fix/no-fix decision. Use `bug-triage`.
- A single release needs a results report for stakeholders. Use `test-summary-report`.
- One specific incident needs a causal analysis. Use `five-whys` or `postmortem`.

## Inputs
Required:
- Defect records (export or summary) with at least: created date, severity, status, component/module, and the phase or environment where found.

Optional, improves quality:
- Root-cause category, phase introduced, release/iteration tag, reopen count, closed date.
- Size normalizers: changed lines, story points, number of changes, test cases executed, active users.
- The team's severity definitions and any process changes made during the period.

If defect data is missing, ask for it. If no size normalizer exists, report absolute counts only and state that density cannot be computed; do not invent a denominator.

## Process
1. Profile the data first: period covered, record count, missing fields per column, duplicate/rejected share. State data quality limits before any finding.
2. Normalize categories (merge synonyms in components and root causes; map severities to the team scale). Record every mapping you inferred as `[ASSUMPTION]`.
3. Compute the core metrics per release or period: arrivals vs closures, open backlog, density (defects / size unit if available), escape rate (found in production ÷ total found), reopen rate, median age of open defects by severity.
4. Build a phase-containment view: phase introduced × phase found (requirements, design, code, integration, system test, UAT, production). Highlight defects found two or more phases after they were introduced.
5. Rank components and root-cause categories with a Pareto cut (the ~20% of categories producing most defects). Separate high-count from high-severity clusters.
6. Test every apparent trend against noise: small samples, changed reporting rules, a big release, a new tester or tool. A trend needs at least three data points in the same direction; otherwise call it a signal to watch.
7. Correlate with known events only when the user supplied them (process change, team change, architecture change); label any causal link as a hypothesis, not a conclusion.
8. Derive 3-5 improvement actions, each tied to one finding, with owner role, expected metric movement and a review date `[TBD]` if not given.
9. Define how to measure the effect: which metric, baseline value, target direction, next review point.
10. If the user continues, suggest `five-whys` for the top cluster, `risk-based-testing` to refocus test effort on hot components, or `engineering-metrics-review` for a broader delivery view.

## Output format
```markdown
# Defect Trend Analysis: <product/team>, <period>
## Data Basis
- Records: <n> | Period: <from–to> | Missing fields: <list> | Excluded: <n rejected/duplicates>
- Limits: <what cannot be concluded>

## Key Metrics
| Release/Period | Arrived | Closed | Open | Density | Escape rate | Reopen rate | Median age (Critical/Major) |
|---|---|---|---|---|---|---|---|

## Phase Containment
| Introduced \ Found | Req | Design | Code | Integr. | System | UAT | Prod |
|---|---|---|---|---|---|---|---|

## Findings
1. <finding> — evidence: <numbers> — confidence: High/Medium/Low — [HYPOTHESIS] cause: <...>

## Improvement Actions
| # | Action | Addresses finding | Owner role | Metric to move | Review date |
|---|---|---|---|---|---|

## Watch List (weak signals)
- ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Data quality limits are stated before the findings.
- [ ] Every finding cites the numbers it rests on and carries a confidence level.
- [ ] Density is only reported with a real size normalizer; no invented denominators.
- [ ] Causes are labeled as hypotheses unless the data proves them.
- [ ] Each action is linked to a finding and to a metric that should move.
- [ ] No individual developer or tester is named or ranked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reading a rising defect count as falling quality. More testing, a new tester or better reporting also raises counts; check effort and scope first.
- Using defect metrics to rank people. It destroys reporting honesty; analyze components and process steps instead.
- Declaring a trend from two data points. Mark it as a watch item until the pattern holds.

## Example
Input: 412 defects over 6 releases; fields: created, severity, component, found-in environment; no size data.

Excerpt of output:
- Limits: no size normalizer, so density is not reported; 9% of records lack a component.
- Finding: escape rate rose from 6% to 14% over releases 4-6; 58% of escapes are in `payments` — confidence Medium. `[HYPOTHESIS]` cause: payments integration tests were moved out of the release pipeline in release 4 (confirm with the team).
- Action: restore payments contract tests in the pipeline — metric: escape rate in `payments` — review after 2 releases.
