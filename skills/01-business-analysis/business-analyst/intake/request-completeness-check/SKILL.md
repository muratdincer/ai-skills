---
name: request-completeness-check
description: "Checks a request or intake document against a gap checklist (business, users, data, integration, NFR, legal, operations, reporting, migration) and reports what is missing, vague or contradictory with severity and a ready/not-ready verdict. Use before a request enters analysis, estimation or a sprint/backlog, or when asked 'is this request complete enough to start?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: intake
  title: "Check request completeness"
  related: "request-intake-document, request-clarification-questions, ambiguity-detection, requirements-gap-analysis, definition-of-ready"
  prompt: "Check whether this request is complete enough to start analysis: 'Add a discount approval step for orders above a limit, managers approve by email.'"
---

# Check Request Completeness

## Purpose
Give an explicit verdict on whether a request can move to analysis or estimation, and list exactly which gaps must be closed first, so work does not start on a request that will be reworked.

## When to use
- Before a request enters analysis, estimation, a demand board or the backlog.
- An intake document was drafted and needs a quality gate.
- Estimates keep changing because requests arrive half-defined.

## When not to use
- You only need the questions to send the requester. Use `request-clarification-questions`.
- The input is already a detailed requirements set. Use `requirements-gap-analysis` or `ambiguity-detection`.

## Inputs
Required:
- The request text or intake document.

Optional, improves quality:
- The stage it is heading to (triage, analysis, estimation, build), which sets the bar.
- The organization's mandatory intake fields or definition of ready.
- Domain context (regulated sector, systems involved).

If the request is missing, ask for it. If the target stage is unknown, assume "ready for analysis" and state it.

## Process
1. Determine the bar: "ready for triage" needs goal, requester, type; "ready for analysis" adds scope, stakeholders, constraints; "ready for estimation" adds rules, data, integrations and NFR targets.
2. Run the gap checklist below. For each item decide: PRESENT, WEAK (mentioned but vague or untestable), ABSENT (not mentioned), DEFERRED (consciously postponed, with owner and stage), CONTRADICTORY or N/A (with reason). Record evidence for each: the quoted phrase, or "not mentioned".
3. Do not polish over ambiguity: never rewrite a WEAK item into a precise one yourself. Quote the phrase ("fast", "all users", "like the old system", "etc.", "ASAP") and say what is needed instead; any interpretation you add is labeled `[ASSUMPTION]`.
4. Detect contradictions (e.g., "no personal data" but "export customer contact list").
5. Rate each gap: Blocker (cannot proceed at this stage), Major (will cause rework), Minor (can be closed later).
6. For every Blocker and Major gap, write the question that closes it and who should answer.
7. Give the verdict: Ready, Ready with conditions (list them) or Not ready.
8. Compute a simple coverage indicator: number of applicable items Present vs total applicable. Do not present it as a quality score.
9. If the goal continues, suggest `request-clarification-questions` to turn the gaps into a message, or `requirements-gap-analysis` once detailed requirements exist.

Gap checklist:
- **Business:** problem statement, desired outcome, measurable success criteria, business value justification, sponsor/decision maker, deadline with reason, cost of delay.
- **Actors and roles:** user groups and volumes, internal vs external, channels/devices, accessibility, training impact, systems acting as actors.
- **Triggers and flows:** trigger event, main flow, alternate flows, approvals, manual workarounds today.
- **Pre/postconditions:** what must be true before start; resulting state after success and after failure.
- **Rules and validation:** business rules and their source, thresholds and limits, calculations, field validations.
- **Data:** entities and fields, source of truth, data quality, volumes and growth, personal/sensitive data, classification, retention and deletion.
- **Permissions and security:** who may view, create, change, approve; segregation of duties; sensitive operations; authentication level.
- **Error handling:** invalid input, timeouts, duplicates, partial failures, retries, user messages, who resolves.
- **Integration:** systems in and out, direction, frequency (real-time/batch), interface owner, error handling, dependency on third parties.
- **NFR:** performance targets, peak load, availability and support hours, recovery, localization, accessibility (WCAG 2.2 where relevant).
- **Legal and compliance:** KVKK/GDPR basis and consent, sector regulation, contracts, record keeping.
- **Support and operations:** support owner, monitoring and alerting, manual fallback, runbook, SLA impact, release window constraints.
- **Reporting and audit:** affected KPIs, reports and dashboards, consumers, frequency, historical comparability, audit trail (who, what, when).
- **Rollout, migration and maintenance:** data to migrate or clean, cut-over, parallel run, phased rollout, backward compatibility, decommissioning, long-term owner.

## Output format
```markdown
# Completeness Check: <request title>
Target stage: <triage / analysis / estimation / build> · Verdict: **<Ready / Ready with conditions / Not ready>**
Coverage: <present>/<applicable> applicable items present

## Gaps
| # | Area | Item | Status | Severity | Evidence / quoted phrase | Question to close | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Business | Success criteria | ABSENT | Blocker | not mentioned | ... | Sponsor |

## Contradictions
- "<quote A>" vs "<quote B>" – ...

## Deferred (owner, stage)
- ...

## Not applicable (with reason)
- ...

## Conditions to proceed
1. ...
```

## Quality checklist
- [ ] Every checklist area was evaluated or marked not applicable with a reason.
- [ ] Vague items quote the exact phrase from the request.
- [ ] Severity reflects the target stage, not a generic ideal.
- [ ] Every Blocker has a closing question and an owner.
- [ ] The verdict is consistent with the gap list (no "Ready" with open Blockers).
- [ ] No missing information was filled in by guesswork, and no WEAK item was silently rewritten as precise.
- [ ] Every finding is classified ABSENT, WEAK or DEFERRED (or PRESENT/CONTRADICTORY/N/A) with evidence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Demanding estimation-level detail at triage. Match the bar to the stage or good requests get stuck.
- Marking an area "not applicable" because the requester did not mention it. Data, legal and operations gaps are usually silent, not absent.
- Treating a proposed solution as a complete requirement. "Approve by email" is a mechanism; the rule (who, which limit, what if rejected) is still missing.

## Example
Input: "Add a discount approval step for orders above a limit, managers approve by email."

Excerpt of output:
Target stage: analysis · Verdict: **Not ready**
| # | Area | Item | Status | Severity | Evidence | Question to close | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Rules | Approval rule | WEAK | Blocker | "above a limit" | Is the limit an amount, a discount %, or both? Fixed or per region? | Sales ops |
| 2 | Error handling | Rejection/timeout path | ABSENT | Blocker | not mentioned | What happens if the manager rejects or does not answer in time? | Sales ops |
| 3 | Reporting and audit | Audit trail | ABSENT | Major | not mentioned | Must approvals be auditable (who, when, what value)? | Finance / audit |
