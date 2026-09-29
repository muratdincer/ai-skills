---
description: Writes or improves docstrings, API comments and inline comments so they state contracts, intent, constraints and non-obvious reasons (the why), not a restatement of the code (the what), and flags comments that are wrong, stale or should become code. Use when a developer asks to document a function, class, module or public API, to review existing comments, or to prepare code for handover.
related: readme-writing, api-reference-docs, clean-code-review, code-explanation, legacy-code-comprehension
prompt: Add proper documentation to this pricing module. Keep it useful; I do not want comments that just repeat the code.
---

# Write Code Documentation

## Purpose
Make code safe to use and change by documenting what the code cannot say for itself: the contract a caller relies on, the constraints and invariants, and the reasons behind surprising decisions. Fewer, precise comments beat many that echo the code and rot.

## When to use
- A public function, class, module or library API has no or weak doc comments.
- Existing comments are outdated, misleading or restate the code.
- Code with hidden business rules, workarounds or performance tricks is about to be handed over.

## When not to use
- Project-level setup and usage. Use `readme-writing`.
- Endpoint-level reference for HTTP or message APIs. Use `api-reference-docs`.
- Understanding unfamiliar code before documenting it. Use `code-explanation` or `legacy-code-comprehension` first.

## Inputs
Required:
- The code to document, with language and enough context to understand callers.

Optional, improves quality:
- The team's doc comment convention (e.g., the language's standard docstring or doc-comment style) and whether docs are generated from comments.
- Background on business rules, tickets or incidents behind non-obvious code.
- Intended audience: internal maintainers or external library users.

If the reason for a non-obvious decision cannot be derived from the code, do not invent it: write a `TODO(owner): explain why ...` or list it as an open question.

## Process
1. Determine the visibility of each element (public API, package-internal, private). Public API gets full contract docs; private code gets comments only where the why is non-obvious.
2. Before commenting, look for things that should be code instead: unclear names, magic numbers, long functions. Propose the rename or extraction and skip the comment it would replace.
3. For each public element, write a one-line summary in the language's convention that says what it does for the caller, in domain terms.
4. Document the contract: parameters (meaning, units, allowed ranges, nullability), return value (including empty and not-found cases), errors or exceptions thrown and when, side effects (I/O, state, events), thread-safety and idempotency where relevant.
5. Add constraints and invariants that callers or maintainers must preserve (ordering, precision, time zone, rounding, performance limits).
6. For non-obvious implementation choices, add a short why comment at the exact line: business rule, regulatory reason, bug workaround with its reference, or measured performance trade-off.
7. Add a short usage example for public APIs whose correct use is not obvious; keep it compilable in principle.
8. Remove or rewrite comments that restate the code, are wrong, or reference things that no longer exist; mark deprecated elements with the replacement and removal plan.
9. Label every stated reason you inferred from the code as `[ASSUMPTION]` in your response so the author can confirm it before committing.
10. Present the result as the documented code (or a diff), followed by a short list of proposed code changes and open questions. If the user continues, suggest `api-reference-docs` for external API docs or `clean-code-review` for the naming and structure findings.

## Output format
```markdown
## Documented Code
<code with doc comments and why-comments, in the language's convention>

## Proposed Code Changes Instead of Comments
- <rename / extract constant / extract function> — <reason>

## Removed or Corrected Comments
- <location>: <what was wrong or redundant>

## Open Questions and Assumptions
- [ASSUMPTION] <inferred reason> — confirm with <owner>
```

## Quality checklist
- [ ] Every public element states its contract: inputs, output, errors and side effects.
- [ ] No comment only restates what the next line of code says.
- [ ] Units, ranges, nullability and time zones are explicit wherever they matter.
- [ ] Each why-comment explains a reason a maintainer could not recover from the code, with a reference where one exists.
- [ ] Inferred reasons are flagged `[ASSUMPTION]`; nothing is presented as a fact without evidence.
- [ ] The comment style matches the language convention so documentation tools can parse it.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Documenting what the code does line by line. It doubles maintenance and becomes wrong at the next change; document intent and contract.
- Hiding a bad name behind a comment. Rename the thing instead.
- Writing "handles errors" without saying which errors, how they surface and whether the operation is retried.

## Example
Input: `def price(q, c): return round(q * c.base * (0.9 if q >= 100 else 1), 2)`

Weak: `# multiplies quantity by base price and applies discount`

Strong:
```python
BULK_THRESHOLD = 100   # proposed: replaces magic number
BULK_DISCOUNT = 0.10

def price(quantity: int, catalog_item: CatalogItem) -> Decimal:
    """Return the net line price in the item's currency, rounded to 2 decimals.

    Orders of BULK_THRESHOLD units or more get BULK_DISCOUNT.
    Quantity is expected to be >= 1; it is not validated here.
    """
```
- Open question: should `quantity < 1` raise an error? The current code silently returns 0 or a negative price.
- [ASSUMPTION] The 10% bulk rule comes from the commercial terms; confirm with the pricing owner.
- Proposed: use a decimal type and an explicit rounding mode instead of float `round`.
