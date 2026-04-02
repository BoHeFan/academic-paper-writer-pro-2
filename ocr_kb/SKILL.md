---
name: ocr_kb
description: 使用多模态大模型逐页读取长文档图片，精确提取文本、LaTeX公式和独立科研配图。逐页生成DOCX并每两页核查质量。中间产物全部放在 resources/，最终交付物放在 outputs/。
license: Proprietary. LICENSE.txt has complete terms
---

# 论文排版与整理完全工作流 (Iterative OCR & Typesetting Pipeline)

## 0. 目录规范 (Directory Convention)

所有中间文件和最终产物必须严格遵守以下目录结构，**禁止在项目根目录下放置任何生成文件**：

```
项目根目录/
├── resources/
│   ├── pages/          # 切分出的单页 PNG 图片
│   ├── figures/        # 从页面中裁剪出的独立科研配图
│   ├── md/             # 每页的 Markdown 提取结果 (page_1.md, page_2.md, ...)
│   ├── scripts/        # 所有 Python 辅助脚本 (split_pdf.py, extract_figures.py, generate_docx.py, ...)
│   └── compiled_paper.md  # 最终汇总的完整 Markdown
├── outputs/            # 最终交付的 .docx 文件
├── ocr_kb/             # 本 SKILL 文件
│   └── SKILL.md
└── <source>.pdf        # 用户提供的原始 PDF
```

---

## 1. 逐页精读与追加写入 (Page-by-Page Extraction)

对于切分好的每一张单页图片（`resources/pages/page_N.png`），执行以下操作：

### 1.1 纯文本读取
一页一页地用视觉能力精读图片，将文字原汁原味提取出来。

### 1.2 公式转译
页面中的独立公式或行内公式，必须直接读成标准 LaTeX 语法（`$ $` 或 `$$ $$`）。

### 1.3 插图识别与智能裁剪（关键改进）

> [!IMPORTANT]
> **禁止**直接把整页截图作为图片插入 Markdown。必须从页面中**精确识别并裁剪出独立的科研配图**。

具体流程：
1. **识别**：视觉读取当前页时，判断页面中是否存在独立的科研配图（Figure）或独立的表格图（Table 以图片形式呈现的）。
2. **定位**：确定配图在页面上的大致位置百分比坐标 `(x0%, y0%, x1%, y1%)`。
3. **裁剪**：使用 `PyMuPDF` 的 `page.get_pixmap(clip=Rect(...))` 方法，按坐标从高分辨率页面渲染中裁剪出**单独的**配图，保存到 `resources/figures/figure_N.png`。
4. **引用**：在 Markdown 中使用裁剪后的独立图片路径，而非整页截图：
   ```markdown
   ![Figure 1: 图注说明](resources/figures/figure_1.png)
   ```

### 1.4 写入
将当前页的提取结果写入 `resources/md/page_N.md`。

---

## 2. 逐页 DOCX 生成与双页核查 (Incremental DOCX Generation)

> [!IMPORTANT]
> 不再等到所有页面提取完毕后一次性生成 DOCX。**每完成一页 MD 的提取，就立即将该页内容追加到正在构建的 DOCX 文件中**。

### 2.1 单页流程
```
读一页图片 → 写 page_N.md → 将 page_N.md 内容追加到 DOCX → 标记 task.md 为 [x]
```

### 2.2 双页核查（每 2 页）
每完成 2 页的 DOCX 追加后，必须执行一次**自检核查**：
1. 回顾刚追加的 2 页内容在 DOCX 中的排版效果（字体、公式、配图位置、标题层级）。
2. 对照原始页面图片，确认没有信息丢失或格式错乱。
3. 如果发现问题，立即修复后再继续下一批次。
4. 在 `task.md` 中标注核查通过：`[x] Verified pages N-(N+1)`。

### 2.3 上下文极限保护
- 在 `task.md` 中记录当前进度（已完成第几页）。
- 连续处理 **4 页**后，必须主动悬挂（suspend），使用 `notify_user` 通知用户发送"继续"以刷新上下文窗口。
- 恢复后读取 `task.md`，从断点继续。

---

## 3. 最终排版定稿 (Final Typesetting)

### 3.1 汇总
当所有页面处理并核查完毕后，将 `resources/md/page_1.md` ~ `page_N.md` 合并为 `resources/compiled_paper.md`。

### 3.2 生成最终 DOCX
使用 `resources/scripts/generate_docx.py`，按用户指定的格式规范（如 IEEE）生成最终排版文件，保存到 `outputs/` 目录下。

### 3.3 IEEE 格式要点（如用户指定 IEEE）
- 双栏排版（标题/摘要除外）
- 标题：24pt 居中加粗
- 一级标题：罗马数字 + 全大写（如 `I. INTRODUCTION`）
- 二级标题：字母 + 斜体（如 `A. Background`）
- 正文：Times New Roman 10pt，两端对齐
- 摘要：斜体 9pt
- 公式：通过 Pandoc 转为原生 OMML，编号靠右对齐
- 参考文献：8pt，悬挂缩进

---

## 4. 执行口令指引 (Execution Trigger)

用户发送："按照某某格式排版这个 PDF"时，严格按以下顺序执行：

1. **切图**：运行 `resources/scripts/split_pdf.py`，将 PDF 分割为单页 PNG（`resources/pages/`）。
2. **建立进度**：在 `task.md` 中列出所有页面 `[ ] Page 1` ... `[ ] Page N`。
3. **逐页循环**：
   - `view_file` 看图 → 提取文本/公式/配图 → 写入 `resources/md/page_N.md` → 追加到 DOCX
   - 每 2 页执行一次核查
   - 每 4 页悬挂让用户刷新上下文
4. **汇总**：合并所有 `page_N.md` 为 `resources/compiled_paper.md`。
5. **定稿**：运行 `resources/scripts/generate_docx.py`，输出到 `outputs/`。
