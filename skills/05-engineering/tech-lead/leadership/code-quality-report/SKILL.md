---
description: Interprets static analysis and code metrics (coverage, complexity, duplication, code smells, vulnerabilities, dependency age) and their trends into a code quality report that separates signal from noise, links hotspots to change frequency and defects, and recommends a small set of prioritized actions. Use when a tech lead must report code health to the team or management, when quality gate results or a metrics dashboard need interpretation, or when deciding where to invest refactoring effort.
related: tech-debt-assessment, coding-standards, test-gap-finder, refactoring, defect-trend-analysis
prompt: Here is our static analysis export for the last three releases. Write a code quality report for the engineering manager and tell us where to focus next quarter.
---

# Report on Code Quality

## Purpose
Turn raw quality metrics into a short, honest report: what is improving, what is getting worse, where the risk actually sits and which few actions will pay off. Metrics are evidence for decisions, not targets in themselves.

## When to use
- A periodic (release, quarter) code health report is due for the team or management.
- A quality gate failed or a dashboard shows alarming numbers that need interpretation.
- The team must decide which modules deserve refactoring or testing investment.

## When not to use
- A single pull request needs review. Use `code-review` or `clean-code-review`.
- The goal is a full inventory and repayment plan of technical debt. Use `tech-debt-assessment`.
- Specific untested paths must be found in code. Use `test-gap-finder`.

## Inputs
Required:
- Metric data: static analysis results, coverage, or an export/screenshot description with numbers per module or over time.

Optional, improves quality:
- Several snapshots for trends; change frequency (commits per file/module); defect or incident counts per module.
- Quality gate thresholds, coding standards, audience of the report.
- Recent context: large refactorings, new modules, rule set changes.

If no metric data is provided, ask for it. Never generate metric values; missing ones are `[UNKNOWN]`.

## Process
1. Identify the audience (team vs management) and the period; set the level of detail accordingly.
2. Check data validity before interpreting: same rule set and scope across snapshots, generated or vendored code excluded, coverage measured the same way. Flag any comparability break.
3. Summarize the headline metrics per snapshot: coverage (line and branch if available), cyclomatic/cognitive complexity, duplication, code smells, bugs, vulnerabilities and security hotspots by severity, outdated or vulnerable dependencies.
4. Compute trends (direction and size) and separate new-code quality from overall legacy levels; a stable total can hide worsening new code.
5. Find hotspots: modules with high complexity or low coverage that also change often or have defects. Where churn or defect data is missing, mark the hotspot ranking `[ASSUMPTION]`.
6. Interpret, do not just restate: explain likely causes (e.g., coverage fell because a large untested module was added), and label each interpretation as inferred.
7. Triage issues: security vulnerabilities and critical bugs first, then hotspots, then consistency and smells. Call out noisy rules that should be tuned instead of fixed.
8. Recommend three to five actions, each with owner type, scope, expected effect on a named metric and a verification step (e.g., "branch coverage of billing ≥ 70% at next snapshot").
9. State limits of the data and open questions.
10. If the goal continues, suggest `tech-debt-assessment` for a repayment plan, `test-gap-finder` for low-coverage hotspots, or `refactoring` for a specific module.

## Output format
```markdown
# Code Quality Report: <system> · <period>
Audience: <team/management> · Data: <tool/export, snapshots> · Comparability: <ok / caveats>

## Summary
<3-5 sentences: overall direction, biggest risk, main recommendation>

## Metrics and Trend
| Metric | Previous | Current | Trend | Comment |
|---|---|---|---|---|

## Hotspots
| Module | Complexity | Coverage | Change frequency | Defects | Why it matters |
|---|---|---|---|---|---|

## Recommended Actions
| # | Action | Scope | Target metric and value | Verified by |
|---|---|---|---|---|

## Data Limits and Open Questions
- ...
```

## Quality checklist
- [ ] Every number in the report comes from the provided data; missing values are `[UNKNOWN]`.
- [ ] Comparability of snapshots was checked and caveats are stated.
- [ ] New-code quality is distinguished from legacy totals.
- [ ] Hotspots combine at least two signals (e.g., complexity and change frequency), or the ranking is labeled as an assumption.
- [ ] Each recommendation has a measurable target and a verification step.
- [ ] Security findings are reported separately and ranked by severity.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Chasing a global coverage percentage. Coverage on stable, simple code adds little; focus on changing, complex code.
- Reporting a rule set or scope change as a quality improvement or collapse. Check comparability first.
- Listing hundreds of smells. Management needs direction and three actions; the team needs the hotspot list.

## Example
Input: Coverage 61% → 58% → 55%; duplication stable at 4%; 2 new critical vulnerabilities; billing module complexity highest and 40% of commits.

Weak: "Coverage dropped by 6 points, please write more tests."

Strong excerpt:
- Summary: Overall coverage fell 6 points over three releases, driven mainly by the new export module added without tests `[ASSUMPTION: confirm from per-module data]`. Two critical vulnerabilities in dependencies need fixing this iteration.
- Action 1: Upgrade the two vulnerable libraries; verified by zero critical vulnerabilities in the next scan.
- Action 2: Add characterization tests to billing before further changes; target branch coverage ≥ 60% at next snapshot.
