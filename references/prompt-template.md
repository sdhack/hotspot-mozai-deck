# Prompt Template · 4页完整 Prompt 模板

使用方法：
1. 复制每页模板
2. 把 `{{变量}}` 替换为选题的具体内容
3. 把 style-lock 和 character-lock 的完整内容粘贴到每页 prompt 开头
4. 用 image_edit 工具，传入人物卡 URL，一次调用生成 4 张
5. 生成后立即跑 QA checklist，发现问题当场修正

---

## 变量清单

| 变量 | 说明 | 示例 |
|---|---|---|
| `{{cover_tag1}}` | 封面顶部标签1（热点类型） | 实时热点 |
| `{{cover_tag2}}` | 封面顶部标签2（地点/分类） | 四川凉山 |
| `{{cover_title_line1}}` | 封面标题第一行 | 考低分就和耻辱合影？ |
| `{{cover_title_line2}}` | 封面标题第二行 | 这操作我看不懂 |
| `{{cover_subtitle}}` | 封面副标题 | 四川雷波县·2026秋季教育行政会·8月28日热搜 |
| `{{cover_scene}}` | 封面中间场景描述 | 舞台+大屏幕"耻辱"+教师低头+手机拍照 |
| `{{cover_seedling_action}}` | 封面墨仔动作 | 举"？"牌挠头，困惑表情 |
| `{{cover_mouth}}` | 封面墨仔嘴型 | confused small / surprised O |
| `{{cover_tag_bottom1}}` | 封面底部标签1 | 羞辱式管理 |
| `{{cover_tag_bottom2}}` | 封面底部标签2 | 教师尊严 |
| `{{cover_tag_bottom3}}` | 封面底部标签3 | 教育争议 |
| `{{p2_title}}` | P2标题 | 耻辱教育的3个问题 |
| `{{p2_subtitle}}` | P2副标题 | 羞辱从来不是激励 |
| `{{p2_card1_title}}` | P2卡片1标题 | 问题一：羞辱≠激励 |
| `{{p2_card1_desc}}` | P2卡片1描述 | 当众羞辱只会打击自信，不会提升成绩 |
| `{{p2_card2_title}}` | P2卡片2标题 | 问题二：践踏教师尊严 |
| `{{p2_card2_desc}}` | P2卡片2描述 | 老师也是人，尊严被踩碎了怎么好好教书 |
| `{{p2_card3_title}}` | P2卡片3标题 | 问题三：传递错误价值观 |
| `{{p2_card3_desc}}` | P2卡片3描述 | 老师被羞辱，学生学会的是用羞辱解决问题 |
| `{{p2_seedling_action}}` | P2墨仔动作 | 持放大镜审视卡片，认真表情 |
| `{{p2_mouth}}` | P2墨仔嘴型 | serious line |
| `{{p3_title}}` | P3标题 | 成绩差该怎么办？ |
| `{{p3_subtitle}}` | P3副标题 | 3个正确做法，比羞辱有用一万倍 |
| `{{p3_step1_title}}` | P3步骤1标题 | 做法一：教研帮扶 |
| `{{p3_step1_desc}}` | P3步骤1描述 | 优秀老师带教，集体备课，不是一个人扛 |
| `{{p3_step2_title}}` | P3步骤2标题 | 做法二：分层教学 |
| `{{p3_step2_desc}}` | P3步骤2描述 | 承认学生差异，不同基础用不同方法，不搞一刀切 |
| `{{p3_step3_title}}` | P3步骤3标题 | 做法三：家校沟通 |
| `{{p3_step3_desc}}` | P3步骤3描述 | 和家长一起找原因，不是把锅甩给老师 |
| `{{p3_quote_line1}}` | P3金句第一行 | 好的教育是点燃一把火 |
| `{{p3_quote_line2}}` | P3金句第二行 | 不是浇灭一个人的尊严 |
| `{{p3_seedling_action}}` | P3墨仔动作 | 持清单核对，坚定表情 |
| `{{p3_mouth}}` | P3墨仔嘴型 | determined press |
| `{{p4_title}}` | P4标题 | 教育需要尊严，不是羞辱 |
| `{{p4_subtitle}}` | P4副标题 | 老师有尊严，学生才能学会尊重 |
| `{{p4_tag1}}` | P4标签1 | 拒绝羞辱 |
| `{{p4_tag2}}` | P4标签2 | 尊重教师 |
| `{{p4_tag3}}` | P4标签3 | 科学育人 |
| `{{p4_scene}}` | P4中间场景 | 温暖教室+老师微笑+学生举手 |
| `{{p4_sign_text}}` | P4墨仔举牌文字 | 尊严 |
| `{{p4_bubble_line1}}` | P4对话气泡第一行 | 你怎么看这种耻辱合影？ |
| `{{p4_bubble_line2}}` | P4对话气泡第二行 | 评论区说说你的看法 |
| `{{p4_seedling_action}}` | P4墨仔动作 | 举牌子，微笑表情 |
| `{{p4_mouth}}` | P4墨仔嘴型 | friendly smile |

