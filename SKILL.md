---
name: hotspot-mozai-deck
version: 1.8.0
description: 从热点搜索→候选选题→4-6页墨仔(Mozai)handdrawn配图→配套文案的全流程自动化。v1.8.0 核心变更：①场景叙事型排版（用户要求"少文字多配图"时，每页以一个场景画为主、文字仅标题+短标签≤4字+金句）；②原始画风不可变（任何改动标题/画面/布局都不得弱化style-lock原始画风：双线边框/四角装饰/波浪下划线/pastel标签/铅笔网格涂鸦/墨仔形象一致）；③封面强钩子（第一张图钩子与画面必须吸引人，悬念+反差型"一条自我介绍/让家长群安静了"优于直白陈述型"家长群晒身份？求老师多关照"）；④文案master-copywriting合规检查（G1-G12事实层/抖音生活故事体/去AI味H2/画面感与配图呼应）。v1.7.2 核心变更：颜色代码防护（prompt中禁止出现#XXXXXX十六进制颜色代码，会被渲染成画面乱码，改用文字描述如warm off-white/ink-black/pale blue，并在AVOID中明确禁止hex color codes）。v1.7.1 核心变更：表情动作与内容关联原则。v1.7.0 变更：涂鸦是墨仔的天性+去说教原则+image_edit request_list格式。当用户要求"结合热点出图""墨仔热点图文"时使用。
author: helloianneo
license: MIT
created: 2026-08-28
updated: 2026-09-03
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

- **角色**：墨仔/Mozai（圆胖黑泪滴 + 小芽微卷茎双叶 + 大眼不对称 + 黑色小嘴 + 细四肢，手绘墨迹质感）
- **风格**：refined Chinese handdrawn technical illustration（暖白纸 + cross-hatching + 装饰角 + 双线边框 + 手写中文字体）
- **涂鸦天性（v1.7.0核心）**：墨仔是"一滴在纸上活过来的墨"，它走到哪里，哪里就有涂鸦。每页背景必须有铅笔网格+散布涂鸦图标+交叉排线+墨点，禁止大面积纯白空白
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
- 把 5 个候选选题呈现给用户（每个包含：热点概述、为什么适合、建议页数+理由、墨仔角色、N页结构建议）
- **v1.5.1 新增：必须先决定页数再出结构**——根据每个选题的内容长度和信息量决定建议页数（4页/5页/6页），禁止默认全部5页，页数决定逻辑见 `references/hotspot-template.md` Step 3
- 附 5 选题对比表和推荐
- 等用户回复编号（1-5）或指定其他热点

