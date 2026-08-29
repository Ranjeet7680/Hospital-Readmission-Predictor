"""
Pages 5 to 7: Comprehensive Table of Contents
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from ebook_core import create_styles, C_PRIMARY, C_SECONDARY, C_LIGHT_BG

def get_pages_005_007():
    styles = create_styles()
    flowables = []

    def make_toc_entry(title, page_num, is_part=False):
        t_style = styles['TOCPart'] if is_part else styles['TOCItem']
        dots = ". " * int((480 - len(title)*5.5) / 9)
        if len(dots) < 3: dots = "..."
        line = f"<b>{title}</b> {dots} <b>{page_num}</b>" if is_part else f"{title} <font color='#94a3b8'>{dots}</font> <b>{page_num}</b>"
        return Paragraph(line, t_style)

    # ==========================================
    # PAGE 5: Table of Contents — Parts I to VII
    # ==========================================
    flowables.append(Paragraph("Table of Contents — Volume I: Core AI & Modeling", styles['PartHeader']))
    flowables.append(Paragraph("Master Structural Index of Parts I through VII", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    toc_p1 = [
        ("Front Matter & Legal Governance (Pages 1–4)", "1", True),
        ("PART I — INTRODUCTION & THE $26B READMISSION CRISIS", "8", True),
        ("Chapter 1: The Clinical, Financial & Policy Landscape (CMS HRRP)", "8", False),
        ("Chapter 2: Problem Statement, Structural Healthcare Deficiencies & Stakeholders", "9", False),
        ("Chapter 3: The 30-Day Critical Transition Window & Pathophysiology", "10", False),
        ("Chapter 4: Traditional Clinical Risk Scores vs Modern Machine Learning", "11", False),
        
        ("PART II — PRODUCT BLUEPRINT & CAREAI ARCHITECTURE", "13", True),
        ("Chapter 5: Closed-Loop Decision Intelligence Architecture", "13", False),
        ("Chapter 6: User Personas, Clinical User Journeys & Workflow Integration", "14", False),
        ("Chapter 7: CareAI Agent Core & Multilingual Conversational Triaging", "15", False),
        ("Chapter 8: End-to-End System Wireframe & Microservices Interaction Blueprint", "16", False),

        ("PART III — CLINICAL DATA ENGINEERING & EHR INGESTION", "18", True),
        ("Chapter 9: The Diabetes 130-US Hospitals Dataset Deconstructed (101,766 Encounters)", "18", False),
        ("Chapter 10: Ingestion Pipelines, Clinical Data Cleaning & Imputation Strategies", "19", False),
        ("Chapter 11: Polypharmacy Risk Index & Derived Biomarker Feature Engineering", "20", False),
        ("Chapter 12: Class Imbalance Dynamics & SMOTE / Clustered Resampling Protocols", "21", False),

        ("PART IV — MACHINE LEARNING MODELING & TABULAR BENCHMARKING", "24", True),
        ("Chapter 13: Algorithmic Comparative Benchmark (Logistic, RF, LightGBM, CatBoost)", "24", False),
        ("Chapter 14: XGBoost Clustered Model Architecture (0.9794 ROC-AUC / 0.9412 PR-AUC)", "25", False),
        ("Chapter 15: Bayesian Hyperparameter Optimization & Stratified K-Fold Validation", "27", False),
        ("Chapter 16: Probability Calibration, Brier Score & Decision Curve Analysis (DCA)", "28", False),

        ("PART V — DEEP LEARNING ARCHITECTURES & TABULAR TRANSFORMERS", "31", True),
        ("Chapter 17: Tabular Deep Learning: Multi-Layer Perceptrons vs FT-Transformers", "31", False),
        ("Chapter 18: Column Embedding Layers & Multi-Head Self-Attention in PyTorch", "32", False),
        ("Chapter 19: Focal Loss Mathematical Derivation & Training Dynamics", "34", False),
        ("Chapter 20: Tabular ResNet vs Gradient Boosting: When Deep Learning Wins", "35", False),

        ("PART VI — EXPLAINABLE AI (XAI) & TREESHAP INTERPRETABILITY", "37", True),
        ("Chapter 21: Cooperative Game Theory & The Shapley Axiomatic Framework", "37", False),
        ("Chapter 22: TreeSHAP Exact Polynomial Decomposition Algorithm", "38", False),
        ("Chapter 23: Bedside Local Waterfall Plots & Clinical Biomarker Explanations", "39", False),
        ("Chapter 24: Global SHAP Summary Beeswarms & High-Order Feature Interactions", "40", False),

        ("PART VII — REINFORCEMENT LEARNING & DIGITAL TWIN SIMULATION", "43", True),
        ("Chapter 25: Post-Discharge Care as a Markov Decision Process (MDP)", "43", False),
        ("Chapter 26: State-Action-Reward Mathematical Formulation for Readmission", "44", False),
        ("Chapter 27: Deep Q-Network (DQN) Architecture & Experience Replay Buffer", "45", False),
        ("Chapter 28: Digital Twin Healthcare Simulation & Optimal Outreach Policies", "47", False),
    ]
    for title, pg, is_part in toc_p1:
        flowables.append(make_toc_entry(title, pg, is_part))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 6: Table of Contents — Parts VIII to XIV
    # ==========================================
    flowables.append(Paragraph("Table of Contents — Volume II: Connected Health & Systems", styles['PartHeader']))
    flowables.append(Paragraph("Master Structural Index of Parts VIII through XIV", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    toc_p2 = [
        ("PART VIII — MEDICAL DOCUMENT INTELLIGENCE & OCR PIPELINES", "49", True),
        ("Chapter 29: Discharge Summary Ingestion & Computer Vision Preprocessing", "49", False),
        ("Chapter 30: Clinical Named Entity Recognition (NER) & ICD-9/10 Normalization", "50", False),
        ("Chapter 31: Automated SOAP Note Synthesis & Physician Discharge Drafting", "51", False),
        ("Chapter 32: Document Validation, Hallucination Prevention & Human Verification", "52", False),

        ("PART IX — REAL-TIME TELEMEDICINE & SECURE VIDEO CONSULTATION", "54", True),
        ("Chapter 33: Tele-Triage & Post-Discharge Virtual Care Architecture", "54", False),
        ("Chapter 34: WebRTC Signaling, Peer-to-Peer Mesh vs SFU Infrastructure", "55", False),
        ("Chapter 35: In-Call Real-Time SHAP Risk Telemetry & Vital Sign Overlays", "56", False),
        ("Chapter 36: End-to-End Encryption (DTLS-SRTP) & WebRTC Media Security", "57", False),

        ("PART X — CRYPTOGRAPHIC DIGITAL HEALTH ID & 3D INTERACTIVE CARDS", "59", True),
        ("Chapter 37: Decentralized Patient Identification & The Universal Health ID", "59", False),
        ("Chapter 38: HMAC-SHA256 Cryptographic Token Generation & QR Verification", "60", False),
        ("Chapter 39: Three.js 3D Interactive Holographic Health Card Rendering", "61", False),
        ("Chapter 40: ABHA / Ayushman Bharat & FHIR R4 Patient Identifier Mapping", "62", False),

        ("PART XI — HEALTHCARE SECURITY, HIPAA/HITECH & RBAC", "64", True),
        ("Chapter 41: Healthcare Threat Modeling & Zero-Trust Clinical Architecture", "64", False),
        ("Chapter 42: Role-Based Access Control (RBAC) & Granular Clinical Permissions", "65", False),
        ("Chapter 43: JWT Asymmetric Authentication & Token Refresh Cycles", "66", False),
        ("Chapter 44: Comprehensive HIPAA, HITECH, GDPR & Audit Trail Logging", "67", False),

        ("PART XII — REAL-TIME CLINICAL ANALYTICS & EXECUTIVE DASHBOARDS", "69", True),
        ("Chapter 45: Executive Decision Intelligence & Hospital-Wide KPI Telemetry", "69", False),
        ("Chapter 46: Real-Time Readmission Rate Tracking & Departmental Heatmaps", "70", False),
        ("Chapter 47: Clinical Resource Allocation & High-Risk Nurse Staffing Optimization", "71", False),
        ("Chapter 48: MLOps Model Drift Monitoring, Data Shift & Automated Retraining", "72", False),

        ("PART XIII — RESPONSIVE UI/UX DESIGN & CLINICAL WORKFLOWS", "74", True),
        ("Chapter 49: Ergonomic Clinical Interface Design & Cognitive Load Reduction", "74", False),
        ("Chapter 50: Physician Triage Dashboard & Risk Stratification Table Components", "75", False),
        ("Chapter 51: Patient Mobile Portal, Multilingual Localization & High Contrast", "76", False),
        ("Chapter 52: WCAG 2.1 Level AA Accessibility & Dark Mode Engineering", "77", False),

        ("PART XIV — CLINICAL AUDIO ENGINEERING & HEARTBEAT SOUNDSCAPES", "79", True),
        ("Chapter 53: Audio Feedback in High-Stress Clinical Decision Environments", "79", False),
        ("Chapter 54: Web Audio API Synthesizer & Dynamic Heartbeat Telemetry Soundscapes", "80", False),
        ("Chapter 55: Auditory Alerts, Urgency Sonification & Earcons for Rapid Triage", "81", False),
        ("Chapter 56: Voice Interfaces & Cognitive Accessibility for Geriatric Patients", "82", False),
    ]
    for title, pg, is_part in toc_p2:
        flowables.append(make_toc_entry(title, pg, is_part))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 7: Table of Contents — Parts XV to XX & Appendices
    # ==========================================
    flowables.append(Paragraph("Table of Contents — Volume III: Scalability, Ethics & Reference", styles['PartHeader']))
    flowables.append(Paragraph("Master Structural Index of Parts XV through XX & Appendices A to H", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    toc_p3 = [
        ("PART XV — NETWORK RESILIENCE, OFFLINE-FIRST & EDGE AI", "83", True),
        ("Chapter 57: Edge Computing in Bandwidth-Constrained Healthcare Environments", "83", False),
        ("Chapter 58: Service Workers, Cache-First Strategies & IndexedDB Storage", "84", False),
        ("Chapter 59: Background Sync, Queue Reconciliation & Conflict Resolution", "85", False),
        ("Chapter 60: Lightweight Edge AI Inference with ONNX Runtime Web", "86", False),

        ("PART XVI — MICROSERVICES ARCHITECTURE & CLOUD DEPLOYMENT", "87", True),
        ("Chapter 61: High-Throughput FastAPI Asynchronous Microservices Backend", "87", False),
        ("Chapter 62: Redis Distributed Session Cache & In-Memory Rate Limiting", "88", False),
        ("Chapter 63: PostgreSQL 16 Relational Storage & Schema Optimization", "89", False),
        ("Chapter 64: Docker Containerization, CI/CD Pipelines & Cloud Scalability", "90", False),

        ("PART XVII — DEVELOPER GUIDE, RESTFUL APIS & PYTHON SDK", "92", True),
        ("Chapter 65: Comprehensive OpenAPI / Swagger Specification & Endpoint Catalog", "92", False),
        ("Chapter 66: High-Performance Python Client SDK (hrp-python-sdk)", "93", False),
        ("Chapter 67: Webhook Architecture & Real-Time Event Subscriptions", "94", False),
        ("Chapter 68: Automated Testing, Pytest Suites & Mock Clinical Data Fixtures", "95", False),

        ("PART XVIII — BIOETHICS, ALGORITHMIC BIAS & REGULATORY GOVERNANCE", "97", True),
        ("Chapter 69: Healthcare AI Ethics, Demographic Parity & Equalized Odds", "97", False),
        ("Chapter 70: Algorithmic Fairness Audits Across Demographic & Socioeconomic Cohorts", "98", False),
        ("Chapter 71: Human-in-the-Loop Clinical Safeguards & Doctor-in-the-Loop Workflows", "99", False),
        ("Chapter 72: Regulatory Alignment with FDA SaMD, EU AI Act & WHO Clinical AI Guidelines", "100", False),

        ("PART XIX — REAL-WORLD HOSPITAL DEPLOYMENT CASE STUDIES", "102", True),
        ("Chapter 73: Case Study 1 — High-Risk Diabetic Ketoacidosis with Severe Polypharmacy", "102", False),
        ("Chapter 74: Case Study 2 — Congestive Heart Failure in an Octogenarian Inpatient", "103", False),
        ("Chapter 75: Case Study 3 — Rural Community Hospital Tele-Triage & Outreach", "105", False),
        ("Chapter 76: Case Study 4 — Complex Surgical Discharge & Post-Op Medication Adherence", "106", False),

        ("PART XX — FUTURE HORIZONS, FOUNDATION MODELS & HEALTHCARE 2030", "108", True),
        ("Chapter 77: Multimodal Foundation Models (Med-PaLM, BioGPT) in Readmission Prevention", "108", False),
        ("Chapter 78: Ambient Clinical Intelligence & Autonomous Inpatient Scribes", "109", False),
        ("Chapter 79: Federated Learning Across Multi-Hospital Consortia & Decentralized Privacy", "110", False),
        ("Chapter 80: Concluding Remarks: The Next Decade of Proactive Connected Health", "111", False),

        ("APPENDICES A THROUGH H — MATHEMATICAL PROOFS & TECHNICAL REFERENCE", "112", True),
        ("Appendix A: Complete Mathematical Proofs (XGBoost, TreeSHAP, Attention, Bellman)", "112", False),
        ("Appendix B: ICD-9 & ICD-10 Diagnostic Category Clinical Mapping Codebook", "113", False),
        ("Appendix C: Complete REST API Endpoints Specification & JSON Payloads", "114", False),
        ("Appendix D: PostgreSQL Relational Database Schema DDL & Table Specifications", "115", False),
        ("Appendix E: Hyperparameter Optimization Grids & Cross-Validation Metrics", "116", False),
        ("Appendix F: Clinical Trial Simulation & Validation Protocol Specification", "117", False),
        ("Appendix G: HIPAA, HITECH & GDPR Regulatory Compliance Verification Checklist", "118", False),
        ("Appendix H: Comprehensive Academic Bibliography & Peer-Reviewed References", "119", False),
    ]
    for title, pg, is_part in toc_p3:
        flowables.append(make_toc_entry(title, pg, is_part))
    flowables.append(PageBreak())

    return flowables

print("sec02_toc loaded.")
