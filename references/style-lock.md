# Style Lock · 通用风格锁

每个页面 prompt 必须包含以下风格描述，逐字复制，不可修改。

> v1.7.0 核心变更：**涂鸦是墨仔的天性**——手绘涂鸦背景（铅笔网格+散布涂鸦图标+交叉排线+墨点）不是可选排版优化，而是墨仔IP的核心视觉特质。墨仔是"一滴在纸上活过来的墨"，它走到哪里，哪里就有涂鸦。每页背景必须有手绘涂鸦质感，**禁止大面积纯白空白**。

---

## 完整风格锁（复制到每页 prompt 开头）

```
Chinese vertical Douyin article page, 3:4, 1080x1440. Richly detailed hand-drawn pencil sketch illustration with ink outlines on warm off-white paper. FAINT PENCIL GRID PATTERN across entire background. SCATTERED TINY DOODLE ICONS everywhere (stars, leaves, pencils, arrows, dots, sparkles — all inanimate). Cross-hatching patches, stippling, subtle ink bleed in background areas. Decorative corner flourishes. Thin double-line border. Premium sketchbook feeling. NO large empty white spaces — fill background with subtle hand-drawn texture and doodles.

ALL TEXT IS CHINESE HANDWRITTEN STYLE. Bold brush/marker hand-lettering for title. Casual pencil handwriting for subtitles and labels. NO formal printed fonts, NO English text, NO character names, NO version labels.
```

---

## 风格要素拆解

| 要素 | 描述 | 不可变 |
|---|---|---|
| 画布比例 | 3:4 竖版，1080x1440 | ✓ |
| 纸张 | warm off-white paper（暖白纸，非纯白，非黄纸） | ✓ |
| 线条 | hand-drawn pencil sketch + ink outlines（铅笔素描+墨水轮廓） | ✓ |
| 纹理 | cross-hatching（交叉排线）+ stippling（点画）+ subtle ink bleed（轻微墨水晕染） | ✓ |
| **涂鸦背景（v1.7.0核心）** | **FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching patches + ink dots，全页覆盖，禁止大面积纯白空白** | **✓** |
| 边框 | thin double-line border（细双线边框） | ✓ |
| 装饰角 | decorative corner flourishes（四角装饰花纹） | ✓ |
| 标题字体 | bold brush/marker hand-lettering（粗毛笔/马克笔手写体） | ✓ |
| 正文字体 | casual pencil handwriting（随意铅笔手写体） | ✓ |
| 禁止 | formal printed fonts（正式印刷字体）、English text（英文）、character names（角色名）、version labels（版本标签）、watermark（水印）、**large empty white spaces（大面积纯白空白，v1.7.0新增）** | ✓ |

---

## 封面特有元素

封面页额外包含：
- 顶部：tiny icon + 2个 pastel tags（热点标签 + 分类标签）
- 标题区：LARGE BOLD HAND-LETTERED title（两行），第二行 wavy underline（波浪下划线）
- 副标题：thin divider + subtitle in pencil handwriting
- 底部：3-4个 pastel tags（关键词标签）

## 正文页特有元素

正文页额外包含：
- 页码：page number handwritten upper-left ONLY（仅左上角，绝不右上角也出现），建议加 small circle 包围
- 标题：centered title in bold hand-lettering with wavy underline，建议加 small icon（铅笔/时钟/毕业帽）
- 副标题：subtitle in pencil handwriting below title，建议两侧加 thin divider lines
- 中间：semantic diagram area（语义图区域，每页不同）
- 底部（可选）：quote box（金句框，double-line border with ornamental corner brackets + small quote mark symbol）

---

## 排版优化指南（v1.2.0 新增，经过多轮迭代验证）

### 卡片优化（P2/P3）

经过多轮迭代，以下排版能显著提升视觉质量：

| 元素 | 描述 | 效果 |
|---|---|---|
| 折叠角 | folded top-right corner | 增加手绘质感 |
| 双线边框 | double-line border | 与整体边框风格统一 |
| Pastel 底色 | pale blue/peach/sage/lavender wash | 区分卡片层次 |
| 阴影 | subtle drop shadow | 增加立体感 |
| 大圆圈编号 | large hand-drawn circled number on left side | 比小数字更醒目，引导阅读顺序 |
| 卡片间箭头 | small downward arrows with tiny stars between cards | 引导阅读顺序 |
| 标题旁小图标 | small relevant icon next to title（key/calendar/chat bubble） | 增加视觉丰富度 |

