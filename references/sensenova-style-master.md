# 商汤固定出图提示词 · 墨仔账号全风格融合版

> 2026-09-10 由账号 38 组 / 192 张已发布图文（2026-08-28 ～ 2026-09-10）反推融合而成，
> 覆盖早期手账卡、中期避坑指南、后期黑板/信息卡三个阶段的共性风格。
> **SENSENOVA-ONLY**：本模板含商汤专属参数（尺寸/JSON/prompt_extend），不得用于其他模型；
> 其他模型的 Prompt 亦不适用本模板的参数段。商汤通道出图一律以本模板为基底。

## 使用方法

每次出图只替换 `【】` 槽位与当页 CONTENT，其余段落逐字保留；按 prompt-template.md 的
SENSENOVA-ONLY 适配节发送（`size:"1056x1408"`、JSON edits、`prompt_extend:false`）。

## 固定模板（逐字使用）

```text
<!-- SENSENOVA-ONLY: 尺寸与请求格式不适用于其他模型 -->

=== CANVAS ===
True portrait 3:4 canvas, 1056x1408. The hand-drawn border sits about 30px inside the canvas
edges: the composition fills the frame generously and outer blank paper margins stay thin and
even on all four sides. No large empty paper bands anywhere.

=== STYLE ===
COLOR ANCHOR (highest priority): the paper tone must match the attached reference sheet background
exactly — a LIGHT warm off-white to pale cream (约 #e8e1d7), never tan, never kraft brown, never
sepia, never dark beige; the whole page stays bright and airy, shading must stay LIGHT. Mode B:
NO pencil grid. Mode A: an extremely faint light-grey pencil grid across the whole background.
All linework is BLACK ink-pencil (pure dark black, not brown or gray) with naturally rough sketchy
character: moderate cross-hatching, light stippling, sketchy construction strokes and perspective
lines on the ground; Mode B scenes are worked pencil sketches but never dark sepia washes.
Slight ink bleed is allowed; never smooth vector, never plastic 3D, never heavy shadows.
OVERALL LOOK (用户规则 2026-09-10，四轮校准后定稿): CLEAN and CRISP — paper bright and
translucent, ZERO grey haze / soft-focus / frosted filter over the page; color temperature
NEUTRAL warm cream (宁中性勿发黄, never cold grey, never yellow cast). BLACK INK LOCK: all
black linework, titles, character body and shadows must stay DEEP saturated charcoal-black with
sharp crisp edges (黑要够黑，白要透亮；发灰、朦胧、泛白即缺陷). Watercolor washes are SMALL
LOCAL accents only (tiny stains near edges or behind one prop) — NEVER a full-page misty wash
band. BACKGROUND DEPTH (封面默认): faint pencil grid + 2-3 tiny high-transparency mist-blue/sage
stains + crisp foreground linework — layering comes from these small accents, not from haze.
Doodle density on covers leans generous: stars, sparkles, arrows, spirals, paper clips, washi
tape strips, music notes, leaves and dots scattered naturally in empty areas (still never over
title, scene or character).
Accents are low-saturation
watercolor / crayon washes in mist blue, peach pink, light sage green and pale lavender-butter;
color only supports information and never competes with text. Inset thin hand-drawn border with
slightly wobbly double lines; the four corners carry small low-density flourishes mixing vine
leaves, tiny bows and star dots. Scattered tiny inanimate doodles float in empty areas only:
stars, sparkles, leaves, pencils, arrows and dots. All visible text is Chinese handwritten style:
titles in charcoal hand-lettering with MEDIUM-THIN strokes (large size but light weight —
never heavy thick brush, no flying-white blobs; 用户规则 2026-09-10：字体不要过粗), supporting text in casual pencil handwriting.
No English, no pinyin, no watermark.

=== CHARACTER ===
Exactly one Mozai (the single reference card defines appearance only — never copy its sheet
layout, text, arrows or multiple poses into the image): a plump pear/teardrop black ink-drop
body (height about 1.1-1.2x width, round heavy bottom tapering smoothly to a small point at
the top where the sprout stem grows — BODY SHAPE LOCK: never a perfect circle, ball, egg or
tall slim teardrop, and this proportion must be IDENTICAL on every page of the set; scaling
up/down never changes it) with soft hand-drawn pencil texture and visible hatching; one thin
slightly curled sprout stem on top with exactly two light sage-green leaves; large round eyes
with big white sclera and subtly asymmetric pupils; exactly two thin arms and two short legs;
no clothes. Choose ONE mouth-blush mode per deck and keep it consistent across all pages:
(A) 定稿模式（默认）: a small restrained smiling mouth, no blush, right hand clearly holds a
pen chosen for this page's theme (毛笔/铅笔/钢笔/马克笔均可，笔型自由，握法固定) with fingers
visibly wrapped around the handle — never floating, never separated; if both hands must do the
page action, the pen lies visibly beside the character instead, never add an arm.
(B) 早期手账模式: usually two soft peach-pink blush circles on the cheeks and a wider open
happy mouth with a small red tongue visible (blush appears on roughly two thirds of early pages —
choose per deck, keep it consistent across the deck); the right hand holds a small clipboard with
pencil-scribble list lines (most common) or a round magnifying glass (inspection / pitfall pages);
a pen (any type) appears only occasionally. In this mode the pencil grid is usually ABSENT, the page
number is plain handwriting "0N / N" at the top-left (no circle, thin underline is optional),
Mozai is a medium presence of 15–30% of canvas height, corner flourishes lean toward vine leaves,
and the main visual is info cards or a pencil scene sketch (no chalkboard).
【当页位置/占比/动作/表情，如：cover-lower-center about 25% tall, waving one arm / interior
bottom-right corner about 9% tall, pointing at the card】

=== LAYOUT ===
【封面页用（2026-09-10 用户规则更新）：
- 顶部标签：two small pastel OUTLINE pill labels 居中并排（两只标签作为一组放在顶部中央，
  左右相邻，不再分立两角），细描边+淡彩底；
- 标题：a two-line title very large, almost full inner width, stroke weight MEDIUM-THIN and light
  (字大笔画不粗，严禁超粗毛笔糊字), second line with a long wavy ink underline; one short pencil subtitle on a single thin rule;
- 下半部分：ONE theme-related hand-drawn scene filling the lower half（主题相关的手绘场景，
  如出行主题的火车站台+车票、防骗主题的聊天界面+二维码等），线条轻细、大量留白、
  不得满幅堆砌；场景即主视觉；
- 墨仔：位置三选一（左下 / 中下 / 右下，按场景构图就近安排，连续封面可轮换），
  约占宽 32–38%；道具自由——毛笔不是必需，可改为与主题相关的手持物
  （车票、票根、写字板、放大镜、手机等），也可空手；表情任选表情库；
- 底部：slim OUTLINE capsules with small hand-drawn dots between neighbors。
内页用：Unique page number "0N / N" in plain handwriting at the TOP-LEFT (circle style only in
Mode A); centered hand-lettered title with MEDIUM-THIN light strokes and wavy underline; main visual is one large information element
(a big number card / 2-3 info cards / a chalkboard / a simple pencil scene) occupying the middle
55-65%; Mozai stays a small corner helper and never covers text.】

=== CONTENT ===
Render every Chinese string verbatim, exactly once, correct characters:
【逐条列出：页码 / 标题 / 副题 / 每张卡片标题与正文 / 底部标签 / 其他可见文字，含各自位置】

=== CONSTRAINTS ===
P0: exactly the listed strings with correct characters; one character only; two leaves, two
arms, two legs; correct page number position. P1: action matches page content; title dominates
the hierarchy; reading areas stay clean. P2: corner flourishes and sparse doodles.

=== AVOID ===
a second character or extra limbs, wrong leaf count, reference-sheet collage or character-sheet
text, faces or human features on any prop / vehicle / ticket / icon, pseudo-letters or fake
numbers on tickets and labels, duplicated or misplaced page number, altered numbers or Chinese
characters, floating pen separated from the hand, body-shape drift between pages (circle/ball/egg
instead of the locked pear teardrop), English or pinyin, watermark, wide empty
paper margins

=== RETRY NOTES (SENSENOVA 高频故障强化) ===
Vehicle and machine fronts must be completely plain (a locomotive is a smokestack + headlamp
circle, no eyes, no mouth, no smile). Tickets, documents and tags carry only abstract dash lines
and plain outlines. No anthropomorphic faces anywhere except Mozai himself.
```

