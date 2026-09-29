---
description: "Reviews Kubernetes manifests, Helm charts or Kustomize output for resource requests and limits, health probes, security context, availability (replicas, disruption budgets, spread), configuration and secret handling, and operability. Returns prioritized findings with corrected YAML. Use when manifests are submitted for review, pods restart or get evicted, or a workload is being prepared for production."
related: "dockerfile-review, secrets-management-plan, capacity-planning, deployment-strategy, resilience-review"
prompt: "Review this Deployment and Service YAML for our order API before we go live on the production cluster."
---

# Review Kubernetes Manifests

## Purpose
Make a workload safe to run in production: correctly sized, observable by the scheduler, hardened, resilient to node and zone loss, and consistent across environments.

## When to use
- Manifests, a Helm chart or rendered Kustomize output are shared for review.
- Pods are OOMKilled, throttled, evicted or restart-looping.
- A workload is being onboarded to a production or shared cluster.

## When not to use
- The container image itself is the concern. Use `dockerfile-review`.
- The cloud/cluster infrastructure code is the concern. Use `iac-review`.
- The question is how many replicas or nodes are needed long term. Use `capacity-planning`.

## Inputs
Required:
- The manifest YAML (or rendered chart output).

Optional, improves quality:
- Workload profile: stateless/stateful, traffic, latency SLO, startup time, memory behavior.
- Cluster policies (admission controllers, Pod Security Standards level, network policy default, service mesh).
- Observed metrics or incidents (OOMKills, throttling, restarts).

If the YAML is missing, ask for it. If a chart is given unrendered, review values and templates and state the assumptions.

## Process
1. Inventory objects and their relations (Deployment/StatefulSet/Job, Service, Ingress/Gateway, ConfigMap, Secret, HPA, PDB, NetworkPolicy, ServiceAccount).
2. Resources: requests set for CPU and memory on every container; memory limit set; CPU limit only if the organization requires it (note throttling risk); requests grounded in measured usage or marked `[ASSUMPTION]`.
3. Probes: readiness reflects ability to serve; liveness checks only the process, not dependencies; startup probe for slow starters; sensible timeouts and thresholds.
4. Security: `runAsNonRoot`, fixed UID, `allowPrivilegeEscalation: false`, drop all capabilities, `readOnlyRootFilesystem`, seccomp `RuntimeDefault`, no hostPath/hostNetwork, dedicated ServiceAccount with automount disabled unless needed, least-privilege RBAC. Compare with Pod Security Standards "restricted".
5. Availability: replicas at least 2 for serving workloads, PodDisruptionBudget, topology spread or anti-affinity across nodes/zones, rolling update surge/unavailable settings, graceful shutdown (`terminationGracePeriodSeconds`, preStop, connection draining).
6. Scaling: HPA metrics and bounds consistent with requests; no conflict between HPA and fixed replicas in GitOps.
7. Configuration and secrets: no secrets in ConfigMaps or env literals; image referenced by immutable tag or digest; `imagePullPolicy` sensible; environment differences only via values/overlays.
8. Networking: NetworkPolicy default deny with explicit allows; Service ports and selectors match; ingress TLS.
9. Operability: labels (app, version, team), annotations for metrics scraping, log to stdout, resource names consistent.
10. Rate findings and give corrected YAML snippets.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `capacity-planning` for requests and replica sizing, `resilience-review` for failure modes, or `deployment-strategy` for the rollout.

## Output format
```markdown
# Kubernetes Manifest Review: <workload>
Summary: <production readiness verdict: Ready / Ready with fixes / Not ready>
| # | Severity | Object | Field | Finding | Fix |
## Corrected Snippets
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every container has requests; memory limits are present.
- [ ] Liveness probes do not depend on downstream services.
- [ ] Security context meets the restricted baseline or deviations are justified.
- [ ] Serving workloads survive a single node drain (replicas, PDB, spread).
- [ ] Suggested values not backed by data are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Liveness probe calling the database: a database blip restarts every pod. Keep liveness local.
- Copying request values from another service. Base them on observed usage and revisit.
- PDB with `minAvailable` equal to replicas, which blocks node drains. Allow at least one disruption.

## Example
Input: Deployment with 1 replica, no resources, liveness `GET /health` that checks database, runs as root.

Excerpt of output:
| # | Severity | Object | Field | Finding | Fix |
|---|---|---|---|---|---|
| 1 | High | Deployment | replicas | Single replica, no PDB | 3 replicas, PDB `maxUnavailable: 1`, zone spread |
| 2 | High | Deployment | livenessProbe | Checks database; cascading restarts | Liveness `/livez` (process only), readiness `/readyz` |
| 3 | High | Deployment | securityContext | Runs as root | `runAsNonRoot: true`, drop ALL, read-only root FS |
