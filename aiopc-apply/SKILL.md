---
name: aiopc-apply
description: Implement a frozen aiopc/OpenSpec change or scoped rework package with focused TDD-style vertical slices.
---

# aiopc-apply

## Purpose

Implement only accepted scope. Treat `acceptance.md` as frozen unless the user approves an acceptance-package change request.

## Inputs

- OpenSpec change id.
- `acceptance.md`.
- Optional rework package or latest `validation-report.md`.

## Minimal reads

Read proposal/tasks/spec delta/acceptance for the active change. If `ui-design.md` exists, read it and only needed sections of `../aiopc-ui-design/REFERENCE.md`. Do not reread history unless it affects current scope.

## Workflow

1. Choose scope: pending tasks or rework-only failed ACs.
2. Implement slices: behavior test -> minimal code -> pass -> next AC.
3. If UI design exists, follow UI IDs, Action Contracts, State Ownership, and required UI verification.
4. Verify with project commands, preferring ECS-like scripts when present.
5. Update tasks and append `change-log.md`; never overwrite prior rounds.

## Stop / Escalate

Stop and draft an acceptance-package or UI Design Change Request if an AC/UI design is wrong, ambiguous, not executable, conflicting, or requires scope expansion.

## Output contract

Return compact implementation candidate: change id, scope, completed items, verification results, intended ACs, blockers, and whether a change request is needed. Details: [REFERENCE.md](REFERENCE.md).

## Guardrails

- Implementation output is a claim, not acceptance evidence.
- Do not claim final completion; hand off to `aiopc-accept`.
- Frozen acceptance stays frozen unless an approved acceptance-package change request exists.
- no-unnecessary-agent: direct reads for known files; agents only for broad unknown exploration.
