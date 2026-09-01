# Prompt Template · 配图 Prompt 模板（v1.6.0 重构）

> v1.6.0 借鉴 awesome-gpt-image-2 的「Prompt as Code」理念重构：把散文式提示词压缩成结构化协议，原子化字段可组合，角色一致性前置，材质光影精细描述，文案克制原则。

---

## 一、Prompt as Code 结构化协议（核心，每页必用）

每页 prompt 必须按以下 7 个字段块顺序组织，字段名用大写标记，不可省略。这是从 awesome-gpt-image-2 借鉴的核心方法论——结构化比散文更可控。

```
=== CANVAS ===
[画布比例、尺寸、平台适配]

=== STYLE ===
[风格锁：纸张、线条、纹理、边框、字体、配色——逐字复制 style-lock.md]

=== LAYOUT ===
[布局协议：信息层级、各区域占比百分比、角色位置与尺寸]

=== CONTENT ===
[内容主体：标题、副标题、卡片/图标/文字的具体内容与数量]

=== CHARACTER ===
[角色锁：完整角色描述+本页差异化状态——逐字复制 character-lock.md 核心+本页变量]

=== CONSTRAINTS ===
[硬约束：数字一致性、卡片不重复、标签不重复、页码唯一等]

=== AVOID ===
[禁止列表：具体列举模型容易犯的错误]
```

> ⚠️ **为什么用结构化协议**：awesome-gpt-image-2 的 544 个案例逆向工程证明，结构化字段比散文描述的可控性高 3-5 倍。模型对大写字段标记的注意力更强，字段顺序固定后，Agent 可以批量替换变量而不破坏结构。

---

## 二、JSON 进阶模板（推荐给 Agent 批量调用）

当需要批量生成多页或多选题时，使用 JSON 模板，Agent 可程序化填充变量后转成自然语言 prompt。

```json
{
  "canvas": {
    "ratio": "3:4",
    "size": "1773x2364",
    "platform": "Douyin vertical article"
  },
  "style": {
    "paper": "warm off-white (#FBFAF5)",
    "lines": "hand-drawn pencil sketch + ink outlines",
    "texture": "cross-hatching + stippling + subtle ink bleed",
    "border": "thin double-line border + decorative corner flourishes",
    "fonts": "bold brush/marker hand-lettering for title, casual pencil handwriting for body",
    "colors": "pastel pale blue/peach/sage/lavender washes, ink-black #1B1B1B"
  },
  "layout": {
    "mode": "content-dominant",
    "title_area": "top 15-20%",
    "content_area": "middle 55-65% (cards/icons/text)",
    "character_area": "corner 8-10% (bottom-left or bottom-right)",
    "decoration_area": "background doodles + tags, scattered"
  },
  "content": {
    "title": "{{页面标题}}",
    "subtitle": "{{副标题}}",
    "page_number": "{{0X/0N}}",
    "cards": [
      {"number": 1, "title": "{{卡片1标题}}", "text": "{{卡片1说明}}", "icon": "{{无生命物体图标}}", "color": "pale blue"},
      {"number": 2, "title": "{{卡片2标题}}", "text": "{{卡片2说明}}", "icon": "{{无生命物体图标}}", "color": "pale peach"},
      {"number": 3, "title": "{{卡片3标题}}", "text": "{{卡片3说明}}", "icon": "{{无生命物体图标}}", "color": "pale sage"}
    ],
    "tags": ["#{{标签1}}", "#{{标签2}}", "#{{标签3}}"],
    "quote": "{{金句，仅金句页}}"
  },
  "character": {
    "core_lock": "round plump black teardrop + small sprout with slightly curly stem + TWO light sage-green leaves + LARGE round eyes with big white whites + SMALL BLACK mouth + exactly TWO thin arms + exactly TWO short legs + hand-drawn ink texture",
    "page_state": {
      "position": "{{bottom-left or bottom-right corner}}",
      "size": "8-10% of page height (content-dominant mode)",
      "action": "{{本页动作}}",
      "eyes": "{{本页眼睛状态}}",
      "mouth": "{{本页嘴型}}",
      "expression": "{{本页情绪}}"
    }
  },
  "constraints": {
    "exactly_one_character": true,
    "exactly_two_arms_legs": true,
    "cards_different": true,
    "tags_no_duplicate": true,
    "page_number_only_once": true,
    "no_random_numbers": true,
    "no_english_text": true,
    "mouth_pink_tongue_when_open": true,
    "no_blush": true,
    "character_consistency": true
  },
  "avoid": [
    "extra limbs, third arm, third leg",
    "all-black mouth hole, no tongue",
    "large mouth, exaggerated expression",
    "pink blush on cheeks",
    "duplicate cards, duplicate tags",
    "random numbers (50%, 10%, 32s, 28%, 40%)",
    "English text (MOZAI, SEEDLING, STOP)",
    "character inside cards or icons",
    "face in icons",
    "formal printed fonts",
    "saturated colors, pure black background"
  ]
}
```

