# Hospital Readmission Predictor (HRP Clinical) — Documentation Wiki

Welcome to the official technical wiki for **Hospital Readmission Predictor (HRP Clinical)** — an enterprise-grade, AI-enabled healthcare decision-support and clinical document intelligence platform.

---

## 🌟 What is HRP Clinical?

HRP Clinical is a clinical AI system that bridges the gap between raw inpatient data, multi-modal predictive intelligence, post-discharge workflow simulation, and doctor-patient collaboration:

$$\text{Data Ingestion} \to \text{Predictive AI (ML/DL)} \to \text{XAI Feature Breakdown} \to \text{RL Workflow Optimization} \to \text{Doctor Verification} \to \text{Tele-Health Follow-up}$$

---

## 🗺️ Wiki Directory & Quick Navigation

### 1. System Design & Workflows
- **[[System-Architecture]]**: End-to-end technical topology, gateways, micro-modules, and data contracts.
- **[[Product-Workflows]]**: User journeys for Patients, Attending Physicians, Care Coordinators, and Hospital Administrators.

### 2. Artificial Intelligence, ML & DL Suite
- **[[ML-Documentation]]**: Diabetes 130-US Hospitals (101k cohort), 10-stage preprocessing, and 7-algorithm benchmark.
- **[[Deep-Learning-Documentation]]**: PyTorch Tabular ANN/MLP, Tabular Transformer (Self-Attention), and Autoencoders.
- **[[Reinforcement-Learning-Documentation]]**: 6-stage care journey MDP, PyTorch PPO Agent, and Safety Constraint Guardrail Engine.
- **[[Explainable-AI]]**: TreeSHAP waterfall factor decomposition, baseline expected value shift, and 2D PCA patient embeddings.
- **[[CareAI]]**: Clinical summarization copilot, bilingual translation engine, and conversational analytics.

### 3. Clinical Portals & Medical Documents
- **[[Video-Consultation]]**: Telemedicine video call, dual live captions (English ↔ हिन्दी), and encrypted EHR notes.
- **[[Medical-Document-Intelligence]]**: Drag-and-drop OCR report extraction, reference range lab tables, and document Q&A.
- **[[Medical-Certificates]]**: Doctor digital signature workflow, official PDF formatting, and public QR verification portal.

### 4. Security, Governance & Infrastructure
- **[[Authentication-and-RBAC]]**: Multi-role access control, MFA 6-digit OTP, Active Sessions, and Break-Glass access.
- **[[API-Reference]]**: Comprehensive REST API reference across all clinical and AI endpoints.
- **[[Database-Schema]]**: Entity-relationship model for Patients, Predictions, Documents, Certificates, and Audit Logs.
- **[[MLOps-and-Monitoring]]**: Statistical drift monitoring (KS-test / PSI), Model Registry, and Experiment Tracking.
- **[[Deployment-Guide]]**: Local setup, Docker containerization, and production staging.
- **[[Security-and-Privacy]]**: HIPAA-conscious data minimization, role scoping, and immutable audit logs.

### 5. Interaction & Experience
- **[[Accessibility-and-i18n]]**: Google Material 3 clinical design, WCAG contrast, and real-time English ↔ हिन्दी translation.
- **[[Network-and-Connectivity]]**: Online/offline state telemetry and network retry handlers.
- **[[Sound-and-Animation]]**: Native Web Audio API sound synthesizer, SVG gauges, and Reduce-Motion controls.

### 6. Developer & Operations Guide
- **[[Developer-Guide]]**: Environment setup, running tests (`pytest`), and code conventions.
- **[[Contributing]]**: Branching strategies, pull request checklists, and coding guidelines.
- **[[Troubleshooting]]**: Common runtime errors, model loading, and database solutions.
- **[[FAQ]]**: Frequently asked questions on prediction interpretation, datasets, and clinical scope.
- **[[Responsible-AI-and-Limitations]]**: Transparent documentation of model limitations and clinician safety guardrails.
- **[[Changelog]]**: Release history and version logs.
- **[[Future-Roadmap]]**: Upcoming integration phases (HL7 FHIR connectors, federated learning).

---

> ⚠️ **Clinical Safety Disclaimer**: This software is intended for research, education, and clinical decision-support only. AI predictions, document extractions, and RL workflow recommendations require human verification by a qualified healthcare professional.
