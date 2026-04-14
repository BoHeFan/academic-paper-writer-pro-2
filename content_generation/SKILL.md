---
name: content_generation
description: 基于代码仓库、笔记、实验数据或论文要求，全自动智能撰写学术论文初稿的主线管线。强制分章逐批检索代码、分步输出，内置规避上下文超限机制和人工审核卡点，无缝衔接格式化引擎。内置严格的学术 Prompt 准则与多模态图表检索能力。
---

# 论文内容智能生成工作流 (Automated Academic Content Generation Pipeline)

本 Skill 专用于 **Pipeline D**。解决"有项目、有数据但没时间写规范八股文"的痛点，将源码或离散数据提炼串联成结构完整的学术论文初稿，严格控制幻觉和上下文崩溃，并**绝对保障顶级学术论文的遣词造句与深度论证标准**。

## 0. 流程总览与组件定义

物料存放在工作区，包括：
- `resources/samples/`：要求文件或参考的优秀范例文献（PDF/DOCX/MD），非必须但如有则优先。
- `resources/outline.md`：大纲定义文件（在第一阶段由系统生成，供用户自由提件与修改）。
- `<用户代码/数据目录>`：论文本体依托的大型项目/数据集目录及其各类脚本日志。

本工程严格采用 **延迟加载 (Lazy Loading)** 和 **按需检索 (Just-in-Time Context)** 设计哲学，避免大型项目全量读取导致的上下文溢出。

## 1. 学术基准提示词工程 (Strict Academic Prompting)

> [!IMPORTANT]
> 大模型在执行所有的章节输出时，**必须在系统层强制包裹以下 Prompt 约束**，严禁出现诸如“毒舌”、“兄弟”、“代码长这样”等随意字眼或过度拟人化的表达。

### 1.1 "Academic Architect" 核心系统指令模型

在撰写任何正文时，必须带入以下系统人设框架：
> **Role:** Act as an expert academic researcher and post-graduate thesis advisor in the domain of Computer Science & Software Engineering.
> **Guidelines for Tone & Style:**
> - **Maintain Formality:** 采用绝对客观、第三人称陈述、精确无歧义的学术性书写风格（Formal, objective, and precise）。杜绝口语化、第一人称情绪发散及非专业俳语。
> - **Academic Rigor:** 从算法复杂度、时空开销、架构解耦 (Decoupling) 等维度对工程代码进行学术升华。必须突出"为什么 (Design Rationale)"和"权衡 (Trade-offs)"，而非仅仅陈述"是什么"。
> - **Rich Formatting:** 当列举功能集、API 规范、硬件配置或测试基准时，**必须强制输出标准的 Markdown 表格 (Tables)** 进行横向维度的专业化对比。
> - **Visual & Diagram Evidence:** 禁止干枯的纯文字堆砌。针对任何架构交互、时序调用或组件流转，**必须**使用 `Mermaid.js` 时序图/状态机或架构图。

> [!CAUTION]
> **铁律 (IRON RULE)：知识隔离指令**（详见主 SKILL.md §11）
> 用户提供的项目代码和素材是唯一的事实来源 (Source of Truth)。Agent 禁止使用自身训练数据中的"记忆"来填补任何信息空缺。如果某个技术细节在项目代码中找不到依据，必须标注 `[素材缺口]` 并暂停该段落，而非凭想象补全。

## 2. 结构定调与大纲生成 (Structure Inference & Approval)

### 2.1 要求与范例解析
当用户提供了会议特定的“要求说明（Call for Papers）”或“参考样例”时，首先通过局部精读提取该会议或期刊习惯的八股文结构、次级标题命名偏好、图表归纳频次及典型引用规范。

### 2.2 起草 `outline.md` 
综合用户的初步想法、工程的根目录 `README.md` 与参考范例，生成 `resources/outline.md`。内容必须囊括：
- **核心论点框架 (Key Contributions)**
- **各级章节标题 (Heading Tree)**
- **各个章节指派的检索策略 (Material Mapping)**（例如：*章节4.1需定位模型的训练函数*；*章节5需查阅 evaluation_results.csv*）
- **图表插入占位 (Proposed Media)**：标明每节应补充哪类架构图或哪几类对比表格。

### 2.3 用户审查卡点 (Mandatory User Review)
生成大纲后，**必须**调用 `notify_user` 强阻断大模型执行流等待人工确认或修改。

## 3. 超大项目上下文控制机制 (Handling Extremely Large Repositories)

1. **地图与索引制备 (Directory Tree Indexing)**：使用树形扫描获取根目录的层级建立“文件寻址地图”，不用实际读取文件内容。
2. **章节局部视界按需挂载 (Section-Scoped Fetching)**：
   - *写 Related Work*：只看根文档提供的关键字，进行外部搜索拓展。
   - *写 Methodology / Implementation*：针对性地执行 `grep_search` 或检索特定算法核心类。

