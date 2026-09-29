---
name: state-management-design
description: "Designs where each piece of front-end state lives (local component, URL, form, shared client, server cache, persisted) and how it flows, is synchronized, invalidated and tested, in a framework-neutral way, and justifies any global store. Use when starting a front-end feature or app, when state is duplicated or out of sync between screens, when a team debates adopting or removing a global store, or when server data caching and optimistic updates must be decided."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: frontend
  title: "Design state management"
  related: "component-design, technical-design-doc, api-contract, adr, web-performance-audit"
  prompt: "Our order management screens keep showing stale data after edits and we have everything in one global store. Help us redesign the state management."
---

# Design State Management

## Purpose
Put every piece of state in the narrowest place that satisfies its consumers, with one source of truth and explicit rules for synchronization and invalidation. The result is a state inventory and a set of decisions that reduce stale data, unnecessary re-renders and accidental coupling.

## When to use
- A new front-end application or feature needs its state architecture decided.
- Screens show stale or inconsistent data, or the same data is copied into several stores.
- The team debates introducing, replacing or removing a global state library.

## When not to use
- The API of one component (props, events, controlled state). Use `component-design`.
- Designing the back-end API that serves the data. Use `api-contract`.
- Recording a single already-made decision. Use `adr`.

## Inputs
Required:
- The feature or screens in scope and the data they show or edit (a description, user stories or current code structure).

Optional, improves quality:
- Framework, rendering mode (server, client, hybrid) and libraries already in use.
- API characteristics: endpoints, pagination, real-time channels, consistency needs.
- Current pain points (stale data, performance, bugs) with examples.
- Offline, multi-tab or collaboration requirements.

If the data and screens are unclear, ask for the main user flows first. Mark any inferred requirement (e.g., offline support) as `[ASSUMPTION]`.

## Process
1. Inventory the state: list each piece of data or UI condition, who reads it, who writes it, its lifetime, and where it lives today.
2. Classify each item: server state (owned by the back end, cached on the client), URL state (filters, pagination, selected tab, anything shareable or bookmarkable), form state (draft values, validation), local UI state (open, hover, focus), shared client state (session, theme, feature flags, cross-screen selections), persisted client state (preferences, offline drafts).
3. Derive rather than store: remove any item computable from others (totals, filtered lists, flags) and note the derivation.
4. Place each item at the lowest level that serves all its readers; lift only to the nearest common owner. A global store holds only shared client state that genuinely crosses distant parts of the tree.
5. For server state, define the cache policy: cache key, freshness window, refetch triggers (focus, reconnect, interval, event), invalidation after mutations, pagination strategy and request deduplication. Never copy server data into a separate client store.
6. Define mutations: pessimistic or optimistic update, rollback on failure, conflict handling (version or ETag), and which cache entries are invalidated or updated.
7. Define synchronization boundaries: URL ↔ state, multiple tabs, real-time pushes, offline queue; state which side wins on conflict.
8. Check performance: subscriptions so that components re-render only on the slice they use, memoized selectors, large lists and normalized entities where many screens edit the same records.
9. Define the testing approach: pure reducers and selectors unit-tested, cache behavior tested with a mocked network layer, critical flows (edit then list refresh) covered by integration tests.
10. Record the decisions with rationale and rejected alternatives; if choosing or changing a library, list the criteria (team familiarity, server-cache support, devtools, bundle size, migration cost) instead of naming a winner by default.
11. If the user continues, suggest `adr` to record the key decision, `component-design` for components affected, or `technical-design-doc` if the change spans several teams.

## Output format
```markdown
# State Management Design: <feature/app>

## State Inventory
| State | Category | Readers | Writers | Lifetime | Location (target) | Notes |
|---|---|---|---|---|---|---|

## Derived Values
- <value> = <derivation>

## Server Cache Policy
| Resource (cache key) | Freshness | Refetch triggers | Invalidated by | Optimistic? |
|---|---|---|---|---|

## Synchronization Rules
- URL: ... · Tabs: ... · Real-time: ... · Offline: ...

## Decisions
| Decision | Rationale | Alternatives rejected |
|---|---|---|

## Migration Steps (if changing existing code)
1. ...

## Testing Approach
- ...

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Every piece of state has exactly one source of truth and a category.
- [ ] Server data is not duplicated in a client store; it has a cache policy with invalidation rules.
- [ ] Shareable view state (filters, pages, tabs) is in the URL unless a reason is given.
- [ ] Derived values are computed, not stored.
- [ ] Each mutation defines update strategy, rollback and invalidation.
- [ ] Inferred requirements are labeled `[ASSUMPTION]` and listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Putting everything in a global store "for consistency", which makes server data stale and couples unrelated screens. Separate server cache from client state.
- Keeping filters and pagination in memory, so refresh, back navigation and shared links lose the view.
- Optimistic updates without rollback or conflict handling, which silently show data the server rejected.

## Example
Input: "Order list and order detail; edits in detail don't show in list; everything in one global store fetched on app start."

Excerpt of output:
| State | Category | Readers | Writers | Lifetime | Location (target) | Notes |
|---|---|---|---|---|---|---|
| Orders page | Server | List | API | Cache, fresh 30 s `[ASSUMPTION]` | Server cache keyed `orders?status&page` | Invalidated by order update |
| Order detail | Server | Detail, list row | Edit form | Cache | Server cache keyed `order:{id}` | Update writes back to list entry |
| Status filter, page | URL | List | Filter bar | Session | Query string | Enables shareable links |
| Edit draft | Form | Edit form | User | Until save or cancel | Form state | Discarded on navigation with confirm |

Decision: remove orders from the global store; keep only session and feature flags there.
