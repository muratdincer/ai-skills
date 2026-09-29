---
description: "Writes a service catalog entry in customer language: what the service is and is not, who can use it, request offerings and how to request them, approvals, fulfilment steps, service levels and support hours, costs if charged, dependencies, responsibilities and ownership. Use when a new IT or internal service is launched, an existing entry is outdated or unclear, requesters keep asking how to get something, or service levels must be published for users."
related: "slo-definition, sla-breach-analysis, raci-matrix, user-guide, faq-builder"
prompt: "Write a catalog entry for our 'Developer VM' service: devs request a Linux VM with 8 vCPU/32 GB, manager approval needed, delivered in 2 business days, deleted after 90 days unless extended."
---

# Write a Service Catalog Entry

## Purpose
Let users understand what they can get, how to ask for it and what to expect, and let the provider fulfil and measure it consistently, so requests arrive complete and expectations match what the service actually delivers.

## When to use
- A new IT, platform or internal shared service goes live.
- An existing entry generates repeated "how do I get..." questions or incomplete requests.
- Service levels, support hours or costs change and must be published.

## When not to use
- Defining the internal SLO targets and error budgets behind the service. Use `slo-definition`.
- Step-by-step usage instructions after the service is delivered. Use `user-guide`.
- Assigning detailed responsibilities across many teams. Use `raci-matrix`.

## Inputs
Required:
- Service name and a description of what it provides and for whom.

Optional, improves quality:
- Request offerings and options, eligibility, approval rules, fulfilment steps and lead times.
- Agreed service levels, support hours and channels, costs or chargeback model.
- Owner, provider team, dependencies, security and data handling rules, the organization's catalog template.

If the service description is missing, ask for it. Do not invent service levels, lead times or prices; mark them `[TBD]` and list them as decisions for the service owner.

## Process
1. Write the service description in the requester's language: the outcome they get, not the technology used. Add who it is for and a one-line "use this when".
2. State explicit exclusions ("what this service does not include") and point to the right service for each common confusion.
3. Define eligibility: who may request (roles, departments, locations), prerequisites (training, licence, cost center).
4. List request offerings (for example, new, change, extend, remove) with options and limits; for each, the fields the requester must provide so requests arrive complete.
5. Describe the request and approval flow: channel, approvers per offering, automatic versus manual fulfilment, what the requester receives on completion.
6. Publish service levels per offering: fulfilment lead time, availability, support hours, first response and resolution targets per priority, and how to report an incident. Use only agreed values; otherwise `[TBD]`.
7. State costs and billing model if applicable, and lifecycle rules (renewal, expiry, decommissioning, data retention and deletion).
8. Add security and compliance obligations: data classification allowed on the service, access controls, acceptable use, personal data handling under KVKK/GDPR if the service processes it.
9. Record ownership and dependencies: service owner, provider team, escalation contact, underpinning services and vendors, and review date.
10. Add three to five FAQs from real or likely requester questions, labeled `[ASSUMPTION]` if not from actual tickets.
11. Hand off: suggest `slo-definition` to set measurable targets behind the published levels, `faq-builder` to expand FAQs, or `sla-breach-analysis` once performance data exists.

## Output format
```markdown
# <Service Name>
| Field | Value |
|---|---|
| Summary | <one sentence outcome> |
| For | <who> |
| Service owner / Provider | <role or name> / <team> |
| Status | live / pilot / retiring |
| Review date | <date> |

## What You Get
...
## Not Included
- ... → use <other service>
## Who Can Request
- Eligibility: ... Prerequisites: ...
## Request Offerings
| Offering | Options / limits | Info you must provide | Approval | Lead time |
|---|---|---|---|---|
## How to Request
1. ...
## Service Levels and Support
| Item | Target |
|---|---|
| Availability | <... or [TBD]> |
| Support hours / channel | ... |
| Incident response / resolution (per priority) | ... |
## Cost and Lifecycle
- Cost: ... Renewal/expiry: ... Data retention and deletion: ...
## Security and Compliance
- ...
## Dependencies
- ...
## FAQ
- Q: ... A: ...
## Decisions Needed from Service Owner
- [TBD] ...
```

## Quality checklist
- [ ] The description states the user outcome in plain language, not implementation details.
- [ ] Exclusions are explicit and redirect to the right service.
- [ ] Every offering lists the information the requester must provide and its approval path.
- [ ] Service levels, lead times and costs are agreed values or `[TBD]`, never invented.
- [ ] Lifecycle, data retention and security rules are stated.
- [ ] Owner, escalation contact and review date are present.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Describing infrastructure ("KVM cluster with Ceph") instead of what the user gets. Lead with the outcome.
- Publishing aspirational service levels that the provider cannot meet; this creates instant SLA breaches.
- Omitting expiry and deletion rules, which leads to resource sprawl and data retained beyond purpose.
- Letting entries age; a stale catalog drives requests back to email and chat.

## Example
Input: "Developer VM: Linux VM 8 vCPU/32 GB, manager approval, 2 business days, deleted after 90 days unless extended."

Excerpt of output:
- Summary: A personal Linux virtual machine for development and testing, ready within 2 business days.
- Not included: production workloads or customer data → use "Application Hosting".
- Offerings: New VM (8 vCPU / 32 GB, larger sizes [TBD]) – requester provides project code and justification – approval: line manager – lead time: 2 business days.
- Lifecycle: deleted 90 days after delivery unless extended; reminder sent before deletion [ASSUMPTION: 7 days].
- Security: no personal or production data on developer VMs [ASSUMPTION: confirm data classification policy].
