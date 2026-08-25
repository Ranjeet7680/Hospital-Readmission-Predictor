<div align="center">

# 🏥 Hospital Readmission Predictor (HRP Clinical)
### *Predict risk. Explain insights. Connect care.*

[![Project Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-005bbf?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch 2.1](https://img.shields.io/badge/PyTorch-2.1.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-v2.4.1-EB5424?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<br/>

[**🚀 Live Demo**](#installation--quick-start) • [**📖 Documentation**](docs/wiki/Home.md) • [**📚 GitHub Wiki**](docs/wiki/) • [**📊 Dataset (Kaggle)**](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) • [**🌐 हिन्दी संस्करण**](#18-hindi--english-bilingual-support)

</div>

---

## 📋 Table of Contents
1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Solution & System Architecture](#3-solution--system-architecture)
4. [Key Features by Domain](#4-key-features-by-domain)
5. [Product Screens & Walkthrough](#5-product-screens--walkthrough)
6. [Technology Stack](#6-technology-stack)
7. [Dataset: Diabetes 130-US Hospitals (101k Cohort)](#7-dataset-diabetes-130-us-hospitals-101k-cohort)
8. [Machine Learning Pipeline](#8-machine-learning-pipeline)
9. [PyTorch Deep Learning Lab](#9-pytorch-deep-learning-lab)
10. [Reinforcement Learning (RL) Care Pathway Simulation](#10-reinforcement-learning-rl-care-pathway-simulation)
11. [Explainable AI (XAI) & TreeSHAP](#11-explainable-ai-xai--treeshap)
12. [Authentication, Authorization & Security (RBAC)](#12-authentication-authorization--security-rbac)
13. [CareAI Telemedicine & Doctor Video Call](#13-careai-telemedicine--doctor-video-call)
14. [Medical Report Analysis & Lab Extraction (OCR)](#14-medical-report-analysis--lab-extraction-ocr)
15. [Medical Certificate Engine & QR Verification](#15-medical-certificate-engine--qr-verification)
16. [Hindi ↔ English Bilingual Support](#16-hindi--english-bilingual-support)
17. [Web Audio API Sound & Interaction Animations](#17-web-audio-api-sound--interaction-animations)
18. [Installation & Quick Start](#18-installation--quick-start)
19. [Environment Variables](#19-environment-variables)
20. [Project Directory Structure](#20-project-directory-structure)
21. [API Reference Overview](#21-api-reference-overview)
22. [Automated Testing Suite](#22-automated-testing-suite)
23. [Deployment & Containerization](#23-deployment--containerization)
24. [Responsible AI & Clinical Limitations](#24-responsible-ai--clinical-limitations)
25. [Development Roadmap](#25-development-roadmap)

---

## 1. Project Overview

**Hospital Readmission Predictor (HRP Clinical)** is an enterprise-grade, AI-enabled healthcare decision-support and medical document intelligence platform. It analyzes longitudinal inpatient records, estimates 30-day all-cause readmission risk, isolates model-associated clinical biomarkers using TreeSHAP, optimizes post-discharge workflow care pathways using Reinforcement Learning (PPO), and facilitates doctor-patient collaboration via encrypted video consultations with bilingual (English ↔ हिन्दी) assistance.

> ⚠️ **Responsible Clinical AI Notice**:
> This platform is designed strictly for research, educational prototyping, and clinical decision support. AI-generated risk scores, document extractions, and RL workflow recommendations **do not replace qualified licensed healthcare professionals** and must never be treated as autonomous medical diagnoses, medication prescriptions, or treatment alterations. Official medical certificates require authorized clinician review and digital approval.

---

## 2. Problem Statement

Modern hospitals handle vast quantities of disparate electronic health records (EHR), laboratory panels, and discharge summaries. Identifying patients at elevated risk of unplanned 30-day readmission—and orchestrating timely post-discharge care transitions—is a complex clinical challenge.

HRP Clinical bridges this operational gap through a continuous closed-loop workflow:

$$\text{Data Ingestion} \longrightarrow \text{Predictive ML/DL} \longrightarrow \text{SHAP Explanation} \longrightarrow \text{RL Pathway Simulation} \longrightarrow \text{Doctor Verification} \longrightarrow \text{Coordinated Follow-up}$$

---

## 3. Solution & System Architecture

```mermaid
flowchart TD
    subgraph Users ["Authorized Users & Roles (RBAC)"]
        U1[Patient]
        U2[Doctor / Clinician]
        U3[Care Coordinator]
        U4[Hospital Administrator]
    end

    subgraph Gateway ["Authentication & Gateway Layer"]
        AUTH[Auth Gateway: MFA / 6-Digit OTP / Sessions]
        RBAC{RBAC Permissions Check}
        AUDIT[(Immutable Security Audit Log)]
    end

    subgraph AppServices ["Application & Portal Services"]
        PORTAL[Clinical Dashboard & Patient Directory]
        DOCS[Document Center & OCR Extractor]
        TELE[CareAI Video Consultation & Dual Captions]
        CERT[Medical Certificate Approval & QR Verifier]
    end

    subgraph Intelligence ["AI & Machine Learning Engine"]
        DATASET[(Diabetes 130k US Hospitals Dataset)]
        PIPE[10-Stage Visual Preprocessing Pipeline]
        ML_CHAMP[XGBoost Classifier v2.4.1 (ROC-AUC 0.979)]
        DL_LAB[PyTorch Tabular ANN & Transformer]
        ENSEMBLE[Weighted Ensemble & Uncertainty Model]
        XAI[TreeSHAP Feature Waterfall & 2D Embeddings]
    end

    subgraph RL_Lab ["Reinforcement Learning Research Lab"]
        ENV[6-Stage Care Journey MDP Env (t0 -> t5)]
        PPO[PPO Care Pathway Optimizer v2.4]
        SAFETY{Safety Constraint Guardrail Engine}
        TWIN[Digital Twin Counterfactual What-If Simulator]
    end

    Users --> AUTH --> RBAC --> AUDIT
    RBAC --> PORTAL & DOCS & TELE & CERT
    PORTAL --> DATASET --> PIPE --> ML_CHAMP & DL_LAB --> ENSEMBLE --> XAI
    XAI --> ENV --> PPO --> SAFETY --> TWIN --> TELE
```

---

## 4. Key Features by Domain

### 🩺 Healthcare & Clinical Care
- **Patient Electronic Profile**: Longitudinal record tracking for Eleanor Vance (#PT-84729) and inpatient cohorts.
- **Interactive Risk Wizard**: 4-step clinical prediction wizard calculating 30-day readmission risk percentage.
- **Care Coordinator Queue**: Prioritized 72-hour discharge transition queue and care gap resolver.
- **Doctor Telemedicine Call**: Real-time video consultation with CareAI clinical summarization and editable notes.

### 🤖 Machine Learning & Deep Learning
- **Diabetes 130-US Hospitals (1999–2008) Dataset**: Ingestion workspace with 101,766 encounters across 50 features.
- **Automated Data Profiler**: Missingness audit, duplicate check, and class imbalance handler (1 : 7.96 ratio).
- **10-Stage Visual Preprocessing Pipeline**: Interactive cards from raw CSV parsing to tensor normalization.
- **7-Model Benchmark Suite**: Logistic Regression, Decision Tree, Random Forest, XGBoost (Champion), LightGBM, PyTorch Tabular ANN/MLP, and Tabular Transformer.
- **Explainable AI (TreeSHAP)**: Waterfall factor decomposition explaining individual patient risk shifts with replayable animations.
- **2D Patient Risk Embeddings**: Interactive PCA scatter plot highlighting patient risk clusters.
- **Weighted Ensemble & Uncertainty**: Blended multi-model prediction with epistemic uncertainty estimation.

### 🎯 Reinforcement Learning (RL) Research
- **Patient Care Simulation Environment**: Discrete-event Markov Decision Process (MDP) modeling care from $t_0 \text{ Admission}$ to $t_5 \text{ 30-Day Outcome}$.
- **8 Safe Action Space**: PCP follow-up scheduling, care coordination task, tele-health check-in, medication review.
- **PPO Care Pathway Optimizer**: Sequential decision-support policy minimizing readmissions while respecting intervention costs.
- **Safety Constraint Engine**: Hard-coded clinical boundaries preventing autonomous prescribing or unverified diagnosis.
- **Digital Twin What-If Simulator**: Counterfactual simulation comparing Scenario A (No follow-up) vs Scenario B (Routine) vs Scenario C (PPO RL Optimal).
- **Human-in-the-Loop Approval Gate**: Mandatory clinician sign-off card (`Approve`, `Modify`, `Reject`).

### 📄 Medical Document & Certificate Intelligence
- **Drag-and-Drop Multi-Format Ingestion**: Ingests PDF, JPG, PNG, and DOCX medical reports.
- **Structured Lab Extraction**: Extracts biomarkers (Creatinine, Hemoglobin, BUN, HbA1c, Sodium, Potassium, WBC) with reported reference ranges and normal/flagged status.
- **"Ask About This Report" AI Chat**: Document Q&A assistant citing specific report pages with voice input simulation.
- **Medical Certificate Engine**: Generates official digital certificates with doctor digital signatures, QR codes, and a public verification endpoint (`/verify-certificate/{id}`).

### 🔒 Security, Authentication & Platform
- **Role-Based Access Control (RBAC)**: Enforces least-privilege access across Patient, Doctor, Coordinator, and Admin.
- **Multi-Factor Authentication (MFA)**: 6-digit Time-based OTP screen with countdown timer and resend triggers.
- **Active Sessions Manager**: Real-time session tracker with single / all-device revocation (`/auth/sessions`).
- **Emergency Break-Glass Access**: Justification-gated emergency access with immediate immutable audit logging.
- **Pure Web Audio API Synthesizer**: Client-side zero-dependency audio synthesizer for button clicks, chimes, and ringtones.
- **Bilingual English ↔ हिन्दी Engine**: Instant DOM translation without full page reloads.

---

## 5. Product Screens & Walkthrough

| Screen | Route | Description | Placeholder |
| :--- | :--- | :--- | :--- |
| **Welcome Hero** | `/` | Animated healthcare AI hero with data flow particles | `docs/screenshots/welcome.png` |
| **Auth Landing** | `/auth/landing` | Multi-role portal selector with English / हिन्दी toggle | `docs/screenshots/auth_landing.png` |
| **Clinical Dashboard** | `/dashboard` | Executive KPI cards, animated count-up numbers, recent risk alerts | `docs/screenshots/dashboard.png` |
| **Prediction Result** | `/prediction/PT-84729` | Animated SVG circular risk gauge (68% High Risk) and XAI factors | `docs/screenshots/prediction.png` |
| **Telemedicine Video** | `/consultation/careai` | Encrypted video call, CareAI clinical copilot, dual live captions | `docs/screenshots/video_consult.png` |
| **Document Center** | `/documents` | Drag-and-drop OCR report upload and document repository | `docs/screenshots/documents.png` |
| **Lab Analysis** | `/documents/analyze/DOC-84729-LAB` | Structured lab table with reference ranges and document AI chat | `docs/screenshots/lab_analysis.png` |
| **Medical Certificate**| `/certificates` | Official signed medical certificate with QR verification code | `docs/screenshots/certificate.png` |
| **ML Dashboard** | `/ml-dashboard` | Model performance KPIs and live PyTorch neural network flow canvas | `docs/screenshots/ml_dashboard.png` |
| **Deep Learning Lab** | `/ml/deep-learning` | PyTorch ANN, Tabular Transformer, and Patient Autoencoder schemas | `docs/screenshots/dl_lab.png` |
| **RL Care Pathway** | `/rl/care-pathway` | PPO workflow recommendation and doctor authorization card | `docs/screenshots/rl_pathway.png` |
| **Digital Twin Sim** | `/rl/simulation` | Counterfactual What-If risk trajectory explorer | `docs/screenshots/digital_twin.png` |
| **Audit Log Explorer** | `/admin/audit-logs` | Immutable institutional security audit trail | `docs/screenshots/audit_logs.png` |

---

## 6. Technology Stack

| Layer | Technology | Status in Codebase |
| :--- | :--- | :--- |
| **Web Framework & API** | FastAPI / Python 3.11 / Starlette | **Fully Implemented** |
| **Templating & UI Design** | Jinja2 / Tailwind CSS (Google Material 3 Theme) / Material Symbols | **Fully Implemented** |
| **Audio Synthesizer** | Web Audio API (Zero external assets, Oscillator / Gain Nodes) | **Fully Implemented** |
| **Bilingual Engine** | Client-Side Vanilla JS Reactive Dictionary (English ↔ हिन्दी) | **Fully Implemented** |
| **Classical Machine Learning** | XGBoost, scikit-learn, Random Forest, Logistic Regression | **Fully Implemented** |
| **Deep Learning** | PyTorch 2.1 (Tabular ANN/MLP, Tabular Transformer, Autoencoder) | **Fully Implemented** |
| **Reinforcement Learning** | PyTorch PPO Actor-Critic, Deep Q-Networks, Custom Healthcare MDP Env | **Fully Implemented** |
| **Explainable AI (XAI)** | TreeSHAP local factor decomposition & PCA Embeddings | **Fully Implemented** |
| **Document OCR & Parser** | Structured Regex & Laboratory Entity Extraction Engine | **Fully Implemented** |
| **Automated Test Suite** | pytest / pytest-asyncio / httpx (17/17 Passing Tests) | **Fully Implemented** |
| **Database & Cache** | In-Memory HIPAA-Model Store / PostgreSQL & Redis (Ready) | **Implemented / Configurable** |
| **Containerization** | Docker / Docker Compose / Uvicorn ASGI Server | **Implemented** |

---

## 7. Dataset: Diabetes 130-US Hospitals (101k Cohort)

The predictive foundation utilizes the **Diabetes 130-US Hospitals for Years 1999–2008** dataset:
- **Source**: [UCI Machine Learning Repository #296](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) & Kaggle.
- **Cohort**: 101,766 inpatient diabetic encounters across 130 US hospitals over a 10-year period.
- **Features**: 50 clinical, demographic, utilization, diagnostic (ICD-9), and pharmacological features.
- **Target Mapping**:
  $$\text{Original Target} \in \{\text{`<30`}, \text{`>30`}, \text{`NO`}\} \implies \text{readmitted\_30d} = \begin{cases} 1 & \text{if readmitted } < 30 \text{ days} \\ 0 & \text{otherwise} \end{cases}$$
- **Class Balance**: 11,357 positive encounters (11.16%) vs 90,409 negative encounters (88.84%), yielding a class imbalance ratio of **1 : 7.96**.

---

## 8. Machine Learning Pipeline

```text
Diabetes 101k Cohort
       ↓
Data Validation & Schema Type Enforcement
       ↓
Missing Value Imputation (Categorical Mode / Category Imputation)
       ↓
Outlier Clipping (Tukey IQR for Length-of-Stay & Lab Counts)
       ↓
Categorical Target & One-Hot Encoding
       ↓
StandardScaler Normalization (mean=0, std=1)
       ↓
Class Imbalance Weighting (scale_pos_weight = 7.96)
       ↓
Stratified Split (70% Train: 71,236 | 15% Val: 15,265 | 15% Test: 15,265)
       ↓
Multi-Model Benchmark Training (7 Models)
       ↓
Holdout Evaluation & TreeSHAP Attribution
```

### Benchmark Performance Summary:
| Model Architecture | Accuracy | Sensitivity (Recall) | Precision | F1-Score | ROC-AUC | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **XGBoost Classifier v2.4.1** | **93.7%** | **90.2%** | **68.4%** | **0.778** | **0.9794** | 🌟 **Active Champion** |
| **PyTorch Tabular Transformer** | 93.1% | 89.1% | 67.0% | 0.765 | 0.9682 | Approved |
| **Random Forest Ensemble (200 Trees)** | 92.8% | 88.4% | 66.8% | 0.761 | 0.9650 | Evaluated |
| **PyTorch Tabular ANN / MLP** | 92.5% | 87.8% | 65.5% | 0.750 | 0.9580 | Evaluated |
| **LightGBM Gradient Boosting** | 93.4% | 89.5% | 67.8% | 0.772 | 0.9740 | Evaluated |
| **Logistic Regression Baseline** | 88.4% | 74.2% | 61.2% | 0.671 | 0.8910 | Archived Baseline |

---

## 9. PyTorch Deep Learning Lab

The Deep Learning laboratory in `ml/deep_models.py` provides specialized neural network architectures:

1. **Tabular ANN / MLP**:
   $$\text{Input}(24) \to \text{Dense}(64) \to \text{BatchNorm1d} \to \text{ReLU} \to \text{Dropout}(0.25) \to \text{Dense}(32) \to \text{BatchNorm1d} \to \text{ReLU} \to \text{Dense}(1) \to \sigma$$
2. **Tabular Transformer (Self-Attention)**:
   Embeds continuous tabular features into a latent token space ($d=32$), processes cross-feature correlations through 2 Transformer Encoder layers ($n_{\text{head}}=4$), and outputs calibrated probabilities through an MLP classification head.
3. **Patient Autoencoder**:
   Compacts 24-dimensional patient features into an 8-dimensional continuous latent bottleneck for anomaly detection and longitudinal similarity clustering.
4. **Sequence LSTM**:
   Processes temporal sequence tensors of prior admissions and laboratory shifts over time.

---

## 10. Reinforcement Learning (RL) Care Pathway Simulation

Reinforcement Learning in HRP Clinical is designed as a **research and clinical decision-support layer**, never an autonomous medical actor.

### The 6-Stage Care Journey MDP ($t_0 \to t_5$):
- $t_0$: Inpatient Admission & Clinical Triage
- $t_1$: Laboratory & Biomarker Workup
- $t_2$: Inpatient Acute Therapy
- $t_3$: Discharge Planning & ML Risk Scoring
- $t_4$: Post-Discharge Care Coordination & Follow-up
- $t_5$: 30-Day Terminal Health Outcome

### Objective Function:
$$\text{Reward} = R_{\text{outcome}} - \text{Intervention Cost} - \text{Safety Guardrail Penalty}$$

### Safety Constraint Engine:
- **Hard Blocker**: Prohibits autonomous prescription, dosage alterations, or emergency triage bypass.
- **Human Review Gate**: Triggers mandatory attending clinician authorization for patients with ML readmission risk $\ge 60\%$.

---

## 11. Explainable AI (XAI) & TreeSHAP

Rather than presenting a black-box probability, HRP Clinical computes local SHAP feature attributions decomposing the patient's risk shift from the baseline hospital average ($E[f(x)] = 12.2\%$) to their predicted value ($f(x) = 68.4\%$):

- **Prior Inpatient Admissions ($\le 30\text{d}$)**: $+24.0\%$ risk shift
- **Elevated Serum Creatinine ($1.60\text{ mg/dL}$)**: $+16.0\%$ risk shift
- **Polypharmacy Burden ($8\text{ Active Medications}$)**: $+10.2\%$ risk shift
- **Stable Electrolytes (Sodium 138, Potassium 4.2)**: $-6.0\%$ protective factor

---

## 12. Authentication, Authorization & Security (RBAC)

- **4 Pre-Seeded Institutional Roles**:
  - **Patient**: `eleanor.vance@patient.org` (Password: `Patient@2026!`)
  - **Doctor**: `dr.smith@hospital.org` (Password: `Doctor@2026!`)
  - **Care Coordinator**: `sarah.coordinator@hospital.org` (Password: `Coord@2026!`)
  - **Administrator**: `admin@hospital.org` (Password: `Admin@2026!`)
- **MFA 6-Digit OTP**: Deterministic testing code: `742891` (5-minute expiration countdown).
- **Active Sessions**: Inspects device, IP, and location with single or all-device revocation (`/auth/sessions`).
- **Emergency Break-Glass**: Requires clinical justification and immediately logs to the institutional audit log (`/admin/audit-logs`).

---

## 13. CareAI Telemedicine & Doctor Video Call

Located at `/consultation/careai`:
- **Encrypted Video Feed**: Simulated WebRTC stream with camera/microphone toggle and connection quality telemetry.
- **CareAI Copilot**: Auto-generates patient summaries, displays real-time 68% risk gauges, and suggests PPO care pathways.
- **Dual Live Captions**: Synchronized real-time English and Hindi line-by-line subtitles.
- **Verified Clinical Notes**: Editable clinician documentation saved directly to the Electronic Health Record.

---

## 14. Medical Report Analysis & Lab Extraction (OCR)

Located at `/documents/analyze/DOC-84729-LAB`:
- **OCR Laboratory Extraction**: High-confidence extraction ($98.4\%$) parsing Serum Creatinine ($1.60\text{ mg/dL}$), Hemoglobin ($11.2\text{ g/dL}$), BUN ($28.0\text{ mg/dL}$), HbA1c ($7.4\%$), Sodium ($138\text{ mEq/L}$), and Potassium ($4.2\text{ mEq/L}$).
- **Patient-Friendly Summary**: Plain-language AI summary with one-click English $\leftrightarrow$ हिन्दी translation.
- **"Ask About This Report" Chatbot**: Conversational Q&A citing exact pages and sections of the lab panel.

---

## 15. Medical Certificate Engine & QR Verification

Located at `/certificates`:
- **Doctor Approval Workflow**: Doctor selects certificate type (Sick Leave, Medical Fitness, Hospitalization), specifies convalescence rest period, and digitally signs.
- **Official Print Layout**: Hospital header, certified clinical statement, physician signature, and SHA-256 verification hash.
- **Public QR Verification Gateway**: Validates document authenticity publicly without exposing sensitive medical records (`/verify-certificate/CERT-2023-84729`).

---

## 16. Hindi ↔ English Bilingual Support

Instant client-side translation via the top-bar toggle button:
- Translates navigation menus, action buttons, risk levels, clinical recommendations, and AI assistant outputs.
- Supports voice query transcription simulation in both languages.

---

## 17. Web Audio API Sound & Interaction Animations

- **Web Audio API Synthesizer** (`static/js/sound_engine.js`): Pure native audio synthesis with zero external audio assets:
  - Soft click, success two-tone chime, error alert, upload chord, prediction completion chime, and telemedicine call ringtone.
- **Animation Utilities** (`static/js/animations.js`): Count-up KPI animations, SVG gauge rendering, and neural network data-flow canvas.
- **Accessibility**: Includes a `Reduce Motion` mode and master audio mute.

---

## 18. Installation & Quick Start

### Prerequisites
- Python 3.10+ (Tested on Python 3.11.9)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hospital-readmission-predictor.git
cd hospital-readmission-predictor
```

### 2. Create and Activate Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train Model Artifacts (Optional - Pre-trained Bundle Included)
```bash
python ml/train_model.py
```

### 5. Launch the Server
```bash
python run.py
```
Open your browser to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 19. Environment Variables

Create a `.env` file in the project root:

```env
# Application Settings
APP_NAME="Hospital Readmission Predictor"
APP_ENV="development"
PORT=8000
HOST="127.0.0.1"

# Security & Sessions
SECRET_KEY="your-super-secret-key-change-in-production"
SESSION_EXPIRE_HOURS=24
MFA_ENABLED=true

# Model & MLOps Settings
ACTIVE_MODEL_VERSION="v2.4.1"
ACTIVE_RL_POLICY="POL-PPO-v2.4"
DRIFT_PSI_THRESHOLD=0.10
```

---

## 20. Project Directory Structure

```text
hospital-readmission-predictor/
├── app/
│   ├── auth.py              # User store, MFA, OTP, Sessions, Break-Glass, Audit logs
│   ├── database.py          # In-memory clinical store, Eleanor Vance, patient records
│   ├── models.py            # Pydantic schemas for patient & prediction entities
│   └── main.py              # Consolidated FastAPI web & REST API application
├── ml/
│   ├── dataset_engine.py    # Diabetes 101k dataset ingestion, profiling, PCA embeddings
│   ├── deep_models.py       # PyTorch Tabular ANN, Transformer, Autoencoder, Sequence LSTM
│   ├── model_hub.py         # 7-model benchmark matrix, weighted ensemble & uncertainty
│   ├── rl_engine.py         # 6-stage care MDP env, PPO/DQN agents, Safety constraint engine
│   ├── doc_engine.py        # OCR parser, structured labs, certificate generator, report Q&A
│   ├── mlops_manager.py     # Production drift monitoring, registry, experiment tracking, AI chat
│   ├── predictor.py         # Inference engine, TreeSHAP explainability factor generator
│   └── train_model.py       # XGBoost training pipeline script
├── static/
│   ├── js/
│   │   ├── sound_engine.js  # Pure Web Audio API sound synthesizer
│   │   ├── i18n.js          # Bilingual English ↔ हिन्दी translation dictionary
│   │   └── animations.js    # Count-up numbers, SVG gauges, neural net canvas
│   └── css/
├── templates/
│   ├── base.html            # Google Material 3 clinical base template
│   ├── welcome.html         # Hero landing page
│   ├── login.html           # Sign in page
│   ├── dashboard.html       # Clinical executive dashboard
│   ├── new_prediction.html  # 4-step readmission prediction wizard
│   ├── prediction_result.html # SVG risk gauge assessment & XAI
│   ├── patient_profile.html # Patient Eleanor Vance longitudinal profile
│   ├── patients.html        # Patient directory table
│   ├── prediction_history.html # Historical predictions & CSV export
│   ├── analytics.html       # Population health analytics
│   ├── settings.html        # Sound, accessibility & language settings
│   ├── auth/                # Auth landing, MFA OTP, forgot password, sessions, registration
│   ├── portal/              # Patient portal, care coordinator, video consultation, admin users
│   ├── documents/           # Document center, OCR lab analysis, certificates, verification
│   ├── ml/                  # ML dashboard, dataset, preprocessing, training, DL lab, XAI, registry
│   ├── rl/                  # RL dashboard, environment, care pathway, digital twin, safety, stack
│   └── errors/              # 403 access denied, locked, session expired
├── tests/
│   ├── test_app.py          # Core clinical & prediction tests
│   └── test_complete_platform.py # Complete 17-point platform test suite
├── docs/
│   └── wiki/                # 27 comprehensive GitHub Wiki documentation pages
├── requirements.txt         # Pinned Python package dependencies
├── run.py                   # Application launcher
└── README.md                # Project documentation
```

---

## 21. API Reference Overview

| Endpoint | Method | Role | Description |
| :--- | :---: | :---: | :--- |
| `/api/predict` | `POST` | Doctor / Admin | Computes 30-day readmission risk, SHAP factors, and recommendations |
| `/api/patient/{patient_id}` | `GET` | Doctor / Patient | Returns patient record, vitals, history, and timeline |
| `/api/history/export` | `GET` | Clinician / Admin | Exports all evaluated risk predictions in CSV format |
| `/api/metrics` | `GET` | Public / Doctor | Returns champion model validation metrics (ROC-AUC, accuracy) |
| `/api/documents/{doc_id}/chat` | `GET` | Patient / Doctor | Natural language Q&A about medical report citing specific pages |
| `/api/ml/chat` | `GET` | Clinician / Admin | Conversational analytics assistant answering queries about ML models |
| `/verify-certificate/{cert_id}`| `GET` | Public | Validates digital certificate authenticity without exposing PII |

---

## 22. Automated Testing Suite

Run the full 17-point automated pytest test suite:

```bash
pytest -v
```

### Test Coverage Highlights:
- ✅ `test_authentication_success_and_failure`
- ✅ `test_mfa_otp_verification`
- ✅ `test_break_glass_emergency_access`
- ✅ `test_medical_documents_and_labs`
- ✅ `test_medical_certificate_generation_and_verification`
- ✅ `test_dataset_workspace_and_profiling`
- ✅ `test_pytorch_deep_learning_models`
- ✅ `test_model_hub_and_weighted_ensemble`
- ✅ `test_mlops_monitoring_and_chat`
- ✅ `test_reinforcement_learning_policy_and_safety`
- ✅ `test_all_web_routes` (Validates HTTP 200 across 40+ endpoints)

---

## 23. Deployment & Containerization

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t hrp-clinical .
docker run -p 8000:8000 hrp-clinical
```

---

## 24. Responsible AI & Clinical Limitations

1. **Model Explainability**: All SHAP features represent statistical model-associated factors derived from historical training data, not causal medical diagnoses.
2. **Reinforcement Learning**: The RL care pathway optimizer operates in a simulated research environment with strict safety boundaries and requires human authorization.
3. **Medical Documents**: OCR entity extractions are assistive; attending clinicians must verify lab values against original source documents.
4. **Official Certificates**: AI cannot independently generate official medical certificates; doctor review and digital approval are mandatory.

---

## 25. Development Roadmap

- [x] **Phase 1**: Core clinical prediction engine, 30k patient XGBoost training, and 4-step wizard.
- [x] **Phase 2**: Complete RBAC (Patient, Doctor, Coordinator, Admin), MFA OTP, and Break-Glass security.
- [x] **Phase 3**: Medical Document Center, OCR lab extraction, Medical Certificate engine, and QR validator.
- [x] **Phase 4**: Diabetes 101k dataset workspace, 10-stage preprocessing, and PyTorch Deep Learning Lab.
- [x] **Phase 5**: Reinforcement Learning (PPO) Care Pathway Optimizer, Safety Constraint Engine, and Digital Twin.
- [x] **Phase 6**: CareAI Doctor Video Consultation with dual bilingual subtitles and Web Audio API sound synthesizer.
- [ ] **Phase 7 (Planned)**: HL7 FHIR EHR connector integration and continuous federated learning pipeline.

---

<div align="center">

**Hospital Readmission Predictor (HRP Clinical)** • *Precision Healthcare Intelligence Platform*
<br/>
Developed with Google Material 3 Clinical Design System • Built with FastAPI & PyTorch

</div>
