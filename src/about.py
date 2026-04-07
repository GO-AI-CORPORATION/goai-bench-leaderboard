TITLE = """
<div class="goai-header">
    <h1>GO AI Bench Leaderboard</h1>
    <p class="goai-subtitle">Open benchmarking leaderboard for NLP models on Burkinab&egrave; languages &mdash; Moor&eacute; &amp; Dioula<br>
    ASR &middot; MT &middot; TTS &mdash; across Health, Education, Child Protection &amp; Environment domains</p>
    <div class="goai-links">
        <a href="https://github.com/GO-AI-CORPORATION/goai-bench">GitHub Toolkit</a> &middot;
        <a href="https://huggingface.co/goaicorp">HuggingFace Org</a> &middot;
        <a href="https://goaicorporation.org/">GO AI Corp</a>
    </div>
    <img class="goai-logo" src="https://raw.githubusercontent.com/GO-AI-CORPORATION/goai-bench-leaderboard/main/assets/go-ai-bench-logo.png" alt="GO AI Bench" />
</div>
"""

# ====================== LEADERBOARD GUIDES ======================

LEADERBOARD_INTRO_EN = """
**Welcome to the GO AI Bench Leaderboard!** Browse and compare models benchmarked on Mooré and Dioula across ASR, MT, and TTS tasks.

**How to use:** Select a language tab below, then a task sub-tab. Use the filters to narrow results by domain, model type, architecture, or size. Click column headers to sort. The 🥇🥈🥉 medals highlight the top 3 models.
"""

LEADERBOARD_INTRO_FR = """
**Bienvenue sur le classement GO AI Bench !** Parcourez et comparez les modèles évalués sur le Mooré et le Dioula pour les tâches ASR, TA et STT.

**Comment utiliser :** Sélectionnez un onglet de langue ci-dessous, puis un sous-onglet de tâche. Utilisez les filtres pour affiner par domaine, type de modèle, architecture ou taille. Cliquez sur les en-têtes de colonnes pour trier. Les médailles 🥇🥈🥉 mettent en avant les 3 meilleurs modèles.
"""

MOORE_GUIDE_EN = """
**Mooré (mos_Latn)** — Dominant language of Burkina Faso with ~8M speakers. Gur (Oti-Volta) family. Select a task below to view rankings.
"""

MOORE_GUIDE_FR = """
**Mooré (mos_Latn)** — Langue dominante du Burkina Faso avec ~8M de locuteurs. Famille Gur (Oti-Volta). Sélectionnez une tâche ci-dessous pour voir les classements.
"""

DIOULA_GUIDE_EN = """
**Dioula (dyu_Latn)** — Major lingua franca of West Africa (~12M speakers). Also known as Dyula/Jula. Mande family. Select a task below to view rankings.
"""

DIOULA_GUIDE_FR = """
**Dioula (dyu_Latn)** — Langue véhiculaire majeure d'Afrique de l'Ouest (~12M de locuteurs). Aussi connue sous le nom de Dyula/Jula. Famille Mandé. Sélectionnez une tâche ci-dessous pour voir les classements.
"""

ASR_GUIDE_EN = """
**Automatic Speech Recognition (ASR)** — Models are ranked by **WER (Word Error Rate)** ↓ lower is better. Secondary metrics: CER, MER.
Filter by domain to see how models perform on Health, Education, or other sector-specific content.
"""

ASR_GUIDE_FR = """
**Reconnaissance automatique de la parole (ASR)** — Les modèles sont classés par **WER (taux d'erreur de mots)** ↓ plus bas = meilleur. Métriques secondaires : CER, MER.
Filtrez par domaine pour voir les performances sur la Santé, l'Éducation ou d'autres contenus sectoriels.
"""

MT_GUIDE_EN = """
**Machine Translation (MT)** — Models are ranked by **chrF++ (character F-score)** ↑ higher is better. Secondary: BLEU, TER. COMET-Kiwi when available.
MT is evaluated in both directions. Use the domain filter to compare performance on specialized content.
"""

