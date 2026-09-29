---
description: Assesses a client's current state across business process, applications, data, technology, organization and delivery practices, producing evidence-backed findings, a maturity rating per dimension with a stated scale, root-cause-linked pain points, and prioritized recommendations with quick wins and a high-level roadmap. Use when a client asks "where do we stand", before a transformation or modernization proposal, or when discovery outputs, interviews and documents must be consolidated into an assessment report.
related: discovery-workshop, fit-gap-analysis, modernization-assessment, capability-map, client-steering-report
prompt: Assess the current state of a mid-size insurer's claims platform from these interview notes and system inventory, and recommend where to start.
---

# Assess a Client's Current State

## Purpose
Give the client an objective, evidence-based picture of where they stand, why the pain exists and what to do first, so investment decisions rest on diagnosed causes rather than symptoms or vendor preference.

## When to use
- A client requests an assessment or health check of an area (platform, process, data, delivery).
- A transformation, modernization or proposal needs a documented baseline.
- Discovery workshops, interviews and documents must be consolidated into findings and recommendations.

## When not to use
- Early engagement where goals are not yet understood. Use `discovery-workshop`.
- A specific package must be compared to requirements. Use `fit-gap-analysis`.
- The focus is purely the technical modernization of one application. Use `modernization-assessment`.

## Inputs
Required:
- Assessment scope (area, units, systems) and the client's question or objective.
- Evidence: interview notes, workshop outputs, documents, system inventory, metrics.

Optional, improves quality:
- A maturity model the client already uses; industry regulations.
- Target state ambitions or strategy.
- Budget, timeline and organizational constraints for recommendations.

If scope or evidence is missing, ask. Do not rate a dimension without evidence; mark it `[INSUFFICIENT EVIDENCE]`.

## Process
1. Confirm the assessment question and scope, and choose dimensions (e.g. business process, applications, data, technology and infrastructure, security and compliance, organization and skills, delivery and operations). Drop dimensions outside scope explicitly.
2. Define the maturity scale up front (e.g. 1 Initial, 2 Repeatable, 3 Defined, 4 Managed, 5 Optimized) with observable criteria per level, or use the client's model. State that ratings are relative to this scale.
3. Inventory the evidence and tag each item by source type (interview, document, metric, observation) and role, minimizing personal data. Note gaps in coverage (e.g. no operations interviews).
4. Extract findings: each is a factual statement with its evidence reference. Distinguish observed facts, stakeholder opinions (attributed by role) and your inferences (`[ASSUMPTION]`).
5. Group findings into pain points and trace each to a root cause (use five whys or cause categories); several pain points often share one cause.
6. Rate each dimension with the evidence that justifies the level and a confidence level (H/M/L). Include strengths, not only weaknesses.
7. Assess business impact per pain point qualitatively (cost, risk, revenue, customer, compliance); use figures only if provided.
8. Formulate recommendations addressing root causes, each with expected outcome, rough effort (S/M/L), dependencies and owner type. Mark quick wins (low effort, visible value) separately from structural changes.
9. Sequence recommendations into a high-level roadmap (now / next / later) respecting dependencies and client capacity.
10. Write an executive summary: overall picture, top 3-5 findings, top recommendations, and the decision requested.
11. If the goal continues, suggest `fit-gap-analysis` for package options, `modernization-assessment` for technical depth, or `proposal-writing` to scope the follow-on work.

## Output format
```markdown
# Current State Assessment: <client> — <scope>
## Executive Summary
## Scope, Approach and Evidence
- Dimensions: ...  - Sources: <n interviews by role, documents, metrics>  - Coverage gaps: ...
## Maturity Scale
| Level | Criteria |
## Maturity by Dimension
| Dimension | Level | Confidence | Key evidence |
## Strengths
## Findings
| ID | Finding | Type (fact / opinion / inference) | Evidence ref |
## Pain Points and Root Causes
| Pain point | Impact | Root cause | Findings |
## Recommendations
| ID | Recommendation | Addresses | Outcome | Effort | Dependencies | Quick win? |
## Roadmap
| Now | Next | Later |
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every finding cites evidence; opinions and inferences are labeled as such.
- [ ] Each maturity rating uses the stated scale, cites evidence and has a confidence level.
- [ ] Pain points are traced to root causes, and recommendations address causes, not symptoms.
- [ ] Strengths are reported alongside weaknesses.
- [ ] No figures, benchmarks or costs are invented.
- [ ] Recommendations are sequenced with dependencies and quick wins marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Recommendations that point to your own offering regardless of findings. Evidence must lead; note options neutrally.
- Rating maturity from one loud interview. Triangulate across roles and documents, and lower confidence when you cannot.
- A long list of equal-weight findings. Prioritize by impact and cluster by root cause.

## Example
Input: "Insurer claims platform: 8 interviews, system inventory; adjusters complain about re-keying, IT says integrations are fragile."

Excerpt of output:
| Pain point | Impact | Root cause | Findings |
|---|---|---|---|
| Adjusters re-key claim data into 3 systems | Handling time, error risk | Point-to-point integrations without a shared claim data model | F3 (adjuster interviews), F7 (inventory: 14 file transfers) |

- Data dimension: Level 2 (Repeatable), confidence M — no data owner named; quality checks manual (F9).
- Quick win: automate the nightly file reconciliation report `[ASSUMPTION: feasible with existing tools]`.
