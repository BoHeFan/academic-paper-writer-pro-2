<div align="center">

# Academic Paper Writer Pro

<img src="../resources/banner.svg" alt="Academic Paper Writer Pro Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Join%20Chat-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install%20Skill-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)
[![爱発電](https://img.shields.io/badge/爱発電-Support%20Me-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/tfboy1/academic-paper-writer/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.creem.io/payment/prod_1yc40mIhKwwrc7iqFOG9G2)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-README-blue?style=flat-square)](../README.md)
[![English](https://img.shields.io/badge/English-README-blue?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/日本語-現在の言語-red?style=flat-square)](#)
[![Français](https://img.shields.io/badge/Français-README-blue?style=flat-square)](README_FR.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-README-blue?style=flat-square)](README_DE.md)

<br/>

学術論文の研究、執筆、組版を支援するプロフェッショナルなAIエージェントスキル。<br/>
構造化されたワークフローを実行し、`.docx` と `.pdf` の精密な処理能力を活用して、<br/>
原稿が各種学術フォーマット要件（IEEE、ACM、Springer、NeurIPS、MLA、APA、各大学テンプレート）に厳密に準拠することを保証します。

</div>


## 1. 前提条件

本スキルを使用する前に、ファイル操作とコマンドラインツールをサポートするAgenticな環境が必要です。以下の2つの主要環境をサポートしています：

### オプション A: OpenCode（推奨）
開発者のワークフローに最適化されたオープンソースAgenticフレームワーク。
- **インストールガイド**: [OpenCode 公式ドキュメント](https://github.com/code-yeongyu/oh-my-opencode)
- **クイックインストール**:
  - **デスクトップ版**:
https://opencode.ai/download
  - **CLI版**:
  ```bash
  npm install -g opencode
  ```

### オプション B: Claude Code
Anthropicが公式にリリースした Agentic CLI ツール。
- **インストールガイド**: [Claude Code 公式ドキュメント](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- **注意**: 環境に `git` と `npm` がインストールされていることを確認してください。

---

## 2. インストール

ユーザー環境の違いを考慮し、**ワンクリック自動インストール** と **手動設定** の2つの方法を提供しています。

> **🔗 公式スキルページ**: [https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)

### オプション1: ワンクリック自動インストール（推奨）
互換性のあるAgenticフレームワーク（Claude CodeやOpenCodeなど）を使用している場合、作業ディレクトリで以下のコマンドを実行するだけで、システムが自動的にリポジトリを取得し依存関係を設定します：

```bash
npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro
```

### オプション2: 手動クローンと設定
ネットワークやフレームワークの制限でワンクリックインストールが使用できない場合、以下の手順でスキルを手動インポートしてください：

#### 1. リポジトリのクローン
Agentのワークスペースまたはスキルディレクトリに移動し、リポジトリをクローンします：

```bash
# スキルディレクトリにクローン
git clone <your-repo-url> academic-paper-writer
```

#### 2. スキルの読み込み
- **OpenCodeの場合**: エージェントは設定パスのスキルを自動検出します。セッションの再起動が必要な場合や、エージェントに「academic-paper-writerスキルを読み込んでください」と明示的に指示する必要がある場合があります。
- **Claude Codeの場合**: コンテキストウィンドウでこのディレクトリを指定するか、マウントして、Claudeにツールセットとして使用するよう指示できます。

---

## 3. 使用ガイド

インストール完了後、自然言語で執筆と組版のプロセス全体を制御できます。

### ステップ1: ファイルの準備
論文用の作業ディレクトリを作成し、以下のコアファイルを準備します：
1.  **ドラフト**: 原稿内容（Markdown、テキスト、または粗いWordドキュメント）。
2.  **スタイルガイド/テンプレート**: 目標フォーマット要件（例：`IEEE_Template.docx` や `Submission_Guidelines.pdf`）。
3.  **参考文献（オプション）**: `.bib` 形式の参考文献ライブラリ（引用精度のため推奨）。

### ステップ2: エージェントの起動
エージェントを起動し、作業ディレクトリを指定します。

```bash
# OpenCode の例
opencode
```

### ステップ3: スキルの起動
自然言語の指示でワークフローを開始します。システムには主要な学術ジャーナルや会議の組版規格（IEEE、ACM、Springer LNCS、NeurIPS、APA、MLA、中国学位論文フォーマット）が組み込まれています。必要なフォーマットを指定するだけです。

**テンプレート不要の直接組版コマンド:**
> 「このWordドラフトをIEEEフォーマットで再組版してください。」
> 「このMarkdownをSpringer LNCS形式のWordドキュメントに変換してください。」
> 「このコンテンツをACM標準ダブルカラム形式で組版してください。」
> 「NeurIPSの要件に従ってシングルカラムレイアウトにしてください。」
> 「この人文学の課題にMLAフォーマットを使用してください。」

**カスタムテンプレートの組版コマンド:**
> 「この論文の組版を手伝ってください。ドラフトとカスタムテンプレートファイルをこのフォルダに入れました。」
> 「このPDF組版ガイドに基づいて、引用フォーマットとレイアウトを修正してください。」

### 次に何が起こるか？
1.  **事前チェック**: エージェントがドラフトとフォーマットガイドが提供されているか確認します。
2.  **深層分析**: エージェントが `.docx` や `.pdf` のフォーマットガイドを読み取り、フォント、マージン、引用スタイルの要件を理解します。
3.  **組版実行**: エージェントが規格準拠の論文版を生成し、`outputs/` ディレクトリに保存します。
4.  **改良**: 「第3節のロジックをチェック」や「これらの図にキャプションを生成」など、さらなる改善を要求できます。

---

## 4. リソース

このリポジトリは、迅速なスタートに役立つ組み込みリソースを提供しています：

*   📂 **`templates/`**: IEEE、ACM、APAなど、主要な学術会議・ジャーナルの公式テンプレートダウンロードリンクが含まれています。
*   📂 **`examples/`**: スキル機能をテストするための標準ドラフト（`draft.md`）とスタイルガイド（`style_guide.md`）が含まれています。
*   ❓ **`TROUBLESHOOTING.md`**: よくある問題のトラブルシューティングガイド（フォーマットエラー、引用の欠落など）。

---

## クレジットと謝辞

本プロジェクトは、**Anthropic** が提供する強力なドキュメント処理能力を活用しています。

*   **Docx & PDF Skills**: Microsoft WordやPDFドキュメントと対話するための基礎ロジックを提供してくれた [Anthropic Skills Repository](https://github.com/anthropics/skills) に特別な感謝を捧げます。これらのモジュールは、本スキルに精密な読み取り、編集、組版能力を付与しています。
