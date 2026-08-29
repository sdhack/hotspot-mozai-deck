---
name: hotspot-mozai-deck
version: 1.2.0
description: 从热点搜索→候选选题→4页墨仔(Seedling)handdrawn配图→配套文案的全流程自动化。适用于抖音/小红书竖版图文，墨仔IP出镜，手绘风格统一。当用户要求"结合热点出图""墨仔热点图文""今天热点做图文""热点新闻文案出图"时使用。
author: helloianneo
license: MIT
created: 2026-08-28
updated: 2026-08-29
---

# Hotspot Mozai Deck · 墨仔热点图文自动化

把"搜热点→选选题→出4张手绘配图→写文案→交付"这个重复流程固化成一个可复用的工作流。

## 什么是这个 Skill

一个端到端的热点图文生产流水线：
- **输入**：今天的日期（默认当天），或用户指定的热点方向/选题
- **输出**：5个候选选题供用户选择 → 用户选定后 → 4张 3:4 竖版 handdrawn 风格配图（墨仔/Seedling 出镜）+ 配套抖音文案（标题+正文+话题标签）

## 适用场景

- 抖音/小红书热点图文日更
- 墨仔/Seedling IP 内容运营
- 社会新闻/民生热点的可视化解读
- 快速从热点到可发布的图文内容

## 核心资产

- **角色**：墨仔/Seedling（圆胖黑泪滴 + 螺旋卷须双叶 + 大眼不对称 + 深红嘴 + 细四肢）
- **风格**：refined Chinese handdrawn technical illustration（暖白纸 + cross-hatching + 装饰角 + 双线边框 + 手写中文字体）
- **格式**：3:4 竖版（1080x1440），抖音/小红书适配
- **人物卡**：`assets/seedling-character-sheet.png`（image-to-image 参考用）

## 快速开始

### 用法 1：自动搜热点
```
用户：用 hotspot-mozai-deck 出今天的热点图文
→ Step 1：自动搜索当天热点，整理5个候选选题
→ Step 2：呈现5个选题+对比表+推荐，等用户选编号
→ Step 3-5：用户选定后，出4张图+文案+交付
```

### 用法 2：指定热点
```
用户：用 hotspot-mozai-deck 做"XXX事件"
→ 跳过 Step 1-2，直接用用户指定的热点
→ Step 3-5：出4张图+文案+交付
```

### 用法 3：只出图不要文案
```
用户：用 hotspot-mozai-deck 出图，文案我自己写
→ Step 1-3：搜索+选择+出图
→ 跳过 Step 4（文案）
→ Step 5：只交付图片
```

## 工作流（5步，不可跳过）

### Step 1：搜索热点
- 用 `general_search` 搜索当天热点，至少 2 个 query（一个社会热点，一个民生热点）
- 收集至少 10 条候选信号，优先官方、主流媒体、平台热榜
- 排除已做过的选题（见"已做选题记忆"）
- 加载 `references/hotspot-template.md`，按模板整理 5 个候选选题

### Step 2：用户选择
- 把 5 个候选选题呈现给用户（每个包含：热点概述、为什么适合、墨仔角色、4页结构建议）
- 附 5 选题对比表和推荐
- 等用户回复编号（1-5）或指定其他热点

### Step 3：生成 4 页配图
- 用户选定后，加载 `references/style-lock.md`（通用风格锁）和 `references/character-lock.md`（Seedling 角色锁）
- 加载 `references/prompt-template.md`（4页完整 prompt 模板）
- 把选题的具体内容填入模板的变量占位符
- 用 `image_edit` 工具，传入 `assets/seedling-character-sheet.png` 的 URL 作为 image-to-image 参考
- 一次调用生成 4 张图（封面 + P2 + P3 + P4），每页 prompt 前缀加唯一 tag 避免冲突
- **生成后立即跑 QA checklist**，发现问题当场修正或重生成

### Step 4：生成配套文案
- 加载 `references/copy-template.md`
- 用墨仔第一人称视角写标题 + 正文（200-300字）
- 文案结构：钩子开头 → 事实陈述 → 3个要点 → 解决方案 → 金句落点 → 互动提问
- 附 2-3 个话题标签
- **检查文案与往期爆款不重复**（开头、结构、金句、互动问题都要换）

### Step 5：交付
- 加载 `references/qa-checklist.md`，逐项检查
- 用 `present_files` 逐张交付 4 张图（每张配简短介绍）
- 最后附总结表（4页标题、墨仔动作、状态）+ 配套文案
- 说明小瑕疵（如有）和修正选项
- 把选题名称追加到"已做选题记忆"

