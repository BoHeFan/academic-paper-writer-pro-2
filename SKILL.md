---
name: academic-paper-writer-pro-2
description: 学术论文写作与排版助手（增强版）。支持PDF/Word/Markdown多种格式，自动选择OCR管道、重排版管道或MD直转管道。新增Pipeline E降AI率功能，支持中文改写和英文LaTeX去AI化。包含环境清理、断点恢复、智能配图裁剪、逐单元增量生成DOCX、质量核查、BibTeX参考文献管理。所有中间文件放resources/，最终产物放outputs/。
---

# 学术论文专家 - Academic Paper Writer Pro 2

> [!TIP]
> **这是一个统一的 Skill**，安装后只需调用 `academic-paper-writer-pro-2` 即可使用所有功能。
> 
> **快速使用**：
> - 论文排版："使用 academic-paper-writer-pro-2 把这篇论文按 IEEE 格式排版"
> - 降AI率："使用 academic-paper-writer-pro-2 对这篇论文进行降AI率处理"
> - 自动写作："使用 academic-paper-writer-pro-2 基于这个项目代码写一篇毕业论文"

## 功能概览 (Feature Overview)

| Pipeline | 功能 | 触发场景 |
|----------|------|----------|
| **Pipeline A** | OCR 管道 | PDF 输入，逐页识别提取 |
| **Pipeline B** | 重排版管道 | Word 输入，按新格式排版 |
| **Pipeline C** | MD 直转管道 | Markdown 输入，转为 Word |
| **Pipeline D** | 内容生成管道 | 项目代码/数据，智能生成论文 |
| **Pipeline E** | 降AI率管道 🆕 | 降低 AI 检测率，中英文改写 |

---

