# 论文降AI率工作流 (AI Detection Rate Reduction Pipeline)

<!--
本文件是 Pipeline E 的子模块规范，通过主 SKILL.md 调用。
不要在此添加 YAML frontmatter，否则会被识别为独立 skill。
-->

> [!IMPORTANT]
> 本文件是 **Pipeline E — AI降重管道** 的完整规范。用于将AI生成的论文文本改写为更自然、更符合人类写作习惯的学术表达，降低AI检测率。

## 0. 概述与触发条件

### 0.1 适用场景

| 场景 | 说明 |
|------|------|
| **AI生成内容降重** | 用户使用大模型生成的论文初稿，需要降低AI检测率 |
| **学术润色** | 已有论文需要提升语言自然度和学术规范性 |
| **格式转换后处理** | Pipeline A/B/C/D 完成后的可选后处理步骤 |

### 0.2 触发方式

1. **显式触发**：用户直接指令
   > "使用 `ai-reduction` 功能对这篇论文进行降AI率处理"
   > "帮我降低这篇论文的AI检测率"
   > "对这段文字进行去AI化改写"

2. **自动触发**：Pipeline D 完成后可选自动调用
   - 在 `content_generation/SKILL.md` 完成内容生成后
   - 用户可选择是否自动进入 Pipeline E

### 0.3 支持的输入格式

| 格式 | 处理方式 |
|------|----------|
| `.md` | 直接读取，按段落/章节处理 |
| `.tex` | LaTeX源文件，保持格式改写 |
| `.docx` | 通过 `docx/SKILL.md` 读取内容 |
| 纯文本 | 直接处理 |

---

## 1. 语言检测与模式选择

### 1.1 自动语言检测

系统自动检测输入文本的主要语言：

```
检测规则：
- 中文字符占比 > 30% → 中文模式
- 英文字符占比 > 70% → 英文模式
- 混合内容 → 分段检测，按段落语言分别处理
```

### 1.2 处理模式

| 模式 | Prompt文件 | 核心规则 |
|------|-----------|----------|
| **中文改写** | `prompts/chinese_rewrite.md` | 动词扩展、词汇替换、句式调整 |
| **英文LaTeX去AI化** | `prompts/english_latex.md` | 词汇规范化、结构自然化、排版规范 |

---

## 2. 中文改写规则 (Chinese Rewrite Rules)

> [!IMPORTANT]
> 详细规则见 `prompts/chinese_rewrite.md`，以下为核心要点摘要。

### 2.1 核心改写手法

#### 2.1.1 增加冗余与解释性 (Verbose Elaboration)

**动词短语扩展**：
| 原文 | 改写 |
|------|------|
| 管理 | 开展...的管理工作 / 进行管理 |
| 交互 | 进行交互 / 开展交互 |
| 配置 | 进行配置 |
| 处理 | 去处理...工作 |
| 恢复 | 进行恢复 |
| 实现 | 得以实现 / 来实现 |

**增加辅助词**：
- 适当增加 "了"、"的"、"地"、"所"、"会"、"可以"、"这个"、"方面"、"当中" 等
- 示例："提供功能" → "拥有...功能"

#### 2.1.2 系统性词汇替换 (Systematic Synonym Substitution)

| 原词 | 替换词 |
|------|--------|
| 采用 / 使用 | 运用 / 选用 / 把...当作...来使用 |
| 基于 | 鉴于 / 基于...来开展 |
| 利用 | 借助 / 运用 / 凭借 |
| 通过 | 借助 / 依靠 / 凭借 |
| 和 / 及 / 与 | 以及（尤其是列举多项时） |
| 并 | 并且 / 还 / 同时 |
| 其 | 它 / 其（根据语境选择） |
| 原因 | 缘由 / 主要原因囊括... |
| 符合 | 契合 |
| 适合 | 适宜 |
| 特点 | 特性 |
| 提升 / 提高 | 提高 / 提升（可互换，保持多样性） |
| 极大(地) | 极大程度(上) |
| 立即 | 马上 |

#### 2.1.3 括号内容处理 (Bracket Content Integration)

**解释性括号**：
- 优先整合：将括号内信息自然融入句子
- 使用引导词："也就是"、"即"、"比如"、"像"
- 示例：
  - `ORM（对象关系映射）` → `对象关系映射即ORM`
  - `功能（如ORM、Admin）` → `功能，比如ORM、Admin等`

**代码/标识符旁括号**：
- 通常直接移除括号
- 示例：
  - `视图 (views.py) 中` → `视图也就是views.py中`

#### 2.1.4 句式微调与口语化倾向

**使用"把"字句**：
- 示例："会将对象移动" → "会把对象移动"

