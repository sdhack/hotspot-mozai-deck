# 单人物卡出图协议

本协议将《墨仔出图提示词模板》的可复用部分纳入技能。用于任何需要墨仔成图的任务；生成前与 [prompt-template.md](prompt-template.md)、[character-lock.md](character-lock.md)、[style-lock.md](style-lock.md)、[v1.9-image-profile.md](v1.9-image-profile.md) 一并读取。

工具或模型的实际参数以当前环境为准。本协议不要求固定供应商、模型、上传器、请求数组或尺寸档位。

## 人物卡

| 文件 | 角色 | 默认使用条件 |
|---|---|---|
| `mozai-ip-sheet-4k.png` | 形体、配色、墨迹质感与默认毛笔姿态的唯一人物真值 | 所有页面默认使用 |

默认采用单人物卡一致性策略：仅使用 4K 主卡作为参考输入，以保证跨页一致性。人物卡只定义单一角色外观，绝不能被拼贴、复刻为人物设定页、九宫格、色卡、箭头或中文说明。

若参考图文字、多角色或卡片布局进入画面，第一次重试先强化"参考图只作外观真值"；第二次重试继续使用 4K 主卡并减少其他视觉干扰，同时保留完整文字角色锁。不得把不合格的参考卡拼贴图交付为成品。

## 逐页规划

生成前建立下表。N 由已冻结文案决定，不以固定五页或六页为目标。

| 页 | 职责 | 页面模式 | 墨仔位置/占比 | 表情与动作 | 毛笔规则 | 可见文字 |
|---:|---|---|---|---|---|---|
| 1 | 封面 / 钩子 | 角色主导 | 下方约 18–25% | 好奇或惊讶，动作指向冲突物 | 右手持笔 | 两行以内标题、短副题、标签 |
| 2 | 问题 / 事实 | 内容主导 | 左下或右下约 8–10% | 思考、困惑或认真 | 右手持笔 | 标题、信息卡、页码 |
| 3 | 方案 / 方法 | 内容主导 | 与前页换侧约 8–10% | 坚定或认真，指向清单 | 右手持笔 | 标题、步骤卡、页码 |
| 4…N-1 | 对比 / 解释 | 按信息职责选择 | 与相邻页改变位置或姿态 | 与结论相符 | 与动作兼容 | 本页唯一结论 |
| N | 收束 / 落点 | 角色主导 | 下方约 18–25% | 温暖微笑、挥手或提示 | 双手忙时笔放在身旁可见 | 页码、结论或可执行提示；互动仅按需 |

整套至少变化四种嘴型、眼神或姿态；内容主导页的主体信息约占 55–65%，墨仔不得压缩阅读区。封面和情绪/收束页可角色主导；少字、多画面请求改用场景叙事。

## Prompt as Code

每页按以下顺序组织，`CHARACTER` 必须先于 `CONTENT`：

```text
=== CANVAS ===
[实际可用的严格 3:4 尺寸；四边至少 20px 连续暖白外留白；内缩边框]

=== STYLE ===
Vertical 3:4 hand-drawn journal news card. Warm off-white to light cream paper with subtle fiber grain and a faint pencil grid across the entire background. Black hand-drawn pencil-and-ink line art with natural uneven line weight, light cross-hatching, stippling and subtle ink bleed. Restrained mist blue, peach pink, light sage green and pale cream yellow accents only. Inset thin double-line hand-drawn border with low-density corner flourishes. Scattered tiny inanimate doodles only: stars, leaves, pencils, arrows, dots and sparkles. Not photography, not plastic 3D, not clean vector, no neon, no saturated colors, no large flat blank white areas. All visible text is Chinese handwritten style; title uses bold brush-marker lettering and supporting text uses casual pencil handwriting. No English, pinyin, character name, version label or watermark.

=== CHARACTER ===
Exactly one Mozai, matching the selected reference: a round plump black ink-drop body with organic hand-drawn ink texture; one thin slightly curled sprout stem with exactly two light sage-green leaves; large round eyes with visible white sclera and subtly asymmetric pupils; a small restrained black mouth [current mouth shape]; exactly two thin arms and two short legs; no blush and no clothes. [Current position, size, eye direction, expression and action.] Right hand clearly holds a small calligraphy brush with visible tapered bristle tip, not a pen, pencil or wand. [If both hands are required: the brush lies visibly beside the character; never add an arm.]

=== LAYOUT ===
[Content-dominant / character-dominant / scene-narrative. Define title, information area, character safe area and fixed page-number position.]

=== CONTENT ===
[List every visible Chinese title, subtitle, card, tag, page number and bubble verbatim, with its position. State exact card count and use inanimate icons.]

=== CONSTRAINTS ===
[P0 facts/text/one character/limbs/leaves/page number/card count; P1 action and readable hierarchy; P2 decoration.]

=== AVOID ===
[Only likely errors for this page: extra character or limb, reference-sheet collage, face in icon, duplicate page number/card/tag, random number, red mouth, watermark.]
```

## Layout and text contract

- **Cover:** no page number by default; at most two title lines, wave underline under the second line, one short subtitle, a low-contrast theme-related mid-ground scene layer between the title area and Mozai (paler than the foreground, roughly 40% line strength, no human figures or faces, never overlapping title, subtitle or capsules; Mozai's silhouette stays crisp against it), up to two top labels and 3–4 keyword capsules. It must enter a concrete scene, problem or information gain immediately.
- **Content cards:** place the single page number once at the same chosen location across the set. Use exactly the planned number of cards; every card has a distinct title, body and inanimate icon. Do not invent statistics, time stamps, currencies or symbols.
- **Closing page:** one concrete, answerable conclusion or action reminder. Add one interaction question or speech bubble only when the user requests it or the content naturally requires it; never add a second bubble.
- **Text:** list exact Chinese text in the prompt and render it on the image by default. Split long prose into short cards; title no more than two lines. Do not use pinyin, radicals or text outside the image to work around rendering. After two targeted text retries, stop and ask whether post-layout text replacement is acceptable.
- **Tone:** state safety or factual guidance clearly, but prefer specific, sharing-oriented phrasing to command-style slogans when the subject permits.

## Preflight and QA

Before generating, verify the cover's stated count equals the body card count, page roles fit the facts, all page text is frozen and each action can be performed with two arms.

After each page, inspect the actual file at readable scale. A page is blocked if any of the following applies: it is not 3:4; the outer margin or page-number sequence is wrong; it contains more than one Mozai; it has extra/missing limbs or leaves; the brush is incompatible with the action; reference-card content appears; essential Chinese text, numbers or facts are wrong; a face appears in any icon/doodle; or a required card/bubble count is wrong.

Retry only the failed page. Retry 1 removes conflicting P2 detail and states the observed defect. Retry 2 simplifies the pose, card density or reference input. Then stop and report the remaining limitation rather than silently switching to a blank-text or altered-text design.
