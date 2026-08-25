# Troubleshooting & Diagnostic Guide

Common issues and their resolutions:

---

## 1. Model Artifact Not Found (`FileNotFoundError: model.joblib`)
- **Cause**: The pre-trained XGBoost bundle was not generated.
- **Solution**: Execute the training script:
  ```bash
  python ml/train_model.py
  ```

---

## 2. Audio Context Blocked by Browser Autoplay Policy
- **Cause**: Modern web browsers prevent audio playback until the user has interacted with the document.
- **Solution**: The `sound_engine.js` automatically resumes the `AudioContext` upon the user's first click anywhere on the page.

---

## 3. Port Conflict on 8000
- **Cause**: Another service or process is binding to port 8000.
- **Solution**: Run Uvicorn on an alternate port:
  ```bash
  uvicorn app.main:app --port 8080 --reload
  ```

---

## 4. PyTest Test Collection Errors
- **Cause**: Python path is not pointing to the repository root.
- **Solution**: Run pytest from the root directory:
  ```bash
  python -m pytest -v
  ```
