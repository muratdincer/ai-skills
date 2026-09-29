---
description: "Writes release notes from a change list, commits or work items, grouped into new features, improvements, fixes, breaking changes, deprecations and known issues, and written for a named audience (end users, administrators, API consumers or internal teams). Use when a version is about to ship and users, customers or support need to know what changed and what they must do."
related: "changelog-entry, semantic-versioning, release-announcement, app-store-release-notes, release-plan"
prompt: "Turn this list of 23 merged tickets into release notes for our customers' administrators for version 3.8."
---

# Write Release Notes

## Purpose
Tell a specific audience what changed in a release, what it means for them and what action they must take, so that upgrades are safe and support is not flooded with avoidable questions.

## When to use
- A version is about to ship and there is a raw change list (tickets, commits, pull request titles).
- A release contains breaking changes, migrations or deprecations that users must act on.
- Different audiences (customers, admins, API consumers, support) need different notes from the same release.

## When not to use
- A developer-facing, per-change log in the repository is needed. Use `changelog-entry`.
- A marketing-style launch message is needed. Use `release-announcement`.
- Store listing text for a mobile app is needed. Use `app-store-release-notes`.

## Inputs
Required:
- The list of changes (tickets, commits, pull requests or a summary).
- The target audience.

Optional, improves quality:
- Version number and release date.
- Known issues and workarounds, upgrade or migration steps, deprecation timelines.
- Style guide, previous release notes for tone and format.

If the change list or the audience is missing, ask. Do not guess the impact of a change from its ticket title alone; mark it `[CONFIRM]` and list it as an open question.

## Process
1. Filter the change list for the audience: drop internal refactors, test and build changes unless they have visible effect (performance, security, compatibility).
2. Classify each remaining change: New, Improved, Fixed, Breaking, Deprecated, Security, Known issue.
3. Identify breaking changes rigorously: removed or renamed fields, endpoints, settings, changed defaults, changed behavior, new required configuration, minimum version changes.
4. Rewrite each item from the reader's point of view: what they can now do or what no longer happens, not what the team did internally.
5. For each breaking or deprecated item, state the required action, deadline and the migration path.
6. For security fixes, state the affected versions and the recommended action without disclosing exploit details before users can patch.
7. Add known issues with workaround and expected fix status only if confirmed; never promise dates that were not given.
8. Order sections by what the reader must act on first: breaking and security, then new and improved, then fixes, then known issues.
9. Check the version number is consistent with the change types; if a breaking change sits in a minor or patch release, flag it.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `semantic-versioning` to confirm the number, `changelog-entry` for the repository log, or `release-announcement` for a marketing message.

## Output format
```markdown
# <Product> <version> Release Notes
Release date: <date or [TBD]> · Audience: <audience>

## Action Required
- **Breaking:** <change> – <who is affected> – <what to do> – <by when>
- **Deprecated:** <feature> – removal planned in <version/date or [TBD]> – <alternative>

## Security
- <issue class> fixed in <component>; affects <versions>. Upgrade recommended.

## New
- <capability from the user's point of view>

## Improved
- ...

## Fixed
- <symptom the user saw> no longer occurs when <condition>.

## Known Issues
- <issue> – workaround: <...>

## Upgrade Notes
<steps, compatibility, minimum versions>
```

## Quality checklist
- [ ] Every item is written in the reader's terms, not internal ticket jargon.
- [ ] All breaking changes and deprecations have a concrete required action.
- [ ] No internal-only change, personal data, customer names or exploit details leaked.
- [ ] Items whose impact was unclear are marked `[CONFIRM]`, not guessed.
- [ ] The version number is consistent with the presence of breaking changes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Hiding a breaking change in the "Improved" list. Readers skim; put it at the top under Action Required.
- Copying ticket titles ("Fix NPE in OrderMapper"). Describe the symptom the user experienced.
- Listing every commit. Notes are curated; a long unfiltered list hides what matters.

## Example
Input: "PAY-812 Remove legacy /v1/refund endpoint; PAY-790 Fix null pointer in invoice export when currency missing; PAY-801 Bump logging library."

Weak: "Removed /v1/refund. Fixed NPE in invoice export. Updated logging library."

Strong:
- **Breaking:** The `/v1/refund` endpoint has been removed. Integrations still calling it will receive errors; switch to `/v2/refunds` (see migration guide) before upgrading.
- **Fixed:** Invoice export no longer fails for invoices without a currency value.
- (Logging library update omitted: no user-visible effect `[ASSUMPTION]`.)
