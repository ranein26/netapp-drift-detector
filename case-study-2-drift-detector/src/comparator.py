from typing import Dict, List

def compare(baseline: Dict, current: Dict) -> List[Dict]:
    findings = []
    for key, expected in baseline.items():
        actual = current.get(key)
        if actual != expected:
            findings.append({
                "resource": key,
                "expected": expected,
                "actual": actual,
                "status": "mismatch"
            })
    # Detect unexpected keys
    for key in current.keys():
        if key not in baseline:
            findings.append({
                "resource": key,
                "expected": None,
                "actual": current[key],
                "status": "unexpected"
            })
    return findings

