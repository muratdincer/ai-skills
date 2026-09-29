---
description: Writes a searchable knowledge base article (how-to, troubleshooting, or explanation) from notes, tickets, chat threads or expert input, with a findable title, the symptoms and search terms readers actually use, applicability, verified steps, expected results and ownership. Use when a question keeps being asked, a support ticket or incident produced a reusable fix, tribal knowledge must be written down, or someone asks to "write a KB article" or "document this for the wiki".
related: how-to-guide, faq-builder, runbook, document-review, glossary-builder
prompt: Turn this support thread about VPN certificate errors on new laptops into a KB article.
---

# Write a Knowledge Base Article

## Purpose
Answer one recurring question once, in a form people can find by searching their own words and follow without help. A good article reduces repeat questions and tickets and stays trustworthy because it has an owner and a review date.

## When to use
- The same question or ticket appears repeatedly.
- A support case, incident or expert conversation produced a fix or explanation worth reusing.
- Knowledge lives in one person's head or a chat thread and must be written down.

## When not to use
- A complete, multi-task guide for end users of a product. Use `user-guide` or `how-to-guide`.
- An operational procedure for on-call or production changes with rollback. Use `runbook`.
- Many short questions from one source document. Use `faq-builder`.

## Inputs
Required:
- Source material: ticket, chat thread, notes, or an expert's explanation of the problem and solution.

Optional, improves quality:
- Audience (end users, support agents, engineers) and their technical level.
- Environment/version scope, screenshots, error messages, related articles.
- The knowledge base's article template, categories and tag conventions.

If the source material is missing, ask for it. If it is unclear whether the solution was verified, ask; otherwise mark the steps `[UNVERIFIED]`.

## Process
1. Pick one article type: how-to (task), troubleshooting (symptom → cause → fix) or explanation (concept/why). Split the source into several articles if it answers more than one question.
2. Identify the audience and what they will type into search: exact error messages, symptoms in user language, product and feature names, common misspellings or synonyms.
3. Write a title that matches the search intent: task ("How to reset ...") or symptom ("Error 'X' when ..."). Avoid internal jargon and ticket numbers in the title.
4. Write a two-line summary answering the question directly, so a reader who stops there is still helped.
5. State applicability: environments, versions, roles, platforms where it applies, and where it does not.
6. For troubleshooting, list symptoms, then causes ordered by likelihood, then a fix per cause with a way to confirm which cause applies.
7. Write steps as numbered, single-action imperatives, with the expected result after key steps and exact UI labels, commands or paths as given in the source. Do not invent menu names, commands or values; mark gaps `[UNKNOWN]`.
8. Add prerequisites (access, permissions, tools) before the steps and a "If this did not work" section with the escalation path.
9. Remove personal data, internal hostnames or secrets that should not be in the audience's view; replace with placeholders.
10. Add metadata: tags/keywords, related articles, owner, last verified date and review interval, and verification status of the steps.
11. If the goal continues, suggest the next skill: `document-review` for a quality pass, `glossary-builder` if terms need defining, or `faq-builder` to derive short Q&A entries.

## Output format
```markdown
# <Search-intent title>
**Summary:** <direct answer in 1-2 sentences>
**Applies to:** <product/version/environment/role> · **Does not apply to:** <...>

## Symptoms (troubleshooting only)
- <exact error message or user-visible behavior>

## Cause (troubleshooting only)
- <cause> — how to confirm: <check>

## Before You Start
- <access, permission, tool>

## Steps
1. <single action> — Expected: <result>

## If This Did Not Work
- <next check> · Escalate to: <team/channel>

## Related
- <article>

---
Keywords: <search terms, synonyms, error codes> · Owner: <role/team or TBD> · Last verified: <date or TBD> · Review every: <interval> · Status: <Verified/[UNVERIFIED]>
```

## Quality checklist
- [ ] The title and keywords contain the words a reader would search for, including exact error text.
- [ ] The summary answers the question without reading further.
- [ ] Each step is one action; key steps have an expected result.
- [ ] Nothing is invented: unknown commands, labels or values are marked; unverified steps are flagged.
- [ ] Applicability, owner and review date are stated; no secrets or personal data.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Titling by internal cause ("Cert chain misconfiguration") while users search by symptom ("VPN says certificate not trusted"). Use the reader's words.
- Copying a chat thread including dead ends. Keep only the confirmed path; move alternatives to "If this did not work".
- Publishing without owner or review date. Unowned articles go stale and erode trust in the whole knowledge base.

## Example
Input: support thread where new laptops fail VPN login with "certificate not trusted"; fix was installing the company root certificate from the self-service portal.

Weak title: "VPN issue fix (ticket 4812)".
Strong title: "VPN error 'certificate not trusted' on a new laptop".
- Summary: New laptops may lack the company root certificate; install it from the self-service portal, then reconnect.
- Step 2: Open the self-service portal and choose `[UNKNOWN: exact menu label]` — Expected: certificate installed confirmation.
- Keywords: VPN, certificate not trusted, new laptop, root certificate · Status: `[UNVERIFIED]` until tested on a clean device.
