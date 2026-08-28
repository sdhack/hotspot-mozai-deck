# Prompt Template · 4页完整 Prompt 模板

使用方法：
1. 复制每页模板
2. 把 `{{变量}}` 替换为选题的具体内容
3. 把 style-lock 和 character-lock 的完整内容粘贴到每页 prompt 开头
4. 用 image_edit 工具，传入人物卡 URL，一次调用生成 4 张

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

Avoid: TWO characters, multiple characters, slim body, elongated body, pointed sharp top, tiny white-dot eyes, centered pupils, no mouth, black mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, giant title, heavy boxes, gibberish, watermark, childish cartoons, thick outlines, saturated colors, corporate template, shadows, gradients, neon, horizontal landscape, clean vector.
```

### 第2页：问题/分析（3卡片）

```
ST2-problems: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
Mouth expression: {{p2_mouth}}

Composition:
- Decorative corners, double-line border.
- Upper 10%: page number 02/04 handwritten upper-left ONLY. Centered title {{p2_title}} in bold hand-lettering with wavy underline. Subtitle {{p2_subtitle}} in pencil handwriting below.
- Below title: horizontal divider with swirls.
- Middle 60%: three stacked cards from top to bottom, each with folded corner and pastel wash, each with icon:
  Card 1 (top, pale blue wash): relevant icon, bold title {{p2_card1_title}}, sub-label {{p2_card1_desc}}. Small number 1.
  Card 2 (middle, pale peach wash): relevant icon, bold title {{p2_card2_title}}, sub-label {{p2_card2_desc}}. Small number 2.
  Card 3 (bottom, pale sage wash): relevant icon, bold title {{p2_card3_title}}, sub-label {{p2_card3_desc}}. Small number 3.
- SEEDLING CHARACTER stands at right side of card stack, {{p2_seedling_action}}. Fine hatching on body.
- Background: faint pencil grid, tiny doodle icons.

Required Chinese text (ALL HANDWRITTEN): 02/04, {{p2_title}}, {{p2_subtitle}}, {{p2_card1_title}}, {{p2_card1_desc}}, {{p2_card2_title}}, {{p2_card2_desc}}, {{p2_card3_title}}, {{p2_card3_desc}}

Avoid: TWO characters, multiple characters, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, smiling mouth, pressed mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, heavy boxes, gibberish, watermark, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, duplicate page number on right.
```

### 第3页：解决方案（3步骤 + 金句）

```
ST3-solutions: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
Mouth expression: {{p3_mouth}}

PAGE NUMBER: upper-left handwritten 03/04 ONLY.

Composition:
- Decorative corners, double-line border.
- Upper 10%: page number 03/04 upper-left. Centered title {{p3_title}} in bold hand-lettering with wavy underline. Subtitle {{p3_subtitle}} in pencil handwriting below.
- Middle 50%: three step cards stacked vertically, connected by downward arrows, each with checkmark icon:
  Step 1 (top, pale blue wash): relevant icon, bold title {{p3_step1_title}}, sub-label {{p3_step1_desc}}.
  Step 2 (middle, pale peach wash): relevant icon, bold title {{p3_step2_title}}, sub-label {{p3_step2_desc}}.
  Step 3 (bottom, pale sage wash): relevant icon, bold title {{p3_step3_title}}, sub-label {{p3_step3_desc}}.
- SEEDLING CHARACTER stands at right side of step stack, {{p3_seedling_action}}. Fine hatching on body. Ink splatter near feet.
- Lower 25%: detailed hand-drawn quote box centered, double-line border with ornamental corner brackets, no fill. Two lines of natural handwritten Chinese: first line {{p3_quote_line1}}, with small ink dot quote mark; second line {{p3_quote_line2}}. Ink dot divider between lines.
- Bottom: decorative corners. Faint pencil grid background.

Required Chinese text (ALL HANDWRITTEN, NO ENGLISH): 03/04, {{p3_title}}, {{p3_subtitle}}, {{p3_step1_title}}, {{p3_step1_desc}}, {{p3_step2_title}}, {{p3_step2_desc}}, {{p3_step3_title}}, {{p3_step3_desc}}, {{p3_quote_line1}}, {{p3_quote_line2}}

Avoid: TWO characters, multiple characters, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, smiling mouth, straight line mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, Latin chars, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, oversized objects, heavy boxes, gibberish, watermark, crowded, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, clean vector, percent sign in page number, color codes, duplicate page number on right, extra speech bubble near character.
```

### 第4页：落点（温暖场景 + 举牌 + 互动气泡）

```
ST4-takeaway: [在这里粘贴 style-lock 完整内容]

[在这里粘贴 character-lock 完整内容]
Mouth expression: {{p4_mouth}}

Composition (FIXED - NO extra hand, NO duplicate speech bubble, NO random numbers):
- Decorative corners all four, double-line border.
- Upper 10%: page number 04/04 handwritten UPPER-LEFT ONLY. Centered title {{p4_title}} in bold hand-lettering with wavy underline. Subtitle {{p4_subtitle}} in pencil handwriting below.
- Below title: small horizontal row of three pastel tags with wobbly hand-drawn borders and handwritten text: left pale blue {{p4_tag1}}, middle pale peach {{p4_tag2}}, right pale sage green {{p4_tag3}}. Decorative dots between tags.
- Middle 30%: a hand-drawn warm scene: {{p4_scene}}. Warm light rays. Large negative space with faint pencil grid, tiny doodle stars. NO extra hand, NO extra fingers.
- Lower 30%: SEEDLING CHARACTER stands at lower-center, holding a small detailed rectangular sign with both arms, sign has double-line border and reads {{p4_sign_text}} in bold hand-lettered ink. Character with fine hatching on body, upward-gazing friendly smile. Above character, ONE detailed hand-drawn speech bubble (double-line border, ornamental tail pointing to character, no fill) containing two lines of natural handwritten Chinese: first line {{p4_bubble_line1}}, second line smaller {{p4_bubble_line2}}. Decorative ink dots around bubble. NO duplicate bubble, NO second bubble.
- Bottom: decorative corners. Faint pencil grid throughout. NO random numbers, NO extra text.

Required Chinese text (ALL HANDWRITTEN, NO ENGLISH): 04/04, {{p4_title}}, {{p4_subtitle}}, {{p4_tag1}}, {{p4_tag2}}, {{p4_tag3}}, {{p4_sign_text}}, {{p4_bubble_line1}}, {{p4_bubble_line2}}

Avoid: TWO characters, multiple characters, slim body, elongated body, pointed sharp top, tiny eyes, centered pupils, O mouth, straight line mouth, pressed mouth, extra limbs, three leaves, one leaf, simple loop, formal fonts, English text, color codes, character names, version labels, MOZAI, SEEDLING, pure black background, yellow paper, oversized objects, heavy boxes, gibberish, watermark, crowded, childish cartoons, thick outlines, saturated colors, corporate template, horizontal landscape, clean vector, SECOND hand, extra fingers, hand pointing, duplicate page number on right, duplicate speech bubble, second bubble, random numbers.
```

---

## 调用方式

用 `image_edit` 工具，`request_list` 包含 4 个对象（每页一个），每个对象：
- `height`: 1440
- `width`: 1080
- `image_reference_url_list`: `["人物卡URL"]`
- `prompt`: 上面对应页的完整 prompt（已替换变量）

每页 prompt 前缀加唯一 tag（如 `ST1-cover:`、`ST2-problems:`）避免文件名冲突。
