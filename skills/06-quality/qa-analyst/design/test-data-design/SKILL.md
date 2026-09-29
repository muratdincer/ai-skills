---
description: "Designs test datasets that are realistic, privacy-safe and cover partitions, boundaries, states and referential edge cases, with a provisioning and reset approach per environment. Use when tests need specific data, when production data is being considered for testing, when data setup is blocking execution or automation, or when someone asks what data a feature needs to be tested."
related: equivalence-boundary-analysis, test-case-writing, data-classification, environment-strategy, privacy-impact-assessment
prompt: "Design the test data for our loan application flow: applicants with different income bands, co-applicants, existing customers and blacklisted IDs, for SIT and UAT."
---

# Design Test Data

## Purpose
Produce a dataset specification that lets every planned test run with known, reproducible data, covers the risky combinations, and never exposes real personal data.

## When to use
- Test cases reference "a valid customer" or "an account with debt" and nobody knows which record to use.
- The team plans to copy production data into a test environment.
- Automated tests fail because shared data is consumed or changed by other runs.
- A new feature introduces entities, states or rules that existing datasets do not cover.

## When not to use
- You still need to decide which input values to test. Use `equivalence-boundary-analysis` first.
- You need a classification of data sensitivity for the whole platform. Use `data-classification`.
- You need an environment landscape and data refresh policy. Use `environment-strategy`.

## Inputs
Required:
- The feature, test cases or scenarios that need data, or the data model/entities involved.

Optional, improves quality:
- Field rules, reference data, state models, integration dependencies.
- Target environments, refresh frequency, existing datasets or generators.
- Data protection constraints (KVKK/GDPR, contractual, internal policy).

If neither the tests nor the entities are known, ask for them. Unknown field rules become `[UNKNOWN]` and open questions.

## Process
1. List the entities, attributes and relationships the tests touch, including reference and configuration data.
2. For each attribute used in a decision, list its partitions and boundaries; reuse existing analysis if given.
3. Add state coverage: every lifecycle state an entity must be in for a test (e.g. draft, active, suspended, closed).
4. Add relational edge cases: orphan records, many children, zero children, circular or duplicate references, cross-system ID mismatches.
5. Add content edge cases: max length, Unicode and Turkish characters (İ/ı, ş, ğ), whitespace, leading zeros, time zones and DST, leap days, currency precision.
6. Classify each field by sensitivity and pick a source per dataset: synthetic generation, masked/pseudonymized copy, or subset of reference data. Default to synthetic; justify any masked production copy and its masking rules.
7. Define ownership and isolation: which data is shared read-only, which is created per test and cleaned up, and how parallel runs avoid collisions (unique prefixes, tenant per run).
8. Define provisioning and reset: seed scripts, API setup, snapshots, refresh cadence per environment, and who runs them.
9. Map each dataset back to the tests that use it, so unused data and uncovered tests are visible.
10. Mark every inferred rule or volume `[ASSUMPTION]` and list open questions.
11. If the user continues, suggest `test-case-writing` to reference the named datasets or `privacy-impact-assessment` when real personal data is still on the table.

## Output format
```markdown
# Test Data Design: <feature / system>
## Entities and Rules in Scope
| Entity | Attribute | Partitions / boundaries | Source rule |
|---|---|---|---|

## Datasets
| ID | Purpose | Key values / state | Sensitivity | Source (synthetic/masked/reference) | Used by tests |
|---|---|---|---|---|---|

## Edge-Case Records
- <record>: <why it exists>

## Isolation and Lifecycle
- Shared read-only: ...
- Created per test / cleanup: ...
- Parallel-run strategy: ...

## Provisioning per Environment
| Environment | Method | Refresh cadence | Owner |
|---|---|---|---|

## Privacy Controls
- Masking / generation rules: ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every test in scope maps to at least one dataset, and every dataset is used.
- [ ] Partitions, boundaries, states and relational edge cases are all represented.
- [ ] No real personal data; any masked copy states its masking rules and legal basis.
- [ ] Parallel and repeated runs cannot corrupt each other's data.
- [ ] Provisioning and reset are repeatable and have an owner or `[TBD]`.
- [ ] Inferred rules and volumes are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Just take a production copy." Masking rarely covers free-text, attachments and logs; prefer synthetic data and treat masked copies as an exception with review.
- Golden records shared by everyone. One test changes the status and ten others fail; create data per test or reset before each run.
- Only happy-path data. Defects cluster in unusual states and relations, so design those deliberately.
- Dates hard-coded to a calendar day. Use relative dates ("today - 91 days") so data does not expire.

## Example
Input: "Loan application: income bands, co-applicants, existing customers, blacklisted IDs; SIT and UAT."

Excerpt of output:
| ID | Purpose | Key values / state | Sensitivity | Source | Used by tests |
|---|---|---|---|---|---|
| LD-03 | Income exactly at band limit | Monthly income = band upper limit `[UNKNOWN: limit value]` | Personal (synthetic) | Generator | TC-011, TC-012 |
| LD-07 | Blacklisted co-applicant, clean main applicant | Co-applicant ID on test blacklist | Personal (synthetic) | Seed script | TC-020 |
| LD-09 | Existing customer with closed account only | Customer status Active, account Closed | Personal (synthetic) | API setup | TC-025 |

- Parallel-run strategy: each automated run creates applicants with prefix `RUN<id>-`; nightly cleanup deletes prefixed records.
