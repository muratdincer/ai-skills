---
description: "Prepares a team for an internal, certification, customer or regulatory audit: confirms scope and criteria, builds an evidence request list with owners and due dates, runs a readiness gap check, and plans the audit week and auditee briefing. Use when an audit date is announced (ISO 27001, SOC 2, KVKK, PCI DSS, BDDK, customer audit), when an auditor sends a PBC/request list, or when previous findings must be closed before the next audit."
related: "control-mapping, access-review, policy-writing, it-risk-assessment, schedule-plan"
prompt: "Our ISO 27001 surveillance audit is in six weeks. Prepare the evidence list, gaps and plan."
---

# Prepare for an Audit

## Purpose
Turn an announced audit into a controlled project: everyone knows what evidence is expected, who delivers it by when, which gaps must be closed first, and how interviews will be handled, so the audit produces no surprises and no avoidable findings.

## When to use
- An audit or assessment date is set: certification, surveillance, SOC 2 examination, KVKK inspection readiness, PCI DSS assessment, customer audit.
- An auditor sends a request list ("prepared by client" list) and it must be distributed and tracked.
- Previous audit findings or nonconformities must be closed and evidenced before the next visit.

## When not to use
- You first need to know which controls satisfy the standard. Use `control-mapping`.
- The finding is a policy that does not exist. Use `policy-writing`.
- You need a periodic entitlement review as the evidence itself. Use `access-review`.

## Inputs
Required:
- Audit type, standard or criteria, and the audit date or window.

Optional, improves quality:
- Scope (entities, sites, systems, processes), audit period for operating-effectiveness audits.
- Auditor's request list, previous audit report and open findings, Statement of Applicability, control mapping.
- Team availability and known blackout dates.

If audit type or date is missing, ask for them. Everything else becomes `[TBD]` or an open question.

## Process
1. Confirm scope, criteria, standard version, audit period (for SOC 2 Type II, the observation period), audit dates, auditor and audit style (remote/on-site, sampling approach).
2. Build the evidence list: for each requirement or request item, the evidence artifact, system of record, period covered, owner, due date and status. Start from the auditor's list if given, otherwise from the control mapping.
3. Prioritize the high-scrutiny areas: management system clauses (risk assessment, internal audit, management review), access management, change management, incident management, supplier management, backup/restore, logging, awareness training.
4. Run a readiness check on every evidence item: exists, complete for the period, dated, approved, consistent with the policy wording. Classify gaps as Missing, Incomplete or Inconsistent.
5. Plan remediation for gaps with owner and date. Distinguish what can be legitimately fixed now (e.g. perform an overdue review) from what cannot be back-dated; never create or alter evidence retroactively.
6. Check previous findings: each has a root cause, corrective action, evidence of implementation and effectiveness.
7. Minimize personal data in evidence: mask national ID numbers, salaries and health data; share samples rather than full exports; use the auditor's secure channel.
8. Prepare the audit logistics: schedule of sessions per area, interviewee per session with a backup, evidence room or shared folder structure, single point of contact, request tracking log.
9. Brief the interviewees: answer what is asked, show evidence rather than describe, say "I will check and come back" when unsure, record follow-up requests.
10. Build a timeline from today to audit day with weekly checkpoints and a dry run or internal pre-audit one to two weeks before.
11. Label every status not confirmed by the user as `[ASSUMPTION]`; suggest `control-mapping` if no mapping exists, `access-review` or `policy-writing` for specific gaps.

## Output format
```markdown
# Audit Preparation: <audit type, standard> – <dates>
## Scope and Criteria
- Scope: ... / Period: ... / Auditor: [TBD] / Format: remote / on-site
## Evidence Tracker
| # | Requirement / request | Evidence | System / location | Period | Owner | Due | Status (Ready/Gap) |
## Gaps and Remediation
| # | Gap type | Description | Action | Owner | Due | Can be closed before audit? |
## Previous Findings
| Finding | Corrective action | Evidence of effectiveness | Status |
## Audit Schedule and Interviewees
| Day / time | Area | Interviewee | Backup |
## Timeline to Audit Day
- Week -6: ... / Week -2: internal dry run / Week 0: audit
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every evidence item has an owner, due date and the period it must cover.
- [ ] Gaps are classified and none is "fixed" by back-dating or fabricating evidence.
- [ ] Previous findings each show effectiveness evidence, not only the action taken.
- [ ] Personal data in evidence is masked or sampled.
- [ ] The timeline includes a dry run before audit day.
- [ ] Unconfirmed statuses and dates are marked `[ASSUMPTION]` or `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Collecting evidence the week before the audit and discovering the control did not operate for months. Start with period coverage checks.
- Over-sharing: sending entire HR or customer datasets instead of samples. Share the minimum needed and log what was shared.
- Interviewees volunteering speculation. Brief them to answer precisely and show evidence.
- Treating the audit as a documentation exercise. If the control does not operate, record it as a gap and fix it properly.

## Example
Input: "ISO 27001 surveillance audit in six weeks; last year we had a minor nonconformity on supplier reviews."

Excerpt of output:
| 7 | A.5.22 supplier service monitoring | Annual supplier review records | GRC folder / Suppliers | Last 12 months | Procurement lead [ASSUMPTION] | Week -4 | Gap: 3 of 11 critical suppliers not reviewed |
| Previous NC-02 supplier reviews | Review template introduced | Completed reviews for all critical suppliers | Open – effectiveness not yet shown |
