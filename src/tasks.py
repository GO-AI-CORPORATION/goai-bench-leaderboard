from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Tuple


@dataclass
class LanguageInfo:
    code: str
    display_name: str
    native_name: str
    iso_639_3: str
    region: str
    description_en: str
    description_fr: str


class Language(Enum):
    mos_Latn = LanguageInfo(
        code="mos_Latn",
        display_name="Mooré",
        native_name="Mòoré",
        iso_639_3="mos",
        region="Burkina Faso, Ghana, Togo",
        description_en="Dominant language of Burkina Faso with ~8M speakers. Gur (Oti-Volta) family.",
        description_fr="Langue dominante du Burkina Faso avec ~8M de locuteurs. Famille Gur (Oti-Volta).",
    )
    dyu_Latn = LanguageInfo(
        code="dyu_Latn",
        display_name="Dioula",
        native_name="Julakan",
        iso_639_3="dyu",
        region="Burkina Faso, Côte d'Ivoire, Mali",
        description_en="Major lingua franca of West Africa (~12M speakers). Mande family.",
        description_fr="Langue véhiculaire majeure d'Afrique de l'Ouest (~12M de locuteurs). Famille Mandé.",
    )


@dataclass
class DomainInfo:
    key: str
    display_name: str
    display_name_fr: str
    description_en: str
    description_fr: str


class Domain(Enum):
    general = DomainInfo("general", "General", "Général", "Cross-domain baseline from FLORES-200", "Base inter-domaine de FLORES-200")
    health = DomainInfo("health", "Health", "Santé", "Maternal/child health, vaccination, nutrition", "Santé maternelle/infantile, vaccination, nutrition")
    education = DomainInfo("education", "Education", "Éducation", "School enrollment, literacy, learning materials", "Scolarisation, alphabétisation, matériels d'apprentissage")
    child_protection = DomainInfo("child_protection", "Child Protection", "Protection de l'enfance", "Birth registration, child labor, child marriage", "Enregistrement des naissances, travail des enfants")
    environment = DomainInfo("environment", "Environment", "Environnement", "Climate change, water, sanitation", "Changement climatique, eau, assainissement")


DOMAIN_KEYS = [d.value.key for d in Domain]
DOMAIN_DISPLAY_NAMES = {d.value.key: d.value.display_name for d in Domain}


@dataclass
class BenchTask:
    task_id: str
    display_name: str
    display_name_fr: str
    primary_metric: str
    primary_metric_display: str
    secondary_metrics: List[str]
    metric_display_names: Dict[str, str]
    direction: str  # "higher" or "lower"
    architectures: List[str]
    description_en: str
    description_fr: str


TASK_CONFIGS: Dict[str, BenchTask] = {
    "asr": BenchTask(
        task_id="asr",
        display_name="ASR",
        display_name_fr="RAP",
        primary_metric="wer",
        primary_metric_display="WER",
        secondary_metrics=["cer", "mer"],
        metric_display_names={"wer": "WER ↓", "cer": "CER ↓", "mer": "MER ↓"},
        direction="lower",
        architectures=["Whisper", "Wav2Vec2", "MMS", "Other"],
        description_en="Automatic Speech Recognition — evaluate speech-to-text accuracy.",
        description_fr="Reconnaissance automatique de la parole — évaluer la transcription.",
    ),
    "mt": BenchTask(
        task_id="mt",
        display_name="MT",
        display_name_fr="TA",
        primary_metric="chrf",
        primary_metric_display="chrF++",
        secondary_metrics=["bleu", "ter", "comet_kiwi"],
        metric_display_names={"chrf": "chrF++ ↑", "bleu": "BLEU ↑", "ter": "TER ↓", "comet_kiwi": "COMET-Kiwi ↑"},
        direction="higher",
        architectures=["Seq2Seq (NLLB)", "Decoder-Only", "Other"],
        description_en="Machine Translation — evaluate translation quality between French and local languages.",
        description_fr="Traduction automatique — évaluer la qualité de traduction entre le français et les langues locales.",
    ),
    "tts": BenchTask(
        task_id="tts",
        display_name="TTS",
        display_name_fr="STT",
        primary_metric="utmos",
        primary_metric_display="UTMOS",
        secondary_metrics=["loopback_wer", "loopback_cer"],
        metric_display_names={"utmos": "UTMOS ↑", "loopback_wer": "Loopback WER ↓", "loopback_cer": "Loopback CER ↓"},
        direction="higher",
        architectures=["SparkTTS", "MMS-TTS", "VITS", "xTTSv2", "Other"],
        description_en="Text-to-Speech — evaluate naturalness (UTMOS) and intelligibility (loopback ASR).",
        description_fr="Synthèse vocale — évaluer le naturel (UTMOS) et l'intelligibilité (ASR en boucle).",
    ),
}

ALL_TASK_IDS = list(TASK_CONFIGS.keys())

MODEL_SIZE_CATEGORIES = ["<0.5B", "0.5B-1B", "1B-2B", "2B-4B", ">4B"]

MODEL_TYPES = ["Open Source", "Proprietary"]


def get_metric_keys(task_id: str) -> List[str]:
    cfg = TASK_CONFIGS[task_id]
    return [cfg.primary_metric] + cfg.secondary_metrics


def get_all_metrics(task_id: str) -> List[Tuple[str, str]]:
    cfg = TASK_CONFIGS[task_id]
    return [(m, cfg.metric_display_names.get(m, m)) for m in get_metric_keys(task_id)]


def is_lower_better(task_id: str) -> bool:
    return TASK_CONFIGS[task_id].direction == "lower"


def size_category_from_b(size_b: float) -> str:
    if size_b <= 0:
        return "<0.5B"
    if size_b < 0.5:
        return "<0.5B"
    if size_b < 1.0:
        return "0.5B-1B"
    if size_b < 2.0:
        return "1B-2B"
    if size_b < 4.0:
        return "2B-4B"
    return ">4B"
