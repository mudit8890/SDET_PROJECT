# SDET Test Project

## Overview
A test automation project demonstrating SDET (Software Development Engineer in Test) fundamentals: writing tests, validating data, and wiring everything into a CI/CD pipeline.

## What's in this project

### ETL Pipeline (`sdet_project/etl/pipeline.py`)
A small extract-transform-load pipeline that:
- Pulls user data from a REST API
- Transforms it into a clean schema
- Loads it into a PostgreSQL database

### Test Suite (14 tests total)
- **`sdet_project/tests/test_api.py`** (5 tests) — API response and status code checks
- **`sdet_project/tests/test_database.py`** (4 tests) — database connection and data integrity checks
- **`sdet_project/tests/test_etl.py`** (5 tests) — extract/transform/load logic
- **`test_simple.py`** (3 tests) — email validation, age validation, API status checks
- **`test_data_validation.py`** (3 tests) — user data, order amount, and email format validation

### CI/CD Pipeline (`.github/workflows/ci.yml`)
Runs automatically on every push and pull request to `main`:
- Spins up a PostgreSQL service container
- Installs dependencies
- Runs the full pytest suite

## How to Run

```bash
pip install -r requirements.txt

# Standalone test scripts
python3 test_simple.py
python3 test_data_validation.py

# Full pytest suite (from sdet_project/)
cd sdet_project
python -m pytest tests/ -v
```

## Skills Demonstrated
- Test automation with Python and pytest
- ETL pipeline design (API → transform → PostgreSQL)
- CI/CD with GitHub Actions
- Data and API validation
- Assertions and test structure
