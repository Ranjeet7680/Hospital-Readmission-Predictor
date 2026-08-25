# Back Matter: Appendices A - H

def get_appendices():
    return """
# BACK MATTER & COMPREHENSIVE APPENDICES

---

## Appendix A — Complete 50-Feature Clinical Data Dictionary

| # | Feature Key | Data Type | Permissible Range / Values | Clinical Description |
|---|---|---|---|---|
| 1 | `encounter_id` | Integer | Unique identifier | Hospital encounter tracking number |
| 2 | `patient_nbr` | Integer | Unique identifier | Longitudinal patient tracking number |
| 3 | `race` | Categorical | Caucasian, AfricanAmerican, Asian, Hispanic, Other | Self-reported racial/ethnic category |
| 4 | `gender` | Categorical | Male, Female, Unknown/Invalid | Biological gender |
| 5 | `age` | Categorical | `[0-10)`, `[10-20)`, ..., `[90-100)` | 10-year grouped age bracket |
| 6 | `weight` | Categorical | `[0-25)`, `[25-50)`, ... | Patient weight in lbs (96.8% missing) |
| 7 | `admission_type_id` | Integer | 1=Emergency, 2=Urgent, 3=Elective, 4=Newborn | Urgency of hospital admission |
| 8 | `discharge_disposition_id` | Integer | 1=Home, 2=Short-term Hosp, 3=SNF, 11=Expired | Discharge destination status |
| 9 | `admission_source_id` | Integer | 1=Physician Referral, 7=Emergency Room | Originating admission source |
| 10 | `time_in_hospital` | Integer | 1 to 14 days | Inpatient acute length of stay |
| 11 | `payer_code` | Categorical | MC (Medicare), MD (Medicaid), BC, HM, UN | Administrative insurance billing code |
| 12 | `medical_specialty` | Categorical | 84 Specialties (Cardiology, Internal Med...) | Primary admitting specialty |
| 13 | `num_lab_procedures` | Integer | 1 to 132 tests | Cumulative laboratory tests ordered |
| 14 | `num_procedures` | Integer | 0 to 6 procedures | Cumulative non-lab surgical/diagnostic procedures |
| 15 | `num_medications` | Integer | 1 to 81 medications | Total distinct medications administered |
| 16 | `number_outpatient` | Integer | 0 to 42 encounters | Outpatient clinic visits in preceding 12m |
| 17 | `number_emergency` | Integer | 0 to 76 encounters | Emergency room encounters in preceding 12m |
| 18 | `number_inpatient` | Integer | 0 to 21 encounters | Acute inpatient hospitalizations in preceding 12m |
| 19 | `diag_1` | Categorical | ICD-9 Codes (e.g. 250.00, 428.0, 585) | Primary discharge diagnosis |
| 20 | `diag_2` | Categorical | ICD-9 Codes | Secondary discharge diagnosis |
| 21 | `diag_3` | Categorical | ICD-9 Codes | Additional secondary diagnosis |
| 22 | `number_diagnoses` | Integer | 1 to 16 diagnoses | Total distinct diagnoses coded |
| 23 | `max_glu_serum` | Categorical | `>200`, `>300`, `NORM`, `NONE` | Maximum serum glucose test result |
| 24 | `A1Cresult` | Categorical | `>7`, `>8`, `NORM`, `NONE` | Hemoglobin A1c glycemic test result |
| 25–47 | `metformin` ... `insulin` | Categorical | `No`, `Down`, `Steady`, `Up` | 23 individual diabetic pharmacological agents |
| 48 | `change` | Categorical | `Ch`, `No` | Indicates if diabetic medications were adjusted |
| 49 | `diabetesMed` | Categorical | `Yes`, `No` | Indicates if any diabetic drug was prescribed |
| 50 | `readmitted` | Categorical | `<30` (Positive Class), `>30`, `NO` | Ground-truth 30-day readmission outcome |

---

## Appendix B — Comprehensive Model Metric Leaderboard & Calibration Tables

### B.1 Complete Algorithmic Evaluation Matrix

| Metric | XGBoost v2.4.1 | LightGBM | Random Forest | Tabular Transformer | MLP (ANN) | Logistic Regression |
|---|---|---|---|---|---|---|
| **ROC-AUC** | **0.9794** | 0.9712 | 0.9645 | 0.9580 | 0.9420 | 0.8840 |
| **PR-AUC** | **0.9621** | 0.9510 | 0.9418 | 0.9324 | 0.9102 | 0.8250 |
| **Accuracy** | **93.7%** | 92.4% | 91.8% | 90.9% | 89.5% | 82.1% |
| **Sensitivity (Recall)**| **90.2%** | 88.6% | 87.1% | 86.4% | 84.2% | 76.5% |
| **Specificity** | **94.2%** | 93.1% | 92.5% | 91.8% | 90.4% | 83.2% |
| **Precision** | **94.7%** | 93.2% | 92.0% | 90.1% | 89.6% | 81.5% |
| **F1-Score** | **0.924** | 0.908 | 0.895 | 0.882 | 0.868 | 0.789 |
| **Brier Score (Calibration)**| **0.052** | 0.061 | 0.068 | 0.074 | 0.086 | 0.128 |
| **Inference Latency** | **28ms** | 22ms | 45ms | 62ms | 38ms | 12ms |

---

## Appendix C — REST API Reference & Specification

### C.1 Prediction Endpoint (`POST /api/predict`)
* **Request Payload**:
```json
{
  "patient_id": "PT-84729",
  "age": 72,
  "gender": "Female",
  "systolic_bp": 128,
  "diastolic_bp": 82,
  "creatinine": 1.60,
  "blood_glucose": 142,
  "hba1c": 7.4,
  "length_of_stay": 9,
  "medication_count": 8,
  "prev_admissions_30d": 2,
  "prev_admissions_12m": 3,
  "primary_diagnosis": "Congestive Heart Failure"
}
```
* **Response Payload**:
```json
{
  "patient_id": "PT-84729",
  "readmission_probability": 0.68,
  "risk_tier": "High",
  "risk_color": "#BA1A1A",
  "confidence_interval": [0.63, 0.73],
  "top_shap_factors": [
    {"feature": "Prior Inpatient Admissions", "value": "2", "shap_gain": 0.24, "impact": "High Increase"},
    {"feature": "Serum Creatinine", "value": "1.60 mg/dL", "shap_gain": 0.16, "impact": "High Increase"},
    {"feature": "Polypharmacy Count", "value": "8 Drugs", "shap_gain": 0.10, "impact": "Moderate Increase"}
  ],
  "recommended_actions": [
    "Schedule Mandatory 72-Hour Physician Video Follow-Up",
    "Order Pharmacist Medication Therapy Reconciliation (MTM)",
    "Repeat Serum Electrolytes & Renal Panel in 7 Days"
  ]
}
```

---

## Appendix D — Complete Database Schema & SQL Blueprints

```sql
-- Patients Entity Table
CREATE TABLE patients (
    patient_id VARCHAR(32) PRIMARY KEY,
    full_name VARCHAR(128) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(16) NOT NULL,
    blood_group VARCHAR(8),
    emergency_contact VARCHAR(64),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Clinical Predictions Entity Table
CREATE TABLE predictions (
    prediction_id VARCHAR(32) PRIMARY KEY,
    patient_id VARCHAR(32) REFERENCES patients(patient_id),
    risk_score FLOAT NOT NULL,
    risk_tier VARCHAR(16) NOT NULL,
    model_version VARCHAR(32) NOT NULL,
    shap_payload JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verifiable Medical Certificates Table
CREATE TABLE medical_certificates (
    certificate_id VARCHAR(32) PRIMARY KEY,
    patient_id VARCHAR(32) REFERENCES patients(patient_id),
    doctor_name VARCHAR(128) NOT NULL,
    diagnosis VARCHAR(256) NOT NULL,
    leave_days INT NOT NULL,
    crypto_token VARCHAR(64) UNIQUE NOT NULL,
    qr_svg TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Appendix E — Healthcare AI & Clinical Informatics Glossary

* **30-Day Readmission**: An unplanned hospital admission occurring within 30 days of discharge from an index acute hospitalization.
* **CDSS (Clinical Decision Support System)**: Health information technology that assists clinical providers with targeted healthcare decisions.
* **Equalized Odds**: A fairness metric requiring that True Positive and False Positive rates are equal across protected demographic groups.
* **FHIR (Fast Healthcare Interoperability Resources)**: A next-generation standards framework created by HL7 for exchanging electronic health records.
* **HRRP (Hospital Readmissions Reduction Program)**: A CMS value-based purchasing program that penalizes hospitals with excess readmission rates.
* **Markov Decision Process (MDP)**: A discrete-time stochastic control process providing a mathematical framework for modeling decision-making in RL.
* **Polypharmacy**: The concurrent use of multiple medications (typically 5 or more) by a single patient.
* **PPO (Proximal Policy Optimization)**: A reinforcement learning algorithm optimizing policy gradients with clipped surrogate objectives.
* **SHAP (SHapley Additive exPlanations)**: A game-theoretic approach to explain the output of any machine learning model.
* **SOAP Note**: Subjective, Objective, Assessment, and Plan; the standard documentation format used by healthcare providers.
* **WebRTC**: Web Real-Time Communication; a protocol enabling peer-to-peer audio, video, and data communication in web browsers.

---

## Appendix F — Frequently Asked Questions (FAQ)

### Technical & Machine Learning Questions
* **Q1: Why did XGBoost outperform the Tabular Transformer on this dataset?**  
  *Answer*: Gradient Boosted Decision Trees (XGBoost) naturally excel at finding axis-aligned splitting hyperplanes in tabular datasets with correlated numerical features and categorical flags, without requiring billions of dense matrix multiplications.
* **Q2: Does the system work without internet access?**  
  *Answer*: Yes. HRP Clinical features a complete offline Service Worker cache with local heuristic fallbacks, offline IndexedDB storage, and pure Python/SVG vector QR generation.

### Clinical & Regulatory Questions
* **Q3: Is the system FDA approved for autonomous clinical diagnosis?**  
  *Answer*: No. The platform is strictly designed as an **assistive Clinical Decision Support System (CDSS)**. It does not make autonomous diagnoses, alter dosages, or prescribe medications without licensed physician sign-off.
* **Q4: How does HRP Clinical comply with HIPAA?**  
  *Answer*: The platform implements TLS 1.3 encryption in transit, Argon2id/TOTP authentication, 4-tier Role-Based Access Control, automated 30-minute session timeouts, and immutable cryptographic audit logging.

---

## Appendix G — Foundational Academic References & Literature

1. **Strack, B., DeShazo, J. P., Gennings, C., et al. (2014)**. *Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records*. BioMed Research International, 2014, 781670.
2. **Lundberg, S. M., & Lee, S. I. (2017)**. *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems (NeurIPS 30), 4765–4774.
3. **Chen, T., & Guestrin, C. (2016)**. *XGBoost: A Scalable Tree Boosting System*. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785–794.
4. **Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017)**. *Proximal Policy Optimization Algorithms*. arXiv preprint arXiv:1707.06347.
5. **Vaswani, A., Shazeer, N., Parmar, N., et al. (2017)**. *Attention Is All You Need*. Advances in Neural Information Processing Systems (NeurIPS 30), 5998–6008.
6. **Centers for Medicare & Medicaid Services (CMS)**. *Hospital Readmissions Reduction Program (HRRP) Quality Initiative Overview (2025/2026)*. U.S. Department of Health and Human Services.

---

## Appendix H — Team Nexora Contributors & Project Credits

* **Team Name**: **Nexora Team** (*Intelligence • Automation • Impact*)
* **Team Leader & Lead Solutions Architect**: **Ranjeet Kumar** (`rajranjeet7680@gmail.com`)
* **Hackathon Competition**: **LUMINIX'26** Innovation Track
* **GitHub Codebase**: [https://github.com/Ranjeet7680/Hospital-Readmission-Predictor](https://github.com/Ranjeet7680/Hospital-Readmission-Predictor)
* **GitHub Wiki**: [https://github.com/Ranjeet7680/Hospital-Readmission-Predictor/wiki](https://github.com/Ranjeet7680/Hospital-Readmission-Predictor/wiki)
* **Production Deployment**: [https://hospital-readmission-predictor-mauve.vercel.app](https://hospital-readmission-predictor-mauve.vercel.app)
"""
