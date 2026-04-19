# 论文排版与整理完全工作流 (Iterative OCR & Typesetting Pipeline)

<!--
本文件是 Pipeline A (OCR管道) 的子模块规范，通过主 SKILL.md 调用。
不要在此添加 YAML frontmatter，否则会被识别为独立 skill。
-->

## 0. 目录规范 (Directory Convention)

所有中间文件和最终产物必须严格遵守以下目录结构，**禁止在项目根目录下放置任何生成文件**：

```
项目根目录/
├── resources/
│   ├── pages/          # 切分出的单页 PNG 图片
│   ├── figures/        # 从页面中裁剪出的独立科研配图（全局编号）
│   ├── md/             # 每页的 Markdown 提取结果 (page_1.md, page_2.md, ...)
│   ├── scripts/        # 所有 Python 辅助脚本（可跨任务复用，清理时不删除）
│   ├── compiled_paper.md  # 最终汇总的完整 Markdown
│   ├── config.json     # 任务配置（源 PDF、格式规范），整个任务期间不变
│   └── checkpoint.json # 运行时进度（当前页、计数器、失败页），随处理更新
├── outputs/
│   ├── <name>_checkpoint_p<N>.docx   # 核查点中间版本
│   └── <name>_final_<date>.docx      # 最终交付版本
├── ocr_kb/
│   └── SKILL.md        # 本文件
└── <source>.pdf        # 用户提供的原始 PDF
```

---

## 0.5 `resources/config.json` 规范 (Task Configuration)

在每次新任务启动时创建，**整个任务期间不修改**。续作时直接读取。所有管道共用同一 schema。

```json
{
  "source_file": "2103.10360v2.pdf",
  "source_type": "pdf",
  "pipeline": "A",
  "format_style": "IEEE",
  "template_file": null,
  "total_units": 16,
  "unit_type": "page",
  "created_at": "2026-04-02T13:00:00+08:00"
}
```

| 字段 | 说明 |
|------|------|
| `source_file` | 用户指定的源文件名（PDF / DOC / DOCX / MD） |
| `source_type` | 文件类型：`"pdf"` / `"doc"` / `"docx"` / `"md"` |
| `pipeline` | 管道类型：`"A"`（OCR）/ `"B"`（重排版）/ `"C"`（MD 直转） |
| `format_style` | 排版格式（IEEE / APA / 用户自定义 / ...） |
| `template_file` | 用户提供的 `.docx` 模板路径，无则 `null` |
| `total_units` | 总处理单元数（Pipeline A = 页数，Pipeline B/C = 章节数） |
| `unit_type` | 进度单位：`"page"`（Pipeline A）/ `"section"`（Pipeline B/C） |
| `created_at` | 任务创建时间 |

> [!NOTE]
> Pipeline A 固定使用 `source_type: "pdf"`, `pipeline: "A"`, `unit_type: "page"`。

---

## 0.6 `resources/checkpoint.json` 规范 (Runtime Checkpoint)

在每完成一个单元（页或章节）的提取 + DOCX 追加后更新。**这是断点恢复的唯一依据。**所有管道共用同一 schema。

```json
{
  "current_unit": 7,
  "unit_type": "page",
  "last_verified_unit": 6,
  "total_units": 16,
  "docx_path": "outputs/GLM_checkpoint_p6.docx",
  "global_figure_count": 4,
  "global_table_count": 2,
  "global_equation_count": 15,
  "needs_review": [3],
  "completed_units": [1, 2, 3, 4, 5, 6],
  "status": "suspended"
}
```

| 字段 | 说明 |
|------|------|
| `current_unit` | 下一个要处理的单元编号 |
| `unit_type` | 单元类型：`"page"`（Pipeline A）/ `"section"`（Pipeline B/C） |
| `last_verified_unit` | 最后一个通过核查的单元编号 |
| `total_units` | 总单元数（从 config.json 同步） |
| `docx_path` | 当前最新的 DOCX 中间版本路径 |
| `global_figure_count` | 全局配图计数器（只增不减） |
| `global_table_count` | 全局表格计数器（只增不减） |
| `global_equation_count` | 全局公式计数器（只增不减） |
| `needs_review` | 标记为"需要复查"的单元编号列表 |
| `completed_units` | 已完成提取的单元编号列表 |
| `status` | `"running"` / `"suspended"` / `"completed"` |

