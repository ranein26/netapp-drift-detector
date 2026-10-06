from datetime import datetime
from typing import List, Dict

def correlate(findings: List[Dict], changes: List[Dict], exceptions: Dict) -> List[Dict]:
    """
    Correlate drift findings with approved changes and exceptions.
    Classify each difference as compliant, authorised change, active exception,
    expired exception, unmanaged object, unauthorised drift, or data-quality issue.
    """

    correlated: List[Dict] = []
    now = datetime.utcnow()

    for f in findings:
        disposition = f.get("status", "unauthorised_drift")

        # Check approved changes
        for ch in changes:
            if ch.get("resource") == f["resource"]:
                try:
                    start = datetime.fromisoformat(ch["window_start"].replace("Z", ""))
                    end = datetime.fromisoformat(ch["window_end"].replace("Z", ""))
                    if start <= now <= end and ch.get("status", "").lower() == "implementing":
                        disposition = "authorised_change"
                except Exception:
                    disposition = "data_quality_issue"

        # Check exceptions
        for exc in exceptions.get("exceptions", []):
            if exc.get("resource") == f["resource"]:
                try:
                    exp = datetime.fromisoformat(exc["expires"].replace("Z", ""))
                    if now <= exp:
                        disposition = "active_exception"
                    else:
                        disposition = "expired_exception"
                except Exception:
                    disposition = "data_quality_issue"

        # If resource not in baseline or unmanaged
        if f.get("status") == "unexpected":
            disposition = "unmanaged_object"

        f["disposition"] = disposition
        correlated.append(f)

    return correlated

