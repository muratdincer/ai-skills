---
name: pipeline-design
description: "Designs a CI/CD pipeline end to end: stages, quality and security gates, artifact handling, environments and promotion rules, independent of the CI product. Use when a team sets up a new pipeline, restructures a slow or fragile one, or needs to document how code moves from commit to production."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: devops-engineer
  area: cicd
  title: "Design a CI/CD pipeline"
  related: "environment-strategy, deployment-strategy, branching-strategy, release-quality-gate, secrets-management-plan"
  prompt: "Design a CI/CD pipeline for our .NET API that deploys to Kubernetes in dev, staging and prod, with a manual approval before prod."
---

# Design a CI/CD Pipeline

## Purpose
Produce a pipeline design where every change is built once, verified by explicit gates and promoted as the same immutable artifact to production, with fast feedback and an auditable trail.

## When to use
- A new service or repository needs a pipeline.
- An existing pipeline is slow, flaky, or rebuilds per environment.
- Audit or compliance requires documented gates and approvals.
- The team is moving to more frequent or automated delivery.

## When not to use
- A specific run failed and needs diagnosis. Use `pipeline-failure-triage`.
- Only the rollout mechanics (canary, blue-green) are in question. Use `deployment-strategy`.
- Only the environment landscape is in question. Use `environment-strategy`.

## Inputs
Required:
- Application type, language/build tool and deployment target (VM, container platform, serverless, mobile store, package registry).
- Target environments and who may approve promotion to production.

Optional, improves quality:
- Branching model, current pipeline and its durations, test suites and their run times.
- Compliance constraints (segregation of duties, change approval, signed artifacts).
- Current DORA metrics (deployment frequency, lead time, change failure rate, recovery time).

If the deployment target or environments are missing, ask. Record everything else as open questions.

## Process
1. Map the trigger model: which events start which pipeline (pull request, merge to main, tag, schedule, manual).
2. Define the commit stage (target under 10 minutes): restore with lockfile, compile, unit tests, lint/static analysis, secret scan, dependency (SCA) scan.
3. Define the artifact: build once, version it (commit SHA plus SemVer if released), sign it, produce an SBOM, push to one registry. Forbid rebuilding per environment.
4. Define the acceptance stage: deploy the artifact to an ephemeral or shared test environment, run integration, contract, API and smoke tests; run DAST or container scans where relevant.
5. Define gates per stage with an explicit rule: blocking vs warning, threshold (e.g. no critical vulnerabilities, coverage not decreasing), and who may override with what record.
6. Define promotion: same artifact digest, environment-specific configuration injected at deploy time, secrets pulled from a secret store, approval points and segregation of duties if required.
7. Define the production deployment step: strategy reference, automated post-deploy verification, automatic or one-click rollback.
8. Design for speed: caching, parallel jobs, test sharding, change-based path filters; list expected duration per stage.
9. Design for security of the pipeline itself: least-privilege runner identities, short-lived credentials (OIDC-style federation where available), pinned action/plugin versions, protected branches.
10. Define observability of the pipeline: stage durations, failure rates, flaky-test tracking, DORA metric sources.
11. Fill the template and mark unknowns.
12. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `environment-strategy` for the target environments, `deployment-strategy` for the production rollout, or `secrets-management-plan` for pipeline credentials.

## Output format
```markdown
# CI/CD Pipeline Design: <service>
## Triggers
| Event | Pipeline | Stages run |
## Stages
| # | Stage | Steps | Target duration | Gate (blocking rule) | Override by |
## Artifact
- Type / registry / versioning / signing / SBOM
## Environments and Promotion
| From | To | Trigger | Approval | Checks after deploy |
## Configuration and Secrets
## Production Deployment and Rollback
## Pipeline Security
## Metrics
## Open Questions / Assumptions
```

## Quality checklist
- [ ] The artifact is built once and promoted by digest; no per-environment rebuilds.
- [ ] Every gate has a measurable rule and an owner for overrides.
- [ ] Commit-stage feedback target is stated and realistic.
- [ ] No long-lived cloud credentials or plaintext secrets in pipeline variables.
- [ ] Rollback is defined and does not depend on a new build.
- [ ] Unknowns are marked `[UNKNOWN]` or `[ASSUMPTION]`, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Rebuilding for each environment, which means production runs an untested binary. Promote the digest.
- Putting slow end-to-end suites in the commit stage. Move them to acceptance and keep the commit stage fast.
- Gates that only warn and are ignored. Make critical gates blocking and log overrides.
- Floating versions of pipeline plugins or base images. Pin them and update deliberately.

## Example
Input: ".NET 8 API, Docker image to Kubernetes, dev/staging/prod, prod needs approval from the product owner."

Excerpt of output:
| # | Stage | Steps | Target duration | Gate |
|---|---|---|---|---|
| 1 | Commit | restore (locked), build, unit tests, analyzers, secret scan, SCA | 8 min | Tests pass; no critical CVE |
| 2 | Package | image build, sign, SBOM, push by digest | 4 min | Image scan: no critical |
| 3 | Staging | deploy digest, API + contract tests, smoke | 12 min | 100% smoke pass |
| 4 | Prod | approval (PO), rolling deploy, synthetic check | 10 min | Error rate below `[TBD]` for 15 min |
