from typing import Any, Dict, List, Tuple

from src.tasks import TASK_CONFIGS, Language, get_metric_keys

REQUIRED_FIELDS = ["model_id", "task", "benchmark_language", "groups", "average"]
VALID_TASKS = set(TASK_CONFIGS.keys())
VALID_LANGUAGES = {lang.value.code for lang in Language}


def validate_goai_json(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errors = []

    for f in REQUIRED_FIELDS:
        if f not in data:
            errors.append(f"Missing required field: '{f}'")

    if errors:
        return False, errors

    task = data.get("task", "")
    if task not in VALID_TASKS:
        errors.append(f"Invalid task '{task}'. Must be one of: {', '.join(sorted(VALID_TASKS))}")

    lang = data.get("benchmark_language", "")
    if lang not in VALID_LANGUAGES:
        errors.append(f"Invalid language '{lang}'. Must be one of: {', '.join(sorted(VALID_LANGUAGES))}")

    if task == "mt" and not data.get("mt_pair"):
        errors.append("MT results must include 'mt_pair' (e.g. 'fra_Latn_mos_Latn')")

    avg = data.get("average", {})
    if not isinstance(avg, dict) or not avg:
        errors.append("'average' must be a non-empty dict of metrics")

    groups = data.get("groups", {})
    if not isinstance(groups, dict) or not groups:
        errors.append("'groups' must be a non-empty dict of domain results")

    if task in VALID_TASKS and not errors:
        expected_metrics = get_metric_keys(task)
        missing = [m for m in expected_metrics if m not in avg]
        comet_filtered = [m for m in missing if m != "comet_kiwi"]
        if comet_filtered:
            errors.append(f"Average missing metrics for task '{task}': {', '.join(comet_filtered)}")

    return len(errors) == 0, errors