**更新时机**（以 Pipeline A 为例，B/C 将"页"替换为"章节"）：
- 每完成一个单元：更新 `current_unit`、`completed_units`、计数器
- 每 2 个单元核查后：更新 `last_verified_unit`
- 核查发现问题：向 `needs_review` 添加单元编号
- 每 4 个单元悬挂前：设 `status = "suspended"`，保存 DOCX 中间版本
- 全部完成后：设 `status = "completed"`

**Pipeline A 中间版本命名**：使用 `_checkpoint_p<N>` 表示页码。Pipeline B/C 使用 `_checkpoint_s<N>` 表示章节。

---

## 0.7 脚本接口契约 (Script Contracts)

> [!IMPORTANT]
> 以下脚本如果 `resources/scripts/` 中已存在，**直接复用**，不要重新生成。仅在不存在时才创建，且必须严格遵守下列接口。

### `split_pdf.py`

```
用法: python resources/scripts/split_pdf.py <pdf_path> <output_dir> [--dpi 300]
输入: PDF 文件路径，输出目录路径
输出: output_dir/page_1.png, page_2.png, ..., page_N.png
退出码: 0 成功，非 0 失败
stdout: 最后一行输出 "TOTAL_PAGES=N"
```

### `extract_figures.py`

```
用法: python resources/scripts/extract_figures.py <page_image> <page_num> <coords_json> <output_dir> <start_index>
输入:
  - page_image: 单页 PNG 路径
  - page_num: 页码（用于日志）
  - coords_json: JSON 字符串，格式 [{"x0%": 10, "y0%": 30, "x1%": 90, "y1%": 70, "caption": "Figure N: ..."}]
  - output_dir: 输出目录
  - start_index: 全局起始编号（从 checkpoint.global_figure_count + 1 开始）
输出: output_dir/figure_<start_index>.png, figure_<start_index+1>.png, ...
退出码: 0 成功，非 0 失败
stdout: 最后一行输出 "FIGURES_EXTRACTED=K"
```

### `generate_docx.py`

```
用法: python resources/scripts/generate_docx.py <compiled_md> <config_json> <output_path>
输入:
  - compiled_md: 汇总后的 Markdown 文件路径
  - config_json: 任务配置文件路径（读取 format_style 等信息）
  - output_path: 输出 DOCX 文件路径
输出: 指定路径的 .docx 文件
退出码: 0 成功，非 0 失败
```

### `latex_to_omml.py`

```
用法: python ocr_kb/scripts/latex_to_omml.py <latex_string> [--inline]
输入:
  - latex_string: LaTeX 公式字符串（不含 $ 定界符）
  - --inline: 可选标志，输出行内 <m:oMath> 而非块级 <m:oMathPara>
输出: 标准输出打印完整的 OMML XML 片段
  - 无 --inline时: <m:oMathPara>...</m:oMathPara>
  - 有 --inline时: <m:oMath>...</m:oMath>
退出码: 0 成功，非 0 失败
stderr: 转换失败时输出错误信息（不支持的 LaTeX 命令等）
支持范围: 基础运算、分式(\frac)、上下标、根号(\sqrt)、
  希腊字母、求和/积分(\sum/\int)、矩阵(\matrix/\pmatrix)、
  常用数学符号(\leq/\geq/\neq/\approx/\infty 等)
```

> [!NOTE]
> 此脚本位于 `ocr_kb/scripts/`（不在 `resources/scripts/`），因为它是 Skill 自带的工具而非任务生成的临时脚本。所有管道共用此脚本。

---

## 1. 逐页精读与追加写入 (Page-by-Page Extraction)

对于切分好的每一张单页图片（`resources/pages/page_N.png`），执行以下操作：

### 1.1 纯文本读取
一页一页地用视觉能力精读图片，将文字原汁原味提取出来。

> [!CAUTION]
> **标题格式规范**：切勿在文本中保留多余或错误的 Markdown 标题符号（如 `#### 3.2.3`）。最终生成 DOCX 时排版脚本会自动映射目标模板（如 IEEE 的罗马数字 I, II, A, B 等）。提取的 Markdown 必须使用极其干净的 `#` 层级（如 `## ` 代表一级标题，`### ` 代表二级标题），**绝对禁止**原文档的旧编号或多余的 `#` 号残留在最终正文内。

