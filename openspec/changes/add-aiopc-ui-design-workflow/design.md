# 设计

## 核心决策

### D1：不新增 skill

网页型需求 UI 设计能力嵌入现有 `aiopc-propose`、`aiopc-apply`、`aiopc-accept`、`aiopc-loop`，不新增独立 skill。

原因：网页型需求是现有 aiopc 流程的增强，而不是独立流程。新增 skill 会增加触发判断、上下文切换和 token 成本。

### D2：共享参考规范按需读取

新增 `aiopc-ui-design/REFERENCE.md` 作为共享深层参考文档。四个高频 `SKILL.md` 只保留短路由规则，不复制完整模板。

`aiopc-ui-design/REFERENCE.md` 必须包含：

- 何时读取本文档
- 快速路由
- 模式选择
- `ui-design.md` 模板
- Action Contract
- State Ownership
- PlantUML Salt/Activity 示例
- UI 设计追踪矩阵
- UI Design Change Request
- UI 验收证据规则

### D3：三种 UI 设计模式

- 不启用：纯后端/API/批处理/无页面交互需求。
- 轻量：单页面小改动、单按钮、单字段、小弹窗、局部调整。
- 完整：新页面、多页面、多表单、复杂交互、列表 + 表单、批量操作或高风险数据变更。

`aiopc-propose` 根据需求复杂度给出推荐，但必须让用户选择。

### D4：单一当前有效 UI 设计

每个 OpenSpec change 最多一个当前有效 `ui-design.md`。多次变更直接更新该文件，历史写入 `ui-design-change-log.md`，未批准请求写入 `ui-design-change-requests/`。

实现和验收只以当前 `ui-design.md` 为准，change log 只用于追溯。

### D5：稳定 UI ID 和追踪矩阵

页面、表单、动作、状态、字段、PlantUML demo、UI 决策必须使用稳定 ID，例如：

- `UI-PAGE-001`
- `UI-FORM-001`
- `UI-ACTION-001`
- `UI-STATE-001`
- `UI-FIELD-001`
- `UI-DEMO-001`
- `UI-DECISION-001`

追踪矩阵覆盖需求目标、设计决策、AC、Task、实现证据、验收证据，确保 UI 内容贯穿全流程。

### D6：防误更新约束

通过 Action Contract 和 State Ownership 双重约束按钮与表单行为：

- Action Contract 明确动作作用范围、目标 ID、payload、允许影响和禁止影响的数据。
- State Ownership 明确状态归属、可修改者和禁止修改者。

行级编辑必须携带唯一目标 ID，禁止无 ID 的 row-level update。

### D7：样式和验证按级别控制

- Style Fidelity：`low`、`medium`、`high`。
- Responsive Scope：`desktop-only`、`desktop-first`、`responsive`。
- UI Quality Baseline：只定义底线，不做完整 UX 审计。

轻量模式默认 `low` 和 `desktop-only`；完整模式默认 `medium` 和 `desktop-first`。

## 取舍

- 共享参考文档会增加规范内容，但通过按需读取避免热路径 token 回涨。
- `ui-design.md` 增加了前置设计成本，但能减少网页实现偏差和返工。
- 静态校验能验证结构与规则存在，不能替代具体业务 UI 的浏览器验收；具体需求仍需在对应 change 中验证。
