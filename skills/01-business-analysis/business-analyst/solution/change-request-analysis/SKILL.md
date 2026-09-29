---
description: "Analyzes a change request against the agreed baseline: classifies it (new scope, modification, clarification, defect in disguise), assesses value, scope, effort drivers, schedule, cost and risk impact, lists options and recommends accept, accept with trade-off, defer or reject with rationale for the change authority. Use when a stakeholder asks to add or change something after requirements were baselined or during delivery, or when a change control board needs a decision paper."
related: "impact-analysis, change-control, change-request-rfc, requirements-sign-off, trade-off-analysis"
prompt: "Marketing wants to add SMS notifications to the loyalty release two weeks before go-live. Analyze the change request and give a recommendation."
---

# Analyze a Change Request

## Purpose
Give the change authority a clear, evidence-based decision paper for a requested change: what it is, why it matters, what it costs in scope, time and risk, and what the options are. This keeps scope changes deliberate instead of silent.

## When to use
- A stakeholder asks to add, modify or remove a requirement after the baseline.
- A change control board or sponsor must decide on a change.
- A "small tweak" arrives late in delivery and its true size is unclear.

## When not to use
- The change is operational (deploying to production, infrastructure change). Use `change-request-rfc`.
- You only need the list of affected items without a decision. Use `impact-analysis`.
- You are defining the project's change control procedure itself. Use `change-control`.

## Inputs
Required:
- The change request as raised (text, ticket, email).
- The current baseline or a description of what was agreed (scope, dates).

Optional, improves quality:
- Impact analysis results, current plan and capacity, remaining contingency.
- Contract terms for changes (if external delivery), decision authority and thresholds.

If the baseline is unknown, say that the analysis cannot distinguish change from original scope and ask for it; do not assume.

## Process
1. Restate the request: requester, literal ask, underlying need (the problem behind it) and why now. Mark inferences.
2. Classify: new scope, modification of agreed scope, clarification of existing scope (no change), defect (baseline not met) or regulatory/mandatory. Clarifications and defects do not go through change approval as new scope.
3. Compare with the baseline: cite the affected requirement IDs or scope items and state old vs requested.
4. Assess value and urgency: which goal it serves, cost of not doing it, cost of doing it later versus now.
5. Assess impact: use or summarize an impact analysis (processes, systems, data, reports, tests, documents); name effort drivers. Use given estimates only; otherwise describe relative size and mark `[ASSUMPTION]`.
6. Assess schedule, cost and quality impact: effect on the critical path and release date, budget or contingency consumption, testing and stabilization risk, especially close to go-live.
7. Identify risks of doing it and of not doing it.
8. Build options: accept as is; accept with trade-off (drop or defer an item of equal size); accept in a later release; accept a reduced version; reject.
9. Recommend one option with rationale and conditions, and name the decision authority and the decision needed by date.
10. List what must be updated if approved: baseline, plan, traceability, test scope, contract, communication.
11. If the user wants to continue, suggest `impact-analysis` for a deeper impact view, `trade-off-analysis` to compare options or `requirements-sign-off` to re-baseline after approval.

## Output format
```markdown
# Change Request Analysis: <CR ID> <title>
Requester: <...> · Raised: <date> · Decision authority: <...> · Decision needed by: <date or [UNKNOWN]>

## Request
- Literal ask: ...
- Underlying need: ... [inferred?]
- Classification: <new scope / modification / clarification / defect / mandatory>
- Baseline items affected: <IDs> (old → requested)

## Assessment
| Dimension | Assessment | Evidence / basis |
|---|---|---|
| Value and urgency | | |
| Scope and effort drivers | | |
| Schedule | | |
| Cost / contingency | | |
| Quality and risk | | |

## Options
| Option | Description | Pros | Cons |
|---|---|---|---|

## Recommendation
<option> – <rationale> – <conditions>

## If Approved, Update
- ...
```

## Quality checklist
- [ ] The request is classified, and clarifications or defects are not treated as new scope.
- [ ] Baseline items are cited, so the delta is explicit.
- [ ] Effort, cost and schedule figures come from the input or are marked `[ASSUMPTION]`.
- [ ] At least one trade-off or deferral option is offered, not just accept/reject.
- [ ] The risk of not doing the change is stated alongside the risk of doing it.
- [ ] Decision authority and needed-by date are named or marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Accepting "small" changes without analysis. Late changes carry test and stabilization cost far beyond build effort.
- Analyzing the requested solution instead of the need. A cheaper option often meets the same need.
- Recommending without a trade-off. If capacity is fixed, something else must move; say what.

## Example
Input: "Marketing wants SMS notifications in the loyalty release, 2 weeks before go-live."

Excerpt of output:
- Classification: New scope (no SMS requirement in baseline; REQ-12 covers email only).
- Underlying need `[inferred]`: reach members without email consent before the launch campaign.
- Schedule: needs SMS gateway integration, consent handling (KVKK/GDPR) and regression; exceeds remaining 2 weeks `[ASSUMPTION]`.
- Recommendation: Accept in the next release; for launch, use in-app banner for members without email consent.
