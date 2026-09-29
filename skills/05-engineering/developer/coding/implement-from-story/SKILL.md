---
description: "Plans and implements a feature from a user story by mapping acceptance criteria to behaviors, reading the existing code conventions, writing code and tests in small verifiable steps, and reporting what was built, how it was verified and what remains open. Use when a developer asks to implement, build or code a story, ticket or feature against given acceptance criteria."
related: "task-breakdown, acceptance-criteria, tdd-cycle, unit-test-writing, pull-request-description"
prompt: "Implement this story in our service: a customer can set a default shipping address; only one address can be default; the default is preselected at checkout."
---

# Implement a Feature From a Story

## Purpose
Deliver working, tested code that satisfies every acceptance criterion, fits the existing codebase conventions, and comes with an honest account of what was verified and what was assumed.

## When to use
- A story or ticket with acceptance criteria is ready to be coded.
- A developer shares relevant code and asks for the implementation of a described behavior.
- A small feature needs to be added end to end (contract, logic, persistence, tests).

## When not to use
- The story is too big or unclear to code directly. Use `task-breakdown` or `acceptance-criteria` first.
- The change is structural with no behavior change. Use `refactoring`.
- A cross-team or hard-to-reverse change. Use `technical-design-doc` first.

## Inputs
Required:
- The story with acceptance criteria, and the relevant existing code (or a description of the stack and structure).

Optional, improves quality:
- Coding standards, test conventions, architecture rules, feature flag policy.
- Related contracts, schemas, similar existing features to mirror.

If no code or stack information is given, ask for it; do not invent a project structure and present it as existing.

## Process
1. Restate each acceptance criterion as an observable behavior with input, action and expected result; list ambiguities and choose a documented `[ASSUMPTION]` for non-blocking ones.
2. Read the existing code paths the change touches: entry point, domain logic, persistence, error handling, tests. Note conventions to follow (naming, layering, DI, error types).
3. Identify the smallest design that fits: where new logic belongs, what changes in contracts or schema, what must stay backward compatible.
4. Plan steps so each ends green: e.g. schema expand → domain rule with unit tests → endpoint/UI with integration test → wiring behind a flag.
5. For each step write the test first or alongside the code; cover the acceptance criterion, its edge cases and the failure path.
6. Implement with the codebase's idioms; validate inputs at boundaries, keep domain invariants in the domain layer, handle concurrency where the criterion implies uniqueness.
7. Add logging/metrics only where they aid operation, without personal data.
8. Self-review the diff: dead code, debug output, TODOs, naming, error messages, security (authorization on every new entry point).
9. Map each acceptance criterion to the tests that prove it.
10. Report: files changed, how to run the tests, assumptions, and follow-ups (docs, flag removal, migration contract step).
11. If the goal continues, suggest `pull-request-description` to open the change for review or `unit-test-writing` to deepen test coverage.

## Output format
```markdown
# Implementation: <story title>
## Plan
1. <step> — ends with: <green test / verifiable state>

## Changes
- `<path>`: <what and why>

## Code
<diff or code blocks per file>

## Acceptance Criteria Verification
| Criterion | Test(s) | Status |

## Assumptions and Follow-ups
- [ASSUMPTION] ...
- Follow-up: ...
```

## Quality checklist
- [ ] Every acceptance criterion has at least one test that would fail without the change.
- [ ] Code follows the existing conventions seen in the provided code.
- [ ] New entry points enforce authorization and validate input.
- [ ] Invariants that must hold under concurrency are protected (constraint, lock or idempotency).
- [ ] No invented files, APIs or library functions; anything uncertain is flagged.
- [ ] Assumptions and follow-ups are listed explicitly.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Implementing the happy path and leaving edge cases implied by the criteria (empty, duplicate, not found, unauthorized).
- Introducing a new pattern or library when the codebase already has one for the job.
- Enforcing "only one default" with a read-then-write in code; concurrent requests produce two defaults. Use a constraint or a transactional swap.

## Example
Input: "Customer sets a default shipping address; only one default; preselected at checkout."

Excerpt of output:
- Plan step 2: `Customer.setDefaultAddress(addressId)` clears the previous default and sets the new one in one transaction; unit tests: switch default, set unknown address → `AddressNotFound`, set another customer's address → forbidden.
- Invariant: partial unique index on `(customer_id) WHERE is_default` plus transaction; integration test runs two concurrent requests and asserts exactly one default.
- `[ASSUMPTION]` Deleting the default address leaves no default; checkout then shows no preselection. Confirm with PO.
