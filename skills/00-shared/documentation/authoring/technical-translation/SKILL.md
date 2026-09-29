---
description: "Translates technical content (specifications, documentation, UI text, error messages, release notes, runbooks) between English and Turkish while preserving terminology, code, identifiers, formatting and meaning, and flags ambiguous source text. Use when a technical document, message or interface must be delivered in the other language, or when an existing translation needs terminology alignment."
related: "glossary-builder, microcopy, error-message-writing, document-review, style-guide-check"
prompt: "Translate this API error-handling section of our developer guide from English to Turkish; keep code and HTTP terms as they are."
---

# Translate Technical Content

## Purpose
Deliver a translation that a native-speaking engineer or user reads as if it had been written in their language, with consistent terminology and every technical token (code, identifiers, units, placeholders) intact.

## When to use
- Specifications, guides, runbooks or release notes must be published in English and Turkish.
- UI strings, error messages or notifications need localization.
- A client or regulator requires a document in the other language.
- An existing translation is inconsistent and needs terminology alignment.

## When not to use
- No agreed terminology exists for a large or long-lived body of content. Run `glossary-builder` first, then translate.
- The source text itself is unclear or poorly written. Use `document-simplify` or `document-review` on the source first.
- UI copy should be rewritten, not translated, for the target audience. Use `microcopy`.

## Inputs
Required:
- The source text and the target language (EN to TR or TR to EN).

Optional, improves quality:
- Glossary or term base, style guide, formality level (for Turkish, "siz" versus "sen").
- Audience (developers, end users, auditors) and publication medium (UI, PDF, wiki).
- Character limits for UI strings.

If the source or direction is missing, ask. Do not guess domain terms with multiple valid translations; list them for confirmation.

## Process
1. Scan the source and freeze non-translatable tokens: code blocks, inline code, identifiers, API paths, config keys, placeholders (`{0}`, `%s`, `{{name}}`), URLs, product names, units and version numbers.
2. Build or apply a term list: decide per term whether to keep the English form (commonly used by Turkish engineers, for example deployment, pipeline, cache), translate it, or use Turkish with the English term in parentheses on first use.
3. Identify ambiguous source sentences and mark them rather than guessing; propose the most likely reading with `[ASSUMPTION]`.
4. Translate for meaning at sentence level, restructuring word order to target-language norms (Turkish is verb-final; English prefers active voice with a clear subject).
5. Keep modal strength precise: must/shall = "-malıdır/zorunludur", should = "-malıdır (önerilir)" per context, may = "-abilir". Requirement strength must not change.
6. Apply Turkish grammar details: suffixes after abbreviations and code terms with an apostrophe (`API'ye`, `JSON'da`), vowel harmony based on pronunciation, correct characters ç, ğ, ı, İ, ö, ş, ü, and dotted/dotless i casing.
7. Localize formats where the text is for end users (dates, decimal separators, currency) but never inside code, logs or data samples.
8. Preserve the source structure: headings, lists, tables, links, emphasis and numbering.
9. Check UI strings against length limits and placeholder order; note where grammar forces reordering.
10. Deliver the translation plus a translator's note listing term decisions, ambiguities and items to confirm.
11. If the user's goal continues, suggest `glossary-builder` to lock the term decisions or `document-review` for a native-speaker review of the target text.

## Output format
```markdown
## Translation (<source> → <target>)
<translated content with original formatting>

## Translator's Notes
| Source term | Chosen rendering | Rationale |
|---|---|---|

Ambiguities: <sentence / interpretation chosen / [ASSUMPTION]>
To confirm: <terms or sentences needing a domain owner>
```

## Quality checklist
- [ ] All code, identifiers, placeholders, URLs and numbers are unchanged.
- [ ] Each term is rendered the same way throughout.
- [ ] Requirement strength (must/should/may) is preserved.
- [ ] Turkish suffixes, apostrophes and special characters are correct.
- [ ] Structure and formatting match the source.
- [ ] Ambiguities are flagged, not silently resolved.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Translating identifiers or log messages that users search for. Keep them in the original and explain in prose if needed.
- Over-translating established English terms ("konuşlandırma boru hattı" for pipeline) that Turkish teams do not use. Follow the team's vocabulary.
- Word-for-word translation that keeps English sentence order, producing stiff Turkish. Restructure for natural flow.

## Example
Input (EN): "If the token has expired, the API returns `401 Unauthorized`. Clients should refresh the token and retry once."

Excerpt of output (TR): "Token'ın süresi dolmuşsa API `401 Unauthorized` döner. İstemciler token'ı yenilemeli ve isteği bir kez tekrar denemelidir."
Note: "should" rendered as "-meli" (recommendation strength kept); "token" kept in English per team usage.
