# aiopc-loop reference

## Loop sequence

```text
frozen acceptance exists
  -> aiopc-apply
  -> aiopc-accept
  -> if passed: stop and report ready for user spot-check
  -> if failed with rework package: aiopc-apply rework
  -> aiopc-accept revalidation
  -> repeat up to 2 automatic rework rounds
  -> otherwise escalate to user
```

## Status format

```md
## aiopc Loop Status

Change: <change-id>
Round: <initial | rework 1 | rework 2>
State: implementing / validating / passed / failed / blocked / escalated

Current result:
- ...

Next action:
- ...

Artifacts:
- ...

User decision needed:
- none / <specific question>
```

## Final format

```md
## aiopc Loop Complete

Change: <change-id>
Conclusion: passed / escalated / blocked

Validation summary:
- Passed ACs:
- Failed ACs:
- Blockers:
- Acceptance-package change requests:
- UI Design Change Requests:

Artifacts updated:
- acceptance.md
- ui-design.md, if enabled
- validation-report.md
- change-log.md
- tasks.md

Recommended user spot-check:
- <small list of high-value checks>
```

## UI design orchestration routing

If `ui-design.md` exists, pass its path to `aiopc-apply` and `aiopc-accept`. Do not parse, summarize, paste, or duplicate UI design details in loop status.

Read `../aiopc-ui-design/REFERENCE.md` only when resolving UI design routing ambiguity, and prefer §7 / §10 only.
