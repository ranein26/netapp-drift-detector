import yaml
import json
import csv
from pathlib import Path
from typing import Any, Dict, List

def load_yaml(path: Path) -> Dict[str, Any]:
    """Load a YAML file into a Python dict."""
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file into a Python dict."""
    with open(path, "r") as f:
        return json.load(f)

def load_csv(path: Path) -> List[Dict[str, Any]]:
    """Load a CSV file into a list of dicts."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def normalize(data: dict) -> dict:
    """
    Normalize resource keys, booleans, list ordering, and null values.
    Handles lists of scalars and lists of dicts safely.
    """
    normalized = {}
    for k, v in data.items():
        key = k.lower()

        if isinstance(v, list):
            if all(isinstance(item, dict) for item in v):
                v = sorted(v, key=lambda x: str(x))
            else:
                v = sorted(v)

        if isinstance(v, bool):
            v = str(v).lower()

        if v is None:
            v = "null"

        normalized[key] = v
    return normalized

