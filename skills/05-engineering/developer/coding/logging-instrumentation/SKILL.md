---
description: "Adds structured logs, metrics and distributed traces to code at the points that answer real operational questions, with consistent field names, correct levels, low-cardinality metric labels, trace context propagation and no secrets or personal data. Use when a feature is going to production, an incident showed missing visibility, or someone asks to add logging, metrics, tracing or telemetry (e.g. OpenTelemetry) to code."
related: "observability-plan, alert-design, slo-definition, error-handling-review, log-analysis"
prompt: "Add logging, metrics and tracing to this order import job that reads a file, validates rows and calls the inventory API."
---

# Add Logging and Instrumentation

## Purpose
Make the code's behavior observable in production so that operators can detect, diagnose and measure it, while keeping telemetry cheap, consistent and free of sensitive data.

## When to use
- New code or a new integration is about to be released.
- An incident or support case could not be diagnosed from existing telemetry.
- An SLO or alert needs a signal the code does not emit yet.

## When not to use
- Designing observability for a whole system or service landscape. Use `observability-plan`.
- Defining alert rules and thresholds. Use `alert-design`.
- Investigating existing logs. Use `log-analysis`.

## Inputs
Required:
- The code to instrument and its language/runtime.

Optional, improves quality:
- The team's telemetry stack and conventions (log format, field names, metric naming, OpenTelemetry usage), existing SLOs, known incident questions.

If the stack is unknown, use vendor-neutral OpenTelemetry concepts and semantic conventions and mark stack-specific details `[TBD]`.

## Process
1. Write the operational questions first: Is it working? How fast? How often does it fail and why? Which input caused it? What is the backlog?
2. Map each question to a signal: metric (rates, durations, sizes, saturation), trace/span (latency across hops), log (discrete event with context).
3. Metrics: use RED for request paths (rate, errors, duration) and USE for resources; histograms for durations; labels with bounded cardinality only (never user id, order id, raw URL).
4. Traces: create spans around external calls and significant internal steps; propagate context across HTTP/messaging; record errors on spans; add attributes following semantic conventions.
5. Logs: structured key-value/JSON; one event per meaningful state change or failure; include correlation/trace id, operation, outcome, duration, stable error code.
6. Levels: ERROR = needs action, WARN = degraded but handled, INFO = business-relevant lifecycle events, DEBUG = diagnostic off by default. No logging inside tight loops without sampling.
7. Privacy and security: never log secrets, tokens, full card numbers or passwords; mask or hash personal data; log IDs not payloads.
8. Keep instrumentation out of business logic where possible (middleware, decorators, interceptors).
9. Define how to verify: a test or local run showing the log line, the metric increment and the span.
10. Suggest dashboard panels and alert candidates linked to the signals, without inventing thresholds.
11. If the goal continues, suggest `alert-design` to turn the candidates into alerts or `observability-plan` for service-wide coverage.

## Output format
```markdown
# Instrumentation: <component>
## Operational Questions → Signals
| Question | Signal type | Name | Labels / attributes |

## Code Changes
<code with instrumentation>

## Log Events
| Event | Level | Fields | When |

## Privacy Notes
## Verification
## Dashboard / Alert Candidates
```

## Quality checklist
- [ ] Every signal answers a stated operational question.
- [ ] Metric labels have bounded cardinality.
- [ ] Trace context is propagated across every outbound call and message.
- [ ] No secrets or unmasked personal data appear in logs, labels or span attributes.
- [ ] Log levels follow the stated rules and no event is logged twice.
- [ ] Names follow the team's convention or OpenTelemetry semantic conventions.
- [ ] Inferences are labeled `[ASSUMPTION]` and listed as assumptions or open questions; nothing unsupported is stated as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- High-cardinality labels (user id, full path) that explode metric storage and cost.
- Logging whole request/response bodies "for debugging", leaking personal data.
- Counting only failures; without total attempts you cannot compute an error rate.

## Example
Input: "Order import job: read file, validate rows, call inventory API per row."

Excerpt of output:
- Metric `order_import_rows_total{result="imported|invalid|failed"}` and histogram `order_import_duration_seconds`.
- Span `inventory.reserve` per call with `http.response.status_code`; job span links row spans.
- Log `import.completed` INFO with `file_id`, `rows_total`, `rows_invalid`, `duration_ms`; invalid rows logged by row number and error code, never with customer name or address.
