---
name: pipeline-failure-triage
description: "Analyzes a failed CI/CD run from its logs and context, classifies the failure (code, test, flaky, dependency, infrastructure, configuration, credentials), identifies the most likely cause with evidence and proposes a fix and a prevention step. Use when a build, test, scan or deploy job fails and someone pastes the log or error."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: devops-engineer
  area: cicd
  title: "Triage a pipeline failure"
  related: "pipeline-design, flaky-test-analysis, log-analysis, stack-trace-analysis, dependency-upgrade"
  prompt: "Our main branch pipeline started failing at the Docker build step this morning, here is the log. What is wrong and how do we fix it?"
---

# Triage a Pipeline Failure

## Purpose
Get a red pipeline back to green quickly by separating the real cause from noise in the log, and leave a fix that prevents the same failure from recurring.

## When to use
- A build, test, scan, packaging or deployment job failed and the log is available.
- A pipeline fails intermittently and the team suspects flakiness or infrastructure.
- A pipeline broke after a dependency, runner image or configuration change.

## When not to use
- The problem is a flaky test suite in general, not one failure. Use `flaky-test-analysis`.
- The application fails in production, not in the pipeline. Use `log-analysis` or `incident-response`.
- The pipeline needs a redesign. Use `pipeline-design`.

## Inputs
Required:
- The failing job log (at least from the first error to the end) or the exact error text.

Optional, improves quality:
- Pipeline definition for the failing stage, last green run and what changed since (commits, dependency bumps, runner image, secrets rotation).
- Whether the failure reproduces on retry or locally.

If there is no log or error text, ask for it. Do not guess from the job name alone.

## Process
1. Find the first real error, not the last line. Skip cascading errors and the generic "exit code 1" wrapper.
2. Classify the failure: compile/code, test assertion, flaky/timing, dependency resolution, network/registry, infrastructure/runner (disk, memory, timeout), configuration/variables, credentials/permissions, quota/rate limit, policy gate (scan, coverage).
3. Correlate with change: compare with the last green run. List what differs (commits, lockfile, base image tag, runner version, secrets, external service).
4. Form 1-3 hypotheses ranked by likelihood, each with the log evidence that supports it and what would disprove it.
5. Propose the cheapest discriminating check for the top hypothesis (rerun with debug logging, pin previous version, run locally with same image, check expiry of a credential).
6. Propose the fix: immediate unblock (revert, pin, retry with reason) and proper fix (code change, config change, dependency update).
7. Decide on retry: retrying is acceptable only when the class is transient and evidence shows it. Otherwise do not recommend retry as the fix.
8. Propose prevention: pinning, caching, a new check, quarantining a flaky test with a ticket, alerting on credential expiry.
9. Note security concerns: if the log exposes a secret, recommend rotating it and masking logs.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `flaky-test-analysis` if the failure is an intermittent test, `dependency-upgrade` if a dependency change broke the build, or `pipeline-design` if the cause is structural.

## Output format
```markdown
# Pipeline Failure Triage: <pipeline / job / run>
- Failing step: <step>
- First error: `<quoted line>`
- Class: <class>
- Changed since last green: <list or [UNKNOWN]>

## Hypotheses
| # | Hypothesis | Evidence | Check to confirm | Likelihood |

## Fix
- Unblock now: ...
- Proper fix: ...
## Prevention
- ...
## Open Questions
```

## Quality checklist
- [ ] The quoted first error really appears in the provided log.
- [ ] Hypotheses cite evidence; none is stated as fact without it.
- [ ] Retry is not proposed as a fix for a deterministic failure.
- [ ] The fix distinguishes an immediate unblock from the durable fix.
- [ ] Any exposed secret is flagged for rotation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reading the last error line, which is usually a consequence. Search upward for the first failure.
- Blaming flakiness without evidence. Check whether it reproduces and whether timing or ordering is involved.
- Fixing by unpinning or bumping everything at once. Change one variable at a time.

## Example
Input: Log shows `failed to solve: node:20: failed to resolve source metadata ... toomanyrequests` during image build; last green run was yesterday.

Excerpt of output:
- Class: network/registry (rate limit).
- Hypothesis 1: anonymous pulls from the public registry hit the rate limit after runner pool scaling. Evidence: `toomanyrequests`. Check: rerun on a runner with authenticated pulls.
- Proper fix: pull base images through an internal mirror/cache and pin by digest.
