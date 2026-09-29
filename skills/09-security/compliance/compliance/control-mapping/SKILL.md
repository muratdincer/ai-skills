---
description: "Maps an organization's existing controls, processes and evidence to a target standard such as ISO/IEC 27001 Annex A or SOC 2 Trust Services Criteria, and shows coverage, evidence gaps and overlaps with other frameworks. Use when preparing for certification, answering a customer security questionnaire, merging frameworks (ISO 27001, SOC 2, KVKK, PCI DSS) or checking whether a control actually produces audit evidence."
related: "audit-preparation, policy-writing, it-risk-assessment, access-review, traceability-matrix"
prompt: "Map our current controls to ISO 27001:2022 Annex A and show which ones have no evidence."
---

# Map Controls to a Standard

## Purpose
Produce a traceable control-to-requirement matrix that shows, for each requirement of a target standard, which internal control satisfies it, what evidence proves it operates, who owns it, and where the gaps are, so certification or audit work is planned on facts rather than assumptions.

## When to use
- Preparing for ISO/IEC 27001 certification or a SOC 2 Type I/II examination.
- A customer or regulator sends a security questionnaire and answers must trace to real controls.
- Several frameworks apply (ISO 27001, SOC 2, KVKK technical and organizational measures, PCI DSS, BDDK) and the team wants one control set mapped to all.
- After a reorganization or tool change, to see which controls lost their owner or evidence.

## When not to use
- The audit date is set and you need the evidence plan and timeline. Use `audit-preparation`.
- The control itself does not exist yet and must be written. Use `policy-writing`.
- You need to decide which risks justify which controls. Use `it-risk-assessment`.

## Inputs
Required:
- The target standard and version (e.g. ISO/IEC 27001:2022 Annex A, SOC 2 TSC 2017 with revised points of focus).
- A description of existing controls, policies or procedures (list, policy set, previous audit report or free text).

Optional, improves quality:
- Scope of the ISMS or system boundary for SOC 2.
- Statement of Applicability, risk register, previous audit findings.
- Other frameworks to cross-map.

If the standard or the control description is missing, ask for it. Do not reproduce paid standard text verbatim; refer to requirement IDs and short paraphrases.

## Process
1. Confirm the target standard, version and scope boundary (entities, locations, systems, services). Note out-of-scope areas explicitly.
2. Normalize the existing controls into a control list: ID, short statement, type (preventive/detective/corrective), nature (manual/automated), frequency, owner.
3. List the requirements of the target standard by ID with a short paraphrase. For ISO 27001 include clauses 4-10 as well as Annex A; for SOC 2 include the common criteria and any selected additional categories.
4. Map each requirement to one or more controls. Rate coverage: Full, Partial, None, or Not applicable (with justification, which feeds the Statement of Applicability for ISO 27001).
5. For each mapping, name the evidence that proves design and operating effectiveness: artifact, system of record, sample period, who produces it. "We do this" without an artifact is a gap.
6. Flag evidence quality issues: screenshots without dates, manual logs, evidence generated on request only, controls without an owner.
7. If other frameworks are in scope, add columns to reuse the same control and evidence (test once, satisfy many). Do not assume equivalence where requirements differ in strength; mark partial overlaps.
8. Summarize gaps by requirement with a proposed remediation (new control, strengthened control, new evidence source), owner and priority based on audit risk.
9. Label every coverage rating that rests on a description rather than seen evidence as `[ASSUMPTION]`, and list open questions per control owner.
10. Hand off: `audit-preparation` to plan evidence collection, `policy-writing` for missing policies, `it-risk-assessment` to justify exclusions.

## Output format
```markdown
# Control Mapping: <standard, version> – <scope> (<date>)
## Scope
- In scope: ... / Out of scope: ...
## Control Inventory
| Control ID | Statement | Type | Manual/Auto | Frequency | Owner |
## Mapping Matrix
| Requirement ID | Paraphrase | Control ID(s) | Coverage | Evidence (artifact, system, period) | Other frameworks | Notes |
## Gaps and Remediation
| Requirement ID | Gap | Proposed action | Owner | Priority |
## Not Applicable Justifications
- <requirement ID> – reason
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every requirement of the chosen standard version appears once, with a coverage rating.
- [ ] Every Full or Partial rating names concrete evidence, not an intention.
- [ ] Not-applicable items have a justification tied to scope or risk.
- [ ] Every control has an owner or is marked `[UNKNOWN]`.
- [ ] No paid standard text is copied verbatim.
- [ ] Cross-framework overlaps are marked partial where strength differs.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mapping policies instead of controls. A policy statement is not evidence that the control operates; map the procedure and its records.
- Mixing ISO 27001:2013 and 2022 control numbers. Confirm the version and use its numbering consistently.
- Rating Full because a tool exists. Tools need configuration evidence and review records to count.
- Forgetting the management system clauses (risk treatment, internal audit, management review) and mapping only Annex A.

## Example
Input: "We use MFA on VPN, quarterly access reviews in a spreadsheet, and weekly backups. Map to ISO 27001:2022."

Excerpt of output:
| A.5.18 | Access rights provisioned, reviewed, removed | AC-03 quarterly access review | Partial | Review spreadsheet per quarter [ASSUMPTION: sign-off not evidenced] | SOC 2 CC6.2 (partial) | No evidence that revocations were executed |
| A.8.13 | Information backup | OPS-02 weekly backup | Partial | Backup job logs | – | No restore test evidence |