---

## 数字一致性检查（生成前必做，v1.2.0 新增）

生成 prompt 前，先核对：
1. 封面标题说"N件事/N个坑" → P2 的卡片数量必须 = N
2. P2 的问题数量 → P3 的解决方案数量必须 = N（或明确说明覆盖关系）
3. 文案正文的编号（第一/第二/...）必须连续到 N
4. 封面底部标签数量 = P4 顶部标签数量（或有明确理由）

不一致时，先调整设计再生成，不要生成后再改数字。

---

## 完整 Prompt 模板（4页，直接复制替换变量）

### 第1页：封面

```
ST1-cover: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
Mouth expression: {{cover_mouth}}

Composition:
- Top: decorative corners. Top-center: tiny icon + pale peach tag handwritten {{cover_tag1}} + pale blue tag handwritten {{cover_tag2}}.
- Upper 22%: LARGE BOLD HAND-LETTERED title two lines: first line {{cover_title_line1}}, second line {{cover_title_line2}}. Second line has wavy underline.
- Below: thin divider + subtitle in pencil handwriting {{cover_subtitle}}.
- Middle 38%: detailed hand-drawn scene: {{cover_scene}}. SEEDLING CHARACTER stands at lower center, {{cover_seedling_action}}. Cross-hatching. Small relevant icon near scene.
- Lower 20%: faint pencil grid + doodle icons. Bottom center: three pastel tags with handwritten text: {{cover_tag_bottom1}} (pale blue), {{cover_tag_bottom2}} (pale peach), {{cover_tag_bottom3}} (pale sage green).
- Bottom: decorative corners.

Required Chinese text (ALL HANDWRITTEN): {{cover_tag1}}, {{cover_tag2}}, {{cover_title_line1}}, {{cover_title_line2}}, {{cover_subtitle}}, {{cover_tag_bottom1}}, {{cover_tag_bottom2}}, {{cover_tag_bottom3}}

Avoid: TWO characters, multiple characters, slim body, elongated body, pointed sharp top, tiny white-dot eyes, centered pupils, no mouth, black mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, giant title, heavy boxes, gibberish, watermark, childish cartoons, thick outlines, saturated colors, corporate template, shadows, gradients, neon, horizontal landscape, clean vector, random numbers, percentages.
```

### 第2页：问题/分析（3-4卡片，v1.2.0 强化排版+图标无脸）

```
ST2-problems: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
CRITICAL: EXACTLY ONE character on this page. The character is ONLY at right side of card stack, holding magnifying glass. NO character inside any card, NO small character anywhere else, NO character in icons. All card icons are INANIMATE objects (NO face, NO character, NO teardrop shape).
Mouth expression: {{p2_mouth}}

Composition (optimized layout):
- Decorative corners, double-line border.
- Upper 10%: page number 02/04 handwritten upper-left ONLY with small circle. Centered title {{p2_title}} in bold hand-lettering with wavy underline and small pencil icon. Subtitle {{p2_subtitle}} in pencil handwriting below with thin divider lines on both sides.
- Below title: horizontal divider with swirls and small stars.
- Middle 60%: three/four stacked cards from top to bottom, each with folded top-right corner, double-line border, pastel wash background, subtle drop shadow, and a large hand-drawn circled number on left side. Each card contains ONLY text and an inanimate object icon (NO face, NO character):
  Card 1 (top, pale blue wash): large circled number 1, inanimate [object1] icon (NO face, NO character), bold title {{p2_card1_title}}, sub-label {{p2_card1_desc}}. Small relevant icon next to title.
  Card 2 (middle, pale peach wash): large circled number 2, inanimate [object2] icon (NO face, NO character), bold title {{p2_card2_title}}, sub-label {{p2_card2_desc}}. Small relevant icon next to title.
  Card 3 (bottom, pale sage wash): large circled number 3, inanimate [object3] icon (NO face, NO character), bold title {{p2_card3_title}}, sub-label {{p2_card3_desc}}. Small relevant icon next to title.
  (Card 4 if needed, pale lavender wash: large circled number 4, ...)
- Small downward arrows between cards with tiny stars.
- SEEDLING CHARACTER stands ONLY at right side of card stack, {{p2_seedling_action}}. Fine cross-hatching on body. This is the ONLY character on the entire page.
- Background: faint pencil grid throughout, tiny doodle icons scattered (inanimate objects only, NO character doodles, NO faces in doodles).

Required Chinese text (ALL HANDWRITTEN): 02/04, {{p2_title}}, {{p2_subtitle}}, {{p2_card1_title}}, {{p2_card1_desc}}, {{p2_card2_title}}, {{p2_card2_desc}}, {{p2_card3_title}}, {{p2_card3_desc}}

Avoid: TWO characters, multiple characters, second character, small character, character inside card, character in icon, face in icon, teardrop shape in card, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, smiling mouth, pressed mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, heavy boxes, gibberish, watermark, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, duplicate page number on right, random numbers, percentages, time labels.
```

