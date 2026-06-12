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
- Constraints:

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
