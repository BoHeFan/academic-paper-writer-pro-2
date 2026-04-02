---
name: academic-paper-writer-pro
description: 基于规范目录结构的学术论文排版助手。支持 PDF / .doc / .docx / .md 多种输入格式，自动选择 OCR 管道、重排版管道或 MD 直转管道。包含环境清理确认、断点恢复、智能配图裁剪、逐单元增量生成 DOCX、双单元质量核查、中间状态保存和 BibTeX 参考文献管理。所有中间文件放 resources/，最终产物放 outputs/。
---

# 学术论文专家（主路由）

> [!IMPORTANT]
> 本文件是**主路由入口 + Pipeline B/C 定义 + 排版格式规范库**。Pipeline A（OCR 管道）的详细规范请参见 `ocr_kb/SKILL.md`。
> 所有管道的 DOCX 生成均使用 `docx/SKILL.md` 中定义的方法（docx-js 创建新文档 / unpack-edit-pack 编辑现有文档）。

## 0. 目录规范 (Directory Convention)

> [!IMPORTANT]
> 所有中间文件和生成产物必须严格遵守以下目录结构，**禁止在项目根目录下放置任何生成文件**（包括 `.md`、`.py`、`.docx` 等）。

```
项目根目录/
├── resources/
│   ├── pages/          # Pipeline A: 切分出的单页 PNG 图片
│   ├── figures/        # 所有管道: 配图（裁剪的或提取的）
│   ├── md/             # 所有管道: 提取/拆分结果
│   │   ├── page_N.md       # Pipeline A 按页
│   │   └── section_N.md    # Pipeline B/C 按章节
│   ├── scripts/        # 所有 Python 辅助脚本（可跨任务复用，清理时不删除）
│   ├── compiled_paper.md  # 最终汇总的完整 Markdown
│   ├── config.json     # 任务配置（源文件、格式、管道类型），整个任务期间不变
│   └── checkpoint.json # 运行时进度（当前单元、计数器、失败项），随处理进度更新
├── outputs/            # 最终交付的 .docx / .bib 文件 + 核查点中间版本
├── ocr_kb/             # Pipeline A: OCR 工作流 Skill
│   └── SKILL.md
├── docx/               # Word 文档操作 Skill（DOCX 生成的技术实现基础）
│   └── SKILL.md
├── pdf/                # PDF 操作 Skill
│   └── SKILL.md
├── SKILL.md            # 本文件（主入口路由 + Pipeline B/C + 排版规范库）
└── <source>.*          # 用户提供的原始文件 (.pdf / .doc / .docx / .md)
```

---

## 1. 新任务启动协议 (Step 0: Pre-flight)

> [!CAUTION]
> 以下三项检查必须在执行**任何**写作或排版动作之前**全部完成**，不可跳过。

### 1.1 环境清理确认

检测 `resources/` 下的 `pages/`、`md/`、`figures/` 以及 `resources/checkpoint.json` 是否存在旧文件。

- **若存在旧文件**：列出文件清单，明确询问用户：
  > "检测到上次任务的中间文件（N 个页面/章节、M 个 Markdown、K 张配图）。是否删除以避免干扰？回复 **删除** 清空，或 **保留** 继续上次任务。"
- **若不存在旧文件**：跳过此步。
- **用户选择"删除"时**：删除 `resources/pages/*`、`resources/md/*`、`resources/figures/*`、`resources/checkpoint.json`、`resources/config.json`。`resources/scripts/` **不删除**（脚本可复用）。
- **用户选择"保留"时**：读取 `resources/checkpoint.json`，进入断点恢复流程（见 §1.3）。

### 1.2 源文件确认与管道选择

扫描项目根目录下的所有支持格式文件（`.pdf`、`.doc`、`.docx`、`.md`）：

- **只有 1 个**：自动选定，根据扩展名决定管道。
- **有多个**：列出所有文件名、类型及大小，要求用户明确指定目标文件。
- **没有**：报错，要求用户放入源文件。

**管道自动选择规则**：

