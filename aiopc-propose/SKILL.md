---
name: aiopc-propose
description: Create or update an OpenSpec change and a concise acceptance package for one-person-company product development. Use when the user describes a new requirement, says a feature is partially done, wants to continue work, or asks to add/optimize an existing function.
---

# aiopc-propose

Prepare the change before implementation. Keep the output small, verifiable, and generic to the current project; do not hard-code a product name unless the user provides it for the current change.

## Modes

Choose one mode before writing artifacts:

- `new`: new business capability or independent bug fix.
- `continue`: unfinished existing OpenSpec change.
- `extend`: add or optimize a functional point in an existing capability.

If the user says work is partially done, inspect active OpenSpec changes, existing acceptance packages, tasks, and relevant code before choosing. If still ambiguous, ask the user to choose.

## Workflow

1. Understand the request.
   - If critical information is missing, ask 1-3 questions only.
   - Ask only when the answer affects acceptance accuracy, scope, roles, data rules, success/failure states, or evidence.
   - Do not ask questions that can be answered by reading the repo.

2. Select or suggest the change id.
   - Use English kebab-case: `<verb>-<business-object>`.
   - Examples: `add-customer-query`, `improve-order-import`, `fix-payment-status-sync`.
   - Let the user rename it before freezing acceptance.

3. Create or update the OpenSpec change.
   - Use OpenSpec as the source of truth for what changes and why.
   - Keep proposal/design/tasks focused on the requested outcome.
   - For `continue` or `extend`, preserve historical acceptance reports and add new sections instead of overwriting evidence.

4. Create or update `acceptance.md`.
   - Initial package must be concise, accurate, and minimal.
   - Organize by user story -> functional point -> AC -> evidence.
   - Each functional point should usually have 2-5 ACs.
   - If one functional point needs more, split it.
   - Default AC type is `automated test` unless another type is explicitly declared.

5. Add impact analysis for `continue` or `extend`.
   - New ACs.
   - Old ACs that must be revalidated.
   - Old ACs whose previous result can be reused.
   - Whether full regression is needed and why.

6. Ask the user to confirm before freezing acceptance.

## Acceptance package template

```md
# Acceptance Package

## Goal
One sentence describing the business result.

## Scope
- Includes:
- Excludes:

## User Story
As a [role], I want [action/goal], so that [business result].

## Functional Points
### FP1: <name>
Use case: <one user-visible behavior or system action>

| AC | Acceptance Criteria | Type | Evidence |
|---|---|---|---|
| AC1 | ... | automated test | test command/output |
| AC2 | ... | API verification | request/response |

Non-automated reason: <required when Type is not automated test>
Later automation: <yes/no and why>

## Impact Analysis
- New ACs:
- Revalidate old ACs:
- Reuse previous results:
- Full regression needed: yes/no, because ...
```

## Guardrails

- Do not create a long acceptance package to appear thorough.
- Do not use vague ACs such as "works correctly" or "good experience".
- Do not enter implementation in this skill.
- Do not let implementation convenience lower acceptance standards.
- Acceptance can change later only through an acceptance-package change request.
