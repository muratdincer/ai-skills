---
name: modernization-assessment
description: "Assesses a legacy system across business fit, technical health, operational risk and change drivers, then evaluates the 7R options (retire, retain, rehost, relocate, replatform, repurchase, refactor/re-architect) with relative effort, value and risk, and recommends a path with decision criteria and first steps. Use when a legacy application is under pressure (end of support, cost, skills, scalability, compliance), when leadership asks \"what should we do with system X?\", or before committing budget to a migration or rewrite."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "Assess a legacy system"
  related: "legacy-code-comprehension, tech-debt-assessment, migration-strategy, build-vs-buy, application-portfolio-assessment"
  prompt: "Assess our 15-year-old .NET Framework order management monolith on-premises. Support for its OS ends next year and only two people know it. What are our options?"
---

# Assess a Legacy System

## Purpose
Turn a vague "this system is old" feeling into a defensible modernization decision: a clear picture of why change is needed, which 7R options are viable, what each costs and returns in relative terms, and which one to start with.

## When to use
- A system faces a hard driver: end of vendor or platform support, key-person risk, compliance gap, cost growth, or inability to scale or change.
- Leadership needs options for one legacy application before budgeting.
- A rewrite has been proposed and needs to be challenged against cheaper options.

## When not to use
- Many applications must be ranked for a portfolio decision. Use `application-portfolio-assessment`.
- The option is chosen and the migration must be sequenced. Use `migration-strategy`.
- The question is only which code-level debt to pay down. Use `tech-debt-assessment`.

## Inputs
Required:
- System description: purpose, users, main technologies and integrations, and the driver for change.

Optional, improves quality:
- Architecture or deployment diagrams, code metrics, incident and change history, running cost.
- Business roadmap for the capability, target platform standards, available skills and budget envelope.
- Data volumes, regulatory constraints, contracts and licenses.

If the driver for change is unknown, ask; without it no option can be ranked. Ask at most five questions; list the rest as open questions.

## Process
1. State the drivers and the deadline behind each (e.g., "OS support ends Q3" `[confirm]`); separate hard drivers (must act) from soft drivers (would be nice).
2. Assess business fit: how critical the capability is, whether it differentiates or is commodity, expected change rate, and whether a standard product exists.
3. Assess technical health: platform currency, architecture (monolith boundaries, coupling, shared database), code quality signals, test coverage, build and deploy automation, documentation, key-person dependency.
4. Assess operational risk: incidents, security vulnerabilities, scalability limits, recovery capability, license and support exposure.
5. Map dependencies: upstream/downstream integrations, data ownership, batch jobs, reports, and hidden consumers of the database.
6. Evaluate each 7R option for feasibility; drop infeasible ones with a one-line reason. For viable ones rate relative effort, value, risk and time to first benefit (Low/Medium/High), never inventing costs.
7. Consider incremental paths (strangler fig, extracting the most volatile capability first) before big-bang rewrites; explain why a rewrite is or is not justified.
8. Recommend one primary option (and a fallback), with decision criteria that would change it, and the preconditions (skills, funding, freeze windows).
9. Propose first steps that reduce uncertainty: a time-boxed spike, dependency discovery, test safety net, data profiling.
10. Label every inference `[ASSUMPTION]`, collect risks and open questions, and if the goal continues suggest `migration-strategy` to plan the chosen path, `build-vs-buy` if repurchase is viable, or `legacy-code-comprehension` to reduce knowledge risk.

## Output format
```markdown
# Modernization Assessment: <system>
Drivers: <hard> / <soft> · Deadline: <date or [UNKNOWN]>

## Current State
| Dimension | Finding | Rating (Good/Fair/Poor) | Evidence |
|---|---|---|---|
| Business fit | ... | | |
| Technical health | ... | | |
| Operational risk | ... | | |
| Dependencies | ... | | |

## Options (7R)
| Option | Feasible? | Effort | Value | Risk | Time to benefit | Notes |
|---|---|---|---|---|---|---|

## Recommendation
- Primary: ... because ...
- Fallback: ...
- Would change if: ...
- Preconditions: ...

## First Steps
1. ...

## Assumptions, Risks and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every option rating is tied to evidence from the input or labeled `[ASSUMPTION]`; no cost figures are invented.
- [ ] All seven options are considered, and dropped ones have a reason.
- [ ] Hard drivers and their deadlines determine the recommendation's timing.
- [ ] Hidden dependencies (shared database, batch jobs, reports) are addressed or listed as open questions.
- [ ] The recommendation states what would change it.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Defaulting to a full rewrite because the code is unpleasant. Rewrites lose embedded business rules; compare with replatform and incremental refactoring first.
- Ignoring the data: the database is often the real monolith, shared by reports and other systems.
- Treating key-person risk as a technical issue only. Capture knowledge before any option starts.

## Example
Input: .NET Framework order monolith on Windows Server with end-of-support next year, shared SQL database used by finance reports, two maintainers.

Excerpt of output:
| Option | Feasible? | Effort | Value | Risk | Time to benefit | Notes |
|---|---|---|---|---|---|---|
| Rehost | Yes | Low | Low | Low | Short | Removes OS deadline only; debt stays |
| Replatform | Yes | Medium | Medium | Medium | Medium | Move to supported runtime and containers; test safety net needed first |
| Refactor (strangler) | Yes | High | High | Medium | Long | Extract pricing first (highest change rate) `[ASSUMPTION]` |

Primary: rehost now to meet the support deadline, then strangler refactoring; would change if a standard order product covers most required flows.
