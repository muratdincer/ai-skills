---
description: "Writes a regular expression for a stated matching need in the target engine's dialect, with a plain-language breakdown, a table of should-match and should-not-match test cases, anchoring and escaping decisions, and a check for catastrophic backtracking. Also explains or fixes an existing regex. Use when someone needs a pattern to validate, extract, search or replace text, pastes a regex and asks what it does, or reports a regex that matches too much, too little or runs slowly."
related: "code-explanation, unit-test-writing, data-quality-rules, secure-code-review, business-rules-catalog"
prompt: "Write a regex that extracts invoice numbers like INV-2024-000123 from email subjects; we use it in JavaScript."
---

# Build and Explain a Regex

## Purpose
Produce a pattern that matches exactly what is intended in the engine where it will run, proven by explicit positive and negative cases, readable by the next developer and safe against pathological input.

## When to use
- Validating, extracting, searching or replacing text with a pattern.
- An existing regex must be understood, fixed or made faster.
- A validation rule from requirements (codes, identifiers, formats) must become a pattern.

## When not to use
- The format has a real parser or standard library function (URLs, email per RFC 5322, dates, JSON, HTML). Recommend the parser instead.
- The need is a data quality rule across a dataset. Use `data-quality-rules`.
- A general walkthrough of surrounding code. Use `code-explanation`.

## Inputs
Required:
- What must match and what must not, ideally with real samples.
- The regex engine or language (for example PCRE, JavaScript, .NET, Java, Python `re`, RE2, POSIX, database dialect).

Optional, improves quality:
- Whether it validates a whole string or finds matches inside text, case sensitivity, Unicode needs, multiline input, the capture groups needed, performance constraints (untrusted input, size).

If the engine is unknown, ask; if the user cannot say, write for a common subset and mark engine-specific features `[ENGINE-DEPENDENT]`.

## Process
1. Restate the matching rule precisely: allowed characters, lengths, fixed parts, optional parts, separators, and where the match may occur.
2. Build the test table first: at least five should-match and five should-not-match cases, including boundaries (min/max length, leading/trailing spaces, adjacent text, Unicode, empty).
3. Decide anchoring: `^...$` or `\A...\z` for full validation (note `$` may match before a trailing newline in some engines); word boundaries or lookarounds for extraction.
4. Write the simplest pattern that satisfies the table; prefer explicit character classes over `.`, bounded quantifiers over `*`/`+` where lengths are known.
5. Use named or non-capturing groups deliberately; capture only what the caller needs.
6. Check for catastrophic backtracking: nested quantifiers, overlapping alternations, `(.*)*`-like shapes; rewrite with atomic groups, possessive quantifiers or unambiguous classes if the engine supports them, or state that input length must be limited.
7. Apply flags consciously: case-insensitive, multiline, dotall, Unicode; say which are required.
8. Run the test table against the pattern mentally, case by case, and fix until every row passes; report any case you are unsure about as `[VERIFY]`.
9. Give the pattern as a string literal escaped correctly for the target language, plus a commented (verbose) version if the engine supports it.
10. For explaining or fixing an existing regex: break it into tokens, state what it actually matches, show a counterexample for each bug, then give the corrected version with the same test table.
11. If the goal continues, suggest `unit-test-writing` to turn the test table into automated tests, or `secure-code-review` if the pattern guards untrusted input.

## Output format
````markdown
# Regex: <purpose>
Engine: <engine> · Mode: <validate whole string / extract> · Flags: <...>

```<language>
<pattern as a correctly escaped literal>
```

## Breakdown
| Part | Meaning |

## Test Cases
| Input | Expected | Result |

## Performance and Safety
- Backtracking risk: <none / mitigated by ...>

## Notes and Limits
- ...
````

## Quality checklist
- [ ] The pattern is written for the stated engine and escaped for the target language.
- [ ] The test table has both should-match and should-not-match rows, including boundaries.
- [ ] Anchoring matches the mode (validation vs extraction).
- [ ] No nested or ambiguous quantifiers remain without a stated mitigation.
- [ ] Cases not verified with certainty are marked `[VERIFY]`.
- [ ] A parser or library alternative was considered for standard formats.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Forgetting anchors so a "validation" pattern accepts `abcINV-2024-000123xyz`.
- Using `.*` greedily across a line and capturing far more than intended.
- Writing lookbehind or possessive quantifiers for an engine that does not support them.
- Trying to validate email or HTML fully with a regex instead of a proper parser plus a pragmatic check.

## Example
Input: "Extract invoice numbers like INV-2024-000123 from email subjects, JavaScript."

Weak: `/INV.*\d+/` (matches `INVALID code 42` and swallows the rest of the subject).

Strong excerpt:
```javascript
/\bINV-(\d{4})-(\d{6})\b/g
```
| Input | Expected | Result |
|---|---|---|
| `Re: INV-2024-000123 overdue` | match `INV-2024-000123` | pass |
| `XINV-2024-000123` | no match | pass |
| `INV-24-000123` | no match | pass |
