---
name: security-finding-report
description: "Writes a clear, reproducible security finding with title, affected asset, severity and scoring, description, impact, reproduction steps, evidence, remediation and references, suitable for a pentest report, bug bounty response or internal tracker. Use when a confirmed or suspected security issue must be documented for developers, management or auditors."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: security-engineer
  area: assessment
  title: "Write a security finding"
  related: "vulnerability-triage, secure-code-review, pentest-scope, bug-report, security-incident-response"
  prompt: "Write a security finding for this: any logged-in user can download another user's invoice PDF by changing the invoice number in the URL."
---

# Write a Security Finding

## Purpose
Document a security issue so that a developer can reproduce and fix it, a manager can judge its risk, and an auditor can verify its closure, without leaking sensitive data.

## When to use
- A pentest, code review, bug bounty or internal test uncovers a security issue.
- A scanner finding has been validated and needs a tracker entry.
- A finding must be communicated to a vendor or customer.

## When not to use
- The priority of a raw report is still undecided. Use `vulnerability-triage`.
- The issue is being actively exploited. Use `security-incident-response`.
- It is a functional defect without security impact. Use `bug-report`.

## Inputs
Required:
- What was observed: the behavior, where (asset, endpoint, component) and how it was triggered.

Optional, improves quality:
- Request/response samples, screenshots, tool output.
- Environment and version, tester role and account type.
- Severity scheme used by the organization (CVSS v3.1/v4.0, internal matrix).

If the observation or location is missing, ask. If reproduction was not confirmed, label the finding "Unconfirmed".

## Process
1. Write a specific title: weakness + location + consequence (e.g. "IDOR in invoice download exposes other customers' invoices").
2. Record the affected asset, environment, version, and the date of discovery.
3. Classify: OWASP Top 10 / API Top 10 category and CWE ID.
4. Score severity with the organization's scheme; if CVSS, give the full vector and justify each metric that is not obvious. Do not guess a vector for unconfirmed facts.
5. Describe the weakness in 2-4 sentences: what is wrong and why it happens.
6. Describe impact in business terms: which data or actions, which users, scale, regulatory relevance (personal data under KVKK/GDPR, possible breach notification duties).
7. Write numbered reproduction steps with preconditions, accounts (by role, not real credentials), requests and expected versus actual results.
8. Attach evidence with sensitive values masked: tokens, passwords, personal data, internal hostnames when shared externally.
9. Give remediation: the root-cause fix, short-term mitigation, and how to verify the fix (retest steps).
10. Add references (CWE, OWASP cheat sheets, vendor advisory) and status fields (owner, due date per SLA, retest result).
11. Label anything inferred beyond the observed evidence as `[ASSUMPTION]`, then suggest `vulnerability-triage` for prioritization or `security-incident-response` if there are signs of active exploitation.

## Output format
```markdown
# <ID>: <specific title>
| Field | Value |
|---|---|
| Asset / component | ... |
| Environment / version | ... |
| Discovered | <date> by <role> |
| Category | OWASP <cat> · CWE-<id> |
| Severity | <rating> (<CVSS vector or scheme>) |
| Status | Open / Unconfirmed / Fixed / Accepted |
| Owner / due | ... |
## Description
## Impact
## Steps to Reproduce
1. ...
Expected: ... Actual: ...
## Evidence (masked)
## Remediation
- Fix: ... · Mitigation: ... · Verification: ...
## References
```

## Quality checklist
- [ ] Another engineer can reproduce the issue from the steps alone.
- [ ] Severity is justified and consistent with the described impact.
- [ ] Secrets and personal data in evidence are masked.
- [ ] Remediation addresses the root cause, not only the tested payload.
- [ ] Verification steps for retest are included.
- [ ] Nothing beyond the observation is claimed; unknowns are marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Vague titles like "Security issue in API". The title should tell the reader the weakness and the stake.
- Overstating impact ("full database compromise") without evidence. Describe what was demonstrated and what is plausible, separately.
- Fixing the symptom: blocking one parameter value instead of adding an authorization check.

## Example
Input: "Changing the invoice number in /invoices/{no}/pdf lets any logged-in user download others' invoices."

Excerpt of output:
# SEC-2026-014: IDOR in invoice PDF download exposes other customers' invoices
| Category | OWASP A01:2021 Broken Access Control · CWE-639 |
Impact: Invoices contain names, addresses and purchase history; sequential numbers allow bulk harvesting. This is a personal data exposure under KVKK/GDPR; involve the privacy officer to assess notification duties.
Fix: verify invoice ownership against the authenticated customer ID on the server; use non-sequential identifiers as defense in depth.
