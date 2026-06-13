## MODIFIED Requirements

### Requirement: aiopc skills SHALL minimize hot-path prompt size

The aiopc workflow skills SHALL keep high-frequency entry prompts concise while preserving the workflow contract required to route work safely.

#### Scenario: Entry file size is reduced

- **WHEN** the optimized skill entry files are measured
- **THEN** the combined character count of `aiopc-propose/SKILL.md`, `aiopc-apply/SKILL.md`, `aiopc-accept/SKILL.md`, and `aiopc-loop/SKILL.md` SHALL be at least 35% lower than the 11680-character baseline

#### Scenario: Rare details remain available

- **WHEN** a skill needs a detailed template, example, or rare escalation rule
- **THEN** the skill SHALL point to an adjacent reference file instead of embedding the full detail in the hot-path entry file

### Requirement: aiopc workflow SHALL avoid avoidable repeated context reads

The aiopc workflow SHALL instruct skills to read only the artifacts needed for the current mode and validation scope.

#### Scenario: Implementation uses focused reads

- **WHEN** `aiopc-apply` handles a normal implementation or rework
- **THEN** it SHALL read the active OpenSpec artifacts, acceptance package, and only current validation or rework artifacts relevant to that scope

#### Scenario: Loop orchestration stays thin

- **WHEN** `aiopc-loop` coordinates apply and accept rounds
- **THEN** it SHALL not duplicate detailed implementation or validation output in chat beyond compact status and artifact paths

### Requirement: aiopc workflow SHALL preserve acceptance quality

Token reduction SHALL NOT weaken acceptance standards or remove independent validation.

#### Scenario: Validation remains evidence-based

- **WHEN** `aiopc-accept` validates an implementation candidate
- **THEN** it SHALL still obtain independent evidence and SHALL NOT accept implementation summaries as proof
