# MLOps & Production Monitoring

Implemented in `ml/mlops_manager.py`, the MLOps subsystem provides continuous surveillance over model drift, feature stability, model versions, and experiment tracking.

---

## 1. MLOps Continuous Lifecycle

```mermaid
flowchart LR
    A[Inpatient Ingestion] --> B[Data Quality Audit]
    B --> C[Drift Detector (PSI / KS-Test)]
    C --> D{PSI > 0.10 Threshold?}
    D -- Yes --> E[Trigger Retraining Alert & Sandbox Validation]
    D -- No --> F[Maintain Production Model Serving]
    E --> G[Model Registry Promotion (Staging -> Production)]
```

---

## 2. Statistical Drift Monitoring

- **Population Stability Index (PSI)**: Monitors population-level shifts across continuous clinical features (`creatinine`, `age`, `length_of_stay`).
- **Kolmogorov-Smirnov (KS) Test**: Validates two-sample distributional consistency between training distributions and live inference cohorts.
- **Drift Threshold**:
  - $\text{PSI} < 0.10$: Normal / No significant drift.
  - $0.10 \le \text{PSI} \le 0.20$: Moderate shift / Flag for data science review.
  - $\text{PSI} > 0.20$: Significant drift / Automated model retraining trigger.

---

## 3. Model Registry & Version Management

Located at `/ml/registry`:
- Tracks registered artifacts (`xgboost-v2.4.1`, `tabular-transformer-v1.0`, `ann-mlp-v2.1`).
- Manages lifecycle stage transitions: `Experimental` $\to$ `Staging` $\to$ `Production` $\to$ `Archived`.
- Supports one-click rollback to prior model versions if live validation metrics degrade.
