# 变更：add-aiopc-ui-design-workflow

## 为什么

网页型需求容易因为页面、表单、按钮、样式、状态和动作作用范围没有提前明确，导致实现与需求理解不一致，产生返工。尤其是列表页中的编辑、保存、批量操作等按钮，如果没有明确作用范围和状态归属，可能出现单个按钮或表单误更新整列表数据的问题。

## 变更内容

- 在 `aiopc-propose` 中增加网页型需求识别与 UI 方案推荐决策点，支持不启用、轻量 `ui-design.md`、完整 `ui-design.md` 三种模式。
- 新增共享参考规范 `aiopc-ui-design/REFERENCE.md`，采用渐进式披露和按需读取，不新增独立 skill。
- 定义 `ui-design.md` 的页面、表单、动作、状态、样式、PlantUML demo、追踪矩阵和实现任务映射规范。
- 增加 Action Contract、State Ownership、UI Field ID、字段映射、权限/可见性、响应式范围、UI 质量底线等约束。
- 定义 UI 设计变更机制：单一当前有效 `ui-design.md`、`ui-design-change-log.md`、`ui-design-change-requests/`。
- 让 `aiopc-apply`、`aiopc-accept`、`aiopc-loop` 在存在 `ui-design.md` 时与其联动。
- 保持热路径 token 控制：四个高频 `SKILL.md` 合计不超过 7600 字符，且不得复制完整 UI 模板。

## 不包含

- 不为具体业务需求生成真实 `ui-design.md`。
- 不渲染 PlantUML 图片。
- 不引入 UI 自动化测试框架。
- 不新增独立 skill。
- 不改变 OpenSpec 基础流程和既有验收门禁。

## 成功标准

- OpenSpec/aiopc 工作流能够在网页型需求中推荐是否启用 UI 设计文档。
- 共享 UI 设计参考规范完整覆盖已确认的页面、表单、动作、状态、PlantUML、追踪和变更规则。
- apply/accept/loop 的职责被更新为按存在的 `ui-design.md` 执行、验收或传递上下文。
- 静态校验能够验证热路径大小、按需读取、模板不复制、引用完整性和关键规则存在。
