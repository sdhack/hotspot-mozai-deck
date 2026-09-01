# Character Lock · 墨仔(Mozai) 角色锁

从用户上传的墨仔人物卡（`assets/seedling-character-sheet.png`）提取的精确角色描述。每个页面 prompt 必须包含核心形象描述，逐字复制。

> v1.5.0 更新：基于2026-09-01课后延时服务选题多轮迭代实战经验。关键变更：新增「用户硬约束」章节（2手2脚绝对不能多、每页表情/眼睛/嘴型/动作必须差异化、张嘴拟人化含舌头、嘴不能太大表情不能太夸张、外观一致性）；新增「嘴型拟人化」详细描述；表情库增强差异化要求；故障排除新增嘴型全黑/表情单一/多手多脚修复方法。

---

## ⚠️ 用户硬约束（v1.5.0 新增，必须严格遵守）

以下约束来自用户多轮迭代中反复强调的硬性要求，**优先级高于一切其他设计考量**：

| # | 约束 | 说明 | 违反后果 |
|---|---|---|---|
| H1 | **严格2手2脚** | 墨仔必须恰好2条手臂+2条腿，多手多脚绝对不能出现 | 直接重生成，不可交付 |
| H2 | **每页表情/眼睛/嘴型/动作必须大幅差异化** | 4-6页中，墨仔的眼睛状态、嘴型、身体动作必须每页不同，不能单一重复 | 重生成差异化状态 |
| H3 | **张嘴时嘴必须拟人化** | 墨仔张嘴（O形嘴/惊讶嘴）时，嘴内部必须可见舌头/牙齿/口腔层次，不能是全黑洞 | 重生成，prompt强调含粉舌 |
| H4 | **嘴不能太大，表情不能太夸张** | 所有嘴型都是小比例（SMALL），表情克制不夸张，避免大嘴笑/大张嘴 | 重生成，强调SMALL mouth |
| H5 | **墨仔人物外观一致性** | 每页墨仔的泪滴形身体、大眼风格、小嘴、头顶小芽+两片叶、手绘墨迹质感必须完全一致 | 重生成，强化角色锁描述 |
| H6 | **无红晕** | 墨仔脸部不能有粉色红晕/腮红，脸部是干净的黑色墨迹 | 重生成，强调NO blush |

> **实战验证**：H1-H6 在2026-09-01课后延时服务选题中经过10+轮迭代验证，是用户最核心的硬性要求。每次生成前必须逐条核对。

---

## 嘴型拟人化规范（v1.5.0 新增）

墨仔张嘴时（curious O / surprised O / confused small 等），嘴部必须拟人化，不能是全黑洞：

```
SMALL open oval mouth (curious "oh?"). Black outline. 
INSIDE: visible PINK/RED TONGUE at bottom of mouth. 
NOT all-black hole. NOT large. Small and subtle.
```

**关键要点**：
- 嘴是**小比例**（SMALL），不是大嘴
- 嘴内部有**粉红色舌头**（PINK/RED TONGUE），不是全黑
- 舌头在嘴的**底部**（at bottom），自然位置
- 适用于所有张嘴表情：curious O、surprised O、confused small、互动提问页

**避免**：
- `ALL-BLACK mouth`（全黑洞）
- `large mouth` / `wide mouth`（大嘴）
- `mouth without tongue`（无舌头）
- `mouth with teeth only`（只有牙齿没有舌头，墨仔风格更适合舌头）

---

## 墨仔 IP 设定（参考用，不写入 prompt）

| 项目 | 内容 |
|---|---|
| 名称 | 墨仔 (Mozai) |
| 昵称 | 小墨、墨墨、墨团子 |
| 标语 | 一滴在纸上活过来的墨 |
| 生日 | 2026年8月26日 |
| 星座 | 处女座 |
| 身份 | 一滴在纸上活过来的墨 |
| 身高 | 一个墨滴的高度（可伸缩） |
| 性格 | 好奇、善良、爱涂鸦，还有一点小调皮；好奇却不失善良 |
| 爱好 | 涂鸦、发呆、观察、想象 |
| 能力 | 感知情绪、激发灵感、点亮心情 |
| 口头禅 | "哇哦，今天又有新想法！" |
| 相信的话 | 只要想象，就能把世界点亮 |
| 小秘密 | 爱听同学的心事，开心的时候会用小墨点跳小舞蹈 |
| 目标 | 用想象点亮世界，让平凡的日子变有趣 |

