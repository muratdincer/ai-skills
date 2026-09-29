---
name: app-store-release-notes
description: "Writes short, user-facing \"What's new\" release notes for mobile app stores from a changelog, ticket list or pull request titles, filters out internal changes, fits each store's character limit and prepares localized variants. Use when a mobile version is about to be submitted to an app store, when a raw changelog must be turned into store copy, or when notes must be localized or shortened for a store."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: mobile
  title: "Write app store release notes"
  related: "release-notes, changelog-entry, mobile-release-checklist, microcopy, voice-and-tone-guide"
  prompt: "Turn this sprint's merged PR titles into App Store and Google Play release notes for version 5.3, in English and Turkish."
---

# Write App Store Release Notes

## Purpose
Tell users in a few lines what is better for them in this version, in the product's voice and within store limits. Good store notes support ratings, reduce support contacts and never leak internal or security details.

## When to use
- A mobile build is ready for store submission and needs "What's new" text.
- Engineering produced a changelog or PR list that must be turned into user language.
- Notes must be localized, shortened, or adapted for different stores.

## When not to use
- Detailed release notes for customers, support or operations. Use `release-notes`.
- The developer-facing change history in the repository. Use `changelog-entry`.
- Checking whether the build is ready to submit at all. Use `mobile-release-checklist`.

## Inputs
Required:
- The list of changes in this version (changelog, tickets, PR titles or a description) and the version number.

Optional, improves quality:
- Target stores and locales; the product's voice-and-tone guide.
- Which changes are behind feature flags or staged rollout, and which are platform-specific.
- Store character limits the team works with, and previous notes for style.

If the change list is missing, ask for it. Do not invent features; if a change's user benefit is unclear, mark it `[ASSUMPTION]` or ask.

## Process
1. Classify each change: user-visible feature, improvement, fix, platform-specific, internal (refactor, dependency, tooling, analytics), or security.
2. Drop internal changes. Treat security fixes generically ("security improvements") without describing the vulnerability.
3. Remove or hold back items behind disabled feature flags or limited rollout, unless the team confirms they are visible to all users of this build.
4. Translate each kept item into user benefit: what the user can now do or what stopped annoying them, in plain words; no ticket numbers, component names or jargon.
5. Order by user value: the headline feature first, then improvements, then fixes grouped in one line if minor.
6. Fit the store limit: confirm the limit per store with the user; if unknown, keep the primary version short enough for the strictest common limit (about 500 characters) and put the most important item in the first line, since stores truncate the preview.
7. Apply the product voice: consistent tense and person, no exaggeration, no promises about future releases, no comparisons to competitors, and nothing that violates store content rules (e.g., references to other platforms or pricing claims the team has not approved).
8. Produce platform variants when features differ between iOS and Android, and localized variants written natively (not word-for-word), checking length again after translation.
9. Add a fallback line for maintenance-only releases instead of a generic "bug fixes" when a real user benefit exists (stability, speed).
10. List assumptions and items excluded, with the reason, so the release owner can confirm.
11. If the user continues, suggest `mobile-release-checklist` for the submission itself, `release-notes` for fuller customer notes, or `microcopy` to refine the wording.

## Output format
```markdown
# Store Release Notes: v<version>

## <Store> · <locale> (<n>/<limit> characters)
<Headline benefit sentence.>
• <benefit>
• <benefit>
• Fixes: <short grouped line>

## Excluded or Held Back
| Item | Reason (internal / flagged / security / unclear) |
|---|---|

## Assumptions and Questions for the Release Owner
- ...
```

## Quality checklist
- [ ] Every line describes a user benefit, with no ticket IDs, internal names or jargon.
- [ ] No feature that is disabled, flagged off or not in this build is mentioned.
- [ ] Security fixes are not described in exploitable detail.
- [ ] Each variant states its character count and fits the confirmed or conservative limit.
- [ ] Localized text reads naturally and is checked for length after translation.
- [ ] Unclear benefits are marked `[ASSUMPTION]` and listed for confirmation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Pasting the engineering changelog ("Refactored PaymentService, bumped SDK"). Users cannot act on it; translate or drop it.
- Announcing a feature that is still behind a flag or rolled out to 5%, which generates support tickets and bad reviews.
- Writing only "Bug fixes and performance improvements" every release when there is a real benefit to name.

## Example
Input: "v5.3 PRs: feat: saved searches; fix: crash when rotating on checkout (Android); chore: upgrade analytics SDK; feat(flag off): dark mode beta."

Weak: "v5.3: saved searches, Android checkout rotation crash fix, analytics SDK upgrade, dark mode beta."

Strong (Google Play, en, 184/500):
"Save your searches and get back to them in one tap from the Search tab.
• Checkout no longer closes unexpectedly when you rotate your phone.
• Smaller fixes and stability improvements."

Excluded: analytics SDK upgrade (internal); dark mode beta (flag off).
