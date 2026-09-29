---
name: release-quality-gate
description: "Evaluates release readiness against agreed exit criteria (tests, defects, coverage, non-functional results, operational readiness, approvals), rates each criterion met, not met or waived with evidence, and produces a go, conditional go or no-go recommendation with conditions and accepted risks. Use before a production release or major deployment, in a go/no-go meeting, or when someone asks whether a build is ready to ship."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Evaluate release readiness"
  related: "test-summary-report, bug-triage, go-no-go, deployment-checklist, rollback-plan"
  prompt: "Assess release 5.2 against our exit criteria: no open critical/major bugs, 95% pass rate, regression complete, performance p95 under 800 ms, security scan clean."
---

# Evaluate Release Readiness

## Purpose
Make the quality part of a release decision explicit and auditable: each exit criterion judged against evidence, every exception visible, and the recommendation traceable to the data.

## When to use
- A release candidate is ready and a quality gate or go/no-go meeting is scheduled.
- A team without formal criteria needs a structured readiness check.
- A release is pushed despite open issues and the accepted risks must be recorded.

## When not to use
- You need the narrative quality report of a test cycle. Use `test-summary-report`.
- You need the full cross-functional go/no-go (support, marketing, operations). Use `go-no-go`.
- You need deployment steps or a rollback procedure. Use `deployment-checklist` or `rollback-plan`.

## Inputs
Required:
- The exit criteria (or permission to propose defaults) and current evidence: test results and open defects.

Optional, improves quality:
- Non-functional results (performance, security, accessibility), coverage data, change size.
- Operational readiness: monitoring, rollback plan, runbooks, support briefing.
- Approvers and waiver policy.

If no criteria exist, propose a default set marked `[ASSUMPTION]` and ask the user to confirm before scoring. If evidence for a criterion is missing, rate it "Not evidenced", never "Met".

## Process
1. List the exit criteria in measurable form; rewrite vague ones ("quality is good") and mark the rewrite for confirmation.
2. Group criteria: functional testing, defects, coverage and regression, non-functional, security/compliance, operational readiness, documentation and approvals.
3. For each criterion record the evidence (report, dashboard, ticket IDs) and its date; stale evidence (older than the build under decision) is flagged.
4. Rate each: Met, Not met, Not evidenced, Waived (with approver and reason).
5. For every Not met item, quantify the gap and its business impact, and state the fix-or-accept options.
6. Check blocker defects individually: confirm severity, workaround, affected users and whether a fix is in the candidate build.
7. Check operational safety nets: rollback tested, feature flags, monitoring and alerts for new functionality, on-call awareness.
8. Decide the recommendation: Go (all met or waived), Conditional go (non-critical gaps with conditions and owners before or after release), No-go (any critical gap without acceptable mitigation).
9. Write conditions as verifiable items with an owner and deadline; record accepted risks with the accepting role.
10. Keep facts, ratings and recommendation separate so the decision owner can disagree with the recommendation without disputing the facts.
11. If the user continues, suggest `go-no-go` for the cross-functional decision or `rollback-plan` if the safety net is missing.

## Output format
```markdown
# Release Quality Gate: <product> <release>
**Recommendation:** <Go / Conditional go / No-go> – <one-line reason>
Build under decision: <id> · Evidence as of: <date>

| # | Criterion | Target | Actual | Evidence | Status |
|---|---|---|---|---|---|

Status: Met / Not met / Not evidenced / Waived

## Gaps and Options
- <criterion>: gap <...>, impact <...>, options <fix / accept / mitigate>

## Blocker Review
| Defect | Severity | Workaround | Fixed in build? |
|---|---|---|---|

## Operational Readiness
- Rollback: ... · Monitoring: ... · Support briefing: ...

## Conditions
- <condition> – <owner> – <before/after release, due>

## Accepted Risks
- <risk> – accepted by <role> – <expiry/review date>
```

## Quality checklist
- [ ] Every criterion is measurable and has evidence tied to the build under decision.
- [ ] Missing evidence is rated "Not evidenced", never "Met".
- [ ] Waivers name an approver role and a reason.
- [ ] The recommendation follows from the ratings and the decision rule.
- [ ] Conditions and accepted risks each have an owner and a date or `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using evidence from an earlier build. Any code change after the evidence date invalidates it unless impact is assessed.
- Treating pass rate as the only criterion. A 99% pass rate with an untested payment path is not ready.
- Recording "Go" without writing down the risks accepted. The next incident review will need them.

## Example
Input: "Release 5.2: no open critical/major, 95% pass, regression complete, p95 < 800 ms, security scan clean."

Excerpt of output:
| # | Criterion | Target | Actual | Evidence | Status |
|---|---|---|---|---|---|
| 1 | Open critical/major defects | 0 | 1 major (B-88) | Triage 12th | Not met |
| 2 | Pass rate | ≥95% | 96.1% | Summary report | Met |
| 4 | p95 latency | <800 ms | `[UNKNOWN]` | Perf test on previous build | Not evidenced |

**Recommendation:** Conditional go – B-88 has a documented workaround; conditions: rerun performance test on build 5.2.0-rc3 before deployment (owner: performance engineer); B-88 fix in 5.2.1.
