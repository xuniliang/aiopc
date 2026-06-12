# aiopc workflow skills change log

## Before

- No `aiopc-*` skills existed under `/Users/liang/.claude/skills`.
- The one-person-company workflow decisions existed only in conversation and memory.

## After

Added four generic, non-tuomai-specific Claude skills:

- `aiopc-propose/SKILL.md` — creates or updates OpenSpec changes and concise acceptance packages.
- `aiopc-apply/SKILL.md` — implements against frozen acceptance packages and records `change-log.md` rounds.
- `aiopc-accept/SKILL.md` — independently validates ACs, writes validation reports, rework packages, and acceptance-package change requests.
- `aiopc-accept/REFERENCE.md` — stores detailed output templates so the main skill stays concise.
- `aiopc-loop/SKILL.md` — orchestrates apply/accept/rework cycles with a default maximum of two automatic rework rounds.

## Verification intent

- Each skill has a frontmatter description with explicit trigger conditions.
- Each skill keeps a focused responsibility instead of one large workflow skill.
- The workflow uses OpenSpec as the change source of truth and acceptance evidence as the completion gate.
