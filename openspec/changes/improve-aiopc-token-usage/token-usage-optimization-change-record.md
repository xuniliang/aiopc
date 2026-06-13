# Token Usage Optimization Change Record

## Before

- `aiopc-propose/SKILL.md`, `aiopc-apply/SKILL.md`, `aiopc-accept/SKILL.md`, and `aiopc-loop/SKILL.md` contained hot-path workflow instructions plus detailed templates and rare branch rules.
- Baseline measured on 2026-06-13: 340 lines and 11680 characters across the four entry files.
- Repeated context sources included embedded templates, broad artifact-read instructions, verbose loop output contracts, and duplicated validation/rework table formats.

## After

- The four high-frequency entry files now contain concise routing instructions, required inputs/selection, core workflow, stop/escalation rules, compact output contracts, and quality guardrails.
- Detailed proposal, apply, accept, and loop templates now live in adjacent `REFERENCE.md` files.
- Minimal-read and no-unnecessary-agent guardrails are explicit in hot-path skill files.
- Static validation is available at `scripts/validate_aiopc_token_usage.py`.
- Optimized total measured by validation script: 7021 characters, a 39.9% reduction from baseline.

## Verification

- `python3 scripts/validate_aiopc_token_usage.py`: PASS; total 7021 chars, baseline 11680 chars, required max 7592 chars, reduction 39.9%.