> [!IMPORTANT]
> 本文件是**主路由入口 + Pipeline B/C 定义 + 排版格式规范库**。
> - Pipeline A（OCR 管道）详细规范：`ocr_kb/SKILL.md`
> - Pipeline D（内容生成）详细规范：`content_generation/SKILL.md`
> - Pipeline E（降AI率）详细规范：`ai_reduction/SKILL.md`
> - DOCX 操作技术实现：`docx/SKILL.md`
> - PDF 操作技术实现：`pdf/SKILL.md`

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
│   ├── ai_reduction/   # Pipeline E: 降AI率中间文件
│   │   ├── original/       # 原始文本备份
│   │   ├── processed/      # 处理后的文本
│   │   └── report.json     # 改写报告
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
├── content_generation/ # Pipeline D: 论文内容智能生成 Skill
│   └── SKILL.md
├── ai_reduction/       # Pipeline E: 论文降AI率 Skill
│   ├── SKILL.md
│   └── prompts/
│       ├── chinese_rewrite.md
│       └── english_latex.md
├── SKILL.md            # 本文件（主入口路由 + Pipeline B/C + 排版规范库）
└── <source>.*          # 用户提供的原始文件 (.pdf / .doc / .docx / .md / 项目代码目录)
```

---

## 1. 新任务启动协议 (Step 0: Pre-flight)

> [!CAUTION]
> 以下四项检查必须在执行**任何**写作或排版动作之前**全部完成**，不可跳过。

### 1.0 技能版本检查与自动更新 (Version Check & Auto Update)

在每次启动处理时，必须首先对比用户本地的 skill 版本和现在的最新版本：
- 运行相应的命令（如 `git fetch origin && git status -uno`）检测本地仓库状态。
- **如果本地版本与最新版本不一致**：应当主动提示并帮助用户自动更新：
  > "检测到 `academic-paper-writer-pro` 技能存在最新版本，是否需要帮您自动更新？回复 **更新** 进行升级，或 **跳过** 继续当前任务。"
- 若用户选择更新，自动执行更新命令（如 `git pull` 或 `npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro`），待更新完成后再进入下一步。

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
| 无 / 目录 | **Pipeline D — 内容生成管道** | 章节 (section) | `content_generation/SKILL.md` |

> [!NOTE]
> **Pipeline E — 降AI率管道**（`ai_reduction/SKILL.md`）可通过以下方式触发：
> - 显式指令："使用 `ai-reduction` 功能对这篇论文进行降AI率处理"
> - Pipeline D 完成后可选自动调用
> - 支持对已生成的 `.md` / `.tex` / `.docx` 文件进行降AI率处理

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

适用场景：用户已有 Word 文档，需要按新的格式规范（如 IEEE）无损排版。为了绝对保留原文原生复杂公式（OMML）、图表和批注，本管道**严禁**使用 Markdown 中转提取方案，必须采用底层 XML 外观平移（Unpack-Edit-Pack）。

#### 第一步：格式转换（仅 .doc）
如果输入是 `.doc`（旧格式），先转换为 `.docx`：
```bash
python docx/scripts/office/soffice.py --headless --convert-to docx <input.doc>
```

#### 第二步：解包 (Unpack) 与提取规范
1. 按 §2.2 解析目标格式参数。
2. 将输入 DOCX 解压到原生 XML 目录：
```bash
python docx/scripts/office/unpack.py <input.docx> resources/unpacked/
```

#### 第三步：XML 级别样式重构 (Edit XML)
此步骤不触碰主体内容逻辑。编写局部脚本直接从底层“换肤”：
1. **替换 Styles (`word/styles.xml`)**：针对格式规范（如 IEEE），将 `styles.xml` 内的全部核心样式强制替换为预设样式名称及字体。
2. **强制排定 `<w:sectPr>`**：在 `word/document.xml` 内，定位节区配置块，强制挂载双栏设定（如 `<w:cols w:num="2" w:space="360"/>`）及要求的纸张尺寸（如 US Letter: `<w:pgSz w:w="12240" w:h="15840"/>`）。
3. **重新绑定 `<w:pStyle>`**：遍历所有 `<w:p>`，通过文字特征或旧样式的权重判定其所属层级，将其挂载为 IEEE 标准的 `Heading1`、`Normal`。这确保绝不触碰封装在同层段落内的公式结构 `<m:oMath>`。

#### 第四步：原貌打包定稿 (Pack)
对重构后的外观进行无缝打包验证：
```bash
python docx/scripts/office/pack.py resources/unpacked/ outputs/<name>_final_<date>.docx --original <input.docx>
```
这彻底废弃了高风险 Markdown 中转生成法，成就 100% 内容与排版无损保留！

---

### 3.3 Pipeline C — MD 直转管道（.md 输入）

> [!CAUTION]
> **绝对禁止使用 Pandoc 进行 Markdown 到 Word 的一键直转！** 
> Pandoc 会丢失所有针对中国学位论文或顶会要求的高度定制化格式（如三线表渲染、首行缩进强绑定等）。必须且只能严格调用 **`docx/SKILL.md` 中定义的 `docx-js` (Node引擎)** 或底层的 `unpack -> edit XML -> pack` 脚本。

适用场景：用户已有 Markdown 格式的论文，需要转为带格式的 Word 文档。

#### 第一步：格式规范解析
按 §2.2 解析目标格式规范，确定所有排版参数。

#### 第二步：章节拆分
1. 读取 `.md` 文件，按**一级标题**（`# ...`）拆分为多个章节。
2. 每个章节保存为 `resources/md/section_N.md`。
3. 统计总章节数。
4. 创建 `resources/config.json`（`pipeline: "C"`, `unit_type: "section"`）。
5. 创建 `resources/checkpoint.json`（`current_unit: 1`，计数器归零）。

#### 第三步：Mermaid 架构图高清预渲染与自愈 (关键)
如果 Markdown 中包含 ````mermaid```` 代码块，在注入 Word 之前，必须执行独立的高清渲染管线：
1. **提取并保存**：将 Mermaid 代码块保存为独立的 `resources/figures/fig_N.mmd` 文件。
2. **挂载环境拦截器**：受限于 Windows 严格的进程穿透策略，必须在根目录动态生成 `puppeteer-config.json`（内容：`{"args": ["--no-sandbox", "--disable-setuid-sandbox"]}`）。
3. **调用 CLI 编译**：执行命令 `npx mmdc -i resources/figures/fig_N.mmd -o resources/figures/fig_N.png -b transparent -p puppeteer-config.json`。
4. **编译容错自愈 (Auto-healing)**：若 mmdc 抛出报错（常因 subgraph 命名含空格、状态标量含括号/单双引号等非严谨语法引起），**Agent 必须捕获报错日志，主动运用 Python 或正则修复 `.mmd` 文本内的语法残缺**，随后重试编译指令，直至高清 `.png` 成功产出。严禁在此步骤静默跳过或残留乱码！
5. **DOM 占位替换**：将 Markdown 原文中的复杂 Mermaid 块一律替换为标准图片引用语法 `![Figure N](resources/figures/fig_N.png)`，以便下一步原生嵌入。