### Step 3：生成 4-6 页配图
- **v1.6.0 新增：Prompt as Code 结构化协议**——每页 prompt 必须按 7 字段块顺序组织：CANVAS / STYLE / LAYOUT / CONTENT / CHARACTER / CONSTRAINTS / AVOID，大写字段标记不可省略。借鉴 awesome-gpt-image-2 的 544 案例逆向工程方法论，结构化比散文可控性高 3-5 倍。详见 `references/prompt-template.md` 第一节
- **v1.6.0 新增：内容主导型排版（默认）**——分析页/金句页必须使用内容主导型：内容区（卡片/图标/文字）占页面 55-65%，墨仔仅占 8-10% 且位置在角落（左下/右下轮换），墨仔周围完全空白。仅封面/互动页可使用角色主导型（墨仔 18-25%）。详见 `references/prompt-template.md` 第三节和 `references/character-lock.md` 灵活尺寸协议
- **v1.6.0 新增：角色一致性前置**——CHARACTER 字段必须放在 CONTENT 字段之前，且包含完整角色锁（不可简写），避免模型生成内容时"忘记"角色设定导致外观漂移。生成后必须核对 8 个身份锚点（身体形状/颜色/质感/头顶芽/叶子/眼睛/嘴巴/四肢）。详见 `references/character-lock.md` v1.6.0 新增章节
- **v1.6.0 新增：五官拆解**——眼睛/嘴巴/头顶芽/身体质感必须拆解到可执行粒度（如眼睛=大圆眼+大白眼白占60-70%+黑瞳孔占30-40%+常不对称），不能只写"大眼睛小嘴巴"。详见 `references/character-lock.md` 五官拆解章节
- **v1.6.0 新增：材质光影强化**——纸张/墨水/光影/pastel底色必须精细描述（如墨水=可变线宽+交叉排线+点画+自然晕染），避免画面扁平无层次。详见 `references/style-lock.md` v1.6.0 新增章节
- **v1.6.0 新增：文案克制原则**——每页文字量上限：封面标题≤12字/行，卡片说明≤20字，金句≤10字/行。超过上限会导致模型渲染错字漏字。详见 `references/prompt-template.md` 第七节
- **v1.7.0 新增：涂鸦是墨仔的天性**——每页背景必须有 FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS（无生命物体：星星/叶子/铅笔/箭头/圆点/闪光/音符）+ cross-hatching patches + ink dots，全页覆盖，**禁止大面积纯白空白**。涂鸦是墨仔IP的核心视觉特质，不是可选排版优化。详见 `references/style-lock.md` v1.7.0 核心变更和 `references/character-lock.md` 涂鸦天性设定
- **v1.7.0 新增：去说教原则（配图）**——标题和卡片措辞用分享式（"我自己的3个小习惯""3个我踩过的"），非命令式（"3个防坑做法，新生必看""只认官方群和通知"）。墨仔是观察者和分享者，不是教导者。详见 `references/copy-template.md` v1.7.0 去说教措辞对照表
- **v1.7.0 新增：image_edit 必须用 request_list 数组格式**——实战验证：扁平参数调用会报错 `required param is empty, field: request_list`。必须用 `image_edit(model_version=..., request_list=[{"prompt":..., "image_reference_url_list":[...], "height":..., "width":...}, ...])` 格式。可一次传入多个请求（如5页同时生成）。详见 `references/character-lock.md` image_edit 工具调用格式
- **v1.7.1 新增：表情动作与内容关联原则**——墨仔的表情和动作必须根据图文内容来定，不能毫无关联。差异化不是目的，内容关联才是目的。封面=惊讶/好奇+拿放大镜/举手；分析问题页=思考/困惑+托腮/拿本子记录；分析方案页=坚定/认真+叉腰/举盾牌/指方向；金句页=沉思/温暖+托腮/手放胸口/盘腿沉思；互动页=好奇/邀请+挥手/拿喇叭/举手提问。生成5页差异化状态表时必须同时填写"内容关联理由"列。详见 `references/character-lock.md` 表情动作与内容关联原则和 `references/prompt-template.md` 5页差异化状态规划模板（v1.7.1增强版）
- **v1.7.2 新增：颜色代码防护**——prompt中**禁止出现任何十六进制颜色代码**（如 #FBFAF5、#1B1B1B、#A8C879、#FBAF5），seedream模型会把它们渲染成画面文字乱码（如"183:5@FBAF5""#1B-COB"出现在角落）。必须改用文字描述：warm off-white paper、ink-black body、light sage-green leaves、pale blue/peach/sage/lavender wash。同时在 AVOID 中明确列出 `hex color codes, pound sign codes, # followed by letters/numbers, color code text in margins`。详见 `references/style-lock.md` v1.7.2 颜色代码防护和 `references/prompt-template.md` 颜色代码防护章节
- **v1.8.0 新增：场景叙事型排版模式（可选，用户要求"少文字多配图"时启用）**——当用户反馈"不能老画文字、也得配图"或要求画面感更强时，从"内容主导型/角色主导型"切换为**场景叙事型**：每页以一个场景画为主（墨仔融入真实场景做主题动作，如举手机看群/指黑板/举"一视同仁"牌/站天平横梁/挥手+喇叭），文字仅保留标题+短标签（≤4字）+金句，其余内容全部用画面表达。场景、动作、表情必须与页面内容强关联。详见 `references/prompt-template.md` 十、场景叙事型排版协议（v1.8.0）
- **v1.8.0 新增：原始画风不可变**——无论怎么改标题、画面、布局（如封面强钩子改造），style-lock 定义的原始画风必须完整保留，**逐项核对不可省略**：细双线边框+四角装饰花纹+标题波浪下划线+封面顶部2个/底部3-4个 pastel 标签+铅笔网格涂鸦背景（无大面积空白）+墨仔形象一致。实战教训：封面改强钩子时最容易弱化这些画风元素导致"画风变了"。详见 `references/style-lock.md` 原始画风不可变（v1.8.0）
- **v1.5.0 新增：生成前先规划5页差异化状态表**——确保每页墨仔的眼睛状态、嘴型、身体动作全部不同（见 prompt-template.md 的"5页差异化状态规划模板"），**且v1.7.1强化：表情动作必须与页面内容强关联**
- **v1.5.0 新增：模型版本选择**——初稿/迭代用 seedream_4.5（1080×1440，速度快），最终交付用 seedream_5.0_pro（1773×2364，画质优）
- 用户选定后，加载 `references/style-lock.md`（通用风格锁）和 `references/character-lock.md`（Seedling 角色锁）
- 加载 `references/prompt-template.md`（4页完整 prompt 模板）
- 把选题的具体内容填入模板的变量占位符
- 用 `image_edit` 工具（**v1.7.0：必须用 request_list 数组格式**），传入 `assets/seedling-character-sheet.png` 的 URL 作为 image-to-image 参考
- **v1.5.1 强化：按Step 2决定的页数生成对应数量的图**（4页就生成4张，5页就生成5张，6页就生成6张），不默认5页；每页 prompt 前缀加唯一 tag 避免冲突
- **v1.5.0 强化：prompt 必加防坑约束**——卡片内容防重复（Card 3 DIFFERENT from 1 and 2）、标签防重复（Each tag ONLY ONCE）、随机数字防护（ONLY number is page number）、墨仔周围空白防护（Area around character COMPLETELY BLANK）、逻辑标题规范（金句页不用"写在最后"）
- **生成后必须逐张下载到本地，用 Read 工具放大（thumbnail_size=large）逐张校验**，不能只看生成结果缩略图
- **校验发现问题后，单独重生成有问题的页面**（不要全部重生成），重生成时在 prompt 中明确列出之前出现的具体错误
- **生成后立即跑 QA checklist**（含 v1.7.0 新增的 J11-J15：涂鸦天性/去说教配图/去说教文案/image_edit格式/背景涂鸦无角色），发现问题当场修正或重生成

### Step 4：生成配套文案
- 加载 `references/copy-template.md`
- 用墨仔第一人称视角写标题 + 正文（200-300字）
- 文案结构：钩子开头 → 事实陈述 → 3个要点 → 解决方案 → 金句落点 → 互动提问
- 附 2-3 个话题标签
- **检查文案与往期爆款不重复**（开头、结构、金句、互动问题都要换）
- **v1.7.0 新增：去说教原则（文案）**——文案口吻是分享者（"我自己的办法是""我踩过的"），非教导者（"你必须""你应该""你千万不要"）；互动提问是平等分享式（"你呢？""你遇到过吗？"），非教导式（"你学会了吗？""你记住了吗？"）；优先用故事/经历切入开头（模板D），让墨仔以"我也踩过坑"的分享者身份出现。详见 `references/copy-template.md` v1.7.0 去说教原则和措辞对照表
- **v1.8.0 新增：master-copywriting 文案合规检查**——发布级文案对照 master-copywriting 标准核查后再交付：①G1-G5 事实层（热点事实可核查、数字跨文案/配图一致、无虚构第一人称经历）；②G6 目的（IP 内容=观点+共鸣+互动完整）；③G7 抖音原生（生活故事体"起点→变化→冲突→选择→结果→落点"，写"正在发生"的场景、具体动作，避免纯评论体）；④G8 去AI味（H2 打散"第一/第二/第三"模板化排比，改口语化自然过渡）；⑤画面感（每格至少 2 个可视觉化元素，与配图场景一一呼应）。详见 `references/copy-template.md` master-copywriting 合规检查（v1.8.0）

