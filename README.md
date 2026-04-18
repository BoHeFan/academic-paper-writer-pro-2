<div align="center">

# Academic Paper Writer Pro 2

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-BoHeFan/academic--paper--writer--pro--2-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BoHeFan/academic-paper-writer-pro-2)
[![License](https://img.shields.io/github/license/BoHeFan/academic-paper-writer-pro-2?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/BoHeFan/academic-paper-writer-pro-2?style=for-the-badge&logo=github&color=yellow)](https://github.com/BoHeFan/academic-paper-writer-pro-2/stargazers)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-当前语言-red?style=flat-square)](#)

<br/>

一个专业的 AI Agent Skill，用于辅助学术论文的研究、撰写、排版与**降AI率**。<br/>
本 Skill 强制执行结构化的工作流程，利用精准的 `.docx` 和 `.pdf` 处理能力，<br/>
确保您的文稿严格符合各类学术格式要求（如 IEEE、ACM、Springer、NeurIPS、MLA、APA 及各类高校模板）。<br/>
**🆕 新增 Pipeline E 降AI率功能**：支持中文改写和英文LaTeX去AI化，有效降低AI检测率。

</div>

---

## 🆕 与原版的区别 (What's New)

本项目基于 [TFboy1/academic-paper-writer](https://github.com/TFboy1/academic-paper-writer) 进行增强开发，主要新增以下功能：

### 新增 Pipeline E — 论文降AI率管道

| 功能模块 | 文件路径 | 说明 |
|----------|----------|------|
| **Pipeline E 主模块** | `ai_reduction/SKILL.md` | 降AI率管道完整规范 |
| **中文改写规则** | `ai_reduction/prompts/chinese_rewrite.md` | 动词扩展、词汇替换、句式调整 |
| **英文LaTeX去AI化** | `ai_reduction/prompts/english_latex.md` | 词汇规范化、结构自然化 |

### 核心功能对比

| 功能 | 原版 | Pro 2 版本 |
|------|------|-----------|
| PDF OCR 管道 (Pipeline A) | ✅ | ✅ |
| Word 重排版管道 (Pipeline B) | ✅ | ✅ |
| Markdown 直转管道 (Pipeline C) | ✅ | ✅ |
| 内容智能生成 (Pipeline D) | ✅ | ✅ |
| **降AI率管道 (Pipeline E)** | ❌ | ✅ **新增** |
| 中文改写规则 | ❌ | ✅ **新增** |
| 英文LaTeX去AI化 | ❌ | ✅ **新增** |
| 技术术语自动保护 | ❌ | ✅ **新增** |

### Pipeline E 功能详解

#### 中文改写规则
- **动词扩展**：`管理` → `开展...的管理工作`
- **词汇替换**：`采用` → `运用`、`基于` → `鉴于`、`利用` → `借助`
- **句式调整**：使用"把"字句、条件句转换
- **技术术语保护**：自动识别并保护 Django、API、JWT 等技术术语

#### 英文LaTeX去AI化
- **词汇规范化**：`leverage` → `use`、`delve into` → `investigate`
- **移除机械表达**：删除 `First and foremost`、`It is worth noting that` 等
- **列表转段落**：将 `itemize/enumerate` 转换为连贯段落
- **修改阈值控制**：原文已足够自然则保留，不强制修改

---

## 1. 环境准备 (Prerequisites)

在使用本 Skill 之前，您需要一个支持文件操作和命令行工具的 Agentic 环境。我们支持以下两种主流环境：

### 选项 A: OpenCode (推荐)
一个专为开发者工作流优化的开源 Agentic 框架。
- **安装指南**: [OpenCode 官方文档](https://github.com/code-yeongyu/oh-my-opencode)
- **快速安装**:
  - **桌面版**: https://opencode.ai/download
  - **命令行版**:
  ```bash
  npm install -g opencode
  ```

### 选项 B: Claude Code
Anthropic 官方推出的 Agentic CLI 工具。
- **安装指南**: [Claude Code 官方文档](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- **注意**: 请确保您的环境中已安装 `git` 和 `npm`。

---

## 2. 安装说明 (Installation)

考虑到不同用户的使用环境，我们提供了 **一键自动化安装** 和 **手动配置** 两种方式。

### 选项一：一键自动化安装 (推荐)

如果您使用的是兼容的 Agentic 框架（如 Claude Code 或 OpenCode），只需在您的工作目录下运行以下一条命令：

```bash
npx skills add https://github.com/BoHeFan/academic-paper-writer-pro-2 --skill academic-paper-writer-pro-2
```

### 选项二：手动克隆与配置

如果受限于网络或框架环境无法使用一键安装，请按以下步骤手动导入本 Skill：

#### 1. 克隆仓库

```bash
git clone https://github.com/BoHeFan/academic-paper-writer-pro-2.git ./agent/skills/academic-paper-writer-pro-2
```

#### 2. 加载 Skill
- **对于 OpenCode**: Agent 会自动检测配置路径下的 Skills。您可能需要重启会话，或显式要求 Agent "加载 academic-paper-writer-pro-2 skill"。
- **对于 Claude Code**: 您可以通过在上下文窗口中提供此目录，或挂载该目录，指示 Claude 将其作为工具集使用。

---

## 3. 使用指南 (Usage Guide)

安装完成后，您可以直接使用自然语言控制整个写作与排版流程。

### 场景一：纯小白一键自动写论文 🚀

如果您没有任何撰写基础，手中仅有项目代码或一份简单的立项任务书：

1. **投喂资料与启动**：将您的项目代码文件夹的绝对路径告诉大模型，或将其拖入当前工作目录。
2. **下达指令**：
   > "阅读这个项目代码里的数据库和源码逻辑，帮我写一篇不少于15000字的毕业设计论文。要求：写完后直接使用 `academic-paper-writer-pro-2` 技能进行全自动排版，并最终导出成学校要求的 Word 文档！"
3. **等待完成**：Agent 将自动完成 **解析代码 → 列举大纲 → 逐章节扩写 → 渲染架构图 → 排版打包** 的全流程。
4. **提取成品**：前往 `outputs/` 文件夹提取 Word 成品。

---

### 场景二：已有草稿的专业学术排版

如果您已经完成了论文的中期草稿（支持 Markdown、Word、PDF 等格式）：

#### 准备文件
1. **论文草稿 (Draft)**：Markdown、Text 或 Word 文档
2. **格式规范/模板 (Style Guide)**：`IEEE_Template.docx` 或 `Submission_Guidelines.pdf`
3. **参考文献 (Optional)**：`.bib` 格式的参考文献库

#### 下达排版指令

**无需提供模板：**
> "请使用 `academic-paper-writer-pro-2` 技能，把这篇 Word 论文草稿按 IEEE 格式重新排版。"
> "使用 `academic-paper-writer-pro-2` 技能，将这个 Markdown 转换为 Springer LNCS 格式的 Word 文档。"
> "调用 `academic-paper-writer-pro-2` 帮我把这篇毕业论文换成严格的中国学位论文规范格式。"

**提供自定义模板：**
> "使用 `academic-paper-writer-pro-2` 排版这篇草稿。我已经放好了自定义的 Word 模板文件。"

---

### 场景三：论文降AI率处理 🆕

如果您担心论文被AI检测工具识别，可以使用新增的 **Pipeline E 降AI率功能**。

#### 功能特点

| 功能 | 说明 |
|------|------|
| **中文改写** | 动词扩展、词汇替换、句式调整，保持技术术语不变 |
| **英文LaTeX去AI化** | 词汇规范化、结构自然化、移除机械表达 |
| **技术术语保护** | 自动识别并保护 Django、API、JWT 等技术术语 |
| **字数控制** | 中文模式输出不超原文，避免膨胀 |

#### 使用方式

**方式一：独立使用**
```
"使用 ai-reduction 功能对这篇论文进行降AI率处理"
"帮我降低这篇论文的AI检测率"
"对这个 LaTeX 文件进行去AI化"
```

**方式二：Pipeline D 后自动调用**
在论文内容生成完成后，系统会询问：
> "论文初稿已生成。是否需要自动进行降AI率处理？"

**方式三：指定语言模式**
```
"使用 ai-reduction 的中文模式改写这段文字"
"对这个英文 LaTeX 片段进行去AI化处理"
```

#### 支持的格式

| 格式 | 说明 |
|------|------|
| `.md` | Markdown 文件，按段落/章节处理 |
| `.tex` | LaTeX 源文件，保持格式改写 |
| `.docx` | Word 文档，提取内容后处理 |
| 纯文本 | 直接处理 |

#### 示例效果

**中文改写示例：**

| 原文 | 改写后 |
|------|--------|
| 本系统采用Django框架进行开发，通过RESTful API实现前后端交互。 | 本系统选用Django框架来开展开发工作，借助RESTful API来实现前后端的交互。 |
| 基于MySQL数据库存储数据，利用Redis进行缓存处理。 | 鉴于MySQL数据库来存储数据，借助Redis开展缓存处理工作。 |

**英文LaTeX去AI化示例：**

| 原文 | 改写后 |
|------|--------|
| `First and foremost, we leverage the transformer architecture to delve into the nuanced patterns.` | `We use the transformer architecture to examine the subtle patterns in the data.` |
| `It is worth noting that this approach is paramount for achieving robust performance.` | `This approach is critical for achieving reliable performance.` |

---

## 4. 项目结构 (Project Structure)

```
academic-paper-writer-pro-2/
├── SKILL.md                    # 主入口（Pipeline 路由 + 排版规范库）
├── ai_reduction/               # 🆕 Pipeline E: 降AI率模块
│   ├── SKILL.md                # 降AI率管道规范
│   └── prompts/
│       ├── chinese_rewrite.md  # 中文改写规则
│       └── english_latex.md    # 英文LaTeX去AI化规则
├── content_generation/         # Pipeline D: 内容智能生成
├── docx/                       # Word 文档操作
├── pdf/                        # PDF 操作
├── ocr_kb/                     # Pipeline A: OCR 管道
├── templates/                  # 格式模板 (IEEE, ACM, APA 等)
├── examples/                   # 示例文件
├── resources/                  # 资源目录
└── README.md                   # 本文件
```

---

## 5. 资源库 (Resources)

本仓库提供了一些内置资源以帮助您快速上手：

*   📂 **`templates/`**: 包含 IEEE, ACM, APA 等主流学术会议/期刊的官方模板下载链接。
*   📂 **`examples/`**: 包含一份标准论文草稿 (`draft.md`) 和样式指南 (`style_guide.md`)，用于测试 Skill 的功能。
*   ❓ **`TROUBLESHOOTING.md`**: 常见问题排查指南（如格式错乱、引用丢失等）。

---

## 6. 致谢 (Credits & Acknowledgments)

本项目基于以下开源项目进行增强开发：

*   **原项目**: [TFboy1/academic-paper-writer](https://github.com/TFboy1/academic-paper-writer) - 提供了完整的学术论文写作与排版框架
*   **Academic Writing Pipeline**: 核心的**反幻觉诚信门禁 (Integrity Gate)** 与**多视角自审评议面板 (Multi-Perspective Review)** 机制，深度借鉴并致敬了由 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 提出的 AI 学术写作质量管控框架
*   **Docx & PDF Operations**: 感谢 [Anthropic Skills Repository](https://github.com/anthropics/skills) 提供了与 Microsoft Word 和 PDF 文档交互的基础逻辑

---

## 7. License

本项目采用与原项目相同的开源协议。

---

<div align="center">

**如果这个项目对您有帮助，请给一个 ⭐ Star 支持一下！**

[![Star History Chart](https://api.star-history.com/svg?repos=BoHeFan/academic-paper-writer-pro-2&type=Date)](https://star-history.com/#BoHeFan/academic-paper-writer-pro-2&Date)

</div>
