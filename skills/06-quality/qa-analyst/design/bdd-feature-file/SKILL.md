---
description: "Writes Gherkin feature files with a business-readable feature description, background, declarative scenarios and scenario outlines with example tables, tagged and traceable to requirements. Use when a team practices behavior-driven development or specification by example, when acceptance criteria must become executable specifications, or when existing Gherkin is imperative, UI-bound or hard to maintain."
related: acceptance-criteria, user-story, test-scenarios-from-requirements, test-automation-script, equivalence-boundary-analysis
prompt: "Write a feature file for the coupon rule: one coupon per order, minimum basket 250 TL, not combinable with campaign prices, expired coupons rejected."
---

# Write BDD Feature Files

## Purpose
Express the expected behavior of a feature as concise Gherkin that business people can read and confirm, and that automation can bind to without rewriting.

## When to use
- Acceptance criteria are agreed and the team wants living, executable specifications.
- A three-amigos or refinement session produced examples that need to be written down.
- Existing feature files are long click-by-click scripts that break on every UI change.

## When not to use
- The behavior itself is not yet agreed. Use `acceptance-criteria` to settle the rules first.
- You need detailed manual steps with per-step expected results. Use `test-case-writing`.
- You need the step-definition or automation code. Use `test-automation-script`.

## Inputs
Required:
- The story, acceptance criteria or business rules to specify.

Optional, improves quality:
- Domain glossary and existing step vocabulary, tagging conventions, language setting (`# language: tr` if the team writes Gherkin in Turkish).
- Boundaries and examples already discussed with the business.

If no rule or criterion is given, ask for it. Unclear outcomes become scenarios tagged `@question` with the open point in a comment.

## Process
1. Extract the rules from the input; each rule becomes a `Rule:` block or a group of scenarios. Keep one feature file per capability, not per screen.
2. Write the feature header: name plus a short "In order to / As a / I want" or plain narrative stating the business value. Use a specific role, never "a user".
3. Put only shared, essential context in `Background`; if it is longer than about three steps or not needed by every scenario, move it into the scenarios.
4. For each rule write at least one positive and one negative scenario. Title each scenario with the behavior, not the test ("Coupon is rejected when basket is below minimum").
5. Write steps declaratively in domain language: Given = state, When = one business action, Then = observable outcome. No clicks, selectors, URLs or technical IDs.
6. Keep one When and one Then per scenario (And under Then only for facets of the same outcome); multiple actions or outcomes mean split the scenario.
7. Use `Scenario Outline` with `Examples` for data variations of the same behavior, choosing rows from equivalence classes and boundaries; do not use outlines to hide different behaviors.
8. Reuse existing step phrasing where given so step definitions stay small; keep wording consistent (same noun for the same concept).
9. Add tags for traceability and execution (`@REQ-123`, `@smoke`, `@wip`, `@question`) according to team convention.
10. Label any inferred rule `[ASSUMPTION]` in a comment and list open questions below the file.
11. If the user continues, suggest `test-automation-script` for step definitions or `acceptance-criteria` when open questions change the rules.

## Output format
```gherkin
@<capability-tag> @<REQ-id>
Feature: <capability>
  <business value narrative with a specific role>

  Background:
    Given <shared essential context>

  Rule: <business rule>

    Scenario: <behavior in one sentence>
      Given <state>
      When <one business action>
      Then <observable outcome>

    Scenario Outline: <behavior varying by data>
      Given <state with <param>>
      When <action>
      Then <outcome with <result>>

      Examples:
        | param | result |
```
Open questions / assumptions: numbered list below the file.

## Quality checklist
- [ ] A business stakeholder can read every scenario without technical knowledge.
- [ ] Each scenario has exactly one When and one Then outcome; Given describes state, not actions.
- [ ] No UI mechanics, selectors, URLs or database details in steps.
- [ ] Every rule has at least one negative scenario; boundaries appear in Examples.
- [ ] Scenarios are independent and titled by behavior.
- [ ] Tags provide traceability to requirements and inferred rules are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Imperative scripts ("When I click Apply, And I type ..."). They couple to the UI and hide the rule; describe intent instead.
- Huge Background sections that every reader must scroll past. Keep only what all scenarios need.
- One Scenario Outline with a column that switches between completely different behaviors. Split into separate scenarios.
- Writing Gherkin after automation as documentation of test code. The value comes from agreeing examples before building.

## Example
Input: "One coupon per order, minimum basket 250 TL, not combinable with campaign prices, expired coupons rejected."

Weak:
```gherkin
Scenario: coupon test
  When I open the basket page and type "SAVE10" into #coupon and click Apply
  Then I see a message and the total changes and the second coupon field is disabled
```
Strong (excerpt):
```gherkin
Rule: The basket must reach the minimum amount

  Scenario Outline: Coupon acceptance depends on basket total
    Given a customer's basket totals <total> TL
    When the customer applies a valid coupon
    Then the coupon is <result>

    Examples:
      | total  | result   |
      | 249.99 | rejected |
      | 250.00 | accepted |
```
Open question: Is the minimum checked before or after campaign discounts? `[ASSUMPTION: before]`
