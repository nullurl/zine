---
name: B端设计规范
description: "【B端设计规范 / b-end-design】 基于 Ant Design 的完整 B 端 UI 设计规范，含 Token、组件、页面模式、业务模板和验收 Checklist。导入 AI 工具后可直接作为 B 端设计顾问使用，替换品牌色即可落地。"
license: MIT
author: B-End Design System
tags: [B端, 设计规范, UI, Ant Design, 后台管理]
version: 2.0
---

# B 端设计规范 Skill

## 目录结构

```
skill/
├── SKILL.md                    # 本文件：技能入口与快速参考
├── tokens/                     # 设计基础变量（色彩、字体、间距、圆角阴影）
│   ├── colors.json
│   ├── typography.json
│   ├── spacing.json
│   └── radius-shadow.json
├── references/                 # 详细规范文档
│   ├── components.md           # 组件规范（按钮、输入框、表格、表单、状态）
│   ├── patterns.md             # 页面设计模式（列表页、详情页、表单页、看板）
│   └── templates.md            # 业务场景模板（审批流、权限、消息、异常页）
├── prompts/                    # 场景化 Prompt
│   ├── base.md                 # 基础人设激活 Prompt
│   ├── prototype.md            # 原型生成 Prompt
│   └── review.md               # 代码审查 Prompt
├── rules/                      # 验收标准
│   └── checklist.md            # 上线前设计验收 Checklist
├── guides/                     # 使用指南
│   ├── validation-guide.md     # 规范验证流程指南
│   └── packaging-guide.md      # Skill 打包说明
├── examples/                   # 可运行 HTML 模板
│   ├── list-page/
│   ├── detail-page/
│   └── form-page/
└── assets/                     # 素材文件（图标、示意图等）
```

## 快速激活

将以下内容作为 System Prompt 或对话开头，即可激活本 Skill：

```
你是 B 端产品专属设计规范顾问，严格依据本 Skill 文档作答。
回答原则：
1. 优先输出硬性规则、标准尺寸、禁用项、最佳实践
2. 回答精简落地，不输出冗余科普内容
3. 所有尺寸以 px 为单位，颜色使用 Token 变量名输出
4. 规范未覆盖的场景，说明「未覆盖，建议参考 Ant Design 规范」
```

## 三种使用方式

**查询规范**
> 「按钮的标准高度是多少？」
> 「表格操作列超过几个需要折叠？」
> → AI 查阅 references/components.md 回答

**生成原型**
> 「用这套 Skill 帮我生成一个订单列表页」
> → AI 使用 prompts/prototype.md 人设，结合 tokens/ 变量和 references/patterns.md 模板生成

**自查验收**
> 「帮我检查这段代码是否符合 B 端设计规范」
> → AI 使用 prompts/review.md 人设，对照 rules/checklist.md 逐项检查

## Token 速查表

| 类别 | 文件 | 关键变量 |
|------|------|----------|
| 色彩 | `tokens/colors.json` | `brand.primary` #1677FF, `func.success` #52C41A, `func.error` #FF4D4F |
| 字体 | `tokens/typography.json` | 页面标题 20px/600, 正文 14px/400, 最小 12px |
| 间距 | `tokens/spacing.json` | 基础单位 4px, 页面边距 24px, 卡片间距 16px |
| 圆角阴影 | `tokens/radius-shadow.json` | 按钮 4px, 卡片 8px, 弹窗 16px |

## 定制方式

1. **换品牌色**：修改 `tokens/colors.json` 中 `brand.primary` 的值，衍生色按规则自动调整（hover 亮 15%，active 深 15%）
2. **加业务模板**：在 `references/templates.md` 中按现有格式新增场景
3. **加页面示例**：在 `examples/` 中新建文件夹，放 HTML 和说明

## 核心原则

- **替换 brand.primary 品牌色后全局生效**
- **所有组件引用 Token 变量，不硬编码数值**
- **规范未覆盖的场景，回退到 Ant Design 规范**
