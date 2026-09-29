---
name: release-plan
description: "Writes a release plan that fixes the release contents, schedule with freeze and cut-over points, named owners, dependencies, communication and the rollback decision point. Use when a release spans several teams, components or environments, needs a change window, or when someone asks for a release schedule, cut-over plan or release runbook overview."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Write a release plan"
  related: "deployment-checklist, rollback-plan, go-no-go, release-notes, change-request-rfc"
  prompt: "Write a release plan for version 4.2: three services, a database migration and a mobile app update, target production date next Thursday night."
---

# Write a Release Plan

## Purpose
Give everyone involved one agreed view of what ships, when each step happens, who owns it and how the release is stopped or reversed, so the release is coordinated rather than improvised on the night.

## When to use
- A release bundles changes from several teams, services, databases or client apps.
- A release needs a change window, customer notice or external approval.
- Past releases slipped or failed because of missed dependencies or unclear ownership.

## When not to use
- Only the step-by-step checks for the deployment itself are needed. Use `deployment-checklist`.
- The question is how a single service reaches users (canary, blue-green). Use `deployment-strategy`.
- The question is planning which features go into upcoming releases over months. Use `release-planning`.

## Inputs
Required:
- Release identifier and the list of changes or work items included.
- Target date or window for production.

Optional, improves quality:
- Components and environments affected, deployment order constraints, database or data migrations.
- Team and owner names, approvers, change-management process.
- Business events to avoid (campaigns, month-end close, peak hours), customer commitments.
- Previous release retrospectives or incidents.

If the change list or the target window is missing, ask. Unknown owners or dates become `[TBD]` with an open question, never invented names.

## Process
1. Build the content inventory: each change with component, owner, risk (High/Medium/Low with reason), feature-flag status and whether it touches data or public contracts.
2. Identify dependencies and ordering: schema before code, backend before client, provider before consumer; mark external dependencies (vendors, app-store review, partner teams).
3. Separate deploy from release: list which changes are dark-launched behind flags and when they are switched on.
4. Build the schedule backwards from the production window: code freeze, release candidate cut, test/staging sign-off, go/no-go, deployment steps, verification, hypercare end.
5. Check the window against business calendar and staffing: no conflict with peak load or critical business events; key owners available; on-call aware.
6. Assign a single release owner (decision authority) and one named owner per step; add backup owners for critical steps.
7. Define entry criteria for go/no-go and the point of no return (e.g. after an irreversible migration) with the rollback decision deadline before it.
8. Plan communication: who is told what and when (internal teams, support, customers, status page), including the "done" and "rolled back" messages.
9. List risks with mitigation and the rollback approach per component; reference the rollback plan.
10. Define hypercare: duration, monitoring focus, owners, exit criteria.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `deployment-checklist` for the execution checks, `rollback-plan` for the undo path, `go-no-go` for the decision meeting, or `release-notes` for the audience-facing summary.

## Output format
```markdown
# Release Plan: <release id>
| Field | Value |
|---|---|
| Release owner | <name or [TBD]> |
| Production window | <date, time, timezone> |
| Change record | <id or [TBD]> |
| Point of no return | <step> – rollback decision by <time> |

## Contents
| Change | Component | Owner | Risk | Flag | Data/contract impact |

## Dependencies and Order
1. ...

## Schedule
| When | Milestone / step | Owner | Exit criterion |

## Go/No-Go Criteria
- ...

## Communication
| When | Audience | Channel | Message | Owner |

## Risks and Rollback
| Risk | Mitigation | Rollback approach |

## Hypercare
<duration, monitoring focus, exit criteria>

## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every change has an owner and a risk rating with reason; unknown owners are `[TBD]`.
- [ ] Deployment order respects schema, API and client compatibility.
- [ ] The point of no return is explicit and the rollback decision deadline precedes it.
- [ ] The window was checked against business events and staffing, or the check is an open question.
- [ ] Communication covers success and rollback outcomes, not only the start.
- [ ] No dates, names or durations were invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A schedule with no slack between staging sign-off and production. Build the schedule backwards and keep buffer for a failed candidate.
- Mobile app changes planned like server releases. Store review time and old client versions in the field require backward-compatible APIs.
- Several people "owning" the release. Name one decision owner; others own steps.

## Example
Input: "Release 4.2: order, payment and notification services, a column split in the orders table, iOS/Android update. Production Thursday 22:00."

Excerpt of output:
- Order: expand migration (add new columns, dual write) → services → mobile store submission; contract step deferred to 4.3 `[ASSUMPTION]`.
- Point of no return: none in this release because the migration is additive; rollback remains possible through hypercare.
- Open question: Has the mobile build been submitted early enough for store review before Thursday? Owner: mobile lead `[TBD]`.
