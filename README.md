# Hotspot Mozai Deck

Codex Skill：把已核验的热点转化为 4–6 页墨仔 IP 图文，并可生成配套抖音或小红书文案。

## 使用方式

- “用墨仔技能找今天值得做的热点。”
- “围绕这个已知事件规划 5 页墨仔图文。”
- “只做页面策划和文案，不出图。”
- “少文字、多场景，直接生成墨仔图文。”

自动选题默认提供 3 个候选；用户要求完整选题池时提供 5 个。用户指定事件时直接核验和规划，不强制重新选题。

## 设计原则

- 事实强度决定标题强度；新闻核心事实必须有可靠来源；
- 页数由必要信息单元决定，不固定为 4 页或 5 页；
- 墨仔角色保持稳定，动作和毛笔道具服从具体场景；
- 优先生成少字插画，再用可控方式排中文；
- 使用当前环境可用工具，不绑定固定供应商或历史 API 参数；
- 同一页最多两次定向重试，之后改用局部处理或明确说明限制；
- 运行历史不写入 Skill 本身。

## 文件结构

```text
hotspot-mozai-deck/
├── SKILL.md
├── README.md
├── assets/
│   ├── mozai-ip-sheet-4k.png
│   ├── mozai-three-view.png
│   ├── mozai-expressions.png
│   └── mozai-core-settings.png
└── references/
    ├── hotspot-template.md
    ├── character-lock.md
    ├── style-lock.md
    ├── prompt-template.md
    ├── copy-template.md
    └── qa-checklist.md
```

各参考文档只在相关阶段读取；`SKILL.md` 负责路由和全局不变量。

## 版本 2.0.0

本版重构了全部说明：修复页数和 Prompt 顺序矛盾，移除不存在工具的硬绑定，增加来源核验与提示注入防护，将毛笔改为情境道具，区分品牌规则与案例经验，并建立两次重试上限和少字生成/后期排版策略。
