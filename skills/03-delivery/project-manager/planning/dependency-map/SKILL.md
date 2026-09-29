---
description: Maps a project's internal and external dependencies, stating what is needed, from whom, by when, the providing and receiving owners, commitment status, criticality and the fallback if the dependency slips. Use when a project relies on other teams, vendors, platforms or decisions, or when missed hand-offs are threatening milestones.
related: schedule-plan, raid-log, cross-team-dependency-board, risk-register, integration-requirements
prompt: Map all dependencies for our loyalty program launch: marketing, the POS vendor, data team and the legal review.
---

# Map Dependencies

## Purpose
Make every hand-off the project relies on explicit, owned and dated, so that commitment gaps and schedule exposure are visible and negotiated before they cause delays.

## When to use
- During planning, before the schedule baseline is agreed.
- When the project needs deliverables, decisions or environments from other parties.
- When a dependency has slipped and its impact must be assessed.

## When not to use
- Program-level dependency planning across many teams in a joint session. Use `cross-team-dependency-board`.
- Activity sequencing within the project. Use `schedule-plan`.
- Technical interface specifications. Use `integration-requirements`.

## Inputs
Required:
- Project scope or plan summary and the parties involved.

Optional, improves quality:
- Schedule and milestones, contracts/SLAs with providers, org charts.

If the parties or plan are unknown, ask for them; list suspected dependencies as `[ASSUMPTION]`.

## Process
1. Scan for dependency types: deliverables from other teams, vendor supplies, platform/environment availability, data access, decisions/approvals, regulatory or legal reviews, shared people.
2. Classify direction: inbound (we need) and outbound (others need from us).
3. For each, record the exact item, providing owner, receiving owner, need-by date and the milestone it feeds.
4. Record commitment status: Not requested, Requested, Agreed, At risk, Delivered. Only "Agreed" if the provider confirmed.
5. Assess criticality: on the critical path or not, and float available.
6. Define the fallback or workaround and the latest decision date for switching to it.
7. Identify dependency chains and circular dependencies; flag clusters on one provider.
8. Add escalation route per provider and a review cadence.
9. Feed at-risk dependencies into the risk register or RAID log.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `raid-log` or `risk-register` to track at-risk dependencies, and `schedule-plan` to reflect them in the timeline.

## Output format
```markdown
# Dependency Map: <project>
| ID | Direction | Item needed | Provider (owner) | Receiver (owner) | Need-by | Feeds milestone | Status | Critical path? | Fallback | Decision date |
|---|---|---|---|---|---|---|---|---|---|---|
## Critical and At-Risk Dependencies
## Provider Concentration
| Provider | # dependencies | Escalation contact |
## Diagram (optional)
<text or Mermaid flowchart of providers → deliverables → milestones>
## Open Questions
```

## Quality checklist
- [ ] Each dependency names a concrete item, not "support from team X".
- [ ] Status "Agreed" only where confirmed by the provider.
- [ ] Every critical dependency has a fallback and decision date.
- [ ] Outbound dependencies are included.
- [ ] Names and dates are not invented; gaps are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Recording dependencies without the provider's knowledge. Confirm in writing.
- Need-by dates equal to the use date, leaving no buffer for integration.
- Ignoring decision dependencies (approvals, legal sign-off), often the longest lead times.

## Example
Input: "Loyalty launch needs POS vendor update, customer data from data team, and legal approval of terms."

Excerpt of output:
| D-01 | Inbound | POS release with loyalty API v2 | POS vendor (account manager) | Integration lead | `[TBD]` | UAT start | Requested | Yes | Manual points entry in back office for 4 weeks | 3 weeks before UAT |
