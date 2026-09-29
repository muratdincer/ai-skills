---
name: risk-register
description: "Builds a project risk register with cause-event-effect risk statements, probability and impact scores, proximity, owners, response strategies (avoid, mitigate, transfer, accept, exploit) with actions and triggers, and residual risk. Use when planning a project, before a gate or steering meeting, or when new threats or opportunities emerge."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Build a risk register"
  related: "raid-log, pre-mortem, technical-risk-review, it-risk-assessment, budget-plan"
  prompt: "Build a risk register for our warehouse management system rollout; here are the plan and concerns raised in the kickoff."
---

# Build a Risk Register

## Purpose
Make uncertain events that could affect objectives explicit, prioritized and owned, with concrete responses, so that risks are managed ahead of time instead of becoming issues.

## When to use
- During planning, to establish the baseline risk register.
- Before gates, steering meetings or major releases.
- When new information (vendor problems, regulatory change, key resignation) changes the risk profile.

## When not to use
- Tracking risks together with assumptions, issues and dependencies in one light log. Use `raid-log`.
- A structured failure brainstorm with the team. Use `pre-mortem` first, then feed this register.
- Enterprise IT or information security risk assessment. Use `it-risk-assessment`.

## Inputs
Required:
- Project context (charter, scope or plan summary).

Optional, improves quality:
- Existing concerns, lessons learned from similar projects, organizational risk scales and appetite.
- Schedule and budget, to quantify impact.

If context is missing, ask for a project summary. Use organizational scales if given; otherwise a 1-5 scale defined in the output.

## Process
1. Elicit risks by category: scope/requirements, schedule, cost, resources, technology, data, vendors, organizational change, regulatory, security, operations.
2. Write each risk as "Because of <cause>, <uncertain event> may occur, leading to <effect on objective>". Reject vague entries like "resources".
3. Separate risks from issues (already happened) and from assumptions; move them to the right log.
4. Score probability and impact (1-5) with defined anchors; score impact against the dominant objective (time, cost, scope, quality) and note which.
5. Add proximity (when the risk could materialize) and early-warning triggers.
6. Rank by score and proximity; identify the top 10.
7. Choose a response strategy per risk: threats (avoid, mitigate, transfer, accept), opportunities (exploit, enhance, share, accept). Define concrete actions with owner and due date.
8. Estimate residual score after response and define fallback plans for high residual risks.
9. Where budgets allow, compute expected monetary value (probability × cost impact) to size contingency; never invent the cost impact.
10. Set review cadence and closure criteria.
11. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `raid-log` for ongoing tracking, or `pre-mortem` to surface risks the team has not yet named.

## Output format
```markdown
# Risk Register: <project>
Scale: P and I 1-5 (anchors below) | Review cadence <x>
| ID | Risk statement (cause → event → effect) | Category | P | I | Score | Proximity | Trigger | Strategy | Actions (owner, due) | Residual | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
## Top Risks Summary
## Scale Anchors
| Score | Probability | Impact on schedule | Impact on cost |
## Contingency Link (EMV, if used)
## Open Questions
```

## Quality checklist
- [ ] Every risk follows cause-event-effect and is an uncertain future event.
- [ ] Each risk has one owner and at least one dated action or an explicit accept decision.
- [ ] Scales are defined; scores are consistent.
- [ ] Opportunities are considered, not only threats.
- [ ] No impact value is fabricated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing generic risks that apply to every project. Make them specific to this context.
- Owners who cannot influence the risk. Assign someone with authority to act.
- Treating the register as a compliance artefact reviewed once. Tie reviews to the reporting cycle.

## Example
Input: "WMS rollout; vendor has never integrated with our ERP; peak season starts in November."

Excerpt of output:
| R-02 | Because the vendor has no prior integration with our ERP, interface defects may surface late in testing, delaying go-live past the pre-peak freeze | Technology | 4 | 5 | 20 | Integration test phase | >10 open interface defects at SIT midpoint | Mitigate | Early interface prototype by M2 (Integration lead) | 12 | Open |
