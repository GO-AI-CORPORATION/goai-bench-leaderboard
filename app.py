import json
import os

import gradio as gr
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from huggingface_hub import snapshot_download

from src.about import (
    ASR_GUIDE_EN,
    ASR_GUIDE_FR,
    CITATION_BUTTON_LABEL,
    CITATION_BUTTON_TEXT,
    DIOULA_GUIDE_EN,
    DIOULA_GUIDE_FR,
    INFO_TEXT_EN,
    INFO_TEXT_FR,
    LEADERBOARD_INTRO_EN,
    LEADERBOARD_INTRO_FR,
    MOORE_GUIDE_EN,
    MOORE_GUIDE_FR,
    MT_GUIDE_EN,
    MT_GUIDE_FR,
    SUBMISSION_TEXT_EN,
    SUBMISSION_TEXT_FR,
    TASKS_TEXT_EN,
    TASKS_TEXT_FR,
    TITLE,
    TTS_GUIDE_EN,
    TTS_GUIDE_FR,
)
from src.display.css_html_js import custom_css
from src.envs import API, EVAL_RESULTS_PATH, REPO_ID, RESULTS_REPO, SEED_DATA_PATH, TOKEN
from src.leaderboard.read_evals import load_all_results
from src.populate import build_leaderboard_df, get_unique_values
from src.submission.submit import generate_preview_html, submit_result
from src.tasks import (
    DOMAIN_DISPLAY_NAMES,
    DOMAIN_KEYS,
    MODEL_SIZE_CATEGORIES,
    MODEL_TYPES,
    TASK_CONFIGS,
    Language,
    get_all_metrics,
)


def restart_space():
    API.restart_space(repo_id=REPO_ID)


try:
    snapshot_download(
        repo_id=RESULTS_REPO,
        local_dir=EVAL_RESULTS_PATH,
        repo_type="dataset",
        tqdm_class=None,
        etag_timeout=10,
        token=TOKEN,
    )
except Exception as e:
    print(f"Could not download HF results (will use seed data only): {e}")

ALL_RESULTS = load_all_results(SEED_DATA_PATH, EVAL_RESULTS_PATH)

UNIQUE_ORGS = ["All"] + get_unique_values(ALL_RESULTS, "organization")
UNIQUE_ARCHS = {
    task_id: ["All"] + cfg.architectures
    for task_id, cfg in TASK_CONFIGS.items()
}


def get_display_columns(task_id):
    cfg = TASK_CONFIGS[task_id]
    metric_keys = [cfg.primary_metric] + cfg.secondary_metrics
    cols_order = ["rank", "model_id", "organization", "model_type", "base_architecture", "model_size_category"]
    cols_order += [f"avg_{m}" for m in metric_keys]
    cols_order += ["total_samples", "timestamp"]

    display_names = {
        "rank": "Rank",
        "model_id": "Model",
        "organization": "Organization",
        "model_type": "Type",
        "base_architecture": "Architecture",
        "model_size_category": "Size",
        "total_samples": "Samples",
        "timestamp": "Date",
    }
    for m in metric_keys:
        display_names[f"avg_{m}"] = cfg.metric_display_names.get(m, m)

    return cols_order, display_names


def apply_filters(df, org, model_type, sizes, architectures, search_text, task_id):
    if df.empty:
        return df

    if org and org != "All":
        df = df[df["organization"] == org]

    if model_type:
        selected = [t for t in model_type if t in MODEL_TYPES]
        if selected and len(selected) < len(MODEL_TYPES):
            df = df[df["model_type"].isin(selected)]

    if sizes:
        selected = [s for s in sizes if s in MODEL_SIZE_CATEGORIES]
        if selected and len(selected) < len(MODEL_SIZE_CATEGORIES):
            df = df[df["model_size_category"].isin(selected)]

    if architectures:
        archs = [a for a in architectures if a != "All"]
        if archs:
            df = df[df["base_architecture"].isin(archs)]

    if search_text and search_text.strip():
        query = search_text.strip().lower()
        mask = (
            df["model_id_raw"].str.lower().str.contains(query, na=False)
            | df["organization"].str.lower().str.contains(query, na=False)
        )
        df = df[mask]

    return df