---

## 三、布局协议（v1.6.0 新增，借鉴信息层级控制）

### 3.1 内容主导型排版（Content-Dominant，默认推荐）

> 基于用户硬约束："生图必须以内容为主，排版美化，手绘风，墨仔为辅，墨仔比例不能占比太高"

```
=== LAYOUT ===
LAYOUT MODE: CONTENT-DOMINANT (content is MAIN visual focus, character is secondary accent).

TITLE AREA: top 15-20% of page. Large bold hand-lettered title with wavy underline + subtitle with thin divider lines.

CONTENT AREA: middle 55-65% of page. This is the MAIN visual focus. Cards/icons/text occupy this space. Cards have folded corners, double-line borders, pastel wash backgrounds, large circled numbers on left, small downward arrows with stars between cards.

CHARACTER AREA: ONLY 8-10% of page height. Positioned at bottom-left OR bottom-right CORNER (never center, never upper area). Character is a small accent, NOT the main subject. Area around character is COMPLETELY BLANK (no text, no icons, no doodles within 1cm of character).

DECORATION AREA: scattered tiny doodle icons (inanimate objects only, NO faces, NO characters) in background gaps, faint pencil grid, pastel tags at bottom.

PAGE NUMBER: upper-left ONLY, inside small circle, appears ONLY ONCE.
```

### 3.2 角色主导型排版（Character-Dominant，仅封面/互动页可选）

```
=== LAYOUT ===
LAYOUT MODE: CHARACTER-DOMINANT (character is main visual focus, content supports it).

CHARACTER AREA: center or lower-center, 20-30% of page height. Character is the main subject, doing a prominent action.

TITLE AREA: top 20-25%. Large title.

CONTENT AREA: surrounding character, 30-40%. Small cards, icons, tags arranged around character.

⚠️ 仅封面页和互动页可使用此模式。分析页/金句页必须使用内容主导型。
```

---

## 四、5 页差异化状态规划模板（v1.6.0 增强）

生成前必须先填写此表，确保每页眼睛/嘴型/动作/位置全部不同，且表情动作与页面内容强关联。借鉴 awesome-gpt-image-2 的「角色一致性前置」原则——把差异化状态写在内容之前。

> v1.7.1 新增：**表情动作与内容关联原则**——墨仔的表情和动作必须根据图文内容来定，不能毫无关联。差异化不是目的，内容关联才是目的。详见 character-lock.md「表情动作与内容关联原则」。