MT_GUIDE_FR = """
**Traduction automatique (TA)** — Les modèles sont classés par **chrF++ (F-score caractère)** ↑ plus haut = meilleur. Secondaires : BLEU, TER. COMET-Kiwi si disponible.
La TA est évaluée dans les deux sens. Utilisez le filtre de domaine pour comparer les performances sur du contenu spécialisé.
"""

TTS_GUIDE_EN = """
**Text-to-Speech (TTS)** — Models are ranked by **UTMOS (naturalness score)** ↑ higher is better. Secondary: Loopback WER/CER (intelligibility via ASR re-transcription).
Filter by domain to see how speech synthesis quality varies across different content types.
"""

TTS_GUIDE_FR = """
**Synthèse vocale (TTS)** — Les modèles sont classés par **UTMOS (score de naturel)** ↑ plus haut = meilleur. Secondaires : Loopback WER/CER (intelligibilité via re-transcription ASR).
Filtrez par domaine pour voir comment la qualité de synthèse varie selon les types de contenu.
"""

# ====================== INFO PAGE ======================

INFO_TEXT_EN = """
## About GO AI Bench

**GO AI Bench** is an open benchmarking toolkit for evaluating NLP models on low-resource Burkinabè languages, developed by **[GO AI Corporation](https://goaicorporation.org/)** under a **UNICEF WCARO** consultancy on NLP for linguistic inclusion.

### Supported Languages

| Language | ISO 639-3 | Script | Region | Speakers |
|----------|-----------|--------|--------|----------|
| **Mooré** | `mos` | Latin | Burkina Faso, Ghana, Togo | ~8M |
| **Dioula** | `dyu` | Latin | Burkina Faso, Côte d'Ivoire, Mali | ~12M |

### Evaluation Tasks

| Task | Primary Metric | Direction | Description |
|------|---------------|-----------|-------------|
| **ASR** | WER | Lower ↓ | Automatic Speech Recognition |
| **MT** | chrF++ | Higher ↑ | Machine Translation (French ↔ Local) |
| **TTS** | UTMOS | Higher ↑ | Text-to-Speech |

### Evaluation Domains

Results are broken down across 5 domains relevant to UNICEF programming:
- **General** — Cross-domain baseline (FLORES-200)
- **Health** — Maternal/child health, vaccination, nutrition
- **Education** — School enrollment, literacy, learning materials
- **Child Protection** — Birth registration, child labor, child marriage
- **Environment** — Climate change, water, sanitation

### How It Works

1. **Benchmark** your model using the [GO AI Bench toolkit](https://github.com/GO-AI-CORPORATION/goai-bench)
2. **Submit** the JSON results on this Space via the "Submit Results" tab
3. **Compare** your model against existing state-of-the-art on the Leaderboard

### Links

- [GO AI Bench Toolkit (GitHub)](https://github.com/GO-AI-CORPORATION/goai-bench)
- [GO AI Corp HuggingFace](https://huggingface.co/goaicorp)
- [GO AI Corporation Website](https://goaicorporation.org/)
"""

