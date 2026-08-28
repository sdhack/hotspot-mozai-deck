# Character Lock · Seedling 角色锁

从用户上传的 Seedling 人物卡（`assets/seedling-character-sheet.png`）提取的精确角色描述。每个页面 prompt 必须包含，逐字复制。

---

## 完整角色锁（复制到每页 prompt）

```
=== SEEDLING CHARACTER (strictly match reference image) ===
CRITICAL: Match reference EXACTLY. Round plump black teardrop creature (plump water drop, NOT slim, NOT elongated). Matte ink-black body with visible pencil/crayon scribble texture (not flat black, has textured strokes). Thin curly tendril with spiral-shaped coil loop + TWO light sage-green leaves (exactly two leaves, not one, not three). LARGE round eyes with big white eye whites and black pupils (pupils often slightly asymmetrical - one eye may look slightly larger or offset, expressive). DEEP RED/DARK CRIMSON mouth (expression varies per page). Exactly TWO thin black arms and exactly TWO thin black legs (short stubby legs). Small shadow under feet. Cute expressive children's book illustration feel. EXACTLY ONE character on page, never two or more.
```

---

## 角色要素拆解

| 要素 | 描述 | 常见错误（必须避免） |
|---|---|---|
| 身体形状 | round plump black teardrop（圆胖黑色泪滴/水滴形） | slim/elongated（修长）、spherical（球形）、pointed top（尖顶） |
| 身体质感 | matte ink-black with pencil/crayon scribble texture（哑光墨黑+铅笔/蜡笔涂鸦纹理） | flat black（纯平黑）、shiny（发光）、hard silhouette（硬剪影） |
| 头顶卷须 | thin curly tendril with spiral-shaped coil loop（细卷发须+螺旋形线圈） | simple loop（简单圆圈）、straight stem（直茎）、no tendril（无卷须） |
| 叶子 | TWO light sage-green leaves（两片浅鼠尾草绿叶） | one leaf（一片）、three leaves（三片）、no leaves（无叶）、dark green（深绿） |
| 眼睛 | LARGE round eyes with big white whites + black pupils（大圆眼+大白眼白+黑瞳孔），常不对称 | tiny white-dot eyes（小白点眼）、centered pupils（瞳孔居中）、no eyes（无眼）、extremely large chibi eyes（超大萌系眼） |
| 嘴巴 | DEEP RED/DARK CRIMSON（深红/暗红），每页表情不同 | black mouth（黑嘴）、no mouth（无嘴）、same shape every page（每页同形状） |
| 手臂 | exactly TWO thin black arms（恰好两条细黑手臂） | extra limbs（多余肢体）、missing arms（缺手臂）、three arms（三臂） |
| 腿 | exactly TWO short stubby legs（恰好两条短粗腿） | extra legs（多余腿）、missing legs（缺腿）、long legs（长腿） |
| 阴影 | small shadow under feet（脚下小阴影） | no shadow（无阴影）、large shadow（大阴影） |
| 数量 | EXACTLY ONE character（恰好一个角色） | multiple characters（多个角色）、two characters（两个） |

---

## 嘴巴表情库（每页必须不同，4页至少3种）

| 表情 | 描述 | 适用场景 |
|---|---|---|
| surprised O | 惊讶O形嘴，小开口 | 封面、突发事件、震惊 |
| serious line | 认真一字嘴，直线或微弯 | 分析问题、清单核对 |
| determined press | 坚定抿嘴，嘴角微下撇 | 解决方案、行动号召 |
| friendly smile | 友好微笑，上弯弧线 | 落点、温暖场景、互动 |
| curious O | 好奇O形嘴，小而圆 | 探索、观察、提问 |
| happy laugh | 开心大笑，张嘴露齿 | 轻松、幽默、积极 |
| confused small | 困惑小嘴，微张或波浪线 | 不解、质疑、反常识 |

**规则**：4页中至少出现3种不同嘴型。封面常用 surprised O 或 confused small。落点页（P4）常用 friendly smile。

---

## 角色尺寸与位置

- 活跃状态时占页面高度 **12-22%**，绝不填满页面
- 位置：封面常在 lower center（下中），正文页常在 right side（右侧）或 lower-left（左下）
- 角色是**动作主体**（actor），不是角落装饰——它必须在做与页面主题相关的动作（拿清单、指方向、举牌子、持放大镜等）

---

## image-to-image 参考

生成时必须传入 `assets/seedling-character-sheet.png` 的 URL 作为 `image_reference_url_list`，用 image_edit 工具（不是 image_gen），确保角色形象严格匹配人物卡。
