# UI 设计工作流变更记录

## 变更前

- aiopc 已有 propose/apply/accept/loop 四段工作流。
- 高频入口 skill 已经过 token 优化，详细模板被移动到 reference 文件。
- 网页型需求没有专门的 UI 设计产物，页面、表单、按钮、状态、样式和动作作用范围主要依赖普通 proposal/design/acceptance 描述。
- 缺少统一的 Action Contract、State Ownership、PlantUML demo、UI 追踪矩阵和 UI 设计变更机制。

## 变更后

- 四个高频 `SKILL.md` 增加了短 UI 设计路由：propose 推荐 no/light/full，apply/accept 在存在 `ui-design.md` 时按需读取并联动，loop 只传递上下文。
- 新增 `aiopc-ui-design/REFERENCE.md` 作为共享深层参考，包含“何时读取本文档”和“快速路由”，避免高频入口一次性导入完整规范。
- `ui-design.md` 规范支持元信息、页面/表单/动作/状态、Action Contract、State Ownership、Style Fidelity、UI Field ID/Data Source/Submit Field/Display Format、Visibility & Enablement、Responsive Scope、UI Quality Baseline、PlantUML Salt/Activity、追踪矩阵、实现任务映射。
- UI 设计变更采用单一当前有效 `ui-design.md`、`ui-design-change-log.md`、`ui-design-change-requests/`。
- 静态校验可验证热路径大小、按需读取规则、共享 reference 结构和关键 UI 工作流规则。

## 验证

- `python3 scripts/validate_aiopc_token_usage.py`: PASS；四个高频入口合计 7201 字符，基线 11680，优化上限 7592，UI workflow 上限 7600，降幅 38.3%。