INFO_TEXT_FR = """
## À propos de GO AI Bench

**GO AI Bench** est un outil de benchmarking ouvert pour évaluer les modèles NLP sur les langues burkinabè à faibles ressources, développé par **[GO AI Corporation](https://goaicorporation.org/)** dans le cadre d'une consultance **UNICEF WCARO** sur le NLP pour l'inclusion linguistique.

### Langues supportées

| Langue | ISO 639-3 | Script | Région | Locuteurs |
|--------|-----------|--------|--------|-----------|
| **Mooré** | `mos` | Latin | Burkina Faso, Ghana, Togo | ~8M |
| **Dioula** | `dyu` | Latin | Burkina Faso, Côte d'Ivoire, Mali | ~12M |

### Tâches d'évaluation

| Tâche | Métrique primaire | Direction | Description |
|-------|------------------|-----------|-------------|
| **ASR** | WER | Plus bas ↓ | Reconnaissance automatique de la parole |
| **TA** | chrF++ | Plus haut ↑ | Traduction automatique (Français ↔ Langues locales) |
| **STT** | UTMOS | Plus haut ↑ | Synthèse vocale |

### Domaines d'évaluation

Les résultats sont ventilés sur 5 domaines pertinents pour la programmation UNICEF :
- **Général** — Base inter-domaine (FLORES-200)
- **Santé** — Santé maternelle/infantile, vaccination, nutrition
- **Éducation** — Scolarisation, alphabétisation, matériels d'apprentissage
- **Protection de l'enfance** — Enregistrement des naissances, travail des enfants
- **Environnement** — Changement climatique, eau, assainissement

### Comment ça marche

1. **Évaluez** votre modèle avec le [toolkit GO AI Bench](https://github.com/GO-AI-CORPORATION/goai-bench)
2. **Soumettez** les résultats JSON sur ce Space via l'onglet « Soumettre des résultats »
3. **Comparez** votre modèle avec l'état de l'art existant sur le Leaderboard

### Liens

- [Toolkit GO AI Bench (GitHub)](https://github.com/GO-AI-CORPORATION/goai-bench)
- [GO AI Corp HuggingFace](https://huggingface.co/goaicorp)
- [Site web GO AI Corporation](https://goaicorporation.org/)
"""

# ====================== TASKS PAGE ======================

TASKS_TEXT_EN = """
## Evaluation Tasks

### ASR — Automatic Speech Recognition

Evaluate speech-to-text transcription accuracy on Mooré and Dioula audio.

| Metric | Description | Range | Better |
|--------|-------------|-------|--------|
| **WER** (primary) | Word Error Rate | 0–∞ | Lower ↓ |
| CER | Character Error Rate | 0–∞ | Lower ↓ |
| MER | Match Error Rate | 0–1 | Lower ↓ |

**Baseline models:** Whisper (base/small/large-v3-turbo), MMS-1b-all, Wav2Vec2-large-MMS-1b

---

### MT — Machine Translation

Evaluate translation quality between French (`fra_Latn`) and target languages in both directions.

| Metric | Description | Range | Better |
|--------|-------------|-------|--------|
| **chrF++** (primary) | Character F-score with word unigrams/bigrams | 0–100 | Higher ↑ |
| BLEU | Bilingual Evaluation Understudy | 0–100 | Higher ↑ |
| TER | Translation Edit Rate | 0–∞ | Lower ↓ |
| COMET-Kiwi | Reference-free quality estimation | −1–1 | Higher ↑ |

**Baseline models:** NLLB-200 (600M, 1.3B, 3.3B)

---

### TTS — Text-to-Speech

Evaluate synthesized speech quality via naturalness scoring and intelligibility (loopback ASR).

| Metric | Description | Range | Better |
|--------|-------------|-------|--------|
| **UTMOS** (primary) | Naturalness MOS prediction | 1–5 | Higher ↑ |
| Loopback WER | Re-transcription WER of synthesized audio | 0–∞ | Lower ↓ |
| Loopback CER | Re-transcription CER of synthesized audio | 0–∞ | Lower ↓ |

**Baseline models:** Spark-TTS, MMS-TTS
"""