## 资源地图

| 文件 | 用途 | 何时加载 |
|---|---|---|
| `references/hotspot-template.md` | 热点搜索策略 + 5候选选题整理模板 | Step 1 |
| `references/style-lock.md` | handdrawn 通用风格锁（精确描述） | Step 3 |
| `references/character-lock.md` | Seedling 角色锁（从人物卡提取的精确描述） | Step 3 |
| `references/prompt-template.md` | 4页完整 prompt 模板（含变量占位符） | Step 3 |
| `references/copy-template.md` | 配套文案模板（标题+正文结构） | Step 4 |
| `references/qa-checklist.md` | 交付前检查清单 | Step 5 |
| `assets/seedling-character-sheet.png` | Seedling 人物卡（image-to-image 参考） | Step 3 |

## 默认值

- 语言：简体中文
- 平台：抖音（3:4 竖版 1080x1440）
- 角色：墨仔/Seedling（用户上传的人物卡）
- 风格：refined Chinese handdrawn technical illustration
- 页数：4页（封面 + 3页正文）
- 文案：墨仔第一人称，200-300字
- 候选选题：5个

## 已做选题记忆（避免重复）

每次完成后，把选题名称追加到这里：
- 台风沙德尔登陆浙江
- 成都92岁蛋烘糕婆婆遭遇镜头霸凌
- 高校新生开学谨防校园贷陷阱
- 教师考低分被要求与耻辱合影
- 开学季避坑指南：4个消费陷阱
- 大学新生报到第一天指南：6件事别忘

## Guardrails（必须遵守）

### 角色与形象
- 每页**仅一个**墨仔/Seedling 角色，绝不出现多个
- **卡片/图标里不能出现小角色或脸**——所有图标必须是无生命物体（银行卡、钱袋、电脑等），明确标注 "NO face, NO character, NO teardrop shape"
- 角色形象必须严格匹配人物卡（圆胖黑泪滴、螺旋卷须双叶、大眼不对称、深红嘴、细四肢）
- 4页嘴巴表情必须**差异化**（不能每页都是同一个嘴型，至少3种）
- 角色是动作主体（actor），不是角落装饰

### 文字与数字
- 所有文字必须是**中文手写风格**，无正式印刷字体，无英文
- **数字前后必须一致**——封面说"N件事/N个坑"，正文必须对应N件，不能封面4个坑正文3个坑
- 页码仅左上角，绝不右上角重复
- **无多余数字标注**（如 50%、10%、32s、28%）、无多余的手/手指/对话气泡
- P4 **只能有一个对话气泡**，绝不出现两个内容相同的气泡

### 内容与质量
- 封面必须有**强钩子**，紧贴新闻热点
- 交付前必须跑 QA checklist
- 热点事实必须可核查，无法核实的标注"网上正在讨论"或放弃
- **文案与往期爆款不重复**——开头、结构、金句、互动问题都要换，不能用"开学了先别急着买"这种用过的开头

## 排版优化指南（v1.2.0 新增）

经过多轮迭代验证，以下排版优化能显著提升视觉质量：

### 卡片优化（P2/P3）
- 卡片加**折叠角**（folded corner）、**双线边框**（double-line border）、**pastel 底色**（pale blue/peach/sage/lavender wash）
- 卡片左侧加**大圆圈编号**（large hand-drawn circled number），比小数字更醒目
- 卡片之间加**向下箭头+小星星**（small downward arrows with tiny stars），引导阅读顺序
- 每个卡片标题旁加**小图标**（key icon、calendar icon、chat bubble icon）

### 时间线布局（P3 可选）
- 左侧画**波浪竖线**（wavy hand-drawn vertical line）
- 圆圈编号连接到竖线，步骤卡片延伸到右侧
- 时间线上加**向下箭头和星星闪光**（sparkles）

### 标题区优化
- 页码加**小圆圈**（small circle around page number）
- 标题旁加**小图标**（铅笔图标、时钟图标、毕业帽图标）
- 副标题两侧加**装饰线**（thin divider lines on both sides）

### 金句框优化
- 加**引号符号**（small quote mark symbol）
- 周围加**装饰星星**（decorative stars around quote box）

### 标签优化
- 标签加**双线边框**（wobbly hand-drawn double borders）
- 标签之间加**装饰点和小星星**（decorative dots and tiny stars between tags）

