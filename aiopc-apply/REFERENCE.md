# aiopc-apply reference

## change-log.md format

```md
## Round <n>: <initial implementation | rework for AC...>

### Trigger
- <task or failed AC>

### Before
- <observable previous behavior or missing capability>

### After
- <observable new behavior>

### Files changed
- <path>: <why changed>

### Verification
- <command or manual step>: <result>
```

## Implementation candidate format

```md
## Implementation Candidate

Change: <change-id>
Scope: <initial implementation | rework round n>

Completed:
- ...

Tests/verification run:
- `...` -> passed/failed

Acceptance notes:
- ACs intended to satisfy:
- Known blockers:
- Acceptance-package change request needed: yes/no
- UI Design Change Request needed: yes/no
```

## Acceptance-package change request trigger

Draft one instead of coding when an AC is unclear, incorrect, not executable, changed by business scope, or requires broadening implementation beyond the frozen package.

## UI design implementation routing

If `ui-design.md` exists, it is the current UI source of truth. Read it before implementing UI tasks, then read only needed sections from `../aiopc-ui-design/REFERENCE.md`:

- Action Contract / State Ownership: §4.
- Field mapping, style, visibility, responsive, quality baseline: §5.
- PlantUML interpretation: §6.
- Traceability and task linkage: §7.
- Apply rules and UI verification: §8.
- UI design change request: §10.

Implementation requirements:

- UI task must reference UI ID or `ui-design.md` section.
- Data-changing buttons/forms must follow Action Contract and State Ownership.
- Row-level update requires target row/record ID; do not update whole lists by form draft.
- Record implemented UI IDs, linked ACs, and verification in `change-log.md`.
- If browser/UI verification cannot run, record UI Verification Blocker and do not report ready for acceptance.
