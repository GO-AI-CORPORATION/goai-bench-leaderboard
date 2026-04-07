from src.tasks import TASK_CONFIGS, get_metric_keys


def get_leaderboard_columns(task_id: str, domain: str = "average"):
    """Return ordered list of (col_key, display_name, col_type) for a task leaderboard."""
    cols = [
        ("rank", "Rank", "str"),
        ("model_id", "Model", "markdown"),
        ("organization", "Organization", "str"),
        ("model_type", "Type", "str"),
        ("base_architecture", "Architecture", "str"),
        ("model_size_category", "Size", "str"),
    ]

    cfg = TASK_CONFIGS[task_id]
    metrics = get_metric_keys(task_id)
    for m in metrics:
        display = cfg.metric_display_names.get(m, m)
        col_key = f"avg_{m}" if domain == "average" else f"domain_{m}"
        cols.append((col_key, display, "number"))

    cols.append(("total_samples", "Samples", "number"))
    cols.append(("timestamp", "Date", "str"))

    return cols


def get_default_visible_columns(task_id: str):
    """Columns visible by default (without architecture/size/date)."""
    return ["rank", "model_id", "organization", "model_type"] + [
        f"avg_{m}" for m in get_metric_keys(task_id)
    ]
