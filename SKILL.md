---
name: academic-paper-writer-pro
description: 基于规范目录结构的学术论文排版助手。支持 PDF 到 Word 的全自动化流程，包含智能配图裁剪、逐页增量生成 DOCX、双页质量核查、中间状态保存和 BibTeX 参考文献管理。所有中间文件放 resources/，最终产物放 outputs/。
---

# 学术论文专家

## 0. 目录规范 (Directory Convention)

> [!IMPORTANT]
> 所有中间文件和生成产物必须严格遵守以下目录结构，**禁止在项目根目录下放置任何生成文件**（包括 `.md`、`.py`、`.docx` 等）。

```
项目根目录/
├── resources/
│   ├── pages/          # 切分出的单页 PNG 图片
│   ├── figures/        # 从页面中裁剪出的独立科研配图
│   ├── md/             # 每页的 Markdown 提取结果 (page_1.md, page_2.md, ...)
│   ├── scripts/        # 所有 Python 辅助脚本 (split_pdf.py, extract_figures.py, generate_docx.py, ...)
│   └── compiled_paper.md  # 最终汇总的完整 Markdown
├── outputs/            # 最终交付的 .docx / .bib 文件
├── ocr_kb/             # OCR 与排版工作流 Skill
│   └── SKILL.md
├── docx/               # Word 文档操作 Skill
│   └── SKILL.md
├── pdf/                # PDF 操作 Skill
│   └── SKILL.md
├── SKILL.md            # 本文件（主入口路由）
└── <source>.pdf        # 用户提供的原始 PDF
```

## 1. 环境初始化与安装
*   **依赖检查**：确保 `pandoc`、`python-docx`、`PyMuPDF (fitz)` 可用。
*   **目录检查**：确保 `resources/`（含子目录）和 `outputs/` 存在，不存在则自动创建。

## 2. 强制性前置检查 (Pre-check Workflow)
在执行任何写作任务前，必须进行以下检查：

1.  **文件完整性检查**：
    *   要求用户把需要排版的文稿和格式要求放入本目录下。
    *   **草稿 (Draft)**：用户的内容文件（`.pdf` 或文本）。
    *   **格式要求 (Style Guide/Template)**：`.docx` 模板或 `.pdf` 指南（如 IEEE 模板）。
    *   **参考文献 (References)**：询问用户是否有 `.bib` 文件。如果有，**必须优先使用**。

2.  **智能路由**：
    *   根据用户上传的格式要求文件类型，读取 `docx/SKILL.md` 或 `pdf/SKILL.md` 获取底层指令。
    *   如果用户要求从 PDF 或图片进行 OCR 提取、公式转换与层级重排，先读取 `ocr_kb/SKILL.md` 调用多模态工作流生成结构化 Markdown 知识库；随后**必须交接回** `docx/SKILL.md` 将 Markdown 转化为最终的 Word 排版文件。

3.  **资源目录准备**：
    *   所有中间文件（MD、脚本、图片）保存在 `resources/` 及其子目录下。
    *   最终输出保存在 `outputs/`。

## 3. 核心处理流程 (Core Pipeline)

### 第一步：深度读取与策略规划 (Analysis & Planning)
*   解析格式规范（字体、边距、引用风格）。
*   解析草稿内容结构（章节、图表占位符）。
*   **长文档分块策略**：按 `ocr_kb/SKILL.md` 规定，逐页提取并逐页生成 DOCX。

### 第二步：逐页提取与增量排版 (Incremental Extraction & Typesetting)

> [!IMPORTANT]
> 不再一次性提取所有页面后生成完整文档。采用**逐页提取 + 逐页生成**的增量模式。

*   每页流程：`读图 → 提取文本/公式/裁剪配图 → 写 resources/md/page_N.md → 追加到 DOCX`
*   **双页核查**：每完成 2 页，对照原图核查排版质量，确认无信息丢失后才继续。
*   **上下文保护**：每 4 页悬挂一次，让用户发送"继续"以刷新上下文窗口。
*   **中间状态保存**：每个核查点保存中间版本到 `outputs/` 以防长任务失败。

### 第三步：参考文献管理 (Reference Management)
*   **优先**：解析用户提供的 `.bib` 文件。
*   **补充**：如果用户未提供 `.bib`，使用 Web Search 搜索缺失的文献。
*   **输出**：在 `outputs/references.bib` 中生成参考文献文件。

### 第四步：最终合成 (Final Assembly)
*   合并所有 `resources/md/page_N.md` 为 `resources/compiled_paper.md`。
*   运行 `resources/scripts/generate_docx.py`，输出到 `outputs/`。
*   最终输出命名：`outputs/[原文件名]_formatted_[日期].docx`。

## 4. 交互式增强 (Post-processing)
排版完成后，主动向用户确认以下增值服务：
*   **语言润色**：询问是否需要提升学术表达的专业度。
*   **多模态图例**：识别草稿中的图片/表格，自动生成专业图例 (Caption)。
*   **逻辑校验**：检查段落间的论证逻辑。

---
