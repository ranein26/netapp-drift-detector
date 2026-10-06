import yaml
import json
import csv
from pathlib import Path
from typing import Any, Dict, List

def load_yaml(path: Path) -> Dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r") as f:
        return json.load(f)

def load_csv(path: Path) -> List[Dict[str, Any]]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def normalize(data: dict) -> dict:
    """
    Normalize resource keys, booleans, list ordering, and null values.
    """
    normalized = {}
    for k, v in data.items():
        key = k.lower()  # lowercase keys
        if isinstance(v, list):
            v = sorted(v)  # sort lists
        if isinstance(v, bool):
            v = str(v).lower()  # normalize booleans
        if v is None:
            v = "null"  # replace nulls
        normalized[key] = v
    return normalized