### Step 5：交付
- 加载 `references/qa-checklist.md`，逐项检查（含 v1.7.0 新增 J11-J15）
- 用 `present_files` 逐张交付 4 张图（每张配简短介绍）
- 最后附总结表（4页标题、墨仔动作、状态）+ 配套文案
- 说明小瑕疵（如有）和修正选项
- 把选题名称追加到"已做选题记忆"

## 资源地图

| 文件 | 用途 | 何时加载 |
|---|---|---|
| `references/hotspot-template.md` | 热点搜索策略 + 5候选选题整理模板 | Step 1 |
| `references/style-lock.md` | handdrawn 通用风格锁（精确描述，v1.7.0含涂鸦天性） | Step 3 |
| `references/character-lock.md` | Seedling 角色锁（从人物卡提取的精确描述，v1.7.0含涂鸦天性设定+image_edit格式） | Step 3 |
| `references/prompt-template.md` | 4页完整 prompt 模板（含变量占位符） | Step 3 |
| `references/copy-template.md` | 配套文案模板（标题+正文结构，v1.7.0含去说教原则） | Step 4 |
| `references/qa-checklist.md` | 交付前检查清单（v1.7.0含J11-J15） | Step 5 |
| `assets/seedling-character-sheet.png` | Seedling 人物卡（image-to-image 参考） | Step 3 |

## 默认值

- 语言：简体中文
- 平台：抖音（3:4 竖版 1080x1440）
- 角色：墨仔/Seedling（用户上传的人物卡）
- 风格：refined Chinese handdrawn technical illustration
- **涂鸦背景（v1.7.0默认开启）**：每页背景必须有铅笔网格+散布涂鸦+交叉排线+墨点，禁止大面积纯白空白
- **去说教（v1.7.0默认开启）**：文案+配图用分享式而非命令式
- 页数：4-6页（**v1.5.1 强化：根据内容长度和信息量决定，禁止默认5页**——4页=单一事件/观点集中/情感驱动；5页=双事件/争议性强/多维度；6页=内容特别丰富/多案例数据；详见 `references/hotspot-template.md` Step 3）
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
- 求职诈骗防骗指南：106人被骗1000万
- 开学季·课后延时服务报名率跟风焦虑（2026-09-01，5页版，墨仔第一人称）
- 开学季·严禁重点班分班（2026-09-01，5页版，墨仔第一人称）
- 中学收220元门禁费引争议（2026-09-01，4页版，墨仔第一人称）
- 开学消费避坑6大陷阱（2026-09-01，5页版，墨仔第一人称）
- 开学安全第一课·校园安全6大提醒（2026-09-01，5页版，墨仔第一人称，内容主导型排版）
- 新生群里的套路·90%的人踩过（2026-09-01，5页版，墨仔第一人称，v1.7.0涂鸦天性+去说教）
- 班级群假班主任诈骗·33人被骗9108元（2026-09-02，4页版，墨仔第一人称，seedream_5.0_pro高清版，v1.7.1表情动作与内容关联）
- 家长群自报"纪委书记"身份求关照（2026-09-03，5页版，墨仔第一人称，seedream_5.0_pro高清版，v1.7.2颜色代码防护，封面P1/金句P4/互动P5经过重生成修复）
- 家长群自报"纪委书记"身份求关照·场景版（2026-09-03，5页重做，从"文字卡片型"改为"场景叙事型"：P1举手机看群/P2指黑板/P3举"一视同仁"牌/P4站天平横梁/P5挥手+喇叭，每页文字仅标题+短标签+金句，配图为主；文案按master-copywriting G7/G8改写为生活故事体）
- 家长群晒身份·封面强钩子版（2026-09-03，P1封面标题改"一条自我介绍/让家长群安静了"，手机消息"我是单位纪委书记"高亮+周围气泡灰化制造"安静"冲突；v3按style-lock完整恢复原始画风：双线边框+四角装饰+波浪下划线+顶部底部pastel标签+铅笔网格涂鸦）

## Guardrails（必须遵守）

