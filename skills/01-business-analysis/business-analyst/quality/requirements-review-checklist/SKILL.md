---
name: requirements-review-checklist
description: "Runs a structured, checklist-driven review of a requirements document or story set before sign-off, covering structure, individual requirement quality (ISO/IEC/IEEE 29148 characteristics), set-level completeness and consistency, NFRs, traceability and approval readiness, and returns findings with a go/no-go recommendation. Use when a BRD, FRD, SRS or backlog slice is about to be baselined, handed to a vendor or approved."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "Run a requirements review"
  related: "ambiguity-detection, requirements-gap-analysis, requirements-consistency-check, requirements-sign-off, document-review"
  prompt: "Review this FRD before we send it to the business for sign-off. Use a proper checklist and tell me if it is ready."
---

# Run a Requirements Review

## Purpose
Give an approver confidence that a requirements package is fit to baseline. The review applies a consistent checklist, records findings by severity and ends with a clear readiness verdict and the fixes needed to reach it.

## When to use
- A BRD, FRD, SRS or story set is about to be signed off or baselined.
- Requirements are handed to a vendor, another team or for a fixed-price estimate.
- A peer review or quality gate requires documented evidence of review.

## When not to use
- You only need wording clarity. Use `ambiguity-detection`.
- You need the sign-off package itself. Use `requirements-sign-off`.
- The document is not a requirements document (e.g. design, policy). Use `document-review`.

## Inputs
Required:
- The requirements document or story set.

Optional, improves quality:
- The intake document or business goals.
- Organization template or mandatory sections.
- Review depth wanted (quick scan vs full review) and the target audience of the document.

If the review depth is not given, do a full review and state that.

## Process
1. Structure check: required sections present (purpose, scope, stakeholders, glossary, assumptions/constraints, functional, NFR, data, interfaces, transition, open issues), version and change history, owner.
2. Individual requirement check, per ISO/IEC/IEEE 29148 characteristics: necessary, appropriate (right abstraction, no design), unambiguous, complete, singular, feasible, verifiable, correct, conforming. Sample every requirement if fewer than ~50; otherwise all high-priority plus a stated sample.
3. Set-level check: complete against goals, consistent (no conflicts/duplicates), feasible within constraints, comprehensible to its audience, bounded (scope and out-of-scope explicit).
4. NFR check: performance, availability, security, privacy (KVKK/GDPR where personal data), accessibility (WCAG 2.2 for UI), auditability, operability; each measurable.
5. Data and interface check: key entities, validation rules, retention, interface partners, error handling.
6. Traceability check: every requirement has an ID, priority and source; goals map to requirements.
7. Readiness check: open issues have owners and dates; assumptions are listed; approvers are named.
8. Record findings with location, checklist item, severity (Critical / Major / Minor / Editorial) and a suggested fix.
9. Decide: Ready / Ready with conditions (list conditions) / Not ready. Critical findings always mean Not ready.
10. If the user wants to continue, suggest `requirements-sign-off` when the verdict is Ready, or `requirements-gap-analysis` / `ambiguity-detection` to work off the findings.

## Output format
```markdown
# Requirements Review: <document> v<version>
Reviewer: <name/role or AI-assisted> · Date: <date> · Depth: <full / sample: which>

## Verdict
<Ready / Ready with conditions / Not ready> – <one-line reason>
Conditions: <list if any>

## Checklist Results
| Area | Item | Result (Pass / Fail / N/A) | Note |
|---|---|---|---|

## Findings
| # | Location | Checklist item | Severity | Finding | Suggested fix |
|---|---|---|---|---|---|

## Statistics
Critical n · Major n · Minor n · Editorial n
```

## Quality checklist
- [ ] Every checklist area was assessed or explicitly marked N/A with a reason.
- [ ] The sampling approach is stated if not every requirement was read.
- [ ] Findings cite exact locations and are actionable.
- [ ] The verdict follows from the severity rules, not from overall impression.
- [ ] Editorial issues are not mixed with substantive ones.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reviewing only the language and missing that whole areas (NFR, migration, reporting) are absent.
- Drowning critical findings in dozens of editorial comments. Group editorial items and keep them last.
- Issuing "Ready" with open Critical items because the deadline is close. Use "Ready with conditions" only for non-critical items.

## Example
Input: FRD v0.9 for a claims portal, 64 requirements, no NFR section.

Excerpt of output:
Verdict: Not ready – no NFR section; 3 requirements unverifiable.
| # | Location | Checklist item | Severity | Finding | Suggested fix |
|---|---|---|---|---|---|
| F1 | Whole doc | NFR present | Critical | No performance, availability or security requirements | Add NFR section; see `nfr-specification` |
| F2 | FR-17 | Verifiable | Major | "Claims are processed quickly" | Define target time `[TBD]` and measurement point |
