---
description: "Reviews a Dockerfile (or Containerfile) for image size, layer and cache efficiency, security hardening and build reproducibility, and returns prioritized findings with corrected snippets. Use when someone shares a Dockerfile for review, an image is large, slow to build or flagged by a scanner, or before a service's first production release."
related: "kubernetes-manifest-review, pipeline-design, secrets-management-plan, dependency-vulnerability-review"
prompt: "Review this Dockerfile for our Node.js service. The image is 1.2 GB and the security scan reports 40 vulnerabilities."
---

# Review a Dockerfile

## Purpose
Turn a working Dockerfile into a small, secure, reproducible and cache-friendly one, with each finding justified and a concrete fix.

## When to use
- A Dockerfile is submitted in a pull request or shared for review.
- The image is large, builds slowly, or has many scanner findings.
- A service is about to go to production for the first time.

## When not to use
- The runtime configuration on the orchestrator is the issue. Use `kubernetes-manifest-review`.
- Vulnerabilities in application dependencies are the topic. Use `dependency-vulnerability-review`.
- The failure is in the build pipeline, not the file. Use `pipeline-failure-triage`.

## Inputs
Required:
- The Dockerfile text.

Optional, improves quality:
- The ignore file (e.g. `.dockerignore`), language/build tool, target runtime platform and architecture.
- Current image size, scanner output, build time.
- Organizational base image policy.

If the Dockerfile is missing, ask for it.

## Process
1. Identify the stack and build type, and whether a multi-stage build is used.
2. Base image: official or approved source, minimal variant (slim, distroless, alpine where libc compatible), pinned by tag and digest, not `latest`.
3. Build stages: separate build tooling from runtime; copy only artifacts into the final stage.
4. Layer and cache: dependency manifests copied and installed before source; related `RUN` commands combined; package caches cleaned in the same layer; ignore file excludes `.git`, tests, local env files.
5. Security: non-root `USER` with fixed UID; no secrets in `ARG`/`ENV`/layers (use build secret mounts); no `curl | sh` without checksum; minimal packages; no SSH or shells needed at runtime where possible; read-only filesystem friendly.
6. Reproducibility: pinned package versions or lockfiles; deterministic install commands (`npm ci`, `pip install --require-hashes`, locked restore); explicit platform if multi-arch.
7. Runtime correctness: exec-form `ENTRYPOINT`/`CMD` so signals reach the process; proper PID 1 handling; `EXPOSE` and `WORKDIR` set; `HEALTHCHECK` only if the orchestrator does not probe.
8. Metadata: OCI labels for source, revision, version.
9. Rate each finding Critical/High/Medium/Low and give a corrected snippet; then provide the full revised Dockerfile if changes are substantial.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `kubernetes-manifest-review` for the runtime configuration or `dependency-vulnerability-review` for base image and package findings.

## Output format
````markdown
# Dockerfile Review: <image/service>
Summary: <2-3 lines: main risks, expected size/security effect (qualitative)>
| # | Severity | Category | Line | Finding | Fix |
## Revised Dockerfile
```dockerfile
...
```
## Open Questions / Assumptions
````

## Quality checklist
- [ ] Every finding references a line or instruction in the input.
- [ ] The final stage runs as non-root and contains no build tooling or secrets.
- [ ] Base image is pinned; no `latest`.
- [ ] Revised file is syntactically valid and preserves the original behavior.
- [ ] No invented size or CVE numbers; expected effects are qualitative unless data was given.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Copying the whole context before installing dependencies, which busts the cache on every change. Copy manifests first.
- Deleting a secret in a later layer; it remains in history. Use build secret mounts.
- Switching to alpine blindly for glibc-dependent runtimes. Verify compatibility or use slim/distroless.

## Example
Input: `FROM node:latest`, `COPY . .`, `RUN npm install`, `CMD npm start`.

Excerpt of output:
| # | Severity | Category | Line | Finding | Fix |
|---|---|---|---|---|---|
| 1 | High | Reproducibility | 1 | Unpinned `latest` full image | Pin `node:<major>-slim@sha256:...` |
| 2 | High | Security | – | Runs as root | Add `USER node` in final stage |
| 3 | Medium | Cache | 2-3 | Source copied before install | Copy `package*.json`, `npm ci --omit=dev`, then copy source |
| 4 | Medium | Runtime | 4 | Shell-form CMD via npm, signals lost | `CMD ["node","server.js"]` |
