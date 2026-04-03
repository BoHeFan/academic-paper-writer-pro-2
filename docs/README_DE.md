<div align="center">

# Academic Paper Writer Pro

<img src="../resources/banner.svg" alt="Academic Paper Writer Pro Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Beitreten-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Installieren-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)
[![爱发电](https://img.shields.io/badge/爱发电-Unterstützen-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/tfboy1/academic-paper-writer/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.creem.io/payment/prod_1yc40mIhKwwrc7iqFOG9G2)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-README-blue?style=flat-square)](../README.md)
[![English](https://img.shields.io/badge/English-README-blue?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/日本語-README-blue?style=flat-square)](README_JA.md)
[![Français](https://img.shields.io/badge/Français-README-blue?style=flat-square)](README_FR.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-Aktuelle%20Sprache-red?style=flat-square)](#)

<br/>

Ein professioneller AI-Agent-Skill zur Unterstützung bei Forschung, Verfassen und Satz akademischer Arbeiten.<br/>
Dieser Skill erzwingt einen strukturierten Workflow mit präzisen `.docx`- und `.pdf`-Verarbeitungsfähigkeiten,<br/>
und stellt sicher, dass Ihre Manuskripte strikt den jeweiligen akademischen Formatanforderungen entsprechen (IEEE, ACM, Springer, NeurIPS, MLA, APA und Hochschulvorlagen).

</div>


## 1. Voraussetzungen

Bevor Sie diesen Skill verwenden, benötigen Sie eine agentische Umgebung, die Dateioperationen und Kommandozeilentools unterstützt. Wir unterstützen die folgenden zwei Hauptumgebungen:

### Option A: OpenCode (Empfohlen)
Ein Open-Source-Agentic-Framework, optimiert für Entwickler-Workflows.
- **Installationsanleitung**: [Offizielle OpenCode-Dokumentation](https://github.com/code-yeongyu/oh-my-opencode)
- **Schnellinstallation**:
  - **Desktop-Version**:
https://opencode.ai/download
  - **CLI-Version**:
  ```bash
  npm install -g opencode
  ```

### Option B: Claude Code
Ein offiziell von Anthropic veröffentlichtes Agentic-CLI-Tool.
- **Installationsanleitung**: [Offizielle Claude Code-Dokumentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- **Hinweis**: Stellen Sie sicher, dass `git` und `npm` in Ihrer Umgebung installiert sind.

---

## 2. Installation

Unter Berücksichtigung verschiedener Benutzerumgebungen bieten wir sowohl eine **automatische Ein-Klick-Installation** als auch eine **manuelle Konfiguration** an.

> **🔗 Offizielle Skill-Seite**: [https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)

### Option 1: Automatische Ein-Klick-Installation (Empfohlen)
Wenn Sie ein kompatibles Agentic-Framework (wie Claude Code oder OpenCode) verwenden, führen Sie einfach den folgenden Befehl in Ihrem Arbeitsverzeichnis aus. Das System ruft automatisch das Repository ab und konfiguriert die Abhängigkeiten:

```bash
npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro
```

### Option 2: Manuelles Klonen und Konfigurieren
Wenn Netzwerk- oder Framework-Einschränkungen die Ein-Klick-Installation verhindern, folgen Sie diesen Schritten zum manuellen Import des Skills:

#### 1. Repository klonen
Navigieren Sie zu Ihrem Agent-Workspace oder Skills-Verzeichnis und klonen Sie dieses Repository:

```bash
# In Ihr Skills-Verzeichnis klonen
git clone <your-repo-url> academic-paper-writer
```

#### 2. Skill laden
- **Für OpenCode**: Der Agent erkennt Skills im Konfigurationspfad automatisch. Möglicherweise müssen Sie die Sitzung neu starten oder den Agent explizit bitten, „den academic-paper-writer-Skill zu laden".
- **Für Claude Code**: Sie können dieses Verzeichnis im Kontextfenster bereitstellen oder einbinden und Claude anweisen, es als Toolset zu verwenden.

---

## 3. Bedienungsanleitung

Nach der Installation können Sie den gesamten Schreib- und Satzprozess in natürlicher Sprache steuern.

### Schritt 1: Dateien vorbereiten
Erstellen Sie ein Arbeitsverzeichnis für Ihre Arbeit und bereiten Sie die folgenden Kerndateien vor:
1.  **Entwurf**: Ihr Originalinhalt (Markdown, Text oder grobes Word-Dokument).
2.  **Stilvorlage/Vorlage**: Zielformatanforderungen (z.B. `IEEE_Template.docx` oder `Submission_Guidelines.pdf`).
3.  **Literaturverzeichnis (Optional)**: Eine Referenzbibliothek im `.bib`-Format (empfohlen für Zitiergenauigkeit).

### Schritt 2: Agent starten
Starten Sie Ihren Agent und zeigen Sie auf Ihr Arbeitsverzeichnis.

```bash
# OpenCode-Beispiel
opencode
```

### Schritt 3: Skill auslösen
Verwenden Sie natürlichsprachliche Anweisungen, um den Workflow zu starten. Unser System enthält eingebaute Satzstandards für wichtige akademische Zeitschriften und Konferenzen (einschließlich IEEE, ACM, Springer LNCS, NeurIPS, APA, MLA und chinesische Dissertationsformate). Geben Sie einfach das benötigte Format an.

**Direkte Satzbefehle (keine Vorlage erforderlich):**
> „Bitte formatieren Sie diesen Word-Entwurf im IEEE-Format um."
> „Konvertieren Sie dieses Markdown in ein Springer LNCS Word-Dokument."
> „Setzen Sie diesen Inhalt im ACM-Standard-Zweispaltenformat."
> „Formatieren Sie gemäß den NeurIPS-Anforderungen im Einspalten-Layout."
> „Verwenden Sie das MLA-Format für diese geisteswissenschaftliche Arbeit."

**Satzbefehle mit benutzerdefinierter Vorlage:**
> „Helfen Sie mir, diese Arbeit zu setzen. Ich habe den Entwurf und die benutzerdefinierte Vorlagendatei in diesem Ordner abgelegt."
> „Basierend auf diesem PDF-Formatierungsleitfaden, helfen Sie mir, das Zitierformat und das Layout zu korrigieren."

### Was passiert als Nächstes?
1.  **Vorprüfung**: Der Agent prüft, ob Sie einen Entwurf und einen Formatierungsleitfaden bereitgestellt haben.
2.  **Tiefenanalyse**: Der Agent liest den `.docx`- oder `.pdf`-Formatierungsleitfaden, um Schriftart-, Rand- und Zitierstilanforderungen zu verstehen.
3.  **Satzausführung**: Der Agent erstellt eine standardkonforme Version der Arbeit, die im Verzeichnis `outputs/` gespeichert wird.
4.  **Verfeinerung**: Sie können weitere Verbesserungen anfordern, z.B. „überprüfen Sie die Logik von Abschnitt 3" oder „erstellen Sie Bildunterschriften für diese Abbildungen".

---

## 4. Ressourcen

Dieses Repository bietet einige eingebaute Ressourcen, um Ihnen den schnellen Einstieg zu erleichtern:

*   📂 **`templates/`**: Enthält Download-Links für offizielle Vorlagen wichtiger akademischer Konferenzen und Zeitschriften, darunter IEEE, ACM, APA usw.
*   📂 **`examples/`**: Enthält einen Standard-Entwurf (`draft.md`) und einen Stilleitfaden (`style_guide.md`) zum Testen der Skill-Funktionalität.
*   ❓ **`TROUBLESHOOTING.md`**: Leitfaden zur Fehlerbehebung häufiger Probleme (Formatierungsfehler, fehlende Zitate usw.).

---

## Danksagungen

Dieses Projekt nutzt die leistungsstarken Dokumentenverarbeitungsfähigkeiten von **Anthropic**.

*   **Docx & PDF Skills**: Besonderer Dank an das [Anthropic Skills Repository](https://github.com/anthropics/skills) für die Bereitstellung der grundlegenden Logik zur Interaktion mit Microsoft Word- und PDF-Dokumenten. Diese Module verleihen diesem Skill präzise Lese-, Bearbeitungs- und Satzfähigkeiten.