### 角色与形象
- 每页**仅一个**墨仔/Seedling 角色，绝不出现多个
- **严格2手2脚**（v1.5.0 用户硬约束）：恰好2条手臂+2条腿，多手多脚绝对不能出现
- **每页表情/眼睛/嘴型/动作必须大幅差异化**（v1.5.0 用户硬约束）：4-6页中眼睛状态、嘴型、身体动作必须每页不同
- **张嘴时嘴必须拟人化**（v1.5.0 用户硬约束）：张嘴时嘴内部必须可见舌头/口腔层次，不能是全黑洞
- **嘴不能太大，表情不能太夸张**（v1.5.0 用户硬约束）：所有嘴型都是小比例（SMALL），表情克制
- **墨仔外观一致性**（v1.5.0 用户硬约束）：每页泪滴形身体、大眼、小嘴、小芽双叶、手绘墨迹质感完全一致
- **无红晕**（v1.5.0 用户硬约束）：脸部无粉色红晕/腮红，是干净黑色墨迹
- **卡片/图标里不能出现小角色或脸**——所有图标必须是无生命物体（银行卡、钱袋、电脑等），明确标注 "NO face, NO character, NO teardrop shape"
- 角色形象必须严格匹配人物卡（圆胖黑泪滴、小芽微卷茎双叶、大眼不对称、黑色小嘴、细四肢、手绘墨迹质感）
- 4页嘴巴表情必须**差异化**（不能每页都是同一个嘴型，至少3种）
- 角色是动作主体（actor），不是角落装饰——即使小比例在角落，也必须在做与页面主题相关的动作
- **内容主导型排版（v1.6.0 用户硬约束）**：分析页/金句页默认内容为主，墨仔为辅。内容区（卡片/图标/文字）占页面 55-65%，墨仔仅占 8-10% 且位置在角落（左下/右下轮换，不连续同侧），墨仔周围完全空白（无文字/图标/涂鸦）。仅封面/互动页可使用角色主导型（墨仔 18-25%）
- **涂鸦天性（v1.7.0 核心约束）**：每页背景必须有 FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS（无生命物体）+ cross-hatching patches + ink dots，全页覆盖，**禁止大面积纯白空白**。背景涂鸦必须是无生命物体（星星/叶子/铅笔/箭头/圆点/闪光/音符），无角色/脸/泪滴形
- **表情动作与内容关联（v1.7.1 核心约束）**：墨仔的表情和动作必须根据图文内容来定，不能毫无关联。封面=惊讶/好奇+拿放大镜/举手；分析问题页=思考/困惑+托腮/拿本子记录；分析方案页=坚定/认真+叉腰/举盾牌/指方向；金句页=沉思/温暖+托腮/手放胸口/盘腿沉思；互动页=好奇/邀请+挥手/拿喇叭/举手提问。不能为了"每页不同"而随便选表情/动作
- **颜色代码防护（v1.7.2 核心约束）**：prompt中禁止出现任何十六进制颜色代码（#FBFAF5、#1B1B1B、#A8C879等），模型会渲染成画面文字乱码。必须用文字描述颜色（warm off-white、ink-black、light sage-green、pale blue等），并在AVOID中明确禁止hex color codes和pound sign codes

### 文字与数字
- 所有文字必须是**中文手写风格**，无正式印刷字体，无英文
- **数字前后必须一致**——封面说"N件事/N个坑"，正文必须对应N件，不能封面4个坑正文3个坑
- 页码仅左上角，绝不右上角重复
- **无多余数字标注**（如 50%、10%、32s、28%、40%）、无多余的手/手指/对话气泡
- **标签不重复**（v1.5.0 新增）：每个标签只出现一次，无同一标签重复出现
- **逻辑标题规范**（v1.5.0 新增）：金句页标题不能用"写在最后"等暗示最后一页的词，推荐"墨仔想说"；标题不能与金句内容重复
- P4 **只能有一个对话气泡**，绝不出现两个内容相同的气泡

### 内容与质量
- 封面必须有**强钩子**，紧贴新闻热点
- **页数必须与内容长度和信息量匹配**（v1.5.1 新增）：禁止内容很少的选题硬凑5页，也禁止内容丰富的选题压缩到4页；页数决定逻辑见 `references/hotspot-template.md` Step 3
- 交付前必须跑 QA checklist
- 热点事实必须可核查，无法核实的标注"网上正在讨论"或放弃
- **文案与往期爆款不重复**——开头、结构、金句、互动问题都要换，不能用"开学了先别急着买"这种用过的开头
- **去说教原则（v1.7.0 新增）**：文案+配图用分享式（"我自己的办法是""我踩过的"），非命令式（"你必须""你应该""新生必看"）；墨仔是观察者和分享者，不是教导者
- **场景叙事型排版（v1.8.0 核心约束）**：用户要求"少文字多配图"/"画面感更强"时，每页以一个场景画为主，墨仔融入真实场景做主题动作，文字仅保留标题+短标签（≤4字）+金句，其余全部用画面表达。严禁把大段文字卡片堆回画面
- **原始画风不可变（v1.8.0 核心约束）**：任何改动（标题/画面/布局/强钩子改造）都不得弱化 style-lock 原始画风——细双线边框、四角装饰花纹、标题波浪下划线、封面顶部/底部 pastel 标签、铅笔网格涂鸦背景（无大面积空白）、墨仔形象一致。改钩子时逐项核对，缺一项即重生成
- **封面强钩子（v1.8.0 核心约束）**：第一张图（封面）的文案钩子和画面必须吸引人。钩子类型：悬念+反差型（"一条自我介绍/让家长群安静了"——什么自我介绍？为什么安静？）优于直白陈述型（"家长群晒身份？求老师多关照"）；画面用关键信息高亮+周围淡化制造冲突氛围（如手机里"我是单位纪委书记"高亮、其余气泡灰化）
- **master-copywriting 合规（v1.8.0 新增）**：发布级文案对照 master-copywriting 核查——事实可核查、数字一致、无虚构经历（G1-G5）、目的完整（G6）、抖音生活故事体（G7）、去AI味（G8）

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

### 背景涂鸦（v1.7.0 从可选提升为核心）

> **涂鸦是墨仔的天性**——墨仔是"一滴在纸上活过来的墨"，它走到哪里，哪里就有涂鸦。每页背景必须有手绘涂鸦质感，禁止大面积纯白空白。

- **FAINT PENCIL GRID**（淡铅笔网格，全页覆盖，20-30%透明度，不突兀）
- **SCATTERED TINY DOODLE ICONS**（散布的小涂鸦图标，必须是无生命物体：星星、叶子、铅笔、箭头、圆点、闪光、音符，不能有角色/脸）
- **cross-hatching patches**（交叉排色块，在背景空白区域增加纹理层次）
- **ink dots and splatters**（墨点和墨溅，增加手绘质感）
- **tiny stars and sparkles**（小星星和闪光）

