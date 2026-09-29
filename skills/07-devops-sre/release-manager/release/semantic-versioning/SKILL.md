---
name: semantic-versioning
description: "Decides the next version number by applying Semantic Versioning 2.0.0 to a list of changes: classifies each change against the public API, detects hidden breaking changes, and handles 0.x, pre-release and build metadata. Use when a library, API, SDK, package or service is about to be released and someone asks which version it should be, or whether a change requires a major bump."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Decide a version number"
  related: "release-notes, changelog-entry, api-deprecation-plan, api-design-review, release-plan"
  prompt: "Current version is 2.4.1. Changes: added optional 'locale' parameter, renamed error code INVALID_TOKEN to TOKEN_INVALID, fixed rounding bug. What is the next version?"
---

# Decide a Version Number

## Purpose
Assign a version number that truthfully tells consumers whether upgrading is safe, by classifying every change against the declared public API as SemVer 2.0.0 requires.

## When to use
- A library, SDK, package, API or component with consumers is about to be released.
- The team disagrees whether a change is breaking.
- A project is moving from 0.x to 1.0.0 or introduces pre-releases (alpha, beta, rc).

## When not to use
- The notes that explain the changes to users are needed. Use `release-notes` or `changelog-entry`.
- A plan to retire an API or version is needed. Use `api-deprecation-plan`.
- The product uses calendar or marketing versions with no compatibility promise; SemVer rules do not apply, say so.

## Inputs
Required:
- Current version.
- The list of changes since that version (commits, pull requests, changelog, diff summary).

Optional, improves quality:
- Definition of the public API (exported types, endpoints, CLI flags, config keys, event schemas, database views consumers read).
- Supported runtime/platform versions, pre-release intent, project conventions.

If the current version or the change list is missing, ask. If the public API is not defined, state the assumed boundary as `[ASSUMPTION]`.

## Process
1. Establish the public API boundary; changes outside it (internals, tests, build) do not affect the number unless behavior visible to consumers changes.
2. Classify each change: MAJOR (incompatible change), MINOR (backward-compatible new functionality or a deprecation), PATCH (backward-compatible bug fix), NONE (no consumer-visible effect).
3. Hunt hidden breaking changes: renamed or removed members, new required parameters or config, changed defaults, narrowed accepted input, widened output that strict clients reject (e.g. new enum value), changed error codes or exception types, changed serialization, dropped platform or runtime support, stricter validation, transitive dependency major bumps exposed in the API.
4. Treat bug fixes that change relied-upon behavior as potentially breaking; flag them for a decision rather than silently calling them patches.
5. Take the highest classification: any MAJOR → increment major, reset minor and patch; else any MINOR → increment minor, reset patch; else PATCH.
6. Apply 0.x rules: before 1.0.0 anything may change; if the project follows the common convention of bumping minor for breaking changes in 0.x, state it explicitly.
7. Handle pre-release and build metadata: pre-release (`-alpha.1`, `-rc.2`) has lower precedence than the release; build metadata (`+build.5`) is ignored in precedence.
8. Recommend mitigations if a MAJOR bump is unwanted: keep the old member deprecated, add rather than rename, make the new parameter optional.
9. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `release-notes` or `changelog-entry` to document the changes, or `api-deprecation-plan` when removals are planned.

## Output format
```markdown
# Version Decision: <component>
Current: <x.y.z> → **Recommended: <x.y.z>**

## Public API Boundary
<what counts as public; [ASSUMPTION] if not given>

## Change Classification
| Change | Classification | Reason |
|---|---|---|

## Rationale
<highest classification wins; key breaking change(s)>

## Alternatives to Avoid a Major Bump (if relevant)
- ...

## Open Questions
```

## Quality checklist
- [ ] The public API boundary is stated or marked as an assumption.
- [ ] Every change is classified with a reason tied to consumer impact.
- [ ] Hidden breaking changes (error codes, defaults, enums, platform support) were checked.
- [ ] Reset rules were applied correctly (minor and patch to 0 on major; patch to 0 on minor).
- [ ] Pre-release and build metadata follow SemVer 2.0.0 precedence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Calling a rename "refactoring" and releasing it as a patch. If consumers reference the name, it is breaking.
- Treating the version as marketing ("big release, so 3.0"). The number encodes compatibility, not size.
- Adding an enum value in a minor without checking that consumers use exhaustive matching or strict deserialization.

## Example
Input: "2.4.1 → added optional 'locale' parameter; renamed error code INVALID_TOKEN to TOKEN_INVALID; fixed rounding bug."

Excerpt of output:
| Change | Classification | Reason |
|---|---|---|
| Optional `locale` parameter | MINOR | New backward-compatible capability |
| Error code rename | MAJOR | Clients matching on `INVALID_TOKEN` break |
| Rounding fix | PATCH | `[CONFIRM]` no consumer relies on the old rounding |

Recommended: **3.0.0**. Alternative: return both codes during a deprecation period and ship **2.5.0**.
