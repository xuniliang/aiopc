#!/usr/bin/env python3
from pathlib import Path
import sys

BASELINE_CHARS = 11680
MAX_CHARS = int(BASELINE_CHARS * 0.65)
SKILL_DIRS = ["aiopc-propose", "aiopc-apply", "aiopc-accept", "aiopc-loop"]
ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text()


def require(condition, message, failures):
    if not condition:
        failures.append(message)


def contains_all(text, needles):
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def main():
    failures = []
    sizes = {}
    total = 0

    for name in SKILL_DIRS:
        skill_path = Path(name) / "SKILL.md"
        text = read(skill_path)
        sizes[str(skill_path)] = len(text)
        total += len(text)
        require("## Purpose" in text, f"{skill_path} missing Purpose section", failures)
        require("## Workflow" in text, f"{skill_path} missing Workflow section", failures)
        require("## Output contract" in text, f"{skill_path} missing Output contract", failures)
        require("[REFERENCE.md](REFERENCE.md)" in text, f"{skill_path} missing reference link", failures)
        require((ROOT / name / "REFERENCE.md").exists(), f"{name}/REFERENCE.md missing", failures)
        require("no-unnecessary-agent" in text, f"{skill_path} missing no-unnecessary-agent guardrail", failures)

    require(total <= MAX_CHARS, f"hot-path size {total} exceeds max {MAX_CHARS}", failures)

    propose = read("aiopc-propose/SKILL.md")
    apply = read("aiopc-apply/SKILL.md")
    accept = read("aiopc-accept/SKILL.md")
    loop = read("aiopc-loop/SKILL.md")

    require("## Mode selection" in propose, "aiopc-propose missing selection rule", failures)
    for path, text in [
        ("aiopc-propose/SKILL.md", propose),
        ("aiopc-apply/SKILL.md", apply),
        ("aiopc-accept/SKILL.md", accept),
    ]:
        require("## Minimal reads" in text, f"{path} missing Minimal reads section", failures)

    for path, text in [
        ("aiopc-apply/SKILL.md", apply),
        ("aiopc-accept/SKILL.md", accept),
        ("aiopc-loop/SKILL.md", loop),
    ]:
        require("## Stop / Escalate" in text, f"{path} missing Stop / Escalate section", failures)

    require(contains_all(loop, ["Delegate", "compact status", "artifact paths"]), "aiopc-loop missing delegation or compact-output guardrails", failures)
    require(contains_all(accept, ["independent evidence", "implementation summaries", "proof"]), "aiopc-accept missing independent-evidence guardrails", failures)
    require(contains_all(apply, ["Frozen acceptance", "frozen unless", "approved acceptance-package change request"]), "aiopc-apply missing frozen-acceptance guardrail", failures)

    for path in [
        "aiopc-propose/REFERENCE.md",
        "aiopc-apply/REFERENCE.md",
        "aiopc-accept/REFERENCE.md",
        "aiopc-loop/REFERENCE.md",
    ]:
        text = read(path)
        require("```" in text, f"{path} missing detailed template block", failures)

    print("aiopc token usage validation")
    for path, chars in sizes.items():
        print(f"- {path}: {chars} chars")
    reduction = (BASELINE_CHARS - total) / BASELINE_CHARS * 100
    print(f"- total: {total} chars")
    print(f"- baseline: {BASELINE_CHARS} chars")
    print(f"- required max: {MAX_CHARS} chars")
    print(f"- reduction: {reduction:.1f}%")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
