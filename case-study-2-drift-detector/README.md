# Case Study 2: Drift Detector

## Overview
The Drift Detector is a Python-based tool designed to identify configuration drift in NetApp environments.  
It compares current system configurations against a defined baseline and highlights mismatches, missing parameters, or version inconsistencies.

## Repository Structure
├── README.md                # Documentation and usage guide
├── requirements.txt         # Python dependencies
├── src/                     # Source code
│    ├── parser.py           # Reads and normalizes configuration files
│    ├── comparator.py       # Compares current vs baseline configs
│    ├── rules.py            # Defines drift detection rules
│    └── init.py
├── tests/                   # Unit tests
│    ├── test_parser.py
│    ├── test_comparator.py
│    ├── test_rules.py
├── findings/                # Example outputs
│    ├── findings.json
│    ├── findings.csv
│    └── report.html
├── Dockerfile               # Containerized execution
└── .github/workflows/ci.yml # Optional CI/CD pipeline


## Features
- **Parser**: Ingests JSON/YAML configuration files.  
- **Comparator**: Detects drift between baseline and current state.  
- **Rules Engine**: Applies custom drift rules (e.g., version mismatch, missing parameters).  
- **Outputs**: Generates findings in JSON, CSV, and HTML formats.  
- **Tests**: Includes unit tests for parser, comparator, and rules.  
- **Containerization**: Dockerfile for portable execution.  
- **CI/CD**: GitHub Actions workflow for automated testing.

## Usage
1. Install dependencies:
   ```bash
## Usage
pip install -r requirements.txt
python src/comparator.py --baseline baseline.json --current current.json --output findings/findings.json
