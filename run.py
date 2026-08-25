"""
Launcher for Hospital Readmission Predictor (HRP Clinical)
Ensures ML model artifact is present and starts the FastAPI server.
"""

import os
import sys
import uvicorn

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "ml", "model.joblib")

    if not os.path.exists(model_path):
        print("Model artifact not found. Training model now on dataset...")
        from ml.train_model import train
        train()

    print("\n" + "="*60)
    print("  Hospital Readmission Predictor (HRP Clinical) - v2.4.1")
    print("  Serving at: http://localhost:8000")
    print("="*60 + "\n")

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
