# Troubleshooting Guide

When using the Academic Paper Writer Skill, you might encounter issues due to the complexity of file formats and AI limitations. Here are common problems and solutions.

## 1. Document Parsing Issues
**Problem**: The Agent cannot read my `.docx` template or draft correctly.
**Solution**:
*   Ensure the file is not password protected.
*   Convert complex `.doc` (older format) files to `.docx`.
*   If tables or images are missing in the parsed text, describe them explicitly in a separate text file (e.g., "Figure 1 shows x, insert it after paragraph 2").

## 2. Formatting Glitches
**Problem**: The output document has broken layout, wrong margins, or font issues.
**Solution**:
*   **Iterative Fixing**: Ask the Agent to fix specific issues. "The margins on page 2 are wrong, fix them."
*   **Simplified Template**: If the provided template is very complex (lots of macros/VBA), try finding a cleaner version.
*   **Manual Touch-up**: AI is great at 90% of the work. For final camera-ready submission, manual adjustment in Word/LaTeX is often faster for the last 10%.

## 3. Reference Hallucinations
**Problem**: The Agent generated fake citations or references.
**Solution**:
*   **Provide a `.bib` file**: If you have a BibTeX file, explicitly upload it and tell the Agent to use ONLY these references.
*   **Verification**: Ask the Agent to "Verify all references against Google Scholar" (this requires the Web Search capability).

## 4. Context Window Limits (Long Papers)
**Problem**: For very long papers (50+ pages), the Agent forgets instructions or cuts off text.
**Solution**:
*   **Chunking**: Ask the Agent to work section by section. "Format the Introduction first," then "Format the Methodology."
*   **Separate Files**: Split your draft into `01_Intro.md`, `02_Method.md`, etc.

## 5. Image/Figure Handling
**Problem**: Images are not inserted or are in the wrong place.
**Solution**:
*   Place all images in a `figures/` folder.
*   Use placeholders in your draft like `[INSERT FIGURE 1 HERE]`.
*   Explicitly tell the Agent: "Insert `figures/fig1.png` at the placeholder [INSERT FIGURE 1 HERE] with width 8cm."
