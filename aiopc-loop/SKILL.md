---
name: aiopc-loop
description: Orchestrate aiopc apply/accept/rework cycles for a frozen OpenSpec change with bounded automatic repair.
---

# aiopc-loop

## Purpose

Coordinate `aiopc-apply` and `aiopc-accept`. Do not implement code or make acceptance judgments here.

## Inputs

- OpenSpec change id or enough context to select one.
- Frozen `acceptance.md`.
- Optional latest validation or rework package.

## Minimal reads

Read only enough to select the change, confirm acceptance exists, detect `ui-design.md`, and route next step. Delegate implementation, validation, and UI detail reads to focused skills.

## Workflow

1. If acceptance is missing/unclear, route to `aiopc-propose` or ask the user.
2. Pass `ui-design.md` context when present; do not parse or paste UI details.
3. Run `aiopc-apply` for implementation or scoped rework.
4. Run `aiopc-accept` for independent validation.
5. Repeat failed rework up to two rounds; stop on pass, blocker, bad acceptance/UI design, user decision, or limit.

## Stop / Escalate

Escalate when the same AC fails twice, more than two rework rounds are needed, scope expands, core architecture/data/permissions/state/query semantics are touched beyond scope, evidence conflicts, or validation cannot run.

## Output contract

Use compact status only: change id, round, state, result, next action, user decision, and artifact paths. Do not paste long tables in chat. Details: [REFERENCE.md](REFERENCE.md).

## Guardrails

- Delegate: do not reinterpret requirements or duplicate focused-skill work.
- Do not claim acceptance without `aiopc-accept` evidence.
- Prefer failed-and-affected revalidation; full revalidation only when impact requires it.
- no-unnecessary-agent: direct reads for known aiopc artifacts; agents only for broad unknown exploration.
