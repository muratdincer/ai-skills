---
name: error-message-writing
description: "Writes user-facing error, validation and warning messages that say what happened, why if it helps, and what to do next, without blame, jargon or leaking internals, with the right placement, severity and accessibility behavior. Use when error states need copy, when existing messages are vague (\"Something went wrong\") or technical, or when an error catalog must be turned into user-facing text."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 10-design
  role: ux-writer
  area: content
  title: "Write error messages"
  related: "microcopy, voice-and-tone-guide, error-scenario-catalog, error-handling-review, design-handoff"
  prompt: "Rewrite these five payment error messages so users know what happened and what to do; the current ones just show API error codes."
---

# Write Error Messages

## Purpose
Help users recover from a failure quickly and with confidence by telling them what happened, whether it is their action or the system's, and the next concrete step, in the product's voice.

## When to use
- A screen, form or flow needs error, validation, warning or failure copy.
- Existing messages are generic, technical, blaming or expose error codes and stack details.
- A list of technical error cases (from an API or error catalog) must be mapped to user-facing messages.

## When not to use
- The text is not about a failure (labels, empty states, confirmations). Use `microcopy`.
- You need to enumerate which errors can happen in the first place. Use `error-scenario-catalog`.
- You are reviewing how the code handles errors. Use `error-handling-review`.

## Inputs
Required:
- The error situations: current messages, error codes, or a description of what fails and when.

Optional, improves quality:
- What the system knows at that moment (which field, retry possible, data saved or lost).
- Voice and tone guide, glossary, length limits, languages.
- Support channel and reference ID format.

If the error situations are missing, ask for them. If the cause or recovery path of a case is unknown, mark it `[UNKNOWN]` rather than guessing.

## Process
1. For each case, identify the cause class: user input, user permission or state, system/service failure, connectivity, or business rule. The class determines who acts next.
2. Determine what the user can do: fix input, retry, wait, change setting, contact someone, or nothing. Confirm whether data was saved, lost or partially processed; never imply safety that is not guaranteed.
3. Choose severity and placement: inline field validation, form-level summary, banner, toast, dialog or full page. Blocking dialogs only when the user must decide.
4. Write the message: what happened in plain words, why only if it helps the user act, and the next step as an instruction or action button. Keep the object specific ("card number", not "input").
5. Remove blame, jargon and internals: no "invalid", "illegal", "fatal", HTTP codes or exception names in the main text. Put a support reference ID in secondary text when support may need it.
6. Match tone to stakes: calm and neutral for serious failures; no humor or exclamation marks in errors; apologize only when the system is at fault, and only once.
7. For validation, state the rule the user must meet, validate at the right moment (on blur or submit, not per keystroke), keep the entered value, and list errors in a summary that links to fields when there are several.
8. Check accessibility against WCAG 2.2: errors are identified in text (not color alone), associated with the field, announced to assistive technology, and focus moves to the summary or first error on submit.
9. Check security and privacy: do not reveal whether an account exists, internal system names or personal data of others; keep messages for authentication failures deliberately generic.
10. Verify length limits and localization (no concatenated fragments, placeholders for dynamic values with plural handling), and label any assumption about cause or recovery `[ASSUMPTION]`.
11. If the goal continues, suggest `error-scenario-catalog` to find uncovered failures, `microcopy` for the surrounding UI text, or `design-handoff` to attach messages to states.

## Output format
```markdown
# Error Messages: <feature / flow>

| ID / code | Cause class | Placement | Message (title + body) | Action | Data state | Note |
|---|---|---|---|---|---|---|
| ... | user input | inline | ... | ... | kept | ... |

## Rules Applied
- Validation timing: ...  - Focus and announcement: ...  - Reference ID: ...

## Before / After
| Current | Proposed | Why |

## Assumptions and Open Questions
- [ASSUMPTION] ...
- [UNKNOWN] recovery path for <code> — owner: ...
```

## Quality checklist
- [ ] Every message says what happened and gives a concrete next step or states that none is needed.
- [ ] No blame, jargon, internal codes or exception names in main text.
- [ ] Claims about saved or lost data are backed by the input or marked `[UNKNOWN]`.
- [ ] Validation messages state the rule and keep the user's input.
- [ ] Errors are text-identified, field-associated and announced; not signaled by color alone.
- [ ] Authentication and permission messages do not leak account or system details.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Something went wrong." It gives no cause and no action; at minimum say whether to retry and whether work was saved.
- Mapping one message per technical code. Users need one message per recovery path; merge codes that lead to the same action.
- Clearing the form on error. Keep the input and point to the exact field.

## Example
Input: "Payment fails with `CARD_DECLINED_51` (insufficient funds). Current message: 'Error 51: Transaction failed.'"

Weak: "Error 51: Transaction failed. Please try again."

Strong: Title "Payment didn't go through" · Body "Your bank declined the card. You haven't been charged. Try another card or contact your bank." · Actions [Use another card] · Placement: form-level banner, focus moves to it.