| 扩展名 | 管道 | 进度单位 | 核心 Skill |
|--------|------|----------|-----------|
| `.pdf` | **Pipeline A — OCR 管道** | 页 (page) | `ocr_kb/SKILL.md` |
| `.doc` / `.docx` | **Pipeline B — 重排版管道** | 章节 (section) | `docx/SKILL.md` + 本文件 §3.2 |
| `.md` | **Pipeline C — MD 直转管道** | 章节 (section) | `docx/SKILL.md` + 本文件 §3.3 |

### 1.3 断点恢复检测

检查 `resources/checkpoint.json` 是否存在且合法：

- **存在且 `status == "suspended"`**：
  向用户展示上次进度（已完成单元数 / 总单元数，管道类型），询问：
  > "检测到上次任务（Pipeline X，已完成 N/M 个单元）。是否从断点继续？回复 **继续** 从第 N+1 个单元开始，或 **重新开始** 清空所有中间文件。"
- **不存在或 `status == "completed"`**：正常启动新任务。

---

## 2. 文件完整性检查与资源准备

### 2.1 文件完整性检查

要求用户把需要排版的文稿和格式要求放入本目录下：
- **草稿 (Draft)**：用户的内容文件（`.pdf`、`.doc`、`.docx` 或 `.md`）。
- **格式要求 (Style Guide/Template)**：`.docx` 模板或 `.pdf` 指南（如 IEEE 模板）。
- **参考文献 (References)**：询问用户是否有 `.bib` 文件。如果有，**必须优先使用**。

### 2.2 格式规范解析（所有管道必执行）

> [!IMPORTANT]
> 在拆分内容或提取文字之前，**必须先完成格式规范解析**，确定所有排版参数。

1. **如果用户提供了 `.docx` 模板**（`config.template_file` 非空）：
   - 使用 `docx/SKILL.md` 的 unpack 方法打开模板
   - 提取样式定义（标题层级、正文字体/字号、行距、页边距、页眉页脚、分栏设置）
   - 将提取到的参数记录到 `config.json` 的 `format_params` 字段

2. **如果用户指定了格式名称**（如"IEEE"、"APA"）：
   - 从本文件 **§6 排版格式规范库** 中读取对应的预设参数
   - 将参数记录到 `config.json` 的 `format_params` 字段

3. **如果两者都有**：模板优先，预设参数作为兜底。

### 2.3 资源目录准备

确保 `resources/`（含子目录 `pages/`、`md/`、`figures/`、`scripts/`）和 `outputs/` 存在，不存在则自动创建。

### 2.4 任务配置持久化

创建或读取 `resources/config.json`（详细格式见 `ocr_kb/SKILL.md` §0.5），记录源文件路径、文件类型、管道类型、格式规范和排版参数，使后续续作无需重复指定。

---

## 3. 核心处理流程（按管道分发）

### 3.1 Pipeline A — OCR 管道（PDF 输入）

> [!IMPORTANT]
> Pipeline A 的**全部详细规范**定义在 `ocr_kb/SKILL.md` 中。本节仅做高层描述。

1. **切图**：运行 `resources/scripts/split_pdf.py` 将 PDF 分割为单页 PNG。
2. **逐页循环**：按 `ocr_kb/SKILL.md` 的规范逐页提取 + 逐页追加 DOCX。
3. **核查与悬挂**：每 2 页核查，每 4 页悬挂。
4. **汇总定稿**：合并所有 `page_N.md` → `compiled_paper.md` → 最终 DOCX。

**DOCX 生成方式**：使用 `docx/SKILL.md` 中的 docx-js 创建新文档，按 §6 格式规范库中的参数配置样式。

---

### 3.2 Pipeline B — 重排版管道（.doc / .docx 输入）

适用场景：用户已有 Word 文档，需要按新的格式规范（如 IEEE）重新排版。

#### 第一步：格式转换（仅 .doc）
如果输入是 `.doc`（旧格式），先转换为 `.docx`：
```bash
python scripts/office/soffice.py --headless --convert-to docx <input.doc>
```
参考 `docx/SKILL.md` 的"Converting .doc to .docx"章节。

