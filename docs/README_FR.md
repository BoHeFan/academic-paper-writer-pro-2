<div align="center">

# Academic Paper Writer Pro

<img src="../resources/banner.svg" alt="Academic Paper Writer Pro Banner" width="100%"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-Rejoindre-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/DrqtEjk6)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Installer-00C853?style=for-the-badge&logo=hackthebox&logoColor=white)](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)
[![爱发电](https://img.shields.io/badge/爱发电-Soutenir-FF69B4?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.ifdian.net/item/1a20ed042f0711f1865a52540025c377)
[![License](https://img.shields.io/github/license/tfboy1/academic-paper-writer?style=for-the-badge&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tfboy1/academic-paper-writer?style=for-the-badge&logo=github&color=yellow)](https://github.com/tfboy1/academic-paper-writer/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.creem.io/payment/prod_1yc40mIhKwwrc7iqFOG9G2)

<br/>

[![简体中文](https://img.shields.io/badge/简体中文-README-blue?style=flat-square)](../README.md)
[![English](https://img.shields.io/badge/English-README-blue?style=flat-square)](README_EN.md)
[![日本語](https://img.shields.io/badge/日本語-README-blue?style=flat-square)](README_JA.md)
[![Français](https://img.shields.io/badge/Français-Langue%20actuelle-red?style=flat-square)](#)
[![Deutsch](https://img.shields.io/badge/Deutsch-README-blue?style=flat-square)](README_DE.md)

<br/>

Un Skill d'Agent IA professionnel pour assister la recherche, la rédaction et la mise en page de publications académiques.<br/>
Ce Skill applique un workflow structuré avec des capacités de traitement `.docx` et `.pdf` précises,<br/>
garantissant que vos manuscrits respectent strictement les exigences de format académique (IEEE, ACM, Springer, NeurIPS, MLA, APA et modèles universitaires).

</div>


## 1. Prérequis

Avant d'utiliser ce Skill, vous avez besoin d'un environnement Agentique prenant en charge les opérations sur les fichiers et les outils en ligne de commande. Nous supportons les deux environnements principaux suivants :

### Option A : OpenCode (Recommandé)
Un framework Agentique open-source optimisé pour les workflows des développeurs.
- **Guide d'installation** : [Documentation officielle OpenCode](https://github.com/code-yeongyu/oh-my-opencode)
- **Installation rapide** :
  - **Version bureau** :
https://opencode.ai/download
  - **Version CLI** :
  ```bash
  npm install -g opencode
  ```

### Option B : Claude Code
Un outil CLI Agentique officiellement publié par Anthropic.
- **Guide d'installation** : [Documentation officielle Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- **Note** : Assurez-vous que `git` et `npm` sont installés dans votre environnement.

---

## 2. Installation

Compte tenu des différents environnements utilisateurs, nous proposons à la fois une **installation automatisée en un clic** et une **configuration manuelle**.

> **🔗 Page officielle du Skill** : [https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro](https://skills.sh/tfboy1/academic-paper-writer/academic-paper-writer-pro)

### Option 1 : Installation automatisée en un clic (Recommandé)
Si vous utilisez un framework Agentique compatible (comme Claude Code ou OpenCode), exécutez simplement la commande suivante dans votre répertoire de travail. Le système récupérera automatiquement le dépôt et configurera les dépendances :

```bash
npx skills add https://github.com/tfboy1/academic-paper-writer --skill academic-paper-writer-pro
```

### Option 2 : Clonage et configuration manuels
Si des limitations réseau ou de framework empêchent l'utilisation de l'installation en un clic, suivez ces étapes pour importer manuellement le Skill :

#### 1. Cloner le dépôt
Naviguez vers votre espace de travail Agent ou répertoire de Skills et clonez ce dépôt :

```bash
# Cloner dans votre répertoire de skills
git clone <your-repo-url> academic-paper-writer
```

#### 2. Charger le Skill
- **Pour OpenCode** : L'Agent détecte automatiquement les Skills dans le chemin de configuration. Vous devrez peut-être redémarrer la session ou demander explicitement à l'Agent de « charger le skill academic-paper-writer ».
- **Pour Claude Code** : Vous pouvez fournir ce répertoire dans la fenêtre de contexte ou le monter, en indiquant à Claude de l'utiliser comme ensemble d'outils.

---

## 3. Guide d'utilisation

Après l'installation, vous pouvez contrôler l'ensemble du processus de rédaction et de mise en page en langage naturel.

### Étape 1 : Préparer les fichiers
Créez un répertoire de travail pour votre article et préparez les fichiers essentiels suivants :
1.  **Brouillon** : Votre contenu original (Markdown, Texte ou document Word brut).
2.  **Guide de style / Modèle** : Exigences de format cibles (par exemple, `IEEE_Template.docx` ou `Submission_Guidelines.pdf`).
3.  **Références (Optionnel)** : Une bibliothèque de références au format `.bib` (recommandé pour la précision des citations).

### Étape 2 : Lancer l'Agent
Démarrez votre Agent et pointez vers votre répertoire de travail.

```bash
# Exemple OpenCode
opencode
```

### Étape 3 : Déclencher le Skill
Utilisez des instructions en langage naturel pour démarrer le workflow. Notre système intègre des normes de mise en page pour les principales revues et conférences académiques (IEEE, ACM, Springer LNCS, NeurIPS, APA, MLA et formats de thèses chinoises). Spécifiez simplement le format dont vous avez besoin.

**Commandes de mise en page directe (sans modèle requis) :**
> « Veuillez reformater ce brouillon Word selon le format IEEE. »
> « Convertir ce Markdown en document Word au format Springer LNCS. »
> « Mettre en page ce contenu au format double colonne standard ACM. »
> « Formater selon les exigences NeurIPS en mise en page simple colonne. »
> « Utiliser le format MLA pour ce devoir en sciences humaines. »

**Commandes avec modèle personnalisé :**
> « Aidez-moi à mettre en page cet article. J'ai placé le brouillon et le fichier de modèle personnalisé dans ce dossier. »
> « Sur la base de ce guide de formatage PDF, aidez-moi à corriger le format des citations et la mise en page. »

### Que se passe-t-il ensuite ?
1.  **Vérification préalable** : L'Agent vérifie que vous avez fourni un brouillon et un guide de format.
2.  **Analyse approfondie** : L'Agent lit le guide de format `.docx` ou `.pdf` pour comprendre les exigences en matière de police, marges et style de citation.
3.  **Exécution de la mise en page** : L'Agent génère une version conforme aux normes, enregistrée dans le répertoire `outputs/`.
4.  **Raffinement** : Vous pouvez demander des améliorations supplémentaires telles que « vérifier la logique de la section 3 » ou « générer des légendes pour ces figures ».

---

## 4. Ressources

Ce dépôt fournit des ressources intégrées pour vous aider à démarrer rapidement :

*   📂 **`templates/`** : Contient des liens de téléchargement pour les modèles officiels des principales conférences et revues académiques, notamment IEEE, ACM, APA, etc.
*   📂 **`examples/`** : Contient un brouillon standard (`draft.md`) et un guide de style (`style_guide.md`) pour tester les fonctionnalités du Skill.
*   ❓ **`TROUBLESHOOTING.md`** : Guide de dépannage des problèmes courants (erreurs de formatage, citations manquantes, etc.).

---

## Crédits et remerciements

Ce projet s'appuie sur les puissantes capacités de traitement de documents fournies par **Anthropic**.

*   **Docx & PDF Skills** : Remerciements spéciaux au [Anthropic Skills Repository](https://github.com/anthropics/skills) pour avoir fourni la logique fondamentale d'interaction avec les documents Microsoft Word et PDF. Ces modules confèrent à ce Skill des capacités précises de lecture, d'édition et de mise en page.
