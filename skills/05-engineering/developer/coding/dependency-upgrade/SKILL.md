---
description: "Plans and executes a library, framework or runtime upgrade: reads release notes and migration guides between the current and target versions, lists breaking changes that actually affect the codebase, orders migration steps, handles transitive conflicts and defines verification and rollback. Use when a dependency must be upgraded for security, end of support or a needed feature, when an automated update pull request fails, or when someone asks how to move from version X to Y."
related: "dependency-vulnerability-review, semantic-versioning, refactoring, changelog-entry, pull-request-description"
prompt: "Plan the upgrade of our web framework from major version 6 to 8; here is the dependency manifest and the list of features we use."
---

# Upgrade a Dependency

## Purpose
Move a dependency to a target version with a known, bounded impact: every relevant breaking change handled, the build and tests green at each step, and a way back if production disagrees.

## When to use
- A vulnerability, end of support or needed feature forces an upgrade.
- An automated dependency update fails to build or breaks tests.
- A major version jump (framework, ORM, runtime, SDK) needs a migration plan.

## When not to use
- Deciding whether a reported vulnerability is exploitable and urgent. Use `dependency-vulnerability-review`.
- Choosing between different libraries. Use `technology-selection`.
- Restructuring code without a version change. Use `refactoring`.

## Inputs
Required:
- Dependency name, current version, target version (or "latest supported").
- The dependency manifest or lock file, or a description of how the dependency is used.

Optional, improves quality:
- Release notes and migration guides the user can paste, build and test output, runtime and platform versions, other dependencies that pin it.

Do not recite breaking changes from memory as fact. Ask the user to paste the relevant release notes, or mark each recalled change `[VERIFY in release notes]`.

## Process
1. Establish the version span and the reason (security, end of support, feature); check versioning scheme (SemVer or not) and whether intermediate majors must be stepped through.
2. Collect changes across the span: breaking changes, deprecations, new minimum runtime or platform versions, changed defaults, removed transitive dependencies.
3. Map each change to the codebase: search points (APIs, config keys, annotations, build plugins) and mark each Affected, Not affected or Unknown.
4. Check the dependency graph: peer or transitive conflicts, other packages that require a compatible version, duplicate versions after resolution.
5. Order the migration: prerequisite upgrades (runtime, build tool), fix deprecations on the old version first, then bump, then adapt to removals, then adopt new defaults deliberately.
6. Keep each step buildable and testable; one dependency bump per commit unless they must move together.
7. Identify behavior changes tests may not catch: default timeouts, serialization, date/time handling, security defaults, logging format, performance.
8. Define verification: full test suite, targeted tests for affected areas, smoke test in a production-like environment, comparison of key metrics after release.
9. Define rollback: revert commit and redeploy, lock file restore, data or config migrations that are one-way and how to handle them.
10. List follow-ups: remove compatibility shims, adopt new features later, update documentation and changelog.
11. If the goal continues, suggest `pull-request-description` to present the change, `changelog-entry` for release notes, or `dependency-vulnerability-review` if the trigger was a vulnerability.

## Output format
```markdown
# Dependency Upgrade: <name> <current> → <target>
Reason: <security/EOL/feature> · Scheme: <SemVer?> · Stepping: <direct / via X>

## Change Impact
| Change | Source | Affected? | Where | Action |

## Dependency Graph Issues
- ...

## Migration Steps
| # | Step | Verification | Commit |

## Behavior Changes to Watch
- ...

## Rollback
- ...

## Follow-ups and Open Questions
- ...
```

## Quality checklist
- [ ] Every breaking change cites a source (release notes, guide) or is marked `[VERIFY in release notes]`.
- [ ] Each change is mapped to the codebase as Affected, Not affected or Unknown.
- [ ] Steps are ordered so the build stays green after each one.
- [ ] Silent behavior changes (defaults, serialization, time, security) are listed.
- [ ] Rollback covers one-way migrations explicitly.
- [ ] Unknown impact is listed as open questions, not assumed safe; every inference is labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Jumping several majors at once and debugging a pile of failures with no idea which change caused which.
- Trusting "tests pass" when the suite does not cover changed defaults such as timeouts or JSON casing.
- Upgrading while leaving deprecated calls in place, then being blocked at the next major.

## Example
Input: "Upgrade HTTP client library 4.x to 5.x; we use it in 12 places, custom retry handler, connection pool config."

Excerpt of output:
| Change | Source | Affected? | Where | Action |
|---|---|---|---|---|
| Retry handler interface replaced | `[VERIFY in release notes]` | Affected | `RetryConfig.kt` | Port to new retry strategy API, keep attempt count and backoff |
| Default connect timeout changed | Migration guide, "Defaults" | Unknown | All clients | Set timeouts explicitly before bump to keep behavior |
