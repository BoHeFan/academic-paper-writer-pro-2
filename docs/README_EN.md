<div align="center">

# Academic Paper Writer Pro

<img src="../resources/banner.svg" alt="Academic Paper Writer Pro Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install%20Skill-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)
[![爱发电](https://img.shields.io/badge/爱发电-Support%20Me-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/tfboy1/academic-paper-writer/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.creem.io/payment/prod_1yc40mIhKwwrc7iqFOG9G2)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-README-blue?style=flat-square)](../README.md)
[![English](https://img.shields.io/badge/English-Current-red?style=flat-square)](#)
[![日本語](https://img.shields.io/badge/日本語-README-blue?style=flat-square)](README_JA.md)
[![Français](https://img.shields.io/badge/Français-README-blue?style=flat-square)](README_FR.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-README-blue?style=flat-square)](README_DE.md)

<br/>

A professional AI Agent Skill for assisting with academic paper research, writing, and typesetting.<br/>
This Skill enforces a structured workflow with precise `.docx` and `.pdf` processing capabilities,<br/>
ensuring your manuscripts strictly comply with various academic format requirements (IEEE, ACM, Springer, NeurIPS, MLA, APA, and university templates).

</div>


## 1. Prerequisites

Before using this Skill, you need an Agentic environment that supports file operations and command-line tools. We support the following two mainstream environments:

### Option A: OpenCode (Recommended)
An open-source Agentic framework optimized for developer workflows.
- **Installation Guide**: [OpenCode Official Docs](https://github.com/code-yeongyu/oh-my-opencode)
- **Quick Install**:
  - **Desktop Version**:
https://opencode.ai/download
  - **CLI Version**:
  ```bash
  npm install -g opencode
  ```

### Option B: Claude Code
An Agentic CLI tool officially released by Anthropic.
- **Installation Guide**: [Claude Code Official Docs](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- **Note**: Ensure `git` and `npm` are installed in your environment.

---

## 2. Installation

Considering different user environments, we provide both **one-click automated installation** and **manual configuration** methods.

> **🔗 Official Skill Page**: [https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)

### Option 1: One-Click Automated Installation (Recommended)
If you are using a compatible Agentic framework (such as Claude Code or OpenCode), simply run the following command in your working directory. The system will automatically fetch the repository and configure dependencies:

```bash
npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro
```

### Option 2: Manual Clone and Configuration
If network or framework limitations prevent using the one-click installation, follow these steps to manually import the Skill:

#### 1. Clone the Repository
Navigate to your Agent workspace or Skills directory and clone this repository:

```bash
# Clone to your skills directory
git clone <your-repo-url> academic-paper-writer
```

#### 2. Load the Skill
- **For OpenCode**: The Agent automatically detects Skills in the configuration path. You may need to restart the session or explicitly ask the Agent to "load the academic-paper-writer skill".
- **For Claude Code**: You can provide this directory in the context window or mount it, instructing Claude to use it as a toolset.

---

## 3. Usage Guide

After installation, you can control the entire writing and typesetting process using natural language.

### Step 1: Prepare Files
Create a working directory for your paper and prepare the following core files:
1.  **Draft**: Your original content (Markdown, Text, or a rough Word document).
2.  **Style Guide/Template**: Target format requirements (e.g., `IEEE_Template.docx` or `Submission_Guidelines.pdf`).
3.  **References (Optional)**: A `.bib` reference library (recommended for citation accuracy).

### Step 2: Launch the Agent
Start your Agent and point to your working directory.

```bash
# OpenCode example
opencode
```

### Step 3: Trigger the Skill
Use natural language instructions to start the workflow. Our system includes built-in typesetting standards for major academic journals and conferences (including IEEE, ACM, Springer LNCS, NeurIPS, APA, MLA, and Chinese thesis formats). Simply specify the format you need.

**Direct typesetting commands (no template required):**
> "Please reformat this Word draft according to IEEE format."
> "Convert this Markdown to a Springer LNCS Word document."
> "Typeset this content in ACM standard double-column format."
> "Format according to NeurIPS requirements in single-column layout."
> "Use MLA format for this humanities assignment."
> "Convert this thesis to Chinese degree thesis format."

**Custom template typesetting commands:**
> "Help me typeset this paper. I've placed the draft and custom template file in this folder."
> "Based on this PDF formatting guide, help me fix the citation format and layout."

### What happens next?
1.  **Pre-check**: The Agent verifies that you've provided a draft and format guide.
2.  **Deep Analysis**: The Agent reads the `.docx` or `.pdf` format guide to understand font, margin, citation style requirements.
3.  **Execute Typesetting**: The Agent generates a standards-compliant paper version, saved in the `outputs/` directory.
4.  **Refinement**: You can further request improvements such as "check the logic of section 3" or "generate captions for these figures".

---

## 4. Resources

This repository provides some built-in resources to help you get started quickly:

*   📂 **`templates/`**: Contains download links for official templates of major academic conferences/journals including IEEE, ACM, APA, etc.
*   📂 **`examples/`**: Contains a standard draft (`draft.md`) and style guide (`style_guide.md`) for testing Skill functionality.
*   ❓ **`TROUBLESHOOTING.md`**: Common issues troubleshooting guide (e.g., formatting errors, missing citations, etc.).

---

## Credits & Acknowledgments

This project leverages the powerful document processing capabilities provided by **Anthropic**.

*   **Docx & PDF Skills**: Special thanks to the [Anthropic Skills Repository](https://github.com/anthropics/skills) for providing the foundational logic for interacting with Microsoft Word and PDF documents. These modules give this Skill precise reading, editing, and typesetting capabilities.