> ⚠️ 涂鸦背景必须是**淡的、不抢主体的**——网格20-30%透明度，涂鸦图标小而分散，交叉排线稀疏。目的是消除大面积纯白空白，增加手绘质感，而不是让背景变得拥挤杂乱。

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

### 卡片/步骤数量精确控制（v1.3.0 新增，实战验证）
不要只写 "five cards"，要写：
```
EXACTLY FIVE cards stacked vertically. NO sixth card. NO extra card. NO more, NO less.
Five cards only, numbered 1 through 5 in large hand-drawn circles on left side of each card.
```
> 实战验证：P2 原生成6张、P3 原生成7张，加此约束后修复为5张。

### 编号连续性控制（v1.3.0 新增，实战验证）
```
numbered 1 through N consecutively. NO duplicate numbers. NO 50%. NO 20h. NO random digits in circles.
Each circle contains ONLY the sequential number 1, 2, 3, 4, 5.
```
> 实战验证：P3 原编号混乱（50%/2/3/3/5/5），加此约束后修复为1-5连续。

### 常见错字预防（v1.3.0 新增，实战验证）
对于易错形近字，在 prompt 中用拼音+偏旁拆解明确区分：
```
TEXT MUST BE 拨打110 (拨 = 扌+发, pronounced bo). NOT 技打 (技 = 扌+支, pronounced ji).
Also 派出所 (only one 派), 冻结 (only one 冻).
```
常见易错字清单：
- 拨打 ≠ 技打
- 派出所 ≠ 派派出所
- 冻结 ≠ 冻冻结
- 保留 ≠ 保保留
> 实战验证：P4 反复生成"技打110"，加拼音+偏旁拆解后修复为"拨打110"。

### 页码唯一性控制（v1.3.0 新增，实战验证）
```
page number appears ONLY ONCE at upper-left inside a small circle.
NO second page number. NO 04/05 near title. NO duplicate number anywhere.
```
> 实战验证：P4 原标题旁重复页码，加此约束后修复为仅左上角一个。

### 符号控制（v1.3.0 新增，实战验证）
```
NO $ sign. NO dollar sign. NO currency symbols. NO % sign in icons.
Money bag icon is plain cloth sack with tie, NO symbol on it.
Shield icon is plain shield, NO $ or other symbol inside.
```
> 实战验证：P1/P2 钱袋和盾牌反复出现$符号，加此约束后修复。

### 图标内无文字/数字（v1.3.0 新增，实战验证）
```
All icons contain NO text, NO numbers, NO letters, NO K306, NO (136).
Icons are pure illustrations only.
ID card icon has chip but NO text/numbers on it.
```
> 实战验证：P2 身份证出现K306、卡片角出现(136)，加此约束后修复。

### 涂鸦背景强化（v1.7.0 新增，实战验证）
```
FAINT PENCIL GRID PATTERN across entire background (20-30% opacity).
SCATTERED TINY DOODLE ICONS everywhere (stars, leaves, pencils, arrows, dots, sparkles — all inanimate, NO faces, NO characters).
Cross-hatching patches, stippling, subtle ink bleed in background areas.
NO large empty white spaces. NO flat plain background.
```
> 实战验证：v1.6.0生成的图背景大面积纯白空白，观感差；加此约束后v1.7.0生成的图手绘质感明显增强。

### 去说教标题/卡片（v1.7.0 新增）
```
Title uses first-person sharing tone: "我自己的3个小习惯" (NOT "3个防坑做法，新生必看").
Card text uses sharing tone: "收费先去官网确认" (NOT "只认官方群和通知").
NO command words: "必须", "应该", "千万不要", "必看", "必读".
```

### 颜色代码防护（v1.7.2 新增，实战验证）

> ⚠️ **seedream模型会把prompt中的十六进制颜色代码渲染成画面文字乱码**——如 `#FBFAF5` 会变成角落的"183:5@FBAF5"，`#1B1B1B` 会变成"#1B-COB"，`#A8C879` 会变成乱码符号。这是经过多轮实战验证的严重问题。

```
NEVER use hex color codes in prompt. NO #FBFAF5, NO #1B1B1B, NO #A8C879, NO #FBAF5, NO any # followed by letters/numbers.
Use text descriptions instead: warm off-white paper, ink-black body, light sage-green leaves, pale blue/peach/sage/lavender wash.
In AVOID list: hex color codes, pound sign codes, # followed by letters/numbers, color code text in corners/margins.
```

