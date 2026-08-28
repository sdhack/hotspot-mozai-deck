# Hotspot Mozai Deck · 墨仔热点图文自动化

> 从热点搜索 → 候选选题 → 4页墨仔(Seedling) handdrawn 配图 → 配套文案的全流程自动化 Skill

适用于抖音/小红书竖版图文，墨仔 IP 出镜，手绘风格统一。

---

## ✨ 特性

- **端到端流水线**：搜热点 → 选选题 → 出图 → 写文案 → 交付，一步到位
- **墨仔 IP 一致性**：内置 Seedling 人物卡 + 角色锁，每页形象严格统一
- **手绘风格统一**：暖白纸 + cross-hatching + 装饰角 + 双线边框 + 手写中文字体
- **4 页标准结构**：封面（钩子）+ P2（问题/分析）+ P3（方案/深度）+ P4（落点/互动）
- **配套文案**：墨仔第一人称，200-300 字，6 段结构，去 AI 味
- **QA 检查清单**：7 大类检查项，交付前自动核验

---

## 📦 安装

### 方式 1：从 GitHub 安装（推荐）

```bash
# 克隆到 Doubao user_skills 目录
git clone https://github.com/helloianneo/hotspot-mozai-deck.git \
  ~/.doubaowork/agent_mode/workspace/.user_skills/hotspot-mozai-deck
```

### 方式 2：手动安装

1. 下载本仓库 ZIP
2. 解压到 `~/.doubaowork/agent_mode/workspace/.user_skills/hotspot-mozai-deck/`
3. 重启 Doubao，Skill 自动加载

### Windows 路径

```
C:\Users\<用户名>\AppData\Local\DoubaoWork\User Data\Default\.doubaowork\agent_mode\workspace\.user_skills\hotspot-mozai-deck\
```

---

## 🚀 使用

### 用法 1：自动搜热点

```
用户：用 hotspot-mozai-deck 出今天的热点图文
```

→ 自动搜索当天热点 → 整理 5 个候选选题 → 你选编号 → 出 4 张图 + 文案

### 用法 2：指定热点

```
用户：用 hotspot-mozai-deck 做"XXX事件"
```

→ 跳过搜索，直接用你指定的热点出图 + 文案

### 用法 3：只出图

```
用户：用 hotspot-mozai-deck 出图，文案我自己写
```

→ 只出 4 张图，不生成文案

---

## 📁 目录结构

```
hotspot-mozai-deck/
├── SKILL.md                          # 主文件：5步工作流 + 资源地图
├── README.md                         # 本文件
├── LICENSE                           # MIT 许可证
├── .gitignore                        # Git 忽略规则
├── assets/
│   └── seedling-character-sheet.png # Seedling 人物卡（image-to-image 参考）
└── references/
    ├── style-lock.md                 # 通用风格锁（暖白纸+cross-hatching+装饰角）
    ├── character-lock.md             # Seedling 角色锁（精确描述+嘴巴表情库）
    ├── prompt-template.md            # 4页完整 prompt 模板（含变量占位符）
    ├── hotspot-template.md           # 热点搜索策略 + 5候选选题整理模板
    ├── copy-template.md              # 配套文案模板（墨仔第一人称，6段结构）
    └── qa-checklist.md               # 交付前检查清单（7大类）
```

---

## 🎨 墨仔/Seedling 角色设定

| 要素 | 描述 |
|---|---|
| 身体 | 圆胖黑色泪滴/水滴形，哑光墨黑+铅笔/蜡笔涂鸦纹理 |
| 头顶 | 细卷发须 + 螺旋形线圈 + 两片浅鼠尾草绿叶 |
| 眼睛 | 大圆眼 + 大白眼白 + 黑瞳孔，常不对称（一大一小） |
| 嘴巴 | 深红/暗红，每页表情不同（惊讶O/认真一字/坚定抿嘴/友好微笑等） |
| 四肢 | 恰好两条细黑手臂 + 两条短粗腿 |
| 其他 | 脚下小阴影，儿童绘本风格 |

> ⚠️ 每页仅一个角色，绝不出现多个。

---

## 📐 4 页标准结构

| 页 | 类型 | 内容 | 墨仔动作 |
|---|---|---|---|
| 封面 | 钩子 | 热点事件 + 反常识/情绪钩子 | 惊讶/困惑表情，举牌子或指方向 |
| P2 | 问题/分析 | 3 个卡片/要点，拆解问题 | 持放大镜审视，认真表情 |
| P3 | 方案/深度 | 3 个步骤/做法 + 金句框 | 持清单核对，坚定表情 |
| P4 | 落点/互动 | 温暖场景 + 举牌 + 对话气泡 | 举牌子，友好微笑 |

---

## 🛠️ 技术栈

- **图像生成**：`image_edit`（image-to-image，传入人物卡参考）
- **热点搜索**：`general_search`
- **文件交付**：`present_files`
- **风格**：refined Chinese handdrawn technical illustration
- **格式**：3:4 竖版 1080x1440（抖音/小红书适配）

---

## 📝 版本历史

| 版本 | 日期 | 变更 |
|---|---|---|
| 1.0.0 | 2026-08-28 | 初始版本，5步工作流 + 7个参考文件 + Seedling人物卡 |
| 1.1.0 | 2026-08-28 | 完善文档：添加快速开始/用法示例/故障排除/版本历史；更新 guardrails；添加 README.md |

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## ⚠️ 免责声明

使用本 Skill 前请阅读仓库根目录的 DISCLAIMER。使用者自行承担输入、输出、数据处理和发布责任。
