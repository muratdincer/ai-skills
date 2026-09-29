---
description: "Assesses IT and information security risk for a scope of assets or services: identifies assets, threats and vulnerabilities, rates likelihood and impact with existing controls, decides treatment (mitigate, transfer, avoid, accept) and produces a risk register entry per risk. Use when building or refreshing an ISO 27001 risk assessment, evaluating a new vendor, system or change, preparing a risk acceptance, or when management asks how risky something is."
related: "threat-model, risk-register, control-mapping, vulnerability-triage, privacy-impact-assessment"
prompt: "Assess IT risk for moving our on-prem ERP to a hosted cloud provider, including vendor and data risks."
---

# Assess IT Risk

## Purpose
Give decision makers a transparent, repeatable view of which information risks matter most, why, and what treatment is proposed, so resources go to the largest risks and residual risk is accepted consciously by an accountable owner.

## When to use
- Building or refreshing the risk assessment of an ISMS (ISO/IEC 27001 clause 6.1.2, method aligned with ISO/IEC 27005).
- Evaluating a new system, vendor, outsourcing or major change before approval.
- A vulnerability or control gap cannot be fixed on time and needs a formal risk acceptance.
- Management or an auditor asks for the rationale behind security priorities.

## When not to use
- You need design-level threats per component of one system. Use `threat-model`.
- The risk is a project delivery risk (schedule, budget, scope). Use `risk-register`.
- The subject is a single vulnerability's severity and fix timeline. Use `vulnerability-triage`.

## Inputs
Required:
- The scope: assets, services, processes or the change being assessed.

Optional, improves quality:
- The organization's risk methodology (scales, risk appetite, acceptance authority).
- Asset inventory with owners and classification, existing controls, incident history, audit findings.
- Business impact information (critical processes, RTO/RPO, regulatory obligations such as KVKK or BDDK).

If the scope is missing, ask for it. If no methodology exists, propose a 5x5 or 3x3 likelihood-impact scale and mark it `[ASSUMPTION]`.

## Process
1. Confirm scope and context: business objectives, internal and external factors, legal obligations, risk appetite and who can accept which risk level.
2. Define or adopt the rating scales: likelihood (with frequency or exposure anchors) and impact across confidentiality, integrity, availability, financial, regulatory, reputational and data subject harm. Write the anchors down so ratings are reproducible.
3. Identify assets in scope (information, applications, infrastructure, people, suppliers) with owner and classification.
4. For each asset or asset group, identify credible threat-vulnerability pairs. Use scenarios ("ransomware via unpatched VPN appliance encrypts ERP database") rather than single words.
5. Record existing controls and judge their effectiveness based on evidence; do not credit controls that are planned or undocumented.
6. Rate inherent (optional) and current risk: likelihood x impact with a one-line justification per rating.
7. Compare with risk appetite. For risks above appetite, choose treatment: mitigate (controls with owner and date), transfer (insurance, contract), avoid (stop the activity) or accept (owner, rationale, expiry, review date).
8. Rate target residual risk after treatment and link treatments to controls (ISO 27001 Annex A IDs if relevant) and to the Statement of Applicability.
9. Identify personal data risks and flag where a privacy impact assessment is also required.
10. Produce the register, a heat map summary and the top risks for management, with decisions required.
11. Label every rating based on assumed facts as `[ASSUMPTION]`, then suggest `threat-model` for deep dives, `control-mapping` to align treatments with a standard or `privacy-impact-assessment` for data subject risks.

## Output format
```markdown
# IT Risk Assessment: <scope> (<date>, method: <name / [ASSUMPTION]>)
## Context and Criteria
- Risk appetite: ... / Acceptance authority: ... / Scales: likelihood 1-5, impact 1-5 with anchors
## Asset Inventory (in scope)
| Asset | Owner | Classification |
## Risk Register
| ID | Asset | Threat scenario | Vulnerability | Existing controls | L | I | Current risk | Treatment | Action / control | Owner | Due | Target residual |
## Heat Map Summary
- High: R3, R7 / Medium: ... / Low: ...
## Decisions Required
- R3: accept / fund mitigation – decision owner
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Rating scales have written anchors and are applied consistently.
- [ ] Every risk is a specific scenario tied to an asset, threat and vulnerability.
- [ ] Existing controls are credited only with evidence; planned controls are not counted.
- [ ] Every risk above appetite has a treatment with owner and date, or an acceptance with authority and expiry.
- [ ] Personal data risks are flagged for a privacy impact assessment where needed.
- [ ] Monetary figures and probabilities are not invented; unknowns are marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Rating threats in isolation ("hackers: High"). Always rate the scenario against a specific asset and vulnerability.
- Accepting risks indefinitely. Every acceptance needs an expiry and a review trigger.
- Letting the loudest stakeholder set the ratings. Use the written anchors and record the justification.
- Confusing inherent and residual risk in reporting, making control investment invisible.

## Example
Input: "Move on-prem ERP to a hosted cloud provider."

Excerpt of output:
| R4 | ERP data | Provider admin misuse or breach exposes customer and payroll data | Shared responsibility unclear, no customer-managed keys | Provider ISO 27001 certificate [ASSUMPTION: SoA not reviewed] | 3 | 5 | High | Mitigate | Contract clause for breach notification within agreed hours, customer-managed encryption keys, review provider SOC 2 report | CIO | [TBD] | Medium |
| R6 | ERP data | Transfer of employee personal data abroad without a valid KVKK Art. 9 mechanism | Hosting region not fixed | None | 4 | 4 | High | Mitigate | Fix region or put transfer mechanism in place; run privacy impact assessment | DPO | [TBD] | Low |
