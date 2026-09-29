---
description: "Produces a secrets management plan: inventory and classification of secrets, central store choice criteria, identity-based access with least privilege, injection into workloads and pipelines, rotation and revocation, audit, and break-glass. Use when a team stores secrets in code, config files or pipeline variables, after a leak, or when designing secret handling for a new platform."
related: "iac-review, pipeline-design, authn-authz-design, security-requirements, kubernetes-manifest-review"
prompt: "Our database passwords and API keys are in appsettings files and pipeline variables. Write a plan to move to proper secrets management."
---

# Plan Secrets Management

## Purpose
Ensure every credential, key and certificate has an owner, lives in a controlled store, reaches workloads without exposure, is rotated on a schedule and can be revoked quickly after a leak.

## When to use
- Secrets are found in repositories, images, config files or plaintext pipeline variables.
- A leak or suspected exposure requires a structured remediation.
- A new platform or cluster needs a secret-handling design.
- An audit asks for rotation and access evidence.

## When not to use
- Designing end-user authentication or authorization. Use `authn-authz-design`.
- Reviewing a specific IaC change for secret leakage. Use `iac-review`.
- Handling an active breach. Use `security-incident-response` first.

## Inputs
Required:
- Types of secrets in use and where they currently live (at least a rough list).
- Runtime and delivery platforms (VMs, containers, serverless, CI system category).

Optional, improves quality:
- Existing secret store or key management service, identity provider, compliance requirements (PCI DSS, ISO/IEC 27001 controls, KVKK/GDPR).
- Team structure and on-call model.

Never ask for or repeat actual secret values. If the user pastes one, tell them to treat it as compromised and rotate it.

## Process
1. Inventory secrets: type (database credential, API key, signing key, TLS certificate, token), consumer, owner, current location, last rotation, blast radius if leaked.
2. Classify criticality (Critical/High/Medium) by blast radius and exposure.
3. Prefer eliminating secrets: workload identity / managed identity, federated short-lived tokens for pipelines, IAM database authentication where supported.
4. Define the central store requirements: encryption with keys in a KMS/HSM, fine-grained access policies, audit logging, versioning, dynamic secrets support, high availability. Stay product-neutral unless the user has one.
5. Define access model: per-application identity, per-environment separation, least privilege, no human read access to production secrets by default, just-in-time elevated access.
6. Define injection: runtime fetch or mounted volume/CSI-style driver, never baked into images or committed; how local development gets non-production secrets.
7. Define rotation: frequency per class, automated where possible, dual-secret overlap to avoid downtime, certificate expiry monitoring.
8. Define leak response: detection (secret scanning in repositories and pipelines, pre-commit hooks), revoke-rotate-verify runbook, history cleanup is secondary to rotation.
9. Define audit and alerting: access logs retained, alerts on unusual access, periodic access review.
10. Define break-glass: sealed emergency access, who, how logged, post-use rotation.
11. Produce a phased migration plan from current state.
12. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `iac-review` to verify the implementation in code, `authn-authz-design` for workload identity, or `pipeline-design` for CI/CD credential flow.

## Output format
```markdown
# Secrets Management Plan: <system/org unit>
## Secret Inventory
| Secret | Type | Consumer | Owner | Current location | Criticality | Target mechanism | Rotation |
## Target Architecture (store, identity, injection)
## Access Model
## Rotation Policy
| Class | Frequency | Automated? | Overlap strategy |
## Detection and Leak Response
## Audit and Break-Glass
## Migration Phases
| Phase | Scope | Exit criteria |
## Open Questions / Assumptions
```

## Quality checklist
- [ ] No secret value appears anywhere in the output.
- [ ] Each secret has an owner and a rotation rule.
- [ ] Secret elimination via workload identity was considered before storing.
- [ ] Rotation strategy avoids downtime (overlap or versioning).
- [ ] Leak response says to rotate first, not only to delete from history.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Moving secrets into a vault but giving every service read access to everything. Scope by identity and environment.
- Scrubbing git history and considering the leak resolved. The secret must be revoked and rotated.
- Rotation without consumer readiness, causing outages. Support two valid versions during rollover.

## Example
Input: "SQL passwords and a payment API key in appsettings.json, pipeline has a cloud admin key as a variable."

Excerpt of output:
| Secret | Criticality | Target mechanism | Rotation |
|---|---|---|---|
| Pipeline cloud admin key | Critical | Replace with federated short-lived identity, scoped per environment | Eliminated |
| Payment API key | Critical | Central store, fetched at runtime by app identity | 90 days `[confirm with provider]` |
| SQL password | High | Managed identity auth if supported, else dynamic credentials | Per lease |
