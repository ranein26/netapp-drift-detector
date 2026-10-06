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

