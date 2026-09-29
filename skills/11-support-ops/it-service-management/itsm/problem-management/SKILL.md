---
name: problem-management
description: "Runs problem management for recurring or major incidents: groups related incidents, frames the problem, drives evidence-based root cause analysis, records a known error with workaround, and proposes permanent fixes through change control with verification criteria. Use when the same incident type keeps recurring, after a major incident, when incident trends point to an underlying cause, or when a problem record must be opened, progressed or closed."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: it-service-management
  area: itsm
  title: "Run problem management"
  related: "known-error-article, five-whys, fishbone-analysis, change-request-rfc, postmortem"
  prompt: "Open a problem record: we had 7 incidents in 3 weeks where the nightly batch overran and the morning reports were late; each was fixed by restarting the job."
---

# Run Problem Management

## Purpose
Find and remove the underlying cause of incidents instead of restoring service again and again, so incident volume, downtime and support effort fall measurably.

## When to use
- Several incidents share a symptom, component or time pattern.
- A major incident was resolved with a workaround and the root cause is still open.
- Trend analysis (by category, CI, change, time) shows a hotspot worth investigating.

## When not to use
- Service is down now and must be restored. Use `incident-response`.
- A blameless write-up of one specific incident is requested. Use `postmortem`.
- Only the knowledge base article for an already confirmed cause is needed. Use `known-error-article`.

## Inputs
Required:
- The incidents (IDs, symptoms, times, resolutions) or the pattern that triggered the problem.

Optional, improves quality:
- Configuration items involved, recent changes, monitoring data, logs, vendor information.
- Business impact per incident (downtime, users, cost if known).
- The organization's problem record template, priority scheme and RCA method preference.

If there is no incident data, ask for at least the incident list with dates and resolutions. Never estimate cost or downtime; mark missing values `[UNKNOWN]`. Mask personal data in incident excerpts.

## Process
1. Group the incidents: list IDs, first/last occurrence, frequency, affected configuration items, resolution applied, and confirm they share a symptom. Exclude outliers with a stated reason.
2. Write the problem statement: what fails, where, how often, since when, and the cumulative impact. It states the symptom pattern, not a presumed cause.
3. Prioritize the problem from cumulative impact, recurrence rate and risk of escalation, and assign a problem owner and target date for RCA.
4. Build a timeline and correlate with changes (releases, config, capacity, data volume, vendor updates) and external events; every correlation is a hypothesis until tested.
5. Run root cause analysis with an explicit method (for example, five whys for a linear chain, fishbone for many factors, fault tree or Kepner-Tregoe is/is-not for comparisons). Record evidence for and against each hypothesis.
6. Test hypotheses one variable at a time (reproduce in a test environment, controlled config change, extra logging). Do not declare a root cause without evidence; if three proposed fixes fail, question the assumptions and the design, not just the next patch.
7. Record the known error once the cause or a reliable workaround is confirmed; separate the workaround (restores service) from the permanent fix (removes cause).
8. Propose permanent fix options with cost, risk and effort, and raise a change through change control for the chosen one.
9. Define verification: the metric and observation period that prove the fix worked (for example, zero overruns in 30 consecutive runs) and the monitoring that will detect recurrence.
10. Close the problem only after verification; record lessons learned, contributing factors (process, monitoring, capacity) and follow-up actions with owners.
11. Hand off: suggest `known-error-article` for the knowledge base, `change-request-rfc` for the permanent fix, or `five-whys` / `fishbone-analysis` for a deeper RCA session.

## Output format
```markdown
# Problem: <PRB ID> – <symptom pattern>
| Field | Value |
|---|---|
| Status | new / under investigation / known error / fix in change / verified / closed |
| Owner / RCA target date | <...> |
| Priority | <P> – <cumulative impact and recurrence> |
| Linked incidents | <IDs, count, period> |
| Configuration items | <...> |

## Problem Statement
<what, where, how often, since when, impact>
## Timeline and Correlations
| Date | Event | Source | Correlated? |
|---|---|---|---|
## Root Cause Analysis (<method>)
| Hypothesis | Evidence for | Evidence against | Test / result |
|---|---|---|---|
- Root cause: <confirmed statement> or [UNKNOWN – investigation continues]
- Contributing factors: ...
## Known Error
- Workaround: ... Known error article: <ID / to be written>
## Permanent Fix
| Option | Effort | Risk | Chosen? | Change ID |
|---|---|---|---|---|
## Verification
- Success metric: ... Observation period: ... Monitoring: ...
## Actions
| Action | Owner | Due |
|---|---|---|
```

## Quality checklist
- [ ] The problem statement describes the symptom pattern and impact, not a presumed cause.
- [ ] Every linked incident shares the symptom; exclusions are justified.
- [ ] Root cause is supported by evidence; untested ideas remain hypotheses or `[UNKNOWN]`.
- [ ] Workaround and permanent fix are separated, and the fix goes through change control.
- [ ] Closure depends on a measurable verification period.
- [ ] No invented numbers; missing downtime or cost is `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Closing the problem when the workaround is documented. A known error is a milestone, not the end.
- Stopping at "human error" or "bug in job". Ask why the process or monitoring allowed it.
- Correlating with the latest change and calling it the cause without a test.
- Running RCA as a blame exercise; people withhold information and the real cause stays hidden.

## Example
Input: "7 incidents in 3 weeks where the nightly batch overran and morning reports were late; each fixed by restarting."

Excerpt of output:
- Problem statement: The nightly settlement batch exceeded its 06:00 completion window 7 times in 21 days (INC-...); morning reports were late each time. Restart was the only resolution.
- Correlation [ASSUMPTION]: overruns started after the month-end data volume increase; also coincides with DB index maintenance moved to 02:00 (change CHG-...).
- Test: run batch in staging with production volume, with and without concurrent index maintenance.
- Verification: 30 consecutive runs completing before 05:30 with alerting at 05:00.