### 1.2 公式转译
页面中的独立公式或行内公式（包括表格、图注中的单个数学符号如 `$d_{model}$`），**必须**全部读成标准 LaTeX 语法（行内使用 `$ $`，独立块使用 `$$ $$`）。每个独立公式递增 `checkpoint.json` 的 `global_equation_count`。

> [!IMPORTANT]
> 此举是为了在最终生成 DOCX 时，确保 Python 脚本能通过正则表达式精准捕获这两类边界，并调用 `latex_to_omml.py` 将它们全部挂载为 Word 原生 OMML 公式（`<m:oMath>` 或 `<m:oMathPara>`）。切勿遗漏变量的包裹，否则它们只能渲染成普通文本。

### 1.3 插图识别与智能裁剪

> [!IMPORTANT]
> **禁止**直接把整页截图作为图片插入 Markdown。必须从页面中**精确识别并裁剪出独立的科研配图**。

具体流程：
1. **识别**：视觉读取当前页时，判断页面中是否存在独立的科研配图（Figure）或独立的表格图（Table 以图片形式呈现的）。
2. **定位**：确定配图在页面上的大致位置百分比坐标 `(x0%, y0%, x1%, y1%)`。
3. **全局编号**：从 `checkpoint.json` 读取 `global_figure_count`，本页新配图从 `global_figure_count + 1` 开始编号。裁剪完毕后更新 `global_figure_count`。表格同理使用 `global_table_count`。
4. **裁剪**：使用 `resources/scripts/extract_figures.py` 或 `PyMuPDF` 的 `page.get_pixmap(clip=Rect(...))` 方法，按坐标从高分辨率页面渲染中裁剪出**单独的**配图，保存到 `resources/figures/figure_N.png`（N 为全局编号）。
5. **引用**：在 Markdown 中使用裁剪后的独立图片路径：
   ```markdown
   ![Figure 4: 图注说明](resources/figures/figure_4.png)
   ```

### 1.4 写入
将当前页的提取结果写入 `resources/md/page_N.md`。

### 1.5 更新 Checkpoint
每写完一个 `page_N.md` 并追加到 DOCX 后，立即更新 `checkpoint.json`：
- `current_unit += 1`
- `completed_units` 添加当前页码
- 更新 `global_figure_count` / `global_table_count` / `global_equation_count`

---

## 2. 逐页 DOCX 生成与双页核查 (Incremental DOCX Generation)

> [!IMPORTANT]
> 不再等到所有页面提取完毕后一次性生成 DOCX。**每完成一页 MD 的提取，就立即将该页内容追加到正在构建的 DOCX 文件中**。

### 2.1 单页流程
```
读一页图片 → 写 page_N.md → 将 page_N.md 内容追加到 DOCX → 更新 checkpoint.json
```

### 2.2 双页核查（每 2 页）

每完成 2 页的 DOCX 追加后，必须执行一次**自检核查**：

1. 回顾刚追加的 2 页内容在 DOCX 中的排版效果（字体、公式、配图位置、标题层级）。
2. 对照原始页面图片，确认没有信息丢失或格式错乱。
3. **核查通过**：在 `checkpoint.json` 中更新 `last_verified_unit`。
4. **核查不通过**：
   - 在 `checkpoint.json` 的 `needs_review` 数组中记录问题页码。
   - 尝试立即修复。如果修复成功，从 `needs_review` 中移除该页码。
   - 如果无法修复，**不阻塞后续页面处理**，但在最终汇总前 `needs_review` 必须清零。

### 2.3 上下文极限保护

- 连续处理 **4 页**后，必须主动悬挂（suspend）：
  1. 将 `checkpoint.json` 的 `status` 设为 `"suspended"`。
  2. 保存当前 DOCX 中间版本到 `outputs/`（命名规则见 §2.4）。
  3. 使用 `notify_user` 通知用户发送"继续"以刷新上下文窗口。
- 恢复后读取 `checkpoint.json`，从 `current_unit` 继续。

### 2.4 中间版本命名规则

| 类型 | 命名格式 | 示例 |
|------|----------|------|
| 核查点中间版本 | `outputs/<原文件名>_checkpoint_p<最后完成页码>.docx` | `outputs/GLM_checkpoint_p6.docx` |
| 最终交付版本 | `outputs/<原文件名>_final_<YYYYMMDD>.docx` | `outputs/GLM_final_20260402.docx` |