### 第3页：解决方案（3-4步骤 + 金句，v1.2.0 强化）

```
ST3-solutions: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
CRITICAL: EXACTLY ONE character on this page. The character is ONLY at right side of step stack. NO character inside any step card, NO character in icons. All step icons are INANIMATE objects (NO face, NO character).
Mouth expression: {{p3_mouth}}

PAGE NUMBER: upper-left handwritten 03/04 ONLY with small circle.

Composition (timeline layout optional):
- Decorative corners, double-line border.
- Upper 10%: page number 03/04 upper-left in circle. Centered title {{p3_title}} in bold hand-lettering with wavy underline and small clock icon. Subtitle {{p3_subtitle}} in pencil handwriting below with divider lines.
- Below title: horizontal divider with swirls.
- Middle 50%: three/four step cards stacked vertically, connected by downward arrows with tiny stars, each with checkmark icon and inanimate object icon (NO face, NO character). Optional: wavy vertical timeline on left with circled numbers connected to it.
  Step 1 (top, pale blue wash): inanimate [object1] icon (NO face), bold title {{p3_step1_title}}, sub-label {{p3_step1_desc}}.
  Step 2 (middle, pale peach wash): inanimate [object2] icon (NO face), bold title {{p3_step2_title}}, sub-label {{p3_step2_desc}}.
  Step 3 (bottom, pale sage wash): inanimate [object3] icon (NO face), bold title {{p3_step3_title}}, sub-label {{p3_step3_desc}}.
  (Step 4 if needed, pale lavender wash: ...)
- SEEDLING CHARACTER stands ONLY at right side of step stack, {{p3_seedling_action}}. Fine cross-hatching on body. Ink splatter near feet. This is the ONLY character on the page.
- Lower 25%: detailed hand-drawn quote box centered, double-line border with ornamental corner brackets and small quote mark symbol, no fill. Two lines of natural handwritten Chinese: first line {{p3_quote_line1}}, with small ink dot quote mark; second line {{p3_quote_line2}}. Ink dot divider between lines. Small decorative stars around quote box.
- Bottom: decorative corners. Faint pencil grid background with tiny inanimate doodles.

Required Chinese text (ALL HANDWRITTEN, NO ENGLISH): 03/04, {{p3_title}}, {{p3_subtitle}}, {{p3_step1_title}}, {{p3_step1_desc}}, {{p3_step2_title}}, {{p3_step2_desc}}, {{p3_step3_title}}, {{p3_step3_desc}}, {{p3_quote_line1}}, {{p3_quote_line2}}

Avoid: TWO characters, multiple characters, second character, character inside card, character in icon, face in icon, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, smiling mouth, straight line mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, Latin chars, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, oversized objects, heavy boxes, gibberish, watermark, crowded, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, clean vector, percent sign in page number, color codes, duplicate page number on right, extra speech bubble near character, random numbers, 50%, extra percentages, time labels, statistics.
```

### 第4页：落点（温暖场景 + 举牌 + 互动气泡，v1.2.0 强化气泡唯一+无多余数字）