## 4. 严密的逐章节深度解构与撰写 (Deep Analysis Drafting)

> [!CAUTION]
> **撰写 Implementation (核心代码实现) 的避坑指南：**
> 1. **拒绝无脑贴代码**：严禁连续抛出超过 30 行的代码。代码块展示必须“极尽精简”，只摘录状态机扭转、核心事务拦截或特定的核心算法。
> 2. **深度分析架构设计**：必须配有“代码逻辑解析”：如使用了什么设计模式？为何采用该异步库？如何防范死锁？
> 3. **图文并茂**：在进入核心逻辑解析前，**先调用互联网搜索查证最权威的高清架构原理图（如 TCP握手图、LLM Transformer 图例等），或渲染核心流程的 Mermaid 序列图**，再进行行级别的精剖。

### 4.1 撰写与悬挂
1. 依照 `outline.md` 获取素材并用平实考究的学术语言撰写为 `resources/md/section_{current_unit}.md`。
2. 每次完成生成后依据"“4 节冷却法则”"丢弃已使用的深层代码片段，仅保留大纲结构继续推进。
3. **转场强化注入 (Mid-Conversation Reinforcement)**：每当开始撰写新章节时，必须在内部重新注入以下提醒（详见主 SKILL.md §11.2）：
   - 铁律重申："你正在撰写学术论文。你的唯一事实来源是用户提供的项目素材。禁止使用记忆填充。"
   - 反模式检测："检查你即将写的内容是否与前序章节存在大段重复论述。如果是，请用交叉引用替代。"

## 5. 终稿自检与硬性指标机审 (Quality Assurance & Hard Requirements Check)

在所有分章生成完毕后，不要急于交由自动排版，**必须**依次执行以下三个门禁：

### 5.1 物理级脑本校对 (Mechanical QA)
1. **强制执行物理计数脚本 (Mandatory Script Verification)**：严禁大模型通过"肉眼阅读"敷衍估算。必须使用命令行（如 `wc -m` 或 Python 脚本）精确计算生成的合并 `.md` 的中文字符总量。
2. **多模态图表拦截审查**：搜索文档中的 `![` 和 `|---|`（表格）标记，统计其实际数量。必须确保每个大章节至少具有 1-2 张架构配图与对应的 1-2 份三线比对表格。
3. **出具验证自查清单 (Verification Checklist)**：
   - [ ] **物理约束 (Word Count)**：如果任务要求 1.5 万字，脚本跑出仅有 3000 字，**必须阻止流程并强制触发多轮深度扩写死循环，直至达标！**
   - [ ] **图表约束 (Media Integrity)**：图表数量是否符合技术论文标准？
   - [ ] **幻觉与占位**：调用 `grep` 排查是否存在未处理的 `[TODO]` 或极短的空壳章节。
4. **拦截或返工卡点**：如未达标，严禁将残缺文档丢给排版引擎，必须主动重新深入代码库提取细节并重写该异常章节，直到 QA 完全亮绿灯。

### 5.2 学术诚信门禁 (Integrity Gate) — 详见主 SKILL.md §9
物理 QA 通过后，必须执行主 SKILL.md §9 定义的 **7 模式阻断清单**，逐项检查实现漏洞伪装、数据编造、方法论漂移、引文幻觉、捷径依赖、空壳章节、重复论述。全部通过后生成 `resources/integrity_report.md`。

### 5.3 多视角自审评议 (Self-Review Panel) — 详见主 SKILL.md §10
诚信门禁通过后，Agent 必须切换为 6 种审稿人人格（结构/技术/语言/数据/格式/魔鬼辩护人）进行多维度评分。语言审稿人环节必须执行主 SKILL.md §12 的**中文 AI 高频词 25 词警报、句式多样性检测、清嗓子开头检测与标点控制**等子规则。总分 ≥ 80 方可移交排版；< 80 则返工修订并重新评分，并使用主 SKILL.md §13 的**分数轨迹追踪**确保每轮修订不出现维度退化。

## 6. 与排版管道衔接组装 (Handoff to Pipeline C)

> [!CAUTION]
> **严禁使用 Pandoc 进行 Markdown 到 Word 的一键直转！** Pandoc 会丢失所有针对中国学位论文或顶会要求的高度定制化格式（如三线表渲染、首行缩进强绑定等）。

1. 确认 QA + 诚信门禁 + 自审评议（字数与图表容量 + 完整性报告 + 评分 ≥ 80 分）绝对达标后：合并出最终版 `resources/compiled_paper.md`。
2. 更改配置中心 `config.json` 的 pipeline 标记为 `"C"`（表示 MD 已就绪）。
3. 严格调用 **`docx/SKILL.md` 中定义的 `docx-js` (Node引擎)** 进行排版组装，或者在生成后使用原生的 **`unpack -> edit XML -> pack`** 底层手术替换格式文件，确保所有的排版参数 100% 对齐（如严格的中英文字体映射与学术表格规范）。
