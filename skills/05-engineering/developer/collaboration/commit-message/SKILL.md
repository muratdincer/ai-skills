---
description: Writes a commit message in Conventional Commits format with a precise subject, a body that explains why the change was made, and footers for breaking changes and work item references. Use when a developer has a diff, a list of changes or a short description and needs a commit message, or wants to split a mixed change into well-scoped commits.
related: pull-request-description, changelog-entry, semantic-versioning, branching-strategy
prompt: Write a commit message for this diff. It adds retry with backoff to the payment client and fixes the timeout config key name.
---

# Write a Commit Message

## Purpose
Produce a commit message that a reviewer, a future maintainer running history search, and release tooling can all use: a scannable subject, the reasoning behind the change, and machine-readable signals for versioning and changelogs.

## When to use
- A diff or change description is ready and needs a commit message.
- A staged change mixes concerns and should be split into several commits.
- A team adopts Conventional Commits and wants messages that drive automated versioning or changelogs.

## When not to use
- Describing a whole branch for reviewers. Use `pull-request-description`.
- Writing user-facing release history. Use `changelog-entry` or `release-notes`.

## Inputs
Required:
- The diff, or a precise description of what changed.

Optional, improves quality:
- The reason for the change (bug, requirement, incident, refactoring goal).
- Work item or issue ID, team scope names, whether the change is breaking.
- Team conventions (allowed types and scopes, subject length, sign-off rules).

If neither a diff nor a description is given, ask for one. If the reason is missing, write the body with a `[TBD: why]` placeholder instead of guessing.

## Process
1. Read the change and list each logical modification. If they serve unrelated purposes (e.g., a feature plus an unrelated rename), recommend separate commits and write one message per commit.
2. Choose the type: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`, `revert`, `style`. Pick by user-visible effect, not by file types touched.
3. Choose an optional scope from the module or bounded context affected, using the team's existing scope names when known.
4. Write the subject: imperative mood, lowercase after the colon, no trailing period, at most ~50 characters (hard limit 72). It says what the commit does, not what the developer did.
5. Decide whether the change is breaking (public API, schema, config key, message contract, CLI flag). If so, add `!` after the type/scope and a `BREAKING CHANGE:` footer with migration guidance.
6. Write the body, wrapped at 72 columns: the problem or motivation, why this approach, notable side effects or trade-offs. Do not restate the diff line by line.
7. Add footers: `Refs:` or `Closes:` with work item IDs, `Co-authored-by:` if pairing, and any required sign-off.
8. Check that the message contains no secrets, customer data, internal hostnames or credentials copied from the diff.

## Output format
```markdown
<type>(<scope>)<!>: <imperative subject, <=50 chars>

<why: problem or motivation, 1-3 sentences>
<how / trade-offs worth knowing, optional>

BREAKING CHANGE: <what breaks and how to migrate>   (only if breaking)
Refs: <work item ID or [TBD]>
```
If splitting is recommended, list each proposed commit with the files or hunks it contains, followed by its message.

## Quality checklist
- [ ] One logical change per commit; mixed changes are flagged with a split proposal.
- [ ] Type reflects the effect (`fix` vs `refactor` vs `perf`) and matches team conventions.
- [ ] Subject is imperative, specific and within the length limit.
- [ ] Body explains why; nothing in it can be read directly from the diff alone.
- [ ] Breaking changes are marked both with `!` and a `BREAKING CHANGE:` footer.
- [ ] No invented issue IDs; unknown references are `[TBD]`.

## Common pitfalls
- Vague subjects such as "fix bug" or "update code". Name the behavior: "fix: reject expired tokens in refresh flow".
- Labelling a behavior change as `refactor`. A refactoring changes no observable behavior; otherwise it is `feat` or `fix`.
- Hiding a breaking config or contract change in a `chore`. Release tooling will then publish it as a patch.

## Example
Input: "Added exponential backoff retry (3 attempts) to PaymentClient; renamed config key `payment.timeOut` to `payment.timeout`."

Excerpt of output (split into two commits):
```
fix(payment)!: rename timeout config key to payment.timeout

The old key was misspelled and silently ignored, so the client
always used the 100 s library default.

BREAKING CHANGE: rename `payment.timeOut` to `payment.timeout`
in every environment config before deploying.
Refs: [TBD]
```
```
feat(payment): retry transient failures with exponential backoff
```
