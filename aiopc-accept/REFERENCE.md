# aiopc-accept reference

## validation-report.md format

```md
# Validation Report

## Conclusion
passed / failed / blocked

## Scope
- Change:
- Acceptance package version/date:
- Validation strategy: full / failed items + affected regression

## AC Results
| AC | Functional Point | Type | Result | Evidence |
|---|---|---|---|---|
| AC1 | ... | automated test | passed | `npm test ...` passed |

## UI Validation
| UI ID | Expected | Result | Evidence |
|---|---|---|---|

## Reused Previous Results
- ACx: previously passed, related code not touched, result reused.

## Failures
### <AC id>
- Current result:
- Expected result:
- Evidence:
- Suggested repair direction:

## Blockers
- ...

## Acceptance Package Issues
- none / see change request below
```

## Rework package format

```md
# Rework Package

## Goal
Fix validation failures only; do not expand scope.

## Failed ACs
### <AC id>: <title>
- Current result:
- Expected result:
- Evidence:
- Suggested repair direction:

## Regression checks required
- ...

## Prohibited
- Do not change acceptance criteria.
- Do not refactor unrelated code.
- Do not delete, skip, or weaken tests.
```

## Acceptance-package change request format

```md
# Acceptance Package Change Request

## Problem type
unclear / incorrect / not executable / business change / scope change

## Original AC
<quote exact AC>

## Why it is a problem
...

## Proposed change
Before: ...
After: ...

## Impact
- Affects implementation: yes/no
- Affects tests: yes/no
- Expands scope: yes/no
- Requires revalidation: yes/no
```

## UI design validation routing

If `ui-design.md` exists, validate it as UI acceptance basis. Read only needed sections from `../aiopc-ui-design/REFERENCE.md`:

- Action Contract / State Ownership: §4.
- Traceability matrix: §7.
- UI validation evidence: §9.
- UI Design Change Request: §10.

Validation requirements:

- Check implemented UI IDs against `ui-design.md` and linked ACs.
- Data-changing Action Contracts need repeatable evidence or before/after data records.
- Full UI design should include visual evidence for key pages when available.
- If implementation differs from current `ui-design.md` without approved change request, fail the relevant UI ID/AC.