TASKS_TEXT_FR = """
## Tâches d'évaluation

### ASR — Reconnaissance automatique de la parole

Évaluer la précision de transcription parole-vers-texte sur l'audio Mooré et Dioula.

| Métrique | Description | Plage | Meilleur |
|----------|-------------|-------|----------|
| **WER** (primaire) | Taux d'erreur de mots | 0–∞ | Plus bas ↓ |
| CER | Taux d'erreur de caractères | 0–∞ | Plus bas ↓ |
| MER | Taux d'erreur de correspondance | 0–1 | Plus bas ↓ |

**Modèles de base :** Whisper (base/small/large-v3-turbo), MMS-1b-all, Wav2Vec2-large-MMS-1b

---

### TA — Traduction automatique

Évaluer la qualité de traduction entre le français (`fra_Latn`) et les langues cibles dans les deux sens.

| Métrique | Description | Plage | Meilleur |
|----------|-------------|-------|----------|
| **chrF++** (primaire) | F-score caractère avec unigrammes/bigrammes | 0–100 | Plus haut ↑ |
| BLEU | Bilingual Evaluation Understudy | 0–100 | Plus haut ↑ |
| TER | Taux d'édition de traduction | 0–∞ | Plus bas ↓ |
| COMET-Kiwi | Estimation de qualité sans référence | −1–1 | Plus haut ↑ |

**Modèles de base :** NLLB-200 (600M, 1.3B, 3.3B)

---

### STT — Synthèse vocale (Text-to-Speech)

Évaluer la qualité de la parole synthétisée via le score de naturel et l'intelligibilité (ASR en boucle).

| Métrique | Description | Plage | Meilleur |
|----------|-------------|-------|----------|
| **UTMOS** (primaire) | Prédiction MOS de naturel | 1–5 | Plus haut ↑ |
| Loopback WER | WER de re-transcription de l'audio synthétisé | 0–∞ | Plus bas ↓ |
| Loopback CER | CER de re-transcription de l'audio synthétisé | 0–∞ | Plus bas ↓ |

**Modèles de base :** Spark-TTS, MMS-TTS
"""

# ====================== SUBMISSION PAGE ======================

SUBMISSION_TEXT_EN = """
## Submit Your Results

### Step 1: Benchmark your model

Run the [GO AI Bench toolkit](https://github.com/GO-AI-CORPORATION/goai-bench) to evaluate your model:

```bash
pip install -e .
python scripts/run_benchmark.py --task asr --language mos_Latn --model your-model-id --verbose
```

This generates a **summary.json** file with your results.

### Step 2: Upload and preview

Upload your JSON result file below. A preview card will show your results before submission.

### Step 3: Fill optional metadata

Add information about your model (type, organization, architecture, size) to help others filter and compare.

### Step 4: Submit

Click "Submit" to add your results to the leaderboard. You need to be logged in with your HuggingFace account.
"""

SUBMISSION_TEXT_FR = """
## Soumettre vos résultats

### Étape 1 : Évaluer votre modèle

Exécutez le [toolkit GO AI Bench](https://github.com/GO-AI-CORPORATION/goai-bench) pour évaluer votre modèle :

```bash
pip install -e .
python scripts/run_benchmark.py --task asr --language mos_Latn --model votre-modele-id --verbose
```

Cela génère un fichier **summary.json** avec vos résultats.

### Étape 2 : Uploader et prévisualiser

Uploadez votre fichier JSON de résultats ci-dessous. Une carte de prévisualisation affichera vos résultats avant la soumission.

### Étape 3 : Remplir les métadonnées optionnelles

Ajoutez des informations sur votre modèle (type, organisation, architecture, taille) pour aider les autres à filtrer et comparer.

### Étape 4 : Soumettre

Cliquez sur « Soumettre » pour ajouter vos résultats au classement. Vous devez être connecté avec votre compte HuggingFace.
"""

# ====================== CITATION ======================

CITATION_BUTTON_LABEL = "Citation"
CITATION_BUTTON_TEXT = r"""@misc{goai_bench_2026,
  title={GO AI Bench: Open Evaluation Platform for Burkinabè Languages},
  author={GO AI Corporation},
  year={2026},
  howpublished={\url{https://github.com/GO-AI-CORPORATION/goai-bench}},
  note={Developed under UNICEF WCARO consultancy on NLP for linguistic inclusion}
}"""
