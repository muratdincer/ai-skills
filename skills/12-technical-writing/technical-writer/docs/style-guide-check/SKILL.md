---
description: Checks a document against a style guide and terminology list and reports each deviation with location, rule, severity and a concrete rewrite: terminology, voice and tone, grammar and mechanics, formatting conventions, UI and code references, inclusive and accessible language. Use before publishing or reviewing documentation, UI text, release notes or knowledge-base articles, when several authors have produced inconsistent content, or when a team wants to enforce its own or a public style guide.
related: glossary-builder, document-review, document-simplify, user-guide, how-to-guide
prompt: Check this installation guide against our style guide and terminology list and give me the fixes as a table.
---

# Check Against a Style Guide

## Purpose
Make a document consistent with the organization's writing rules and approved terminology, with every finding traceable to a rule and a ready-to-apply fix, so reviewers and authors spend time on substance rather than on style debates.

## When to use
- A document, help page or UI text set is about to be published or sent for review.
- Several authors or translators produced content with inconsistent terms and formatting.
- A team adopts a style guide (its own, or a public one such as a major vendor's developer documentation guide) and wants existing content checked.

## When not to use
- Reviewing technical accuracy, completeness or structure. Use `document-review`.
- Rewriting content for a lower reading level or a non-expert audience. Use `document-simplify`.
- Defining the terminology itself. Use `glossary-builder` first, then check against it.

## Inputs
Required:
- The text to check.
- The style rules to apply: the style guide (or relevant excerpts) and any terminology list; or the user's explicit choice of a named public guide.

Optional, improves quality:
- Content type and audience (UI text, API docs, end-user help), target language and locale conventions.
- Known exceptions, product names and trademarks, previous review comments.

If no style rules are given, ask which guide to apply. If the user has none, offer a minimal baseline (consistent terms, active voice, sentence-case headings, second person, locale date/number formats) and label every finding from it `[BASELINE – not an agreed rule]`. Do not attribute rules to a guide you have not been given.

## Process
1. Extract the applicable rules into a short checklist by category: terminology, voice and tone, grammar and mechanics, capitalization and punctuation, headings and lists, UI labels and code formatting, numbers/dates/units, links, inclusive and accessible language.
2. Build the term list: approved term, forbidden variants, product names and casing; note where the text uses several variants for one concept.
3. Read the document section by section and record each deviation with its location (heading or paragraph), the quoted original, the rule broken and a concrete rewrite.
4. Classify severity: Must fix (breaks terminology, legal/trademark, accessibility or meaning), Should fix (clear rule violation), Consider (preference or readability).
5. Check accessibility-related writing: descriptive link text, alt-text placeholders for images, no instructions relying only on color or position, plain-language headings (in line with WCAG 2.2 content guidance).
6. Separate rule violations from your own preferences; anything not backed by the given rules is labeled `[SUGGESTION]` and never Must fix.
7. Group repeated issues into one pattern finding with occurrence count and locations, instead of listing the same fix many times.
8. Flag rules that are ambiguous or conflict with each other, and cases where applying a rule would change technical meaning; route those to open questions rather than silently rewriting.
9. Optionally produce the corrected text when asked, keeping technical content, code and UI labels unchanged unless the rule is about them.
10. Summarize: counts by severity and category, top patterns, and rules that the guide should clarify.
11. If the user's goal continues, suggest `glossary-builder` to formalize terms, `document-review` for technical accuracy or `document-simplify` for readability.

## Output format
```markdown
# Style Check: <document>
Rules applied: <style guide / version / excerpts> | Terminology list: <name or none>

## Summary
Must fix: <n> | Should fix: <n> | Consider: <n>
Top patterns: ...

## Findings
| # | Location | Original | Rule | Severity | Suggested rewrite |

## Terminology Consistency
| Concept | Approved term | Variants found (count) |

## Accessibility Notes
- ...

## Open Questions and Rule Gaps
- <ambiguous or conflicting rule / meaning risk>
```

## Quality checklist
- [ ] Every finding cites a specific rule from the given guide, or is labeled `[SUGGESTION]` / `[BASELINE – not an agreed rule]`.
- [ ] Every finding has an exact location, the quoted original and a concrete rewrite.
- [ ] Repeated issues are grouped as patterns with counts.
- [ ] No rewrite changes technical meaning, code, commands or UI labels unintentionally.
- [ ] Terminology variants are consolidated in the terminology table.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Presenting personal taste as a rule. Tie every Must/Should finding to the guide; the rest is a suggestion.
- "Fixing" UI labels or code identifiers to match prose rules. Quote UI and code exactly as they appear in the product.
- Listing 40 identical comma fixes. Report the pattern once with locations so the author can fix it in one pass.

## Example
Input: "Check against our guide: sentence-case headings, 'sign in' (not 'login' as a verb), second person, no 'simply/just'."

Excerpt of output:
- Weak: "The tone could be better in some places."
- Strong: "| 3 | §Getting Started, para 2 | 'Simply login to the Admin Console' | No 'simply'; 'sign in' as verb | Should fix | 'Sign in to the Admin Console' |"
- Pattern: heading "Configuring The Gateway" and 6 other headings use title case → sentence case (Should fix, 7 occurrences).
- Open question: "Admin Console" is capitalized throughout – product name or generic term? Confirm with the terminology list.
