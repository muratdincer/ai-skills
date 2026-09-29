---
description: Builds and runs a go/no-go checklist for a mobile app release covering versioning, build and signing, permissions and privacy declarations, store listing and assets, quality gates, backend and forced-update compatibility, staged rollout, monitoring and rollback, and reports each item as done, open or blocked with evidence. Use when an iOS or Android build is being prepared for store submission or phased rollout, or when a team wants a repeatable mobile release checklist.
related: app-store-release-notes, release-quality-gate, deployment-checklist, rollback-plan, go-no-go
prompt: We're submitting version 4.2.0 of our Android and iOS apps next Tuesday. It adds location-based offers. Run the mobile release checklist with me.
---

# Run a Mobile Release Checklist

## Purpose
Make sure a mobile build can be submitted, approved, rolled out and, if needed, contained without surprises. Mobile releases cannot be rolled back like a server deployment, so the checklist front-loads what stores, users and old app versions will encounter.

## When to use
- An iOS or Android build is being prepared for store submission.
- A phased or staged rollout is planned and needs criteria to advance or halt.
- The team wants a reusable checklist tailored to its app.

## When not to use
- Writing the "What's new" text. Use `app-store-release-notes`.
- Server-side deployment steps. Use `deployment-checklist`.
- The formal cross-team release decision meeting. Use `go-no-go`.

## Inputs
Required:
- App name, target platforms, version being released, and the list of changes (or release scope).

Optional, improves quality:
- Planned submission and release dates, rollout strategy, feature flags involved.
- New permissions, SDKs or data collection added in this version.
- Minimum supported OS and app versions, backend changes shipping alongside.
- The team's existing checklist or previous release issues.

If the change list is missing, ask for it, since permissions, privacy declarations and compatibility depend on it. Items the user cannot confirm stay "Open", never "Done".

## Process
1. Confirm scope and platforms; flag changes with store-review risk (new permissions, background location, payments, account creation without deletion, user-generated content, health or financial data).
2. Versioning: user-facing version follows the team's scheme (e.g., SemVer) and build numbers increase monotonically per platform; release branch or tag is created; the version is consistent across platforms if the team requires it.
3. Build and signing: release configuration (no debug flags, logging level, test endpoints removed), correct signing identity and certificates not near expiry, reproducible build from CI, symbol and mapping files uploaded for crash symbolication.
4. Permissions and privacy: each new permission has a purpose string that matches actual use and is requested in context; store privacy declarations (data collected, purpose, linked to user, tracking) are updated for new SDKs; personal data is minimized and account deletion is available where required by store policy or law (KVKK/GDPR).
5. Store listing: release notes, screenshots for changed screens, age rating answers, in-app purchase and subscription metadata, localized text, review notes and demo account for the review team (credentials shared through the store's reviewer channel, never in the checklist).
6. Quality gates: regression and smoke tests on the minimum and latest supported OS versions and representative devices, accessibility spot-check, crash-free rate of the beta/internal track, performance (startup time, app size increase) against budget.
7. Compatibility: backend changes are backward compatible with the versions still in use; forced or soft update rules are set if old versions will break; data or schema migrations on device are tested from the oldest supported upgrade path.
8. Feature flags and remote config: new features default safely, flags can be turned off without a new build, kill switch exists for risky features.
9. Rollout plan: staged percentages and hold periods, metrics that gate each step (crash-free users, ANR or hang rate, key funnel conversion, support tickets), who can halt the rollout, and timing that avoids store review and weekend gaps.
10. Containment and rollback: since installed builds cannot be withdrawn, define the halt procedure, flag-off options, hotfix path with expedited review if needed, and user communication.
11. Report every item as Done (with evidence), Open (owner, due) or Blocked, and give a go/no-go recommendation. Suggest `app-store-release-notes` for the store text, `rollback-plan` for a detailed containment plan, or `go-no-go` for the formal decision.

## Output format
```markdown
# Mobile Release Checklist: <app> v<version> (<platforms>)
Submission: <date> · Rollout start: <date> · Release owner: <name or [UNKNOWN]>

## Store-Review Risks
- ...

| Area | Item | Platform | Status (Done/Open/Blocked) | Evidence / Owner / Due |
|---|---|---|---|---|
| Versioning | ... | | | |
| Build & signing | ... | | | |
| Permissions & privacy | ... | | | |
| Store listing | ... | | | |
| Quality gates | ... | | | |
| Compatibility | ... | | | |
| Flags & config | ... | | | |

## Rollout Plan
| Step | Audience % | Hold | Advance if | Halt if |
|---|---|---|---|---|

## Containment
- Halt: ... · Flag-off: ... · Hotfix path: ... · User comms: ...

## Recommendation
<Go / Go with conditions / No-go> — <reasons, open blockers>
```

## Quality checklist
- [ ] Every new permission, SDK or data type is traced to a purpose string and an updated privacy declaration.
- [ ] Backward compatibility with older installed versions and the upgrade path are explicitly addressed.
- [ ] Rollout steps have measurable advance and halt criteria and a named decision owner.
- [ ] No item is marked Done without evidence; unconfirmed items stay Open.
- [ ] No credentials, signing keys or reviewer passwords appear in the output.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating the release like a server deploy with instant rollback. Old builds stay on devices; plan flags, forced-update rules and hotfix paths before release.
- Adding an SDK that collects data without updating privacy declarations, leading to rejection or policy violations.
- Releasing to 100% at once on a Friday, so a crash spike runs through the weekend without anyone able to halt it.

## Example
Input: "v4.2.0, Android and iOS, adds location-based offers, submit Tuesday."

Excerpt of output:
- Store-review risk: new location permission. Use while-in-use only `[ASSUMPTION]`; background location would need separate justification.

| Area | Item | Platform | Status | Evidence / Owner / Due |
|---|---|---|---|---|
| Permissions & privacy | Location purpose string explains offers near the user | iOS, Android | Open | Mobile lead, Mon |
| Permissions & privacy | Privacy declaration adds "precise location, used for app functionality" | Both stores | Open | Product + legal, Mon |
| Compatibility | Offers API returns empty list, not error, for v4.1 clients | Backend | Done | Contract test run link |
| Flags & config | `location_offers` remote flag default off, enable per rollout step | Both | Done | Config screenshot |