**条件句式转换**：
- 示例："若...，则..." → "要是...，那就..." 或 "如果...，就..."

**增加语气词/连接词**：
- 在句首或句中添加 "那么"、"这样"、"同时" 等

### 2.2 禁止事项

| 禁止 | 说明 |
|------|------|
| **过于口语化** | 不要出现 "至于xxx呢" 这类表达 |
| **字数膨胀** | 输出内容不应多于原文 |
| **第一人称** | 不使用 "我"、"我们" |
| **技术术语修改** | 所有技术术语、代码、API路径等绝对不变 |

### 2.3 技术术语保护清单

以下内容**绝对禁止修改**：
- 技术术语：Django, RESTful API, Ceph, RGW, S3, JWT, ORM, MySQL 等
- 代码片段：views.py, settings.py, accounts.CustomUser, .folder_marker 等
- 库名：Boto3, djangorestframework-simplejwt 等
- 配置项：CEPH_STORAGE, DATABASES 等
- API路径：/accounts/api/token/refresh/ 等
- 数学公式：保持原样
- 变量名、函数名、类名

---

## 3. 英文LaTeX去AI化规则 (English LaTeX De-AI Rules)

> [!IMPORTANT]
> 详细规则见 `prompts/english_latex.md`，以下为核心要点摘要。

### 3.1 词汇规范化 (Vocabulary Normalization)

#### 3.1.1 AI高频词替换表

| 避免（AI高频） | 使用（自然表达） |
|---------------|-----------------|
| leverage | use, utilize, employ |
| delve into | investigate, examine, explore |
| tapestry | context, framework, landscape |
| underscore | highlight, emphasize, show |
| paramount | important, critical, essential |
| pivotal | key, central, important |
| burgeoning | growing, expanding |
| multifaceted | complex, various |
| nuanced | subtle, detailed |
| robust | reliable, stable, strong |
| seamless | smooth, integrated |
| cutting-edge | advanced, modern, state-of-the-art |
| groundbreaking | innovative, novel |
| revolutionize | transform, change, improve |

#### 3.1.2 词汇选择原则

- **朴实精准**：优先使用简单、准确的学术词汇
- **避免堆砌**：不要为"高级感"而使用复杂词汇
- **术语适度**：仅在表达特定技术含义时使用术语

### 3.2 结构自然化 (Structure Naturalization)

#### 3.2.1 禁止格式

| 禁止 | 替代方案 |
|------|----------|
| 列表格式（itemize/enumerate） | 转化为逻辑连贯的普通段落 |
| 生硬过渡词 | 通过句子逻辑递进自然连接 |

**机械连接词移除清单**：
- First and foremost
- It is worth noting that
- It is important to note that
- In order to（简化为 to）
- On the one hand... On the other hand（简化或重组）

#### 3.2.2 标点规范

| 减少使用 | 替代方案 |
|----------|----------|
| 破折号（—） | 逗号、括号或从句结构 |
| 连续多个逗号 | 重组句子结构 |

### 3.3 排版规范 (Formatting Rules)

| 规则 | 说明 |
|------|------|
| **禁用加粗** | 正文中不使用 `\textbf{}` 进行强调 |
| **禁用斜体** | 正文中不使用 `\textit{}` 或 `\emph{}` 进行强调 |
| **保持LaTeX纯净** | 不引入无关的格式指令 |
| **数学公式原样** | 保留所有 `$...$` 和 `\[...\]` |

### 3.4 修改阈值 (Modification Threshold)

> [!CAUTION]
> **宁缺毋滥**：如果输入文本已经自然、地道且无明显AI特征，保留原文，不要为修改而修改。

**判断标准**：
- 文本语气自然，无机械感
- 词汇使用恰当，无AI高频词堆砌
- 句式多样，无模板化痕迹
- 逻辑流畅，无生硬过渡

**正向反馈**：对高质量输入，应在输出中明确肯定。

### 3.5 输出格式

```
## Part 1 [LaTeX]
（重写后的LaTeX代码，如果原文足够好则输出原文）

## Part 2 [Translation]
（对应的中文直译）

## Part 3 [Modification Log]
如果进行了修改：
- 简要说明调整了哪些机械化表达

如果未修改：
- 输出：[检测通过] 原文表达地道自然，无明显AI味，建议保留。
```

---

## 4. 处理流程 (Processing Workflow)

### 4.1 预处理阶段

```
Step 1: 输入验证
├── 检查文件格式
├── 检测文本语言
└── 统计基本信息（段落数、字数）

Step 2: 内容拆分
├── Markdown: 按段落/章节拆分
├── LaTeX: 按段落/环境拆分
├── DOCX: 提取文本内容后按段落拆分
└── 创建 checkpoint.json 记录进度
```