> [!NOTE]
> 每次保存新的核查点版本时，**保留上一个版本**不要删除，以便出问题时可以回退。

---

## 3. 最终排版定稿 (Final Typesetting)

### 3.1 needs_review 清零检查

在进入定稿之前，检查 `checkpoint.json` 的 `needs_review`：
- **不为空**：列出所有待复查页码，逐页重新核查并修复。全部修复后才可继续。
- **为空**：直接进入汇总。

### 3.2 汇总
将 `resources/md/page_1.md` ~ `page_N.md` 按顺序合并为 `resources/compiled_paper.md`。

### 3.3 生成最终 DOCX
使用 `resources/scripts/generate_docx.py`，按 `config.json` 中指定的格式规范生成最终排版文件，保存到 `outputs/`。

### 3.4 排版格式应用

排版参数从 `config.json` 的 `format_params` 读取（由主 SKILL.md §2.2 在启动时解析并写入）。

具体格式预设（IEEE / APA / 中国学位论文等）的完整参数表定义在**主 SKILL.md §6 排版格式规范库**中，本文件不再重复。

**Pipeline A 的 DOCX 生成方式**：使用 `docx/SKILL.md` 中的 docx-js 创建新文档，或使用 unpack-edit-pack 方式基于模板编辑。

关于 图片、表格、页眉页脚、分栏、公式 的排版细则，参见**主 SKILL.md §5 通用排版细则**。

### 3.5 更新 Checkpoint
设 `checkpoint.json` 的 `status = "completed"`，记录最终文件路径。

---

## 4. 执行口令指引 (Execution Triggers)

### 4.1 全新任务

用户发送 "按照某某格式排版这个 PDF" 时（主 SKILL.md 路由到 Pipeline A）：

1. **清理确认**：按主 SKILL.md §1.1 执行环境清理确认。
2. **选定源文件**：按主 SKILL.md §1.2 确认源 PDF 并选择 Pipeline A。
3. **创建配置**：写 `resources/config.json`（`pipeline: "A"`, `unit_type: "page"`）。
4. **切图**：运行 `resources/scripts/split_pdf.py`。
5. **建立进度**：创建 `resources/checkpoint.json`（`current_unit = 1`, `unit_type: "page"`，所有计数器归零）。
6. **逐页循环**：按 §1 和 §2 执行。
7. **汇总定稿**：按 §3 执行。
8. **输出报告**：按主 SKILL.md §5 输出完成报告。

### 4.2 断点续作

用户发送 "继续" 时：

1. 读取 `resources/checkpoint.json`。
2. 从 `current_unit` 指定的页码继续逐页循环。
3. 所有全局计数器从 checkpoint 恢复，不重置。

### 4.3 部分重跑

用户发送 "重跑第 N 页" 或 "rerun page N" 时：

1. 读取 `resources/checkpoint.json`，确认第 N 页在 `completed_units` 中。
2. 重新读取 `resources/pages/page_N.png`，重新执行 §1 的提取流程。
3. 覆盖写入 `resources/md/page_N.md`。
4. **注意**：如果该页有配图，需要更新对应的 `figure_*.png`，但**不改变全局编号**——复用原编号。
5. 从 `needs_review` 中移除 N（如果存在）。
6. 重新生成最终 DOCX（重新执行 §3.2 ~ §3.3）。

### 4.4 批量重跑

用户发送 "重跑第 X-Y 页" 时：

按 §4.3 对范围内每一页逐一执行重跑。

---

## 5. 完成后结构化总结 (Completion Report)

> [!IMPORTANT]
> 全部页面处理完毕并生成最终 DOCX 后，**必须**输出以下总结，不可省略。

```
【完成报告】
源文件：<config.source_file>
输入类型：<config.source_type>
处理管道：Pipeline <config.pipeline>
格式规范：<config.format_style>
总单元数：<checkpoint.total_units>（<config.unit_type>）
提取公式数：<checkpoint.global_equation_count>
裁剪配图数：<checkpoint.global_figure_count>
提取表格数：<checkpoint.global_table_count>
核查点版本数：<outputs/ 中 checkpoint 文件的数量>
最终文件：outputs/<最终文件名>.docx
遗留问题：<needs_review 中的单元编号 / 无>
```

---
