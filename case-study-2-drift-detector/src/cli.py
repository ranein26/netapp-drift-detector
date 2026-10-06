import argparse
from pathlib import Path

from parser import load_yaml, load_json, load_csv, normalize
from comparator import compare
from correlator import correlate
from reporter import write_json, write_csv, write_html

def main():
    parser = argparse.ArgumentParser(description="NetApp Drift Detector CLI")
    parser.add_argument("--baseline", required=True, help="Path to approved_baseline.yaml")
    parser.add_argument("--current", required=True, help="Path to current_config.json")
    parser.add_argument("--changes", required=True, help="Path to approved_changes.csv")
    parser.add_argument("--exceptions", required=True, help="Path to exceptions.yaml")
    parser.add_argument("--standards", required=True, help="Path to standards.yaml")
    parser.add_argument("--output", default="reports", help="Output directory for findings")

    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load and normalize inputs
    baseline = normalize(load_yaml(Path(args.baseline)))
    current = normalize(load_json(Path(args.current)))
    changes = load_csv(Path(args.changes))
    exceptions = load_yaml(Path(args.exceptions))
    standards = load_yaml(Path(args.standards))

    # Compare baseline vs current
    findings = compare(baseline, current)

    # Correlate with changes and exceptions
    correlated = correlate(findings, changes, exceptions)

    # Report outputs
    write_json(correlated, output_dir)
    write_csv(correlated, output_dir)
    write_html(correlated, output_dir)

    # Exit code based on standards.yaml
    exit_code = standards.get("exit_codes", {}).get("default", 1)
    exit(exit_code)

if __name__ == "__main__":
    main()