### 时间线布局（P3 可选）

对于步骤/流程类内容，时间线布局比普通卡片堆叠更有设计感：

- 左侧画 wavy hand-drawn vertical line（波浪竖线）
- 圆圈编号连接到竖线（circled numbers connected to timeline）
- 步骤卡片延伸到右侧
- 时间线上加 downward arrows 和 sparkles（星星闪光）

### 标题区优化

| 元素 | 描述 |
|---|---|
| 页码圆圈 | page number with small circle around it |
| 标题小图标 | small icon next to title（铅笔图标/时钟图标/毕业帽图标） |
| 副标题装饰线 | thin divider lines on both sides of subtitle |

### 金句框优化

- 加 small quote mark symbol（引号符号）
- 周围加 decorative stars（装饰星星）
- ornamental corner brackets（装饰角括号）

### 标签优化

- wobbly hand-drawn double borders（手绘双线边框）
- 标签之间加 decorative dots and tiny stars（装饰点和小星星）

### 场景丰富度（P1/P4）

校园/生活场景建议包含以下元素以增加丰富度：
- 欢迎横幅（welcome banner）
- 大树（trees on both sides）
- 背景建筑带窗户（academic buildings with windows）
- 飞鸟（birds flying）
- 云朵（clouds）
- 落叶（scattered fallen leaves）
- 地图指示牌（campus map signboard）
- 阳光光线（warm light rays）

### 背景涂鸦（v1.7.0 从可选提升为核心）

> **涂鸦是墨仔的天性**——墨仔是"一滴在纸上活过来的墨"，它走到哪里，哪里就有涂鸦。每页背景必须有手绘涂鸦质感，禁止大面积纯白空白。

- **FAINT PENCIL GRID**（淡铅笔网格，全页覆盖，20-30%透明度，不突兀）
- **SCATTERED TINY DOODLE ICONS**（散布的小涂鸦图标，必须是无生命物体：星星、叶子、铅笔、箭头、圆点、闪光、音符，不能有角色/脸）
- **cross-hatching patches**（交叉排色块，在背景空白区域增加纹理层次）
- **ink dots and splatters**（墨点和墨溅，增加手绘质感）
- **tiny stars and sparkles**（小星星和闪光）

> ⚠️ 涂鸦背景必须是**淡的、不抢主体的**——网格20-30%透明度，涂鸦图标小而分散，交叉排线稀疏。目的是消除大面积纯白空白，增加手绘质感，而不是让背景变得拥挤杂乱。

---

## 配色（pastel 标签）

| 用途 | 颜色 |
|---|---|
| 标签1（冷色） | pale blue wash（淡蓝） |
| 标签2（暖色） | pale peach wash（淡桃） |
| 标签3（中性） | pale sage green wash（淡鼠尾草绿） |
| 标签4（可选） | pale lavender wash（淡薰衣草紫） |
| 墨水 | ink-black (deep black, NOT pure black, NOT dark gray) |
| 纸张 | warm off-white (NOT pure white, NOT yellow, NOT gray) |

> ⚠️ **v1.7.2 颜色代码防护**：prompt中禁止使用任何十六进制颜色代码（如 #FBFAF5、#1B1B1B、#A8C879），seedream模型会把它们渲染成画面文字乱码。必须用文字描述颜色。此表中的颜色名称仅供参考，写入prompt时用文字描述而非代码。

---

## 禁止元素（必须在 Avoid 列表明确列出）

- formal printed fonts（正式印刷字体）
- English text（英文，包括 STOP、MOZAI、SEEDLING 等）
- character names（角色名）
- version labels（版本标签，如 v2.0）
- watermark（水印）
- random numbers（随机数字，如 50%、10%、32s、28%）
- time labels（时间标签）
- statistics（统计数据）
- pure black background（纯黑背景）
- yellow paper（黄纸）
- giant title（超大标题）
- heavy boxes（厚重方框）
- gibberish（乱码）
- childish cartoons（幼稚卡通）
- thick outlines（粗轮廓）
- saturated colors（饱和色彩）
- corporate template（企业模板风格）
- shadows/gradients/neon（阴影/渐变/霓虹）
- horizontal landscape（横版）
- clean vector（干净矢量风格）
- **LARGE EMPTY WHITE SPACES（大面积纯白空白，v1.7.0新增）**
- **flat plain background（扁平无纹理背景，v1.7.0新增）**
- **hex color codes（十六进制颜色代码，v1.7.2新增）**——如 #FBFAF5、#1B1B1B、#A8C879，会被渲染成画面文字乱码
- **pound sign codes（#号后跟字母数字，v1.7.2新增）**

