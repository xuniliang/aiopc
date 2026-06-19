---
name: aiopc-propose
description: Create or update an OpenSpec change and concise acceptance package for aiopc requirements, continuations, and functional optimizations.
---

# aiopc-propose

## Purpose

Prepare a small, verifiable OpenSpec change and acceptance package. Do not implement.

## Mode selection

- `new`: new capability or independent bug fix.
- `continue`: unfinished existing change.
- `extend`: add or optimize an existing capability.

For partially done work, inspect active changes before choosing. Ask 1-3 questions only when acceptance accuracy depends on unknown scope, roles, data rules, states, or evidence.

## Minimal reads

Read only what selects mode and acceptance scope. For clear new work, do not scan unrelated code or old changes. For `continue`/`extend`, read only directly relevant change artifacts, acceptance, tasks, and code.

## Workflow

1. State assumptions and select a kebab-case change id.
2. For webpage/form/button work, recommend no/light/full `ui-design.md`; read only needed sections of `../aiopc-ui-design/REFERENCE.md` after user chooses.
3. Create/update proposal, useful design/tasks, spec delta, and `acceptance.md`.
4. Keep acceptance concise: story -> functional point -> AC -> evidence.
5. For `continue`/`extend`, add impact analysis and ask the user to confirm before freezing acceptance.

## Output contract

Return change id, artifact paths, AC summary, open questions, and confirmation request. Put long templates in files, not chat. Details: [REFERENCE.md](REFERENCE.md).

## Guardrails

- Acceptance standards follow user value, not implementation convenience.
- Default AC type is `automated test` unless explicit.
- Do not create vague ACs like "works correctly".
- no-unnecessary-agent: direct reads for known aiopc/OpenSpec files; agents only for broad unknown research.
