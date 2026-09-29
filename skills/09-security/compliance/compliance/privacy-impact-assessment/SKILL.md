---
name: privacy-impact-assessment
description: "Runs a KVKK/GDPR data protection impact assessment (DPIA) for a feature or system: maps processing activities, legal bases, data flows and transfers, rates risks to data subjects and proposes privacy-by-design measures. Use when a new feature or system processes personal or special category data, introduces profiling, monitoring, new recipients or cross-border transfers, or when legal or the DPO asks for a DPIA."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: compliance
  area: compliance
  title: "Run a privacy impact assessment"
  related: "data-classification, threat-model, retention-policy, security-requirements, it-risk-assessment"
  prompt: "Run a privacy impact assessment for our new customer loyalty app that tracks store visits by location and sends personalized offers."
---

# Run a Privacy Impact Assessment

## Purpose
Show, before go-live, what personal data a feature or system processes, on what legal basis, with which risks to the people concerned, and which measures bring those risks to an acceptable level, so the organization can decide and demonstrate accountability under KVKK (Law No. 6698) and GDPR.

## When to use
- A new feature or system processes personal data, especially special category data (health, biometrics, religion, criminal records) or data about children or employees.
- Processing involves profiling, systematic monitoring, location tracking, large-scale combination of datasets or automated decisions with significant effect.
- Data is shared with a new processor or third party, or transferred abroad.
- An existing processing activity changes purpose, scope or technology.

## When not to use
- You need to classify data assets without assessing a processing activity. Use `data-classification`.
- You need security threats to a system rather than risks to data subjects. Use `threat-model`.
- You need retention periods and deletion rules only. Use `retention-policy`.

## Inputs
Required:
- A description of the feature or system: purpose, data collected, users, data subjects, where data goes.

Optional, improves quality:
- Record of processing activities (VERBIS entry for KVKK, Article 30 record for GDPR).
- Architecture or data flow diagram, list of processors and sub-processors, hosting locations.
- Existing privacy notices, consent texts, retention policy, security controls.
- Whether the organization acts as controller, joint controller or processor.

If the feature description is missing, ask for it. Ask one focused question at a time for anything that blocks the legal basis analysis; everything else becomes an open question. Use placeholders instead of real personal data in examples and minimize any sample data the user shares.

## Process
1. Screen the need: list which high-risk indicators apply (special category data, large scale, profiling, monitoring, vulnerable subjects, new technology, cross-border transfer, automated decisions). If none apply, state that a full DPIA may not be required and record the screening result.
2. Describe the processing: purpose(s), data subject categories, data categories, sources, recipients, systems, retention, controller/processor roles.
3. Map the data flow from collection to deletion, including backups, logs, analytics and support tools. Mark every transfer outside Türkiye or the EEA.
4. Determine the legal basis per purpose: KVKK Art. 5 (general) or Art. 6 (special category); GDPR Art. 6 and Art. 9. Explicit consent is a fallback, not a default; flag purposes that rely on consent but are bundled with a service.
5. Check necessity and proportionality: data minimization, purpose limitation, accuracy, storage limitation. Challenge each field: what breaks if it is not collected?
6. Check data subject rights and transparency: privacy notice (aydınlatma metni) content, consent capture and withdrawal, access, rectification, erasure, objection, and the response path within statutory deadlines.
7. Check transfers: for KVKK, the Art. 9 mechanism used (adequacy, standard contract, binding corporate rules, or occasional transfer exceptions); for GDPR, adequacy or SCCs plus transfer impact assessment.
8. Identify risks to data subjects (not only to the company): unauthorized access, re-identification, function creep, discrimination, loss of control, chilling effect. Rate likelihood and severity (High/Medium/Low) with justification.
9. Propose measures per risk: technical (pseudonymization, encryption, access control, aggregation, deletion jobs) and organizational (DPA with processors, training, approval workflow). Rate residual risk.
10. Decide: proceed, proceed with conditions, or consult the supervisory authority (GDPR Art. 36 if high residual risk remains). Record the DPO/legal opinion as `[TBD]` if not given.
11. Label every inference about data flows, roles or legal basis as `[ASSUMPTION]`; then suggest `retention-policy` for deletion rules, `security-requirements` for technical measures or `threat-model` for the system view.

## Output format
```markdown
# Privacy Impact Assessment: <feature/system> (<date>, v<n>)
## Screening
| Indicator | Applies? | Note |
## Processing Description
| Purpose | Data subjects | Data categories | Source | Recipients | Retention | Legal basis (KVKK / GDPR) |
## Data Flow and Transfers
- Collection -> ... -> deletion; transfers abroad: <country, mechanism>
## Necessity and Proportionality
- <field> – needed for <purpose> / remove / aggregate
## Data Subject Rights and Transparency
- Privacy notice: ... / Consent: ... / Rights handling: ...
## Risks to Data Subjects
| ID | Risk | Likelihood | Severity | Measures | Residual risk | Owner |
## Decision
- Outcome: proceed / proceed with conditions / consult authority
- DPO / legal opinion: [TBD]
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every purpose has its own legal basis under both KVKK and GDPR where both apply.
- [ ] Special category data is identified and handled under KVKK Art. 6 / GDPR Art. 9.
- [ ] Each data field has a stated necessity; unnecessary fields are flagged for removal.
- [ ] Transfers abroad name the mechanism or are marked `[UNKNOWN]`.
- [ ] Risks are framed from the data subject's perspective and each High risk has a measure.
- [ ] No legal conclusion is presented as final without DPO/legal review noted.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using consent as the legal basis for everything. Where the service cannot work without the data, consent is not freely given; look for contract or legitimate interest first.
- Forgetting secondary copies: logs, analytics events, support ticket attachments, backups and test environments.
- Treating cloud hosting in another country as "not a transfer". Remote access or storage abroad is a transfer under both regimes.
- Assessing only security risks to the company. A DPIA is about rights and freedoms of people.

## Example
Input: "Loyalty app tracks store visits via location and sends personalized offers."

Excerpt of output:
| R2 | Continuous location tracking reveals routines and home address (profiling beyond purpose) | M | H | Geofence only store areas, no background tracking outside geofences, store visit events not raw coordinates, 12-month retention [ASSUMPTION] | Low | Mobile lead |
- Legal basis for personalized offers: explicit consent (KVKK Art. 5/1, GDPR Art. 6(1)(a)), separate from loyalty membership terms; withdrawal must be possible in-app.