#### 第四步：逐章节转换与排版
使用 `docx/SKILL.md` 中的 docx-js 创建新 DOCX 文档（必须通过代码映射所有样式！），按 §6 的格式参数配置样式，然后逐章节转换内容：

1. **公式转换**：
   - 行内公式 `$...$` → 原生 OMML（通过 `ocr_kb/scripts/latex_to_omml.py`，接口见 `ocr_kb/SKILL.md` §0.7）
   - 独立公式 `$$...$$` → OMML 公式段落，编号靠右对齐
   - 更新 `checkpoint.json` 的 `global_equation_count`
2. **表格转换**：
   - Markdown 表格 → Word 表格 XML（按 §5.3 表格排版参数 + `docx/SKILL.md` Tables 章节，**强制输出学术三线表**）
   - 更新 `global_table_count`
3. **图片嵌入**：
   - `![caption](path)` → 检查图片文件是否存在
   - 将图片复制到 `resources/figures/`（如不在其中），全局编号
   - 按 §5.2 图片排版参数嵌入 DOCX
   - 更新 `global_figure_count`
4. **文本排版**：
   - 标题层级映射（`#` → Heading 1，`##` → Heading 2，...）
   - 按 §6 格式参数应用字体、字号、段间距、对齐方式。**特别是段落首行缩进（2字符）的精确控制**。
5. 追加到输出 DOCX。
6. 更新 `checkpoint.json`。

#### 第五步：核查与上下文保护
- 与 Pipeline B 完全相同（每 2 章节核查，每 4 章节悬挂）。
- **增加物理拦截**：如果检测到没有按要求生成表格数据和足够的页面容量，则报废该生成的 docx。

#### 第六步：汇总定稿
1. 所有 `section_N.md` 已在拆分时创建，合并为 `resources/compiled_paper.md`。
2. 最终 DOCX 保存为 `outputs/<name>_final_<date>.docx`。


---

### 3.4 Pipeline D — 内容生成管道（项目记录/代码输入）

适用场景：用户没有完整的论文草稿，只有代码、实验数据或笔记，希望基于现有项目素材智能生成符合学术格式的论文初稿。

详情操作规范见 `content_generation/SKILL.md`，主要流程概览：
1. 分析用户提供的各种技术素材，提取并与用户确认论文整体大纲结构。
2. 以逐节自回归生成的方式构建高质量学术文本，保存至 `resources/md/section_N.md`。
3. 系统在生成完毕后，自动将其流转到 Pipeline C（MD 直转管道），复用其排版能力输出最终样式。

---

### 3.5 所有管道的通用规则

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
| ACM | `templates/acm.md` | ACM 计算机学会会议、期刊论文 |
| Springer LNCS | `templates/springer_lncs.md` | 计算机科学讲义等学术专著 |
| NeurIPS | `templates/nips.md` | NeurIPS 及机器学习相关会议 |
| MLA | `templates/mla.md` | 人文学科、语言文学领域论文 |

**查找规则**：
1. 用户说 "按 IEEE 排版" → 读取 `templates/ieee.md`
2. 用户说 "按 APA 排版" → 读取 `templates/apa7.md`
3. 用户说 "按学位论文排版" / "按毕业论文排版" → 读取 `templates/chinese_thesis.md`
4. 用户说 "按 ACM 排版" → 读取 `templates/acm.md`
5. 用户说 "按 Springer 排版" / "按 LNCS 排版" → 读取 `templates/springer_lncs.md`
6. 用户说 "按 NeurIPS 排版" / "按 NIPS 排版" → 读取 `templates/nips.md`
7. 用户说 "按 MLA 排版" → 读取 `templates/mla.md`
8. 无法匹配 → 进入 §6.2 用户自定义流程

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
- **逻辑校验**：检查段落间的论证逻辑。

---

