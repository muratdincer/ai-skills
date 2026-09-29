---
description: "Writes an error budget policy that states, for defined budget consumption thresholds, what the development and operations teams must do (release restrictions, reliability work, postmortem requirements), who decides exceptions, and how disputes are escalated. Use when SLOs exist but have no consequences, when feature pressure keeps overriding reliability, or when someone asks what happens when the error budget is exhausted."
related: "slo-definition, alert-design, postmortem, release-quality-gate, go-no-go"
prompt: "Our checkout SLO is 99.9% over 28 days and we burned 80% of the budget in the first week. Write an error budget policy that the product and engineering leads can sign."
---

# Write an Error Budget Policy

## Purpose
Turn SLOs into an agreed decision rule that balances feature velocity and reliability, signed in advance by product and engineering, so the conversation during a bad month is about executing the policy, not negotiating it.

## When to use
- SLOs exist but nobody changes behavior when they are missed.
- Product and engineering repeatedly argue about freezing releases after incidents.
- A service is being onboarded to SRE or platform support that requires a budget policy.

## When not to use
- The SLIs and SLOs themselves are not yet defined. Use `slo-definition`.
- The need is paging rules for fast burn. Use `alert-design`.
- The question is a one-off ship decision for a specific release. Use `go-no-go`.

## Inputs
Required:
- The SLOs with targets and windows.
- The teams involved: service owners, product owner, operations/SRE, decision makers.

Optional, improves quality:
- Current and historical budget consumption, recent incidents.
- Release cadence and deployment mechanism (to judge what "freeze" means in practice).
- Organization escalation path, existing change policies, dependency SLOs.

If there are no SLOs, stop and suggest `slo-definition`. Missing names or roles become `[TBD]`.

## Process
1. State the policy's goals and scope: services, SLOs, window, and the principle that budget exists to be spent on change.
2. Define consumption thresholds (e.g. 50%, 75%, 100% of budget in the window) and a fast-burn condition, each with mandatory actions.
3. For each threshold specify actions for development (release restrictions, required reviews, only reliability or security fixes), operations (extra monitoring, capacity), and product (reprioritize backlog toward reliability items).
4. Define what "release freeze" allows: security patches, fixes that reduce burn, regulatory changes; define who approves exceptions.
5. Attribute burn: exclude or separately handle budget consumed by dependencies outside the team's control, planned maintenance, or misconfigured SLI; state how attribution disputes are resolved.
6. Set the postmortem requirement: any single incident consuming more than a stated share of budget `[TBD]` requires a postmortem with actions prioritized in the next iteration.
7. Define exit criteria for restrictions (budget recovered, actions complete) and the case of persistently unused budget (consider tighter SLO or faster releases).
8. Define escalation for disagreement and the signatories; set a review cadence for the policy itself.
9. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `alert-design` for burn-rate paging, `postmortem` for budget-consuming incidents, or `release-quality-gate` to encode the release restriction.

## Output format
```markdown
# Error Budget Policy: <service(s)>
SLOs covered: <list> · Window: <N days> · Effective: <date> · Review: <cadence>
Signatories: <product lead>, <engineering lead>, <SRE/ops lead> ([TBD] if unknown)

## Goals and Scope
## Thresholds and Actions
| Budget consumed | Development | Operations | Product | Approver of exceptions |
|---|---|---|---|---|
| ≥ 50% | ... | ... | ... | ... |
| ≥ 75% | ... | ... | ... | ... |
| ≥ 100% | ... | ... | ... | ... |
| Fast burn | ... | ... | ... | ... |

## Allowed During Freeze
## Burn Attribution and Exclusions
## Postmortem Requirement
## Exit Criteria
## Escalation and Disputes
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every threshold has concrete, verifiable actions for each team, not "be careful".
- [ ] Freeze exceptions and their approver are defined.
- [ ] Attribution of dependency-caused burn is addressed.
- [ ] Exit criteria and an unused-budget rule exist.
- [ ] Signatories include both product and engineering decision makers.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A policy written by SRE alone. Without product sign-off, it is overridden at the first deadline.
- Treating 100% as the only trigger. Earlier thresholds let the team act before a freeze.
- Punitive framing. The budget is a tool for choosing risk; the policy should never assign blame.

## Example
Input: "Checkout 99.9% / 28 days; 80% burned in week one after two bad deploys."

Excerpt of output:
| Budget consumed | Development | Product | Approver of exceptions |
|---|---|---|---|
| ≥ 75% | Only changes behind flags with canary; rollback rehearsed for each release | Top reliability items from the two postmortems enter the next iteration | Engineering lead |
| ≥ 100% | Freeze except security and burn-reducing fixes until budget recovers or actions complete | Feature commitments re-planned | Product + engineering lead jointly |
