---
description: Assesses an application portfolio on business fit and technical fit and assigns each application a TIME disposition (Tolerate, Invest, Migrate, Eliminate) with rationale, cost and risk signals and a sequenced rationalization plan. Use when rationalizing applications, preparing a budget cycle, planning cloud or ERP programs, or after a merger leaves overlapping systems.
related: capability-map, modernization-assessment, tech-debt-assessment, build-vs-buy, target-state-architecture
prompt: Here is our list of 40 applications with owners, costs and user counts; classify them with TIME and propose what to retire first.
---

# Assess the Application Portfolio

## Purpose
Give leadership an evidence-based disposition for every application so that spend moves from duplicated or failing systems to those that differentiate the business.

## When to use
- Budget planning or cost reduction targets application run cost.
- A merger, divestiture or ERP/cloud program leaves overlapping applications.
- Security or end-of-support exposure must be quantified across the estate.
- A capability map shows duplication and needs an application-level decision.

## When not to use
- One legacy system needs a detailed modernization path. Use `modernization-assessment`.
- The question is a single replacement decision. Use `build-vs-buy`.
- Code-level debt within one system. Use `tech-debt-assessment`.

## Inputs
Required:
- Application inventory: name, purpose, owner, supported capability or process.
- Some measure of business value or usage (users, transactions, criticality).

Optional:
- Annual run cost (licenses, infrastructure, support), incident counts, change frequency.
- Technology stack, vendor support dates, security findings.
- Capability map and strategic priorities.

If the inventory is missing, ask for it. Do not invent costs or dates; mark them `[UNKNOWN]` and lower confidence.

## Process
1. Normalize the inventory: one row per deployable application; merge aliases; flag shadow IT and SaaS explicitly.
2. Define scoring criteria with weights before scoring. Business fit: capability coverage, user satisfaction, strategic alignment, regulatory need. Technical fit: supportability (end-of-life dates), architecture quality, security posture, operability, skills availability.
3. Score each application 1-5 per criterion; record evidence and a confidence level (High/Medium/Low).
4. Plot on the TIME quadrant: high business/high technical = Invest; high business/low technical = Migrate; low business/high technical = Tolerate; low/low = Eliminate.
5. Overlay cost and risk: high cost with low value, end-of-support within 18 months, critical vulnerabilities, single-person knowledge.
6. Group by capability to expose duplicates; for each duplicate cluster pick a survivor with rationale.
7. Check dependencies and data ownership before any Eliminate or Migrate: interfaces, reports, archives and retention obligations.
8. Sequence the plan into waves: quick wins (low dependency eliminations), risk-driven migrations, strategic investments.
9. Estimate impact qualitatively or with given figures only; never invent savings.
10. List decisions needed from owners and the data gaps that lowered confidence.
11. Separate facts from owner-provided data from your inferences, labeling each inferred score `[ASSUMPTION]`; if the goal continues, suggest `modernization-assessment` for Migrate candidates, `build-vs-buy` for replacements or `target-state-architecture`.

## Output format
```markdown
# Application Portfolio Assessment – <scope>
Criteria and weights: <table> · Data as of: <date>

## Portfolio Summary
| Disposition | Count | Share of known run cost |

## Application Assessments
| App | Capability | Owner | Business fit | Technical fit | TIME | Key risk | Confidence | Rationale |
|---|---|---|---|---|---|---|---|---|

## Duplicate Clusters
| Capability | Applications | Proposed survivor | Why |

## Rationalization Roadmap
| Wave | Applications | Action | Dependencies | Owner |

## Data Gaps and Decisions Needed
```

## Quality checklist
- [ ] Criteria and weights were fixed before scoring.
- [ ] Every score has evidence or a confidence marker.
- [ ] Every Eliminate/Migrate checks dependencies, data retention and archive needs.
- [ ] Duplicate clusters have a named survivor and rationale.
- [ ] No costs, savings or dates are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Letting the loudest owner rescore their system. Use evidence and a fixed rubric.
- Forgetting data. Eliminating an app without an archive or retention plan creates compliance risk.
- Treating TIME as the plan. It is a disposition; the roadmap needs dependencies and waves.

## Example
Input: "HR has two leave systems and an old payroll tool on an unsupported database."

Excerpt of output:
| App | Business fit | Technical fit | TIME | Key risk | Rationale |
|---|---|---|---|---|---|
| LeaveTrack | 2 | 2 | Eliminate | Duplicate | Covered by HR suite leave module `[confirm feature parity]` |
| PayrollLegacy | 5 | 1 | Migrate | DB end of support `[UNKNOWN date]` | Critical process on unsupported stack |