**故事背景**：墨仔原本只是一滴普通的墨，某天在纸上意外醒来，它发现这个世界充满色彩与故事，于是决定从小墨点开始，探索奇妙的校园。在学校的每一天，墨仔都会陪伴同学，记录他们的灵感与情绪，一点一点，让生活变得更温暖。

---

## 完整角色锁（复制到每页 prompt 核心形象部分）

```
=== MOZAI CHARACTER (strictly match reference image) ===
CRITICAL: Match reference EXACTLY. Round plump black teardrop creature (plump water drop shape, NOT slim, NOT elongated, NOT spherical). Ink-black body (#1B1B1B-ish) with hand-drawn ink texture, natural ink bleed and scribble strokes (NOT flat black, has textured ink strokes). Small sprout on top with slightly curly thin stem + TWO light sage-green leaves (芽叶绿 #A8C879, exactly two leaves, not one, not three). LARGE round eyes with big white eye whites and black pupils (pupils often slightly asymmetrical - one eye may look slightly larger or offset, expressive). SMALL BLACK/DARK mouth (simple line or curve, expression varies per page, NOT red). Exactly TWO thin black arms with small hands and exactly TWO short black legs with small feet. Small shadow under feet. Cute warm hand-drawn children's book illustration feel. EXACTLY ONE character on page, never two or more. The character is ONLY at [position], doing [action]. NO character inside any card, NO small character anywhere else, NO character in icons. All icons are INANIMATE objects (NO face, NO character, NO teardrop shape).
```

> ⚠️ 使用时把 `[position]` 和 `[action]` 替换为具体的位置和动作。

---

## 角色要素拆解