## 8. 排版与环境避坑指南 (Troubleshooting & Best Practices)

> [!WARNING]
> 在执行自动排版和文稿生成时，经常会遇到 Markdown 解析与底层的环境冲突。排版流水管线中必须遵守以下防患规范：

### 8.1 Markdown 嵌套加粗解析的正则剥离
**问题**：`marked.lexer` 在处理复杂嵌套段落（如列表内部的加粗 `**text**`）时，由于默认不会深度递归提取 Inline 级的 `tokens`，易导致 `**` 符号直接作为标点纯文本泄漏到 DOCX 输出中。
**规范**：在构建 `docx-js` 的段落（Paragraph）文本挂载时，**完全摒弃 AST 的样式标记匹配**，统一改用前置自定义正则表达式（如 `text.split(/(\*\*[\s\S]*?\*\*)/g)`）来显式切分，并直接映射为 `new TextRun({ text: innerText, bold: true })`。

### 8.2 Mermaid 编译器的极端脆弱性与语法清洗
**问题**：`npx mmdc` 对生成代码极度挑剔。例如 `usecaseDiagram` 在新版中被废弃不支持，以及在 `erDiagram` 中实体属性若尾随带有双引号 `"` 的外侧注释，会直接导致渲染线程死锁与命令行崩溃。
**规范**：在调用执行环境前，利用替换脚本清洗不合规关键词（把旧语法强转 `flowchart`），并严格剔除危险引号。为防止 Windows 进程隔离出错，配置文件参数中需挂载 `{"args": ["--no-sandbox", "--disable-setuid-sandbox"]}`。

### 8.3 跨平台正则匹配换行符陷阱 (\r\n)
**问题**：在跨平台操作用 Regex 强制提取边界闭合代码块（如 `/```mermaid\n([\s\S]*?)```/g`）时，一旦遇到 Windows 宿主写入的文件采用 `\r\n` 回车换行符，匹配将直接失效导致大片丢图。
**规范**：凡涉猎多行文本切削，务引入容错通配符 `\r?\n` 作为边界判断器，切勿硬编码单一换行类型。

### 8.4 DOCX-JS ImageRun 组件隐性必填项崩溃
**问题**：调用 `ImageRun` 插入 Buffer 图像流引擎时，若遗漏传入 `altText` 参数嵌套组合，编译流水线将毫无明确堆栈反馈地隐蔽崩溃（Packer throw catch 不明）。
**规范**：`ImageRun` 对象初始化时，务必完全补齐挂载三个不可或缺的安全元数据字段：`altText: { title: "x", description: "x", name: "x" }`，以及静态注明 `type: "png"`。

### 8.5 自动化更新时的操作句柄锁 (EBUSY) 防护
**问题**：`fs.writeFileSync` 在意图输出刷新目标文档时，若文档恰好处于用户的浏览窗口进程内占用，即触发 `EBUSY: resource busy or locked` 阻截退出。
**规范**：自动化脚本的导出端名称，应动态拼接自增式数字角标或是动态流转的时间戳（如 `_V3_CLEAN`），从系统层面免于强制覆写锁的冲突灾难。

---

## 9. 学术诚信门禁系统 (Academic Integrity Gate) — 反幻觉 7 模式阻断

> [!CAUTION]
> 本节机制适用于 **Pipeline D（内容生成管道）** 在内容写作完毕后、排版组装前的强制拦截点。不可跳过，不可由 Agent 自行判定"无需执行"。

### 9.1 触发时机
- **预审阶段 (Pre-Review Gate)**：全部章节初稿 `section_N.md` 生成完毕后立即触发。
- **终审阶段 (Final Gate)**：经自审修订后、移交 Pipeline C 排版前再次触发。

### 9.2 七模式阻断清单 (7-Mode Blocking Checklist)

Agent 必须逐项自查并输出结构化报告，每项标注 `✅ 通过` 或 `❌ 阻断（附具体位置与原因）`：

