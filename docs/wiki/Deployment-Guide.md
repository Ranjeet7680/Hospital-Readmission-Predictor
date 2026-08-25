# Deployment Guide

This guide covers deploying the HRP Clinical platform locally, inside Docker containers, and in cloud staging environments.

---

## 1. Local Development Setup

```bash
# 1. Clone repository
git clone https://github.com/your-username/hospital-readmission-predictor.git
cd hospital-readmission-predictor

# 2. Virtual environment setup
python -m venv .venv

# On Windows:
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

# 3. Dependency installation
pip install -r requirements.txt

# 4. Train model artifacts
python ml/train_model.py

# 5. Run test suite
pytest -v

# 6. Start server
python run.py
```

---

## 2. Docker Container Deployment

### `Dockerfile`
```dockerfile
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build & Run Commands
```bash
docker build -t hrp-clinical:2.4.1 .
docker run -d -p 8000:8000 --name hrp-app hrp-clinical:2.4.1
```
