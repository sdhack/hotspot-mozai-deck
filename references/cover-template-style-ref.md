# 封面固定模版：学风格不学构图（2026-09-12 用户定稿）

本文件是主题 3「新手机今晚发布 / 孩子已经在攒钱了」封面（`01-封面-style-0912.jpg`）验收通过后固化的**封面出图模版**。定位：备份母版 `backup-prompt-gpt2.md` 的封面专用变体——**只从用户提供的参考图学习风格/画风/字体，绝不复制其场景、构图与版式**。

## 适用条件

- 用户点名「固定封面模版」「学风格封面」「只学风格画风字体」时，本模版作为该次封面的完整视觉锁。
- 与其他模版冲突时：封面结构规则（角色位置锁、标签胶囊、标题层级）以本模版为准；角色身份、文字准确性、内容安全不变量仍按 SKILL.md 全局执行。

## 双参考输入（gpt-image-2 edits 通道）

| 顺序 | 图片 | 职责 |
|---|---|---|
| 1 | 用户提供或指定的画风参考图（定稿来源：`e:\Users\Administrator\Documents\DOUBAO墨仔日记260905\秋季传染病合集\01_封面_秋季传染病合集.jpg`） | 只提供纸感、墙面粉理、淡彩晕染、涂鸦语言、边框与手写字感 |
| 2 | `assets/mozai-ip-sheet-4k.jpg` | 墨仔外观唯一真值（仅外观，禁复刻设定卡版式） |

Prompt 开头声明（逐字）：

```text
The FIRST attached image is a style reference: learn ONLY its art style, texture and lettering feel.
The SECOND attached image is the character appearance truth (appearance only, never copy its sheet
layout or poses). Replace everything with the BRAND NEW cover described below — keep no text,
layout, page number or scene from either image.
```

## 模版正文（[...] 为当页填充位；未标注处逐字保留）

```text
=== CANVAS ===
True portrait 3:4 canvas. A thin, elegant single hand-drawn black border runs about 30px inside the canvas
edges on all four sides, with delicate vine-leaf and star-dot corner flourishes like fine pen doodles. The
composition fills the frame; outer paper margins stay thin and even.

=== STYLE ===
Learn ONLY the art style, texture and lettering feel of the attached style reference — do NOT copy its scene,
composition, objects or layout. Cozy hand-drawn journal card on warm cream paper (never yellow, never beige)
with a very faint square grid; soft grey pencil cross-hatch shading with gentle pastel watercolor blotches
(dusty blue, pale sage green, cream — NO dusty pink, NO orange/salmon per the 2026-09-15 no-red-orange lock) floating loosely in empty wall areas; scattered tiny grey doodles of
stars, hearts, pencils, leaves and sparkles; a muted, low-saturation watercolor world; no vivid, bright, neon
or highly saturated color anywhere, no strong red, orange, magenta or golden yellow. All linework is confident
black hand-drawn ink with wobbly sketch strokes and cross-hatched shading. Lettering style learned from the
reference: all text is natural irregular Chinese handwriting with rounded confident marker strokes, slightly
tilted and uneven — NEVER printed, typeset or computer-font. Title lines are the largest, deepest black
elements with medium-thick crisp strokes; smaller text stays clearly subordinate.

=== CHARACTER ===
Exactly one Mozai: a plump pear/teardrop-shaped black ink-drop creature, body height 1.1-1.2 times its width,
round heavy bottom tapering to a curled pointed top bearing a thin sprout with exactly two sage-green leaves;
big white oval eyes with black pupils, subtle expressive eyebrows, a small black mouth (never red); exactly two
thin arms and two short legs; no blush, no clothes; whole body filled with dense graphite-like scribble
cross-hatching. This body proportion is identical across the set. Position: standing at the [LEFT/RIGHT] edge
of the desk scene, about 15% of the page height tall, friendly warm smile with relaxed kind eyebrows, leaning
slightly toward the scene while holding a short black marker in his right hand, fingers clearly wrapped around
the barrel. [表情与动作按当页主题替换；默认友善，需担忧时写 worried caring expression with soft raised eyebrows。]

=== LAYOUT ===
CLEAR TITLE-BODY HIERARCHY: the TITLE is the single dominant text element — largest and heaviest, deep black,
top band. Cover composition: two small pastel label capsules at top CENTERED as a group (washes only dusty-blue /
sage-green / cream — no pink, no orange); then two title lines in STAGGERED rhythm per the 2026-09-15 rule:
line 1 starts at the left margin, line 2 indented one character and slightly larger, key word(s) carrying a
soft pale-sage watercolor halo, deep black, with a thin wavy hand-drawn underline
under the last line; then one short subtitle. The MIDDLE-LOWER band holds ONE concrete hand-drawn life scene:
[当页具体生活场景，必含：主题人物（按 2026-09-15 表情口径：孩子可回头露正脸，表情走"忐忑带期待"；家长可正面入场，表情温和迟疑，双人对视优先；
两人视线共同指向故事焦点）+ 主题道具组合 + 台灯或光源 + 桌面/床面小物件；
禁哭脸/惊恐表情、品牌 logo、可读屏幕内容]。 人物动作链按「封面人物动作逻辑锁」执行。Mozai stands
at the scene's edge, never at the bottom edge or below the capsules. The BOTTOM band keeps clean quiet paper
with one short keyword line and 3-4 slim capsules in a row, plus tiny grey doodles.

=== CONTENT ===
Render this Chinese text exactly, character for character, each string exactly once:
- Top capsule 1: [标签1，与底部胶囊不重复]
- Top capsule 2: [标签2]
- Title line 1: [第一行标题]
- Title line 2: [第二行标题]
- Thin wavy underline under title line 2
- Subtitle: [一句副题]
- [场景小标签（如 攒钱中），可选项]
- Bottom keyword line: [一句关键词行]
- Bottom capsule 1: [胶囊1] / Bottom capsule 2: [胶囊2] / Bottom capsule 3: [胶囊3]
- All numbers black and correctly written; red/orange/salmon are FORBIDDEN anywhere in the image
  （2026-09-15 全套禁红橙锁：旧"单一红色元素"默认取消；确需警示色时用尘蓝或灰色图标替代）。

=== CONSTRAINTS ===
P0: exactly the listed strings, each once; one character only; two leaves, two arms, two legs; pear body
proportion locked; child/parent faces only in the approved gentle expression range (worried-hopeful child,
hesitant-gentle parent, never crying or terrified); brand logos; screen blank; numbers black; NO red,
orange or salmon anywhere（2026-09-15）. P1: title dominates the
hierarchy with the staggered two-line layout and key-word halo（排版审美验收：错位+底晕+层级缺一即重做）; scene readable and tidy; Mozai clear and crisp against the scene, never at the bottom edge or below
the capsules. P2: wall blotches, doodles, corner flourishes.

=== AVOID ===
copying the reference image's scene, layout or composition, a second character or extra limbs, wrong leaf
count, circle/ball/egg body or body-shape drift, the character placed at the bottom edge or below the capsules,
crying, terrified or distressed faces on child or parent, rigid flat aligned title rows without the staggered
rhythm, readable screen content or brand
logos, printed or typeset-looking text anywhere, thin faint sketchy body text, vivid or saturated colors, red
or orange elements anywhere, English or pinyin, watermark, wide empty paper margins, dark or gloomy overall tone.
```

