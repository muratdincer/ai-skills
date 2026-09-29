---
description: Writes changelog entries in the Keep a Changelog format (Added, Changed, Deprecated, Removed, Fixed, Security) from commits, merged pull requests or a change list, written for the people who consume the software, with breaking changes and migration steps called out. Use when preparing a release section, updating the Unreleased section after a merge, or turning noisy commit history into a readable change history.
related: commit-message, release-notes, semantic-versioning, pull-request-description, app-store-release-notes
prompt: Turn these merged PR titles into a changelog entry for version 2.4.0 of our client library.
---

# Write a Changelog Entry

## Purpose
Give consumers of a library, service or application a curated, human-readable record of notable changes per version, so they can decide whether and how to upgrade. A changelog is for the reader, not a dump of commit history.

## When to use
- A version is about to be released and its changelog section must be written.
- A pull request was merged and the Unreleased section needs an entry.
- A project has only commit history and needs a readable change history.

## When not to use
- Announcing a release to end users with context and highlights. Use `release-notes`.
- Short, store-limited text for a mobile app update. Use `app-store-release-notes`.
- Deciding the version number itself. Use `semantic-versioning`.

## Inputs
Required:
- The changes: commits, merged pull request titles and descriptions, or a change list.

Optional, improves quality:
- Target version and release date; the previous version.
- The existing changelog (to match style, links and wording).
- Audience (library consumers, API clients, operators) and issue tracker links.

If no changes are provided, ask for them. If the version or date is unknown, write the entry under `[Unreleased]` or with `[TBD]`.

## Process
1. Collect all changes since the previous version and drop pure internal noise (formatting, test-only, CI tweaks, refactorings with no observable effect) unless the audience is contributors.
2. Merge related items: several commits for one feature become one entry.
3. Classify each entry into exactly one Keep a Changelog section: Added (new capabilities), Changed (changes to existing behavior), Deprecated (still works, will be removed), Removed, Fixed (bugs), Security (vulnerabilities). When a change is labeled wrongly in commits (e.g., a behavior change as `refactor`), classify by effect and note it.
4. Write each entry from the consumer's point of view: what they can now do or what behaves differently, in one line, starting with a verb or the affected feature. Avoid internal class names unless they are the public API.
5. Identify breaking changes (removed or renamed public API, changed defaults, schema or config changes, stricter validation, changed error codes) and mark them `**BREAKING:**` with a one- or two-line migration step.
6. For Security entries, state affected versions and severity reference (e.g., CVE ID if one exists) without exploit details.
7. Add references: issue or pull request numbers as links, when available; do not invent numbers.
8. Order sections as Keep a Changelog prescribes and entries within a section by importance to the consumer.
9. Put the version header in the format `## [x.y.z] - YYYY-MM-DD` (ISO 8601 date) and add or update the comparison link at the bottom if the existing changelog uses them.
10. Check the version against the changes: breaking changes need a major bump, new features a minor, fixes a patch (for SemVer projects). If they disagree, flag it and suggest `semantic-versioning`; for a user-facing announcement, suggest `release-notes`.

## Output format
```markdown
## [<x.y.z> | Unreleased] - <YYYY-MM-DD | TBD>
### Added
- <consumer-facing change> ([#<ref>](<link>))
### Changed
- **BREAKING:** <what changed>. Migration: <step>.
### Deprecated
- <item> — use <replacement>; removal planned in <version or [TBD]>.
### Removed
### Fixed
### Security
- <vulnerability fixed, affected versions, reference>
```
Omit empty sections.

## Quality checklist
- [ ] Every entry describes an effect a consumer can observe, not an implementation step.
- [ ] Each entry sits in exactly one correct section; empty sections are omitted.
- [ ] Every breaking change is marked and has a migration step.
- [ ] No references, versions or dates are invented; unknowns are `[TBD]`.
- [ ] The version number is consistent with the kinds of changes, or the mismatch is flagged.
- [ ] Internal noise (CI, formatting, test-only changes) is excluded for external audiences.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Pasting commit subjects verbatim ("fix typo", "wip", "address review"). Curate and rewrite for the reader.
- Hiding a breaking default change under Fixed. Anything that can break an upgrade goes under Changed or Removed with a BREAKING marker.
- Writing "various bug fixes and improvements". List the notable ones or say nothing.

## Example
Input: PRs "#212 add retry option to HttpClient", "#215 refactor: timeout default 30s -> 10s", "#218 fix NPE when header missing", "#219 bump test deps".

Weak: "- Refactor timeout default. - Bump test deps. - Fix NPE."

Strong excerpt:
```markdown
## [3.0.0] - [TBD]
### Added
- Configurable retry for transient HTTP failures via `retry` option ([#212]).
### Changed
- **BREAKING:** Default request timeout reduced from 30 s to 10 s. Migration: set `timeout: 30s` to keep the previous behavior ([#215]).
### Fixed
- Requests no longer fail with a null reference when an optional header is missing ([#218]).
```
Note: #215 was labeled `refactor` but changes behavior; the version must be a major bump, not 2.4.0.
