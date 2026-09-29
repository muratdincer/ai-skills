---
name: secure-code-review
description: "Reviews source code or a diff for security weaknesses, mapped to OWASP Top 10 categories and CWE IDs, tracing untrusted input from source to sink and giving severity, evidence and a concrete fix per finding. Use when a pull request touches authentication, authorization, input handling, crypto, file or network access, or when someone asks to check code for vulnerabilities."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 09-security
  role: security-engineer
  area: assessment
  title: "Review code for security"
  related: "code-review, security-finding-report, vulnerability-triage, security-requirements, threat-model"
  prompt: "Review this ASP.NET Core controller and its repository class for security issues before we merge."
---

# Review Code for Security

## Purpose
Find exploitable weaknesses in code before release and give developers precise, verifiable fixes, without drowning them in theoretical noise.

## When to use
- A change touches authentication, session, authorization, input parsing, queries, file handling, deserialization, crypto or outbound calls.
- A SAST tool produced findings that need human validation.
- Code is being prepared for a pentest, audit or public exposure.

## When not to use
- General readability or design review. Use `code-review` or `clean-code-review`.
- Findings are in third-party packages. Use `dependency-vulnerability-review`.
- You need to write up one confirmed issue formally. Use `security-finding-report`.

## Inputs
Required:
- The code or diff to review, with the language and framework.

Optional, improves quality:
- How the code is reached (public endpoint, internal job, admin only) and the trust level of callers.
- Relevant configuration, middleware, ORM and validation layers.
- Security requirements or ASVS level, SAST output.

If code is missing, ask for it. If the entry point is unclear, state your assumption about exposure.

## Process
1. Identify entry points (sources): HTTP parameters, headers, cookies, message payloads, files, environment, database values written by users.
2. Identify sinks: SQL/NoSQL queries, OS commands, file paths, templates/HTML output, deserializers, redirects, outbound URLs (SSRF), LDAP/XPath, logging.
3. Trace each source to each sink; note validation, encoding or parameterization on the path. Unbroken tainted paths are candidate findings.
4. Check access control on every operation: authentication required, role or scope checked, object ownership verified (IDOR), tenant filter applied.
5. Check crypto and secrets: hard-coded secrets, weak algorithms or modes, predictable randomness, missing TLS validation, password hashing (Argon2id, bcrypt, PBKDF2 with adequate cost).
6. Check error handling and logging: stack traces or internal details leaked, sensitive or personal data written to logs, missing audit events.
7. Check framework-specific pitfalls: mass assignment/over-posting, CSRF protection, CORS configuration, unsafe deserialization settings, disabled security headers.
8. For each finding record: location, OWASP Top 10 category, CWE ID, exploit scenario, severity (with reasoning or CVSS if the team uses it), confidence, and a code-level fix.
9. Separate confirmed findings from suspicious patterns that need runtime verification.
10. Summarize: counts by severity, blocking issues for merge, and positive controls observed.
11. Hand off: write each Critical or High issue up with `security-finding-report`, route disputed severity to `vulnerability-triage`, and feed recurring gaps into `security-requirements`.

## Output format
```markdown
# Security Code Review: <component / PR>
Scope: <files> · Exposure: <public/internal/admin> [ASSUMPTION if inferred]
## Summary
- Blocking: <n> · High: <n> · Medium: <n> · Low/Info: <n>
## Findings
### SCR-01 <title>
- Location: <file:line>
- Category: OWASP A0x:<year> <name> · CWE-<id>
- Severity / confidence: <High/Med/Low> / <Confirmed/Likely/Needs verification>
- Scenario: <how an attacker exploits it>
- Fix: <specific change, with a short code snippet>
## Needs Runtime Verification
- ...
## Good Practices Observed
- ...
```

## Quality checklist
- [ ] Every finding has a location, CWE, exploit scenario and a concrete fix.
- [ ] Severity reflects actual reachability and exposure, not only the pattern.
- [ ] Object-level and tenant authorization were checked for each data access.
- [ ] Secrets, tokens or personal data found in code are reported masked, never repeated in full.
- [ ] Speculative issues are labeled as needing verification.
- [ ] Merge-blocking items are clearly separated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting every string concatenation as injection. Confirm the value is attacker-controlled and reaches a sink.
- Missing authorization flaws because the code "looks clean". Broken access control rarely shows as a dangerous function call.
- Recommending generic "sanitize input". Name the exact control: parameterized query, allow-list, context-aware encoding.

## Example
Input: a controller action `GET /orders/{id}` that calls `repo.Get(id)` with `[Authorize]` only.

Excerpt of output:
### SCR-01 Missing ownership check on order retrieval
- Category: OWASP A01:2021 Broken Access Control · CWE-639
- Scenario: Any authenticated user enumerates `id` and reads other customers' orders, including addresses.
- Fix: Filter by the caller's customer ID from the validated token: `repo.Get(id, User.GetCustomerId())`; return 404 on mismatch.
