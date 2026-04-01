---
name: academic-paper-writer-pro
description: 基于规范目录结构的排版助手。具备强制性的目录检查机制，支持中间状态保存、分块处理长文档及 BibTeX 参考文献管理。
---

# 学术论文专家 

## 0. 环境初始化与安装
*   **安装检查**：首先询问用户是否已经安装了 `opencode` 或 `claude-code`。
*   **依赖检查**：确保 `pandoc` 或相关文档转换工具可用（可选）。

## 1. 强制性前置检查 (Pre-check Workflow)
在执行任何写作任务前，AI 必须进行以下检查：

1.  **文件完整性检查**：
    *   要求用户把需要排版的文稿和格式要求放入本目录下。
    *   **草稿 (Draft)**：用户的内容文件。
    *   **格式要求 (Style Guide/Template)**：`.docx` 模板或 `.pdf` 指南。
    *   **参考文献 (References)**：询问用户是否有 `.bib` 文件。如果有，**必须优先使用**该文件中的引用。
    *   *如果没有文件*：引导用户查看 `academic-paper-writer/templates/` 获取官方模板，或使用 `academic-paper-writer/examples/` 中的示例进行测试。

2.  **智能路由**：
    *   根据用户上传的格式要求文件类型，读取 `academic-paper-writer/docx/SKILL.md` 或 `academic-paper-writer/pdf/SKILL.md` 获取底层指令。
    *   如果用户要求从 PDF 或图片进行 OCR 提取、公式转换与层级重排，先读取 `academic-paper-writer/ocr_kb/SKILL.md` 调用多模态工作流生成结构化 Markdown 知识库；随后**必须交接回** `academic-paper-writer/docx/SKILL.md` 将 Markdown 转化为最终的 Word 排版文件。

3.  **资源目录准备**：
    *   所有中间文件、图片必须保存在 `academic-paper-writer/resources/`。
    *   最终输出保存在 `academic-paper-writer/outputs/`。

## 2. 核心处理流程 (Core Pipeline)

### 第一步：深度读取与策略规划 (Analysis & Planning)
*   解析格式规范（字体、边距、引用风格）。
*   解析草稿内容结构（章节、图表占位符）。
*   **长文档分块策略 (Chunking Strategy)**：
    *   如果草稿超过 3000 字或包含 5+ 个章节，**必须**按章节拆分处理。
    *   创建任务清单：`[ ] Section 1`, `[ ] Section 2`...

### 第二步：智能排版与中间状态 (Execution & Checkpointing)
*   **执行排版**：使用 `docx` skill 工具生成文档。
*   **中间状态保存 (Checkpointing)**：
    *   每完成一个主要章节或关键步骤，**必须**保存一个中间版本。
    *   命名格式：`outputs/_step2_section1_done.docx`。
    *   *目的*：防止长任务失败导致全部重来，允许用户对中间结果进行人工干预。

### 第三步：参考文献管理 (Reference Management)
*   **优先**：解析用户提供的 `.bib` 文件，确保引用标识符（Citation Key）与文档一致。
*   **补充**：如果用户未提供 `.bib`，使用 Web Search 搜索缺失的文献。
*   **输出**：在生成最终文档的同时，**必须**生成一个 `outputs/references.bib` 文件供用户核对。

### 第四步：最终合成 (Final Assembly)
*   合并所有章节。
*   生成目录 (TOC)。
*   插入图表（确保图片在 `resources/` 中存在）。
*   最终输出命名：`outputs/[原文件名]_formatted_[日期].docx`。

## 3. 交互式增强 (Post-processing)
排版完成后，主动向用户确认以下增值服务：
*   **语言润色**：询问是否需要提升学术表达的专业度（可针对特定段落）。
*   **多模态图例**：识别草稿中的图片/表格，自动生成专业的图例 (Caption)。
*   **逻辑校验**：检查段落间的论证逻辑。
*   **故障排查**：如果用户对结果不满意，引导用户阅读 `academic-paper-writer/TROUBLESHOOTING.md`。

---
