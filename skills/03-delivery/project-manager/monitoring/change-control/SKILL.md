---
description: Runs a change request through change control: captures the request, assesses impact on scope, schedule, cost, quality, risk and contract, lays out options, routes it to the right decision authority and updates the change log and baselines. Use when someone asks to add, remove or alter approved scope, dates or budget, when a vendor submits a change order, or when scope creep must be made visible and decided.
related: scope-statement, impact-analysis, raid-log, decision-log, earned-value-analysis
prompt: The client now wants SSO with their Azure AD in addition to the agreed login. Prepare a change request with impact assessment for the change board.
---

# Run Change Control

## Purpose
Make every change to an approved baseline explicit, assessed and decided by the right authority, so that scope, schedule and budget stay consistent and nobody absorbs unapproved work silently.

## When to use
- A stakeholder requests new or changed scope after the baseline is approved.
- A date, budget or quality target must move.
- A vendor submits a change order or claims additional effort.
- Informal "small additions" are accumulating and need to be surfaced.

## When not to use
- The baseline is not yet approved. Refine it with `scope-statement`.
- Deep technical or requirements impact of a change. Use `impact-analysis`, then return here for the decision.
- An operational change to production systems. Use the service change process, not project change control.

## Inputs
Required:
- The change description (what, who asked, why).
- The current baseline reference (scope statement, schedule, budget) or its relevant parts.

Optional, improves quality:
- Governance thresholds (who approves what size of change), contract change clauses.
- Estimates from the team, dependency map, current RAID log.

If the change description or baseline reference is missing, ask for it. Everything else becomes an open question.

## Process
1. Log the request with an ID, requester, date and the requester's stated reason; separate the literal ask from the underlying need and mark any inferred need `[ASSUMPTION]`.
2. Classify: scope addition, scope reduction, scope modification, schedule change, budget change, quality/standard change, or correction of a baseline error (not a change).
3. Check whether it is actually in the baseline; if the baseline already covers it, close it as clarification with a reference.
4. Assess impact on scope, schedule (critical path or not), cost (effort, licenses, vendor), quality, risk, resources, dependencies and contract; use ranges and mark team estimates not yet received as `[TBD]`.
5. Identify side effects: work already done that would be discarded, regulatory or security implications, effects on other projects.
6. Build options: approve as requested, approve with trade-off (swap out equal scope), defer to a later phase, reject. Give consequences of each.
7. Determine the decision authority from governance thresholds; if thresholds are not given, propose one and mark it `[ASSUMPTION]`.
8. Recommend an option with a one-paragraph rationale, keeping facts and PM judgment distinct.
9. After the decision, record it, update baselines (scope, schedule, budget), RAID entries and the change log, and communicate to affected parties.
10. If the user's goal continues, suggest `impact-analysis` for deeper technical impact, `decision-log` for recording the decision or `earned-value-analysis` to rebaseline tracking.

## Output format
```markdown
# Change Request CR-<id>: <short title>
| Field | Value |
|---|---|
| Requested by / date | <...> |
| Type | <classification> |
| Reason (stated) | <...> |
| Underlying need | <... or [ASSUMPTION]> |
| Decision authority | <role / board> |
| Status | Submitted / Assessed / Approved / Rejected / Deferred |

## Impact Assessment
| Dimension | Impact | Confidence | Notes |
|---|---|---|---|
| Scope | | | |
| Schedule | | | |
| Cost | | | |
| Quality / risk | | | |
| Resources / dependencies | | | |
| Contract | | | |

## Options
| Option | Consequences | Cost / time |

## Recommendation
## Decision Record
Decision: <...> | By: <...> | Date: <...> | Baselines updated: <list>

## Open Questions
```

## Quality checklist
- [ ] The change is compared against the actual baseline, not memory.
- [ ] Every impact dimension is assessed or marked `[TBD]` with an owner.
- [ ] At least one alternative to "approve as requested" is offered.
- [ ] The decision authority matches the change size.
- [ ] Baseline and log updates are listed for after the decision.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Approving "small" changes informally; their sum becomes the overrun. Log every change, even when auto-approved under a threshold.
- Assessing only cost and ignoring the critical path, test effort or operations.
- Treating defects in delivered work as change requests (or the reverse). Check against acceptance criteria.

## Example
Input: "Client wants SSO with their Azure AD besides the agreed username/password login."

Excerpt of output:
- Type: Scope addition. Baseline covers only local login (Scope statement §3.2).
- Underlying need: `[ASSUMPTION]` central account lifecycle for joiners/leavers, driven by their security policy.
- Options: (a) add in current release – schedule impact `[TBD – team estimate]`; (b) swap with reporting module; (c) phase 2.
- Decision authority: change board (above PM threshold) `[confirm threshold]`.
