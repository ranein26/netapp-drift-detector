import json, csv
from pathlib import Path
from jinja2 import Template
from typing import List, Dict

def write_json(findings: List[Dict], path: Path):
    """Write findings to JSON file."""
    with open(path / "findings.json", "w") as f:
        json.dump(findings, f, indent=2)

def write_csv(findings: List[Dict], path: Path):
    """Write findings to CSV file."""
    fieldnames = ["severity", "resource", "attribute", "expected", "actual", "disposition", "evidence", "recommended_action"]
    with open(path / "findings.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for fnd in findings:
            writer.writerow({fn: fnd.get(fn, "") for fn in fieldnames})

def write_html(findings: List[Dict], path: Path):
    """Write findings to HTML report."""
    template = Template("""
    <html><body>
    <h2>Drift Detector Report</h2>
    <p>Total Findings: {{ findings|length }}</p>
    <table border="1">
      <tr>
        {% for key in ["severity","resource","attribute","expected","actual","disposition","evidence","recommended_action"] %}
          <th>{{ key }}</th>
        {% endfor %}
      </tr>
      {% for f in findings %}
      <tr>
        <td>{{ f.get("severity","") }}</td>
        <td>{{ f.get("resource","") }}</td>
        <td>{{ f.get("attribute","") }}</td>
        <td>{{ f.get("expected","") }}</td>
        <td>{{ f.get("actual","") }}</td>
        <td>{{ f.get("disposition","") }}</td>
        <td>{{ f.get("evidence","") }}</td>
        <td>{{ f.get("recommended_action","") }}</td>
      </tr>
      {% endfor %}
    </table>
    </body></html>
    """)
    html = template.render(findings=findings)
    with open(path / "report.html", "w") as f:
        f.write(html)

def determine_exit_code(findings: List[Dict], standards: Dict) -> int:
    """
    Determine exit code based on standards.yaml severity mapping.
    Example standards.yaml:
    exit_codes:
      compliant: 0
      mismatch: 1
      unauthorised_drift: 2
      data_quality_issue: 3
    """
    exit_codes = standards.get("exit_codes", {})
    highest_code = 0
    for f in findings:
        sev = f.get("severity") or f.get("status") or "default"
        code = exit_codes.get(sev, exit_codes.get("default", 1))
        highest_code = max(highest_code, code)
    return highest_code

