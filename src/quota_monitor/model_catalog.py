import json
import re
from pathlib import Path

DATE_SUFFIX = re.compile(r"-20\d{2}-\d{2}-\d{2}$")


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_catalog(path: Path | None = None) -> dict:
    catalog_path = path or project_root() / "data" / "models.json"
    return json.loads(catalog_path.read_text(encoding="utf-8"))


def clean_model_name(name: str) -> str:
    return DATE_SUFFIX.sub("", name or "unknown")


def build_index(catalog: dict) -> dict:
    index = {}
    for group_id, group in catalog["groups"].items():
        for model in group["models"]:
            entry = {**model, "group": group_id}
            index[model["id"]] = entry
            for alias in model.get("aliases", []):
                index[alias] = entry
    return index


def find_model(name: str, catalog: dict) -> dict | None:
    index = build_index(catalog)
    return index.get(name) or index.get(clean_model_name(name))
