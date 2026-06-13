# aiopc-propose reference

## Acceptance package format

```md
# Acceptance Package

## Goal
<one sentence>

## Scope
- Includes:
- Excludes:

## User Story
As a [role], I want [action/goal], so that [business result].

## Functional Points
### FP1: <name>
Use case: <one visible behavior or system action>

| AC | Acceptance Criteria | Type | Evidence |
|---|---|---|---|
| AC1 | ... | automated test | command/output |

Non-automated reason: <required when Type is not automated test>
Later automation: <yes/no and why>

## Impact Analysis
- New ACs:
- Revalidate old ACs:
- Reuse previous results:
- Full regression needed: yes/no, because ...
```

## Change id guidance

Use English kebab-case: `<verb>-<business-object>`.

Examples: `add-customer-query`, `improve-order-import`, `fix-payment-status-sync`.

## Proposal artifact checklist

- `proposal.md`: why, what changes, out of scope, success criteria.
- `design.md`: only when tradeoffs or structure matter.
- `tasks.md`: implementation checklist.
- `specs/<capability>/spec.md`: OpenSpec requirement delta.
- `acceptance.md`: frozen only after user confirmation.
