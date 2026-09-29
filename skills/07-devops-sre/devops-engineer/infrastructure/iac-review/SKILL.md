---
description: "Reviews infrastructure as code (Terraform/OpenTofu, Bicep, CloudFormation, Pulumi, Ansible and similar) and plan output for security misconfigurations, state and drift risks, destructive changes, modularity, naming/tagging and cost. Use when an IaC pull request or plan needs review, before applying changes to shared or production infrastructure, or when auditing an existing IaC codebase."
related: "secrets-management-plan, finops-review, environment-strategy, threat-model, pipeline-design"
prompt: "Review this Terraform module and plan output. It creates a storage bucket, a database and a VPC for our new service."
---

# Review Infrastructure as Code

## Purpose
Catch insecure, destructive or unmaintainable infrastructure changes before they are applied, and leave the codebase more modular and consistent.

## When to use
- An IaC pull request or a plan/what-if output is shared for review.
- Changes are about to be applied to production or shared infrastructure.
- An existing IaC repository is being audited for security and structure.

## When not to use
- Kubernetes workload YAML is the subject. Use `kubernetes-manifest-review`.
- The question is the overall secret handling design. Use `secrets-management-plan`.
- The main concern is spend, not code. Use `finops-review`.

## Inputs
Required:
- The IaC code or the diff under review.

Optional, improves quality:
- Plan/what-if output (strongly recommended for change reviews).
- Target environment, state backend setup, module registry, organization policies (tagging, regions, encryption, network).
- Compliance baseline in use (e.g. CIS benchmarks).

If no code or diff is provided, ask. If there is no plan output, review statically and state that destructive changes could not be verified.

## Process
1. Understand intent: what the change should create, modify or destroy, and in which environment.
2. Plan analysis: list every destroy and replace action; flag replacements of stateful resources (databases, disks, buckets, DNS zones, key vaults) as blocking unless intended; check `prevent_destroy`/deletion protection.
3. Security: public exposure (0.0.0.0/0 ingress, public buckets, public IPs), encryption at rest and in transit, customer-managed keys where policy requires, IAM least privilege (no wildcard actions/resources), logging enabled, private endpoints, no secrets in code, variables or state outputs (mark outputs sensitive).
4. State and drift: remote state with locking and encryption, state segregation per environment/blast radius, no manual changes, import instead of recreate for existing resources.
5. Versioning: provider and module versions pinned with constraints; lock file committed.
6. Structure: reusable modules with clear inputs/outputs, no copy-paste per environment, environment differences in variables, sensible defaults, validation rules on inputs.
7. Naming and tagging: organization convention, mandatory tags (owner, cost center, environment, data classification).
8. Reliability and cost: zone redundancy where required, backups and retention, right-sized SKUs, lifecycle rules; flag cost-heavy choices qualitatively.
9. Pipeline: plan on pull request, apply only from pipeline with approval, policy-as-code checks.
10. Rate findings and propose code fixes.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `secrets-management-plan` for credential findings, `threat-model` for exposed attack surface, or `finops-review` for cost findings.

## Output format
```markdown
# IaC Review: <module / change>
Verdict: Approve / Approve with changes / Block
## Destructive or Risky Plan Actions
| Resource | Action | Stateful? | Intended? | Required safeguard |
## Findings
| # | Severity | Category | File:line / resource | Finding | Fix |
## Suggested Code Changes
## Open Questions / Assumptions
```

## Quality checklist
- [ ] All destroy/replace actions on stateful resources are listed and resolved.
- [ ] No public exposure or wildcard IAM left unexplained.
- [ ] Secrets are not in code, variables defaults, or unmasked outputs.
- [ ] Provider/module versions are pinned.
- [ ] If no plan output was available, the review says so.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Renaming a resource or module address, causing destroy-and-recreate of a database. Use moved/import blocks.
- Reviewing only the diff and missing the effect of changed module defaults. Check the plan.
- One state for all environments, so a dev change can lock or break production. Split state by environment and domain.

## Example
Input: Terraform diff renames `<provider>_db_instance.main` to `<provider>_db_instance.orders`; plan shows `-/+ destroy and then create replacement`.

Excerpt of output:
| Resource | Action | Stateful? | Intended? | Required safeguard |
|---|---|---|---|---|
| db instance orders | replace | Yes | No (rename only) | Add `moved` block; enable deletion protection; re-run plan |
Verdict: Block until the plan shows no replacement.