| 要素 | 描述 | 常见错误（必须避免） |
|---|---|---|
| 身体形状 | round plump black teardrop（圆胖黑色泪滴/水滴形） | slim/elongated（修长）、spherical（球形）、pointed top（尖顶） |
| 身体颜色 | ink-black 墨黑 (#1B1B1B-ish) | 纯黑 #000、深灰、其他颜色 |
| 身体质感 | hand-drawn ink texture, natural ink bleed, scribble strokes（手绘墨迹感，自然墨迹晕染，涂鸦笔触） | flat black（纯平黑）、shiny（发光）、hard silhouette（硬剪影）、pencil/crayon only（仅铅笔蜡笔，缺墨迹感） |
| 头顶芽 | small sprout with slightly curly thin stem + TWO light sage-green leaves（小芽+微卷细茎+两片芽叶绿） | spiral coil loop（螺旋线圈）、straight stem（直茎）、no sprout（无芽） |
| 叶子 | TWO light sage-green leaves 芽叶绿 (#A8C879)（两片浅鼠尾草绿叶） | one leaf（一片）、three leaves（三片）、no leaves（无叶）、dark green（深绿） |
| 眼睛 | LARGE round eyes with big white whites + black pupils（大圆眼+大白眼白+黑瞳孔），常不对称 | tiny white-dot eyes（小白点眼）、centered pupils（瞳孔居中）、no eyes（无眼）、extremely large chibi eyes（超大萌系眼） |
| 嘴巴 | SMALL BLACK/DARK mouth（小黑色/深色嘴），简单线条或弧线，每页表情不同 | DEEP RED/CRIMSON mouth（深红嘴）、no mouth（无嘴）、same shape every page（每页同形状）、large mouth（大嘴） |
| 手臂 | exactly TWO thin black arms with small hands（恰好两条细黑手臂+小手） | extra limbs（多余肢体）、missing arms（缺手臂）、three arms（三臂） |
| 腿 | exactly TWO short black legs with small feet（恰好两条短黑腿+小脚） | extra legs（多余腿）、missing legs（缺腿）、long legs（长腿） |
| 阴影 | small shadow under feet（脚下小阴影） | no shadow（无阴影）、large shadow（大阴影） |
| 数量 | EXACTLY ONE character（恰好一个角色） | multiple characters（多个角色）、two characters（两个） |
| 位置 | ONLY at 指定位置 | character inside card（卡片里出现角色）、character in icon（图标里出现角色） |

---

## 嘴巴表情库（每页必须不同，4页至少3种）

基于新版人物卡的5种基础表情延展：

| 表情 | 描述 | 适用场景 |
|---|---|---|
| happy smile 开心 | 上弯弧线微笑，眼睛弯成月牙 | 落点、温暖场景、互动、积极内容 |
| playful wink 调皮 | 一只眼眨眼，嘴角微歪 | 轻松、幽默、俏皮内容 |
| curious O 好奇 | 小O形嘴，眼睛睁大看向前方 | 探索、观察、提问、发现新事物 |
| surprised O 惊喜 | O形嘴，眼睛圆睁，头顶可加闪光 | 封面、突发事件、震惊、好消息 |
| thinking 思考 | 小嘴微抿或波浪线，眼睛看向侧上方 | 分析问题、清单核对、深度内容 |
| serious line 认真 | 一字嘴，直线或微弯 | 严肃话题、重要提醒 |
| determined press 坚定 | 抿嘴，嘴角微下撇 | 解决方案、行动号召 |
| confused small 困惑 | 小嘴微张，眼睛微斜 | 不解、质疑、反常识 |

**规则（v1.5.0 强化）**：
- 4-6页中**每页嘴型必须不同**（不是至少3种，是每页都不同）
- 不仅嘴型不同，**眼睛状态也必须每页不同**（睁大/眯起/闭眼/向上看/坚定聚焦等）
- **身体动作也必须每页不同**（站立/盘腿坐/踩石头/坐云上/举牌子等）
- 封面常用 curious O 或 surprised O（含粉舌拟人化）
- 落点页（金句页）常用 happy smile（小微笑，不夸张）
- 互动页常用 curious O（含粉舌，提问表情）
- **所有嘴型都是 SMALL 小比例**，不能大嘴/大张嘴
- **张嘴必须含粉舌**，不能全黑洞

---

## 角色尺寸与位置

- 活跃状态时占页面高度 **12-22%**，绝不填满页面
- 位置：封面常在 lower center（下中），正文页常在 right side（右侧）或 lower-left（左下）
- 角色是**动作主体**（actor），不是角落装饰——它必须在做与页面主题相关的动作（拿清单、指方向、举牌子、持放大镜等）

---

## 角色唯一性强化（经过多轮踩坑验证）

### 问题：卡片/图标里出现小角色

经过多轮迭代发现，模型容易把卡片里的图标（如电脑、钱袋、银行卡）渲染成小墨仔角色，导致一页出现两个角色。

### 解决方案：三重描述

不要只写 "EXACTLY ONE character"，要写：

```
EXACTLY ONE character on page, never two or more.
The character is ONLY at [position], doing [action].
NO character inside any card, NO small character anywhere else, NO character in icons.
All card icons are INANIMATE objects (NO face, NO character, NO teardrop shape).
```

### 每个图标必须标注

每个卡片/步骤里的图标都要明确标注：
```
inanimate [object] icon (NO face, NO character, NO teardrop shape)
```

示例：
- `inanimate bank card icon with chip (NO face, NO character, NO teardrop shape)`
- `inanimate money bag icon with coins (NO face, NO character, NO teardrop shape)`
- `inanimate laptop icon with screen (NO face, NO character, NO teardrop shape)`

### 背景涂鸦也要注意

背景里的 tiny doodle icons 也必须是无生命物体，不能有角色/脸：
```
tiny doodle icons scattered (inanimate objects only, NO character doodles, NO faces in doodles)
```

---

## image-to-image 参考

生成时必须传入 `assets/seedling-character-sheet.png` 的 URL 作为 `image_reference_url_list`，用 image_edit 工具（不是 image_gen），确保角色形象严格匹配人物卡。

### 人物卡 URL 管理

- 人物卡本地路径：`assets/seedling-character-sheet.png`
- 生成前用 `FileBatchUpload` 上传获取 URL（URL 可能过期，每次生成前重新上传）
- 把 URL 传入 `image_reference_url_list` 参数

---

## 常见角色问题快速修复

| 问题 | 原因 | 修复方法 |
|---|---|---|
| 出现第二个角色 | prompt 不够强 | 重生成，用三重描述：EXACTLY ONE + ONLY at position + NO character in cards/icons |
| 卡片图标变成小墨仔 | 图标被模型渲染成角色 | 重生成，每个图标标注 "inanimate icon (NO face, NO character, NO teardrop shape)" |
| 背景涂鸦里出现小脸 | 涂鸦未限制 | 重生成，强调 "doodles are inanimate objects only, NO character doodles, NO faces" |
| 角色太胖/太瘦 | 身体形状描述不够 | 重生成，强调 round plump teardrop (not slim, not spherical) |
| 眼睛太大/太小 | 眼睛描述不够精确 | 重生成，强调 LARGE round eyes with big white whites (not tiny dot eyes, not extremely large chibi eyes) |
| 嘴巴变成红色 | 旧版描述残留或模型误渲染 | 重生成，强调 SMALL BLACK/DARK mouth, NOT red, NOT crimson |
| 嘴巴每页都一样 | 未指定每页不同嘴型 | 重生成，每页 prompt 指定不同 mouth expression |
| 头顶变成螺旋卷须 | 旧版描述残留 | 重生成，强调 small sprout with slightly curly stem, NOT spiral coil loop |
| 头顶尖顶 | 身体形状被误渲染 | 重生成，强调 round plump teardrop, NOT pointed top, rounded top |
| 叶子数量不对 | 未强调 exactly two | 重生成，强调 exactly TWO light sage-green leaves |
| 身体变成纯平黑 | 质感描述不够 | 重生成，强调 hand-drawn ink texture, natural ink bleed, scribble strokes (NOT flat black) |

---

## v1.6.0 新增：角色一致性前置原则（借鉴 awesome-gpt-image-2）

> awesome-gpt-image-2 避坑指南："角色一致性前置——动作序列越长越容易换脸换衣服，要把'同一角色、同一服装、同比例'写在动作列表之前。"

### 为什么要前置

经过 10+ 轮实战迭代发现：当 prompt 中角色描述放在内容描述之后时，模型容易在生成卡片/图标时"忘记"角色设定，导致角色外观漂移（身体变圆/变瘦、头顶芽变螺旋卷、嘴巴变红、眼睛变小）。把完整角色锁放在 prompt 的 CHARACTER 字段（内容之前），能显著提升一致性。

### 前置写法

在每页 prompt 中，CHARACTER 字段必须包含完整角色锁（不是简写），且放在 CONTENT 字段之前：

```
=== CHARACTER ===（放在 CONTENT 之前）
=== MOZAI CHARACTER (strictly match reference image) ===
[完整角色锁描述，逐字复制，不可省略任何要素]
PAGE STATE: [本页位置/尺寸/动作/眼睛/嘴型/情绪]
EXACTLY ONE character... [唯一性强化]
```

### 一致性检查（生成后必做）

逐张放大校验时，必须核对以下 8 个身份锚点：
1. 身体形状：圆胖泪滴（非球形/非修长/非尖顶）
2. 身体颜色：墨黑 #1B1B1B（非纯黑 #000/非深灰）
3. 身体质感：手绘墨迹感+自然晕染（非纯平黑/非发光）
4. 头顶芽：小芽+微卷细茎（非螺旋线圈/非直茎/非无芽）
5. 叶子：恰好两片浅鼠尾草绿叶（非一片/非三片/非深绿）
6. 眼睛：大圆眼+大白眼白+黑瞳孔（非小白点眼/非瞳孔居中）
7. 嘴巴：小黑色嘴（非深红/非无嘴/非大嘴）
8. 四肢：恰好2条手臂+2条腿（非多余/非缺失）

> 任何一个锚点漂移都必须重生成，不能"差不多就行"。

---

## v1.6.0 新增：五官拆解（借鉴 awesome-gpt-image-2「拆解五官」原则）

> awesome-gpt-image-2 避坑指南："不要只写'很美的女孩'，大模型不知道你的审美标准。拆解成'桃花眼、高鼻梁、野生眉'。"

墨仔的五官也必须拆解到可执行的粒度，不能只写"大眼睛小嘴巴"。

### 眼睛拆解

```
LARGE round eyes (diameter approximately 25-30% of body width).
Big white eye whites (sclera occupies 60-70% of eye area).
Black round pupils (occupies 30-40% of eye area, NOT tiny dot).
Pupils often slightly asymmetrical — one eye may look slightly larger or offset, or pupils point in slightly different directions (expressive, NOT cross-eyed).
Eyes have subtle ink outline (NOT thick black ring, NOT no outline).
NO eyelashes, NO eyebrows as separate thick lines (brows are subtle ink strokes above eyes).
Eye white is clean white (NOT off-white, NOT yellowish).
```

### 嘴巴拆解

```
SMALL BLACK/DARK mouth (width approximately 15-20% of body width, NOT wide, NOT large).
Mouth is simple line or curve (NOT detailed lips, NOT teeth visible unless specified).
Expression varies per page (at least 4 different mouth shapes across 5 pages).
When open: SMALL open oval (width ≤20% body width), visible PINK/RED TONGUE inside (small tongue, NOT filling entire mouth), anthropomorphic human-like mouth interior (NOT all-black hole, NOT abyss).
When closed: simple curved line (smile/frown/neutral) or straight line (serious) or wavy line (thinking).
Mouth color is black/dark ink (NOT red, NOT crimson, NOT pink unless tongue).
NO blush around mouth, NO pink cheeks.
```

### 头顶芽拆解

```
Small sprout on top of head (height approximately 15-20% of body height).
Thin slightly curly stem (curvature is gentle, NOT tight spiral coil loop, NOT straight vertical).
TWO light sage-green leaves (#A8C879) at top of stem.
Leaves are small oval/teardrop shape (each leaf approximately 8-10% of body width).
Leaves face slightly outward (one left, one right), NOT both facing same direction.
Stem color is dark green/black ink (NOT brown, NOT yellow).
NO flower, NO bud, NO extra leaves.
```

### 身体质感拆解

```
Ink-black body (#1B1B1B-ish, NOT pure #000, NOT dark gray).
Hand-drawn ink texture: visible scribble strokes, cross-hatching lines, natural ink bleed at edges.
Body edge is slightly irregular (hand-drawn feel, NOT perfect smooth silhouette, NOT hard geometric shape).
Subtle texture variation: some areas slightly lighter (ink wash effect), some areas darker (dense scribble), creates depth.
NOT flat black (solid fill with no texture).
NOT shiny/glossy (no highlights, no reflections).
NOT pencil/crayon only (must have ink texture, not just light pencil lines).
Body has small shadow underneath feet (soft gray shadow, NOT hard black shadow, NOT large shadow).
```

---

## v1.6.0 新增：灵活尺寸与位置协议

基于用户硬约束"墨仔为辅，比例不能占比太高"，角色尺寸不再固定为 12-22%，而是根据布局模式灵活调整。

### 内容主导型（Content-Dominant，默认）

```
CHARACTER SIZE: SMALL, occupying ONLY 8-10% of page height.
CHARACTER POSITION: bottom-left OR bottom-right CORNER (alternate pages to avoid same side consecutively).
Character is a small accent, NOT the main visual focus.
Area around character is COMPLETELY BLANK (no text, no icons, no doodles within 1cm).
Character must still be doing a relevant action (holding notebook, pointing, waving) — NOT just standing idly.
```

适用页面：P2 分析、P3 分析、P4 金句+应急

### 角色主导型（Character-Dominant，仅封面/互动页）

```
CHARACTER SIZE: MEDIUM, occupying 18-25% of page height.
CHARACTER POSITION: lower-center OR center (main visual focus).
Character is the main subject, doing a prominent action.
Content (cards/icons/tags) arranged around character, NOT competing with it.
```

适用页面：P1 封面（可选）、P5 互动（可选）

### 尺寸选择决策树

```
用户是否明确要求"墨仔为辅/比例小/内容为主"？
├─ 是 → 全部页面使用内容主导型（8-10%，角落）
└─ 否 → 默认混合模式：
    ├─ P1 封面：角色主导型（18-25%，下中）
    ├─ P2/P3 分析：内容主导型（8-10%，角落）
    ├─ P4 金句：内容主导型（8-10%，角落）
    └─ P5 互动：角色主导型（18-25%，下中）
```

> ⚠️ 无论哪种模式，角色都必须是"动作主体"（在做与页面主题相关的动作），不能变成纯装饰。即使小比例在角落，也要有明确的动作和表情。
| 多手多脚（v1.5.0 新增） | 模型误渲染多余肢体 | 重生成，强调 EXACTLY TWO arms + EXACTLY TWO legs + NO extra limbs + NO third arm/leg，在Avoid列表列举 extra limbs, three arms, three legs |
| 张嘴是全黑洞（v1.5.0 新增） | 未强调嘴部拟人化 | 重生成，强调 SMALL open oval mouth + visible PINK/RED TONGUE at bottom + NOT all-black hole |
| 嘴太大/表情太夸张（v1.5.0 新增） | 未强调小比例嘴型 | 重生成，强调 SMALL mouth + NOT wide + NOT large + restrained expression + NO big laughing mouth |
| 每页表情/动作单一重复（v1.5.0 新增） | 未指定每页差异化 | 重生成，每页prompt指定不同的眼睛状态+嘴型+身体动作，生成前先规划5页差异化状态表 |
| 脸部出现红晕/腮红（v1.5.0 新增） | 模型误渲染粉色脸颊 | 重生成，强调 NO blush + NO pink cheeks + NO rosy cheeks + face is clean black ink |
| 墨仔外观不一致（v1.5.0 新增） | 角色锁描述不够强或人物卡URL过期 | 重新上传人物卡获取新URL，重生成，强化完整角色锁描述（泪滴形+大眼+小嘴+小芽双叶+手绘墨迹） |
