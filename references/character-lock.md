# Character Lock · 墨仔(Mozai) 角色锁

从用户上传的墨仔人物卡（`assets/seedling-character-sheet.png`）提取的精确角色描述。每个页面 prompt 必须包含核心形象描述，逐字复制。

> v1.4.0 更新：基于2026-08-31新版墨仔IP设定图更新。关键变更：嘴巴颜色从深红改为黑色线条、头顶芽形态从螺旋卷须改为小芽微卷茎、身体质感强调手绘墨迹感、新增IP设定信息与表情库。
>
> v1.7.0 核心变更：**涂鸦是墨仔的天性**——墨仔是"一滴在纸上活过来的墨"，它走到哪里，哪里就有涂鸦。涂鸦背景不是可选排版，而是墨仔IP的核心视觉特质，每页背景必须有手绘涂鸦质感。

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
| **天性（v1.7.0新增）** | **涂鸦是墨仔的天性——它走到哪里，哪里就有涂鸦。每页背景必须有铅笔网格+散布涂鸦图标+交叉排线+墨点的手绘质感，禁止大面积纯白空白。** |

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
| **涂鸦天性（v1.7.0新增）** | **背景必须有FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching patches + ink dots，全页覆盖，禁止大面积纯白空白** | **flat plain background（扁平无纹理背景）、large empty white spaces（大面积纯白空白）** |

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

**规则**：4页中至少出现3种不同嘴型。封面常用 curious O 或 surprised O。落点页（P4）常用 happy smile。

---

## 角色尺寸与位置

- 活跃状态时占页面高度 **12-22%**，绝不填满页面
- 位置：封面常在 lower center（下中），正文页常在 right side（右侧）或 lower-left（左下）
- 角色是**动作主体**（actor），不是角落装饰——它必须在做与页面主题相关的动作（拿清单、指方向、举牌子、持放大镜等）

---

## 表情动作与内容关联原则（v1.7.1 新增，核心约束）

> ⚠️ **墨仔的表情和动作必须根据图文内容来定，不能毫无关联。** 差异化不是目的，内容关联才是目的。每页的表情/动作必须能反映该页的内容情绪和主题，不能为了"每页不同"而随便选一个表情/动作。

### 页面类型与表情动作关联表

| 页面类型 | 内容特征 | 推荐表情 | 推荐动作 | 必须避免 |
|---|---|---|---|---|
| 封面（钩子/震惊） | 反常识、冲突、震惊、数字冲击 | surprised O 惊喜、curious O 好奇、圆睁+眉上扬 | 拿放大镜指方向、举手、指标题 | happy smile 开心、闭眼、叉腰 |
| 分析（问题/套路/现象） | 列举问题、分析原因、揭示套路 | thinking 思考、confused small 困惑、serious line 认真、皱眉观察 | 托腮思考、拿本子记录、拿放大镜看、抱臂沉思 | happy smile 开心、挥手、张嘴大笑 |
| 分析（方案/做法/建议） | 列举解决方案、行动建议、防坑做法 | determined press 坚定、serious line 认真、自信眼神 | 双手叉腰、举盾牌、指方向、拿清单勾选、竖拇指 | confused 困惑、波浪线嘴、托腮 |
| 金句（感悟/落点/金句） | 金句、感悟、温暖收尾、观点表达 | 沉思、happy smile 温暖、闭眼微笑、感悟眼神 | 托腮、手放胸口、盘腿坐沉思、闭眼、拿笔 | surprised 惊讶、张嘴、挥手、叉腰 |
| 互动（提问/邀请/引导） | 互动提问、引导评论、邀请分享 | curious O 好奇、happy smile 邀请、期待眼神、圆睁 | 挥手、拿喇叭、举手提问、递话筒、指评论区 | serious 严肃、抿嘴、叉腰、闭眼 |

### 关联检查（生成前必做）

生成5页差异化状态表时，必须同时填写"内容关联理由"列，说明每页表情/动作与页面内容的关联：

| 页 | 页面类型 | 内容主题 | 表情 | 动作 | 内容关联理由 |
|---|---|---|---|---|---|
| P1 | 封面 | {{封面钩子内容}} | {{表情}} | {{动作}} | {{为什么这个表情/动作适合这个内容}} |
| P2 | 分析（问题） | {{P2问题内容}} | {{表情}} | {{动作}} | {{关联理由}} |
| P3 | 分析（方案） | {{P3方案内容}} | {{表情}} | {{动作}} | {{关联理由}} |
| P4 | 金句 | {{P4金句内容}} | {{表情}} | {{动作}} | {{关联理由}} |
| P5 | 互动 | {{P5互动内容}} | {{表情}} | {{动作}} | {{关联理由}} |

### 常见错误（必须避免）

1. **为了差异化而差异化**：P2分析页用happy smile开心表情（应该用thinking思考），P3方案页用confused困惑表情（应该用determined坚定）
2. **动作与内容无关**：P2列举套路时墨仔在挥手（应该在拿本子记录或托腮思考），P4金句页墨仔在拿喇叭（应该在托腮沉思）
3. **表情情绪与内容矛盾**：P3讲防坑做法时墨仔张嘴大笑（应该坚定认真），P5互动提问时墨仔严肃抿嘴（应该好奇邀请）
4. **所有页都是同一个表情**：虽然满足了"内容关联"，但违反了"每页差异化"——必须同时满足两个条件

### 双重约束（必须同时满足）

- ✅ **内容关联**：每页表情/动作必须与该页内容主题和情绪相关联
- ✅ **每页差异化**：5页的眼睛状态、嘴型、身体动作必须全部不同（至少4种嘴型、4种眼睛状态）

> 这两个约束不是互斥的——在内容关联的范围内，仍然可以做到每页差异化。例如：P2分析页可以用thinking（托腮），P3方案页可以用determined（叉腰），P4金句页可以用沉思（闭眼微笑），P5互动页可以用curious（挥手），P1封面可以用surprised（拿放大镜）——5页表情/动作都不同，且都与内容关联。

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

### image_edit 工具调用格式（v1.7.0 新增，实战验证）

> ⚠️ **必须使用 request_list 数组格式**，不能用扁平参数。实战验证：扁平参数调用会报错 `required param is empty, field: request_list`。

```
image_edit(
  model_version="seedream_5.0_pro",
  request_list=[
    {"prompt": "...", "image_reference_url_list": ["人物卡URL"], "height": 2364, "width": 1773},
    {"prompt": "...", "image_reference_url_list": ["人物卡URL"], "height": 2364, "width": 1773},
    ...
  ]
)
```

可一次传入多个请求（如5页同时生成），也可以单次传入一个请求。

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
| **背景大面积纯白空白（v1.7.0新增）** | **未强调涂鸦背景** | **重生成，强调 FAINT PENCIL GRID + SCATTERED TINY DOODLE ICONS + cross-hatching patches + ink dots, NO large empty white spaces, NO flat plain background** |
| **背景涂鸦有角色/脸（v1.7.0新增）** | **涂鸦未限制为无生命物体** | **重生成，强调 doodles are inanimate objects only (stars, leaves, pencils, arrows, dots), NO character doodles, NO faces in doodles** |
