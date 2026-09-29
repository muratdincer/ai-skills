---
name: change-request-rfc
description: "Writes an IT change request (RFC) ready for change approval or a change advisory board: reason, scope and affected configuration items, change type, risk and impact assessment, implementation plan, test evidence, backout plan with trigger, schedule, communication and verification. Use when a production change to infrastructure, applications, configuration or data needs approval, when a CAB submission is due, or when an emergency change must be documented."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: it-service-management
  area: itsm
  title: "Write a change request (RFC)"
  related: "rollback-plan, deployment-checklist, deployment-strategy, technical-risk-review, problem-management"
  prompt: "Write an RFC to upgrade the production PostgreSQL cluster from 14 to 16 this Saturday night; 3 apps depend on it, we tested on staging last week."
---

# Write a Change Request (RFC)

## Purpose
Give approvers enough evidence to decide quickly and implementers a plan they can execute and reverse safely, so changes succeed first time and failed changes are rolled back before they become incidents.

## When to use
- A normal change to production (infrastructure, application, configuration, access, data) needs approval.
- A change goes to a change advisory board or an approver who needs a risk view.
- An emergency change was or must be made and needs documentation and retrospective approval.

## When not to use
- A pre-approved standard change with an existing template. Use that template or `runbook`.
- A change to project scope, budget or timeline. Use `change-control`.
- Only the technical rollback procedure is needed. Use `rollback-plan`.

## Inputs
Required:
- What will change, where (environment, systems) and why.
- Planned date/time or the constraint that sets it.

Optional, improves quality:
- Affected configuration items and dependencies, test results, previous similar changes and their outcome.
- The organization's RFC template, risk matrix, change windows and freeze periods.
- Implementer, approvers, business owner, vendor involvement.

If what, where or why is missing, ask in one message. Do not fill the risk rating, downtime or test results without evidence; mark them `[UNKNOWN]` or `[ASSUMPTION]`. Never include credentials, keys or connection strings in the RFC.

## Process
1. State the change and its reason as a business and technical outcome (for example, end-of-support version, security fix, capacity, problem PRB-...), and the risk of not doing it.
2. Classify the change type (standard, normal, emergency) using the organization's definitions; justify emergency status explicitly.
3. List affected configuration items, upstream and downstream dependencies, users and services; check the change calendar for conflicts and freeze periods.
4. Assess impact: expected downtime or degradation, data migration or schema effects, performance, security and compliance implications (for example, personal data processing under KVKK/GDPR, audit logging).
5. Rate risk with likelihood x impact (use the organization's matrix, otherwise a 3x3 scale marked `[ASSUMPTION]`), listing the top risks with mitigations.
6. Write the implementation plan as timed, numbered steps with owner and checkpoint, including pre-checks (backups verified, capacity, access) and go/no-go point.
7. Document test evidence: environment, what was tested, results, and differences from production that limit confidence.
8. Write the backout plan: measurable trigger (for example, error rate above threshold for 10 min or step X fails), steps, time needed, data implications, and the point of no return if any.
9. Define post-implementation verification: technical checks, business smoke tests, monitoring to watch and for how long, and who confirms success.
10. Plan communication: who is notified before, during and after (users, support, stakeholders), and service desk readiness.
11. Hand off: suggest `rollback-plan` for a detailed backout, `deployment-checklist` for execution, or `technical-risk-review` for a high-risk change.

## Output format
```markdown
# RFC: <ID> – <short title>
| Field | Value |
|---|---|
| Type | standard / normal / emergency – <justification> |
| Requester / Implementer / Business owner | <...> |
| Planned window | <start–end, time zone>; conflicts checked: yes/no |
| Affected CIs and services | <...> |
| Expected downtime | <duration or none or [UNKNOWN]> |
| Risk | <Low/Medium/High> – <likelihood x impact reasoning> |

## Reason and Benefit
<why now; risk of not changing>
## Impact Assessment
- Users/services: ... Data: ... Security/compliance: ...
## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
## Implementation Plan
| # | Time | Step | Owner | Checkpoint |
|---|---|---|---|---|
## Test Evidence
- Environment / result / gaps vs production
## Backout Plan
- Trigger: ... Steps: ... Duration: ... Point of no return: ...
## Verification
- Technical: ... Business: ... Monitoring: <what, how long> ... Sign-off: <who>
## Communication
- Before / during / after: ...
## Open Questions for Approvers
1. ...
```

## Quality checklist
- [ ] The reason and the risk of not changing are explicit.
- [ ] Every implementation step has an owner and a checkpoint, with a go/no-go point.
- [ ] The backout plan has a measurable trigger, duration and point of no return.
- [ ] Risk rating is justified; test gaps versus production are stated.
- [ ] Conflicts with other changes and freeze periods were checked.
- [ ] No credentials in the RFC; missing evidence is `[UNKNOWN]`, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Backout: restore from backup" without restore time or a tested backup. State duration and last restore test.
- Rating everything Low to pass approval. Approvers then stop trusting ratings.
- Bundling unrelated changes into one RFC, which makes backout impossible to reason about.
- Declaring success when the deployment finishes, before business verification and monitoring.

## Example
Input: "Upgrade production PostgreSQL 14 to 16 this Saturday night; 3 apps depend on it; tested on staging last week."

Excerpt of output:
- Reason: version 14 end of community support approaching [ASSUMPTION: confirm date]; no change means no security patches.
- Risk: Medium – high impact (3 apps), likelihood reduced by staging test; staging data volume is 20% of production [ASSUMPTION], so upgrade duration is uncertain.
- Backout trigger: any app health check failing 15 min after cutover, or pg_upgrade step failing. Backout: switch connection back to untouched v14 primary; point of no return: first write to v16.
- Open question: are all 3 apps' drivers certified for v16?
