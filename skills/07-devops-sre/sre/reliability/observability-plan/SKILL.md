---
name: observability-plan
description: "Plans observability for one or more services: which metrics, structured logs and distributed traces to emit, correlation and context propagation, cardinality and retention budgets, dashboards per audience and gaps against SLOs and runbooks. Use when a service is being built or onboarded, when incidents take long to diagnose, when telemetry cost is out of control, or when someone asks what to instrument."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Plan observability"
  related: "slo-definition, alert-design, logging-instrumentation, dashboard-spec, runbook"
  prompt: "Plan observability for our order service: .NET API, Kafka consumer, PostgreSQL. We only have container CPU/memory graphs and unstructured logs today."
---

# Plan Observability

## Purpose
Define what telemetry each service emits, how it is correlated, stored and visualized, so that on-call can answer "is it broken, for whom, and why" quickly, at a cost the organization accepts.

## When to use
- A new service is being designed or a service is being onboarded to production.
- Postmortems show long time to detect or diagnose because signals were missing or uncorrelated.
- Telemetry volume or cost has grown without a plan (high-cardinality metrics, debug logs in production).

## When not to use
- Only the alerting rules need design and signals exist. Use `alert-design`.
- The task is adding log statements to specific code. Use `logging-instrumentation`.
- A single business dashboard is needed. Use `dashboard-spec`.

## Inputs
Required:
- Service list with a short description of each (type: API, worker, consumer, batch, frontend) and main dependencies.
- What telemetry exists today, or a statement that it is unknown.

Optional, improves quality:
- SLOs and critical user journeys; recent incidents and what was hard to diagnose.
- Telemetry backend constraints, retention limits, budget.
- Data classification of what may appear in logs (personal data, secrets).

If the service list is missing, ask for it. Do not assume a vendor; describe signals in neutral terms (an open standard such as OpenTelemetry may be named as a reference).

## Process
1. Map each service's role and its request/data flow, including async hops (queues, topics, schedulers) where context is usually lost.
2. Define golden signals per service type: request services use rate, errors, duration (RED) plus saturation; resources use utilization, saturation, errors (USE); consumers add lag and age of oldest message; batch jobs add last success time, duration and records processed.
3. Tie SLIs to the metrics above and confirm each SLO can be computed from them; list gaps.
4. Specify structured logging: mandatory fields (timestamp, level, service, version, environment, trace ID, span ID, request or correlation ID, tenant if relevant), event naming, levels policy (no debug in production by default), and what must never be logged (secrets, tokens, full personal data; mask or hash instead).
5. Specify tracing: entry and exit spans, context propagation across HTTP and messaging headers, span attributes to include, sampling strategy (head-based rate plus tail-based keep for errors and slow requests) and its effect on SLI accuracy.
6. Set a cardinality and volume budget: forbid unbounded labels (user ID, full URL, request ID) on metrics, cap log volume per service, and define retention per signal (e.g. high-resolution short, aggregates long) `[PROPOSED]`.
7. Design dashboards per audience: service overview (SLOs and golden signals), dependency view, and deep-dive; every dashboard answers one question and links to traces and logs with the same time range and filters.
8. Cross-check against alerts and runbooks: every paging alert has the signals needed for its first diagnostic step.
9. Define ownership, rollout order (highest-risk service first) and a verification step: a synthetic failure or recent incident replayed to prove the signals show it.
10. Label every inference `[ASSUMPTION]`, list open questions, and suggest next skills: `alert-design` for paging, `slo-definition` if SLIs are missing, `logging-instrumentation` for code changes, `runbook` for diagnosis steps.

## Output format
```markdown
# Observability Plan: <system>
Scope: <services> · Owner: <team> · Backend: <neutral description or [UNKNOWN]>

## Service Signal Matrix
| Service | Type | Metrics (RED/USE/lag) | Key log events | Trace spans | SLI coverage |

## Logging Standard
- Mandatory fields / levels policy / never-log list

## Tracing and Context Propagation
## Cardinality, Volume and Retention Budget
| Signal | Resolution | Retention | Limit |

## Dashboards
| Name | Audience | Question it answers | Links |

## Gaps vs. SLOs, Alerts, Runbooks
## Rollout and Verification
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every service has golden signals appropriate to its type, including async lag where relevant.
- [ ] Trace and correlation IDs propagate across every synchronous and asynchronous hop.
- [ ] Every SLO can be computed from the planned signals, or the gap is listed.
- [ ] Unbounded metric labels are excluded and retention is defined per signal.
- [ ] A never-log list covers secrets and personal data, with masking guidance.
- [ ] A verification step proves the signals would show a real failure.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Dashboards full of host metrics and no user-facing signal. Start from SLIs and golden signals, add resources below them.
- Losing context at the message broker. Propagate trace context in message headers and record consumer spans linked to the producer.
- Sampling that silently drops the errors you need. Keep errors and slow traces regardless of head sampling rate.

## Example
Input: ".NET order API, Kafka consumer, PostgreSQL; only container CPU/memory and plain-text logs."

Excerpt of output:
| Service | Type | Metrics | Trace spans | SLI coverage |
|---|---|---|---|---|
| order-api | API | rate, 5xx ratio, p95/p99 duration per route template | inbound HTTP, DB query, Kafka produce | availability, latency |
| order-consumer | Consumer | consumer lag, oldest message age, processing errors | Kafka consume linked to producer span | freshness `[PROPOSED]` |

Gap: order status freshness SLO cannot be computed today; needs message age metric.
