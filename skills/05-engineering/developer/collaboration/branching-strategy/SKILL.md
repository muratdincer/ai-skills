---
description: Recommends a branching strategy (trunk-based development, GitHub Flow, GitFlow or a documented variant) based on release cadence, number of supported versions, team size, CI maturity and compliance needs, and defines the resulting branch, merge and release rules. Use when a team sets up a repository, struggles with merge conflicts or long-lived branches, changes its release model, or must support multiple production versions.
related: pipeline-design, release-plan, semantic-versioning, deployment-strategy, working-agreement
prompt: We are 12 developers on one service, we deploy weekly but want daily, and hotfixes take too long because of our develop branch. Which branching strategy should we use?
---

# Choose a Branching Strategy

## Purpose
Select a branching model that matches how the team actually releases, and write it down as enforceable rules. The right model minimizes integration pain and lead time; the wrong one creates merge debt and slow hotfixes.

## When to use
- A new repository or team needs agreed branch rules.
- Long-lived branches cause painful merges, or hotfixes are slow.
- The release model changes (e.g., from scheduled releases to continuous delivery, or to supporting several versions).

## When not to use
- Designing the CI/CD pipeline itself. Use `pipeline-design`.
- Choosing how code reaches users in production (canary, blue-green). Use `deployment-strategy`.

## Inputs
Required:
- Release model: how often, and whether deployment is continuous, scheduled, or shipped to customers (installed/mobile/library).
- Number of versions that must be supported in parallel.

Optional, improves quality:
- Team size and number of teams in the repository, monorepo or polyrepo.
- CI duration, test automation level, feature flag capability.
- Regulatory or audit requirements (change approval, traceability).
- Current pain points.

If the release model or supported version count is missing, ask; the recommendation depends on them.

## Process
1. Profile the context: release cadence, parallel supported versions, CI speed and reliability, test automation coverage of critical paths, feature flag availability, team count.
2. Apply decision heuristics:
   - Continuous or daily deployment, one production version, reliable CI under ~15 minutes: trunk-based development with short-lived branches (< 2 days) and feature flags.
   - Frequent deployments but review via pull requests and moderate CI: GitHub Flow (main always deployable, short feature branches, deploy from main).
   - Scheduled releases with stabilization periods, or several supported versions (installed software, SDKs, mobile with forced upgrades lagging): release branches off main, or GitFlow only when parallel versions and a heavy release process are real constraints.
3. Name the risks of the chosen model in this context (e.g., trunk-based without flags exposes unfinished work; GitFlow lengthens lead time and hotfix paths).
4. Define branch types, naming (`feature/<id>-<slug>`, `release/<x.y>`, `hotfix/<id>`), maximum lifetime and who may create them.
5. Define merge rules: merge method (squash, rebase, merge commit) and why, required reviews, required checks, branch protection, linear history or not.
6. Define release and hotfix flow: where tags are cut, how fixes are forward- or back-ported (cherry-pick direction), versioning scheme.
7. Define prerequisites and a migration plan from the current model, with measurable signals (branch age, PR lead time, merge conflict frequency, hotfix lead time).
8. Summarize as a one-page policy the team can adopt in its working agreement.
9. Suggest the follow-ups the policy implies: `pipeline-design` to enforce it in CI, `semantic-versioning` and `release-plan` for release branches and tags, `working-agreement` to record it with the team.

## Output format
```markdown
# Branching Strategy: <repository/team>
## Context
| Factor | Value |
|---|---|
| Release cadence | ... |
| Supported versions in parallel | ... |
| CI duration / reliability | ... |
| Feature flags | yes/no |

## Recommendation
<model> — <why, tied to the factors above>
Rejected: <model> — <reason>

## Branch Rules
| Branch | Naming | Created from | Merges into | Max lifetime | Protection |
|---|---|---|---|---|---|

## Merge and Review Policy
- ...

## Release and Hotfix Flow
1. ...

## Prerequisites and Migration Steps
- ...

## Success Signals
- <metric> — current [UNKNOWN] — target ...
```

## Quality checklist
- [ ] The recommendation is justified by the stated release model and supported versions, not by popularity.
- [ ] At least one alternative is rejected with a reason.
- [ ] Hotfix and back-port flows are explicit.
- [ ] Branch lifetime limits and protection rules are concrete.
- [ ] Prerequisites (CI speed, flags, tests) are listed with gaps.
- [ ] Current metrics that were not provided are `[UNKNOWN]`, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Adopting GitFlow for a continuously deployed web service. The develop branch adds a second integration point and slows every fix.
- Declaring trunk-based development without feature flags or fast CI. Unfinished work leaks, and teams retreat to long-lived branches.
- Cherry-picking fixes only onto the release branch. Fix on main first and port backwards, or the bug returns in the next release.

## Example
Input: 12 developers, one service, weekly deploys aiming for daily, hotfixes slow due to `develop`, CI takes 25 minutes, no feature flags.

Excerpt of output:
- Recommendation: GitHub Flow now, moving to trunk-based once CI < 15 minutes and feature flags exist. Rejected: keeping GitFlow — only one production version is supported, so `develop` and release branches add latency without benefit.
- Hotfix flow: branch from `main`, PR with expedited review, deploy from `main`; no separate hotfix merge back to `develop`.
- Prerequisite: reduce CI to under 15 minutes; current branch age [UNKNOWN] — measure for two weeks before switching.
