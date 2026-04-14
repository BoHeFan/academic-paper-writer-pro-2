<div align="center">

# Academic Paper Writer Pro

<img src="resources/banner.svg" alt="Academic Paper Writer Pro Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install%20Skill-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)
[![爱发电](https://img.shields.io/badge/爱发电-Support%20Me-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/tfboy1/academic-paper-writer/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.creem.io/payment/prod_1yc40mIhKwwrc7iqFOG9G2)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-当前语言-red?style=flat-square)](#)
[![English](https://img.shields.io/badge/English-README-blue?style=flat-square)](docs/README_EN.md)
[![日本語](https://img.shields.io/badge/日本語-README-blue?style=flat-square)](docs/README_JA.md)
[![Français](https://img.shields.io/badge/Français-README-blue?style=flat-square)](docs/README_FR.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-README-blue?style=flat-square)](docs/README_DE.md)

<br/>

一个专业的 AI Agent Skill，用于辅助学术论文的研究、撰写与排版。<br/>
本 Skill 强制执行结构化的工作流程，利用精准的 `.docx` 和 `.pdf` 处理能力，<br/>
确保您的文稿严格符合各类学术格式要求（如 IEEE、ACM、Springer、NeurIPS、MLA、APA 及各类高校模板）。

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

> **🔗 官方 Skill 主页**: [https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)

### 选项一：一键自动化安装 (推荐)
如果您使用的是兼容的 Agentic 框架（如 Claude Code 或 OpenCode），只需在您的工作目录下运行以下一条命令，系统将自动拉取代码仓库并配置依赖，免去手动操作：

```bash
npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro
```

### 选项二：手动克隆与配置
如果受限于网络或框架环境无法使用一键安装，请按以下步骤手动导入本 Skill：

#### 1. 克隆仓库
导航至您的 Agent 工作区或 Skills 目录，并克隆本仓库：

```bash
# 克隆到您的 skills 目录
git clone <your-repo-url> academic-paper-writer
```

#### 2. 加载 Skill
- **对于 OpenCode**: Agent 会自动检测配置路径下的 Skills。您可能需要重启会话，或显式要求 Agent "加载 academic-paper-writer skill"。
- **对于 Claude Code**: 您可以通过在上下文窗口中提供此目录，或挂载该目录，指示 Claude 将其作为工具集使用。

---

## 3. 使用指南 (Usage Guide)

安装完成后，您可以直接使用自然语言控制整个写作与排版流程。

### 第一步：准备文件
为您的论文创建一个工作目录，并准备以下核心文件：
1.  **论文草稿 (Draft)**：您的原始内容（Markdown、Text 或粗糙的 Word 文档）。
2.  **格式规范/模板 (Style Guide)**：目标格式要求（例如 `IEEE_Template.docx` 或 `Submission_Guidelines.pdf`）。
3.  **参考文献 (Optional)**：`.bib` 格式的参考文献库（推荐提供，以确保引用准确）。

### 第二步：启动 Agent
启动您的 Agent 并指向您的工作目录。

```bash
# OpenCode 示例
opencode
```

### 第三步：触发 Skill
使用自然语言指令启动工作流。我们的系统内置了多种主流学术期刊和会议的排版规范（包括 IEEE、ACM、Springer LNCS、NeurIPS、APA、MLA 以及中国学位论文格式），你可以直接指出你需要哪种格式。

**无需提供模板的直接排版指令 (Prompts):**
> "请把这篇 Word 论文草稿按 IEEE 格式重新排版。"
> "把这个 Markdown 转换为 Springer LNCS 格式的 Word 文档。"
> "将这部分内容按照 ACM 标准双栏格式排版。"
> "按照 NeurIPS 的要求进行单栏排版。"
> "使用 MLA 格式要求排版这篇人文学科作业。"
> "帮我把这篇毕业论文换成中国学位论文格式。"

**提供自定义模板的排版指令 (Prompts):**
> "帮我排版这篇论文。我已经在这个文件夹里放好了草稿和自定义的模板文件。"
> "根据这个 PDF 排版指南，帮我修正引文格式和排版布局。"

### 接下来会发生什么？
1.  **前置检查 (Pre-check)**：Agent 会验证您是否提供了草稿和格式指南。
2.  **深度解析 (Analysis)**：Agent 将读取 `.docx` 或 `.pdf` 格式指南，理解字体、边距、引用样式等要求。
3.  **执行排版 (Execution)**：Agent 将生成一份符合规范的论文版本，保存在 `outputs/` 目录中。
4.  **精细化调整 (Refinement)**：您可以进一步要求改进，例如 "检查第三节的逻辑" 或 "为这些图表生成说明文字"。

### 第四步：纯小白一键自动写论文 (Auto Thesis Writing) 🚀 
如果您没有任何开发基础，手中只有写了一半的代码，或者只有一个简单的立项任务书，您可以让 AI 从零开始为您**全自动生成成千上万字的毕业设计/长篇学术论文**：
1. **投喂资料**：只需将您的项目代码文件夹的位置告诉大模型，或者将他拖入拖入工作目录。
2. **下达小白“魔法指令”**：
   > “帮我阅读这个项目代码里的数据库和界面，写一篇不少于15000字的毕业设计论文。注意：用 `academic-paper-writer-pro` 技能全自动排版，并最终帮我导出成学校要求的 Word 文档！”
3. **喝杯咖啡等待极客魔法**：Agent 会立刻接管一切。它会自动帮您**列举高大上的 IMRAD 标准大纲 -> 逐章节进行学术扩写 -> 设计并渲染出高清全彩架构图 (Mermaid转PNG) -> 套用标准宋体/黑体生成严丝合缝的最终 `.docx`。**
4. **一键提交**：待 AI 提示执行完毕后，前往 `outputs/` 文件夹提取成品直接提交！如果有 AI 绘制的专属图片，它们也会整齐地归档在 `resources/figures/` 文件夹中为您服务。

---

## 4. 资源库 (Resources)

本仓库提供了一些内置资源以帮助您快速上手：

*   📂 **`templates/`**: 包含 IEEE, ACM, APA 等主流学术会议/期刊的官方模板下载链接。
*   📂 **`examples/`**: 包含一份标准论文草稿 (`draft.md`) 和样式指南 (`style_guide.md`)，用于测试 Skill 的功能。
*   ❓ **`TROUBLESHOOTING.md`**: 常见问题排查指南（如格式错乱、引用丢失等）。

---

## 致谢 (Credits & Acknowledgments)

本项目利用了 **Anthropic** 提供的强大的文档处理能力。

*   **Docx & PDF Skills**: 特别感谢 [Anthropic Skills Repository](https://github.com/anthropics/skills) 提供了与 Microsoft Word 和 PDF 文档交互的基础逻辑。这些模块赋予了本 Skill 精准的读取、编辑和排版能力。
