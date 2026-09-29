---
description: Audits a web page or front-end application for loading and runtime performance using Core Web Vitals (LCP, INP, CLS) and supporting metrics, traces each problem to its cause in the critical rendering path, JavaScript, images, fonts or third parties, and returns prioritized fixes with expected effect and a way to verify them. Use when a page feels slow, Core Web Vitals fail in field data, a performance budget is exceeded, or a lab report or trace needs interpreting.
related: performance-optimization, performance-test-plan, observability-plan, slo-definition, component-design
prompt: Our product listing page has LCP around 4.8 s and INP 350 ms on mobile. Here is the lab report and the page's head section. What should we fix first?
---

# Audit Web Performance

## Purpose
Turn performance measurements into a short, evidence-based list of fixes that move the user-facing metrics. The audit separates field reality from lab diagnostics and ties every recommendation to a metric, a cause and a verification step.

## When to use
- Field data (real-user monitoring or public field datasets) shows Core Web Vitals in the "needs improvement" or "poor" range.
- A lab report, performance trace or waterfall needs to be interpreted and turned into work items.
- A release is about to break an agreed performance budget, or a redesign must be checked before launch.

## When not to use
- Server-side or algorithmic hotspots found by a profiler. Use `performance-optimization`.
- Planning load or stress tests for back-end capacity. Use `performance-test-plan`.
- Defining performance objectives and alerting in production. Use `slo-definition` or `observability-plan`.

## Inputs
Required:
- The page or route and at least one measurement: field metrics, a lab report, a trace, a waterfall, or the relevant HTML, resource list and bundle sizes.

Optional, improves quality:
- Device and network profile of real users, target percentiles (default p75), existing performance budget.
- Framework and rendering mode (server-rendered, static, client-rendered, hybrid), CDN and caching setup.
- Third-party script inventory and business owners.

If no measurement exists, ask for one; without it, give only a checklist of likely causes marked `[ASSUMPTION]` and a measurement plan.

## Process
1. Establish the baseline: metric values at p75 for LCP, INP and CLS, split by device class and page type; state whether each number is field or lab. Use the common thresholds (LCP 2.5 s, INP 200 ms, CLS 0.1 for "good") unless the team has its own budget.
2. Identify the LCP element and break its time into sub-parts: time to first byte, resource load delay, resource load duration, element render delay. Fix the largest sub-part first.
3. For TTFB, check redirects, server response, caching headers, CDN hits and whether HTML is cacheable or streamed.
4. For load delay and duration, check discoverability of the LCP resource in HTML (not injected by script, not lazy-loaded), priority hints, preload/preconnect, image format and responsive sizes, and compression.
5. For render delay, list render-blocking CSS and scripts, web font loading strategy, client-side rendering or hydration that must finish before content paints.
6. For INP, find long tasks and the interactions that trigger them: heavy event handlers, large re-renders, synchronous layout, main-thread third parties. Propose yielding, splitting work, deferring non-urgent updates and reducing hydration cost.
7. For CLS, find shifting elements and their cause: images or embeds without dimensions, late-injected banners, font swaps, animations of layout properties.
8. Review JavaScript and third parties: bundle size per route, unused code, duplicate libraries, tag managers and widgets; each third party gets an owner and a keep, defer, or remove recommendation.
9. Prioritize fixes by expected metric impact, confidence and effort; label impact as an estimate `[ASSUMPTION]` unless measured.
10. Define verification for each fix: which metric, which tool or dashboard, and the field-data delay before results are visible. Propose or update a performance budget enforced in CI.
11. If the user continues, suggest `performance-optimization` for back-end TTFB causes, `slo-definition` to make the targets official, or `observability-plan` to add real-user monitoring.

## Output format
```markdown
# Web Performance Audit: <page/route>
Data: <field / lab / both> · Device & network: <profile> · Percentile: p75

## Baseline
| Metric | Value | Source | Target | Status |
|---|---|---|---|---|

## LCP Breakdown
- Element: ... · TTFB: ... · Load delay: ... · Load duration: ... · Render delay: ...

## Findings and Fixes
| # | Metric | Cause (evidence) | Fix | Expected impact | Effort | Confidence |
|---|---|---|---|---|---|---|

## Third-Party Review
| Script | Owner | Cost | Recommendation |
|---|---|---|---|

## Verification and Budget
- ...

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Every metric value states whether it is field or lab data and at which percentile.
- [ ] Each finding links a metric, a concrete cause with evidence, and a specific fix.
- [ ] The LCP element is identified and its time is broken into sub-parts.
- [ ] Impact estimates without measurement are marked `[ASSUMPTION]`.
- [ ] Every fix has a verification step and the metric it should move.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Optimizing the lab score on a fast desktop while real users are on mid-range phones. Base priorities on field data for the real device mix.
- Lazy-loading the LCP image or injecting it by script, which delays the most important paint.
- Treating total bundle size as the goal. INP depends on main-thread work during interactions; measure long tasks, not only kilobytes.

## Example
Input: "Product listing, mobile p75 LCP 4.8 s, INP 350 ms. Hero image is set by a carousel script; 3 tag managers."

Excerpt of output:
| # | Metric | Cause (evidence) | Fix | Expected impact | Effort | Confidence |
|---|---|---|---|---|---|---|
| 1 | LCP | Hero image discovered only after carousel script runs (load delay 2.1 s in trace) | Render first slide as `<img>` in HTML with high fetch priority and explicit size; initialize carousel after | LCP -1.5 to -2 s `[ASSUMPTION]` | S | High |
| 2 | INP | Filter click triggers 280 ms long task re-rendering whole grid | Update only changed tiles; defer analytics call; yield before rendering results | INP below 200 ms `[ASSUMPTION]` | M | Medium |
| 3 | INP/LCP | Three tag managers loading overlapping tags | Consolidate to one; marketing to confirm owners | TBD | M | Low |
