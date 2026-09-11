# gpt-image-2 备用出图提示词母版（第二套视觉体系，无参考图）

本文件是 v1.9 母版之外的**第二套完整出图提示词**：不依赖任何参考图，纯 Prompt 即可生成"浓黑排线墨仔 + 近白暖纸手账卡"风格。2026-09-11 经「家长群月饼团购」一套 5 图逐轮校准定稿。适用于：v1.9 淡彩风格之外的加重版、或需要更强手绘故事感时的备份选择。

## 使用方式

覆盖式模板：`CANVAS → STYLE → CHARACTER → LAYOUT → CONTENT → CONSTRAINTS → AVOID` 顺序组装，`[...]` 为当页填充位。配合第 5 节落盘后处理链使用。

## CANVAS（逐页固定）

```text
True portrait 3:4 canvas. A double-line hand-drawn black border runs about 30px inside the canvas edges on all
four sides, with dense vine-leaf, bow and star-dot corner flourishes climbing along the corners and sides,
drawn with bold wobbly strokes. The composition fills the frame; outer paper margins stay thin and even.
```

## STYLE（逐页固定）

```text
Cozy hand-drawn journal storybook card on an off-white, near-white warm paper with only a very subtle creamy
tint (never yellow, never beige), covered with sparse subtle fiber speckles and a VERY FAINT hand-drawn square
grid pattern across the entire background: thin even light-grey pencil lines forming small squares, like fine
graph paper — visible on close look, extremely subtle at first glance. All linework is bold confident black
hand-drawn ink with naturally wobbly sketch strokes and heavy cross-hatched shading. Colors are ONLY a
restrained muted dusty palette — dusty pink, pale sage, cream yellow, pale lavender at low saturation on the
white paper; no vivid, bright, neon or highly saturated color anywhere (no strong red, orange, magenta or golden
yellow); every colored element stays quiet and gentle. A few tiny scattered doodles (stars, hearts, sparkles,
leaves) fill empty areas away from text.
```

## CHARACTER 锚点（逐页固定 + 当页动作）

```text
Exactly one Mozai: a plump pear/teardrop-shaped black ink-drop creature, body height 1.1-1.2 times its width,
round heavy bottom tapering to a curled pointed top bearing a thin sprout with exactly two sage-green leaves;
big white oval eyes with black pupils, subtle expressive eyebrows, a small black mouth (never red); exactly two
thin arms and two short legs; no blush, no clothes; the whole body filled with dense graphite-like scribble
cross-hatching. This body proportion is identical on every page of the set. [当页位置/占比/表情/动作。表情需
友善时显式写 friendly warm smile, relaxed kind eyebrows — 否则易画成怒眉。]
```

## LAYOUT / 场景规则

```text
- CLEAR TITLE-BODY HIERARCHY: the TITLE is the single dominant text element — largest and heaviest, deep black,
  top band. Body cards, bubbles and capsules are clearly subordinate (about half the title size or less).
- Scene props (gift-box, chat bubbles with only EMPTY circles and squiggle lines — never avatar silhouettes or
  person shapes, crescent moon, osmanthus branches, pencil, notebook) are painted in the SAME muted hand-painted
  watercolor as the character's world: clearly colored, soft dusty tones — never ghost-pale, never vivid,
  slightly subordinate to the black character.
- Cover: two small pastel label capsules at top CENTERED as a group; up to two title lines with a wavy
  hand-drawn underline under the last line; one short subtitle; 3-4 keyword capsules near the bottom.
- Inner pages: page number 「NN/05」 in a small hand-drawn circle at the top-left; sticky-note style cards or
  speech bubbles with small pastel circular icons; vary card/bubble alignment between pages.
```

## CONTENT（逐字文本 + 文字三锁）

```text
Render this Chinese text exactly, character for character: [逐条引号列出]
- ALL TEXT IS HANDWRITTEN: every piece of text — title, body, page number, capsule labels, card numbers, prop
  labels — is natural irregular Chinese handwriting (uneven sizes, slightly tilted strokes, natural wiggle).
  NEVER a printed, typeset, computer-font or label-maker look.
- Body text is LARGE, DARK, DEEP-BLACK with medium-thick strokes, crisp and readable at phone-screen size.
- All numbers black and correctly written; avoid error-prone characters at copywriting stage (「尴」被连续写错，
  改用同义措辞规避)。
```

## AVOID 母版

```text
a second character or extra limbs, wrong leaf count, circle/ball/egg body or body-shape drift between pages,
printed or typeset-looking text anywhere, thin faint sketchy body text, vivid or saturated colors, avatar
silhouettes or faces inside chat bubbles, angry eyebrows unless intended, red numbers, English or pinyin,
watermark, wide empty paper margins
```

## 落盘后处理链（PIL，顺序固定，与 Prompt 同时生效）

```python
im = ImageEnhance.Contrast(im).enhance(1.04)     # 提对比去灰
im = ImageEnhance.Color(im).enhance(0.72)        # 全局降饱和定稿值
TARGET = np.array([254.0, 251.5, 246.5])         # 近白暖纸目标色
for _ in range(3):                               # 迭代白平衡：p60 高亮像素测纸色，逐通道缩放
    lum = a.mean(axis=2); sel = a[lum > np.percentile(lum, 60)]
    a = np.clip(a * (TARGET / np.clip(sel.mean(0), 1, 255)), 0, 255)
# 不均匀暖斑：14x19 低频噪声双三次放大为暖色场，R ±0.6% / G ±0.35% / B ∓0.2%
# —— "稍微暖"必须是深浅不一的斑驳，严禁整页平涂暖色（用户明确否决过匀黄）
im.save(path, "JPEG", quality=92)                # 一律 JPEG，FF D8 FF 头校验
```

## 校准史（勿回退）

- 纸色 Prompt 写 warm cream/#f3ead6 会带黄 → 只写 near-white, never yellow；
- 暖色偏 R×1.015/B×0.98 叠加发黄 → 弃用，改白平衡+暖斑；
- Color 0.88→0.85→0.80→0.72 逐轮收敛（用户"再收敛一点"）；
- 轻铅笔细线正文小屏发糊 → 正文清晰锁；
- 未约束表情时"坚定点头"被画成怒眉 → 友善表情需显式；
- 场景太素（ghost-pale）与太艳（vivid）各被打回一次 → 统一灰调水彩锁；
- 生成文件名必须版本化（时间戳），严禁覆盖上一版；接口有日配额（429），批量脚本按页重跑。
