from typing import Dict, List, Any

def compare(baseline: Dict[str, Any], current: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Compare baseline vs current configuration and detect drift.
    Returns a list of findings with resource, attribute, expected, actual, and status.
    """

    findings: List[Dict[str, Any]] = []

    # Check for mismatches and missing resources
    for key, expected in baseline.items():
        actual = current.get(key)

        if actual is None:
            findings.append({
                "resource": key,
                "expected": expected,
                "actual": None,
                "status": "missing"
            })
        elif actual != expected:
            findings.append({
                "resource": key,
                "expected": expected,
                "actual": actual,
                "status": "mismatch"
            })
        else:
            findings.append({
                "resource": key,
                "expected": expected,
                "actual": actual,
                "status": "compliant"
            })

    # Detect unexpected resources present in current config
    for key, actual in current.items():
        if key not in baseline:
            findings.append({
                "resource": key,
                "expected": None,
                "actual": actual,
                "status": "unexpected"
            })

    return findings

