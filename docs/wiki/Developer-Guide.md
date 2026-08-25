# Developer Guide

This guide assists new engineers and data scientists in contributing to HRP Clinical.

---

## 1. Local Workspace Setup

```bash
git clone https://github.com/your-username/hospital-readmission-predictor.git
cd hospital-readmission-predictor

# Setup virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # On Windows
source .venv/bin/activate      # On Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

---

## 2. Running Automated Tests

The repository includes a 17-point automated pytest test suite:

```bash
pytest -v
```

All tests in `tests/test_complete_platform.py` and `tests/test_app.py` must pass before submitting pull requests.

---

## 3. Code Standards & Architecture Guidelines

1. **Safety First**: AI outputs must always be labeled as assistive analysis. Never remove doctor verification gates on medical certificates or clinical predictions.
2. **Deterministic Fallbacks**: Ensure all template routes pass fallback context dictionaries if database records are missing.
3. **No External Audio Assets**: Always use `sound_engine.js` for acoustic cues to prevent missing file errors.
4. **Bilingual Completeness**: When adding new UI elements, include corresponding entries in `static/js/i18n.js`.
