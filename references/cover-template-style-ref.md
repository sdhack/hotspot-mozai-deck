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
(dusty blue, muted orange, pale pink) floating loosely in empty wall areas; scattered tiny grey doodles of
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
top band. Cover composition: two small pastel label capsules at top CENTERED as a group (soft dusty-blue and
dusty-pink washes behind the labels); then two title lines, deep black, with a thin wavy hand-drawn underline
under the last line; then one short subtitle. The MIDDLE-LOWER band holds ONE concrete hand-drawn life scene:
[当页具体生活场景，必含：儿童严格背影/后脑勺（零面部特征）+ 主题道具组合 + 台灯或光源 + 桌面/床面小物件；
禁大人手、大人形象、正面人脸、品牌 logo、可读屏幕内容]。 No adult hand or adult figure anywhere. Mozai stands
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
- All numbers black and correctly written; the ONLY red element is a tiny alarm-clock outline on the scene
  showing black handwritten [时间数字]（无时间主题时改为：the ONLY red element is a single tiny
  warning/attention icon outline）。

=== CONSTRAINTS ===
P0: exactly the listed strings, each once; one character only; two leaves, two arms, two legs; pear body
proportion locked; the child strictly back view with zero facial features; no adult hand or adult figure; no
brand logos; screen blank; numbers black; red only on the single permitted red element. P1: title dominates the
hierarchy; scene readable and tidy; Mozai clear and crisp against the scene, never at the bottom edge or below
the capsules. P2: wall blotches, doodles, corner flourishes.

=== AVOID ===
copying the reference image's scene, layout or composition, a second character or extra limbs, wrong leaf
count, circle/ball/egg body or body-shape drift, the character placed at the bottom edge or below the capsules,
the child's face or profile from any angle, adult hands or adult figures, readable screen content or brand
logos, printed or typeset-looking text anywhere, thin faint sketchy body text, vivid or saturated colors, red
numbers, English or pinyin, watermark, wide empty paper margins, dark or gloomy overall tone.
```

## 落盘后处理链（与 backup-prompt-gpt2.md 相同，顺序固定）

`Contrast 1.04 → Color 0.72 → 白平衡迭代3轮至 TARGET(254, 251.5, 246.5) → 14×19 低频噪声暖斑（R ±0.6% / G ±0.35% / B ∓0.2%）→ JPEG quality 92 + FF D8 FF 头校验`。尺寸 1024×1365（raw 1086×1448），版本化文件名，禁覆盖上一版。

## 校准记录

- 2026-09-12 首次验收 pass：文字逐字正确（含小标签「攒钱中」放大核对）、孩子严格背影、红色仅闹钟、墨仔梨形排线+笔手贴合、画风迁移到位且未复制参考图构图。
- 底部关键词行两侧可能生成 ≡ 类装饰小符，非错字，可接受；若要求零多余符号，在 CONTENT 中加「no decorative glyphs around the keyword line」。
- 场景小标签（3 字以内）易被写成异体字，QA 时必须放大逐字核对。
