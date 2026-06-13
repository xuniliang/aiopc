# Acceptance Package

## Goal

Reduce aiopc workflow token consumption while preserving OpenSpec-driven implementation and independent acceptance gates.

## Scope

- Includes: aiopc propose/apply/accept/loop skill prompt structure, reference-file split, compact output contracts, minimal-read guardrails, and local static validation.
- Excludes: product-specific workflows, external token billing instrumentation, changes to non-aiopc skills, and weakening acceptance criteria.

## User Story

As a solo developer using aiopc, I want routine aiopc runs to load less repeated prompt content, so that the workflow stays cheaper and faster without losing quality gates.

## Functional Points

### FP1: Shrink hot-path skill entry prompts

Use case: Starting any aiopc skill loads a concise entry prompt instead of full templates and rare details.

| AC | Acceptance Criteria | Type | Evidence |
|---|---|---|---|
| AC1 | The combined character count of `aiopc-propose/SKILL.md`, `aiopc-apply/SKILL.md`, `aiopc-accept/SKILL.md`, and `aiopc-loop/SKILL.md` is at least 35% below the 11680-character baseline. | automated test | Run the static validation command/script and record before/after counts. |
| AC2 | Each of the four `SKILL.md` files still contains its purpose, required inputs or selection rule, core workflow, stop/escalation rule where applicable, and compact output contract. | automated test | Static validation checks required section markers or keywords per file. |
| AC3 | Detailed templates removed from hot-path entry files are available from adjacent reference files and linked from the relevant `SKILL.md`. | automated test | Static validation checks reference-file existence and links. |

### FP2: Avoid repeated context reads and unnecessary orchestration overhead

Use case: aiopc skills read only the artifacts needed for the current branch of the workflow.

| AC | Acceptance Criteria | Type | Evidence |
|---|---|---|---|
| AC4 | `aiopc-propose`, `aiopc-apply`, and `aiopc-accept` include explicit minimal-read rules scoped to their current mode or validation scope. | automated test | Static validation checks minimal-read guardrail text in each file. |
| AC5 | `aiopc-loop` explicitly delegates implementation and validation details to focused skills and limits chat output to compact status, result, next action, and artifact paths. | automated test | Static validation checks loop delegation and compact-output guardrails. |
| AC6 | The workflow documentation includes a rule to avoid spawning agents when direct reads of known aiopc files are sufficient. | automated test | Static validation checks no-unnecessary-agent guardrail text. |

### FP3: Preserve acceptance quality

Use case: Token optimization does not remove the workflow's quality gates.

| AC | Acceptance Criteria | Type | Evidence |
|---|---|---|---|
| AC7 | `aiopc-accept` still requires independent evidence and forbids using implementation summaries as acceptance proof. | automated test | Static validation checks acceptance evidence guardrails. |
| AC8 | `aiopc-apply` still treats acceptance criteria as frozen unless an approved acceptance-package change request exists. | automated test | Static validation checks frozen-acceptance guardrail. |

## Impact Analysis

- New ACs: AC1-AC8.
- Revalidate old ACs: none; this is a new optimization change.
- Reuse previous results: none.
- Full regression needed: no, because the repo is markdown-only and static validation of all aiopc skill contracts covers the affected surface.
