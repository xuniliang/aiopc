# Design

## Baseline

Measured on 2026-06-13:

| File | Lines | Characters |
|---|---:|---:|
| `aiopc-propose/SKILL.md` | 92 | 3461 |
| `aiopc-apply/SKILL.md` | 94 | 2918 |
| `aiopc-accept/SKILL.md` | 57 | 2537 |
| `aiopc-loop/SKILL.md` | 97 | 2764 |
| Total | 340 | 11680 |

## Approach

1. Keep `SKILL.md` files as hot-path entry points.
   - Preserve only trigger, inputs, mode selection, core workflow, stop conditions, and compact output contract.
   - Move detailed templates and examples to adjacent `REFERENCE.md` files.

2. Add read-budget guidance per skill.
   - `propose`: read active change list only for continue/extend ambiguity; otherwise write minimal artifacts.
   - `apply`: read proposal/tasks/acceptance and only current validation/rework artifacts.
   - `accept`: read acceptance plus touched artifacts needed to obtain evidence.
   - `loop`: do not read implementation details directly; route to focused skills and summarize.

3. Reduce duplicated output.
   - Status messages should include only change id, state, blockers, next action, and artifact paths.
   - Long AC tables belong in `validation-report.md`, not repeated in chat unless failures need user action.

4. Validate by static checks.
   - Measure hot-path entry file character count against baseline.
   - Check each entry file mentions minimal reads and reference-file loading.
   - Check reference files contain templates moved out of entry files.

## Tradeoffs

- Smaller entry prompts may require one extra file read when a rare template is needed.
- Static size checks prove prompt shrinkage, not real API token billing; they are a practical local proxy for this markdown-only repo.
