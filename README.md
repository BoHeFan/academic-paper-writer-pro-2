<div align="center">

# Academic Paper Writer Pro 2

<img src="resources/banner.svg" alt="Academic Paper Writer Pro 2 Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install%20Skill-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer-pro-2/academic-paper-writer-pro-2)
[![爱发电](https://img.shields.io/badge/爱发电-Support%20Me-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/TFboy1/academic-paper-writer/stargazers)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-当前语言-red?style=flat-square)](#)
[![English](https://img.shields.io/badge/English-README-blue?style=flat-square)](docs/README_EN.md)

<br/>

一个专业的 AI Agent Skill，用于辅助学术论文的研究、撰写、排版与**降AI率**。<br/>
本 Skill 强制执行结构化的工作流程，利用精准的 `.docx` 和 `.pdf` 处理能力，<br/>
确保您的文稿严格符合各类学术格式要求（如 IEEE、ACM、Springer、NeurIPS、MLA、APA 及各类高校模板）。<br/>
**🆕 新增 Pipeline E 降AI率功能**：支持中文改写和英文LaTeX去AI化，有效降低AI检测率。

</div>


## 1. 环境准备 (Prerequisites)

在使用本 Skill 之前，您需要一个支持文件操作和命令行工具的 Agentic 环境。我们支持以下两种主流环境：

### 选项 A: OpenCode (推荐)
一个专为开发者工作流优化的开源 Agentic 框架。
- **安装指南**: [OpenCode 官方文档](https://github.com/code-yeongyu/oh-my-opencode)
- **快速安装**:
  - **桌面版**:
https://opencode.ai/download
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

> **🔗 官方 Skill 主页**: [https://skills.sh/tfboy1/academic-paper-writer-pro-2/academic-paper-writer-pro-2](https://skills.sh/tfboy1/academic-paper-writer-pro-2/academic-paper-writer-pro-2)

### 选项一：一键自动化安装 (推荐)
如果您使用的是兼容的 Agentic 框架（如 Claude Code 或 OpenCode），只需在您的工作目录下运行以下一条命令，系统将自动拉取代码仓库并配置依赖，免去手动操作：

```bash
npx skills add https://github.com/TFboy1/academic-paper-writer-pro-2 --skill academic-paper-writer-pro-2
```

### 选项二：手动克隆与配置
如果受限于网络或框架环境无法使用一键安装，请按以下步骤手动导入本 Skill：

#### 1. 克隆仓库
导航至您的 Agent 工作区或 Skills 目录，并克隆本仓库：

```bash
# 克隆到您的 skills 目录
git clone https://github.com/TFboy1/academic-paper-writer-pro-2.git ./agent/skills/academic-paper-writer-pro-2
```

#### 2. 加载 Skill
- **对于 OpenCode**: Agent 会自动检测配置路径下的 Skills。您可能需要重启会话，或显式要求 Agent "加载 academic-paper-writer-pro-2 skill"。
- **对于 Claude Code**: 您可以通过在上下文窗口中提供此目录，或挂载该目录，指示 Claude 将其作为工具集使用。

---

## 3. 使用指南 (Usage Guide)

安装完成后，您可以直接使用自然语言控制整个写作与排版流程。

### 场景一：纯小白一键自动写论文 (Auto Thesis Writing) 🚀
如果您没有任何撰写基础，手中仅有项目代码或一份简单的立项任务书，您可以让 AI 从零开始为您**“先创作，后排版”**，全自动生成上万字的毕业设计或学术论文：

1. **投喂资料与启动**：只需启动您的 Agent，并将您的项目代码文件夹的绝对路径告诉大模型，或者将其拖入当前工作目录。
2. **下达小白“魔法指令”**：
   > “阅读这个项目代码里的数据库和源码逻辑，帮我写一篇不少于15000字的毕业设计论文。要求：写完后直接使用 `academic-paper-writer-pro` 技能进行全自动排版，并最终导出成学校要求的 Word 文档！”
3. **喝杯咖啡等待极客魔法**：Agent 将接管所有的脑力与体力劳动。它的运作逻辑为：**解析代码功能 -> 列举 IMRAD 标准学术大纲 -> 逐章节展开深度学术扩写 -> 设计并渲染出高清全彩架构图 (分离Mermaid渲染PNG) -> 最终调用排版引擎将大段文字与图片严丝合缝打包至 `.docx` 中。**
4. **一键提取与提交**：待 AI 弹出完成报告后，前往本目录下的 `outputs/` 文件夹直接提取装订成册的 Word 成品！所有生成的架构图原文件也会被悉心收藏在 `resources/figures/` 供您单独取用。

---

### 场景二：已有草稿的专业学术排版 (Professional Typesetting)
如果您已经靠自己完成了论文的中期草稿（支持 Markdown、Word、PDF 等格式文件），只需借助本技能完成最终的底层无损学术排版。

#### 第一步：准备文件
为您的论文创建一个工作目录，并准备以下核心文件：
1.  **论文草稿 (Draft)**：您的原始内容（Markdown、Text 或粗糙的 Word 文档）。
2.  **格式规范/模板 (Style Guide)**：目标格式要求（例如 `IEEE_Template.docx` 或 `Submission_Guidelines.pdf`）。
3.  **参考文献 (Optional)**：`.bib` 格式的参考文献库（推荐提供，以确保引用准确）。

#### 第二步：启动 Agent
启动您的 Agent 并指向您的工作目录。

```bash
# OpenCode 示例
opencode
```

#### 第三步：下达排版指令
使用自然语言指令启动排版工作流。本系统内置了多种主流学术规范（IEEE、ACM、Springer LNCS、NeurIPS、APA、MLA 及中国学位论文格式）。直接对 Agent 说：

**无需提供模板的直接排版指令 (Prompts):**
> "请使用 `academic-paper-writer-pro-2` 技能，把这篇 Word 论文草稿按 IEEE 格式重新排版。"
> "使用 `academic-paper-writer-pro-2` 技能，将这个 Markdown 转换为 Springer LNCS 格式的 Word 文档。"
> "调用 `academic-paper-writer-pro-2` 帮我把这篇毕业论文换成严格的中国学位论文规范格式。"

**提供自定义模板的排版指令 (Prompts):**
> "使用 `academic-paper-writer-pro` 排版这篇草稿。我已经放好了自定义的 Word 模板文件。"
> "使用 `academic-paper-writer-pro` 技能，根据文件夹里这个 PDF 指南帮我无损修正论文的引文格式与排版布局。"

#### 接下来会发生什么？
1.  **自动研判 (Analysis)**：Agent 验证资料并提取特定的字体、边距、引用样式等要求。
2.  **底层执行 (Execution)**：Agent 将通过无损的三线表还原、公式转换（原生OMML）以及高清图片挂载，生成一份符合规范的排版版本。
3.  **最终输出与精调 (Refinement)**：排版完毕的 `.docx` 将保存在 `outputs/` 目录。您可以随时进一步指令：“检查第三节逻辑”，或是 “为这些图表补全说明文字”。

---

### 场景三：论文降AI率处理 (AI Detection Rate Reduction) 🆕

如果您担心论文被AI检测工具识别，可以使用新增的 **Pipeline E 降AI率功能**，将AI生成的文本改写为更自然的学术表达。

#### 功能特点

- **中文改写**：动词扩展、词汇替换、句式调整，保持技术术语不变
- **英文LaTeX去AI化**：词汇规范化、结构自然化、移除机械表达
- **技术术语保护**：自动识别并保护所有技术术语不被修改

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

**中文改写示例**：

原文：
```
本系统采用Django框架进行开发，通过RESTful API实现前后端交互。
```

改写后：
```
本系统选用Django框架来开展开发工作，借助RESTful API来实现前后端的交互。
```

**英文LaTeX去AI化示例**：

原文：
```latex
First and foremost, we leverage the transformer architecture to delve into 
the nuanced patterns in the data.
```

改写后：
```latex
We use the transformer architecture to examine the subtle patterns in the data.
```

---

## 4. 资源库 (Resources)

本仓库提供了一些内置资源以帮助您快速上手：

*   📂 **`templates/`**: 包含 IEEE, ACM, APA 等主流学术会议/期刊的官方模板下载链接。
*   📂 **`examples/`**: 包含一份标准论文草稿 (`draft.md`) 和样式指南 (`style_guide.md`)，用于测试 Skill 的功能。
*   ❓ **`TROUBLESHOOTING.md`**: 常见问题排查指南（如格式错乱、引用丢失等）。

---

## 致谢 (Credits & Acknowledgments)

本项目在架构设计与底层文档处理上，深受开源社区诸多优秀项目的启发与支持：

*   **Academic Writing Pipeline**: 核心的**反幻觉诚信门禁 (Integrity Gate)** 与**多视角自审评议面板 (Multi-Perspective Review)** 机制，深度借鉴并致敬了由 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 提出的 AI 学术写作质量管控框架。感谢其在限制大模型幻觉及长文本一致性上的卓越前瞻设计！
*   **Docx & PDF Operations**: 感谢 [Anthropic Skills Repository](https://github.com/anthropics/skills) 提供了与 Microsoft Word 和 PDF 文档交互的基础逻辑，赋予了本系统精准的读取与打包能力。
