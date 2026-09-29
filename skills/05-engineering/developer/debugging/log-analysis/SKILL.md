---
description: Analyzes application, infrastructure or access logs to build a timeline, correlate events across services by request or trace ID, detect anomalies and error clusters, and state what the evidence supports and what it does not. Use when a developer shares log excerpts or exports around an incident, failure, slowdown or odd behavior and asks what happened, when it started or which component is at fault.
related: stack-trace-analysis, debugging-hypotheses, incident-response, postmortem, logging-instrumentation
prompt: Here are logs from the API gateway and the order service between 14:00 and 14:20. What happened when checkout started failing?
---

# Analyze Logs

## Purpose
Turn raw log lines into an evidence-based account: a timeline of what happened, which component failed first, how the failure propagated, and which conclusions are proven versus inferred. The output feeds debugging, incident response and postmortems.

## When to use
- Logs from one or more services around a failure window are available.
- Error rates or latencies changed and the cause is unclear.
- A single request must be traced across services.

## When not to use
- Only a single exception with a stack trace is at hand. Use `stack-trace-analysis`.
- Designing what to log going forward. Use `logging-instrumentation` or `observability-plan`.
- Coordinating an active incident. Use `incident-response`.

## Inputs
Required:
- Log lines or an export covering the time window, with timestamps.

Optional, improves quality:
- The symptom and when it was first noticed; deployments, config or traffic changes in the window.
- Log schema (fields, levels), time zone of each source, service topology.
- Baseline logs from a healthy period for comparison.

If timestamps or time zones are ambiguous, state the assumption explicitly before building the timeline. Mask personal data, tokens and IPs of individuals in any quoted line.

## Process
1. Normalize: convert all timestamps to one time zone (preferably UTC), note clock-skew risks between hosts, and identify key fields (level, service, trace/correlation ID, user/tenant ID, endpoint, status, latency).
2. Establish the symptom window: first and last occurrence of the error signature, and the last known good point.
3. Cluster messages by signature (message template with variable parts removed) and count per minute; highlight signatures that are new or whose rate changed in the window.
4. Find the earliest anomaly: the first new signature, first latency jump, or first resource warning (pool exhaustion, GC, disk, retries) before the user-visible error.
5. Correlate across sources by trace/correlation ID or tight time alignment; follow one failing request end to end and one successful request for contrast.
6. Map propagation: upstream cause → downstream symptoms (timeouts, retries, circuit breaker opens, queue backlog). Watch for retry storms amplifying load.
7. Check coincident changes: deployments, config reloads, certificate expiry, scheduled jobs, traffic spikes.
8. Separate findings into Confirmed (directly seen in logs), Inferred (consistent with logs but not proven) and Unknown (evidence missing).
9. List the gaps: missing fields, sampled or dropped logs, services without logs, and what to collect next.

## Output format
```markdown
# Log Analysis: <symptom> (<window, time zone>)
## Summary
<3-4 sentences: what happened, first failing component, impact>

## Timeline
| Time (UTC) | Source | Event | Evidence (masked excerpt) |
|---|---|---|---|

## Error Signatures
| Signature | Count | First seen | Rate change | Services |
|---|---|---|---|---|

## Propagation
<cause> → <effect> → <user-visible symptom>

## Findings
- Confirmed: ...
- Inferred: ...
- Unknown: ...

## Next Steps and Missing Evidence
- ...
```

## Quality checklist
- [ ] All times are in one stated time zone and skew assumptions are noted.
- [ ] The earliest anomaly is identified, not just the loudest error.
- [ ] At least one request is traced end to end, or the lack of correlation IDs is flagged.
- [ ] Confirmed, inferred and unknown findings are clearly separated.
- [ ] Quoted log lines are masked for personal data and secrets.
- [ ] Coincident changes (deploys, jobs, traffic) were checked.

## Common pitfalls
- Treating the highest-volume error as the cause. Downstream timeouts and retries are often louder than the upstream root cause.
- Mixing local and UTC timestamps, which reorders the timeline and suggests false causality.
- Concluding "no errors" from logs that are sampled, filtered by level, or missing for one service. State the coverage.

## Example
Input: Gateway and order service logs, 14:00-14:20 UTC; checkout errors reported from 14:07.

Excerpt of output:
- 14:05:12 order-service: first `connection pool exhausted (max=20)` warning; no deploy in window; nightly report job logged start at 14:05:00 on the same database. 
- 14:07:03 gateway: 504s on `POST /checkout` begin; retries x3 per request triple order-service load.
- Confirmed: pool exhaustion precedes gateway 504s. Inferred: report job holds connections. Unknown: database-side locks (no DB logs provided).