> 实战验证：v1.7.1及之前版本的prompt中大量使用 `#FBFAF5`、`#1B1B1B`、`#A8C879`，导致生成图角落出现"183:5@FBAF5""#1B-COB""#15-2065"等乱码。v1.7.2全部改为文字描述后，乱码问题完全消除。

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
| 文字错字/漏字 | 模型渲染不准 | 可接受小瑕疵，严重则重生成，减少文字量；常见错字在prompt中用拼音+偏旁拆解预防 |
| 卡片/步骤数量错误（多了/少了） | prompt数量约束不够强 | 重生成，强调 EXACTLY N cards + NO sixth/extra card + NO more NO less |
| 编号混乱/重复 | 未约束编号格式 | 重生成，强调 numbered 1 through N consecutively + NO duplicates + NO 50%/20h/random digits |
| 常见错字（拨打→技打等） | 模型混淆形近字 | 重生成，prompt中用拼音+偏旁拆解明确区分（拨=扌+发 bo，技=扌+支 ji）；见"常见错字清单" |
| 页码重复（标题旁又出现） | 页码约束不够强 | 重生成，强调 ONLY ONCE upper-left + NO second page number + NO near title |
| 图标内出现文字/数字 | 图标未约束为纯图形 | 重生成，强调 icons contain NO text/numbers/letters + 列举具体例子 K306/(136) |
| $符号反复出现（钱袋/盾牌） | 图标默认带货币符号 | 重生成，强调 NO $ sign + money bag is plain cloth sack with NO symbol + shield NO symbol |
| image_edit 工具不可用 | 工具未加载 | 用 tool_search 搜索 image_edit，或降级用 image_gen |
| 人物卡 URL 失效 | 本地文件未上传 | 用 FileBatchUpload 重新上传 assets/seedling-character-sheet.png |
| 多手多脚（v1.5.0） | 模型误渲染多余肢体 | 重生成，强调 EXACTLY TWO arms/legs + NO extra limbs + NO third arm/leg |
| 张嘴全黑洞（v1.5.0） | 未强调嘴部拟人化 | 重生成，强调 SMALL open oval + visible PINK/RED TONGUE + NOT all-black |
| 嘴太大表情夸张（v1.5.0） | 未强调小比例嘴型 | 重生成，强调 SMALL mouth + NOT wide + NOT large + restrained expression |
| 每页表情单一重复（v1.5.0） | 未指定每页差异化 | 生成前规划5页差异化状态表，每页指定不同眼睛+嘴型+动作 |
| 脸部红晕腮红（v1.5.0） | 模型误渲染粉色脸颊 | 重生成，强调 NO blush + NO pink cheeks + face is clean black ink |
| 卡片内容重复（v1.5.0） | 模型生成重复卡片 | 重生成，强调 Card 3 is DIFFERENT from 1 and 2 + NO duplicate content |
| 标签重复出现（v1.5.0） | 模型重复渲染标签 | 重生成，强调 Each tag ONLY ONCE + NO duplicate tags |
| 金句页标题逻辑矛盾（v1.5.0） | 用"写在最后"但后面还有页 | 改为"墨仔想说"等不暗示最后一页的标题；标题不与金句重复 |
| 随机数字40%/10%（v1.5.0） | 模型角落生成随机数字 | 重生成，强调 ONLY number is page number + NO random numbers + NO 40%/10% |
| 墨仔附近英文Mozai（v1.5.0） | 模型误渲染角色名 | 重生成，强调 Area around character COMPLETELY BLANK + no text/letters/"Mozai" |
| 墨仔外观不一致（v1.5.0） | 角色锁不够强或人物卡URL过期 | 重新上传人物卡，重生成，强化完整角色锁描述 |
| **背景大面积纯白空白（v1.7.0）** | **未强调涂鸦背景** | **重生成，强调 FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching patches + ink dots, NO large empty white spaces, NO flat plain background** |
| **背景涂鸦有角色/脸（v1.7.0）** | **涂鸦未限制为无生命物体** | **重生成，强调 doodles are inanimate objects only (stars, leaves, pencils, arrows, dots), NO character doodles, NO faces in doodles** |
| **标题/卡片说教式（v1.7.0）** | **措辞用了命令式** | **改标题/卡片为分享式（"我自己的3个小习惯"而非"3个防坑做法，新生必看"）** |
| **文案教导式（v1.7.0）** | **用了"你必须""你应该"** | **改文案为第一人称分享（"我自己的办法是""我踩过的"）** |
| **image_edit报错required param is empty（v1.7.0）** | **用了扁平参数** | **改用request_list数组格式调用：image_edit(model_version=..., request_list=[{"prompt":..., "image_reference_url_list":[...], "height":..., "width":...}])** |
| **颜色代码乱码（v1.7.2）** | **prompt中出现#XXXXXX十六进制颜色代码，被模型渲染成画面文字** | **重生成，prompt中移除所有十六进制颜色代码，改用文字描述（warm off-white/ink-black/light sage-green/pale blue等），AVOID中加hex color codes, pound sign codes** |
| **副标题重复渲染（v1.7.2）** | **副标题被模型渲染成两行相同文字** | **重生成，CONSTRAINTS中加"Subtitle appears ONLY ONCE. NO duplicate subtitle."** |
| **装饰线上出现随机数字（v1.7.2）** | **副标题下方装饰线被模型加上数字** | **重生成，CONSTRAINTS中加"Divider line is plain, NO numbers on it."** |
| **墨仔动作未执行（如叉腰变成垂手）（v1.7.2）** | **动作描述不够强，模型忽略** | **重生成，CONSTRAINTS中加"BOTH HANDS CLEARLY ON HIPS. NO arms hanging down."，AVOID中加"arms hanging down"** |
| **场景叙事型画面文字仍偏多（v1.8.0）** | **用了内容主导型文字卡片习惯，未切换到场景叙事型** | **重生成，每页文字仅限标题+短标签≤4字+金句，其余内容用场景画表达（黑板上画图标、手机屏幕只留1条高亮消息、其余气泡灰化无文字）** |
| **封面强钩子改造后画风弱化（v1.8.0）** | **改标题/画面时丢了style-lock封面元素（边框/装饰角/波浪下划线/标签/涂鸦）** | **重生成，完整恢复原始画风：THIN DOUBLE-LINE BORDER + DECORATIVE CORNER FLOURISHES + WAVY UNDERLINE + 顶部#标签 + 底部#标签 + FAINT PENCIL GRID涂鸦，逐项核对** |
| **封面钩子平淡不抓人（v1.8.0）** | **标题用直白陈述，缺悬念/反差** | **改标题为悬念+反差型（"一条自我介绍/让家长群安静了"优于"家长群晒身份？求老师多关照"）；画面让关键消息高亮、周围淡化制造冲突** |
| **文案偏评论体、画面感弱（v1.8.0）** | **未按master-copywriting抖音原生要求写** | **改写为生活故事体（起点→变化→冲突→选择→结果→落点），加"正在发生"的场景和具体动作，每格至少2个可视觉化元素，去"第一/第二/第三"模板排比** |

## 版本历史

