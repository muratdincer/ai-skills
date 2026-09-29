---
description: "Designs authentication and authorization for an application or API: identity provider and protocol choice (OIDC, OAuth 2.x, SAML), login and token flows, token lifetimes and storage, roles, claims or attributes, and least-privilege enforcement points. Use when building a new app or API, adding SSO or MFA, opening APIs to partners or machine clients, or redesigning a role model."
related: "security-requirements, threat-model, access-review, api-design-review, secrets-management-plan"
prompt: "Design authentication and authorization for our B2B SaaS: web SPA, public REST API for partners, multi-tenant, customers want SSO with their own Entra ID or Okta."
---

# Design Authentication and Authorization

## Purpose
Produce an identity and access design that states who can authenticate, how, with which tokens, and what each identity may do, so that implementation is consistent and least privilege is enforced by design.

## When to use
- A new application, API or tenant model is being designed.
- SSO, MFA, passwordless or partner/machine access is being added.
- The role model has grown organically and needs redesign.

## When not to use
- You need to review who currently has which access. Use `access-review`.
- You need the full list of security controls, not only identity. Use `security-requirements`.
- You are storing and rotating secrets and keys. Use `secrets-management-plan`.

## Inputs
Required:
- Client types (browser SPA, server web app, mobile, service, CLI, partner) and the resources they access.

Optional, improves quality:
- Existing identity provider, directory, tenancy model.
- User populations (employees, customers, partners, admins) and regulatory needs (strong customer authentication, KVKK/GDPR).
- Current role list, sensitive operations, audit requirements.

If client types or resources are missing, ask. Other gaps become assumptions.

## Process
1. List identities: human populations, service identities, partner systems, admin/support staff. Note who owns each identity lifecycle (joiner, mover, leaver).
2. Choose the protocol per client: OIDC authorization code with PKCE for browser and mobile; client credentials or workload identity for services; token exchange for on-behalf-of calls; SAML only when a federation partner requires it. Avoid implicit and password grants.
3. Define authentication strength: MFA policy, step-up for sensitive operations, session lifetime, re-authentication, account recovery and lockout behavior.
4. Define tokens: access token format (JWT or opaque), audience, scopes, lifetime (short), refresh token rotation and binding, storage per client (no tokens in local storage for SPAs; prefer a backend-for-frontend), revocation.
5. Choose the authorization model: RBAC for coarse duties, ABAC/ReBAC for tenant, ownership or data-level rules. Write the permission matrix: role x resource x action.
6. Place enforcement points: gateway (authentication, scope), service (business authorization, object-level checks against IDOR), data layer (row-level or tenant filters).
7. Apply least privilege and separation of duties: default deny, no wildcard scopes, admin roles split, break-glass accounts with monitoring.
8. Define audit logging: authentication events, privilege changes, denied access; mask personal data in logs.
9. List threats addressed (token theft, replay, confused deputy, privilege escalation) and residual risks.
10. Record decisions and open questions for an ADR.
11. Suggest the next skill: `security-requirements` to turn the design into testable controls, `threat-model` to attack the flows, `access-review` to define periodic review of the roles.

## Output format
```markdown
# AuthN/AuthZ Design: <system>
## Identities and Lifecycle
| Population | Source of truth | Lifecycle owner | MFA |
## Flows per Client
| Client | Protocol / grant | Token storage | Session / token lifetime |
## Token Design
- Audience, scopes, claims, signing, rotation, revocation
## Authorization Model
| Role / attribute | Resource | Actions | Condition (tenant, ownership) |
## Enforcement Points
- Gateway: ... / Service: ... / Data: ...
## Admin, Break-glass and Support Access
## Audit Events
## Threats Addressed and Residual Risks
## Decisions and Open Questions
```

## Quality checklist
- [ ] Every client type has an explicit, current best-practice flow; no implicit or password grant.
- [ ] Object-level authorization is enforced in the service, not only at the gateway.
- [ ] Tenant isolation is enforced at more than one layer for multi-tenant systems.
- [ ] Token lifetimes, rotation and revocation are defined.
- [ ] Admin and support access follows least privilege and is audited.
- [ ] Unknown IdP capabilities or policies are marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Encoding every permission as a role, causing role explosion. Use attributes or relationships for data-level rules.
- Trusting claims from the client or skipping audience validation. Validate issuer, audience, signature and expiry on every service.
- Long-lived API keys for partners. Prefer client credentials with short tokens and per-partner scopes.

## Example
Input: "Multi-tenant B2B SaaS, SPA plus partner API, customers bring their own Entra ID or Okta."

Excerpt of output:
- SPA: OIDC code + PKCE via a backend-for-frontend; HTTP-only cookie session, no tokens in the browser.
- Partner API: client credentials, 10-minute access tokens [ASSUMPTION], scopes `orders.read`, `orders.write`, one client per partner.
- Tenant rule: every query filtered by `tenant_id` from the validated token, plus row-level security in the database.
