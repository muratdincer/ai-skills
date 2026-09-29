---
name: master-data-strategy
description: "Defines a master data management approach for one or more domains (customer, product, supplier, location, etc.): system of record per attribute, golden record and survivorship rules, match/merge logic, implementation style, stewardship roles and workflows, and data distribution to consuming systems. Use when the same entity exists inconsistently across systems, duplicates harm operations or reporting, or a master data or golden record initiative is being scoped."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: data-architect
  area: governance
  title: "Define master data management"
  related: "data-quality-rules, logical-data-model, data-lineage-doc, raci-matrix, data-classification"
  prompt: "Define a master data approach for customer data that exists in our CRM, ERP and e-commerce platform."
---

# Define Master Data Management

## Purpose
Establish one trusted, governed version of key business entities and the rules and roles that keep it trusted, so operations and analytics stop reconciling conflicting copies.

## When to use
- The same customer, product or supplier appears with different identifiers and attributes across systems.
- Duplicates or conflicting attributes cause operational errors (wrong shipments, double invoicing) or unreliable reporting.
- A golden record, MDM hub or data governance program is being scoped.

## When not to use
- Only checks on one dataset are needed. Use `data-quality-rules`.
- Only the structure of the entity is being designed. Use `logical-data-model`.
- Only the flow of the data between systems must be documented. Use `data-lineage-doc`.

## Inputs
Required:
- The master data domain(s) and the systems that create or hold that data.

Optional:
- Attribute lists per system, known duplicate rates, business processes that create/change records, pain points, regulatory requirements, organizational structure for ownership.

If the systems holding the domain are unknown, ask; survivorship cannot be defined without them.

## Process
1. Scope the domain: entity definition, what is master data vs. transactional or reference data, and in-scope attributes (start with those that drive processes and reporting).
2. Inventory sources: for each system, which attributes it creates, updates or only reads, its local identifier and its known quality.
3. Assign system of record per attribute (or attribute group), not per entity; different systems can legitimately own different attributes.
4. Choose an implementation style and justify it: registry (index of cross-references), consolidation (golden record for analytics), coexistence (golden record synced back), centralized (create in the hub only). State the trade-off in intrusiveness vs. control.
5. Define matching: blocking keys, match attributes with normalization (case, whitespace, transliteration, address standardization, phone formats), deterministic rules first, probabilistic scoring with auto-merge, review and no-match thresholds `[TBD, calibrate on a sample]`.
6. Define survivorship per attribute: source priority, most recent, most complete, most frequent or stewarded value; plus rules for unmerge and for preserving source cross-references.
7. Define identifiers: global master ID, cross-reference table, and how consumers resolve local IDs.
8. Define stewardship: data owner (accountable), data stewards (operational), their workflows for match review, exception queues, create/change requests, and service levels for resolving them.
9. Define distribution: how the golden record reaches consumers (events, APIs, batch), latency needs, and how conflicting local edits are handled.
10. Define quality and success metrics: duplicate rate, match precision/recall on a labeled sample, completeness of critical attributes, stewardship backlog age; baseline values are `[UNKNOWN]` until measured.
11. Address privacy: personal data in the domain, consent and legal basis, deletion requests propagated to all copies, minimized attributes.
12. Propose a phased roadmap (one domain and few sources first), with risks and open questions. If the goal continues, suggest `data-quality-rules` for critical attributes, `raci-matrix` for stewardship roles or `logical-data-model` for the golden record structure.

## Output format
```markdown
# Master Data Strategy: <domain>
Style: <registry/consolidation/coexistence/centralized> — <rationale>

## Scope and Definition
<entity definition, in-scope attributes, exclusions>

## System of Record Matrix
| Attribute group | Created in | Updated in | System of record | Survivorship rule |
|---|---|---|---|---|

## Matching
Blocking: <...> | Normalization: <...> | Rules: <deterministic, probabilistic> | Thresholds: auto <...> / review <...>

## Identifiers and Distribution
<master ID, cross-reference, delivery mechanism, latency>

## Stewardship
| Role | Who | Responsibilities | Service level |
|---|---|---|---|

## Metrics
| Metric | Baseline | Target |
|---|---|---|

## Privacy
- ...

## Roadmap, Risks and Open Questions
- Phase 1: ...
- [RISK] ... | [TBD] ...
```

## Quality checklist
- [ ] System of record is defined per attribute group, not only per entity.
- [ ] The implementation style is justified against the organization's constraints.
- [ ] Match thresholds are calibrated or marked `[TBD]`; unmerge is possible.
- [ ] Every stewardship workflow has an owner and a service level.
- [ ] Deletion and consent propagate to all copies of personal data.
- [ ] Baselines and targets are not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating MDM as a tool purchase. Without stewardship roles and time, the golden record decays.
- Big-bang scope across all domains and sources. Prove value on one domain with the most painful duplicates.
- Aggressive auto-merge. False merges (two real people into one) are far costlier than missed matches; start conservative and review.

## Example
Input: "Customer data lives in CRM, ERP and e-commerce; duplicate customers cause double invoices."

Excerpt of output:
- Style: coexistence — ERP must keep creating customers for invoicing; golden record synced back via events.
- Survivorship: billing address from ERP (system of record); email and marketing consent from e-commerce, most recent wins.
- Matching: block on normalized postcode + last name; auto-merge only on exact tax ID match; fuzzy name/address scores go to steward review.
