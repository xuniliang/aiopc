---
name: aiopc-apply
description: Implement an OpenSpec change against a frozen acceptance package using focused TDD-style vertical slices. Use when the user wants to implement, continue implementation, or repair failures from an aiopc rework package.
---

# aiopc-apply

Implement only what the OpenSpec change and acceptance package require. Treat the acceptance package as frozen unless the user approves a change request.

## Inputs

- OpenSpec change id.
- `acceptance.md`.
- Optional rework package from `aiopc-accept`.

If the change is ambiguous, inspect active OpenSpec changes and ask only when selection cannot be inferred.

## Workflow

1. Read the OpenSpec change artifacts.
   - proposal/design/tasks/spec deltas, as available.
   - `acceptance.md`.
   - existing `validation-report.md`, rework package, and `change-log.md` if present.

2. Choose the work scope.
   - Normal implementation: follow pending OpenSpec tasks and ACs.
   - Rework: fix only failed ACs and directly affected regression items from the rework package.

3. Implement in vertical slices.
   - Prefer one behavior test -> minimal implementation -> pass -> next behavior.
   - Default AC type is automated test; write tests unless the AC explicitly uses another type.
   - Supplemental tests are allowed and encouraged, but they must not change acceptance standards or scope.

4. Keep changes surgical.
   - Do not refactor unrelated code.
   - Do not delete or skip tests to pass.
   - Do not modify acceptance criteria directly.
   - If an AC is wrong, ambiguous, or not executable, stop and draft an acceptance-package change request.

5. Verify locally using project-appropriate commands.
   - Prefer the same build/start/test scripts expected in ECS-like environments when present.
   - For UI changes, start the app and exercise the path in a browser if available.

6. Update tracking artifacts.
   - Mark completed OpenSpec tasks.
   - Append to `change-log.md` for each implementation or rework round.
   - Do not overwrite previous rounds.

## change-log.md format

```md
## Round <n>: <initial implementation | rework for AC...>

### Trigger
- <task or failed AC>

### Before
- <observable previous behavior or missing capability>

### After
- <observable new behavior>

### Files changed
- <path>: <why changed>

### Verification
- <command or manual step>: <result>
```

## Output

```md
## Implementation Candidate

Change: <change-id>
Scope: <initial implementation | rework round n>

Completed:
- ...

Tests/verification run:
- `...` -> passed/failed

Acceptance notes:
- ACs intended to satisfy:
- Known blockers:
- Acceptance-package change request needed: yes/no
```

## Guardrails

- Implementation output is a claim, not acceptance evidence.
- Do not claim final completion; hand off to `aiopc-accept` for independent validation.
- In rework mode, fix only the rework package plus directly affected regressions.