## 风格参照扩展（2026-09-10"班级群诈骗封面"参照，商汤已验证可学）

在基础模板之上，允许以下扩展项（按页面叙事需要选用）：

1. **侦查者表情包**：皱眉斜眼（怒眉压眼）、眯眼怀疑；可同时"左手举放大镜罩住单眼 + 右手拿手机 + 笔（毛笔/铅笔/钢笔均可）斜背在身后"的三道具叙事姿态（道具总数仍受两臂限制，笔可背负不可消失成第三只手）。
2. **炭笔斑驳黑**：墨仔身体的黑色排线更粗犷，黑色里留白色斑点肌理（炭笔扫粗纸感），不是均匀细排线。
3. **多色混合晕染标签**：顶部标签的水彩底可用粉+蓝+黄或绿+黄多色混晕，不再限定单一淡色。
4. **叙事道具组**：聊天气泡（含极简头像）、二维码卡片、手机聊天 UI 等半色调线稿道具，带淡彩点缀——适配防骗、群聊、通知类主题。
5. **背景暖奶油+淡格纹**：纸面散布粉/蓝/绿软水彩渍与墨点，格纹若有似无。
6. **底部胶囊**可带黄/绿/粉极淡彩底（描边仍为细灰黑线）。
7. **手帐涂鸦密度（封面默认）**：背景为浅灰蓝方格纸纹理（清晰但极淡）；顶部两角小段斜贴和纸胶带；标签做成微斜手绘贴纸；标题四周散布手写批注小涂鸦（箭头、圈圈、五角星、短线、螺旋）；主题场景内加手帐批注元素（虚线路径+小箭头、小旗子、速度短线）；散落曲别针、胶带贴纸、叶芽等小物。密度中等、随手自然，不遮挡文字与人物。

