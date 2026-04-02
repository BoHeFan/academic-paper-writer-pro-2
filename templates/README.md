# Academic Paper Templates

This directory is intended to store academic paper templates. Due to copyright and binary format constraints, we provide the official download links below. Please download the appropriate template for your submission and place it here or in your working directory.

## IEEE (Institute of Electrical and Electronics Engineers)
*   **Conference Template (Word/LaTeX)**: [IEEE Author Center - Article Templates](https://ieeeauthorcenter.ieee.org/create-your-ieee-article/use-authoring-tools-and-ieee-article-templates/ieee-article-templates/)
    *   *Direct Link (Word)*: [Conference Template Word](https://www.ieee.org/content/dam/ieee-org/ieee/web/org/conferences/conference-template-a4.docx) (Note: Link may change, verify on official site)
*   **Journal Template**: Same link as above, select "Transactions, Journals, and Letters".

## ACM (Association for Computing Machinery)
*   **Master Article Template**: [ACM TAPS Workflow](https://www.acm.org/publications/taps/word-template-workflow)
    *   *Submission Template*: Use the single-column submission template for review.
    *   *Primary Article Template*: Use the specific template for your OS (Windows/Mac) for final camera-ready submission.

## APA (American Psychological Association)
*   **Student Paper Setup Guide**: [APA Style - Student Paper Setup Guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf)
*   **Sample Papers (Word)**: [APA Style - Sample Papers](https://apastyle.apa.org/style-grammar-guidelines/paper-format/sample-papers)
    *   *Student Sample Paper*: [Download .docx](https://apastyle.apa.org/style-grammar-guidelines/paper-format/student-paper.docx)
    *   *Professional Sample Paper*: [Download .docx](https://apastyle.apa.org/style-grammar-guidelines/paper-format/professional-paper.docx)

## Springer (LNCS - Lecture Notes in Computer Science)
*   **Information for Authors**: [Springer LNCS](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines)
    *   *Word Template*: [Download splnproc1703.zip](https://resource-cms.springernature.com/springer-cms/rest/v1/content/7117506/data/v1)

## NeurIPS (Neural Information Processing Systems)
*   **Conference Guidelines**: [NeurIPS Paper Information](https://neurips.cc/Conferences/2024/PaperInformation)
*   **Style Files**: NeurIPS natively provides LaTeX style files (`neurips_2024.sty`), but our system encapsulates the exact font, margin, and layout requirements (US Letter, 10pt, single column) into our automated pipeline.

## MLA (Modern Language Association)
*   **General Guidelines**: [Purdue OWL MLA Formatting](https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_general_format.html)
*   **Core Configuration**: 1-inch margins, double-spacing, Times New Roman 12pt, half-inch indent for paragraphs.

---

## 🎯 如何使用内置的格式预设 (How to use these templates)

本仓库已经在 `templates/` 文件夹内为您提前定义了以上所有主流学术格式（IEEE, ACM, Springer LNCS, NeurIPS, APA, MLA, 中国学位论文）的 `.md` 规范描述。

**您只需要在对话中直接告诉 Agent：**
- "将这份文档按 `[这里填入格式，比如 ACM]` 排版"

Agent 就会自动从对应的 `.md` 规范文件中读取字体、行距、边距、编号等规则，从底层重新修改您论文的 XML 外观，无需您手动下载应用 Word 模板即可实现一键换装！

**Tip**: 如果您的目标会议比较冷门，或者有着极为特殊的自定义排版要求，您仍然可以按照传统方式——直接在工作目录下放置一个 `.docx` 模板文件，告诉 Agent："参考这个模板进行排版"。
