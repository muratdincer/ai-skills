---
name: srs-writing
description: "Writes a Software Requirements Specification aligned with ISO/IEC/IEEE 29148: purpose and scope, system context and interfaces, functional requirements, quality attributes, data, constraints and verification method per requirement, each uniquely identified and traceable. Use when a system or subsystem must be specified for design, build, a vendor or an audit, or when business requirements must be turned into a verifiable system-level specification."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: system-analyst
  area: specification
  title: "Write a Software Requirements Specification"
  related: "frd-writing, nfr-specification, use-case-spec, integration-requirements, traceability-matrix"
  prompt: "Write an SRS for the payment reconciliation service based on this FRD and the interface list."
---

# Write a Software Requirements Specification

## Purpose
Produce a system-level specification that designers, developers, testers and vendors can build and verify against without re-interpreting business documents. Every requirement is singular, verifiable, uniquely identified and traced to its source.

## When to use
- Business or functional requirements exist and must be restated as system requirements for one system or subsystem.
- Work is outsourced, regulated or audited and needs a formal, versioned specification.
- Several teams or suppliers build parts of one system and need a shared contract.

## When not to use
- The need is still business-level (what the business must achieve). Use `brd-writing` or `frd-writing`.
- Only quality attributes are missing. Use `nfr-specification`.
- Only one interface or API must be specified. Use `integration-requirements` or `api-contract`.

## Inputs
Required:
- The source requirements (BRD, FRD, stories, use cases) or a description of the system's responsibilities.
- The system boundary: which system is being specified.

Optional, improves quality:
- Context diagram, interface list, data model, existing architecture decisions.
- Regulations and internal standards, organization SRS template.
- Target users, environments and operating constraints.

If the source material or the system boundary is missing, ask for it. Everything else becomes `[TBD]` or an open issue in the document.

## Process
1. Fix the system boundary: name the system, list external actors and neighbouring systems, and state what is explicitly outside. Describe the context as a list or diagram-as-code.
2. Set conventions: requirement ID scheme (e.g. SRS-FR-###, SRS-NFR-###, SRS-IF-###), priority scale, and the words "shall" (binding), "should" (desired), "may" (optional).
3. Derive functional requirements from each source item. Write one behaviour per requirement as "The system shall ..." with trigger, input, processing rule and observable output. Split any statement with "and/or".
4. Specify external interfaces: user interfaces (roles, key screens, accessibility to WCAG 2.2 where users are people), system interfaces (partner, direction, protocol, message, frequency, error handling), and hardware or communication constraints.
5. Specify data requirements: key entities, attributes that carry rules, retention, archival, and personal data classification with masking or minimization needs under KVKK/GDPR.
6. Specify quality attributes with measurable fit criteria: performance, availability, recoverability, security, auditability, operability, scalability. No adjectives without a number or condition; missing numbers become `[TBD]` with an owner.
7. List design and implementation constraints (mandated platforms, standards, regulations) separately from requirements, and record assumptions and dependencies; label inferred ones `[ASSUMPTION]`.
8. Assign a verification method to every requirement: Test, Demonstration, Inspection or Analysis.
9. Trace each requirement back to its source ID and flag source items with no system requirement (coverage gaps) and system requirements with no source (gold plating or missing source).
10. Check each requirement against ISO/IEC/IEEE 29148 characteristics: necessary, unambiguous, complete, singular, feasible, verifiable, correct, conforming.
11. If the user wants to continue, suggest `traceability-matrix` to maintain links, `nfr-specification` to deepen quality attributes or `requirements-review-checklist` before sign-off.

## Output format
```markdown
# Software Requirements Specification: <system>
Version: <x.y> · Status: <Draft / Review / Baselined> · Owner: <name or [TBD]>

## 1. Introduction
Purpose · Scope (in / out) · Definitions (link glossary) · References · Conventions (ID scheme, shall/should/may)

## 2. Overall Description
System context (actors, neighbouring systems) · User classes · Operating environment · Constraints · Assumptions and dependencies

## 3. Functional Requirements
| ID | Requirement ("The system shall ...") | Source | Priority | Verification |
|---|---|---|---|---|

## 4. External Interface Requirements
### 4.1 User interfaces  ### 4.2 System interfaces  ### 4.3 Communication interfaces
| ID | Interface | Direction | Protocol / format | Frequency | Error handling |

## 5. Data Requirements
| Entity | Key rules | Retention | Personal data (Y/N, class) |

## 6. Quality Attributes
| ID | Attribute | Fit criterion | Verification |

## 7. Traceability and Coverage
Unmapped source items · Requirements without source

## 8. Open Issues
| # | Issue | Owner | Needed by |
```

## Quality checklist
- [ ] Every requirement has a unique ID, a source, a priority and a verification method.
- [ ] Each requirement states one behaviour and is observable at the system boundary.
- [ ] No quality attribute uses an adjective without a measurable fit criterion or `[TBD]`.
- [ ] Constraints and assumptions are separated from requirements and inferred items are labeled.
- [ ] Coverage gaps in both directions are listed, not silently filled.
- [ ] Personal data is classified and masking or minimization is stated where it appears.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Copying business requirements verbatim. "Users can reconcile payments" is not a system requirement; state the trigger, rule and output.
- Writing design as requirements ("store in table X"). Keep solution choices in design documents unless they are genuine constraints.
- Leaving interfaces as a name only. Direction, format, frequency and failure behaviour are what integration teams need.

## Example
Input: "FR-12: Finance wants unmatched bank transactions to be visible daily."

Weak: "The system shall show unmatched transactions quickly."

Strong:
| ID | Requirement | Source | Priority | Verification |
|---|---|---|---|---|
| SRS-FR-031 | The system shall, after each bank statement import completes, mark every transaction without a matching ledger entry as "Unmatched". | FR-12 | Must | Test |
| SRS-FR-032 | The system shall list Unmatched transactions to users in the Reconciler role, filterable by value date and account. | FR-12 | Must | Demonstration |
| SRS-NFR-007 | The Unmatched list shall load within `[TBD]` seconds for `[TBD]` transactions. | FR-12 | Should | Test |
