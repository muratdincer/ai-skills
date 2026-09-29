---
name: slo-definition
description: "Defines user-centric SLIs and SLOs for a service: identifies critical user journeys, chooses indicator types (availability, latency, freshness, correctness, throughput), specifies exact good/valid event definitions and measurement points, and sets targets and compliance windows with the resulting error budget. Use when a service needs reliability targets, when alerts are noisy or unrelated to user pain, or when someone asks what an SLO should be."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Define SLIs and SLOs"
  related: "error-budget-policy, alert-design, observability-plan, nfr-specification, kpi-definition"
  prompt: "Define SLIs and SLOs for our checkout API. We have load balancer logs and Prometheus metrics; business says checkout must 'always work'."
---

# Define SLIs and SLOs

## Purpose
Express how reliable a service must be in terms users feel, with precise, measurable indicators and targets, so that reliability work, alerting and release decisions share one objective definition.

## When to use
- A new or existing service has no agreed reliability targets.
- Existing targets are infrastructure-centric (CPU, host up) rather than user-centric.
- Business asks for "100%" or "always available" and a realistic target must be negotiated.

## When not to use
- The SLO exists and the question is what to do when budget burns. Use `error-budget-policy`.
- Alerts on existing SLOs must be designed. Use `alert-design`.
- Contractual commitments to customers are being drafted; SLOs inform them but an SLA needs legal and commercial review.

## Inputs
Required:
- Service description and its main users (people or other services).
- What users do with it (key requests, journeys, data they consume).

Optional, improves quality:
- Available telemetry and where it is measured (client, edge/load balancer, service, synthetic probes).
- Historical performance data, incidents, dependency SLOs.
- Business criticality, contractual SLAs, maintenance windows.

If the users and their key interactions are unknown, ask. Without historical data, targets are proposals marked `[PROPOSED]` to be validated against real data.

## Process
1. List critical user journeys (CUJs) and rank them by business impact; start with 1-3.
2. For each CUJ pick SLI types that reflect user pain: request/response → availability and latency; data pipelines → freshness, coverage, correctness; storage → durability; streaming → throughput and lag.
3. Specify each SLI as a ratio: good events / valid events. Define exactly what is valid (exclude health checks, client-caused 4xx where appropriate, synthetic traffic) and what is good (status class, latency threshold, correct response).
4. Choose the measurement point and state its blind spots (server-side misses network and client failures; edge is a common compromise; synthetics cover low-traffic paths).
5. Set targets from user expectation and historical performance, not from hope; express latency as percentile thresholds (e.g. 99% of requests under X ms) rather than averages.
6. Check achievability: a service cannot exceed the product of its hard dependencies' reliability without redundancy; flag conflicts.
7. Choose the compliance window (rolling 28 or 30 days is common) and compute the error budget in events or minutes.
8. Define ownership, review cadence, and what is out of scope (planned maintenance, specific clients).
9. Record SLAs separately if any, with the SLO stricter than the SLA to give a safety margin.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `error-budget-policy` for actions on burn, `alert-design` for burn-rate alerts, or `observability-plan` to close telemetry gaps.

## Output format
```markdown
# SLOs: <service>
Owner: <team> · Window: <rolling N days> · Review: <cadence>

## Critical User Journeys
1. <journey> – why it matters

## SLI Specifications
| CUJ | SLI type | Good events | Valid events | Measured at | Blind spots |

## SLO Targets
| SLI | Target | Window | Error budget | Basis (history / [PROPOSED]) |

## Dependencies and Achievability
## Exclusions
## Related SLA (if any)
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Each SLI is a good/valid ratio with exact inclusion and exclusion rules.
- [ ] SLIs describe user-visible behavior, not resource usage.
- [ ] Latency uses percentile thresholds, not averages.
- [ ] Targets are below 100% and justified by data or marked `[PROPOSED]`.
- [ ] Measurement point and its blind spots are stated.
- [ ] Error budget is computed for the window.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A 99.99% target on a service that depends on a 99.9% database with no redundancy. Check dependency math.
- Counting all 4xx as bad (users' own mistakes) or all as good (hides auth outages). Decide per status code.
- Too many SLOs. A handful per service that map to real journeys is actionable; dozens are ignored.

## Example
Input: "Checkout API, edge load-balancer logs available, ~2M requests/day."

Excerpt of output:
| CUJ | SLI type | Good events | Valid events | Measured at |
|---|---|---|---|---|
| Place order | Availability | responses not 5xx and not 429 | all POST /orders excluding synthetic probes | Edge LB |
| Place order | Latency | responses under `[TBD]` ms | same as above, successful only | Edge LB |

Target: availability 99.9% over rolling 28 days `[PROPOSED]` → budget ≈ 0.1% of valid requests (~56k of ~56M `[ASSUMPTION: volume stays at 2M/day]`).