| 页 | 页面类型 | 内容主题 | 位置 | 尺寸 | 动作 | 眼睛 | 嘴型 | 情绪 | 布局模式 | 内容关联理由 |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 封面 | 封面（钩子/震惊） | {{封面钩子内容}} | 右下角 | 18-25% | {{动作1}} | {{眼睛1}} | {{嘴型1}} | {{情绪1}} | 角色主导 | {{为什么这个表情/动作适合封面内容}} |
| P2 分析 | 分析（问题/套路） | {{P2问题内容}} | 左下角 | 8-10% | {{动作2}} | {{眼睛2}} | {{嘴型2}} | {{情绪2}} | 内容主导 | {{关联理由}} |
| P3 分析 | 分析（方案/做法） | {{P3方案内容}} | 右下角 | 8-10% | {{动作3}} | {{眼睛3}} | {{嘴型3}} | {{情绪3}} | 内容主导 | {{关联理由}} |
| P4 金句 | 金句（感悟/落点） | {{P4金句内容}} | 左下角 | 8-10% | {{动作4}} | {{眼睛4}} | {{嘴型4}} | {{情绪4}} | 内容主导 | {{关联理由}} |
| P5 互动 | 互动（提问/邀请） | {{P5互动内容}} | 右下角 | 18-25% | {{动作5}} | {{眼睛5}} | {{嘴型5}} | {{情绪5}} | 角色主导 | {{关联理由}} |

**差异化+内容关联双重检查清单（生成前必过）**：
- [ ] 5 页眼睛状态全部不同（至少 4 种）
- [ ] 5 页嘴型全部不同（至少 4 种，张嘴页含粉舌）
- [ ] 5 页身体动作全部不同
- [ ] 5 页位置交替（左下/右下轮换，不连续同侧）
- [ ] 张嘴页不超过 2 页（通常 P1 封面 + P5 互动）
- [ ] 闭眼/微笑页至少 1 页（通常 P4 金句）
- [ ] **v1.7.1 新增：每页表情与页面类型匹配**（封面=惊讶/好奇，分析问题=思考/困惑，分析方案=坚定/认真，金句=沉思/温暖，互动=好奇/邀请）
- [ ] **v1.7.1 新增：每页动作与页面内容相关**（分析问题=托腮/拿本子/拿放大镜，分析方案=叉腰/举盾牌/指方向，金句=托腮/手放胸口/盘腿沉思，互动=挥手/拿喇叭/举手提问）
- [ ] **v1.7.1 新增：内容关联理由已填写**（每页都有明确的关联理由，不是"随便选一个"）

---

## 五、实战防坑强化模板（v1.6.0 增强，借鉴避坑指南）

以下约束必须写入每页 prompt 的 CONSTRAINTS 和 AVOID 字段。每条都来自实战踩坑验证。

### 5.1 角色防坑
```
=== CONSTRAINTS ===
EXACTLY ONE character on page, never two or more.
EXACTLY TWO thin black arms with small hands, EXACTLY TWO short black legs with small feet. NO extra limbs, NO third arm, NO third leg, NO multi-hand multi-foot.
Character is ONLY at [position], doing [action]. NO character inside any card, NO small character anywhere else, NO character in icons.
All card icons are INANIMATE objects (NO face, NO character, NO teardrop shape).
Character appearance strictly matches reference: round plump black teardrop, small sprout with slightly curly stem + TWO light sage-green leaves, LARGE round eyes with big white whites, SMALL BLACK mouth, hand-drawn ink texture with natural ink bleed.
When mouth is open: SMALL open oval shape, visible PINK/RED TONGUE inside, anthropomorphic human-like mouth interior, NOT all-black hole, NOT wide, NOT large.
NO blush, NO pink cheeks, NO red cheeks. Face is clean black ink.
Mouth expression is SMALL and restrained, NOT exaggerated, NOT wide open.
```

### 5.2 内容防坑
```
=== CONSTRAINTS ===
EXACTLY [N] cards stacked vertically. NO [N+1]th card. NO extra card. NO more, NO less.
Card [N] is DIFFERENT from Card 1 and Card 2. NO duplicate content, NO repeated titles, NO same icon.
Each tag appears ONLY ONCE. NO duplicate tags.
Page number appears ONLY ONCE at upper-left inside small circle. NO second page number. NO page number near title.
The ONLY number on the page is the page number [0X/0N]. NO random numbers, NO percentages, NO time labels, NO statistics, NO 50%, NO 10%, NO 32s, NO 28%, NO 40%.
ALL TEXT IS CHINESE HANDWRITTEN STYLE. NO English text, NO character names (NO "Mozai", NO "SEEDLING"), NO version labels, NO formal printed fonts.
Area around character is COMPLETELY BLANK. No text, no icons, no doodles, no letters within 1cm of character.
Title and quote content are DIFFERENT. Title does NOT repeat quote text.
```

