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
- `tasks.md`: implementation checklist; for UI tasks, reference UI IDs or `ui-design.md` sections.
- `specs/<capability>/spec.md`: OpenSpec requirement delta.
- `acceptance.md`: frozen only after user confirmation.
- `ui-design.md`: optional; current UI source of truth when enabled.

## UI design routing

For webpage/form/button/interaction requirements, recommend one mode and let the user choose:

- no UI design: pure backend/API/batch/data/config work, or no page/form/button interaction.
- light `ui-design.md`: single-page small change, one button/field/dialog, or local page adjustment.
- full `ui-design.md`: new/multiple pages, forms, list + form, complex interaction, batch operation, or risky data-changing UI.

Read only needed sections of `../aiopc-ui-design/REFERENCE.md`:

- Generate UI design: §1, §2, §3, §4, §5, §8.
- UI change request: §10.

If UI design is enabled, `acceptance.md` must reference `ui-design.md` and include ACs for key UI IDs and data-changing Action Contracts.
