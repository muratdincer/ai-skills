---
name: bug-triage
description: "Triages a set of bugs by validating completeness, detecting duplicates, separating severity (impact) from priority (order of fixing), assigning owner and target, and flagging release blockers, producing a decision table and follow-up list. Use when new or backlog defects must be reviewed in a triage meeting, when a release is near and open bugs need a blocker decision, or when someone asks which bugs to fix first."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Triage bugs"
  related: "bug-report, release-quality-gate, defect-trend-analysis, risk-based-testing, ticket-triage"
  prompt: "Triage these 14 open bugs before Friday's release: decide severity, priority, duplicates and which ones block the release."
---

# Triage Bugs

## Purpose
Turn an unordered set of defect reports into clear, justified decisions: what gets fixed, by whom, in which release, and what blocks shipping.

## When to use
- A regular triage session reviews newly reported defects.
- A release candidate has open bugs and a blocker/non-blocker decision is needed.
- The defect backlog has grown and needs cleaning (duplicates, stale, rejected).

## When not to use
- A single defect still needs to be written up properly. Use `bug-report`.
- You need statistics and root-cause patterns over time. Use `defect-trend-analysis`.
- You need the overall go/no-go decision for a release. Use `release-quality-gate`.

## Inputs
Required:
- The list of bugs with at least title, description and current status.

Optional, improves quality:
- Severity and priority definitions used by the team, release date and scope, component owners.
- Usage data, customer reports, SLA commitments, known workarounds.

If the bug list is missing, ask for it. If the team has no severity/priority scale, use the default below and mark it `[ASSUMPTION]`.

## Process
1. Confirm the scales. Default severity: Critical (data loss, security, outage, no workaround), Major (core function broken, hard workaround), Minor (limited function, easy workaround), Trivial (cosmetic). Default priority: P1 fix now, P2 this release, P3 next release, P4 backlog.
2. Validate each report: reproducible steps, environment, expected result. Mark incomplete ones "Need info" with the exact missing item and the person to ask.
3. Detect duplicates and clusters by symptom, component and root cause signals; keep the most complete report as primary and link the others.
4. Classify each item: defect, change request/new requirement, works as designed, environment/data issue, cannot reproduce. Only defects continue.
5. Assess severity from technical impact, independently of who reported it.
6. Assess priority from severity combined with business factors: affected users and frequency, visibility, compliance or contractual exposure, workaround cost, fix risk and effort, release timing. Explain every case where priority differs from severity.
7. Flag release blockers against the release exit criteria; blockers must be P1/P2 with a named owner.
8. Assign owner (team or component) and target release or iteration; do not name individuals unless given.
9. Record the decision and rationale for each bug in one line so absent stakeholders can follow.
10. Summarize: counts by decision, blockers, items needing information, and risks accepted by deferral.
11. If the user continues, suggest `release-quality-gate` for the ship decision or `defect-trend-analysis` when clusters point to systemic issues.

## Output format
```markdown
# Bug Triage: <scope / date>
Scales used: <team scale or default [ASSUMPTION]>

| Bug | Title | Class | Severity | Priority | Blocker | Owner | Target | Rationale |
|---|---|---|---|---|---|---|---|---|

## Duplicates and Clusters
- <primary> ← <duplicates> – <shared symptom>

## Need Info
- <bug>: <missing item> – ask <role>

## Summary
- Blockers: n (list) · Fix this release: n · Deferred: n · Rejected/WAD: n
- Risks accepted by deferral: ...
```

## Quality checklist
- [ ] Severity and priority are assessed separately and differences are explained.
- [ ] Every blocker has an owner and a target, and is traceable to an exit criterion.
- [ ] Duplicates are linked to a single primary report.
- [ ] Non-defects (change requests, works as designed) are separated with a reason.
- [ ] No owner names, dates or user counts are invented; unknowns are `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Equating severity and priority. A cosmetic typo on the payment page may be P1; a crash in a retired admin screen may be P4.
- Letting the loudest stakeholder set priority. Use the same factors for every bug and write the rationale.
- Deferring the same bug every release. Items deferred more than twice should be explicitly accepted or closed.

## Example
Input: "14 open bugs, release Friday."

Excerpt of output:
| Bug | Title | Class | Severity | Priority | Blocker | Rationale |
|---|---|---|---|---|---|---|
| B-102 | Invoice PDF shows wrong VAT total for multi-rate baskets | Defect | Critical | P1 | Yes | Legal document incorrect; no workaround |
| B-109 | Logo misaligned on login page in dark mode | Defect | Trivial | P3 | No | Cosmetic, low visibility |
| B-111 | "Export should include tax number" | Change request | – | – | No | New requirement; route to backlog |
| B-114 | Same as B-102, reported from mobile | Duplicate | – | – | – | Linked to B-102 |
