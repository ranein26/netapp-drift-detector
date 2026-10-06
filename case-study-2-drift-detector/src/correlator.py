from datetime import datetime
from typing import List, Dict

def correlate(findings: List[Dict], changes: List[Dict], exceptions: Dict) -> List[Dict]:
    correlated = []
    now = datetime.utcnow()

    for f in findings:
        disposition = "unauthorised_drift"

        # Check approved changes
        for ch in changes:
            if ch["resource"] == f["resource"]:
                start = datetime.fromisoformat(ch["window_start"].replace("Z",""))
                end = datetime.fromisoformat(ch["window_end"].replace("Z",""))
                if start <= now <= end and ch["status"].lower() == "implementing":
                    disposition = "authorised_change"

        # Check exceptions
        for exc in exceptions.get("exceptions", []):
            if exc["resource"] == f["resource"]:
                exp = datetime.fromisoformat(exc["expires"])
                if now <= exp:
                    disposition = "active_exception"
                else:
                    disposition = "expired_exception"

        f["disposition"] = disposition
        correlated.append(f)

    return correlated