| 版本 | 日期 | 变更 |
|---|---|---|
| 1.0.0 | 2026-08-28 | 初始版本，5步工作流 + 7个参考文件 + Seedling人物卡 |
| 1.1.0 | 2026-08-28 | 完善文档：添加快速开始/用法示例/故障排除/版本历史；更新 guardrails；添加 README.md |
| 1.2.0 | 2026-08-29 | 实战迭代：新增排版优化指南（卡片折叠角/大圆圈编号/时间线布局）；新增 Prompt 强化技巧（角色唯一性/图标无脸/气泡唯一/无多余数字）；Guardrails 增加数字一致性/图标无脸/气泡唯一/文案不重复；故障排除增加卡片小角色/双气泡/数字不一致/文案重复等新问题；更新已做选题记忆 |
| 1.3.0 | 2026-08-29 | 实战深度迭代：页数从固定4页改为4-6页灵活调整（根据内容丰富度）；新增6条Prompt强化技巧（卡片数量精确控制/编号连续性/常见错字预防用拼音+偏旁拆解/页码唯一性/符号控制$/图标内无文字数字）；故障排除新增6条（卡片数量错误/编号混乱/常见错字/页码重复/图标内文字/$符号）；工作流Step3新增"生成后必须逐张下载放大校验+单独重生成有问题页面"；更新已做选题记忆 |
| 1.4.0 | 2026-08-31 | 墨仔人物卡大更新：替换为新版墨仔IP完整设定图（含三视图/表情延展/动作延展/校园场景/色彩设定/表情包）；角色锁全面重写，关键变更：嘴巴颜色从深红改为黑色线条、头顶芽从螺旋卷须改为小芽微卷茎、身体质感强调手绘墨迹感自然晕染、新增墨仔IP设定信息（生日/星座/性格/口头禅/故事背景）、表情库从7种扩展为8种（新增调皮wink/思考thinking）、故障排除新增"嘴巴变红""头顶变螺旋卷须""身体变纯平黑"修复方法 |
| 1.5.0 | 2026-09-01 | 基于课后延时服务选题10+轮迭代实战深度优化：character-lock.md新增「用户硬约束」6条（严格2手2脚/每页差异化/张嘴拟人化含粉舌/嘴不大表情不夸张/外观一致性/无红晕）+「嘴型拟人化规范」+表情库规则强化（每页嘴型/眼睛/动作全部不同）+故障排除新增7条；prompt-template.md新增「实战防坑强化模板」6条（卡片内容防重复/标签防重复/随机数字防护/逻辑标题规范/墨仔周围空白防护/5页差异化状态规划模板）+「模型版本建议」（seedream_5.0_pro推荐）；qa-checklist.md更新A8-A15（嘴巴拟人化/手臂腿强化/无红晕/外观一致性）+新增J1-J5实战检查项（卡片不重复/标签不重复/逻辑标题/5页差异化/随机数字防护）；SKILL.md Guardrails新增用户硬约束6条+标签不重复+逻辑标题规范；Step3新增5页差异化规划+模型版本选择+防坑约束；已做选题记忆追加"课后延时服务报名率跟风焦虑" |
| 1.5.1 | 2026-09-01 | 页数决定逻辑优化：基于实战反馈"根据内容长度和信息量决定页数"未被严格执行，新增完整页数决定体系。hotspot-template.md新增Step 3「页数决定逻辑」（4页/5页/6页适用场景+内容特征+结构+检查清单+禁止事项），候选选题呈现模板新增「建议页数+理由」字段，对比表新增「建议页数」列，新增「页数与内容匹配检查」；SKILL.md Step 2新增页数决定要求，默认值强化页数决定逻辑，Step 3明确按决定页数生成对应数量图，Guardrails新增页数匹配约束；qa-checklist.md新增页数与内容匹配度检查项 |
| 1.6.0 | 2026-09-01 | 借鉴 awesome-gpt-image-2 的 Prompt as Code 理念全面重构 prompt 体系：prompt-template.md 从空文件重构为13.9KB完整文档，新增「Prompt as Code 结构化协议」（7字段块CANVAS/STYLE/LAYOUT/CONTENT/CHARACTER/CONSTRAINTS/AVOID）、「JSON进阶模板」、「内容主导型排版协议」（内容55-65%+墨仔8-10%角落）、「5页差异化状态规划模板增强版」、「实战防坑强化模板增强版」、「模型版本适配」、「文案克制原则」、「完整Prompt示例」、「Prompt生成工作流」；character-lock.md新增「角色一致性前置原则」（CHARACTER字段放在CONTENT之前+8个身份锚点检查）、「五官拆解」（眼睛/嘴巴/头顶芽/身体质感拆解到可执行粒度）、「灵活尺寸与位置协议」（内容主导型8-10%角落+角色主导型18-25%+决策树）；style-lock.md新增「材质与光影强化」（纸张/墨水/光影/pastel底色精细描述）、「信息层级百分比控制」（内容主导型/角色主导型各区域占比+层级检查）、「seedream_5.0_pro风格适配」；SKILL.md Step3新增6条v1.6.0工作流要求，Guardrails新增内容主导型排版约束，已做选题记忆追加4个新选题 |
| 1.7.0 | 2026-09-01 | 基于新生群套路选题多轮迭代实战深度优化，三大核心变更：①**涂鸦是墨仔的天性**——手绘涂鸦背景（铅笔网格+散布涂鸦图标+交叉排线+墨点）从可选排版优化提升为墨仔IP核心视觉特质，每页背景必须有手绘涂鸦质感，禁止大面积纯白空白；style-lock.md完整风格锁重写添加涂鸦背景要求，风格要素拆解新增涂鸦背景行，禁止元素新增大面积纯白空白/扁平无纹理背景，背景装饰从可选提升为核心；character-lock.md墨仔IP设定新增"涂鸦是墨仔的天性"条目，角色要素拆解新增涂鸦天性行，常见问题新增背景大面积纯白空白/背景涂鸦有角色脸修复方法；②**去说教原则**——文案+配图用分享式（"我自己的3个小习惯""我踩过的"）而非命令式（"3个防坑做法，新生必看""只认官方群"），墨仔是观察者和分享者不是教导者；copy-template.md全面重写添加去说教原则（开头优先故事/经历切入模板D、要点列举用分享式措辞、解决方案用第一人称分享、金句用观察型/感悟型、互动提问用平等分享式）、去说教措辞对照表（说教式vs分享式）、去AI味检查新增去说教项、文案去重检查新增去说教口吻项；SKILL.md Step4新增去说教原则（文案），Guardrails新增去说教原则，Prompt强化技巧新增去说教标题/卡片，常见问题新增标题/卡片说教式/文案教导式修复方法；③**image_edit必须用request_list数组格式**——实战验证扁平参数调用会报错required param is empty, field: request_list，必须用request_list数组格式；character-lock.md新增image_edit工具调用格式章节（含正确调用示例），SKILL.md Step3新增image_edit格式要求，常见问题新增image_edit报错修复方法；qa-checklist.md新增J11-J15检查项（涂鸦天性/去说教配图/去说教文案/image_edit格式/背景涂鸦无角色），风格一致性F8新增涂鸦背景，内容构图G7新增去说教标题/卡片，文案检查H11-H12新增去说教口吻/去说教标题提问；已做选题记忆追加"新生群里的套路·90%的人踩过" |
| 1.7.1 | 2026-09-01 | 基于用户反馈"墨仔的表情和动作是根据图文的内容来了，不能毫无关联"新增表情动作与内容关联原则：①character-lock.md新增「表情动作与内容关联原则」完整章节，包含页面类型与表情动作关联表（封面=惊讶/好奇+拿放大镜/举手；分析问题=思考/困惑+托腮/拿本子记录；分析方案=坚定/认真+叉腰/举盾牌/指方向；金句=沉思/温暖+托腮/手放胸口/盘腿沉思；互动=好奇/邀请+挥手/拿喇叭/举手提问）、关联检查模板（新增内容关联理由列）、常见错误（为了差异化而差异化/动作与内容无关/表情情绪与内容矛盾）、双重约束（内容关联+每页差异化必须同时满足）；②prompt-template.md 5页差异化状态规划模板增强，新增"页面类型"和"内容关联理由"列，差异化检查清单新增3条内容关联检查项（表情与页面类型匹配/动作与页面内容相关/内容关联理由已填写）；③SKILL.md Step3新增表情动作与内容关联工作流要求，Guardrails新增表情动作与内容关联核心约束，版本历史新增v1.7.1；④qa-checklist.md新增J16-J18检查项（表情与页面类型匹配/动作与页面内容相关/内容关联理由已填写） |
| 1.7.2 | 2026-09-03 | 基于班级群假班主任诈骗选题seedream_5.0_pro实战迭代，核心变更：①**颜色代码防护**——实战发现prompt中的十六进制颜色代码（#FBFAF5/#1B1B1B/#A8C879/#FBAF5）会被seedream模型渲染成画面文字乱码（如"183:5@FBAF5""#1B-COB""#15-2065"出现在角落），全部改为文字描述（warm off-white/ink-black/light sage-green/pale blue等），style-lock.md和character-lock.md的完整锁移除所有颜色代码，prompt-template.md新增颜色代码防护章节，qa-checklist.md新增J19检查项；②**副标题重复渲染防护**——P1初稿副标题被渲染成两行相同文字，CONSTRAINTS新增"Subtitle appears ONLY ONCE"；③**装饰线随机数字防护**——P3初稿装饰线上出现"03 03 03"，CONSTRAINTS新增"Divider line is plain, NO numbers on it"；④**墨仔动作强化**——P3初稿墨仔未执行双手叉腰（手臂下垂），CONSTRAINTS新增"BOTH HANDS CLEARLY ON HIPS, NO arms hanging down"；⑤已做选题记忆追加"班级群假班主任诈骗·33人被骗9108元" |
| 1.8.0 | 2026-09-03 | 基于家长群晒身份选题多轮迭代（场景版重做+master-copywriting合规+封面强钩子+画风修复），四大核心变更：①**场景叙事型排版**——用户反馈"不能老画文字，也得配图"，新增第三排版模式：每页以一个场景画为主（墨仔融入场景做主题动作：举手机看群/指黑板/举"一视同仁"牌/站天平横梁/挥手+喇叭），文字仅标题+短标签≤4字+金句；prompt-template.md新增"十、场景叙事型排版协议"；②**原始画风不可变**——用户反馈"原始画风要求不能变"，封面强钩子改造时易弱化style-lock元素（双线边框/四角装饰/波浪下划线/pastel标签/涂鸦背景），规定任何改动必须逐项核对完整保留；style-lock.md新增"原始画风不可变"章节；③**封面强钩子**——第一张图文案钩子和画面必须吸引人，悬念+反差型（"一条自我介绍/让家长群安静了"）优于直白陈述型，画面关键消息高亮+周围灰化制造冲突；④**master-copywriting文案合规**——发布级文案对照G1-G12核查（事实层/抖音生活故事体/去AI味H2/画面感与配图呼应），copy-template.md新增合规检查章节；SKILL.md Step3/Step4/Guardrails/故障排除同步更新；qa-checklist.md新增K系列检查项；已做选题记忆追加"场景版""封面强钩子版" |

## 最终回复格式

交付完成后，报告：
- 选题名称和热点来源
- 4页标题 + 墨仔动作 + 状态（完美/小瑕疵）
- Seedling 形象一致性检查结果
- 配套文案（标题+正文+话题标签）
- 小瑕疵说明（如有）和修正选项
