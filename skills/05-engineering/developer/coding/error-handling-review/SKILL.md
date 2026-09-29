---
description: "Reviews how code detects, propagates, retries, falls back from and reports errors: exception design, swallowed or over-broad catches, retry and timeout policy, idempotency, resource cleanup, transactional consistency and user-facing error messages. Use when failures are silent or confusing, before hardening a service or integration, or when someone asks to review error handling, exceptions or resilience of code."
related: "resilience-review, logging-instrumentation, error-message-writing, code-review, error-scenario-catalog"
prompt: "Review the error handling in this payment client: it calls the provider over HTTP, retries on failure and updates the order status."
---

# Review Error Handling

## Purpose
Find where failures are lost, misclassified, retried unsafely or shown badly, and give concrete fixes so the code fails predictably, recovers where it can and tells operators and users the right thing.

## When to use
- Incidents showed silent failures, duplicate side effects or misleading error messages.
- Code calls external systems (HTTP, queues, databases, files) and is about to go to production.
- A reviewer wants a focused look at exceptions, retries and fallbacks.

## When not to use
- System-level resilience (bulkheads, failover, capacity). Use `resilience-review`.
- Wording of user-facing messages only. Use `error-message-writing`.
- A general pull request review. Use `code-review`.

## Inputs
Required:
- The code (and its language) whose error handling is reviewed.

Optional, improves quality:
- Called services' error contracts and idempotency guarantees, SLOs/timeouts, team error-handling conventions, recent incidents.

If the external contract is unknown, state which findings depend on it and mark them `[UNKNOWN]`.

## Process
1. List failure points: every external call, parse, conversion, lock, resource acquisition and invariant check.
2. For each, classify errors: expected business outcome (e.g. insufficient funds) vs transient technical (timeout, 503) vs permanent technical (400, schema mismatch) vs programming bug.
3. Check detection: timeouts set on every remote call; status codes and response bodies checked; partial responses handled.
4. Check propagation: no empty or log-and-continue catches; no catching the base exception type except at boundaries; cause/context preserved when wrapping; business outcomes modeled as results or domain errors, not generic exceptions.
5. Check retries: only transient errors; bounded attempts with exponential backoff and jitter; total time within caller's timeout; the operation is idempotent (idempotency key) or retries are unsafe.
6. Check consistency: side effects across a failure (DB updated but call failed, or vice versa); transactions and compensations; outbox for "update and notify".
7. Check cleanup: resources released on all paths (finally/using/defer/with); locks released; no half-written files.
8. Check fallbacks and circuit breaking: fallback is correct for the business, not just "return empty"; degraded mode is visible.
9. Check reporting: one log entry per error at the right boundary with correlation id and no secrets or personal data; user-facing messages are actionable and leak no internals; API errors use a stable code.
10. Prioritize findings (Critical: data loss/duplicate money movement; High: silent failure; Medium: poor diagnosis; Low: style) and give code-level fixes.

## Output format
```markdown
# Error Handling Review: <unit>
## Failure Point Inventory
| # | Operation | Error classes | Current handling |

## Findings
| # | Severity | Location | Problem | Consequence | Fix |

## Recommended Pattern
<short code sketch for the main fix>

## Open Questions
```

## Quality checklist
- [ ] Every remote call has a timeout and a classified error path.
- [ ] Retries are limited to transient errors and to idempotent operations.
- [ ] No finding recommends catching everything without a boundary reason.
- [ ] Consistency across failures (DB vs external side effect) is analyzed.
- [ ] Logging advice avoids duplicates, secrets and personal data.

## Common pitfalls
- Retrying non-idempotent calls (payments, emails) and causing duplicates. Require an idempotency key or do not retry.
- Logging and rethrowing at every layer, producing five stack traces for one error. Log once at the boundary.
- Treating business outcomes as exceptions and technical failures as normal results, which confuses callers and metrics.

## Example
Input: "PaymentClient: call provider, catch Exception, retry 5 times, then set order to FAILED."

Excerpt of output:
| # | Severity | Location | Problem | Consequence | Fix |
|---|---|---|---|---|---|
| 1 | Critical | `charge()` retry loop | Retries on read timeout without idempotency key | Customer may be charged twice | Send `Idempotency-Key = orderId`; retry only connect errors/503 |
| 2 | High | `catch (Exception)` | Card declined treated like a technical error | Order marked FAILED and retried | Map declines to `PaymentDeclined` result; no retry |
