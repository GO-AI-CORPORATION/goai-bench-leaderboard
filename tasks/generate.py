import csv
import json
import os

import pandas as pd
import yaml


def process_notion_data():
    if os.path.exists("tasks/notion.csv"):
        df = pd.read_csv("tasks/notion.csv")

        df.rename(columns={"Created by": "Donated By"}, inplace=True)
        df.rename(columns={"Pretty name": "Name"}, inplace=True)
        df.rename(columns={"Task": "Task type"}, inplace=True)

        df["Task"] = df.apply(lambda row: f"[{row['Name']}]({row['Corpus URL']})", axis=1)
        df = df.drop(columns=["Corpus URL", "Corpus"])
        df.insert(0, "Task", df.pop("Task"))

        df["Paper"] = df.apply(lambda row: f"[📄]({row['Paper']})", axis=1)

        df["Domain"] = "Miscellaneous"  # TODO: Remove this line and update enums Domain and Categories

        df.fillna("N/A", inplace=True)

        df.to_csv("tasks/tasks.csv", index=False)

        print("Notion data processed successfully.")
    else:
        print("Notion data not found.")


def generate_dummy_results():
    """
    Generate the necessary files whenever the leaderboard tasks are updated. This includes creating a dummy results JSON file for the results repository, a list of harness tasks for the backend Space, and a YAML file for the harness leaderboard group.
    """
    tasks = []
    with open("tasks/tasks.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append(row)

    dummy_results = {}
    harness_tasks = []
    for task in tasks:
        harness = task["Harness"]
        metric = task["Metric"]
        if harness and metric:
            dummy_results[harness] = (
                {f"{metric},none": 0.0} if metric != "exact_match" else {f"{metric},remove_whitespace": 0.0}
            )
            harness_tasks.append(harness)

    with open("tasks/backend.json", "w", encoding="utf-8") as jsonfile:
        json.dump(harness_tasks, jsonfile, ensure_ascii=False, indent=4)

    results_json = {
        "config": {
            "model_dtype": "torch.float16",
            "model_name": "demo-leaderboard/gpt2-demo",
            "model_sha": "ac3299b02780836378b9e1e68c6eead546e89f90",
        },
        "results": dummy_results,
    }
    with open("tasks/dummy_results.json", "w", encoding="utf-8") as jsonfile:
        json.dump(results_json, jsonfile, ensure_ascii=False, indent=4)

    harness_yaml = {
        "group": "laleaderboard",
        "group_alias": "laleaderboard",
        "task": harness_tasks,
        "aggregate_metric_list": [
            {
                "metric": "acc",
                "aggregation": "mean",
                "weight_by_size": True,
            }
        ],
        "metadata": {"version": 1.0},
    }

    with open("tasks/harness.yaml", "w", encoding="utf-8") as yamlfile:
        yaml.dump(harness_yaml, yamlfile, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print("JSON and YAML files created successfully.")


if __name__ == "__main__":
    process_notion_data()
    generate_dummy_results()
