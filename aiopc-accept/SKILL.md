---
name: aiopc-accept
description: Independently validate an OpenSpec change against its acceptance package and produce evidence, a validation report, and rework package when needed. Use when implementation is ready for acceptance, a rework needs revalidation, or acceptance criteria may be inaccurate.
---

# aiopc-accept

Validate independently. The implementer's summary is only a claim to verify, never evidence.

## Inputs

- OpenSpec change id.
- `acceptance.md`.
- Implementation candidate summary or rework result.
- Previous `validation-report.md` if this is a revalidation.

## Workflow

1. Read the acceptance package and relevant OpenSpec artifacts.
2. Determine validation scope.
   - First validation: validate all ACs in scope.
   - Rework validation: validate failed ACs plus affected regression ACs.
   - Full revalidation is required for changes to shared components, core business rules, data structure, permissions, state flows, query semantics, unclear impact, or repeated failures.
3. Obtain evidence independently.
   - Run tests, API calls, data checks, browser checks, or log checks as appropriate.
   - If an AC has no type, treat it as `automated test`.
   - If a non-automated AC lacks a reason, mark the acceptance package as needing correction.
4. Classify each AC as `passed`, `failed`, `blocked`, or `not-run`.
5. Write/update `validation-report.md` without deleting prior history.
6. If failures are implementation defects, write a rework package.
7. If the acceptance package is inaccurate, ambiguous, too broad, or not executable, write an acceptance-package change request.

## Required outputs

Use the templates in [REFERENCE.md](REFERENCE.md).

- `validation-report.md`: conclusion, scope, AC table, reused results, failures, blockers, acceptance-package issues.
- Rework package: only failed ACs, expected/current results, evidence, constraints, and regression checks.
- Acceptance-package change request: problem type, original AC, proposed change, and impact analysis.

## Revalidation strategy

Default to speed:

- Revalidate failed ACs.
- Revalidate ACs affected by implementation changes.
- Reuse previous passed results only when related code was not touched.

Escalate to full revalidation when impact is broad or unclear.

## Guardrails

- Do not pass an AC without evidence.
- Do not treat blocked validation as passed.
- Do not modify code in this skill.
- Do not lower acceptance standards to match the current implementation.
- Do not accept implementation-agent output as evidence.