| # | 失败模式 | 检查内容 | 中文说明 |
|---|----------|----------|----------|
| 1 | 实现漏洞伪装创新 | 代码解析中是否将 Bug 或遗漏包装为"设计特性" | 严禁将代码错误美化为"创新点" |
| 2 | 实验数据编造 | 测试章节中的性能数据是否有实际代码或日志来源 | 严禁凭空捏造延迟、吞吐量等数字 |
| 3 | 方法论漂移 | 设计章节描述的架构是否与实际代码结构一致 | 严禁描述一套、代码另一套 |
| 4 | 引文幻觉 | 参考文献中是否存在伪造的作者、年份或期刊名 | 标记所有无法验证的引用为 `[CITE_UNVERIFIED]` |
| 5 | 捷径依赖 | 是否把调用第三方 API 直接等同于"本系统实现了 XX 算法" | 严禁混淆调用与自研 |
| 6 | 空壳章节 | 是否存在少于 300 字的极短章节或大量 `[TODO]` 占位 | 必须返工扩写 |
| 7 | 重复论述 | 多个章节中是否反复解释同一概念（如每章都重新介绍前后端分离） | 去重并交叉引用 |

### 9.3 阻断逻辑
- 存在任何一项 `❌`：**严禁**将文档移交排版。Agent 必须定位问题章节并自动修复后重跑本清单。
- 全部 `✅`：生成 `resources/integrity_report.md` 并继续流程。

---

## 10. 多视角自审评议面板 (Multi-Perspective Self-Review Panel)

> [!IMPORTANT]
> 本节要求 Agent 在完成初稿后，**切换为审稿人人格**进行多维度质量评估。该机制灵感源自同行评审 (Peer Review) 体系，目的在于在没有人类审稿人的情况下，最大程度暴露文本中的逻辑断裂与论证薄弱点。

### 10.1 评审团组成（5 视角 + 魔鬼辩护人）

Agent 必须依次以下列 6 种角色审读全文，每种角色输出独立的简短评语（中文）：

| 角色 | 关注维度 | 中文说明 |
|------|----------|----------|
| 结构审稿人 | 章节逻辑链路、论证递进关系 | 大纲是否清晰？章节之间是否存在逻辑断裂？ |
| 技术审稿人 | 算法描述准确性、系统架构合理性 | 技术细节是否经得起推敲？有无明显的工程谬误？ |
| 语言审稿人 | 学术措辞、句式多样性、口语残留 | 是否有"的的的"叠用、口语化表达、AI 八股化痕迹？ |
| 数据审稿人 | 图表引用完整性、数据自洽性 | 文中引用的图/表编号是否真实存在？数据是否互相矛盾？ |
| 格式审稿人 | 标题层级、引文格式、段落缩进 | 是否符合目标学术模板的排版要求？ |
| **魔鬼辩护人** | **专门反驳核心论点** | **尝试攻击论文的最弱论点，提出最严厉的质疑** |

### 10.2 量化评分表 (0-100 Quality Rubric)

| 维度 | 权重 | 评分标准 |
|------|------|----------|
| 论证逻辑 (Argumentation) | 25% | 推理链条完整性、因果关联强度 |
| 技术深度 (Technical Depth) | 25% | 是否真正触及代码内核而非表层描述 |
| 语言质量 (Language Quality) | 20% | 避免 AI 套话、句式丰富、术语精准 |
| 图表充实度 (Media Richness) | 15% | 每章至少 1 图 1 表 |
| 格式规范 (Format Compliance) | 15% | 严格对齐目标模板要求 |

### 10.3 决策映射
- **≥ 80 分**：通过，直接进入排版管道。
- **65-79 分**：小修 (Minor Revision)，Agent 自动修订评审指出的问题后重新评分。
- **50-64 分**：大修 (Major Revision)，Agent 必须对相关章节进行深度重写。
- **< 50 分**：退稿 (Reject)，输出诊断报告并通知用户介入。

### 10.4 魔鬼辩护人 — 反谄媚机制 (Anti-Sycophancy Protocol)
- 魔鬼辩护人在提出攻击性质疑后，**不允许在一次对抗中连续两次让步**。
- 每次"让步"前必须对反驳的有效性进行 1-5 分评估，仅当评估 ≥ 4 分时才可让步。
- 设定让步率追踪器：全局让步率超过 60% 时触发"锁帧检测 (Frame-Lock Detection)"警报，要求 Agent 退后一步审视前提假设。

---

## 11. 反泄漏与上下文腐蚀防护 (Anti-Leakage & Context-Rot Prevention)