def create_leaderboard_tab(task_id, language_code, mt_pair=None):
    """Create a complete leaderboard tab with filters and table."""
    cfg = TASK_CONFIGS[task_id]
    cols_order, display_names = get_display_columns(task_id)

    base_df = build_leaderboard_df(ALL_RESULTS, task_id, language_code, mt_pair)

    task_guide = {
        "asr": (ASR_GUIDE_EN, ASR_GUIDE_FR),
        "mt": (MT_GUIDE_EN, MT_GUIDE_FR),
        "tts": (TTS_GUIDE_EN, TTS_GUIDE_FR),
    }
    guide_en, guide_fr = task_guide.get(task_id, ("", ""))

    with gr.Column():
        gr.Markdown(guide_en + "\n\n" + guide_fr, elem_classes="guide-text")

        with gr.Row(elem_classes="filter-row"):
            domain_dd = gr.Dropdown(
                choices=["All"] + [DOMAIN_DISPLAY_NAMES[k] for k in DOMAIN_KEYS],
                value="All",
                label="Domain / Domaine",
                interactive=True,
            )
            org_dd = gr.Dropdown(
                choices=UNIQUE_ORGS,
                value="All",
                label="Organization / Organisation",
                interactive=True,
            )
            arch_dd = gr.Dropdown(
                choices=UNIQUE_ARCHS.get(task_id, ["All"]),
                value="All",
                label="Architecture",
                interactive=True,
            )

        with gr.Row(elem_classes="filter-row"):
            type_cb = gr.CheckboxGroup(
                choices=MODEL_TYPES,
                value=MODEL_TYPES,
                label="Model Type / Type de modèle",
                interactive=True,
            )
            size_cb = gr.CheckboxGroup(
                choices=MODEL_SIZE_CATEGORIES,
                value=MODEL_SIZE_CATEGORIES,
                label="Model Size / Taille du modèle",
                interactive=True,
            )

        with gr.Row():
            search_box = gr.Textbox(
                label="",
                placeholder="Search by model name or organization / Rechercher par nom de modèle ou organisation...",
                show_label=False,
                scale=5,
            )
            search_btn = gr.Button("🔍 Search", elem_classes="goai-btn", scale=1)

        visible_cols = [c for c in cols_order if c in base_df.columns] if not base_df.empty else cols_order
        display_df = base_df[visible_cols].copy() if not base_df.empty else pd.DataFrame(columns=visible_cols)
        display_df = display_df.rename(columns=display_names)

        table = gr.Dataframe(
            value=display_df,
            datatype=["str", "markdown", "str", "str", "str", "str"]
            + ["number"] * max(len(visible_cols) - 8, 0)
            + ["number", "str"],
            interactive=False,
            elem_id="llm-benchmark-tab-table",
        )

    def update_table(domain, org, model_type, sizes, arch, search_text):
        domain_key = "average"
        if domain and domain != "All":
            for k, v in DOMAIN_DISPLAY_NAMES.items():
                if v == domain:
                    domain_key = k
                    break

        df = build_leaderboard_df(ALL_RESULTS, task_id, language_code, mt_pair, domain_key)
        if df.empty:
            return pd.DataFrame(columns=[display_names.get(c, c) for c in cols_order])

        arch_list = [arch] if arch and arch != "All" else None
        df = apply_filters(df, org, model_type, sizes, arch_list, search_text, task_id)

        vis = [c for c in cols_order if c in df.columns]
        df = df[vis].rename(columns=display_names)
        return df

    all_inputs = [domain_dd, org_dd, type_cb, size_cb, arch_dd, search_box]
    for inp in [domain_dd, org_dd, type_cb, size_cb, arch_dd]:
        inp.change(update_table, inputs=all_inputs, outputs=[table])
    search_btn.click(update_table, inputs=all_inputs, outputs=[table])
    search_box.submit(update_table, inputs=all_inputs, outputs=[table])


