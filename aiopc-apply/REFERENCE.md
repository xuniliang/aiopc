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
```

## Acceptance-package change request trigger

Draft one instead of coding when an AC is unclear, incorrect, not executable, changed by business scope, or requires broadening implementation beyond the frozen package.
