## MODIFIED Requirements

### Requirement: aiopc SHALL support optional UI design workflow for webpage requirements

aiopc SHALL recommend an optional UI design workflow when a requirement involves pages, forms, buttons, interactions, visual layout, or UI states.

#### Scenario: UI design mode is recommended

- **WHEN** `aiopc-propose` receives a webpage-style requirement
- **THEN** it SHALL recommend one of: no UI design, light `ui-design.md`, or full `ui-design.md`
- **AND** it SHALL let the user choose before generating the UI design artifact

#### Scenario: Non-UI requirement does not create UI design noise

- **WHEN** a requirement is pure backend, API, batch, data repair, or configuration work
- **THEN** `aiopc-propose` SHALL default to no `ui-design.md`
- **AND** it SHALL record the reason in proposal artifacts when relevant

### Requirement: aiopc UI design SHALL be traceable across workflow artifacts

When enabled, `ui-design.md` SHALL guide proposal, design, acceptance, tasks, implementation, validation, and change logs.

#### Scenario: Stable UI IDs are used

- **WHEN** `ui-design.md` defines pages, forms, actions, states, fields, demos, or UI decisions
- **THEN** each traceable item SHALL have a stable UI ID
- **AND** tasks, ACs, implementation logs, and validation reports SHALL reference those IDs where applicable

#### Scenario: Traceability matrix links lifecycle artifacts

- **WHEN** `ui-design.md` is enabled
- **THEN** it SHALL include a traceability matrix linking UI sections to proposal goals, design decisions, ACs, tasks, implementation evidence, and validation evidence

### Requirement: aiopc UI actions SHALL prevent unintended broad data mutation

UI actions that change business data SHALL define exact action scope and state ownership constraints.

#### Scenario: Data-changing action has an action contract

- **WHEN** a button, form submit, link, menu item, or batch operation creates, edits, deletes, submits, enables, disables, or otherwise changes business data
- **THEN** `ui-design.md` SHALL define its Action Contract with scope, target ID, payload, affected data, not-affected data, UI state changes, failure behavior, implementation constraints, and acceptance checks

#### Scenario: List and form state ownership is explicit

- **WHEN** a UI design includes list data, form drafts, dialogs, selection, pagination, filtering, or batch operations
- **THEN** `ui-design.md` SHALL define State Ownership for relevant states
- **AND** row-level updates SHALL require a target row or record ID

### Requirement: aiopc UI design SHALL be maintainable through approved changes

UI design changes SHALL keep one current source of truth while preserving history.

#### Scenario: Current UI design source is unique

- **WHEN** a change has UI design enabled
- **THEN** the current effective UI implementation source SHALL be `ui-design.md`
- **AND** approved changes SHALL update that file and append `ui-design-change-log.md`
- **AND** pending changes SHALL live under `ui-design-change-requests/`

#### Scenario: Implementation does not silently change UI design

- **WHEN** `aiopc-apply` finds `ui-design.md` inaccurate, conflicting, or not executable
- **THEN** it SHALL stop and draft a UI Design Change Request instead of silently changing implementation scope

### Requirement: aiopc UI design reference SHALL use progressive disclosure

The UI design workflow SHALL not undo hot-path token optimization.

#### Scenario: Shared UI reference is read on demand

- **WHEN** UI design rules are needed
- **THEN** skills SHALL route to needed sections of `aiopc-ui-design/REFERENCE.md`
- **AND** high-frequency `SKILL.md` files SHALL NOT embed full UI templates, Action Contract templates, or PlantUML examples

#### Scenario: Hot-path skill size remains bounded

- **WHEN** static validation is run
- **THEN** the combined character count of `aiopc-propose/SKILL.md`, `aiopc-apply/SKILL.md`, `aiopc-accept/SKILL.md`, and `aiopc-loop/SKILL.md` SHALL be no more than 7600 characters
