---
name: incident-response
description: "Guides a live incident from declaration to resolution: severity assessment, role assignment (incident commander, operations, communications, scribe), a mitigation-first plan with hypotheses and parallel workstreams, a timestamped timeline, update cadence and exit criteria. Use when an outage or degradation is happening or suspected, when someone asks what to do right now about production impact, or to structure an ongoing incident channel."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: incident
  title: "Run incident response"
  related: "runbook, incident-communication, postmortem, log-analysis, security-incident-response"
  prompt: "We have an incident: checkout error rate jumped to 15% ten minutes after the 14:05 deploy. Help me run it."
---

# Run Incident Response

## Purpose
Coordinate a live incident so that user impact is reduced as fast as possible, people work in clear roles without duplicating effort, stakeholders stay informed, and a reliable timeline exists for the postmortem.

## When to use
- Production impact is happening or suspected (alerts, customer reports, SLO burn).
- An incident channel is open but chaotic: no commander, parallel uncoordinated fixes, no updates.
- A responder asks for a structured next step while under pressure.

## When not to use
- The event is a suspected security breach or data leak. Use `security-incident-response`; evidence handling and legal duties differ.
- The incident is over and learning is the goal. Use `postmortem`.
- Only the wording of an update is needed. Use `incident-communication`.

## Inputs
Required:
- What is observed now: symptoms, affected service, start time if known.

Optional, improves quality:
- Recent changes (deploys, config, infrastructure, dependencies), alerts firing, dashboards.
- Severity definitions and on-call/escalation roster of the organization.
- Relevant runbooks.

Do not delay mitigation to gather inputs. Ask at most the one or two questions that change the next action; everything else becomes a workstream or open question.

## Process
1. Declare and classify: assign a severity from user impact (scope, function lost, data at risk), using the organization's scale or a proposed SEV1-4 marked `[PROPOSED]`; state that severity can be changed as facts change.
2. Assign roles: incident commander (coordinates, decides, does not debug), operations lead(s), communications lead, scribe; name a handover rule for long incidents.
3. Establish the facts: start time, what changed recently, blast radius (users, regions, tenants), what is known vs. assumed; label each assumption.
4. Choose mitigation first: if a recent change correlates, roll it back or disable its flag before root-cause analysis; other options are traffic shift, scaling, failover, load shedding, dependency bypass.
5. Run parallel workstreams with one owner each (e.g. mitigate, diagnose, customer impact), each with a hypothesis, a time box and a report-back time; change one variable at a time.
6. Keep a timestamped timeline of observations, decisions and actions with their owners, in UTC or a stated time zone.
7. Set the update cadence by severity (e.g. every 30 minutes for the highest, or on material change) and hand content to `incident-communication`.
8. Escalate when a time box expires without progress, when data integrity is at risk, or when more authority is needed (e.g. customer-facing decision).
9. Confirm mitigation with signals (SLIs back within normal range for an agreed period), then decide monitoring duration before closing.
10. Close: record resolution, residual risk, follow-up owners, and whether a postmortem is required by policy (typically for the highest severities or budget-breaching events).
11. Label every inference `[ASSUMPTION]` and suggest the next skill: `postmortem` after resolution, `runbook` if a procedure was missing, `incident-communication` for the final update.

## Output format
```markdown
# Incident: <short title> · Severity: <SEVn> · Status: <investigating / mitigating / monitoring / resolved>
Started: <time> · Declared: <time> · IC: <name> · Ops: <name> · Comms: <name> · Scribe: <name>

## Current Impact
## Known Facts vs. Assumptions
## Mitigation Plan
| Option | Risk | Decision | Owner |

## Workstreams
| Workstream | Owner | Hypothesis | Time box | Report back at |

## Timeline
| Time | Event / decision / action | Who |

## Next Update Due
## Exit Criteria and Follow-ups
```

## Quality checklist
- [ ] Severity is based on user impact and roles are assigned, with the commander not debugging.
- [ ] Mitigation options are considered before root-cause work.
- [ ] Every workstream has one owner, a hypothesis and a time box.
- [ ] The timeline records times, decisions and owners; facts are separated from assumptions.
- [ ] The next update time and exit criteria are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Debugging the root cause while users are still affected. If a rollback is safe, do it first.
- Everyone joining the call and trying fixes at once. Assign owners and change one thing at a time so effects stay attributable.
- Declaring resolved at the first green graph. Confirm on SLIs over an agreed monitoring period.

## Example
Input: "Checkout errors at 15% since about 14:15; deploy at 14:05."

Excerpt of output:
- Severity: SEV2 `[PROPOSED: partial loss of a critical function; confirm against org scale]`.
- Fact: deploy at 14:05; errors since ~14:15. Assumption: the deploy is related `[ASSUMPTION: correlation, not yet proven]`.
- Mitigation decision: roll back the 14:05 deploy (low risk, fast) – Ops lead; in parallel, Diagnose workstream checks error logs for the new code path, report back at 14:40.
- Next update: 14:45 or on material change.
