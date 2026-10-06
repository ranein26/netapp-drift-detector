import json, csv
from pathlib import Path
from jinja2 import Template
from typing import List, Dict

def write_json(findings: List[Dict], path: Path):
    with open(path / "findings.json", "w") as f:
        json.dump(findings, f, indent=2)

def write_csv(findings: List[Dict], path: Path):
    with open(path / "findings.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=findings[0].keys())
        writer.writeheader()
        writer.writerows(findings)

def write_html(findings: List[Dict], path: Path):
    template = Template("""
    <html><body>
    <h2>Drift Detector Summary</h2>
    <p>Total Findings: {{ findings|length }}</p>
    <table border="1">
      <tr>
        {% for key in findings[0].keys() %}
          <th>{{ key }}</th>
        {% endfor %}
      </tr>
      {% for f in findings %}
      <tr>
        {% for v in f.values() %}
          <td>{{ v }}</td>
        {% endfor %}
      </tr>
      {% endfor %}
    </table>
    </body></html>
    """)
    html = template.render(findings=findings)
    with open(path / "report.html", "w") as f:
        f.write(html)

