from typing import List, Optional

import pandas as pd

from src.display.formatting import make_clickable_model, rank_label
from src.leaderboard.read_evals import BenchResult, filter_results
from src.tasks import TASK_CONFIGS, get_metric_keys, is_lower_better


def build_leaderboard_df(
    results: List[BenchResult],
    task: str,
    language: str,
    mt_pair: Optional[str] = None,
    domain: str = "average",
) -> pd.DataFrame:
    filtered = filter_results(results, task, language, mt_pair)
    if not filtered:
        return pd.DataFrame()

    cfg = TASK_CONFIGS[task]
    metrics = get_metric_keys(task)
    ascending = is_lower_better(task)

    rows = []
    for r in filtered:
        m = r.get_metrics(domain)
        row = {
            "model_id_raw": r.model_id,
            "model_id": make_clickable_model(r.hf_model_id or r.model_id),
            "organization": r.organization,
            "model_type": r.model_type,
            "base_architecture": r.base_architecture,
            "model_size_category": r.model_size_category,
            "model_size_b": r.model_size_b,
            "total_samples": r.total_samples,
            "timestamp": r.timestamp[:10] if r.timestamp else "",
        }
        for mk in metrics:
            val = m.get(mk)
            if val is not None:
                row[f"avg_{mk}"] = round(float(val), 4)
            else:
                row[f"avg_{mk}"] = None
        rows.append(row)

    df = pd.DataFrame(rows)

    primary_col = f"avg_{cfg.primary_metric}"
    if primary_col in df.columns:
        df = df.sort_values(by=primary_col, ascending=ascending, na_position="last")
        df = df.reset_index(drop=True)
        df["rank"] = [rank_label(i + 1) for i in range(len(df))]
    else:
        df["rank"] = range(1, len(df) + 1)

    return df


def get_unique_values(results: List[BenchResult], field: str) -> List[str]:
    vals = sorted({getattr(r, field, "") for r in results if getattr(r, field, "")})
    return vals