---

## v1.6.0 新增：材质与光影强化（借鉴 awesome-gpt-image-2）

> awesome-gpt-image-2 避坑指南："材质和光影是灵魂——一定要堆叠材质（如'磨砂质感'）和灯光（如'轮廓光'）的关键词，商品图一旦没有光影，立刻变成地摊货。"

手绘风格同样需要精细的材质和光影描述，否则画面会扁平、无层次。

### 纸张材质拆解

```
PAPER TEXTURE: warm off-white paper with subtle fiber texture.
Paper has slight unevenness — not perfectly flat, has gentle variations in tone (some areas slightly warmer, some slightly cooler).
Faint pencil grid lines visible in background (very light, 20-30% opacity, NOT prominent).
Paper edges within border have slight natural deckle edge feel (NOT clean cut).
NO pure white, NO yellow paper, NO gray paper.
NO hex color codes in prompt — use text descriptions only.
```

### 墨水材质拆解

```
INK TEXTURE: hand-drawn ink outlines with natural ink bleed at edges (slight softening, NOT sharp vector lines).
Ink has variable line weight — some strokes thicker (pressure), some thinner (light touch).
Cross-hatching lines create shading (parallel lines at 45° and 90°, varying density).
Stippling dots create texture (small dots, varying density, NOT uniform).
Subtle ink wash effects in some areas (diluted ink creates soft gray tones).
Ink color is deep ink-black (NOT pure black, NOT dark gray).
NO thick outlines (uniform 2px+ lines), NO clean vector edges, NO flat color fills.
NO hex color codes in prompt — use text descriptions only.
```

### 光影描述（手绘风格适用）

```
LIGHTING: soft, diffused overhead lighting (like natural daylight through a window).
Subtle shadows under cards and character (soft gray, 20-30% opacity, NOT hard black shadows).
Cards have slight drop shadow (offset 2-3px down-right, soft blur, creates layered feel).
Character has small shadow under feet (soft ellipse, grounds character on page).
NO harsh directional light, NO strong highlights, NO neon glow, NO gradient shadows.
NO 3D rendering lighting — this is 2D hand-drawn illustration, lighting is subtle and flat.
```

### Pastel 底色材质

```
PASTEL WASH: watercolor-like soft wash on card backgrounds.
Wash has uneven edges — natural watercolor bleed effect (NOT clean geometric fill).
Wash opacity 30-40% (light, transparent, paper texture visible through it).
Color variations within wash — some areas slightly more saturated, some lighter.
NO flat solid color fill, NO gradient, NO opaque background.
Colors (use text descriptions, NO hex codes): pale blue, pale peach, pale sage, pale lavender.
NO hex color codes in prompt — use text descriptions only.
```

---

## v1.6.0 新增：信息层级百分比控制

借鉴 awesome-gpt-image-2 的「信息层级」理念，每页必须明确各区域占比，避免模型随意分配空间。

### 内容主导型页面层级（P2/P3/P4）

```
PAGE LAYOUT (percentages of total page height):
- Top margin + page number: 3-5%
- Title area (title + subtitle + wavy underline): 15-20%
- Content area (cards/icons/text — MAIN FOCUS): 55-65%
- Character area (small corner accent): 8-10%
- Bottom margin + tags: 5-8%
- Total: 100%

Content area must be the LARGEST zone. Character must NOT exceed 10%.
Cards within content area: each card 25-30% of content area height, with 5-8% gap between cards.
```

### 角色主导型页面层级（P1 封面/P5 互动，可选）

```
PAGE LAYOUT (percentages of total page height):
- Top margin + tags: 5-8%
- Title area (large title + subtitle): 20-25%
- Character area (main subject): 25-35%
- Content area (small cards/icons around character): 20-25%
- Bottom margin + tags: 5-8%
- Total: 100%

Character is the main visual focus but title must still be prominent.
Content arranged around character, NOT overlapping character's face/body.
```

