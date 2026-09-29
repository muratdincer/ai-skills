---
name: access-review
description: "Runs a user access review (access recertification) for an application, database, cloud account or directory group: compares entitlements with HR and role data to detect excessive, orphaned, dormant, shared and toxic (separation-of-duties conflicting) permissions, and produces revoke/keep decisions with evidence for auditors. Use for periodic ISO 27001, SOC 2, SOX or BDDK access reviews, after reorganizations, or when privilege creep is suspected."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: security-engineer
  area: operations
  title: "Run an access review"
  related: "authn-authz-design, audit-preparation, control-mapping, it-risk-assessment, raci-matrix"
  prompt: "Here is the export of users and roles from our ERP and the HR active employee list. Run a quarterly access review and flag what should be revoked."
---

# Run an Access Review

## Purpose
Confirm that every account and entitlement is still needed, owned and compliant with least privilege and separation of duties, and leave an auditable trail of decisions.

## When to use
- A periodic access recertification is due (quarterly or annually per policy).
- After reorganizations, mergers, mass leavers or a role model change.
- An auditor, incident or suspicion of privilege creep triggers a targeted review.

## When not to use
- Designing a new role or permission model. Use `authn-authz-design`.
- Collecting evidence for many controls at once. Use `audit-preparation`.
- Investigating a suspected compromised account. Use `security-incident-response`.

## Inputs
Required:
- Entitlement export for the system in scope (account, role/group/permission, last login if available).

Optional, improves quality:
- HR roster (active, leavers, movers with department and manager).
- Role catalog with intended permissions, separation-of-duties (SoD) rule set.
- Previous review results and approved exceptions.

If the entitlement export is missing, ask. If HR data is missing, flag orphan detection as not possible and list it as a gap. Work with pseudonymized identifiers where possible; do not repeat personal data beyond what the review needs.

## Process
1. Define scope and review period: system, environments, account types (human, service, shared, break-glass), reviewers (managers and system owners).
2. Normalize data: one row per account-entitlement; map accounts to HR identities by a stable key; mark unmatched accounts.
3. Detect orphaned accounts: no matching active employee or contractor, or owner left.
4. Detect dormant accounts: no login beyond the policy threshold (e.g. 90 days) [ASSUMPTION if policy unknown].
5. Detect excessive access: entitlements beyond the role catalog, privileged roles held by non-admin functions, movers keeping old department access.
6. Detect toxic combinations using SoD rules (e.g. create vendor + approve payment; develop + deploy to production without review).
7. Review non-human and shared accounts: owner, purpose, credential rotation, interactive login disabled.
8. Prepare a decision list per reviewer: Keep / Revoke / Modify / Exception, with reason; exceptions need compensating control and expiry.
9. Track remediation: tickets for revocations, target dates, verification that access was actually removed.
10. Summarize for auditors: population, completeness check (export totals vs system totals), findings by type, decisions, time to remediate.
11. Label every finding based on inference (e.g. a role assumed to be toxic without a documented SoD rule) as `[ASSUMPTION]`; suggest `audit-preparation` or `control-mapping` when the review is evidence for an audit.

## Output format
```markdown
# Access Review: <system> – <period>
## Scope and Population
- Accounts reviewed: <n> (human <n>, service <n>, shared <n>) · Source export date: ...
- Completeness check: <export count vs system count>
## Findings
| # | Account (pseudonymized) | Entitlement | Finding type | Evidence | Proposed decision | Reviewer |
## SoD Conflicts
| Account | Conflicting entitlements | Rule | Decision / compensating control |
## Exceptions
| Account | Reason | Compensating control | Approver | Expires |
## Remediation Tracking
| Ticket | Action | Due | Verified |
## Summary for Audit
## Gaps and Open Questions
```

## Quality checklist
- [ ] Population completeness is verified, not assumed.
- [ ] Every finding type (orphaned, dormant, excessive, SoD, shared/service) was checked or marked as not possible.
- [ ] Reviewers are not approving their own access.
- [ ] Exceptions have an approver and expiry.
- [ ] Personal data is minimized and accounts are pseudonymized in shared outputs.
- [ ] Revocations include a verification step.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Rubber-stamping: managers approve everything in bulk. Present only the risky rows for decision and require a reason for Keep on privileged access.
- Ignoring service and shared accounts because they have no manager. Assign an owner for each.
- Closing the review when decisions are made instead of when access is actually removed.

## Example
Input: "ERP export with 412 accounts and roles, HR active list with 380 people."

Excerpt of output:
| 7 | U-0193 | AP_Clerk + Vendor_Master_Maintain | SoD conflict | Can create a vendor and post invoices to it | Revoke Vendor_Master_Maintain | Finance manager |
| 12 | U-0241 | Any | Orphaned | No match in HR list; last login 140 days ago | Revoke | System owner |
