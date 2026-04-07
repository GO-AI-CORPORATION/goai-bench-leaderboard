"""One-time script to enrich results_final.json with submission metadata."""
import json, sys, os

MODEL_META = {
    "goaicorp/mos-whisper-large-v3-turbo": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Whisper", "model_size_b": 0.809},
    "goaicorp/mos-whisper-small": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Whisper", "model_size_b": 0.244},
    "goaicorp/mos-wav2vec2-large-mms-1b": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Wav2Vec2", "model_size_b": 0.965},
    "facebook/mms-1b-all": {"organization": "Meta", "model_type": "Open Source", "base_architecture": "MMS", "model_size_b": 0.965},
    "openai/whisper-base": {"organization": "OpenAI", "model_type": "Open Source", "base_architecture": "Whisper", "model_size_b": 0.074},
    "openai/whisper-large-v3-turbo": {"organization": "OpenAI", "model_type": "Open Source", "base_architecture": "Whisper", "model_size_b": 0.809},
    "openai/whisper-small": {"organization": "OpenAI", "model_type": "Open Source", "base_architecture": "Whisper", "model_size_b": 0.244},
    "goaicorp/Spark-TTS-mos": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "SparkTTS", "model_size_b": 0.5},
    "goaicorp/mos-mms-tts-v2": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "MMS-TTS", "model_size_b": 0.3},
    "facebook/nllb-200-distilled-600M": {"organization": "Meta", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 0.6},
    "facebook/nllb-200-3.3B": {"organization": "Meta", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 3.3},
    "facebook/nllb-200-1.3B": {"organization": "Meta", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 1.3},
    "goaicorp/mos-nllb-3.3B-fr2mos": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 3.3},
    "goaicorp/mos-nllb-600M-fr2mos": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 0.6},
    "goaicorp/mos-nllb-600M-mos2fr": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 0.6},
    "goaicorp/mos-nllb-3.3B-mos2fr": {"organization": "GO AI Corp", "model_type": "Open Source", "base_architecture": "Seq2Seq (NLLB)", "model_size_b": 3.3},
}

SIZE_CATEGORIES = [
    (0.5, "<0.5B"),
    (1.0, "0.5B-1B"),
    (2.0, "1B-2B"),
    (4.0, "2B-4B"),
    (float("inf"), ">4B"),
]

def size_category(b):
    for threshold, label in SIZE_CATEGORIES:
        if b < threshold:
            return label
    return ">4B"

src = os.path.join(os.path.dirname(__file__), "..", "..", "goai-bench", "benchmarking-report", "results_final.json")
dst = os.path.join(os.path.dirname(__file__), "..", "data", "results_final.json")

with open(src, encoding="utf-8") as f:
    data = json.load(f)

for entry in data:
    mid = entry["model_id"]
    meta = MODEL_META.get(mid, {})
    entry["organization"] = meta.get("organization", "Unknown")
    entry["model_type"] = meta.get("model_type", "Open Source")
    entry["base_architecture"] = meta.get("base_architecture", "Other")
    sz = meta.get("model_size_b", 0)
    entry["model_size_b"] = sz
    entry["model_size_category"] = size_category(sz)
    entry["hf_model_id"] = mid
    entry["submitter"] = "goaicorp"

os.makedirs(os.path.dirname(dst), exist_ok=True)
with open(dst, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Enriched {len(data)} entries -> {dst}")
