---
description: Reviews a pull request or diff for correctness, design, tests, security, performance and readability, and returns prioritized, actionable findings with a clear verdict. Use when someone asks to review a PR, a diff, a patch or a code snippet before merge, or wants a second opinion on a change.
related: review-comment-writing, clean-code-review, secure-code-review, error-handling-review, pull-request-description
prompt: Review this pull request diff. It adds a discount calculation endpoint to the order service.
---

# Review a Pull Request

## Purpose
Catch defects and design problems before merge, at a cost proportional to the change's risk, and give the author feedback they can act on immediately. The output is a verdict plus a prioritized list of findings, not a line-by-line style commentary.

## When to use
- A PR or diff is ready for review.
- An author wants a pre-review before requesting human reviewers.
- A risky change (data, security, concurrency, public contract) needs a focused second look.

## When not to use
- A deep dive into only one dimension. Use `secure-code-review`, `concurrency-review`, `error-handling-review` or `clean-code-review`.
- Polishing the wording of comments you already have. Use `review-comment-writing`.
- Assessing the whole codebase rather than a change. Use `code-quality-report` or `tech-debt-assessment`.

## Inputs
Required:
- The diff or changed code, with enough surrounding context to understand it.

Optional, improves quality:
- PR description and linked work item / acceptance criteria.
- Team coding standards, architecture constraints, test results.
- Language/framework versions and runtime context (service, library, UI).

If only a fragment is given and correctness depends on unseen code, review what is visible and list the assumptions as `[ASSUMPTION]` and open questions.

## Process
1. Establish intent: read the description or infer it from the diff; if intent is unclear, say so first, because correctness can only be judged against intent.
2. Size the risk: public contracts, persistence, money, auth, concurrency and migrations raise the review depth.
3. Correctness: trace the main path and edge cases (null/empty, boundaries, time zones, rounding, idempotency, retries, partial failure). Check that acceptance criteria are actually met.
4. Design: responsibility placement, coupling, layering violations, leaky abstractions, duplication with existing code, backward compatibility of contracts.
5. Tests: do tests fail if the change is reverted? Are edge cases and error paths covered? Are tests deterministic?
6. Security: input validation, authorization on every new entry point, injection, secrets in code, sensitive data in logs (OWASP ASVS as reference).
7. Operability and performance: N+1 queries, unbounded loops or payloads, missing timeouts, logging and metrics on new paths, resource cleanup.
8. Readability: names, function size, comments explaining why; only raise style issues that a linter would not catch.
9. Classify each finding: `blocker` (must fix before merge), `major` (should fix, or agree follow-up), `minor`, `nit`, `question`, `praise`. Anchor each to file and line or code excerpt.
10. Give the verdict: Approve, Approve with comments, Request changes, or Needs discussion, with a one-line reason.

## Output format
```markdown
# Review: <PR title>
**Verdict:** <Approve | Approve with comments | Request changes | Needs discussion> — <reason>
**Risk level:** <High/Medium/Low> — <why>

## Summary
<2-3 sentences: what the change does and overall assessment>

## Findings
| # | Severity | Location | Finding | Suggested fix |
|---|---|---|---|---|
| 1 | blocker | <file:line> | <issue and consequence> | <concrete change> |

## Tests
- Covered: ...
- Missing: ...

## Questions for the Author
- ...

## What Is Good
- ...
```

## Quality checklist
- [ ] Every blocker states the concrete failure scenario, not just a principle.
- [ ] Findings are anchored to a location and include a suggested fix.
- [ ] Severity is proportionate; nits are not mixed in with blockers.
- [ ] Assumptions about unseen code are labeled `[ASSUMPTION]`.
- [ ] Tests were assessed for whether they would catch a regression.
- [ ] The verdict is consistent with the findings.

## Common pitfalls
- Spending the review on formatting while missing a missing authorization check. Review in risk order.
- Reviewing only the diff lines. Many bugs sit in unchanged callers or in what the diff forgot to change.
- Requesting a redesign at PR time without a blocker-level reason. Propose a follow-up instead.

## Example
Input: Diff adding `POST /orders/{id}/discount` that computes `total * (1 - pct/100)` with `double` and saves the result.

Excerpt of output:
- Verdict: Request changes — money is computed in floating point and the endpoint lacks an ownership check.
- 1 | blocker | OrderController:42 | Any authenticated user can apply a discount to any order ID. | Verify order ownership or a staff role before applying.
- 2 | blocker | DiscountService:18 | `double` arithmetic causes rounding errors on totals. | Use a decimal type and an explicit rounding mode.
- 3 | minor | DiscountServiceTest | No test for pct > 100 or negative pct. | Add boundary tests and validation.
