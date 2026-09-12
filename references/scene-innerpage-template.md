# 场景插画内页模版（2026-09-12 定稿）

来源：主题 3「iPhone18今晚开售」一套 6 图 v3/v4 轮次（用户反馈"内页缺大型插画、排版单一、墨仔融合度不够"后重构，judge 全 pass）。定位：内页出图的**场景主导**模版，与 `cover-template-style-ref.md`（封面）配套，均基于 `backup-prompt-gpt2.md` 的浓黑排线视觉体系。

## 硬规则（Prompt 与 QA 同时生效）

1. **大幅插画为主体**：每页一幅与主题对应的大型场景插画，约占画面一半；纯文字排版页即缺陷。
2. **墨仔融入场景**：必须与场景道具互动（凑看/攀爬/坐桌角/挥手等），不做角落贴纸；占比约 9%（内容页）～15%（封面与收束页），上限 18%。
3. **标题波浪线**：每页标题正下方（两行标题则末行下）画手绘波浪下划线。
4. **持笔可选**：墨仔不强制持笔；无笔页面严禁为保留道具生成额外手臂。边框/场景中的铅笔涂鸦与笔筒道具不算违规。
5. **手足硬锁**：恰好两臂两腿，成图后放大清点；第三只手/第三条腿/多余的手/分叉肢体即阻断，只重做该页。
6. **标题逐字锁**：标题末字后禁止自动补句号等标点（曾在「…三道锁」后生成「。」被打回）。
7. **人物安全**：画面中儿童一律严格背影/后脑勺，零面部特征；无大人形象；手机屏幕空白无 logo。
8. **无红色**：内页无红色元素；低饱和粉/绿/蓝点缀不限。

## 双参考输入与开头声明（逐字）

FIRST = 风格参考图（只学风格/质感/字感，不复制场景构图）；SECOND = `assets/mozai-ip-sheet-4k.jpg`（仅外观真值）。

```text
The FIRST attached image is a style reference: learn ONLY its art style, texture and lettering feel.
The SECOND attached image is the character appearance truth (appearance only, never copy its sheet layout or
poses). Replace everything with the BRAND NEW inner page described below — keep no text, layout, page number
or scene from either image.
```

## CHARACTER 段固定骨架（当页只填位置/表情/动作）

```text
Exactly one Mozai: a plump pear/teardrop-shaped black ink-drop creature, body height 1.1-1.2 times its width,
round heavy bottom tapering to a curled pointed top bearing a thin sprout with exactly two sage-green leaves;
big white oval eyes with black pupils, subtle expressive eyebrows, a small black mouth (never red); no blush,
no clothes; whole body filled with dense graphite-like scribble cross-hatching. LIMB COUNT HARD LOCK: exactly
TWO thin arms and exactly TWO short legs — count them before finalizing; a third arm, a third leg, an extra
hand or a split limb is a blocking defect. The pen is OPTIONAL ... Mozai is INSIDE the scene and interacts
with its props — never a corner sticker floating beside text blocks.
```

## 已验证的五个布局家族（按页轮换，防排版单一）

| 家族 | 场景骨架 | 文字落点 |
|---|---|---|
| 群像围观 | 教室课间，几个孩子背影围看一部手机，墨仔踮脚凑看 | 标题+波浪线；下方 2-3 行 caption（pastel 圆点+短句） |
| 思想气泡 | 孩子伏案背影，头顶 2-3 个气泡写短问句，墨仔坐桌角抱笔记本 | 气泡内问句；下方编号答句条 |
| 英雄物件 | 超大主体物（如挂三把锁的手机），墨仔爬梯子操作 | 标题+波浪线；下方与物件对位的名称+短句行 |
| 台阶立面 | 三级木台阶从左下到右上，孩子背影向上爬，墨仔在旁加油 | 台阶立面各写一行短句；顶部小旗 |
| 告别收束 | 黄昏街道孩子骑车远去（车筐放手机），墨仔路边挥手 | 标题+波浪线；2-3 行信号行+结论行（细铅笔线上） |

## 页码与落盘

- 页码「NN/总页数」手绘小圆圈，左上角固定；封面无页码。
- 后处理链与封面相同：`Contrast 1.04 → Color 0.72 → 白平衡迭代至(254, 251.5, 246.5) → 14×19 暖斑 → JPEG q92 + FF D8 FF 校验`；尺寸 1024×1365；版本化文件名禁覆盖。

## 校准记录

- 2026-09-12 v3→v4：首版墨仔 26% 页高超标被打回 → Prompt 写「strictly SMALL, clearly smaller than one content block」后收敛到 9-15%。
- P4 标题被自动补「。」→ CONTENT 中写「the last character must be X, NEVER add a period」后修复；波浪线也曾画到第一行下 → 明确「directly under the SECOND/LAST line」。
- judge 误判教训：验收 Prompt 必须写清「边框铅笔涂鸦/笔筒道具不算墨仔持笔违规」，否则会把风格元素当缺陷。