### 4.2 核心处理阶段

```
Step 3: 逐单元处理
├── 读取当前单元内容
├── 识别并标记技术术语（保护区域）
├── 应用对应语言的改写规则
├── 验证技术术语未被修改
├── 输出改写结果
└── 更新 checkpoint.json

Step 4: 质量检查（每2单元）
├── 检查字数是否超标（中文模式）
├── 检查技术术语完整性
├── 检查格式是否正确（LaTeX模式）
└── 标记需要人工复核的区域
```

### 4.3 后处理阶段

```
Step 5: 汇总输出
├── 合并所有改写单元
├── 生成改写报告
├── 保存到 outputs/ 目录
└── 列出所有修改点供用户确认
```

---

## 5. 技术术语保护机制

### 5.1 自动识别规则

```python
# 技术术语识别正则
TECH_PATTERNS = [
    r'[A-Z][a-z]+[A-Z][a-zA-Z]*',  # CamelCase
    r'[a-z_]+\.[a-z_]+',            # dotted.names
    r'/[a-zA-Z0-9/_\-]+',           # API paths
    r'\$[^\$]+\$',                  # LaTeX math
    r'\\[a-zA-Z]+\{[^\}]*\}',       # LaTeX commands
    r'[A-Z]{2,}',                   # Acronyms (API, ORM, JWT)
]
```

### 5.2 保护流程

1. **预处理标记**：识别所有技术术语，用特殊标记包裹
   - 示例：`Django` → `[[TECH:Django]]`
   
2. **改写执行**：对非标记区域应用改写规则

3. **后处理还原**：移除保护标记，还原技术术语
   - 示例：`[[TECH:Django]]` → `Django`

4. **验证检查**：对比原文和输出，确保技术术语完全一致

---

## 6. 目录规范

```
项目根目录/
├── resources/
│   ├── ai_reduction/
│   │   ├── original/        # 原始文本备份
│   │   ├── processed/       # 处理后的文本
│   │   └── report.json      # 改写报告
│   └── checkpoint.json      # 进度记录
├── outputs/
│   └── <name>_reduced_<date>.md  # 最终输出
└── ai_reduction/
    ├── SKILL.md             # 本文件
    └── prompts/
        ├── chinese_rewrite.md
        └── english_latex.md
```

---

## 7. 使用示例

### 7.1 中文改写示例

**原文**：
```
本系统采用Django框架进行开发，通过RESTful API实现前后端交互。
系统具有用户管理、权限控制等功能。
```

**改写后**：
```
本系统选用Django框架来开展开发工作，借助RESTful API来实现前后端的交互。
系统拥有用户管理、权限控制等方面的功能。
```

### 7.2 英文LaTeX示例

**原文**：
```latex
First and foremost, we leverage the transformer architecture to delve into the 
nuanced patterns in the data. It is worth noting that this approach is paramount 
for achieving robust performance.
```

**改写后**：
```latex
We use the transformer architecture to examine the subtle patterns in the data. 
This approach is critical for achieving reliable performance.
```

**Modification Log**：
- Removed "First and foremost" (mechanical transition)
- "leverage" → "use" (avoid AI high-frequency word)
- "delve into" → "examine" (avoid AI high-frequency word)
- "nuanced" → "subtle" (avoid AI high-frequency word)
- Removed "It is worth noting that" (mechanical transition)
- "paramount" → "critical" (avoid AI high-frequency word)
- "robust" → "reliable" (avoid AI high-frequency word)

---

## 8. 质量保证

### 8.1 自动检查项

| 检查项 | 说明 | 阈值 |
|--------|------|------|
| 技术术语完整性 | 所有技术术语未被修改 | 100% |
| 字数控制（中文） | 输出字数不超过原文 | ≤ 105% |
| 格式完整性（LaTeX） | 所有LaTeX命令有效 | 100% |
| AI高频词检测 | 检测是否还有AI痕迹 | 报告残留 |

### 8.2 人工复核触发条件

以下情况需要人工复核：
- 技术术语被修改（自动拒绝）
- 改写后语义可能变化
- 原文已足够自然，无需修改
- 用户指定区域

---

## 9. 与其他Pipeline的集成

### 9.1 作为后处理步骤

```
Pipeline D (内容生成)
        ↓
    [用户选择]
        ↓
Pipeline E (降AI率) ← 可选
        ↓
Pipeline C (排版)
```

### 9.2 独立使用

用户可直接调用 Pipeline E 处理已有文档：
> "使用 ai-reduction 对这篇论文进行降AI率处理"

---

## 10. 完成报告格式

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
保留原文段落：<unchanged_count> 段（原文已足够自然）
最终文件：outputs/<name>_reduced_<date>.md
```
