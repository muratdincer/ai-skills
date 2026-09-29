---
name: code-explanation
description: "Explains what a piece of code does, why it is likely written that way and what risks it carries, at the depth the reader needs: a one-paragraph summary, a step-by-step walkthrough of control and data flow, side effects, assumptions, edge cases and suspicious spots. Use when someone pastes code and asks what it does, how it works, why it behaves a certain way, or needs to understand code before changing or reviewing it."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: coding
  title: "Explain code"
  related: "legacy-code-comprehension, code-documentation, clean-code-review, regex-builder, technical-onboarding"
  prompt: "Explain what this function does and whether anything in it looks risky."
---

# Explain Code

## Purpose
Give the reader an accurate mental model of a piece of code quickly: what it achieves, how data moves through it, what it touches outside itself and where it may break, clearly separating what the code shows from what is inferred.

## When to use
- Someone needs to understand a function, class, query, script or configuration before changing it.
- A reviewer or newcomer asks "what does this do?" or "why does this return X?".
- Code uses an unfamiliar idiom, library or language feature.

## When not to use
- A whole unfamiliar codebase or module landscape must be mapped. Use `legacy-code-comprehension`.
- The goal is a quality judgment with findings. Use `clean-code-review` or `code-review`.
- The output should be permanent comments or docstrings. Use `code-documentation`.

## Inputs
Required:
- The code snippet or file.

Optional, improves quality:
- Language/framework version, the caller or context, the reader's background, the specific question (for example "why is this slow", "why does it return null").

If a referenced function, type or config is not provided, explain based on its name and usage and mark that part `[INFERRED from name]`.

## Process
1. Identify language, framework and the kind of code (handler, domain logic, query, script, config, test).
2. Write a one-paragraph summary in domain terms: inputs, output, main effect. Answer the user's specific question first if they asked one.
3. Walk through the code in execution order, grouping lines into steps; explain intent, not syntax, unless the syntax is the unusual part.
4. Trace data flow: where each input comes from, how it is transformed, what is returned or persisted.
5. List side effects and external interactions: I/O, database writes, network calls, global or shared state, events, logging, time and randomness.
6. State implicit assumptions and contracts: nullability, ordering, units, encoding, time zone, transaction boundaries, thread-safety.
7. Walk the edge cases: empty, null, very large, duplicate, concurrent, failure of each external call. Say what happens in each.
8. Flag risks and oddities with severity (bug likely, risk, smell), each with the line or construct and why; do not rewrite the code unless asked.
9. Separate facts from inferences: anything about the "why" or about unseen code is labeled `[INFERRED]`.
10. Adapt depth to the reader: a short summary first, details below; avoid explaining basics to a senior reader.
11. If the goal continues, suggest `code-documentation` to capture the explanation, `clean-code-review` for improvement findings or `legacy-code-comprehension` if the surrounding system is also unclear.

## Output format
```markdown
# Code Explanation: <function/file>
**In short:** <one paragraph>

## Step by Step
1. <lines x-y>: <what and why>

## Data Flow
<input> → <transformation> → <output/persistence>

## Side Effects
- ...

## Assumptions and Contracts
- ...

## Edge Cases
| Case | What happens |

## Risks and Oddities
| Severity | Where | Issue | Why it matters |

## Inferred / Unverified
- [INFERRED] ...
```

## Quality checklist
- [ ] The summary answers the user's actual question in the first lines.
- [ ] Every claim about unseen code or original intent is labeled `[INFERRED]`.
- [ ] All side effects and external calls are listed.
- [ ] Edge cases state concrete outcomes, not "might fail".
- [ ] Explanation depth matches the reader; no line-by-line syntax narration.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Paraphrasing each line ("increments i by one") instead of explaining intent and flow.
- Presenting a guess about why the code exists as fact. Label it and suggest who or what (history, ticket) can confirm.
- Missing hidden behavior in framework conventions, such as lazy loading, implicit transactions or default serialization.

## Example
Input: a 25-line function `applyDiscount(cart)` that loops items, reads `promo` from a static cache and mutates `item.price`.

Weak: "The function loops over the items and changes their prices."

Strong excerpt:
- **In short:** Applies the active promotion to eligible cart items by overwriting each item's price in place; returns nothing.
- Side effect: mutates `item.price`, so calling it twice applies the discount twice.
- Risk (bug likely): percentage computed with integer division, so 15% of 999 yields 149, not 149.85.
- [INFERRED] The static promo cache is refreshed elsewhere; stale promotions are possible if refresh fails.
