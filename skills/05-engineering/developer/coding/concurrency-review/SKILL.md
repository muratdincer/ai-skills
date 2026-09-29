---
name: concurrency-review
description: "Reviews code for concurrency defects: data races, check-then-act and lost updates, deadlocks and lock ordering, unsafe publication, async/await misuse, thread-pool starvation, and duplicate or out-of-order processing in distributed consumers, with a concrete interleaving and fix per finding. Use when code uses threads, async, locks, shared state, background workers, message consumers or concurrent database updates, or when someone reports intermittent failures that look timing-related."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: coding
  title: "Review concurrency"
  related: "code-review, error-handling-review, debugging-hypotheses, resilience-review, integration-test-writing"
  prompt: "Review this wallet top-up service for concurrency problems; it reads the balance, adds the amount and saves, and is called from both the API and a message consumer."
---

# Review Concurrency

## Purpose
Find the interleavings that corrupt data, hang the system or duplicate side effects before they appear in production, and give fixes whose correctness can be argued, not just hoped for.

## When to use
- Code shares mutable state between threads, tasks, requests or service instances.
- Async code, locks, background workers or message consumers are introduced or changed.
- A bug is intermittent, load-dependent or disappears under a debugger.

## When not to use
- General pull request review across all aspects. Use `code-review`.
- System-level failure modes such as timeouts, retries and circuit breakers. Use `resilience-review`.
- The failure is already reproduced and needs root-causing. Use `debugging-hypotheses`.

## Inputs
Required:
- The code and its language/runtime (memory model and async model differ).

Optional, improves quality:
- How it is invoked (per request, scheduled, consumer, number of instances), the data store and its isolation level, message broker delivery guarantees, observed symptoms.

If the deployment shape (single vs multiple instances) is unknown, review for both and mark findings that depend on it `[ASSUMPTION]`.

## Process
1. Inventory shared state: fields, statics, caches, singletons, collections, files, database rows, external resources. Note who reads and writes each.
2. Identify concurrency sources: threads, thread pools, async continuations, parallel loops, request handlers, multiple instances, consumers with parallelism, retries and redeliveries.
3. For each shared item, check invariants under interleaving: check-then-act, read-modify-write, lazy initialization, iteration during modification, non-atomic compound updates.
4. Locks: minimal scope, no I/O or awaits inside critical sections where the runtime forbids or penalizes it, consistent lock ordering, timeouts, no locking on publicly reachable objects.
5. Async: no sync-over-async blocking, no fire-and-forget without error handling, cancellation propagated, no async void outside event handlers, context capture rules of the runtime respected.
6. Distributed and database: lost updates (use optimistic concurrency with a version/ETag or atomic update statements), unique constraints for idempotency, at-least-once delivery handled with idempotency keys, ordering assumptions stated per key.
7. Resources: pool sizes, unbounded queues, thread-pool starvation, back-pressure.
8. For every finding, write a concrete interleaving (T1 does X, T2 does Y, result Z) and rate severity: Critical (data corruption, money, deadlock), High (duplicate side effect, starvation), Medium (stale read with impact), Low (hardening).
9. Propose the simplest correct fix: remove sharing (immutability, confinement), use an atomic primitive or concurrent collection, database-level atomicity, or a lock, in that order of preference.
10. Specify how to test it: stress or race test, deterministic scheduling, concurrent integration test against the real store, or a race detector if the runtime offers one.
11. If the goal continues, suggest `integration-test-writing` for concurrent tests against real boundaries or `resilience-review` for system-level retry and failure behavior.

## Output format
```markdown
# Concurrency Review: <component>
Execution model: <threads/async/instances/consumers> · Assumptions: <list>

## Shared State Inventory
| State | Readers | Writers | Protection today |

## Findings
| # | Severity | Location | Interleaving | Impact | Fix |

## Test Plan
- ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Every finding has a concrete interleaving, not just "may be unsafe".
- [ ] Multi-instance and redelivery scenarios are considered, not only in-process threads.
- [ ] Fixes prefer removing sharing or database atomicity over broad locks.
- [ ] No fix introduces I/O or awaits inside a lock without saying why it is safe.
- [ ] Each Critical/High finding has a test approach.
- [ ] Deployment-dependent findings are marked `[ASSUMPTION]` and listed in open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Fixing a lost update with an in-process lock when the service runs on several instances. Use the database (version column, conditional update) instead.
- Treating a thread-safe collection as making compound operations atomic; "contains then add" is still a race.
- Assuming a message broker delivers exactly once or in global order.

## Example
Input: "TopUp(walletId, amount): balance = repo.Get(walletId); balance += amount; repo.Save(balance). Called from API and consumer; 3 instances."

Excerpt of output:
| # | Severity | Location | Interleaving | Impact | Fix |
|---|---|---|---|---|---|
| 1 | Critical | `TopUp` | T1 reads 100, T2 reads 100, T1 saves 150, T2 saves 120 | Lost top-up of 50 | `UPDATE wallet SET balance = balance + @amt WHERE id=@id` or version-checked update with retry |
| 2 | High | Consumer | Redelivery after timeout applies the same top-up twice | Double credit | Store `topup_id` with a unique constraint in the same transaction |
