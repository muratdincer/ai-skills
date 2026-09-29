---
name: postmortem
description: "Writes a blameless postmortem from incident notes, chat logs, alerts and timelines: summary, customer and business impact, a timestamped timeline, detection and response analysis, contributing factors and root causes traced beyond the trigger, what went well, and prioritized corrective actions with owners and due dates. Use after an incident is resolved, when an SLO breach or near miss needs a formal review, or when a draft postmortem must be made blameless and actionable."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: incident
  title: "Write a blameless postmortem"
  related: "incident-response, incident-communication, runbook, error-budget-policy, alert-design"
  prompt: "Here are the chat log and alert history of last night's payment outage. Write a blameless postmortem with timeline, root causes and action items."
---

# Write a Blameless Postmortem

## Purpose
Turn an incident into durable learning: an accurate account of what happened, why the system allowed it, and a small set of owned actions that make recurrence less likely or less harmful. Blameless means focusing on conditions and decisions in context, not on who made a mistake.

## When to use
- An incident has been mitigated and the team needs the review document.
- An SLO was breached, error budget consumed, or a near miss deserves learning.
- A draft postmortem blames individuals or lacks actionable follow-ups and needs rework.

## When not to use
- The incident is still ongoing. Use `incident-response`.
- The need is status updates to customers or stakeholders during the incident. Use `incident-communication`.
- A generic project retrospective, not an incident. Use `lessons-learned` or `retrospective-facilitation`.

## Inputs
Required:
- Incident material: timeline notes, chat or bridge log, alerts, or a written account of what happened and how it was resolved.

Optional, improves quality:
- Metrics and dashboards, deployment and change history, customer impact data (affected users, failed transactions), SLO and error budget data.
- Existing action items, severity definitions, organization postmortem template.

If there is no incident material, ask. Missing timestamps or numbers are marked `[UNKNOWN]`, never estimated as fact.

## Process
1. Write a factual summary: what failed, for whom, how long, how it was mitigated; severity per the organization's scale.
2. Quantify impact from data only: duration (start, detection, mitigation, resolution), affected users or requests, failed transactions, SLO and error budget consumed, data loss, contractual or regulatory implications. Mark unknowns.
3. Build the timeline with timestamps and time zone: first trigger, first symptom, detection, escalation, key decisions, mitigation, recovery, all-clear. Tag each entry with its source.
4. Compute and comment on response metrics: time to detect, time to engage, time to mitigate, time to resolve; identify where time was lost.
5. Analyze causes beyond the trigger: ask why the change or condition caused harm, why it was not caught earlier (tests, review, canary), why detection took as long as it did, and why recovery was slow. Use a structured method (e.g., five whys per branch, or a contributing factor tree); expect several contributing factors, not a single root cause.
6. Rewrite any blaming language into system terms ("the deploy tool allowed a config change without validation" instead of "X pushed a bad config"). Remove names from the narrative; refer to roles.
7. Record what went well and where the team got lucky; luck is a hidden risk.
8. Define corrective actions in categories: prevent, detect, mitigate, process; each specific, with owner role, priority and due date `[TBD]` if not given, and a way to verify it is done. Prefer a few high-leverage actions over many small ones.
9. List open questions and follow-up investigations; separate confirmed facts from inferences labeled `[ASSUMPTION]`.
10. If the goal continues, suggest `runbook` to document the mitigation, `alert-design` for detection gaps, or `error-budget-policy` if the SLO consequences need a decision.

## Output format
```markdown
# Postmortem: <incident title> (<date>)
Severity: <level> · Status: Draft/Reviewed · Authors: <roles> · Blameless: yes

## Summary
<3-5 sentences>

## Impact
| Measure | Value | Source |
|---|---|---|
| Duration (start → resolved) | | |
| Affected users / requests | | |
| SLO / error budget consumed | | |

## Timeline (<time zone>)
| Time | Event | Source |
|---|---|---|

## Response Metrics
| Time to detect | Time to engage | Time to mitigate | Time to resolve |
|---|---|---|---|

## Contributing Factors and Root Causes
- Trigger: ...
- Why it caused harm: ...
- Why it was not caught earlier: ...
- Why detection/recovery took this long: ...

## What Went Well / Where We Got Lucky
## Corrective Actions
| # | Action | Category | Owner role | Priority | Due | Verified by |
|---|---|---|---|---|---|---|

## Open Questions
```

## Quality checklist
- [ ] Every timestamp and impact number comes from the provided material or is marked `[UNKNOWN]`.
- [ ] The narrative names roles and systems, not individuals, and contains no blaming language.
- [ ] Causes go beyond the trigger and cover why it was not prevented, detected sooner or recovered faster.
- [ ] Each corrective action is specific, owned, prioritized and verifiable; none is "be more careful".
- [ ] Facts and inferences are separated; inferences are labeled `[ASSUMPTION]`.
- [ ] Personal or customer data in logs is masked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Stopping at "human error". Ask what made the error possible and easy, and fix that condition.
- A long list of low-value actions that are never done. Pick a few that address the largest contributing factors.
- Rewriting the timeline with hindsight. Record what responders knew at each moment, which explains their decisions.

## Example
Input: "Config change at 22:10 set payment gateway timeout to 1 s; errors rose; alert at 22:41; rollback at 23:05."

Weak: "Root cause: engineer set a wrong timeout. Action: be more careful with configs."

Strong excerpt:
- Trigger: a configuration change reduced the gateway timeout to 1 s.
- Why it caused harm: gateway p99 latency is above 1 s at peak `[ASSUMPTION: confirm from metrics]`, so a share of payments timed out.
- Why not caught: configuration changes bypass the canary stage used for code deploys.
- Why detection took 31 min: the alert fires on 10% error rate over 15 min; the error rate stayed around 6%.
| # | Action | Category | Owner role | Priority | Verified by |
|---|---|---|---|---|---|
| 1 | Route config changes through the same canary and automated rollback as code | Prevent | Platform lead | High | Test change rolled back automatically in staging |
| 2 | Add burn-rate alert on payment success SLO | Detect | SRE | High | Alert fires in replay of this incident |
