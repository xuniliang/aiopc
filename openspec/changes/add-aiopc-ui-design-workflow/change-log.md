# Change Log

## Round 1: initial implementation

### Trigger
- 实现冻结验收包 `add-aiopc-ui-design-workflow`，覆盖 AC1-AC20。

### Before
- aiopc 没有专门的网页型需求 UI 设计工作流。
- 高频入口 skill 只支持通用 propose/apply/accept/loop 路由。
- 缺少 `ui-design.md` 模式选择、Action Contract、State Ownership、稳定 UI ID、追踪矩阵和 UI 设计变更机制。

### After
- 四个高频 `SKILL.md` 已加入简短 UI 设计路由，并继续保持热路径大小约束。
- 新增 `aiopc-ui-design/REFERENCE.md`，以“何时读取本文档”和“快速路由”实现渐进式披露。
- 共享规范覆盖 no/light/full 模式、`ui-design.md` 模板、稳定 UI ID、Action Contract、State Ownership、字段映射、样式精度、权限可见性、响应式范围、UI 质量底线、PlantUML、追踪矩阵、apply/accept 联动和 UI Design Change Request。
- `aiopc-propose/REFERENCE.md`、`aiopc-apply/REFERENCE.md`、`aiopc-accept/REFERENCE.md`、`aiopc-loop/REFERENCE.md` 已按阶段引用共享规范，不复制完整模板。
- 静态校验脚本已增强，覆盖 token 上限、按需读取、共享 reference 结构和关键 UI 工作流规则。

### Files changed
- `aiopc-propose/SKILL.md`: 增加 no/light/full `ui-design.md` 推荐路由。
- `aiopc-apply/SKILL.md`: 增加存在 `ui-design.md` 时的读取、实现和变更请求规则。
- `aiopc-accept/SKILL.md`: 增加存在 `ui-design.md` 时的 UI 验收联动规则。
- `aiopc-loop/SKILL.md`: 增加只传递 UI 设计上下文、不解析细节的路由规则。
- `aiopc-ui-design/REFERENCE.md`: 新增共享 UI 设计工作流规范。
- `aiopc-propose/REFERENCE.md`: 增加 UI 模式推荐和生成路由。
- `aiopc-apply/REFERENCE.md`: 增加 UI 实现、Action Contract、State Ownership 和 UI 验证路由。
- `aiopc-accept/REFERENCE.md`: 增加 UI Validation、Action Contract 和追踪矩阵验收路由。
- `aiopc-loop/REFERENCE.md`: 增加 UI 设计编排路由。
- `scripts/validate_aiopc_token_usage.py`: 增加 AC1-AC20 相关静态校验。

### Verification
- `python3 scripts/validate_aiopc_token_usage.py`: PASS；四个高频入口合计 7201 字符，基线 11680，优化上限 7592，UI workflow 上限 7600，降幅 38.3%。
