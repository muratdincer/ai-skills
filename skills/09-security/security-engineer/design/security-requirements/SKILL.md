---
name: security-requirements
description: "Defines testable security requirements for a system or feature, aligned to OWASP ASVS levels and chapters, with rationale, verification method and priority. Use when a new application or feature needs security acceptance criteria, when a threat model must be turned into backlog items, or when a customer or regulator asks for a security requirements baseline."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: security-engineer
  area: design
  title: "Define security requirements"
  related: "threat-model, nfr-specification, authn-authz-design, secure-code-review, acceptance-criteria"
  prompt: "Define security requirements for our new customer self-service portal; it handles personal data and payments are done via a hosted payment page."
---

# Define Security Requirements

## Purpose
Produce a concise, testable set of security requirements that developers can build against and testers can verify, anchored to OWASP ASVS so coverage and level are explicit.

## When to use
- A new application, API or significant feature enters design or refinement.
- A threat model has produced mitigations that must become requirements.
- A tender, customer contract or auditor asks for a documented security baseline.

## When not to use
- You still need to discover what threats exist. Use `threat-model` first.
- You need general quality attributes (performance, availability). Use `nfr-specification`.
- You are reviewing existing code against requirements. Use `secure-code-review`.

## Inputs
Required:
- A description of the system or feature: users, interfaces, data handled and how it is deployed.

Optional, improves quality:
- Target ASVS level (L1, L2, L3) or the risk profile to derive it.
- Threat model output, existing security standards or policies.
- Regulatory scope (KVKK/GDPR, PCI DSS, sector rules), identity provider, tech stack.

If the system description is missing, ask for it. If the ASVS level is not given, propose one with justification and mark it `[ASSUMPTION]`.

## Process
1. Summarize the system context: exposure (internet/internal), user types, data classes, integrations.
2. Choose the ASVS level: L1 for low-risk, L2 as default for applications handling personal or business-critical data, L3 for high-value transactions or safety-critical systems. State the reason.
3. Select relevant ASVS chapters (e.g. authentication, session management, access control, validation and encoding, cryptography, error handling and logging, data protection, API, configuration). Drop chapters that do not apply and say why.
4. Write each requirement as one testable "shall" statement tailored to the context; cite the ASVS chapter/requirement reference instead of copying its text.
5. Add context-specific requirements from the threat model and regulation: data minimization, retention, masking in logs, consent, data subject request handling for KVKK/GDPR.
6. For each requirement define verification: automated test, SAST/DAST/SCA rule, code review, configuration check, pentest.
7. Prioritize with MoSCoW or Must/Should/Could and tie Must items to release gates.
8. Mark conflicts and trade-offs (e.g. session timeout vs usability) and who decides.
9. List open questions and assumptions.
10. Suggest the next skill: `acceptance-criteria` to make each requirement testable in work items, `threat-model` if threats have not yet been modeled, `secure-code-review` for verification.

## Output format
```markdown
# Security Requirements: <system/feature>
Target level: OWASP ASVS <version> L<n> – <justification>
## Context
- Exposure, users, data classes, integrations
## Requirements
| ID | Requirement (shall) | ASVS ref | Source (ASVS / threat / regulation) | Priority | Verification | Owner |
|---|---|---|---|---|---|---|
| SEC-01 | ... | V<chapter>.<section> | ... | Must | Automated test | ... |
## Excluded Chapters
- <chapter> – reason
## Trade-offs and Decisions Needed
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every requirement is a single, testable statement with a verification method.
- [ ] The ASVS level and version are stated and justified.
- [ ] Personal data requirements cover minimization, masking in logs and retention.
- [ ] No ASVS text is quoted verbatim; references point to the section.
- [ ] Must requirements are linked to a release gate.
- [ ] Nothing about existing controls is invented; unknowns are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing "the system shall be secure" style requirements. Each item must describe observable behavior.
- Copying the whole ASVS into the backlog. Tailor to context and drop what does not apply, with a reason.
- Forgetting non-functional security needs such as logging, monitoring and secret rotation.

## Example
Input: "Customer self-service portal, internet facing, stores names, phone numbers and addresses; payments via hosted payment page."

Excerpt of output:
- Target level: ASVS L2 – internet-facing, personal data, no card data stored.
| SEC-04 | The portal shall invalidate the server-side session on logout and after 15 minutes of inactivity [ASSUMPTION: timeout to be confirmed] | V3 | ASVS | Must | Automated test |
| SEC-11 | Application logs shall not contain phone numbers or addresses in clear text | V7 | KVKK | Must | Log review + test |
