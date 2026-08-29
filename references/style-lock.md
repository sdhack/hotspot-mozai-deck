# Style Lock · 通用风格锁

每个页面 prompt 必须包含以下风格描述，逐字复制，不可修改。

---

## 完整风格锁（复制到每页 prompt 开头）

```
Chinese vertical Douyin article page, 3:4, 1080x1440. Richly detailed hand-drawn pencil sketch illustration with ink outlines on warm off-white paper. Cross-hatching, stippling, subtle ink bleed. Decorative corner flourishes. Thin double-line border. Premium sketchbook feeling.

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
| 边框 | thin double-line border（细双线边框） | ✓ |
| 装饰角 | decorative corner flourishes（四角装饰花纹） | ✓ |
| 标题字体 | bold brush/marker hand-lettering（粗毛笔/马克笔手写体） | ✓ |
| 正文字体 | casual pencil handwriting（随意铅笔手写体） | ✓ |
| 禁止 | formal printed fonts（正式印刷字体）、English text（英文）、character names（角色名）、version labels（版本标签）、watermark（水印） | ✓ |

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

### 背景装饰

- faint pencil grid（淡铅笔网格）
- tiny doodle icons scattered（散布的小涂鸦图标，必须是无生命物体，不能有角色/脸）
- tiny doodle stars and sparkles（小星星和闪光）

---

## 配色（pastel 标签）

| 用途 | 颜色 |
|---|---|
| 标签1（冷色） | pale blue wash（淡蓝） |
| 标签2（暖色） | pale peach wash（淡桃） |
| 标签3（中性） | pale sage green wash（淡鼠尾草绿） |
| 标签4（可选） | pale lavender wash（淡薰衣草紫） |
| 墨水 | ink-black (#1A1A1A-ish, not pure #000) |
| 纸张 | warm off-white (#FBFAF5-ish) |

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
