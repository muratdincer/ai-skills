---
description: Systematically surfaces edge cases for a feature, flow, API or requirement across boundaries, empty/null, duplicates, concurrency, time zones and dates, permissions, partial failure, retries and idempotency, volume and abuse, and turns each into an expected behavior or an open question. Use when a story, spec or design looks "happy-path only", before acceptance criteria or test design, or when someone asks "what could go wrong?" or "what cases are we missing?".
related: acceptance-criteria, error-scenario-catalog, equivalence-boundary-analysis, requirements-gap-analysis, test-scenarios-from-requirements
prompt: Find the edge cases for this story: as a warehouse clerk I want to reserve stock for a customer order so that the items are not sold twice.
---

# Elicit Edge Cases

## Purpose
Expose the non-happy-path situations a requirement silently ignores, and force a decision on the expected behavior for each, before they surface as defects, incidents or disputes in production.

## When to use
- A story, use case, API or screen spec describes only the main flow.
- Before writing acceptance criteria, test scenarios or an error-handling design.
- A feature touches money, stock, identity, scheduling or shared resources.

## When not to use
- Error messages and recovery for already-known failures need to be catalogued. Use `error-scenario-catalog`.
- Test inputs need to be partitioned into classes and boundaries. Use `equivalence-boundary-analysis`.
- The whole specification must be checked for missing categories. Use `requirements-gap-analysis`.

## Inputs
Required:
- The requirement, story, flow or API description to analyze.

Optional, improves quality:
- Data model or field definitions, business rules, roles, integrations.
- Expected volumes, time zones and locales in use, known incidents.

If the requirement is missing, ask for it. If key domain facts are missing (for example who can act, or which systems are involved), state an assumption and list it as an open question.

## Process
1. Summarize the main flow in 3-7 steps and list its entities, actors, inputs, state changes and external calls. These are the attack surface.
2. Boundaries and formats: min/max, zero, negative, just above/below limits, length, precision and rounding, encoding, special characters, locale formats.
3. Empty, null and missing: absent optional fields, empty lists, first-ever use (no data), deleted or archived referenced records.
4. Duplicates and identity: double submit, same request twice, duplicate records from import, case/whitespace variants, merged or renamed entities.
5. Concurrency and ordering: two actors on the same record, race between check and act, stale reads, out-of-order or late events, lock/timeout behavior.
6. Time and dates: time zones, DST transitions, end of month/year, leap day, business calendars and holidays, clock skew, expiry exactly at the boundary, backdated or future-dated input.
7. Permissions and state: unauthorized role, role change mid-flow, cross-tenant access, action on an object in the wrong state, revoked session.
8. Partial failure, retries and idempotency: downstream timeout after the side effect, retry duplicates, compensation/rollback, messages delivered twice or never, what the user sees meanwhile.
9. Volume and abuse: large payloads, bulk operations, pagination limits, rate limits, enumeration, injection, automated misuse, resource exhaustion.
10. For each case, write the expected behavior if the input states it; otherwise propose one marked `[ASSUMPTION]` and add a decision question with a likely owner. Rate likelihood and impact (H/M/L) and keep only relevant cases.
11. Suggest the next skill: `acceptance-criteria` to turn decided cases into criteria, `test-scenarios-from-requirements` for test design, or `error-scenario-catalog` for failure messaging.

## Output format
```markdown
# Edge Cases: <feature / story>
**Main flow:** 1. ... 2. ... 3. ...
**Scope analyzed:** <entities, actors, integrations>

| # | Category | Case (Given/When) | Expected behavior | Source (stated / [ASSUMPTION]) | L | I |
|---|---|---|---|---|---|---|
| EC-01 | Concurrency | Two clerks reserve the last unit at the same time | One succeeds, the other gets "insufficient stock" | [ASSUMPTION] | M | H |

## Decisions Needed
1. <question> – <why it matters> – <owner>

## Categories Checked with No Relevant Case
- <category> – <reason>
```

## Quality checklist
- [ ] All ten categories were considered; skipped ones are listed with a reason.
- [ ] Each case is concrete (specific values, actors, timing), not a generic heading.
- [ ] Each case has an expected behavior or an explicit decision question; assumed behavior is labeled.
- [ ] High-impact cases involving money, data integrity, security or privacy are flagged first.
- [ ] Cases are relevant to this feature; generic noise is removed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing categories instead of cases ("concurrency issues"). Write the specific situation and the expected outcome.
- Deciding business behavior yourself. Propose, label as `[ASSUMPTION]`, and route the decision to the product owner.
- Stopping at input validation. The costliest cases are usually concurrency, partial failure and time.
- Producing 80 cases of equal weight. Rank by impact and likelihood so the team handles the top ones.

## Example
Input: "As a warehouse clerk I want to reserve stock for a customer order so that the items are not sold twice."

Excerpt of output:
| # | Category | Case | Expected behavior | Source | L | I |
|---|---|---|---|---|---|---|
| EC-03 | Retries | Reservation call times out after stock was decremented; clerk clicks again | Second call is idempotent (same order ID), no double reservation | [ASSUMPTION] | M | H |
| EC-07 | Time | Reservation expiry falls on a DST change night | Expiry computed in UTC; UI shows local time | [ASSUMPTION] | L | M |
| EC-09 | Permissions | Order is cancelled while the reservation is being created | Reservation is released; clerk is notified | [TBD] | M | M |

Decision needed: How long does a reservation hold stock if the order is not confirmed? – Product owner.