#### 第二步：格式规范解析
按 §2.2 解析目标格式规范，确定所有排版参数。

#### 第三步：内容提取与章节拆分
1. 使用 pandoc 或 `docx/SKILL.md` 的 unpack 方法读取 `.docx` 内容。
2. 按**一级标题**（或用户指定的拆分层级）将文档拆分为多个章节。
3. 每个章节写入 `resources/md/section_N.md`，保留：
   - 原始文本内容
   - 公式（如有 OMML 原生公式，转为 LaTeX 保存在 MD 中）
   - 表格结构（转为 Markdown 表格）
   - 图片引用（提取图片到 `resources/figures/`，在 MD 中使用相对路径引用）
4. 创建 `resources/config.json`（`pipeline: "B"`, `unit_type: "section"`）。
5. 创建 `resources/checkpoint.json`（`current_unit: 1`，计数器归零）。

#### 第四步：逐章节重排版
使用 `docx/SKILL.md` 中的 docx-js 创建新 DOCX 文档，按 §6 的格式参数配置样式（字体、页边距、页眉页脚等），然后逐章节填充内容：

1. 读取 `section_N.md`。
2. **文本排版**：按 §6 格式参数应用标题样式、正文字体字号、段间距、对齐方式。
3. **公式处理**：MD 中的 LaTeX → `latex_to_omml.py` → 原生 OMML 插入 DOCX（参考 `docx/SKILL.md` §447-468 Formulas (OMML) 章节）。
4. **图片嵌入**：从 `resources/figures/` 读取，按 §5.2 图片排版参数嵌入 DOCX。
5. **表格转换**：Markdown 表格 → Word 表格 XML，按 §5.3 表格排版参数和 `docx/SKILL.md` Tables 章节生成。
6. 追加到输出 DOCX。
7. 更新 `checkpoint.json`（`current_unit += 1`、更新计数器）。

#### 第五步：核查与上下文保护
- **每 2 个章节**：核查排版质量，对照原文确认无信息丢失。
- **每 4 个章节**：保存中间版本到 `outputs/<name>_checkpoint_s<N>.docx`，悬挂等待用户刷新上下文。
- 核查不通过 → 记录到 `checkpoint.json` 的 `needs_review`。

#### 第六步：汇总定稿
1. 合并所有 `section_N.md` → `resources/compiled_paper.md`。
2. 最终 DOCX 已在逐章节追加过程中构建完毕，保存为 `outputs/<name>_final_<date>.docx`。

---

### 3.3 Pipeline C — MD 直转管道（.md 输入）

适用场景：用户已有 Markdown 格式的论文，需要转为带格式的 Word 文档。

#### 第一步：格式规范解析
按 §2.2 解析目标格式规范，确定所有排版参数。

#### 第二步：章节拆分
1. 读取 `.md` 文件，按**一级标题**（`# ...`）拆分为多个章节。
2. 每个章节保存为 `resources/md/section_N.md`。
3. 统计总章节数。
4. 创建 `resources/config.json`（`pipeline: "C"`, `unit_type: "section"`）。
5. 创建 `resources/checkpoint.json`（`current_unit: 1`，计数器归零）。

#### 第三步：逐章节转换与排版
使用 `docx/SKILL.md` 中的 docx-js 创建新 DOCX 文档，按 §6 的格式参数配置样式，然后逐章节转换内容：

1. **公式转换**：
   - 行内公式 `$...$` → 原生 OMML（通过 `ocr_kb/scripts/latex_to_omml.py`，接口见 `ocr_kb/SKILL.md` §0.7）
   - 独立公式 `$$...$$` → OMML 公式段落，编号靠右对齐
   - 更新 `checkpoint.json` 的 `global_equation_count`
2. **表格转换**：
   - Markdown 表格 → Word 表格 XML（按 §5.3 表格排版参数 + `docx/SKILL.md` Tables 章节）
   - 更新 `global_table_count`
3. **图片嵌入**：
   - `![caption](path)` → 检查图片文件是否存在
   - 将图片复制到 `resources/figures/`（如不在其中），全局编号
   - 按 §5.2 图片排版参数嵌入 DOCX
   - 更新 `global_figure_count`