```
ST4-takeaway: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
CRITICAL: EXACTLY ONE character on this page. EXACTLY ONE speech bubble on this page. NO second bubble, NO duplicate bubble, NO two bubbles. The ONLY number on this page is the page number 04/04. NO random numbers, NO percentages, NO time labels, NO statistics.
Mouth expression: {{p4_mouth}}

Composition (FIXED - ONE character, ONE bubble, NO extra hand, NO random numbers):
- Decorative corners all four, double-line border.
- Upper 10%: page number 04/04 handwritten UPPER-LEFT ONLY in small circle. This is the ONLY number on the page. Centered title {{p4_title}} in bold hand-lettering with wavy underline and small graduation cap icon. Subtitle {{p4_subtitle}} in pencil handwriting below with divider lines.
- Below title: small horizontal row of three/four pastel tags with wobbly hand-drawn double borders and handwritten text: pale blue {{p4_tag1}}, pale peach {{p4_tag2}}, pale sage green {{p4_tag3}}, (pale lavender {{p4_tag4}} if 4 tags). Decorative dots and tiny stars between tags. NO numbers in tags.
- Middle 30%: a richly detailed hand-drawn warm scene: {{p4_scene}}. Warm light rays. Large negative space with faint pencil grid, tiny doodle stars and sparkles. NO extra hand, NO extra fingers, NO numbers, NO percentages, NO time labels in scene.
- Lower 30%: SEEDLING CHARACTER stands at lower-center, holding a small detailed rectangular sign with both arms, sign has double-line border and reads {{p4_sign_text}} in bold hand-lettered ink. Character with fine cross-hatching on body, upward-gazing friendly smile. Above character, EXACTLY ONE detailed hand-drawn speech bubble (double-line border, ornamental tail pointing to character, no fill, small decorative dots around) containing two lines of natural handwritten Chinese: first line {{p4_bubble_line1}}, second line smaller {{p4_bubble_line2}}. NO second bubble, NO duplicate bubble.
- Bottom: decorative corners. Faint pencil grid throughout with tiny doodles (star, heart, flower, leaf, sparkles). NO random numbers, NO percentages, NO time stamps, NO extra text, NO statistics.

Required Chinese text (ALL HANDWRITTEN, NO ENGLISH): 04/04, {{p4_title}}, {{p4_subtitle}}, {{p4_tag1}}, {{p4_tag2}}, {{p4_tag3}}, {{p4_sign_text}}, {{p4_bubble_line1}}, {{p4_bubble_line2}}

Avoid: TWO characters, multiple characters, second character, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, straight line mouth, pressed mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, color codes, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, oversized objects, heavy boxes, gibberish, watermark, crowded, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, clean vector, SECOND hand, extra fingers, hand pointing, duplicate page number on right, DUPLICATE SPEECH BUBBLE, second bubble, TWO bubbles, RANDOM NUMBERS, percentages, 32s, 28%, 50%, time labels, statistics, any number except 04/04, extra text.
```

---

## Prompt 强化技巧速查（v1.2.0 新增）

| 问题 | 强化写法 |
|---|---|
| 出现第二个角色 | `EXACTLY ONE character. The character is ONLY at [position]. NO character inside any card, NO small character anywhere else.` |
| 卡片图标变成小墨仔 | 每个图标标注 `inanimate [object] icon (NO face, NO character, NO teardrop shape)` |
| P4 出现两个气泡 | `EXACTLY ONE speech bubble. NO second bubble, NO duplicate bubble, NO two bubbles.` |
| 出现多余数字 | `The ONLY number on this page is the page number. NO random numbers, NO percentages, NO time labels.` + Avoid 列举 `50%, 32s, 28%` |
| 封面数字与正文不一致 | 生成前先核对：封面N件=P2卡片数=P3步骤数=文案编号数 |

---

## 调用方式

用 `image_edit` 工具，`request_list` 包含 4 个对象（每页一个），每个对象：
- `height`: 1440
- `width`: 1080
- `image_reference_url_list`: `["人物卡URL"]`
- `prompt`: 上面对应页的完整 prompt（已替换变量）

每页 prompt 前缀加唯一 tag（如 `ST1-cover:`、`ST2-problems:`）避免文件名冲突。

---

## v1.5.0 新增：实战防坑强化模板

基于2026-09-01课后延时服务选题10+轮迭代实战验证，以下强化写法能有效避免模型反复出现的问题。

### 1. 卡片内容防重复（P2/P3 必加）

**问题**：即使写 `EXACTLY THREE cards`，模型仍可能生成4张卡片，且卡片2和卡片3内容重复。

**强化写法**：
```
EXACTLY THREE cards arranged horizontally side by side. 
NO fourth card. NO extra card. NO more, NO less.
Card 3 is DIFFERENT from cards 1 and 2 - it has unique title and unique description.
NO duplicate content between cards.
```

**实战验证**：P3原生成4张卡片且卡片2/3重复，加此约束后修复为3张不重复。

### 2. 标签防重复（封面/P5 必加）

**问题**：底部标签或顶部标签可能重复出现同一个标签（如"课后延时"出现两次）。