## 落盘后处理链（与 backup-prompt-gpt2.md 相同，顺序固定）

`Contrast 1.04 → Color 0.72 → 白平衡迭代3轮至 TARGET(254, 251.5, 246.5) → 14×19 低频噪声暖斑（R ±0.6% / G ±0.35% / B ∓0.2%）→ JPEG quality 92 + FF D8 FF 头校验`。尺寸 1024×1365（raw 1086×1448），版本化文件名，禁覆盖上一版。

## 校准记录

- 2026-09-12 首次验收 pass：文字逐字正确（含小标签「攒钱中」放大核对）、孩子严格背影、红色仅闹钟、墨仔梨形排线+笔手贴合、画风迁移到位且未复制参考图构图。
- 底部关键词行两侧可能生成 ≡ 类装饰小符，非错字，可接受；若要求零多余符号，在 CONTENT 中加「no decorative glyphs around the keyword line」。
- 场景小标签（3 字以内）易被写成异体字，QA 时必须放大逐字核对。
- 2026-09-12 补充：①标题含必要产品名（如 iPhone18）时，在 CONTENT 中声明「the string XXX is the ONLY permitted Latin text in the whole image」，AVOID 同步改为「no English or pinyin except XXX」；②标题逐字锁：禁止自动补句号（曾在「…三道锁」后生成「。」）；③墨仔肢体写入手足硬锁（恰好两臂两腿，放大清点）；④持笔可选——封面书桌场景可保留马克笔，其他页面按动作自然决定；⑤波浪线固定画在标题末行下。
- 2026-09-14 补充（网安周封面 v1–v4 四轮迭代沉淀）：①「儿童严格背影/屏幕空白/无大人形象」三项降级为按文案灵活调整的软约束（底线：无可读屏幕文字、无品牌、不渲染恐惧）；大人可入场且**不限于剪影或背影**，可按文案画出动作、姿态与面部，同受动作逻辑锁约束；②封面必须有故事性瞬间（谁/在哪/正在发生什么），非静态摆拍；③人物动作逻辑锁：姿势必须是完整自然动作链，v3 的「身体朝门却双手反扣身后椅背」被用户打回，v4 改为「STOOD UP from the chair, FACING the doorway in profile, feet flat, arms at sides」一次通过——写动作就写最简单可读的完整动作，并附 no twisted necks, no impossible body rotations 禁词；④接口失败模式再次验证：真实超时后连续 400 拒绝窗口，冷却 90–120 秒后单发重试即成功。
- 2026-09-15 定稿（「放学独自回家」封面 v1–v3 三轮迭代沉淀，用户确认固化）：①封面标题错位排版锁——两行标题第一行顶左边距、第二行缩进一字且略大，重点词加淡鼠尾草绿水彩底晕，波浪线在末行下，QA 加排版审美验收；②人物表情口径——孩子回头露正脸"忐忑带期待"、家长正面"温和迟疑半抬手"，双人对视为优先构图，禁哭脸惊恐；③全套禁红橙锁——胶囊底晕只用尘蓝/鼠尾草绿/奶白，树叶只用灰绿，v1 因粉色胶囊+橙红树叶被打回，v2 收紧后通过；④教训：模型会把"淡粉"当合规色，禁令必须写 NO red, NO orange, NO salmon 并逐处列举可用色。
