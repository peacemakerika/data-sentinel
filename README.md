# Data Sentinel

> An intelligent data integrity engine for modern data pipelines.

---

## Overview

Data Sentinel is an open-source data integrity engine designed to validate, monitor, and improve the quality of data flowing through modern data pipelines.

It helps detect schema mismatches, data type errors, duplicate records, and other integrity issues before they propagate to databases, dashboards, machine learning models, or downstream applications.

The long-term vision of Data Sentinel is to evolve from a rule-based validation tool into an intelligent system capable of learning normal data behavior, detecting anomalies, identifying root causes, and helping engineers build trustworthy data infrastructure.

---

## Why Data Sentinel?

Modern software systems depend on data.

Every day, millions of records flow through APIs, ETL pipelines, event streams, and databases. While these systems rarely fail completely, they often suffer from silent data corruption.

A pipeline may continue running while producing duplicate records, missing fields, incorrect data types, unexpected values, or inconsistent datasets. These issues often remain unnoticed until they affect dashboards, business decisions, or machine learning models.

Data Sentinel aims to detect these problems as early as possible, allowing engineers to trust their data before it reaches downstream systems.

---

## Current Features

- JSON data loading
- Schema validation
- Data type validation
- Duplicate record detection
- Modular validation architecture

---

## Planned Features

- Statistical anomaly detection
- Configurable validation rules
- Historical data profiling
- Automatic schema inference
- Root cause analysis
- Streaming pipeline support
- Machine learning-based anomaly detection
- HTML and PDF reporting
- Database connectors
- REST API

---

## Project Structure

```
data-sentinel/
│
├── checks/          # Validation modules
├── utils/           # Utility functions
├── data/            # Sample datasets
├── docs/            # Documentation
├── tests/           # Unit tests
├── main.py          # Entry point
├── README.md
└── .gitignore
```

---

## Roadmap

### Version 0.1

- JSON loading
- Schema validation
- Type validation
- Duplicate detection

### Version 0.2

- Statistical anomaly detection
- Better reporting
- Configurable validation rules

### Version 0.5

- Historical profiling
- Smart validation engine

### Version 1.0

- Intelligent data integrity platform

---

## Installation

```bash
git clone https://github.com/peacemakerika/data-sentinel.git

cd data-sentinel

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

Example output:

```
Schema Errors: 0
Type Errors: 1
Duplicate Errors: 2

Integrity Score: 96%
```

---

## Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

Please open an issue before submitting a pull request.

---

## License

This project is currently under development.

A license will be added before the first stable release.