**强化写法**：
```
EXACTLY THREE pastel tags in a single row. NO fourth tag. 
Each tag ONLY ONCE. "{{tag1}}" ONLY ONCE. "{{tag2}}" ONLY ONCE. "{{tag3}}" ONLY ONCE.
NO duplicate tags. NO tag appears twice.
```

**实战验证**：P1底部标签原重复出现，P5标签"课后延时"原重复，加此约束后修复。

### 3. 随机数字防护（每页必加，尤其P4）

**问题**：模型可能在页面角落生成随机数字（如"40%"、"10%"、"32s"）。

**强化写法**：
```
The ONLY number on this page is the page number {{NN}}/05.
NO random numbers. NO percentages. NO time labels. NO statistics. 
NO 40%. NO 10%. NO 32s. NO 28%. NO any number except page number.
```

**实战验证**：P4左上角原出现"40%"随机数字，加此约束后修复。

### 4. 逻辑标题规范（金句页必加）

**问题**：金句页标题用"写在最后"，但后面还有互动页，逻辑矛盾。

**规范**：
- 金句页（P4）标题**不能用**"写在最后"、"最后想说"、"结束语"等暗示"这是最后一页"的词
- 推荐标题："墨仔想说"、"一句话送给你"、"记住这句话"、"墨仔的话"
- 金句页标题**不能与金句内容重复**（如标题"报名率是别人的节奏"+金句也是同一句话）

**强化写法**：
```
Title is "{{title}}" - NOT containing word "最后". NOT "写在最后". 
Title is DIFFERENT from quote content. Quote is "{{quote_line1}} / {{quote_line2}}".
```

**实战验证**：P4原标题"写在最后"逻辑矛盾，改为"墨仔想说"后修复。

### 5. 墨仔周围空白防护（每页必加）

**问题**：模型可能在墨仔附近生成英文角色名"Mozai"、随机文字或数字。

**强化写法**：
```
Area around character COMPLETELY BLANK - no text, no letters, no "Mozai", no numbers, no tags. ONLY character.
```

**实战验证**：P2/P3墨仔附近原出现英文"Mozai"，加此约束后修复。

### 6. 5页差异化状态规划模板（生成前必做）

生成5页配图前，必须先规划每页墨仔的差异化状态，确保眼睛/嘴型/动作全部不同：

| 页 | 角色定位 | 眼睛状态 | 嘴型 | 身体动作 | 场景 |
|---|---|---|---|---|---|
| P1 封面 | 困惑好奇 | 右眼瞪大+左眼眯起(wink) | 小O形(含粉舌) | 站立举手机+挠头 | 大手机+班级群 |
| P2 分析 | 沉思分析 | 双眼向上看 | 波浪线~ | 盘腿坐地+托腮 | 3卡片横向排列 |
| P3 方案 | 果断坚定 | 双眼坚定聚焦+眉蹙 | 抿嘴嘴角下撇 | 踩石头+叉腰+指方向 | 3卡片横向排列 |
| P4 金句 | 悠闲开心 | 双眼闭成小月牙 | 小微笑弧线 | 盘腿坐大云+托腮 | 天空云朵夕阳 |
| P5 互动 | 期待邀请 | 大圆眼注视观众 | 小O形(含粉舌) | 站立举牌子+挥手 | 对话气泡+评论图标 |

**规则**：
- 5页眼睛状态必须全部不同
- 5页嘴型必须全部不同（P1和P5虽都是O形，但P1是wink好奇，P5是注视观众期待，场景和动作不同）
- 5页身体动作必须全部不同
- 张嘴页（P1/P5）必须含粉舌拟人化
- 所有嘴型都是SMALL小比例，不夸张

---

## 模型版本建议（v1.5.0 新增）

| 模型 | 分辨率 | 画质 | 适用场景 |
|---|---|---|---|
| seedream_4.5（默认） | 1080×1440 | 良好 | 快速迭代、初稿生成 |
| **seedream_5.0_pro（推荐）** | **1773×2364** | **优秀** | **最终交付、高质量要求** |

**建议**：
- 初稿/迭代阶段用 seedream_4.5（速度快，成本低）
- 最终交付版用 seedream_5.0_pro（画质提升64%，手绘质感更细腻，墨仔外观一致性更好）
- PRO版在 `image_edit` 工具的 `model_version` 参数中指定 `"seedream_5.0_pro"`

**实战验证**：2026-09-01课后延时服务选题，PRO版画质明显优于4.5版，墨仔外观一致性更好，手绘细节更丰富。
