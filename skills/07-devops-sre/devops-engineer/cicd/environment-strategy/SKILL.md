---
name: environment-strategy
description: "Defines the environment landscape for a system: which environments exist and why, parity with production, test data policy, access and change rights, lifecycle (persistent vs ephemeral) and ownership. Use when environments multiply without purpose, tests pass in staging but fail in production, or a new platform needs its environment model agreed."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: devops-engineer
  area: cicd
  title: "Define environment strategy"
  related: "pipeline-design, test-data-design, secrets-management-plan, finops-review, deployment-strategy"
  prompt: "We have dev, test, uat, preprod and prod and nobody knows which one to use for what. Define an environment strategy for us."
---

# Define Environment Strategy

## Purpose
Give every environment a clear purpose, owner, data policy and access model so that tests are meaningful, cost is justified and production-like verification happens before production.

## When to use
- A new product or platform needs its environment model.
- Environments drift apart and "works in staging" failures are frequent.
- Test data, access or cost of non-production environments is a concern.
- Ephemeral per-branch environments are being considered.

## When not to use
- The promotion flow and gates are the topic. Use `pipeline-design`.
- The topic is designing test data sets. Use `test-data-design`.
- Only non-production cost is in question. Use `finops-review`.

## Inputs
Required:
- Current or planned environments, and the system's main components and dependencies (databases, queues, third-party APIs).

Optional, improves quality:
- Who uses each environment (developers, QA, business UAT, performance, partners).
- Regulatory constraints on data (KVKK/GDPR, PCI DSS, banking regulation).
- Infrastructure cost per environment, provisioning method (IaC or manual).

If the component list is missing, ask for it; other gaps go to open questions.

## Process
1. List each environment with its single primary purpose and its primary consumers. Merge or remove environments without a distinct purpose.
2. Decide lifecycle per environment: persistent, ephemeral per pull request, or on demand for performance tests.
3. Define parity with production per dimension: infrastructure topology, versions (OS, runtime, database engine), configuration, network/security controls, scale, data volume. State accepted gaps explicitly.
4. Define external dependencies per environment: real sandbox, contract stub, service virtualization.
5. Define the data policy: synthetic, masked copy of production, or subset. Never plain production personal data outside production; reference KVKK/GDPR data minimization.
6. Define access and change rights: who can deploy, who can change configuration, who can read data; whether manual changes are allowed (ideally none beyond dev).
7. Define provisioning and drift control: all environments from the same IaC modules with per-environment variables; drift detection.
8. Define refresh and reset cadence, and stability windows (e.g. UAT freeze during acceptance).
9. Define ownership and cost controls: owner per environment, schedules to shut down idle non-prod, tagging.
10. Fill the template and list gaps and migration steps from the current state.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `pipeline-design` for promotion between environments, `secrets-management-plan` for per-environment secrets, or `test-data-design` for non-production data.

## Output format
```markdown
# Environment Strategy: <system>
| Env | Purpose | Consumers | Lifecycle | Deploy trigger | Data | Access (deploy/config/data) | Owner |
## Parity with Production
| Dimension | Dev | Test | Staging | Accepted gap |
## External Dependencies per Environment
## Data Policy and Masking
## Provisioning and Drift Control
## Refresh, Freeze and Uptime Schedules
## Changes from Current State
## Open Questions / Assumptions
```

## Quality checklist
- [ ] Each environment has exactly one primary purpose and an owner.
- [ ] Parity gaps with production are explicit, especially for the last pre-production environment.
- [ ] No unmasked production personal data outside production.
- [ ] Manual changes and who may deploy are defined per environment.
- [ ] All environments are provisioned from the same code with variables.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A staging environment that differs in database engine version or network policy, so it proves nothing. Record and close parity gaps.
- Shared long-lived test environments that everyone mutates. Use ephemeral environments for feature validation.
- Copying production data for convenience. Mask or synthesize, and document the legal basis.

## Example
Input: "dev, test, uat, preprod, prod; uat and preprod are both used by business; test uses a prod copy."

Excerpt of output:
| Env | Purpose | Lifecycle | Data |
|---|---|---|---|
| pr-* | Feature validation per pull request | Ephemeral | Synthetic |
| test | Integrated system tests, QA automation | Persistent | Synthetic + masked subset |
| staging (merge uat+preprod) | UAT and release verification, prod-like topology | Persistent, freeze during acceptance | Masked production subset `[confirm masking rules]` |
