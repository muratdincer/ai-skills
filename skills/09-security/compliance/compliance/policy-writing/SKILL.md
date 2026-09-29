---
name: policy-writing
description: "Writes or revises a security or IT policy with purpose, scope, enforceable rules, roles, exceptions, compliance measurement and review cycle, and separates policy from standards and procedures. Use when a policy is missing, outdated, flagged in an audit, or needed for ISO 27001, SOC 2, KVKK or internal governance (e.g. acceptable use, access control, password, backup, remote work, AI usage)."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: compliance
  area: compliance
  title: "Write a security/IT policy"
  related: "control-mapping, audit-preparation, it-risk-assessment, retention-policy, document-review"
  prompt: "Write an access control policy for our company; we are preparing for ISO 27001 and use Entra ID and GitHub."
---

# Write a Security/IT Policy

## Purpose
Produce a short, enforceable policy that states what must be true, who is accountable and how compliance is measured, so employees can follow it, auditors can test it and exceptions are handled consistently.

## When to use
- A required policy does not exist (audit finding, certification gap, customer requirement).
- An existing policy is outdated after a technology, organization or regulatory change.
- Rules exist only as tribal knowledge or scattered wiki pages and need a governing document.
- A new risk area needs a position quickly (e.g. generative AI usage, bring-your-own-device).

## When not to use
- You need to check which controls map to a standard. Use `control-mapping`.
- You need data retention periods per data category. Use `retention-policy`.
- You need step-by-step operational instructions. Use `runbook`.

## Inputs
Required:
- The policy topic and the organization context (size, sector, main systems or regulation in scope).

Optional, improves quality:
- Existing policy, audit findings or control requirements to satisfy (ISO/IEC 27001 Annex A control IDs, SOC 2 criteria, KVKK technical and organizational measures).
- Policy template, document numbering, approval body (e.g. information security committee).
- Known exceptions or constraints.

If the topic or context is missing, ask for it (at most 5 short questions in one batch). Everything else becomes `[TBD]` or an open question.

## Process
1. Define the policy's objective in one or two sentences, tied to a risk or requirement it addresses.
2. Set scope: people (employees, contractors, third parties), assets, locations, systems; state what is excluded.
3. Separate levels: the policy states mandatory principles ("must/must not"); technical values that change often (password length, tool names, retention days) go to a referenced standard or procedure.
4. Write rules as testable statements with "must", "must not" or "should", one requirement per sentence. Each rule should be auditable: an auditor can find evidence of compliance or non-compliance.
5. Define roles and responsibilities: policy owner, approvers, implementers, all users. Use a short RACI if more than three roles.
6. Define the exception process: who can request, who approves, maximum duration, compensating controls, register of exceptions.
7. Define compliance and enforcement: how compliance is measured (reviews, logs, metrics), consequences of violation in line with HR procedures, reporting channel.
8. Add references: related policies, standards, procedures and the requirements satisfied (ISO 27001 control IDs, KVKK, SOC 2), without quoting paid standards.
9. Add document control: version, owner, approval date, review cycle (typically annual or on significant change), change history.
10. Review for readability: plain language, no rationale essays inside rules, target 2-4 pages; move background to an appendix.
11. Mark every rule based on assumed organization context as `[ASSUMPTION]`; suggest `control-mapping` to link rules to controls or `audit-preparation` if an audit is near.

## Output format
```markdown
# <Policy Name>
| Document ID | [TBD] | Version | 1.0 | Owner | <role> | Approved by | <body> [TBD] | Approval date | [TBD] | Next review | [TBD] |

## 1. Purpose
## 2. Scope
- Applies to: ... / Excluded: ...
## 3. Policy Statements
3.1 <rule with must / must not>
3.2 ...
## 4. Roles and Responsibilities
| Role | Responsibility |
## 5. Exceptions
## 6. Compliance and Enforcement
## 7. Related Documents and Requirements
- ISO/IEC 27001:2022 A.x.y, KVKK ..., <internal standard>
## 8. Definitions
## 9. Change History
| Version | Date | Change | Author |
```

## Quality checklist
- [ ] Every rule is a single, testable "must/must not/should" statement.
- [ ] Frequently changing technical values are referenced to a standard, not hard-coded.
- [ ] Scope, owner, exception process and review cycle are present.
- [ ] Roles are assigned to positions, not named individuals.
- [ ] Requirements satisfied are referenced by ID without verbatim quotes.
- [ ] Organization-specific facts not given are marked `[TBD]` or `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing aspirational statements ("security is everyone's responsibility") that no one can audit. Convert them to concrete obligations or delete them.
- Embedding procedures in the policy, forcing a re-approval each time a tool changes. Keep the policy stable; put the how in procedures.
- No exception path, so people silently bypass the policy. Provide a lightweight, time-limited exception process.
- Copying another company's policy with controls the organization does not operate, creating audit nonconformities.

## Example
Input: "Access control policy, 300 employees, Entra ID and GitHub, ISO 27001 prep."

Weak rule: "Access should be given appropriately and reviewed regularly."
Strong rules:
- 3.2 Access to production systems must be granted only through an approved request that names a business justification and an approver other than the requester.
- 3.5 Privileged access must use MFA and named accounts; shared administrator accounts must not be used. (ISO/IEC 27001:2022 A.8.2, A.8.5)
- 3.7 Access rights must be reviewed at least quarterly for privileged roles and semi-annually for others [ASSUMPTION], per the Access Review Procedure.
