import os

from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

TOKEN = os.environ.get("HF_TOKEN") or os.environ.get("TOKEN")

OWNER = "goaicorp"
REPO_ID = f"{OWNER}/goai-bench-leaderboard"
# One dataset holds both folders: requests/ and results/
DATA_REPO = f"{OWNER}/goai-bench-submissions"
REQUESTS_DIR = "requests"
RESULTS_DIR = "results"

CACHE_PATH = os.getenv("HF_HOME", ".")
DATA_PATH = os.path.join(CACHE_PATH, "goai-bench-submissions")
EVAL_REQUESTS_PATH = os.path.join(DATA_PATH, REQUESTS_DIR)
EVAL_RESULTS_PATH = os.path.join(DATA_PATH, RESULTS_DIR)

SEED_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "results_final.json")

API = HfApi(token=TOKEN)
