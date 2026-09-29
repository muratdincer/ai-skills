---
description: Writes a product or brand voice and tone guide with 3-5 voice principles, each defined by what it is and is not, do/don't example pairs, a tone map that shifts by user context (success, error, onboarding, sensitive moments), grammar and terminology conventions, and a review checklist for writers. Use when a product lacks consistent UI writing, when several teams write copy differently, when entering a new language or market, or when an existing voice guide is too vague to apply.
related: microcopy, error-message-writing, style-guide-check, positioning-statement, glossary-builder
prompt: Create a voice and tone guide for our B2B invoicing app in Turkish and English; our copy currently sounds different on every screen.
---

# Write a Voice and Tone Guide

## Purpose
Give everyone who writes product text a shared, testable definition of how the product sounds, so copy stays consistent across screens, teams and languages while tone adapts to the user's situation.

## When to use
- UI and messaging copy is inconsistent across teams or features.
- A product is launching, rebranding or expanding into a new language or market.
- An existing voice guide lists adjectives ("friendly, smart") but writers cannot apply it.

## When not to use
- You need copy for specific screens now. Use `microcopy` or `error-message-writing`.
- You need to check a document against an existing guide. Use `style-guide-check`.
- You need market positioning rather than writing style. Use `positioning-statement`.

## Inputs
Required:
- Product description and primary audience (who reads the copy, in what context).
- At least a few real copy samples, or a statement that none exist yet.

Optional, improves quality:
- Brand values, positioning, existing brand guidelines.
- Target languages and formality conventions (e.g. Turkish "siz" vs "sen").
- Known user complaints about tone; regulated or sensitive domains.

If audience or product description is missing, ask. Ask at most 5 focused questions at a time and reuse anything already given.

## Process
1. Summarize the audience: expertise, emotional state in key moments, reading context (desk, mobile, under time pressure), and accessibility or plain-language needs.
2. Audit supplied copy samples: note inconsistencies in formality, person, terminology, capitalization and emotion. These findings justify each principle; if no samples exist, state that principles are `[ASSUMPTION]` pending real copy.
3. Derive 3-5 voice principles. Define each as "X, not Y" (e.g. "Direct, not curt") with a one-line explanation of why it fits this audience. Reject generic adjectives no competitor would disagree with.
4. For each principle, write at least one do/don't pair using realistic product copy.
5. Build a tone map: for key contexts (onboarding, routine task, success, warning, error, data loss or security, billing, sensitive personal moments) set dials such as formality, warmth, humor and urgency, with a sample line.
6. Set language mechanics per language: form of address, person (we/you), sentence vs title case, contractions, numbers, dates, currency, punctuation, emoji policy, inclusive and gender-neutral language.
7. Seed a terminology list: preferred terms, banned terms and their replacements; point to `glossary-builder` for the full glossary.
8. Add accessibility and plain-language rules: reading level target, sentence length, avoid idioms that do not translate, link text rules.
9. Write a short review checklist writers run on any copy, and a governance note: owner, how to propose changes, where examples are collected.
10. Separate evidence-based rules (from the audit) from preferences you proposed; label the latter `[ASSUMPTION]` for stakeholder validation.
11. If the goal continues, suggest `microcopy` or `error-message-writing` to apply the guide, or `style-guide-check` to audit existing content against it.

## Output format
```markdown
# Voice and Tone Guide: <product>
## Audience
- ...

## Voice Principles
### 1. <X, not Y>
Why: ...
| Do | Don't |
|---|---|

## Tone Map
| Context | Formality | Warmth | Humor | Urgency | Example |
|---|---|---|---|---|---|

## Language Mechanics
| Rule | EN | TR |

## Terminology
| Use | Avoid | Note |

## Accessibility and Plain Language
- ...

## Writer's Checklist
- [ ] ...

## Governance
- Owner: ...  - Change process: ...

## Assumptions to Validate
- ...
```

## Quality checklist
- [ ] Each principle is phrased as "X, not Y" and has at least one realistic do/don't pair.
- [ ] The tone map covers error, success and at least one high-stakes context.
- [ ] Mechanics are stated per target language, including form of address.
- [ ] Rules are traceable to the audience or copy audit; proposals are labeled `[ASSUMPTION]`.
- [ ] A writer could decide between two drafts using only this guide.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Adjective lists ("friendly, innovative, human"). They cannot be tested; define boundaries with "not" and examples.
- One tone everywhere. Voice stays constant; tone must calm down for errors, billing and security.
- Translating the English guide. Formality, address and humor work differently per language; set rules natively.

## Example
Input: "B2B invoicing app for accountants, EN and TR; copy mixes 'sen' and 'siz' and jokes in error messages."

Weak principle: "Friendly — we are approachable and fun."

Strong principle: "Precise, not pedantic." Why: accountants act on exact numbers and dates.
| Do | Don't |
|---|---|
| "Invoice #1042 is due on 15 March." | "Heads up! Something's due soon 🙂" |
| TR: "1042 numaralı faturanızın son ödeme tarihi 15 Mart." (always "siz") | TR: "Faturan yakında patlıyor!" |