### 5.3 常见错字预防（拼音+偏旁拆解）
```
=== CONSTRAINTS ===
TEXT MUST BE 拨打110 (拨 = 扌+发, pronounced bo). NOT 技打 (技 = 扌+支, pronounced ji).
TEXT MUST BE 过马路 (马 = 马字旁, pronounced ma). NOT 过下路 (下 = 下, pronounced xia).
Also 派出所 (only one 派), 冻结 (only one 冻), 保留 (only one 保).
```

### 5.4 符号控制
```
=== CONSTRAINTS ===
NO $ sign. NO dollar sign. NO currency symbols. NO % sign in icons.
Money bag icon is plain cloth sack with tie, NO symbol on it.
Shield icon is plain shield, NO $ or other symbol inside.
All icons contain NO text, NO numbers, NO letters. Icons are pure illustrations only.
```

---

## 六、模型版本适配（v1.6.0 新增）

### seedream_5.0_pro（最终交付推荐，1773×2364）
- 画质更优，细节更丰富，文字渲染更准确
- prompt 中可增加更精细的材质描述（见 style-lock.md 增强版）
- 对结构化协议的响应更好，字段标记更有效
- 适合最终交付版

### seedream_4.5（初稿/迭代用，1080×1440）
- 速度快，适合快速验证布局和内容
- prompt 可适当简化，减少材质细节描述
- 适合初稿和迭代修改

---

## 七、文案克制原则（v1.6.0 新增，借鉴 awesome-gpt-image-2）

> awesome-gpt-image-2 避坑指南："图表场景优先使用短句文案，千万不要把大段正文塞进画面里，模型不是排版工人。"

每页文字量上限：
- **封面标题**：最多 2 行，每行不超过 12 字
- **副标题**：最多 1 行，不超过 15 字
- **卡片标题**：每张卡片不超过 6 字
- **卡片说明**：每张卡片不超过 20 字（1-2 句短句）
- **金句**：最多 2 行，每行不超过 10 字
- **互动气泡**：最多 2 行，每行不超过 12 字
- **标签**：每页 2-4 个，每个不超过 8 字

> ⚠️ 超过上限的文字会导致模型渲染错字、漏字、乱码。宁可文字少而精，不要多而乱。

---

## 八、完整 Prompt 示例（P2 分析页，内容主导型）

