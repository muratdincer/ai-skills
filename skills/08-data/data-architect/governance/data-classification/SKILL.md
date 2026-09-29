---
description: "Classifies datasets and fields by sensitivity and privacy category: confidentiality level, personal data, special-category data under KVKK Article 6 and GDPR Articles 9-10, direct vs. indirect identifiers, and derives handling controls such as masking, encryption, access and retention. Use when onboarding data to a platform, preparing a DPIA or access model, or when asked to tag PII or sensitive columns."
related: "privacy-impact-assessment, retention-policy, data-catalog-entry, access-review, secrets-management-plan"
prompt: "Classify the columns of our customer and loan application tables for KVKK and propose masking rules."
---

# Classify Data Sensitivity

## Purpose
Assign every field and dataset a defensible sensitivity and privacy classification, and translate it into concrete handling controls, so that access, masking, retention and breach response are driven by the data rather than by guesswork.

## When to use
- New sources or datasets are onboarded to a shared platform or analytics environment.
- An access model, masking policy, DPIA or data sharing agreement is being prepared.
- An audit or regulator asks where personal or special-category data resides.

## When not to use
- A full privacy risk assessment of a processing activity is needed. Use `privacy-impact-assessment`.
- Only retention periods are being defined. Use `retention-policy`.
- Secrets and credentials handling. Use `secrets-management-plan`.

## Inputs
Required:
- Field list with names and, ideally, descriptions or sample value patterns (never real personal values).

Optional:
- The organization's classification scheme (levels and definitions), data subjects involved, processing purposes, jurisdictions, existing controls.

If no scheme is given, use a four-level default (Public, Internal, Confidential, Restricted) and mark it `[ASSUMPTION]`. If only real data samples are available, ask for masked samples instead.

## Process
1. Confirm the scheme: confidentiality levels with definitions, and the privacy categories to tag (personal, special category, criminal data, children's data, financial/payment, authentication).
2. For each field decide whether it relates to an identified or identifiable natural person, directly or in combination.
3. Tag identifier role: direct identifier (name, national ID, email, phone), quasi-identifier (birth date, postcode, gender, job title), sensitive attribute, or non-personal.
4. Tag special categories per KVKK Article 6 (e.g. health, biometric, genetic, religion, political opinion, union membership, criminal convictions, appearance/dress) and GDPR Articles 9-10. Note that free-text fields often contain them.
5. Assess combination and inference risk: quasi-identifiers that together re-identify; derived fields that reveal sensitive attributes (e.g. pharmacy purchases implying health).
6. Assign the confidentiality level per field; the dataset inherits the highest field level unless fields are separated.
7. Derive controls per level/category: encryption at rest and in transit, column masking or tokenization, pseudonymization for analytics, row-level restrictions, logging of access, export restrictions, retention and deletion.
8. Identify data minimization opportunities: fields not needed for the stated purpose, precision reduction (birth year instead of date), aggregation.
9. Flag cross-border transfer and third-party exposure where known.
10. Record uncertain classifications for the data owner/DPO to confirm.

## Output format
```markdown
# Data Classification: <dataset/system>
Scheme: <levels> | Jurisdictions: <KVKK/GDPR/...> | Reviewed by: <[TBD]>

## Field Classification
| Field | Personal? | Identifier role | Special category | Level | Controls | Minimization note |
|---|---|---|---|---|---|---|

## Combination / Inference Risks
- <fields> together allow <risk> → <control>

## Dataset-Level Result
Level: <...> | Contains special category: <yes/no> | Recommended split: <...>

## Handling Controls by Level
| Level | Storage | Access | Masking | Sharing | Retention |
|---|---|---|---|---|---|

## Items to Confirm (owner/DPO)
1. ...
```

## Quality checklist
- [ ] Every field has a level and a personal/non-personal decision.
- [ ] Special categories are checked explicitly, including free-text fields.
- [ ] Quasi-identifier combinations are assessed.
- [ ] Each level maps to concrete controls, not just labels.
- [ ] No real personal values appear in the output.
- [ ] Uncertain items are routed to the owner/DPO.

## Common pitfalls
- Treating only direct identifiers as personal data. Quasi-identifiers and pseudonymized data remain personal data.
- Ignoring free-text, notes and attachment fields, where special-category data often hides.
- Labelling without controls. A classification that does not change access or masking has no effect.

## Example
Input: "loan_application: applicant_name, tckn, birth_date, city, monthly_income, health_declaration_text, score."

Excerpt of output:
- tckn: direct identifier, Restricted; tokenize in analytics, reveal only in underwriting role.
- health_declaration_text: special category (health, KVKK Art. 6), Restricted; exclude from analytics layer.
- birth_date + city: quasi-identifiers; publish birth year only in analytical marts.