4. **文本排版**：
   - 标题层级映射（`#` → Heading 1，`##` → Heading 2，...）
   - 按 §6 格式参数应用字体、字号、段间距、对齐方式
5. 追加到输出 DOCX。
6. 更新 `checkpoint.json`。

#### 第四步：核查与上下文保护
- 与 Pipeline B 完全相同（每 2 章节核查，每 4 章节悬挂）。

#### 第五步：汇总定稿
1. 所有 `section_N.md` 已在拆分时创建，合并为 `resources/compiled_paper.md`。
2. 最终 DOCX 保存为 `outputs/<name>_final_<date>.docx`。

---

### 3.4 所有管道的通用规则

以下规则不分管道，**强制执行**：

| 规则 | 说明 |
|------|------|
| **逐单元处理** | 不论是页还是章节，每完成一个单元就追加到 DOCX 并更新 checkpoint |
| **每 2 单元核查** | 对照源文件确认无信息丢失或格式错乱 |
| **每 4 单元悬挂** | 保存中间版本，通知用户发送"继续"刷新上下文 |
| **needs_review 清零门禁** | 最终汇总前，`needs_review` 必须为空 |
| **中间版本保留** | 核查点版本不删除，以便回退 |
| **全局编号** | figure / table / equation 三个计数器全局递增，跨单元不重置 |

---

## 4. 参考文献管理

- **优先**：解析用户提供的 `.bib` 文件。
- **补充**：如果用户未提供 `.bib`，**不要自行编造或搜索文献**。标记所有缺失的引用（列出引用标记名），通知用户手动补充。
- **输出**：在 `outputs/references.bib` 中生成参考文献文件。

---

## 5. 通用排版细则 (Cross-Pipeline Formatting Details)

> [!IMPORTANT]
> 以下细则适用于所有管道，具体参数受 §6 格式规范库中的预设值或用户模板覆盖。DOCX 的技术实现统一参考 `docx/SKILL.md`。

### 5.1 模板文件使用流程

当 `config.template_file` 非空时：

1. **方式一（推荐）**：使用 `docx/SKILL.md` 的 unpack 方法打开模板，提取 `word/styles.xml` 中的样式定义，然后用 docx-js 创建新文档时复制这些样式。
2. **方式二**：直接复制模板文件为输出文件，然后用 unpack → edit XML → pack 的方式替换内容，保留模板的全部样式和页面设置。

当 `config.template_file` 为空时：
- 使用 docx-js 创建全新文档，按 §6 格式规范库的预设参数手动配置样式。

### 5.2 图片排版参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 宽度策略 | 等比缩放至栏宽的 80% | 单栏论文 = 页面内容宽度×80%；双栏论文 = 栏宽×95% |
| 位置 | 行内嵌入，居中对齐 | 不使用浮动定位 |
| 图注格式 | "Figure N: 说明文字" | 图下方，居中，比正文小 1pt，加粗 "Figure N" 部分 |
| 图注与正文间距 | 上方 6pt，下方 12pt | |
| 图片质量 | 原始分辨率，不压缩 | |

**docx-js 实现参考**：`docx/SKILL.md` Images 章节（§220-232），注意 `type` 参数必填，`altText` 三个子字段都必填。

### 5.3 表格排版参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 宽度 | 满栏宽（DXA 单位） | 单栏 = 页面内容宽度；双栏 = 栏宽 |
| 边框 | 细线 `#CCCCCC`，1pt | |
| 表头 | 加粗，浅蓝底色 `#D5E8F0` | 使用 `ShadingType.CLEAR`（不用 SOLID） |
| 单元格内边距 | 上下 80 DXA，左右 120 DXA | |
| 表注格式 | "Table N: 说明文字" | 表上方，居中，比正文小 1pt |

**docx-js 实现参考**：`docx/SKILL.md` Tables 章节（§173-219），必须同时设置 `columnWidths` 和每个 cell 的 `width`，且必须使用 `WidthType.DXA`。