```
=== CANVAS ===
Chinese vertical Douyin article page, 3:4 ratio, 1773x2364 pixels.

=== STYLE ===
Richly detailed hand-drawn pencil sketch illustration with ink outlines on warm off-white paper (#FBFAF5). Cross-hatching, stippling, subtle ink bleed. Decorative corner flourishes. Thin double-line border. Premium sketchbook feeling.
ALL TEXT IS CHINESE HANDWRITTEN STYLE. Bold brush/marker hand-lettering for title. Casual pencil handwriting for subtitles and labels. NO formal printed fonts, NO English text, NO character names, NO version labels.
Pastel color palette: pale blue wash, pale peach wash, pale sage green wash, pale lavender wash. Ink-black #1B1B1B.

=== LAYOUT ===
LAYOUT MODE: CONTENT-DOMINANT. Content (cards/icons/text) is MAIN visual focus occupying 55-65% of page. Character is secondary accent.
TITLE AREA: top 15-20%. Large bold hand-lettered title "3个最应该记住的安全提醒" with wavy underline + warning triangle icon. Subtitle "交通·防溺水·防欺凌" with thin divider lines on both sides.
CONTENT AREA: middle 55-65%. EXACTLY THREE cards stacked vertically with small downward arrows and tiny stars between cards. Each card has folded top-right corner, double-line border, pastel wash background, large hand-drawn circled number on left side, small relevant icon next to title.
  Card 1 (pale blue): circled number 1, title "交通安全", text "未满12岁不骑自行车，未满16岁不骑电动车，过马路走斑马线", icon: inanimate traffic light and bicycle (NO face, NO character).
  Card 2 (pale peach): circled number 2, title "防溺水", text "不私自下水，遇到溺水立即呼救拨打110/120，不盲目下水施救", icon: inanimate lifebuoy (NO face, NO character).
  Card 3 (pale sage): circled number 3, title "防欺凌", text "遭遇欺负不隐忍，第一时间告知老师家长，同学友善相处", icon: inanimate shield (NO face, NO character).
CHARACTER AREA: ONLY 8-10% of page height at BOTTOM-LEFT corner. Character is small accent, NOT main subject. Area around character COMPLETELY BLANK.
DECORATION AREA: faint pencil grid in background, tiny doodle icons scattered in gaps (inanimate objects only: small helmet, tiny lifebuoy outline, shield outline — NO faces, NO characters), page number "02/05" at upper-left inside small circle (ONLY ONCE).

=== CHARACTER ===
=== MOZAI CHARACTER (strictly match reference image) ===
Round plump black teardrop creature (plump water drop shape, NOT slim, NOT elongated, NOT spherical). Ink-black body (#1B1B1B-ish) with hand-drawn ink texture, natural ink bleed and scribble strokes (NOT flat black). Small sprout on top with slightly curly thin stem + TWO light sage-green leaves (#A8C879, exactly two leaves). LARGE round eyes with big white eye whites and black pupils (pupils slightly asymmetrical). SMALL BLACK mouth (wavy line ~ shape, thinking expression, NOT red, NOT large). Exactly TWO thin black arms with small hands and exactly TWO short black legs with small feet. Small shadow under feet. Cute warm hand-drawn children's book illustration feel.
PAGE STATE: sitting cross-legged at bottom-left corner, holding small notebook in left hand, right hand resting on cheek (thinking pose). Eyes looking upward to the side with slightly furrowed brows. Mouth is wavy line ~ (thinking). Expression: thoughtful, concerned. Size: 8-10% of page height.
EXACTLY ONE character on page, never two or more. NO character inside any card, NO small character anywhere else, NO character in icons. NO blush, NO pink cheeks.

=== CONSTRAINTS ===
EXACTLY THREE cards. NO fourth card. Card 3 is DIFFERENT from Card 1 and 2. NO duplicate content.
Each tag ONLY ONCE. Page number "02/05" appears ONLY ONCE at upper-left. NO second page number.
The ONLY number on page is page number 02/05 and card numbers 1,2,3. NO random numbers, NO percentages.
TEXT MUST BE 过马路 (马 = 马字旁). NOT 过下路. TEXT MUST BE 拨打110 (拨 = 扌+发). NOT 技打.
NO $ sign, NO currency symbols. All icons contain NO text, NO numbers, NO letters.
Area around character COMPLETELY BLANK. NO text/icons/doodles within 1cm of character.
Character appearance strictly consistent with reference image.

=== AVOID ===
extra limbs, third arm, third leg, multi-hand multi-foot, all-black mouth hole, large mouth, exaggerated expression, pink blush, duplicate cards, duplicate tags, random numbers (50%, 10%, 32s, 28%), English text (MOZAI, SEEDLING, STOP), character inside cards or icons, face in icons, formal printed fonts, saturated colors, pure black background, yellow paper, giant title, heavy boxes, gibberish, childish cartoons, thick outlines, corporate template, shadows/gradients/neon, horizontal landscape, clean vector.
```

---

## 九、Prompt 生成工作流（Agent 执行步骤）

1. **填写 5 页差异化状态表**（第四节），确保每页眼睛/嘴型/动作/位置不同
2. **确定每页布局模式**（内容主导型 or 角色主导型），分析页/金句页必须内容主导
3. **按结构化协议组装 prompt**（第一节 7 字段块顺序），或用 JSON 模板（第二节）
4. **填入实战防坑约束**（第五节），根据页面类型选择适用的防坑条目
5. **检查文案克制原则**（第七节），每页文字量不超过上限
6. **传入人物卡 URL**，用 image_edit 工具生成
7. **生成后逐张下载放大校验**，发现问题单独重生成（在 prompt 中明确列出之前的错误）
