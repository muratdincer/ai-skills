---
description: Analyzes a stack trace or crash report to identify the failing frame, the exception chain and root cause candidates, and proposes fixes and the next diagnostic step. Use when a developer pastes an exception, stack trace, crash log, panic or unhandled error from any language or runtime and asks what went wrong or where to look.
related: debugging-hypotheses, log-analysis, bug-reproduction, error-handling-review, code-explanation
prompt: What is causing this stack trace? NullPointerException in OrderMapper.toDto called from OrderController.getOrder.
---

# Analyze a Stack Trace

## Purpose
Read a stack trace the way an experienced engineer does: find the frame where your code went wrong (not just where the exception surfaced), unwrap the cause chain, and turn it into ranked cause candidates with concrete fixes and checks.

## When to use
- An exception, crash, panic or unhandled promise rejection is available as text.
- A trace is long, wrapped or asynchronous and the real cause is unclear.
- A crash report from a mobile or desktop client needs a first diagnosis.

## When not to use
- There is no trace, only symptoms. Use `debugging-hypotheses` or `log-analysis`.
- The failure cannot be triggered and needs a reproduction first. Use `bug-reproduction`.

## Inputs
Required:
- The full stack trace including every "Caused by" / inner exception / chained section and the message text.

Optional, improves quality:
- The source of the frames in your own code, language/runtime and framework versions.
- When it happens (always, under load, after deploy) and the input or request that triggered it.
- Surrounding log lines with timestamps and correlation IDs.

If the trace is truncated ("... 42 more") and the missing part matters, say so and ask for the full version. Mask tokens, personal data and connection strings in the trace.

## Process
1. Identify runtime and format (JVM, .NET, Python, Node.js, Go, Swift/Kotlin crash, native). Note whether frames are ordered innermost-first or outermost-first.
2. Read the full trace, including every "Caused by", inner, aggregated and suppressed exception; do not stop at the first line. Unwrap the exception chain: list each exception type and message from outermost to root cause. The deepest cause is usually the most informative.
3. Split frames into framework/library frames and application frames; find the topmost application frame in the root cause — that is the primary suspect location.
4. Interpret the exception type precisely (null dereference, index out of range, timeout, deadlock detection, serialization, class loading/version mismatch, out of memory, cancellation) and what state must have been true for it to occur.
5. For async or reactive traces, reconstruct the logical call path (continuations, thread pool, event loop) and note where context was lost.
6. Check for environmental signatures: version conflicts (method not found, class cast between identical names), configuration (missing key, bad URL), resource exhaustion (pool, file handles, memory), permissions.
7. Produce ranked cause candidates, each with the evidence from the trace, a quick verification (log to add, value to inspect, test to write) and a proposed fix.
8. Distinguish the fix from the guard: trace the bad value backwards through the data flow to where it was created, and fix the invalid state at its origin; add defensive handling only where the input is truly untrusted.
9. Recommend a regression test that reproduces the failing state.
10. If no candidate can be verified from the trace alone, suggest `debugging-hypotheses` (no fix until the root cause is confirmed) or `log-analysis` for surrounding events; if the fix concerns exception handling design, suggest `error-handling-review`.

## Output format
```markdown
# Stack Trace Analysis: <exception type> in <component>
**Runtime:** ...  **Root cause exception:** <type: message>
**Primary suspect frame:** <class/function:line>

## Exception Chain
1. <outer> → 2. <inner> → 3. <root cause>

## What the Trace Tells Us
- ...

## Cause Candidates
| # | Candidate | Evidence | How to verify | Proposed fix | Likelihood |
|---|---|---|---|---|---|

## Regression Test
- ...

## Missing Information
- ...
```

## Quality checklist
- [ ] The root cause exception, not only the outer wrapper, is identified.
- [ ] The primary suspect is an application frame, with framework frames explained, not blamed.
- [ ] Each candidate cites evidence from the trace and a verification step.
- [ ] Fixes address the origin of the invalid state, not just catch the exception.
- [ ] Secrets and personal data from the trace are not repeated in the output.
- [ ] Assumptions about unseen code are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Diagnosing the outermost exception (e.g., a generic "request failed") and ignoring the nested cause.
- Blaming the framework because it owns the top frames. The defect is almost always in the first application frame or in data passed to the framework.
- Fixing a null reference with a null check that hides the real bug (why was it null?). Trace the value back to where it should have been set.

## Example
Input: `NullPointerException: Cannot invoke "Customer.getName()" because "order.customer" is null at OrderMapper.toDto(OrderMapper.java:27) at OrderController.getOrder(OrderController.java:45)`.

Excerpt of output:
- Primary suspect: `OrderMapper.toDto:27` — assumes every order has a loaded customer.
- Candidate 1 (High): Customer relation is lazy and not fetched in this query path. Verify: check the repository method used by `getOrder`. Fix: fetch the relation in that query.
- Candidate 2 (Medium): Orders created by guest checkout have no customer by design. Verify: query orders with null customer_id. Fix: model guest orders explicitly and map a guest DTO; add a test with a guest order.
