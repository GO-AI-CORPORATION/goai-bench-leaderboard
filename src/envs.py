import os

from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

TOKEN = os.environ.get("TOKEN")

OWNER = "goaicorp"
REPO_ID = f"{OWNER}/goai-bench-leaderboard"
QUEUE_REPO = f"{OWNER}/goai-bench-requests"
RESULTS_REPO = f"{OWNER}/goai-bench-results"

CACHE_PATH = os.getenv("HF_HOME", ".")
EVAL_REQUESTS_PATH = os.path.join(CACHE_PATH, "eval-queue")
EVAL_RESULTS_PATH = os.path.join(CACHE_PATH, "eval-results")

SEED_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "results_final.json")

API = HfApi(token=TOKEN)