def create_submission_tab():
    """Create the submission tab with file upload, preview, and metadata fields."""
    with gr.Row():
        with gr.Column(scale=1):
            json_upload = gr.File(
                label="Upload JSON result / Uploader le fichier JSON",
                file_types=[".json"],
                type="filepath",
            )
            preview_html = gr.HTML(
                value="<p style='color: #999; text-align: center; padding: 40px;'>"
                "Upload a JSON file to preview / Uploadez un fichier JSON pour prévisualiser</p>"
            )

        with gr.Column(scale=1):
            gr.Markdown("### Model Metadata / Métadonnées du modèle")
            model_type_dd = gr.Dropdown(
                choices=MODEL_TYPES,
                value="Open Source",
                label="Model Type / Type de modèle",
                interactive=True,
            )
            organization_tb = gr.Textbox(
                label="Organization / Organisation",
                placeholder="e.g. GO AI Corp, Meta, Anonymous...",
            )
            hf_model_id_tb = gr.Textbox(
                label="HuggingFace Model ID (if open source)",
                placeholder="e.g. goaicorp/mos-whisper-large-v3-turbo",
            )
            arch_dd = gr.Dropdown(
                choices=[
                    "Whisper", "Wav2Vec2", "MMS", "Seq2Seq (NLLB)", "Decoder-Only",
                    "SparkTTS", "MMS-TTS", "VITS", "xTTSv2", "Other",
                ],
                value="Other",
                label="Base Architecture",
                interactive=True,
            )
            size_tb = gr.Textbox(
                label="Model Size (B) / Taille du modèle (milliards)",
                placeholder="e.g. 1.3",
            )

    def on_upload(file):
        if file is None:
            return "<p style='color: #999; text-align: center;'>No file uploaded</p>"
        try:
            with open(file, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                data = data[0]
            return generate_preview_html(data)
        except Exception as e:
            return f"<p style='color: red;'>Error parsing JSON: {e}</p>"

    json_upload.change(on_upload, inputs=[json_upload], outputs=[preview_html])

    with gr.Row():
        submit_btn = gr.Button(
            "🚀 Submit Results / Soumettre les résultats",
            elem_classes="goai-btn",
            scale=2,
        )

    result_md = gr.HTML()

    submit_btn.click(
        submit_result,
        inputs=[json_upload, model_type_dd, organization_tb, hf_model_id_tb, arch_dd, size_tb],
        outputs=[result_md],
    )


# ====================== BUILD APP ======================

demo = gr.Blocks(css=custom_css, theme=gr.themes.Default())

with demo:
    gr.HTML(TITLE)

    with gr.Tabs(elem_classes="tab-buttons") as main_tabs:
        # ===== LEADERBOARD TAB =====
        with gr.TabItem("🏅 Leaderboard", id=1):
            gr.Markdown(
                LEADERBOARD_INTRO_EN + "\n\n" + LEADERBOARD_INTRO_FR,
                elem_classes="guide-text",
            )

            with gr.Tabs(elem_classes="tab-buttons") as lang_tabs:
                # ----- Mooré -----
                with gr.TabItem("🇧🇫 Mooré (mos)", id=10):
                    gr.Markdown(MOORE_GUIDE_EN + "\n" + MOORE_GUIDE_FR, elem_classes="guide-text")

                    with gr.Tabs(elem_classes="tab-buttons") as mos_task_tabs:
                        with gr.TabItem("🎤 ASR", id=101):
                            create_leaderboard_tab("asr", "mos_Latn")

                        with gr.TabItem("🔄 MT: FR → Mooré", id=102):
                            create_leaderboard_tab("mt", "mos_Latn", "fra_Latn_mos_Latn")

                        with gr.TabItem("🔄 MT: Mooré → FR", id=103):
                            create_leaderboard_tab("mt", "mos_Latn", "mos_Latn_fra_Latn")

                        with gr.TabItem("🔊 TTS", id=104):
                            create_leaderboard_tab("tts", "mos_Latn")

                # ----- Dioula -----
                with gr.TabItem("🇧🇫 Dioula (dyu)", id=11):
                    gr.Markdown(DIOULA_GUIDE_EN + "\n" + DIOULA_GUIDE_FR, elem_classes="guide-text")

                    with gr.Tabs(elem_classes="tab-buttons") as dyu_task_tabs:
                        with gr.TabItem("🎤 ASR", id=111):
                            create_leaderboard_tab("asr", "dyu_Latn")

                        with gr.TabItem("🔄 MT: FR → Dioula", id=112):
                            create_leaderboard_tab("mt", "dyu_Latn", "fra_Latn_dyu_Latn")

                        with gr.TabItem("🔄 MT: Dioula → FR", id=113):
                            create_leaderboard_tab("mt", "dyu_Latn", "dyu_Latn_fra_Latn")

        # ===== INFO TAB =====
        with gr.TabItem("💡 Info", id=2):
            with gr.Tabs(elem_classes="tab-buttons"):
                with gr.TabItem("🇬🇧 English", id=21):
                    gr.Markdown(INFO_TEXT_EN, elem_classes="docs-content")
                with gr.TabItem("🇫🇷 Français", id=22):
                    gr.Markdown(INFO_TEXT_FR, elem_classes="docs-content")

        # ===== TASKS TAB =====
        with gr.TabItem("📝 Tasks / Tâches", id=3):
            with gr.Tabs(elem_classes="tab-buttons"):
                with gr.TabItem("🇬🇧 English", id=31):
                    gr.Markdown(TASKS_TEXT_EN, elem_classes="docs-content")
                with gr.TabItem("🇫🇷 Français", id=32):
                    gr.Markdown(TASKS_TEXT_FR, elem_classes="docs-content")

        # ===== SUBMIT TAB =====
        with gr.TabItem("🚀 Submit Results / Soumettre", id=4):
            with gr.Tabs(elem_classes="tab-buttons"):
                with gr.TabItem("🇬🇧 English", id=41):
                    gr.Markdown(SUBMISSION_TEXT_EN, elem_classes="docs-content")
                    create_submission_tab()
                with gr.TabItem("🇫🇷 Français", id=42):
                    gr.Markdown(SUBMISSION_TEXT_FR, elem_classes="docs-content")
                    gr.Markdown(
                        "*Utilisez le formulaire dans l'onglet English ci-dessus / "
                        "Use the form in the English tab above*"
                    )

    # ===== CITATION =====
    with gr.Row():
        with gr.Accordion("📙 Citation", open=False):
            gr.Textbox(
                value=CITATION_BUTTON_TEXT,
                label=CITATION_BUTTON_LABEL,
                lines=8,
                elem_id="citation-button",
                show_copy_button=True,
            )

if os.environ.get("SPACE_ID"):
    scheduler = BackgroundScheduler()
    scheduler.add_job(restart_space, "interval", seconds=1800)
    scheduler.start()

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("GRADIO_SERVER_PORT", "7860")),
    allowed_paths=["assets"],
    show_api=False,
)
