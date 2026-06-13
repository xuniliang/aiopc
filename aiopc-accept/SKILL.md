---
name: aiopc-accept
description: Independently validate an aiopc/OpenSpec change, produce evidence, validation report, and rework/change requests when needed.
---

# aiopc-accept

## Purpose

Validate independently. Implementation summaries are claims, never proof.

## Inputs

- OpenSpec change id.
- `acceptance.md`.
- Implementation candidate or rework result.
- Latest `validation-report.md` only for revalidation.

## Minimal reads

Read acceptance and artifacts needed for the current AC scope. First validation covers all ACs. Revalidation covers failed ACs plus affected regression checks. Reuse previous passes only when related code and evidence inputs were untouched.

## Workflow

1. Determine validation scope.
2. Obtain independent evidence with tests, API calls, data checks, browser checks, or logs.
3. Classify each AC as `passed`, `failed`, `blocked`, or `not-run`.
4. Write/update `validation-report.md` without deleting history.
5. Write a rework package for implementation defects, or an acceptance-package change request for bad ACs.

## Stop / Escalate

Escalate to full revalidation when impact is broad/unclear, or shared components, core rules, data structures, permissions, state flows, query semantics, or repeated failures are involved.

## Output contract

Return conclusion, scope, failures/blockers, artifact paths, and next action. Long tables/templates belong in files using [REFERENCE.md](REFERENCE.md).

## Guardrails

- Require independent evidence for every passed AC.
- Do not use implementation summaries as proof.
- Do not treat blocked validation as passed.
- Do not modify code or lower acceptance standards.
- no-unnecessary-agent: direct reads/commands for known validation artifacts; agents only for broad unknown exploration.