### 5.4 页眉页脚与页码

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 页码 | 底部居中，阿拉伯数字 | |
| 页眉 | 空（除非格式规范要求） | IEEE 无页眉，学位论文通常有 |
| 首页特殊 | 首页无页眉页码（如格式要求） | |

**docx-js 实现参考**：`docx/SKILL.md` Headers/Footers 章节（§251-268），使用 `PageNumber.CURRENT`。

### 5.5 分栏排版

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 栏数 | 由格式规范决定（IEEE = 2栏，APA = 1栏） | |
| 栏间距 | 360 DXA（0.25 inch） | |
| 标题/摘要 | 通常跨栏（section break 分隔） | |

**docx-js 实现**：通过 `sections` 属性设置不同的 section 拥有不同的栏数：
```javascript
// 标题区域 - 单栏
{ properties: { column: { count: 1 } }, children: [/* 标题、作者、摘要 */] },
// 正文区域 - 双栏
{ properties: { column: { count: 2, space: 360 } }, children: [/* 正文 */] }
```

### 5.6 公式排版

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 行内公式 | OMML `<m:oMath>`，与正文同行 | |
| 独立公式 | OMML `<m:oMathPara>`，居中 | |
| 公式编号 | 靠右对齐，格式 `(N)` | |
| LaTeX → OMML | 通过 `ocr_kb/scripts/latex_to_omml.py` | |

**docx-js / XML 实现参考**：`docx/SKILL.md` Formulas (OMML) 章节（§447-469）。

---

## 6. 排版格式规范库 (Format Style Library)

> [!IMPORTANT]
> 格式预设以独立 `.md` 文件存放在 `templates/` 目录下，每个文件包含完整的排版参数表。当用户指定格式名称时，读取对应文件。如果用户提供了 `.docx` 模板，模板中的设置**覆盖**预设。

### 6.1 内置格式预设

| 格式名称 | 文件 | 适用场景 |
|----------|------|----------|
| IEEE | `templates/ieee.md` | IEEE 会议论文、期刊论文 |
| APA 第7版 | `templates/apa7.md` | 心理学、社会科学论文 |
| 中国学位论文 | `templates/chinese_thesis.md` | 国内高校本硕博学位论文 |

**查找规则**：
1. 用户说 "按 IEEE 排版" → 读取 `templates/ieee.md`
2. 用户说 "按 APA 排版" → 读取 `templates/apa7.md`
3. 用户说 "按学位论文排版" / "按毕业论文排版" → 读取 `templates/chinese_thesis.md`
4. 无法匹配 → 进入 §6.2 用户自定义流程

### 6.2 用户自定义格式

当用户指定的格式不在内置预设中时：
1. 要求用户提供 `.docx` 模板或明确描述格式要求。
2. 从模板或描述中提取参数，填充 `config.json` 的 `format_params`。
3. 如果用户描述不完整，对缺失参数读取 `templates/ieee.md` 作为兜底默认值。

### 6.3 扩展新格式

如需添加新的格式预设（如 ACM、Springer LNCS 等），只需在 `templates/` 目录下新建对应的 `.md` 文件，按现有模板的表格结构填写参数即可。

---

## 7. 完成后总结输出

排版完成后，**必须**输出以下结构化完成报告：

```
【完成报告】
源文件：<config.source_file>
输入类型：<config.source_type>
处理管道：Pipeline <config.pipeline>
格式规范：<config.format_style>
总单元数：<checkpoint.total_units>（<config.unit_type>）
提取公式数：<checkpoint.global_equation_count>
裁剪/嵌入配图数：<checkpoint.global_figure_count>
提取/转换表格数：<checkpoint.global_table_count>
核查点版本数：<outputs/ 中 checkpoint 文件的数量>
最终文件：outputs/<最终文件名>.docx
遗留问题：<needs_review 中的单元编号 / 无>
```

随后主动向用户确认以下可选增值服务：
- **语言润色**：是否需要提升学术表达的专业度。
- **多模态图例**：是否需要自动生成专业图例 (Caption)。
- **逻辑校验**：检查段落间的论证逻辑。

---
