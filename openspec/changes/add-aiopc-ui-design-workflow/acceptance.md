# 验收包

## 目标

为 aiopc 增加可选的网页型需求 UI 设计工作流，让页面、表单、按钮、状态、样式、PlantUML demo 和实现/验收联动在需求阶段被明确，同时不让高频 skill token 消耗回涨。

## 范围

- 包含：UI 设计模式推荐、共享按需读取参考规范、`ui-design.md` 模板规则、Action Contract、State Ownership、稳定 UI ID、追踪矩阵、UI 设计变更机制、apply/accept/loop 联动、静态校验。
- 不包含：具体业务页面设计、PlantUML 图片渲染、UI 自动化框架接入、新增独立 skill、改变 OpenSpec 基础流程。

## 用户故事

作为使用 aiopc 的开发者，我希望网页型需求在实现前明确页面、表单、按钮、状态、样式和动作作用范围，并能追踪到任务和验收证据，从而减少实现偏差和返工。

## 功能点

### FP1：网页型需求推荐 UI 设计模式

用例：`aiopc-propose` 识别网页/表单/按钮/交互需求后推荐 UI 设计模式，而不是强制启用。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC1 | `aiopc-propose` 的工作流或 reference 明确支持三种模式：不启用、轻量 `ui-design.md`、完整 `ui-design.md`，并要求用户选择。 | automated test | 静态校验检查模式说明和用户选择规则。 |
| AC2 | 纯后端/API/批处理/无页面交互需求默认不启用 `ui-design.md`，且可记录原因。 | automated test | 静态校验检查 no-UI 场景规则。 |

### FP2：共享 UI 设计规范按需读取

用例：新增 UI 能力时不把完整模板塞回高频入口文件。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC3 | 新增 `aiopc-ui-design/REFERENCE.md`，包含“何时读取本文档”和“快速路由”，并按章节组织生成、实现、验收、变更所需内容。 | automated test | 静态校验检查文件和章节。 |
| AC4 | 四个高频 `SKILL.md` 不复制完整 `ui-design.md` 模板、Action Contract 模板或 PlantUML 示例，只保留短路由规则。 | automated test | 静态校验检查禁止内容和引用方式。 |
| AC5 | 四个高频 `SKILL.md` 合计字符数不超过 7600。 | automated test | 静态校验输出字符统计。 |

### FP3：`ui-design.md` 模板覆盖网页实现关键细节

用例：启用 UI 设计后，开发者能明确页面、表单、字段、按钮、状态、样式和 PlantUML demo。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC6 | 共享规范定义轻量和完整 `ui-design.md` 的最低内容要求，完整模式包含元信息、页面清单、表单清单、页面设计、表单设计、Action Contracts、PlantUML、追踪矩阵和实现任务映射。 | automated test | 静态校验检查模板章节。 |
| AC7 | 共享规范定义稳定 UI ID 规则，覆盖 Page/Form/Action/State/Field/Demo/Decision，并说明 ID 不因标题改名而变化且不复用。 | automated test | 静态校验检查 UI ID 规则。 |
| AC8 | 共享规范定义 PlantUML Salt 页面线框图和复杂交互 Activity 图规则，并说明内嵌/拆分到 `ui-design-assets/*.puml` 的触发条件。 | automated test | 静态校验检查 PlantUML 与拆分规则。 |

### FP4：按钮、表单和状态作用范围可验证

用例：避免单个按钮或表单误更新整列表数据。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC9 | 共享规范定义 Action Contract，要求数据变更 action 写明 Scope、Target ID、Payload、Affected Data、Not Affected Data、UI State Changes、Failure Behavior、Implementation Constraints、Acceptance Checks。 | automated test | 静态校验检查 Action Contract 字段。 |
| AC10 | 共享规范定义 State Ownership，要求列表、表单草稿、选择、分页、筛选等状态写明 Owner、Scope、Can Mutate By、Must Not Mutate。 | automated test | 静态校验检查 State Ownership 字段。 |
| AC11 | 共享规范定义 UI Field ID、Data Source、Submit Field、Display Format，避免展示字段和提交字段混淆。 | automated test | 静态校验检查字段映射规则。 |

### FP5：UI 设计与 aiopc 全流程联动

用例：`ui-design.md` 不只是设计文档，而是指导任务、实现、验收和变更追溯。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC12 | 共享规范定义 UI 设计追踪矩阵，链接 UI Section、Proposal Goal、Design Decision、Acceptance AC、Task、Implementation Evidence、Validation Evidence。 | automated test | 静态校验检查追踪矩阵字段。 |
| AC13 | `tasks.md` 规则要求 UI task 引用 UI ID 或 `ui-design.md` section；`ui-design.md` 末尾提供实现任务映射；UI 变更时同步更新 task。 | automated test | 静态校验检查任务联动规则。 |
| AC14 | `aiopc-apply` 规则要求存在 `ui-design.md` 时读取并遵守它，发现冲突时停止并提出 UI Design Change Request；启用 UI 设计时必须记录必要 UI 验证或 blocker。 | automated test | 静态校验检查 apply 联动规则。 |
| AC15 | `aiopc-accept` 规则要求存在 `ui-design.md` 时作为 UI 验收依据，并记录 UI Validation、Action Contract 和追踪矩阵相关证据。 | automated test | 静态校验检查 accept 联动规则。 |
| AC16 | `aiopc-loop` 规则要求只传递 UI 设计上下文，不全量解析或复制 UI 细节。 | automated test | 静态校验检查 loop 联动规则。 |

### FP6：UI 设计变更可维护

用例：多次 UI 变更后仍有唯一当前实现依据和可追溯历史。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC17 | 共享规范定义每个 change 只有一个当前有效 `ui-design.md`，已批准变更写入 `ui-design-change-log.md`，未批准请求写入 `ui-design-change-requests/`。 | automated test | 静态校验检查变更机制规则。 |
| AC18 | 共享规范定义 UI Design Change Request 模板，包含变更类型、原设计、变更后设计、变更原因、影响分析和需要重验的 AC/Task。 | automated test | 静态校验检查变更请求模板。 |

### FP7：UI 质量和验证边界明确

用例：网页实现不仅功能正确，还满足必要的样式、权限、响应式、错误提示和防误操作底线。

| AC | 验收标准 | 类型 | 证据 |
|---|---|---|---|
| AC19 | 共享规范定义 Style Fidelity、Visibility & Enablement、Responsive Scope 和 UI Quality Baseline。 | automated test | 静态校验检查这些章节和默认值。 |
| AC20 | 共享规范定义 UI 验收证据规则：轻量至少一种 UI 证据，完整关键页面建议截图，数据变更 action 必须有可重复证据或前后数据记录。 | automated test | 静态校验检查 UI evidence 规则。 |

## 影响分析

- 新 AC：AC1-AC20。
- 需要重验旧 AC：需要重验 `improve-aiopc-token-usage` 的热路径大小目标，因为本次会修改高频 `SKILL.md`。
- 可复用旧结果：旧的 11680 字符基线和 7021 字符优化结果可作为背景，但本次必须重新测量。
- 是否需要完整回归：不需要业务功能回归；该仓库为 markdown/workflow repo，静态校验覆盖受影响面。
