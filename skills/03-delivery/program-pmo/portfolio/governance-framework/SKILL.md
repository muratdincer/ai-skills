---
description: Defines project or program governance sized to its risk: decision rights by decision type, governance forums with membership and mandate, stage or decision gates with entry criteria, tolerances and escalation paths, and the reporting cadence that feeds each forum. Use when a new project or program is being set up, when decisions stall or are taken in the wrong place, when an audit or sponsor asks "who decides what", or when existing governance is too heavy or too light.
related: raci-matrix, steering-committee-pack, project-charter, change-control, communication-plan
prompt: Define governance for a 14-month ERP replacement program with an external integrator, three business units and an IT steering committee that already exists.
---

# Define Project Governance

## Purpose
Establish who decides what, where, when and on what information, with tolerances that let the delivery team act without asking and escalation paths for when they cannot, so decisions are fast, owned and traceable without bureaucracy.

## When to use
- A project or program is being initiated and its control structure must be agreed.
- Decisions stall, are revisited repeatedly, or are made by people without the mandate.
- An audit, sponsor or new executive asks for a clear decision and reporting structure.
- Existing governance is disproportionate (too many boards, or none for a high-risk effort).

## When not to use
- Only task-level responsibility for deliverables is needed. Use `raci-matrix`.
- The need is the content of one steering meeting. Use `steering-committee-pack`.
- Only the scope change process is in question. Use `change-control`.

## Inputs
Required:
- The project or program: goal, size (budget/duration order of magnitude), and main parties (sponsor, business units, suppliers).

Optional, improves quality:
- Existing corporate governance (portfolio board, architecture board, change advisory, risk committee) and mandatory gates.
- Contract structure with suppliers; regulatory or audit requirements.
- Known decision problems or past failures.
- The team's delivery approach (fixed iterations, flow, phased).

If the project description is missing, ask. Unknown roles and names stay `[TBD]`; do not invent people.

## Process
1. Size the governance to the risk: assess complexity, budget, regulatory exposure, number of parties and novelty; state the resulting governance weight (light, standard, heavy) and why. Reuse existing corporate forums rather than creating parallel ones.
2. Define the decision types the effort will face: strategy/business case, scope, budget and contingency release, schedule/milestones, architecture and technology, supplier/contract, risk acceptance, quality/release (go/no-go), benefits.
3. Assign decision rights per decision type: who decides, who must be consulted, who is informed, and the threshold that moves the decision up a level. Exactly one decider per decision type and level.
4. Set tolerances per level (time, cost, scope, quality, risk, benefits): within tolerance the level below decides; forecast breach triggers escalation. Express tolerances as numbers or `[TBD]`, never vague words.
5. Design the forums: for each, purpose, chair, members, mandate (which decisions), quorum, frequency, inputs required and outputs (decision log entries). Remove any forum without decision rights.
6. Define gates or decision points aligned with the delivery approach: phased projects use stage gates; iterative delivery uses outcome or funding checkpoints. For each gate: entry criteria, evidence required, decision options (proceed, proceed with conditions, redirect, stop), decision owner.
7. Define escalation paths with time limits: issue raised → owner level → next level within <n> working days, with the information an escalation must contain.
8. Define reporting cadence: which report goes to which forum, how often, owner, and the minimum content (status against tolerance, decisions needed, risks, financials).
9. Define assurance: independent reviews, audit touchpoints, how decisions and changes are recorded and made traceable.
10. Check for gaps and overlaps: every decision type has an owner at each level; no two forums claim the same decision; the delivery team has room to act within tolerance.
11. List assumptions and open questions, then suggest `raci-matrix` for deliverable-level roles, `steering-committee-pack` for the first board meeting, or `change-control` for the change process.

## Output format
```markdown
# Governance Framework: <project / program>
Governance weight: <light / standard / heavy> — <rationale>

## Structure
<sponsor → steering committee → program/project lead → workstreams; existing corporate forums linked>

## Decision Rights
| Decision type | Team level | Project/program lead | Steering committee | Corporate forum | Escalation threshold |
|---|---|---|---|---|---|

## Tolerances
| Dimension | Lead tolerance | Steering tolerance | Beyond → |
|---|---|---|---|

## Forums
| Forum | Purpose / mandate | Chair | Members | Frequency | Inputs | Outputs |
|---|---|---|---|---|---|---|

## Gates / Decision Points
| Gate | When | Entry criteria | Evidence | Decision owner | Options |
|---|---|---|---|---|---|

## Escalation Path
## Reporting Cadence
| Report | Audience / forum | Frequency | Owner | Minimum content |
|---|---|---|---|---|

## Assurance and Traceability
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Governance weight is justified by risk and reuses existing corporate forums.
- [ ] Every decision type has exactly one decider per level and a numeric or `[TBD]` escalation threshold.
- [ ] Every forum has a mandate with real decision rights; none duplicates another.
- [ ] Gates have entry criteria, required evidence and explicit stop/redirect options.
- [ ] Escalation paths have time limits and required content.
- [ ] No invented names or thresholds; inferences are labeled and listed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Creating forums that only receive updates. A forum without decisions to take is a reporting meeting; merge or remove it.
- Setting no tolerances, so every deviation escalates. Delegate within numeric tolerances to keep decisions close to the work.
- Imposing phase-gate governance on iterative delivery. Gate on outcomes and funding checkpoints instead of document completion.

## Example
Input: "14-month ERP replacement, external integrator, 3 business units, existing IT steering committee."

Excerpt of output:
| Decision type | Program lead | Steering committee | Escalation threshold |
|---|---|---|---|
| Contingency release | up to `[TBD]`% of contingency | above that | Any release that would leave contingency below `[TBD]` |
| Scope change | within agreed backlog, no milestone impact | milestone or cross-BU impact | Change moves a milestone > 2 weeks `[ASSUMPTION]` |
| Supplier change request | recommends | approves | Any change to contract value |

- Forum decision: reuse the existing IT steering committee as the program board (with the 3 BU heads added) rather than creating a new one.
