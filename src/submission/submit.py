import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import gradio as gr

from src.display.formatting import styled_error, styled_message, styled_warning
from src.envs import API, DATA_REPO, EVAL_RESULTS_PATH, RESULTS_DIR, TOKEN
from src.submission.check_validity import validate_goai_json
from src.tasks import TASK_CONFIGS, Domain, Language, get_metric_keys, size_category_from_b

REFRESH_INTERVAL_MIN = 60


def _result_fingerprint(data: Dict[str, Any]) -> str:
    """Deterministic hash of the core result fields to detect exact duplicates."""
    key_parts = [
        data.get("model_id", ""),
        data.get("task", ""),
        data.get("benchmark_language", ""),
        data.get("mt_pair", ""),
        json.dumps(data.get("average", {}), sort_keys=True),
        json.dumps(data.get("groups", {}), sort_keys=True),
    ]
    return hashlib.sha256("|".join(key_parts).encode()).hexdigest()[:16]


def _existing_fingerprints() -> set:
    """Collect fingerprints of already-submitted results on disk."""
    fps: set = set()
    if not os.path.isdir(EVAL_RESULTS_PATH):
        return fps
    for root, _, files in os.walk(EVAL_RESULTS_PATH):
        for fname in files:
            if not fname.endswith(".json"):
                continue
            try:
                with open(os.path.join(root, fname), encoding="utf-8") as f:
                    d = json.load(f)
                if isinstance(d, list):
                    d = d[0] if len(d) == 1 else {}
                fps.add(_result_fingerprint(d))
            except Exception:
                pass
    return fps


def generate_preview_html(data: Dict[str, Any]) -> str:
    task = data.get("task", "?")
    cfg = TASK_CONFIGS.get(task)
    lang_code = data.get("benchmark_language", "?")
    lang_name = lang_code
    for l in Language:
        if l.value.code == lang_code:
            lang_name = l.value.display_name
            break

    model_id = data.get("model_id", "Unknown")
    mt_pair = data.get("mt_pair", "")
    direction_label = ""
    if mt_pair:
        parts = mt_pair.split("_")
        if len(parts) >= 4:
            src = "_".join(parts[:2])
            tgt = "_".join(parts[2:])
            direction_label = f"<span class='preview-badge'>{src} → {tgt}</span>"

    header = f"""
    <div class="preview-card">
        <div class="preview-header">
            <h3>📋 {model_id}</h3>
            <div class="preview-badges">
                <span class="preview-badge task">{task.upper()}</span>
                <span class="preview-badge lang">{lang_name}</span>
                {direction_label}
            </div>
        </div>
    """

    avg = data.get("average", {})
    avg_html = "<div class='preview-section'><h4>📊 Average Metrics / Métriques moyennes</h4><div class='metric-grid'>"
    if cfg:
        for mk in get_metric_keys(task):
            val = avg.get(mk)
            display = cfg.metric_display_names.get(mk, mk)
            val_str = f"{val:.4f}" if val is not None else "N/A"
            is_primary = mk == cfg.primary_metric
            cls = "metric-primary" if is_primary else "metric-secondary"
            avg_html += f"<div class='metric-card {cls}'><span class='metric-name'>{display}</span><span class='metric-value'>{val_str}</span></div>"
    avg_html += "</div></div>"

    groups = data.get("groups", {})
    domain_html = ""
    if groups:
        domain_html = "<div class='preview-section'><h4>🏷️ Per-Domain Results / Résultats par domaine</h4>"
        domain_html += "<table class='preview-table'><thead><tr><th>Domain</th><th>N</th>"
        if cfg:
            for mk in get_metric_keys(task):
                domain_html += f"<th>{cfg.metric_display_names.get(mk, mk)}</th>"
        domain_html += "</tr></thead><tbody>"
        for domain_key, domain_data in groups.items():
            display_name = domain_key.replace("_", " ").title()
            n = domain_data.get("n_samples", 0)
            domain_html += f"<tr><td>{display_name}</td><td>{n}</td>"
            if cfg:
                for mk in get_metric_keys(task):
                    val = domain_data.get(mk)
                    val_str = f"{val:.4f}" if val is not None else "N/A"
                    domain_html += f"<td>{val_str}</td>"
            domain_html += "</tr>"
        domain_html += "</tbody></table></div>"

    samples = data.get("total_samples", 0)
    ts = data.get("timestamp", "")[:19]
    footer = f"""
        <div class="preview-footer">
            <span>📝 {samples} samples</span>
            <span>🕐 {ts}</span>
        </div>
    </div>
    """

    return header + avg_html + domain_html + footer


def submit_result(
    json_file,
    model_type: str,
    organization: str,
    hf_model_id: str,
    base_architecture: str,
    model_size_b: str,
    profile: Optional[gr.OAuthProfile] = None,
) -> str:
    if profile is None:
        return styled_error("🔒 HuggingFace login required / Connexion HuggingFace requise")

    if json_file is None:
        return styled_error("Please upload a JSON result file / Veuillez uploader un fichier JSON")

    filepath = json_file if isinstance(json_file, str) else json_file.name
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return styled_error(f"Invalid JSON file: {e}")

    if isinstance(data, list):
        if len(data) == 1:
            data = data[0]
        else:
            return styled_error("Please submit one result at a time / Soumettez un résultat à la fois")

    valid, errors = validate_goai_json(data)
    if not valid:
        return styled_error("Validation errors:<br>" + "<br>".join(f"• {e}" for e in errors))

    fp = _result_fingerprint(data)
    if fp in _existing_fingerprints():
        return styled_error(
            "⚠️ Duplicate submission detected — these exact results have already been submitted.<br>"
            "Soumission en doublon détectée — ces résultats identiques ont déjà été soumis."
        )

    data["model_type"] = model_type or "Open Source"
    data["organization"] = organization or "Anonymous"
    data["hf_model_id"] = hf_model_id or data["model_id"]
    data["base_architecture"] = base_architecture or "Other"
    try:
        size_val = float(model_size_b) if model_size_b else 0.0
    except ValueError:
        size_val = 0.0
    data["model_size_b"] = size_val
    data["model_size_category"] = size_category_from_b(size_val)
    data["submitter"] = profile.username
    data["submitted_time"] = datetime.now(timezone.utc).isoformat()

    model_slug = data["model_id"].replace("/", "_")
    task = data["task"]
    lang = data["benchmark_language"]
    mt_pair = data.get("mt_pair", "")
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{task}_{lang}_{model_slug}_{mt_pair}_{ts}.json"

    out_dir = os.path.join(EVAL_RESULTS_PATH, profile.username)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    try:
        API.upload_file(
            path_or_fileobj=out_path,
            path_in_repo=f"{RESULTS_DIR}/{profile.username}/{filename}",
            repo_id=DATA_REPO,
            repo_type="dataset",
            commit_message=f"Add {data['model_id']} {task} {lang} results",
        )
    except Exception as e:
        return styled_warning(
            f"Result saved locally but upload failed: {e}<br>"
            "Résultat sauvegardé localement mais l'upload a échoué."
        )

    return styled_message(
        f"✅ Result submitted successfully! / Résultat soumis avec succès !<br>"
        f"Model: {data['model_id']} | Task: {task.upper()} | Language: {lang}<br><br>"
        f"⏳ The leaderboard will be automatically updated within {REFRESH_INTERVAL_MIN} minutes.<br>"
        f"Le classement sera automatiquement mis à jour dans {REFRESH_INTERVAL_MIN} minutes."
    )
