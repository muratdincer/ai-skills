---
name: threat-model
description: "Builds a threat model for a system or feature by decomposing it into a data flow diagram, applying STRIDE per element and trust boundary, rating each threat and proposing mitigations with owners. Use when designing a new system, adding an integration, changing trust boundaries or data flows, or when someone asks what could go wrong security-wise."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: security-engineer
  area: design
  title: "Build a threat model"
  related: "security-requirements, authn-authz-design, solution-architecture-document, pentest-scope, it-risk-assessment"
  prompt: "Build a threat model for our new mobile banking API: mobile app, API gateway, .NET backend, PostgreSQL and a third-party KYC provider."
---

# Build a Threat Model

## Purpose
Identify credible threats to a system early, before they become vulnerabilities, and turn each one into a concrete mitigation, a test or an explicit risk decision.

## When to use
- A new system, service or major feature is being designed.
- A trust boundary changes: new external integration, new user type, move to cloud, new admin interface.
- Sensitive or personal data starts flowing through a component for the first time.
- An existing threat model is older than the architecture it describes.

## When not to use
- You need a list of testable security controls for a backlog. Use `security-requirements`.
- You are assessing organization-wide risk across assets, not one system. Use `it-risk-assessment`.
- An attack is already in progress. Use `security-incident-response`.

## Inputs
Required:
- A description of the system: components, data stores, external actors and data flows (text, diagram or architecture doc).

Optional, improves quality:
- Data classification (personal, special category, payment, secrets).
- Deployment topology, network zones, identity provider.
- Existing security controls and known past incidents.
- Compliance scope (KVKK/GDPR, PCI DSS, BDDK, ISO 27001).

If the system description is missing, ask for it. Everything else becomes an assumption or open question.

## Process
1. Restate the scope: what is in the model, what is explicitly out (e.g. corporate network, CI/CD) and the version of the architecture used.
2. Build a data flow diagram in text: external entities, processes, data stores, data flows. Number every element (E1, P1, D1, F1).
3. Draw trust boundaries: internet/DMZ, service mesh, tenant boundary, third-party boundary, admin plane. Flows crossing a boundary get the most attention.
4. List assets and their security objectives (confidentiality, integrity, availability, privacy) with the data classification.
5. Apply STRIDE per element: processes get all six; data stores get T, R, I, D; data flows get T, I, D; external entities get S, R.
6. For each threat write a concrete attack scenario (actor, entry point, technique), not a category name. Reference CWE or MITRE ATT&CK where it helps.
7. Record existing controls, then rate residual risk with likelihood x impact (High/Medium/Low) and a one-line justification. Use the team's own scale if one exists.
8. Propose mitigations per threat: preventive, detective, responsive. Prefer design changes over compensating controls.
9. Turn each mitigation into a traceable item: security requirement, backlog item, test case or accepted risk with an accountable owner.
10. List assumptions, out-of-scope areas and open questions; state when the model must be revisited.
11. Suggest the next skill: `security-requirements` to turn mitigations into controls, `pentest-scope` to validate the highest risks, `it-risk-assessment` for accepted risks at organization level.

## Output format
```markdown
# Threat Model: <system> (v<architecture version>, <date>)
## Scope and Assumptions
- In scope: ... / Out of scope: ...
- [ASSUMPTION] ...
## Data Flow Diagram (text)
| ID | Element | Type | Trust zone | Data (classification) |
## Trust Boundaries
- TB1: <from> -> <to>: flows F1, F3
## Threats
| ID | Element | STRIDE | Scenario | Existing controls | Likelihood | Impact | Risk | Mitigation | Owner | Tracking |
## Accepted Risks
- <threat ID> – rationale – approver – review date
## Open Questions
1. ...
## Revisit Triggers
- New external integration, auth change, new data category
```

## Quality checklist
- [ ] Every flow that crosses a trust boundary has at least one threat analyzed.
- [ ] Scenarios are specific enough to write a test from.
- [ ] Every High risk has a mitigation or an explicitly accepted risk with an approver.
- [ ] Personal data flows are marked and privacy threats (linkability, over-collection) are considered.
- [ ] No control is claimed that the input does not support; unknowns are marked `[UNKNOWN]`.
- [ ] Mitigations are traceable to requirements, backlog items or tests.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing generic threats ("SQL injection") without tying them to an element and entry point. Anchor each threat to a DFD element.
- Ignoring the admin, support and CI/CD paths. Privileged planes are often the weakest boundary.
- Treating the model as a one-off document. Define revisit triggers and link it to the architecture version.
- Rating everything High. Justify likelihood with exposure and attacker effort.

## Example
Input: "Mobile app calls API gateway, which calls a .NET service; the service stores customers in PostgreSQL and calls an external KYC provider."

Excerpt of output:
| T4 | F3 service -> KYC | Information disclosure | Attacker on a misconfigured egress proxy reads national ID numbers sent to KYC | TLS 1.2 [ASSUMPTION] | M | H | High | Enforce TLS 1.3 with certificate pinning to the provider, send only the minimum fields, log without IDs | Backend lead | SEC-REQ-07 |