## 风格融合说明（反推自 192 张成图）

> 早期部分已升级为全量审计：2026-08-28～08-29 的 9 组共 41 张全部经 VLM 逐张识别
> （审计明细：`账号图文拉取/yd3tdz-6jv0-20260910-122159/style_audit.jsonl`，early=true），
> 模式 B 的细节以上述 41 张统计为准；9 月之后的图文仍是三期抽样融合。

| 风格要素 | 融合结论 | 来源阶段 |
|---|---|---|
| 纸底 | 暖白→奶油色，细纤维颗粒+极淡铅笔网格（后期网格更淡，取淡值） | 全期一致 |
| 线稿 | 黑色铅笔+炭笔混合，排线/点描/轻晕染；早期略糙、后期干净，取"自然不均匀" | 全期一致 |
| 点缀色 | 雾蓝/蜜桃粉（早期偏橙）/浅鼠尾草绿/淡薰衣草+奶油黄 | 全期一致 |
| 标题 | 大号手写体但笔画中细轻盈（用户规则：字体不要过粗），1–2 行，第二行下手绘波浪线 | 全期一致 |
| 顶部标签 | 早期圆角胶囊（带小图标）→ 中期和纸胶带 #标签，模板兼容两种写法 | 8/28 vs 9/1 |
| 底部 | 固定 3 枚 pastel 关键词标签（胶囊/胶带/缎带均可） | 全期一致 |
| 页码 | 左上圆圈内 `0N / N`，全套同位同字级 | 全期一致 |
| 角饰 | 早期蝴蝶结繁复 → 后期藤叶/几何角饰低密度，模板取低密度混合 | 演变 |
| 墨仔 | 双模式：A 定稿（无腮红+克制嘴+右手持笔，笔型按主题自由，默认）/ B 早期手账（腮红+红嘴+写字板或放大镜，可无笔）；同套图只取其一；**全套身体比例锁定梨形水滴（高约宽 1.1–1.2 倍），禁止逐页高矮胖瘦漂移** | 8/28 vs 9 月起 |
| 内页主视觉 | 大数字卡 / 2–3 信息卡 / 黑板 / 素描场景四型轮换，墨仔缩角 | 9/6–9/10 |

## 已知取舍

- 角色双模式：(A) 定稿模式（无腮红、右手持笔且笔型按主题自由，2026-09 起的现行角色锁）与 (B) 早期手账模式
  （腮红+红嘴+写字板/放大镜，8 月底风格）均已纳入模板，**同一套图只能二选一并全套一致**；
  模式 B 下允许整页无笔。默认用 A，用户点名"早期风/腮红款"时切 B。两种模式下墨仔的梨形
  水滴体态比例（高约宽 1.1–1.2 倍）全套锁定一致，不随占比、动作或页面布局漂移。
- 中期封面"墨仔占画面中心 35%+"的大角色构图，模板中归入封面槽位的可选占比（20–30%）；
  内页仍强制小角色。
