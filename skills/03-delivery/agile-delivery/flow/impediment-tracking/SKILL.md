---
name: impediment-tracking
description: "Builds and maintains an impediment log: captures each blocker with the blocked work, impact, owner and next action, classifies it by what is needed to remove it (team, other team, management, external), applies an escalation ladder with time thresholds, and surfaces recurring systemic causes. Use when a team reports blockers in a daily sync, work is stuck waiting on others, or someone asks to organize, escalate or report on open impediments."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Track impediments"
  related: "daily-sync-summary, escalation-message, cross-team-dependency-board, raid-log, retrospective-facilitation"
  prompt: "Here are the blockers from this week's syncs: test environment down since Tuesday, waiting for the security team's approval on the firewall rule, and the product owner hasn't answered on the refund rules. Organize and tell me what to escalate."
---

# Track Impediments

## Purpose
Make every blocker visible with a clear owner and next action, escalate it at the right level before it silently eats the iteration, and turn repeat blockers into systemic improvements instead of recurring firefighting.

## When to use
- Blockers come up in daily syncs or chats and need to be captured consistently.
- Work items are waiting on another team, a decision or an external party.
- A weekly or iteration-level impediment report or escalation is needed.

## When not to use
- Planning and negotiating dependencies before work starts. Use `cross-team-dependency-board`.
- Project-level risks, assumptions and issues log for governance. Use `raid-log`.
- Writing the escalation message itself. Use `escalation-message` after this skill decides what to escalate.

## Inputs
Required:
- The blockers as described (sync notes, chat messages or a list), with the work they block where known.

Optional, improves quality:
- Date each blocker was raised, the existing impediment log.
- Iteration goal or release milestones, to judge impact.
- Escalation paths and contacts (team lead, other team leads, management, vendor manager).

If the blocked work or date raised is not stated, record `[UNKNOWN]` and add it to the open questions; do not guess.

## Process
1. Normalize each blocker into one entry: what is blocked (item IDs), what is blocking it, since when, and the observable effect. Rewrite vague entries ("waiting on infra") into specific ones or mark what is missing.
2. Separate impediments from ordinary tasks and risks: an impediment already stops or slows committed work; a risk might in the future (send to `raid-log`); a task the team can do itself is just work.
3. Classify by resolver: within team, other team, product/business decision, management/organization, external vendor or customer.
4. Assess impact: which committed or goal-critical items are affected, days lost so far, and the date by which it becomes critical. Rate High/Medium/Low with a one-line reason.
5. Assign one owner (person or role driving resolution, not necessarily the resolver) and a concrete next action with a date.
6. Apply the escalation ladder with thresholds unless the team has its own: same day inside the team; after 1 working day to the other team's lead; after 2-3 working days or when goal-critical, to management/sponsor `[default, adjust to team policy]`. Mark which items must escalate now.
7. For each escalation, state the specific ask (decision, resource, access, date) and the cost of delay; hand the drafting to `escalation-message`.
8. Record workarounds and their cost or risk separately; a workaround does not close the impediment.
9. Close entries only when the blocked work can proceed; record resolution date and actual days lost.
10. Look for patterns across entries (same team, same environment, same kind of decision) and list systemic causes as candidates for the next retrospective.
11. Suggest `retrospective-facilitation` for systemic causes, `escalation-message` for escalations, and `daily-sync-summary` to keep the log current.

## Output format
```markdown
# Impediment Log – <team>, updated <date>

| ID | Blocked work | Impediment | Raised | Resolver type | Impact (H/M/L) | Owner | Next action – date | Escalation level | Status |
|---|---|---|---|---|---|---|---|---|---|

## Escalate Now
| ID | To whom (role) | Specific ask | Cost of delay |
|---|---|---|---|

## Workarounds in Place
- <ID>: <workaround> – <cost/risk>

## Resolved Since Last Update
- <ID>: resolved <date>, days lost <n>

## Recurring Patterns (for retrospective)
- ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Each entry names the blocked work, a single owner and a dated next action.
- [ ] Risks and ordinary tasks are not logged as impediments.
- [ ] Escalation decisions follow stated thresholds and include a specific ask.
- [ ] Impact is tied to committed or goal-critical work, with unknowns marked.
- [ ] Recurring causes are identified, not only individual blockers.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Logging blockers without an owner. "The team" owns nothing; name a person or role who drives it.
- Waiting too long to escalate out of politeness. Escalation with a clear ask is a service, not an accusation.
- Closing an impediment because a workaround exists. Track the workaround's cost and keep the root blocker open.

## Example
Input: test environment down since Tuesday; firewall rule awaiting security approval; product owner has not answered on refund rules.

Excerpt of output:
| ID | Blocked work | Impediment | Resolver type | Impact | Next action – date | Escalation level |
|---|---|---|---|---|---|---|
| IMP-1 | 3 stories in Test | Test environment down since Tue | Other team (platform) | High – goal-critical | Owner to call platform lead today | Management now (3 days) |
| IMP-2 | PAY-44 | Firewall rule awaiting approval | Other team (security) | Medium | Request decision date by Thu | Other team lead |
- Weak entry: "Infra problems." Strong entry: "Test environment unavailable since Tue 09:00; blocks PAY-41/42/45 verification."
