# Change: improve-aiopc-token-usage

## Why

The aiopc workflow consumes too many tokens for common propose/apply/accept/loop runs because high-frequency skill entry files contain full workflow detail, repeated templates, and broad validation guidance that is loaded even when only a small branch is needed.

## What Changes

- Shrink high-frequency `aiopc-*` `SKILL.md` entry files into concise routing instructions.
- Move verbose templates, examples, and rarely used escalation details into reference files read only when needed.
- Add explicit minimal-read rules so each skill reads only the active change artifacts required for the current mode.
- Tighten loop status, implementation candidate, validation, and rework outputs to compact summaries with artifact links instead of repeated long tables when not needed.
- Add static validation for entry-file size and required token-saving guardrails.

## Out of Scope

- Changing the core aiopc responsibilities: propose, apply, accept, and loop remain separate skills.
- Changing OpenSpec semantics or acceptance standards.
- Adding external token metering services.
- Optimizing unrelated Claude Code skills.

## Success Criteria

- The combined character count of the four high-frequency entry files is reduced by at least 35% from the recorded baseline of 11680 characters.
- Each high-frequency skill still exposes its trigger, minimal inputs, stop conditions, and required output contract.
- Detailed templates remain available in reference files for cases that need them.
- The workflow includes explicit rules to avoid repeated reads, unnecessary agents, unnecessary full revalidation, and verbose duplicate summaries.
