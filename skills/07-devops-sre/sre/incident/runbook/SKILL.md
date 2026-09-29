---
description: "Writes an operational runbook for one alert or failure mode: symptoms and impact, fast triage, diagnosis branches with exact checks and expected results, safe remediation steps with verification and rollback, escalation and follow-up. Use when a paging alert has no runbook, when on-call relies on tribal knowledge, after an incident showed a missing procedure, or when someone asks how to handle a recurring operational problem."
related: "alert-design, incident-response, known-error-article, postmortem, observability-plan"
prompt: "Write a runbook for the alert OrderQueueLagHigh: Kafka consumer lag above 10k for 10 minutes on the order-events topic."
---

# Write a Runbook

## Purpose
Give an on-call engineer who may not know the system a safe, fast path from an alert or symptom to mitigation, with each step verifiable, so recovery does not depend on who happens to be on call.

## When to use
- A paging alert exists without a linked runbook.
- A recurring operational task or failure is handled from memory by one or two people.
- A postmortem action item asks for a documented procedure.

## When not to use
- The alert itself is noisy or not actionable. Fix it with `alert-design` first; do not document a workaround for a bad alert.
- A full site or region recovery is needed. Use `dr-plan`.
- The audience is end users or support agents with a known workaround. Use `known-error-article`.

## Inputs
Required:
- The alert or symptom the runbook covers, and the affected service.
- What is known about causes and fixes (past incidents, expert notes), or a statement that little is known.

Optional, improves quality:
- Architecture and dependencies, dashboards, log and trace queries, access requirements.
- Past incident timelines and postmortems for this failure.
- Escalation contacts and service owner.

If the alert or symptom is unclear, ask. Commands, hostnames and queries not given by the user are placeholders marked `[TBD]`; never invent them.

## Process
1. State what the alert means in user terms: which users or functions are affected, and the severity guidance (when to declare an incident).
2. Write a first-five-minutes triage: confirm the alert is real (dashboard link, check), check scope (one instance, zone, tenant, or all), and check recent changes (deploys, config, feature flags, infrastructure).
3. List likely causes ordered by frequency and ease of checking, drawn from history; mark causes inferred without history as `[ASSUMPTION]`.
4. For each cause write a diagnosis branch: the exact check, the expected result if this is the cause, and the next step if not.
5. Write remediation steps per cause, preferring safe and reversible mitigations first (roll back the recent change, shift traffic, scale out, restart one instance, disable a feature flag) before risky fixes.
6. For each remediation add verification (which signal returns to normal and in how long) and rollback if the step makes things worse.
7. Mark dangerous steps explicitly (data deletion, failover, queue purge) with required approval and preconditions.
8. Define escalation: when to escalate (time box, unknown cause, data risk), to whom, and what information to hand over.
9. Add follow-up: what to record in the incident timeline, and what to capture for a postmortem.
10. Add metadata: owner, last reviewed date, last used date, and a review trigger (after each use or on system change).
11. Label every inference `[ASSUMPTION]`, list open questions, and suggest next skills: `incident-response` if the issue grows, `postmortem` after use, or `alert-design` if the alert needs tuning.

## Output format
```markdown
# Runbook: <alert or symptom>
Service: <name> · Owner: <team> · Last reviewed: <date or [TBD]> · Severity guidance: <when to declare>

## What This Means
## Triage (first 5 minutes)
1. Confirm: <check> → <expected>
2. Scope: ...
3. Recent changes: ...

## Diagnosis
| Likely cause | Check | If yes | If no |

## Remediation
### Cause A
1. <step> · Verify: <signal, time> · Rollback: <how>

## Dangerous Actions (approval required)
## Escalation
## Follow-up and Records
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every step is concrete and verifiable; placeholders are marked `[TBD]` rather than invented.
- [ ] Triage checks recent changes and scope before deep diagnosis.
- [ ] Safe, reversible mitigations come before risky fixes.
- [ ] Every remediation has verification and rollback.
- [ ] Dangerous actions require approval and state preconditions.
- [ ] Escalation has a time box and a named target.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Investigate the logs" as a step. Name the query, the field and what a bad result looks like.
- Jumping to root-cause fixing during an outage. The runbook's job is mitigation first; root cause belongs to the postmortem.
- Runbooks that rot. Tie review to each use and to changes of the system, and record the last-used date.

## Example
Input: "Alert OrderQueueLagHigh: consumer lag > 10k for 10 min on order-events."

Excerpt of output:
| Likely cause | Check | If yes | If no |
|---|---|---|---|
| Recent consumer deploy | Deploy history for order-consumer in last 2 h | Roll back to previous version, watch lag trend for 10 min | Next row |
| Poison message | Consumer error logs for repeated offset `[TBD: query]` | Move message to dead-letter per procedure (approval: service owner) | Next row |
| Traffic spike | Produce rate vs. 7-day baseline | Scale consumers up to partition count | Escalate to order team |