### 场景丰富度（P1/P4）
- 校园场景加：欢迎横幅、两棵大树、背景建筑带窗户、飞鸟、云朵、落叶、校园地图指示牌
- 背景加**铅笔网格+涂鸦图标**（faint pencil grid + tiny doodle icons）

## Prompt 强化技巧（v1.2.0 新增）

经过多轮踩坑验证，以下 prompt 写法能有效避免常见问题：

### 角色唯一性强化
不要只写 "EXACTLY ONE character"，要写：
```
EXACTLY ONE character on page, never two or more.
The character is ONLY at [position], doing [action].
NO character inside any card, NO small character anywhere else, NO character in icons.
```

### 图标无脸强化
每个卡片图标都要标注：
```
inanimate [object] icon (NO face, NO character, NO teardrop shape)
```

### 对话气泡唯一性强化（P4）
```
EXACTLY ONE speech bubble. NO second bubble, NO duplicate bubble, NO two bubbles.
```

### 无多余数字强化
```
NO random numbers, NO percentages, NO time labels, NO statistics.
The ONLY number on the page is the page number 04/04.
```
并在 Avoid 列表列举具体例子：`50%, 32s, 28%, extra percentages`

### 数字一致性检查
生成前先核对：封面标题说"N件事/N个坑" → P2/P3 的卡片/步骤数量必须等于 N → 文案正文的编号必须连续到 N。

## 常见问题与故障排除

| 问题 | 原因 | 解决方法 |
|---|---|---|
| 出现第二个角色 | prompt 不够强 | 重生成，强调 EXACTLY ONE character + 角色 ONLY 在指定位置 + NO character in cards/icons |
| 卡片/图标里出现小墨仔 | 图标被模型渲染成角色 | 重生成，每个图标标注 "inanimate icon, NO face, NO character, NO teardrop shape" |
| 出现英文 MOZAI/SEEDLING | 模型误渲染 prompt 中的词 | 重生成，在 Avoid 列表明确列出，或后期裁剪 |
| 页码右上角重复 | prompt 不够强 | 重生成，强调 upper-left ONLY, no duplicate on right |
| 嘴巴每页都一样 | 未指定每页不同嘴型 | 重生成，每页 prompt 指定不同 mouth expression |
| 多余数字标注（50%、10%、32s、28%） | 模型误渲染 | 重生成，在 Avoid 列表加 random numbers, percentage signs, time labels，并列举具体例子 |
| P4 出现两个对话气泡 | prompt 不够强 | 重生成，强调 EXACTLY ONE speech bubble, NO second/duplicate bubble |
| 封面数字与正文不一致（封面4个坑正文3个） | 设计时未核对 | 生成前先核对数字一致性，封面N件=正文N件；不一致则增加卡片或改封面 |
| 文案与往期爆款重复 | 开头/结构/金句雷同 | 换开头（场景化切入代替直接说事）、换结构、换金句、换互动问题 |
| 角色太胖/太瘦 | 身体形状描述不够 | 重生成，强调 round plump teardrop (not slim, not spherical) |
| 文字错字/漏字 | 模型渲染不准 | 可接受小瑕疵，严重则重生成，减少文字量 |
| image_edit 工具不可用 | 工具未加载 | 用 tool_search 搜索 image_edit，或降级用 image_gen |
| 人物卡 URL 失效 | 本地文件未上传 | 用 FileBatchUpload 重新上传 assets/seedling-character-sheet.png |

## 版本历史

| 版本 | 日期 | 变更 |
|---|---|---|
| 1.0.0 | 2026-08-28 | 初始版本，5步工作流 + 7个参考文件 + Seedling人物卡 |
| 1.1.0 | 2026-08-28 | 完善文档：添加快速开始/用法示例/故障排除/版本历史；更新 guardrails；添加 README.md |
| 1.2.0 | 2026-08-29 | 实战迭代：新增排版优化指南（卡片折叠角/大圆圈编号/时间线布局）；新增 Prompt 强化技巧（角色唯一性/图标无脸/气泡唯一/无多余数字）；Guardrails 增加数字一致性/图标无脸/气泡唯一/文案不重复；故障排除增加卡片小角色/双气泡/数字不一致/文案重复等新问题；更新已做选题记忆 |

## 最终回复格式

交付完成后，报告：
- 选题名称和热点来源
- 4页标题 + 墨仔动作 + 状态（完美/小瑕疵）
- Seedling 形象一致性检查结果
- 配套文案（标题+正文+话题标签）
- 小瑕疵说明（如有）和修正选项