### 11.1 知识隔离指令 (Knowledge Isolation Directive)

在 Pipeline D 的内容生成全过程中，Agent 必须遵守以下铁律：

> **IRON RULE (铁律)：用户提供的项目代码和素材是唯一的事实来源 (Source of Truth)。Agent 禁止使用自身训练数据中的"记忆"来填补任何信息空缺。如果某个技术细节在项目代码中找不到依据，必须标注 `[素材缺口]` 并暂停该段落，而非凭想象补全。**

### 11.2 转场强化注入 (Mid-Conversation Reinforcement)

在多轮章节生成中，每当 Agent 开始撰写新章节时（即从 `section_N.md` 切换到 `section_N+1.md`），必须在内部 System Prompt 中重新注入以下两条提醒：

1. **铁律重申**："你正在撰写学术论文。你的唯一事实来源是用户提供的项目素材。禁止使用记忆填充。"
2. **反模式检测**："检查你即将写的内容是否与前序章节存在大段重复论述。如果是，请用交叉引用（如'如第 X 章所述'）替代重复段落。"

### 11.3 素材缺口标记协议 (Material Gap Protocol)

当 Agent 在撰写过程中发现需要但用户未提供的技术细节时：
- **禁止**使用 AI 内部知识悄悄补全。
- **必须**在该位置插入标记：`[素材缺口：此处需要 XX 的具体实现代码/数据/配置]`
- 在最终的诚信报告 (§9) 中统一列出所有素材缺口，通知用户手动补充。

---

## 12. 写作质量自检清单 (Writing Quality Check) — 中文学术特化

> [!IMPORTANT]
> 本清单在 §10 自审评议的"语言审稿人"环节中强制执行，用于检测 AI 生成文本中常见的模式化痕迹。

### 12.1 AI 高频词警报 (25 个中文高频词)

以下词汇在单篇论文中出现超过指定阈值时触发警告：

| 类别 | 高频词示例 | 单篇上限 |
|------|-----------|----------|
| 虚化修饰 | 有效地、显著地、极大地、充分地、深入地 | 每词 ≤ 5 次 |
| 套话开头 | 随着...的发展、众所周知、近年来、值得注意的是 | 每词 ≤ 3 次 |
| 过度承诺 | 完美地、彻底地、毫无疑问、无可争议 | 每词 ≤ 2 次 |
| AI 典型词 | 赋能、闭环、抓手、痛点、沉淀、拉齐、颗粒度 | 每词 ≤ 2 次 |
| 连接词堆砌 | 因此、然而、此外、与此同时、综上所述 | 每种 ≤ 8 次 |

### 12.2 句式多样性检测 (Burstiness Check)
- 连续 3 个段落的**首句**不得使用相同的句式结构（如连续三段都以"本系统..."开头）。
- 段落长度标准差应 > 30 字（避免机器式的均匀段落）。

### 12.3 清嗓子开头检测 (Throat-Clearing Detection)
- 检测并删除无信息量的开场白，如"为了更好地理解..."、"在本节中，我们将..."。
- 学术写作应直接进入论述核心，而非预告即将说什么。

### 12.4 标点模式控制
- 破折号（——）单篇使用 ≤ 5 次。
- 感叹号（！）在正文中绝对禁用（仅允许出现在致谢等非正文部分）。

---

## 13. 修订分数轨迹追踪 (Score Trajectory Tracking)

当论文经历多轮"写 → 审 → 改"循环时，Agent 必须记录每轮评分，防止修订过程中某些维度意外退化：

```
| 轮次 | 论证逻辑 | 技术深度 | 语言质量 | 图表充实度 | 格式规范 | 总分 |
|------|----------|----------|----------|------------|----------|------|
| R1   | 72       | 68       | 75       | 60         | 80       | 71   |
| R2   | 78       | 75       | 73 ⚠️↓   | 70         | 82       | 76   |
| R3   | 82       | 80       | 80       | 75         | 85       | 81 ✅|
```

- 任何维度分数较上一轮**下降 ≥ 5 分**时，标注 `⚠️↓` 并在修订报告中说明退化原因。
- 总分达到 ≥ 80 分方可移交 Pipeline C 排版引擎。

---

## 14. Pipeline E — 降AI率管道 (AI Detection Rate Reduction)

