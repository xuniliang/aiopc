# Change Log

## Round 1: initial implementation

### Trigger
- Implement frozen acceptance package for `improve-aiopc-token-usage`.

### Before
- Four high-frequency aiopc `SKILL.md` entry files embedded detailed templates and rare branch rules.
- Baseline: 11680 characters across `aiopc-propose`, `aiopc-apply`, `aiopc-accept`, and `aiopc-loop` entry files.

### After
- Hot-path entry files now contain concise routing instructions, minimal-read rules, compact output contracts, stop/escalation rules, and no-unnecessary-agent guardrails.
- Detailed templates live in adjacent `REFERENCE.md` files.
- Added static validation script for size threshold and required guardrails.
- New total: 7021 characters across the four entry files, a 39.9% reduction.

### Files changed
- `aiopc-propose/SKILL.md`: compact proposal workflow entry.
- `aiopc-propose/REFERENCE.md`: moved acceptance-package and artifact templates.
- `aiopc-apply/SKILL.md`: compact implementation workflow entry.
- `aiopc-apply/REFERENCE.md`: moved change-log and implementation-candidate templates.
- `aiopc-accept/SKILL.md`: compact independent validation entry.
- `aiopc-accept/REFERENCE.md`: retained validation, rework, and change-request templates.
- `aiopc-loop/SKILL.md`: compact orchestration entry.
- `aiopc-loop/REFERENCE.md`: moved loop status/final output templates.
- `scripts/validate_aiopc_token_usage.py`: automated static acceptance checks.

### Verification
- `python3 scripts/validate_aiopc_token_usage.py`: PASS; total 7021 chars, baseline 11680 chars, required max 7592 chars, reduction 39.9%.
