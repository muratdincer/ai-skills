---
description: "Specifies non-functional requirements as measurable statements across quality characteristics (performance, availability, reliability, security, privacy, usability, accessibility, maintainability, compatibility, portability, operability, compliance), each with metric, target, measurement condition, verification method and source. Use when quality expectations are vague ('fast', 'secure', '24/7'), when NFRs are missing from a BRD or FRD, or when asked to 'define NFRs'."
related: "frd-writing, nfr-to-architecture, slo-definition, security-requirements, performance-test-plan"
prompt: "Define the NFRs for our new customer self-service portal; the business only said it must be fast, secure and always available."
---

# Specify Non-Functional Requirements

## Purpose
Turn quality expectations into measurable, verifiable requirements with owners and sources, so architecture, testing and operations can design for and prove them instead of arguing over adjectives.

## When to use
- Stakeholders state qualities in adjectives: fast, scalable, secure, always on, easy to use.
- A BRD or FRD is being completed and quality attributes are missing or untestable.
- A vendor contract, SLA or architecture decision needs quality targets.

## When not to use
- Targets must be turned into architecture tactics. Use `nfr-to-architecture`.
- Service level objectives and error budgets for a running service are needed. Use `slo-definition`.
- A detailed security control set is needed. Use `security-requirements`.

## Inputs
Required:
- The system or feature in scope and the quality expectations stated so far (even vague ones).

Optional, improves quality:
- Expected users and load, business hours and critical periods, regulations (KVKK/GDPR, sector rules), existing SLAs, current system measurements, organization NFR baseline.

If the scope is missing, ask for it. For missing targets, do not invent numbers: propose a candidate range as `[ASSUMPTION]` with the question that fixes it.

## Process
1. Collect every quality statement from the input and quote it; note who said it and why it matters to them.
2. Map each to a quality characteristic using ISO/IEC 25010 as the checklist: performance efficiency, reliability/availability, security, usability/accessibility, maintainability, compatibility, portability; add privacy, operability/observability and compliance.
3. Walk the checklist for characteristics nobody mentioned and add them as `[TBD]` requirements or explicit N/A with reason.
4. Rewrite each statement as a measurable requirement: metric, target, measurement condition (load, percentile, period, location, data volume), and scope (which function or interface).
5. Prefer percentiles and ranges over averages ("p95 ≤ 2 s at 500 concurrent users"), and state the peak scenario explicitly.
6. For availability and recovery, state service hours, allowed downtime, RTO and RPO separately; do not equate "24/7" with 100%.
7. For security and privacy, reference the applicable standard (OWASP ASVS level, KVKK/GDPR data minimization, retention) and personal data categories involved.
8. For usability and accessibility, set a verifiable target (WCAG 2.2 AA, task success rate, supported devices and languages).
9. Assign each NFR a verification method (load test, penetration test, audit, accessibility audit, monitoring), an owner and a priority; flag conflicts (e.g. strict retention vs. analytics needs) as trade-offs.
10. Label every candidate target without a source `[ASSUMPTION]` and list the question and owner that confirms it.
11. If the goal continues, suggest `nfr-to-architecture` for design tactics, `slo-definition` for operational targets, or `performance-test-plan` to verify.

## Output format
```markdown
# Non-Functional Requirements: <system / feature>
Scope: <functions, interfaces> · Sources: <documents, stakeholders>

| ID | Characteristic | Requirement | Metric and target | Condition | Verification | Priority | Source |
|---|---|---|---|---|---|---|---|
| NFR-PERF-01 | Performance | ... | p95 ≤ ... | ... | Load test | Must | ... |

## Not Applicable (with reason)
## Trade-offs and Conflicts
## Assumptions and Open Questions
- [ASSUMPTION] <candidate target> — confirm with <owner>
```

## Quality checklist
- [ ] Every NFR has a metric, a target and a measurement condition; no adjectives remain.
- [ ] All ISO/IEC 25010 characteristics plus privacy, operability and compliance are covered or marked N/A with reason.
- [ ] Availability states service hours, downtime, RTO and RPO separately.
- [ ] Every NFR has a verification method and an owner.
- [ ] No target is presented as agreed without a source; candidates are `[ASSUMPTION]`.
- [ ] Personal data categories and minimization/retention needs are identified where relevant.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Copying generic targets ("99.99%", "1 second") without the load, percentile or cost behind them. Tie every number to a scenario and a source.
- Averages instead of percentiles. An average of 1 s can hide a 10 s tail that users feel.
- Writing NFRs no one can test before go-live. Add the verification method now, or the requirement will silently be dropped.

## Example
Input: "The portal must be fast, secure and always available."

Weak: "The system shall be fast and highly available."

Strong:
| ID | Requirement | Metric and target | Condition | Verification |
|---|---|---|---|---|
| NFR-PERF-01 | Invoice list page responds quickly | p95 ≤ 2 s `[ASSUMPTION]` | 500 concurrent users, month-end peak `[TBD: confirm peak]` | Load test |
| NFR-AVL-01 | Portal is available during service hours | ≥ 99.5% monthly `[ASSUMPTION]`, RTO 4 h, RPO 15 min `[TBD]` | 24/7 excluding announced maintenance | Monitoring |
| NFR-SEC-01 | Authentication and session controls | OWASP ASVS Level 2 | All external endpoints | Penetration test |

Open question: What is the business cost of one hour of portal downtime at month end? — Customer service director
