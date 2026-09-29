---
name: readme-writing
description: "Writes or restructures a repository README that states what the project is, who it is for, how to get it running, how to use and configure it, and how to contribute, with commands that can be copied and verified. Use when a repository has no README, an outdated or sprawling one, new joiners struggle to run the project, or a library or service is about to be shared with other teams."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: docs
  title: "Write a README"
  related: "code-documentation, api-reference-docs, technical-onboarding, how-to-guide, changelog-entry"
  prompt: "Write a README for our internal invoice-service repo. It is a REST API with a PostgreSQL database and a background worker; here is the folder structure and the Makefile."
---

# Write a README

## Purpose
Give anyone who lands on the repository an answer, within a minute, to "what is this, should I care, and how do I run it", and give contributors a verified path from clone to a passing test run. A good README cuts onboarding time and repeated questions in team channels.

## When to use
- A repository has no README, or the README describes a state the code no longer has.
- New team members or other teams repeatedly ask how to set up or run the project.
- A library, SDK, CLI or service is about to be published internally or as open source.

## When not to use
- Documenting individual functions, classes or design reasons in code. Use `code-documentation`.
- Documenting every endpoint, parameter and error of an API. Use `api-reference-docs`.
- A full onboarding program with people, access and first tasks. Use `technical-onboarding`.

## Inputs
Required:
- What the project is and does (a sentence from the user, the existing README, or the code structure).
- How it is built and run: build files, scripts, Makefile, container files or the commands the team uses.

Optional, improves quality:
- Target audience (end users of a library, service operators, internal contributors).
- Configuration files and environment variables, required external services.
- Contribution rules, license, owners and support channels, CI badges.

If build and run information is missing, ask for it in one short batch; do not invent commands. Mark any command you could not verify from the input as `[UNVERIFIED]`.

## Process
1. Identify the audience and project type (library, service, CLI, application, monorepo); this decides the section order. Libraries lead with installation and usage; services lead with running locally and configuration.
2. Write the opening: project name, one-sentence description of what it does and for whom, and status (active, maintenance, deprecated) if known.
3. List prerequisites with exact runtime and tool requirements as stated in the build files; do not guess versions, write `[TBD: version]` instead.
4. Write the quick start: the shortest command sequence from clone to a working result (running service, passing tests or first successful call), each step with its expected outcome.
5. Document configuration as a table: variable or key, purpose, default, required or optional, example value. Never include real secrets; show placeholders and where secrets come from.
6. Add usage: two or three realistic examples (code snippet, CLI call or HTTP request) covering the main use case, not every option.
7. Describe the project layout briefly (top-level folders and their responsibility) and the key architectural facts a contributor needs, linking to deeper docs instead of repeating them.
8. Add development workflow: how to run tests, linters and formatters, how to run a single test, and the branching and pull request rules if known.
9. Add operations and support: how to deploy or release (or a link), where logs and dashboards live, owners and support channel, license.
10. Cut: remove marketing language, duplicated content and anything that will rot quickly (hard-coded counts, dated statements); link to the source of truth instead.
11. Mark every unverified command or inferred fact as `[UNVERIFIED]` or `[ASSUMPTION]` and list open questions for the owners.
12. If the user needs more, suggest `api-reference-docs` for endpoint details, `technical-onboarding` for a full onboarding plan, or `changelog-entry` to start a changelog.

## Output format
```markdown
# <Project name>
<One sentence: what it does and for whom.> Status: <active | maintenance | deprecated | [UNKNOWN]>

## Quick Start
1. <command>  # expected: <outcome>

## Prerequisites
- <runtime/tool and version or [TBD: version]>

## Configuration
| Key / variable | Purpose | Default | Required | Example |
|---|---|---|---|---|

## Usage
<2-3 realistic examples>

## Project Structure
- `<folder>/` — <responsibility>

## Development
- Run tests: `<command>` · Single test: `<command>` · Lint/format: `<command>`

## Deployment and Operations
<link or short steps; logs, dashboards>

## Contributing, Owners and Support
<rules, owner team, channel, license>

<!-- Open questions: ... -->
```

## Quality checklist
- [ ] The first two lines tell a stranger what the project is and whether it is relevant to them.
- [ ] The quick start goes from clone to a verifiable result, and each step states its expected outcome.
- [ ] No command, version or default is invented; unverified items are marked `[UNVERIFIED]` or `[TBD]`.
- [ ] No secrets, internal credentials or personal data appear; placeholders show the format only.
- [ ] Deep content is linked rather than duplicated, and nothing time-sensitive is hard-coded.
- [ ] Section order matches the audience (library users vs contributors vs operators).
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A quick start that silently depends on a local setup (preinstalled database, cached credentials). Test it mentally on a clean machine and list every dependency.
- Writing the README as a design document. Keep architecture to what a contributor needs and link to the design doc or ADRs.
- Copying `.env` files with real values into examples. Use obvious placeholders such as `<your-api-key>`.

## Example
Input: "invoice-service: REST API + worker, PostgreSQL, Makefile has `make up`, `make test`."

Weak excerpt: "## Setup — Install everything and run the project."

Strong excerpt:
- Quick start: 1) `make up` — expected: API on `http://localhost:8080/health` returns `200`; worker logs `listening on queue invoices` `[UNVERIFIED: queue name]`. 2) `make test` — expected: all tests pass.
- Configuration: `DATABASE_URL` | connection string | none | required | `postgres://user:<password>@localhost:5432/invoices`.
- Open question: Which runtime version does the build require? `[TBD: version]`
