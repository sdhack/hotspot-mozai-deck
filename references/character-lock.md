# 墨仔角色规范

## 身份锚点

1. 圆润墨滴形身体，不是球形、细长水滴或人形躯干；
2. 黑色墨迹质感，边缘有自然手绘变化，不是塑料 3D；
3. 头顶一根微卷细茎；
4. 恰好两片浅鼠尾草绿色叶子；
5. 大圆眼、眼白明显，瞳孔可轻微不对称；
6. 小比例黑色嘴，表情克制；
7. 正常情况下恰好两条细手臂和两条短腿；
8. 无腮红、无衣服或未经要求的拟人身体部件。

人物卡是视觉真值，文字描述用于补充而非覆盖人物卡。始终使用 `assets/mozai-ip-sheet-4k.jpg` 作为唯一人物参考。

## 体态一致锁（2026-09-10 用户规则，P0 阻断项）

同一套图文的所有页面中，墨仔的身体形状与比例必须完全一致，禁止出现"这页高、那页胖、另一页圆球"的漂移。以 4K 人物卡为真值，逐页 Prompt 的 CHARACTER 段必须写入以下锁定描述（中/英按渠道选用）：

- 身体是**上窄下宽的梨形/水滴形**：高约为宽的 1.1–1.2 倍，底部圆胖、重心下沉，向上平滑收窄，在顶端收出一个小尖角，芽茎从尖角长出；
- **不是正圆、不是球形、不是鸡蛋形、不是细长泪滴、不是人形躯干**；
- 眼睛占身体上半部约三分之一，位置与大小跨页一致；手臂与腿的粗细、长短跨页一致；
- 整套图内墨仔的"胖瘦高矮"不得随页面布局、占比或道具改变：占比缩放只等比缩放整体，不改变身体宽高比。

英文锁（供 Prompt 母版使用）：

```text
BODY SHAPE LOCK (identical on every page of the set): a plump pear/teardrop ink-drop body,
height about 1.1-1.2x its width, round heavy bottom, tapering smoothly to a small point at
the top where the sprout stem grows; NOT a perfect circle, NOT a ball, NOT an egg, NOT a
tall slim teardrop. Scaling the character up or down must never change this proportion.
```

成图后 QA 时把该页墨仔与人物卡及前页并排比对：身体宽高比或轮廓家族（梨形 vs 圆球 vs 鸡蛋）不一致即为阻断缺陷，只重做该页。

## 持笔道具（笔型自由，2026-09-10 用户规则更新）

- 默认右手清楚持握一支笔：毛笔、铅笔、钢笔、圆珠笔、马克笔均可，按页面主题选择最贴合的一种；这是 v1.9 的持笔锚点，应在每页 Prompt 中显式声明，但**笔型不再是毛笔专属**；
- 同一页内笔必须与手真实接触（手指包裹笔杆，不悬空不分家）；同一套图内笔型可以按页主题变化（如校园页铅笔、出行页钢笔），但持握方式一致；
- 双手动作：双手优先完成主题动作时，笔放在紧邻场景中且保持清晰可见；不得无故省略；
- 禁止为了同时拿多个道具生成第三只手；
- 笔不得误变成魔杖、武器或无法辨认的棍状物。

## 动作与表情

动作必须服务页面内容。观察页可托腮、记录或看放大镜；方法页可指向步骤、勾选清单或扶盾牌；情绪或收束页可挥手、递话筒或举手提问。这里是例子，不是固定映射。

系列页避免全部使用同一姿态。情绪连续时允许相近表情，只需在构图、视线、手势或身体朝向中至少改变一项。不要为了差异化选用与内容冲突的表情。

张嘴时保持小比例，可以看见简单口腔层次；不强制每个张嘴表情都出现红色舌头。闭嘴、微笑、疑问和认真表情均可。

## 尺寸与位置

- 角色至少应让用户看清眼睛、芽叶、四肢和关键手势；
- 内容主导页中角色不抢主信息，但仍是可辨认的次要视觉主体。解释、步骤、对比和提醒页默认让信息卡、关键词组或手绘场景占据中心；墨仔放在边角，以指向、观察、勾选或递话筒等动作服务阅读，不复制封面的角色中心构图；
- 角色主导页可居中或占较大面积；
- 场景叙事页让角色自然融入场景，不必永远站在左右下角。

角色周围保留低噪声安全区：不放文字或高对比图标；暖白纸纹理、极淡网格可以穿过安全区。

## 参考图选择

| 需求 | 参考图 |
|---|---|
| 常规、侧面或背面动作 | 4K 主卡；用文字和场景说明补充动作方向 |
| 特定表情或姿势 | 4K 主卡；用文字明确当前表情和姿势 |
| 理解性格或文字设定 | 阅读本文件，不额外加入人物卡 |

始终使用 4K 主卡作为唯一参考图，不拼接或补入其他人物卡。生成后检查人物卡文字、示意角色或卡片布局没有出现在成图中。

## Prompt 片段

按当前页动作删改，不要逐字复制不适用内容：

```text
=== CHARACTER ===
Exactly one Mozai character, matching the supplied reference: a plump pear/teardrop black ink-drop body (height about 1.1-1.2x width, round heavy bottom tapering to a small point at the top — never a perfect circle, ball or egg; identical proportion on every page of this set) with organic hand-drawn ink texture; one thin slightly curled sprout stem with exactly two light sage-green leaves; large round eyes with visible white sclera and subtly asymmetric pupils; a small restrained black mouth; exactly two thin arms and two short legs; no blush. The character is [action] with [expression]. [Prop rule for this action: a pen, pencil, fountain pen or brush chosen for the page theme, fingers wrapped around the shaft.]
```

优先修复重复角色、叶片数量、肢体数量、身体形状和五官，其次修复动作与场景。装饰性误差不应无限重试。同一页最多两次定向重试；仍失败时减少动作复杂度、使用更干净的参考图或说明限制。