### 层级检查（生成后必做）

逐张放大校验时，用目测估算各区域占比：
- [ ] 内容主导型页面：内容区是否 ≥55%？角色区是否 ≤10%？
- [ ] 角色主导型页面：角色区是否 ≤35%？标题区是否 ≥20%？
- [ ] 标题是否清晰可读，不被其他元素遮挡？
- [ ] 卡片之间是否有足够间距（不拥挤）？
- [ ] 角色周围是否有空白（不被文字/图标包围）？
- [ ] **背景是否有涂鸦纹理（v1.7.0新增）？是否有大面积纯白空白？**

---

## v1.6.0 新增：seedream_5.0_pro 风格适配

针对 seedream_5.0_pro 模型的特点，风格描述可以更精细：

```
FOR SEEDREAM_5.0_PRO (1773x2364):
- Add more texture detail: "richly detailed", "intricate cross-hatching", "fine stippling"
- Emphasize hand-drawn quality: "authentic sketchbook feel", "artist's notebook page"
- Add subtle paper details: "paper grain visible", "slight paper texture"
- The model handles fine detail better, so you can specify smaller decorative elements
- Text rendering is more accurate, but still keep text short (see 文案克制原则)
- **v1.7.0新增：强调涂鸦背景**——"FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching patches, NO large empty white spaces"
```

FOR seedream_4.5 (1080x1440):
- Simplify texture description: "hand-drawn sketch", "ink outlines"
- Reduce decorative elements to avoid clutter
- Keep text even shorter to reduce rendering errors

---

## 原始画风不可变（v1.8.0 核心约束）

> **触发**：用户强调"原始画风要求不能变"（尤其在做封面强钩子改造、场景叙事型切换后）。任何对标题、画面、布局的改动，都不得弱化本技能定义的原始画风。这是比"内容改动"更高的优先级——内容可以换，画风必须锁死。

### 封面原始元素清单（改钩子/改画面时必须逐项核对，缺一项即重生成）

| # | 元素 | 必须保持 |
|---|---|---|
| 1 | 双线边框 | THIN DOUBLE-LINE BORDER around whole page |
| 2 | 四角装饰花纹 | DECORATIVE CORNER FLOURISHES in all four corners |
| 3 | 标题波浪下划线 | WAVY UNDERLINE under title line 2 |
| 4 | 顶部标签 | 2 个 pastel tags（wobbly double-border，如 #家长群 #教育公平） |
| 5 | 底部标签 | 3-4 个 pastel tags + 装饰点（如 #家校关系 #开学季 #教育） |
| 6 | 涂鸦背景 | FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching + ink dots，无大面积空白 |
| 7 | 纸张/墨水 | warm off-white paper + ink-black（非纯黑/非灰）+ 手绘铅笔+墨水轮廓 |
| 8 | 墨仔形象 | 圆胖黑泪滴+小芽微卷茎双叶+大眼+小黑嘴+细四肢+手绘墨迹（strictly match 人物卡） |

### 正文页原始元素清单

| # | 元素 | 必须保持 |
|---|---|---|
| 1 | 页码 | upper-left ONLY inside small circle |
| 2 | 标题 | centered bold hand-lettering + wavy underline |
| 3 | 涂鸦背景 | 同封面（铅笔网格+散布涂鸦+交叉排线+墨点，无大面积空白） |
| 4 | 边框/装饰角 | 细双线边框+四角装饰花纹 |
| 5 | 手写字体 | 全中文手写，无英文/角色名/版本标签/印刷体 |

### 实战教训（为什么必须锁定）

- 封面强钩子改造（v1.8.0 实战）曾把标题改成"一条自我介绍/让家长群安静了"、画面聚焦手机消息，但 v2 弱化了原始画风（边框/装饰角/标签/波浪下划线被简化），用户反馈"原始画风要求不能变"。
- 修复（v3）：在保留强钩子标题与画面冲突的同时，**逐项恢复**双线边框+四角装饰+波浪下划线+顶部底部 pastel 标签+铅笔网格涂鸦，才通过。
- **结论**：钩子/画面可以改，原始画风元素一个都不能少。生成前把上表清单写进 prompt，生成后逐项核对。
