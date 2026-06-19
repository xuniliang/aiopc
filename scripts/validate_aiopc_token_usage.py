#!/usr/bin/env python3
from pathlib import Path
import sys

BASELINE_CHARS = 11680
OPTIMIZED_MAX_CHARS = int(BASELINE_CHARS * 0.65)
UI_WORKFLOW_MAX_CHARS = 7600
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


def contains_none(text, needles):
    lowered = text.lower()
    return all(needle.lower() not in lowered for needle in needles)


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
        require("[REFERENCE.md](REFERENCE.md)" in text, f"{skill_path} missing local reference link", failures)
        require((ROOT / name / "REFERENCE.md").exists(), f"{name}/REFERENCE.md missing", failures)
        require("no-unnecessary-agent" in text, f"{skill_path} missing no-unnecessary-agent guardrail", failures)
        require(contains_none(text, ["@startsalt", "@startuml", "| UI Field ID |", "| State | Owner |"]), f"{skill_path} embeds detailed UI template content", failures)

    require(total <= OPTIMIZED_MAX_CHARS, f"hot-path size {total} exceeds optimized max {OPTIMIZED_MAX_CHARS}", failures)
    require(total <= UI_WORKFLOW_MAX_CHARS, f"hot-path size {total} exceeds UI workflow max {UI_WORKFLOW_MAX_CHARS}", failures)

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
        require("../aiopc-ui-design/REFERENCE.md" in text, f"{path} missing shared UI reference route", failures)

    for path, text in [
        ("aiopc-apply/SKILL.md", apply),
        ("aiopc-accept/SKILL.md", accept),
        ("aiopc-loop/SKILL.md", loop),
    ]:
        require("## Stop / Escalate" in text, f"{path} missing Stop / Escalate section", failures)

    require(contains_all(loop, ["Delegate", "artifact paths"]), "aiopc-loop missing delegation or compact-output guardrails", failures)
    require(contains_all(accept, ["independent evidence", "implementation summaries", "proof"]), "aiopc-accept missing independent-evidence guardrails", failures)
    require(contains_all(apply, ["Frozen acceptance", "approved acceptance-package change request"]), "aiopc-apply missing frozen-acceptance guardrail", failures)
    require(contains_all(propose, ["no/light/full", "ui-design.md", "user chooses"]), "aiopc-propose missing UI mode recommendation and user-choice route", failures)
    require(contains_all(apply, ["ui-design.md", "Action Contracts", "State Ownership", "UI verification"]), "aiopc-apply missing UI implementation linkage", failures)
    require(contains_all(accept, ["ui-design.md", "Action Contracts", "State Ownership", "UI evidence"]), "aiopc-accept missing UI validation linkage", failures)
    require(contains_all(loop, ["ui-design.md", "do not parse", "focused skills"]), "aiopc-loop missing thin UI orchestration rule", failures)

    for path in [
        "aiopc-propose/REFERENCE.md",
        "aiopc-apply/REFERENCE.md",
        "aiopc-accept/REFERENCE.md",
        "aiopc-loop/REFERENCE.md",
    ]:
        text = read(path)
        require("```" in text, f"{path} missing detailed template block", failures)
        require("../aiopc-ui-design/REFERENCE.md" in text, f"{path} missing shared UI reference route", failures)

    ui_ref_path = ROOT / "aiopc-ui-design" / "REFERENCE.md"
    require(ui_ref_path.exists(), "aiopc-ui-design/REFERENCE.md missing", failures)
    ui_ref = ui_ref_path.read_text() if ui_ref_path.exists() else ""

    required_ui_sections = [
        "## 何时读取本文档",
        "## 快速路由",
        "## §1 模式选择",
        "## §2 ui-design.md 最低模板",
        "## §3 稳定 UI ID",
        "## §4 Action Contract 与 State Ownership",
        "## §5 字段、样式、权限、响应式和质量底线",
        "## §6 PlantUML Demo",
        "## §7 全流程联动",
        "## §8 apply 规则",
        "## §9 accept 规则与证据",
        "## §10 UI Design Change Request",
    ]
    for section in required_ui_sections:
        require(section in ui_ref, f"aiopc-ui-design/REFERENCE.md missing section: {section}", failures)

    ui_needles = [
        "不启用", "light", "full", "必须让用户选择", "纯后端", "API", "批处理",
        "元信息", "页面清单", "表单清单", "页面设计", "表单设计", "Action Contracts", "PlantUML", "追踪矩阵", "实现任务映射",
        "UI-PAGE-001", "UI-FORM-001", "UI-ACTION-001", "UI-STATE-001", "UI-FIELD-001", "UI-DEMO-001", "UI-DECISION-001", "不因标题改名", "不复用",
        "@startsalt", "@startuml", "ui-design-assets/*.puml", "超过 80 行", "超过 3 张图",
        "Scope", "Target ID", "Payload", "Affected Data", "Not Affected Data", "UI State Changes", "Failure Behavior", "Implementation Constraints", "Acceptance Checks",
        "State Ownership", "Owner", "Can Mutate By", "Must Not Mutate",
        "Data Source", "Submit Field", "Display Format",
        "Proposal Goal", "Design Decision", "Acceptance AC", "Task", "Implementation Evidence", "Validation Evidence",
        "UI Design Change Request", "ui-design-change-log.md", "ui-design-change-requests/", "当前有效 `ui-design.md`",
        "Style Fidelity", "Visibility & Enablement", "Responsive Scope", "UI Quality Baseline", "low", "medium", "high", "desktop-only", "desktop-first", "responsive",
        "UI Validation", "截图", "前后数据记录",
    ]
    for needle in ui_needles:
        require(needle in ui_ref, f"aiopc-ui-design/REFERENCE.md missing rule text: {needle}", failures)

    print("aiopc token usage and UI workflow validation")
    for path, chars in sizes.items():
        print(f"- {path}: {chars} chars")
    reduction = (BASELINE_CHARS - total) / BASELINE_CHARS * 100
    print(f"- total: {total} chars")
    print(f"- baseline: {BASELINE_CHARS} chars")
    print(f"- optimized max: {OPTIMIZED_MAX_CHARS} chars")
    print(f"- ui workflow max: {UI_WORKFLOW_MAX_CHARS} chars")
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
