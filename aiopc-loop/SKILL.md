---
name: aiopc-loop
description: Orchestrate the aiopc implementation and acceptance loop for an OpenSpec change with bounded automatic rework. Use when the user wants the workflow to implement, validate, repair, and revalidate a change with minimal manual prompting.
---

# aiopc-loop

Coordinate the workflow. Do not directly implement code or make acceptance judgments here; route work to the focused skills and enforce stop conditions.

## Responsibilities

- Select the OpenSpec change and acceptance package.
- Run `aiopc-apply` for implementation or rework.
- Run `aiopc-accept` for independent validation.
- Feed the rework package back to `aiopc-apply` when validation fails.
- Stop after success, blocker, acceptance-package issue, or the automatic rework limit.

## Loop

```text
propose/frozen acceptance exists
  -> aiopc-apply
  -> aiopc-accept
  -> if passed: stop and report ready for user spot-check
  -> if failed with rework package: aiopc-apply rework
  -> aiopc-accept revalidation
  -> repeat up to 2 automatic rework rounds
  -> otherwise escalate to user
```

## Default limits

- Maximum automatic rework rounds: 2.
- Rework scope: failed ACs plus affected regression checks only.
- Revalidation scope: failed ACs plus affected regression checks by default.
- Full revalidation only when impact requires it.

## Stop and escalate when

- The same AC fails twice.
- More than 2 rework rounds are needed.
- Acceptance package appears wrong, ambiguous, or not executable.
- Product or business decision is required.
- Fix requires scope expansion.
- Fix touches core architecture, permissions, data model, state flow, or shared query semantics beyond the accepted scope.
- Test evidence and browser/manual evidence conflict.
- Environment cannot run, start, or validate.

## Status output

```md
## aiopc Loop Status

Change: <change-id>
Round: <initial | rework 1 | rework 2>
State: implementing / validating / passed / failed / blocked / escalated

Current result:
- ...

Next action:
- ...

User decision needed:
- none / <specific question>
```

## Final output

```md
## aiopc Loop Complete

Change: <change-id>
Conclusion: passed / escalated / blocked

Validation summary:
- Passed ACs:
- Failed ACs:
- Blockers:
- Acceptance-package change requests:

Artifacts updated:
- acceptance.md
- validation-report.md
- change-log.md
- tasks.md

Recommended user spot-check:
- <small list of high-value checks>
```

## Guardrails

- Do not reinterpret requirements; send unclear scope back to `aiopc-propose` or the user.
- Do not claim acceptance without `aiopc-accept` evidence.
- Do not continue automatic repair after a stop condition.
- Prefer speed by revalidating only failed and affected items, but never skip high-impact regressions.