> [!IMPORTANT]
> 本管道的**完整详细规范**定义在 `ai_reduction/SKILL.md` 中。本节仅做高层描述和使用指南。

### 14.1 功能概述

Pipeline E 专门用于降低论文的AI检测率，将AI生成的文本改写为更自然、更符合人类写作习惯的学术表达。

**核心能力**：
- **中文改写**：动词扩展、词汇替换、句式调整，保持技术术语不变
- **英文LaTeX去AI化**：词汇规范化、结构自然化、移除机械表达

### 14.2 触发方式

#### 方式一：显式指令
```
"使用 ai-reduction 功能对这篇论文进行降AI率处理"
"帮我降低这篇论文的AI检测率"
"对这段文字进行去AI化改写"
```

#### 方式二：Pipeline D 后自动调用
在 `content_generation/SKILL.md` 完成内容生成后，询问用户：
> "论文初稿已生成。是否需要自动进行降AI率处理？回复 **是** 进入 Pipeline E，或 **否** 直接进入排版。"

#### 方式三：独立处理已有文档
```
"使用 ai-reduction 处理这个 Markdown 文件"
"对这个 LaTeX 文件进行去AI化"
```

### 14.3 支持的输入格式

| 格式 | 处理方式 |
|------|----------|
| `.md` | 直接读取，按段落/章节处理 |
| `.tex` | LaTeX源文件，保持格式改写 |
| `.docx` | 通过 `docx/SKILL.md` 读取内容 |
| 纯文本 | 直接处理 |

### 14.4 处理流程

```
Step 1: 语言检测
├── 自动检测主要语言（中文/英文/混合）
└── 选择对应的改写规则

Step 2: 内容拆分
├── 按段落/章节拆分
├── 识别并标记技术术语（保护区域）
└── 创建 checkpoint.json

Step 3: 逐单元改写
├── 应用对应语言的改写规则
├── 验证技术术语未被修改
├── 字数控制（中文模式：不超原文）
└── 更新 checkpoint.json

Step 4: 质量检查
├── 技术术语完整性验证
├── AI高频词残留检测
└── 生成改写报告

Step 5: 输出
├── 保存改写后的文档
└── 输出改写报告
```

### 14.5 中文改写规则摘要

| 规则类型 | 示例 |
|----------|------|
| 动词扩展 | 管理 → 开展...的管理工作 |
| 词汇替换 | 采用→运用、基于→鉴于、利用→借助 |
| 句式调整 | "会将对象移动" → "会把对象移动" |
| 括号整合 | ORM（对象关系映射）→ 对象关系映射即ORM |

**禁止事项**：
- 过于口语化（如"至于xxx呢"）
- 字数膨胀（输出不应多于原文）
- 修改技术术语

### 14.6 英文LaTeX去AI化规则摘要

| 规则类型 | 示例 |
|----------|------|
| 词汇规范化 | leverage→use, delve into→investigate |
| 移除机械连接词 | First and foremost, It is worth noting that |
| 列表转段落 | itemize/enumerate → 连贯段落 |
| 禁用格式强调 | 不使用 \textbf{}, \textit{} |

**修改阈值**：宁缺毋滥。原文已足够自然则保留。

### 14.7 输出格式

**中文模式**：
```
修改后：<改写后的内容>
```

**英文LaTeX模式**：
```
## Part 1 [LaTeX]
（重写后的LaTeX代码）

## Part 2 [Translation]
（中文直译）

## Part 3 [Modification Log]
（修改说明或"检测通过"）
```

### 14.8 完成报告

```
【降AI率处理报告】
源文件：<source_file>
语言模式：<Chinese/English/Mixed>
处理单元数：<N> 段落
原文总字数：<original_count>
改写后字数：<rewritten_count>
字数变化率：<change_rate>%
技术术语保护：<preserved_count>/<total_count>
AI高频词替换：<replaced_count> 处
保留原文段落：<unchanged_count> 段
最终文件：outputs/<name>_reduced_<date>.md
```

### 14.9 与其他管道的集成

```
Pipeline D (内容生成)
        ↓
    [用户选择]
        ↓
Pipeline E (降AI率) ← 可选
        ↓
Pipeline C (排版)
```

---
