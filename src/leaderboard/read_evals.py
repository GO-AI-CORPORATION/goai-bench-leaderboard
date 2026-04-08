import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from src.display.formatting import make_clickable_model
from src.tasks import (
    TASK_CONFIGS,
    Domain,
    get_metric_keys,
    is_lower_better,
    size_category_from_b,
)


@dataclass
class BenchResult:
    """One benchmark result entry from GO AI Bench JSON output."""

    model_id: str
    task: str
    benchmark_language: str
    total_samples: int
    groups: Dict[str, Dict[str, Any]]
    groups_evaluated: List[str]
    average: Dict[str, Any]
    timestamp: str
    mt_pair: Optional[str] = None
    # Submission metadata
    model_type: str = "Open Source"
    organization: str = "Unknown"
    hf_model_id: str = ""
    base_architecture: str = "Other"
    model_size_b: float = 0.0
    model_size_category: str = "<0.5B"
    submitter: str = ""

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "BenchResult":
        size_b = d.get("model_size_b", 0.0) or 0.0
        return cls(
            model_id=d["model_id"],
            task=d["task"],
            benchmark_language=d["benchmark_language"],
            total_samples=d.get("total_samples", 0),
            groups=d.get("groups", {}),
            groups_evaluated=d.get("groups_evaluated", []),
            average=d.get("average", {}),
            timestamp=d.get("timestamp", ""),
            mt_pair=d.get("mt_pair"),
            model_type=d.get("model_type", "Open Source"),
            organization=d.get("organization", "Unknown"),
            hf_model_id=d.get("hf_model_id", d["model_id"]),
            base_architecture=d.get("base_architecture", "Other"),
            model_size_b=size_b,
            model_size_category=d.get("model_size_category", size_category_from_b(size_b)),
            submitter=d.get("submitter", ""),
        )

    def dedup_key(self) -> str:
        return f"{self.model_id}|{self.task}|{self.benchmark_language}|{self.mt_pair or ''}"

    def get_metrics(self, domain: str = "average") -> Dict[str, Any]:
        if domain == "average":
            return self.average
        return self.groups.get(domain, self.average)

    def primary_score(self) -> float:
        cfg = TASK_CONFIGS.get(self.task)
        if not cfg:
            return 0.0
        val = self.average.get(cfg.primary_metric)
        if val is None:
            return 0.0
        return float(val)


def load_seed_data(seed_path: str) -> List[BenchResult]:
    if not os.path.exists(seed_path):
        return []
    with open(seed_path, encoding="utf-8") as f:
        data = json.load(f)
    return [BenchResult.from_dict(entry) for entry in data]


def load_hf_results(results_path: str) -> List[BenchResult]:
    results = []
    if not os.path.exists(results_path):
        return results
    for root, _, files in os.walk(results_path):
        for fname in files:
            if not fname.endswith(".json"):
                continue
            filepath = os.path.join(root, fname)
            try:
                with open(filepath, encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    for entry in data:
                        if "model_id" in entry and "task" in entry:
                            results.append(BenchResult.from_dict(entry))
                elif isinstance(data, dict) and "model_id" in data and "task" in data:
                    results.append(BenchResult.from_dict(data))
            except (json.JSONDecodeError, KeyError):
                continue
    return results


def load_all_results(seed_path: str, results_path: str) -> List[BenchResult]:
    seed = load_seed_data(seed_path)
    hf = load_hf_results(results_path)

    seen = {}
    for r in seed + hf:
        key = r.dedup_key()
        if key in seen:
            existing = seen[key]
            if r.timestamp > existing.timestamp:
                seen[key] = r
        else:
            seen[key] = r

    return list(seen.values())


def filter_results(
    results: List[BenchResult],
    task: str,
    language: str,
    mt_pair: Optional[str] = None,
) -> List[BenchResult]:
    filtered = [r for r in results if r.task == task and r.benchmark_language == language]
    if mt_pair is not None:
        filtered = [r for r in filtered if r.mt_pair == mt_pair]
    return filtered
