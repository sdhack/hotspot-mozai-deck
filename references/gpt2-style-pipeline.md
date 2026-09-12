# gpt-image-2（image2）统一风格流水线

目的：**任何 agent 不依赖会话记忆，只凭本技能即可用 image2 通道产出与既有成品同风格的墨仔图文**。本文件是端到端操作入口；模版细节见各引用文件。

## 0. 前置检查

- 依赖：`python` + `requests` + `numpy` + `Pillow`。
- Key：环境变量 `GPT2_API_KEY`，或技能本地文件 `assets/gpt2-api-key.txt`（该文件不入 git，公开仓库不含 key；缺失时脚本会明确报错）。接口为 `https://api.790053500.com/v1/images/edits`，模型 `gpt-image-2`；**只有 edits 端点可用**，generations 未订阅。
- 通道时效自检：正式批量前先跑 1 张小图验活；间歇 403(error 1010)/429/502 均为瞬时，退避 20s 重试即可（脚本已内置 4 次重试）。

## 1. 选模版并写 Prompt 文件（UTF-8 无 BOM）

| 任务 | 读取 | Prompt 骨架来源 |
|---|---|---|
| 封面 | [cover-template-style-ref.md](cover-template-style-ref.md) | CANVAS/STYLE/CHARACTER/LAYOUT/CONTENT/CONSTRAINTS/AVOID 全文，`[...]` 填当页内容 |
| 场景内页 | [scene-innerpage-template.md](scene-innerpage-template.md) | 同上，按五个布局家族逐页轮换 |
| 第二套浓黑排线（无风格参考图时） | [backup-prompt-gpt2.md](backup-prompt-gpt2.md) | 纯 Prompt 体系 + canvas 模式 |

Prompt 硬规则（写的时候就要带上，别等 QA）：标题末行下波浪线；标题末字后禁补标点；墨仔持笔可选、无笔页面禁多余手臂；恰好两臂两腿；儿童严格背影零面部；内页无红色；数字黑色。

## 2. 出图命令

```bash
# 封面 / 场景内页（双参考：assets/style-ref-cream-journal.jpg + assets/mozai-ip-sheet-4k.jpg）
python scripts/gen_gpt2_page.py --prompt page01.txt --out "01-封面-v1.jpg" --mode dual --seed 81

# 无风格参考图时的纯 Prompt 通道（拿一张自有成品页当纸张画布）
python scripts/gen_gpt2_page.py --prompt page02.txt --out "02-v1.jpg" --mode canvas --canvas 01-封面-v1.jpg --seed 71
```

脚本内置：双参考输入顺序（FIRST 风格参考、SECOND 人物卡）与整页替换声明、1024×1365、403/429/502 退避重试、拒绝覆盖已存在文件（强制版本化命名）、落盘后处理链（`Contrast 1.04 → Color 0.72 → 白平衡至(254,251.5,246.5) → 14×19 低频暖斑 → JPEG q92 + FF D8 FF 头校验`）。同页重试换 `--seed`。

## 3. 逐页 QA（只重做不合格页，同页最多两次定向重试）

1. 像素比 3:4、四侧留白 ≥20px、页码「NN/总页数」连续且位置一致（封面无页码）。
2. 文字逐字核对：无错字/异体/伪字（3 字小标签必须放大看）、标题末字后无多余标点、波浪线在标题末行下。
3. 墨仔：恰好两臂两腿（放大清点）、梨形体态高 1.1-1.2 倍宽、茎+两片绿叶、笔手贴合或无笔、无球形蛋形漂移、占比达标（内容页 ~9-15%，上限 18%）。
4. 人物安全：儿童背影零面部特征、无大人形象、屏幕空白无 logo、无品牌。
5. 观感：纸面近白不黄、黑线浓黑锐利、无灰雾、内页无红色元素。
6. 风格一致性：与已成页并排对比纸色/线重/点缀色，偏差明显即重做。

## 4. 已知坑（直接规避）

- 参考卡拼贴漏进画面 → 强化「appearance only」声明，第二次重试减少其他视觉干扰。
- 3 字小标签写成异体字 → 换措辞或重试，QA 放大核对。
- 墨仔画得过大 → Prompt 写「strictly SMALL, clearly smaller than one content block」。
- 验收 Prompt 别把「边框铅笔涂鸦/笔筒道具」当持笔违规，属既定风格语言。
- 文件名必须版本化（`-v2`、`-v4b`），严禁覆盖上一版；接口有日配额（429）。
