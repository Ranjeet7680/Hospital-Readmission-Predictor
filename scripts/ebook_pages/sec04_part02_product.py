"""
Pages 13 to 17: Part II — Product Blueprint & CareAI Architecture
"""
import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from ebook_core import create_styles, make_callout, make_table, C_PRIMARY, C_SECONDARY, C_DARK, C_LIGHT_BG

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ebook_assets")

def get_pages_004_008_part2():
    styles = create_styles()
    flowables = []

    # ==========================================
    # PAGE 13: Part II Header & Chapter 5 (Closed-Loop Intelligence)
    # ==========================================
    flowables.append(Paragraph("PART II — PRODUCT BLUEPRINT & CAREAI ARCHITECTURE", styles['PartHeader']))
    flowables.append(Paragraph("Chapter 5 — Closed-Loop Decision Intelligence Architecture", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "The fundamental design philosophy of the Hospital Readmission Predictor is the <b>Closed-Loop Clinical Intelligence Cycle</b>. "
        "Unlike isolated machine learning prototypes that output a static risk number into an EHR without triggering downstream clinical "
        "actions, our platform actively orchestrates a 5-stage closed loop spanning ingestion, risk scoring, clinical explanation, "
        "virtual engagement, and continuous digital monitoring.", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    loop_headers = ["Cycle Stage", "Functional Subsystem", "Data Flow & Clinical Operations", "Guaranteed Outcome"]
    loop_rows = [
        ["1. Ingestion & Preprocessing", "EHR Ingestion Pipeline", "Extracts 47+ clinical attributes, normalizes labs, encodes 23 medications, computes polypharmacy index", "De-duplicated, imputed, feature-engineered patient tensor"],
        ["2. Risk Inference", "ML/DL Model Hub", "Dual-execution via XGBoost Clustered (0.9794 AUC) and PyTorch TabTransformer (0.9682 AUC)", "Calibrated 30-day readmission risk probability (0.00 – 1.00)"],
        ["3. Explainability & Triage", "TreeSHAP Engine", "Calculates exact Shapley values for top 10 biomarkers; sorts patients into priority triage queue", "Clinician-facing waterfall plot & automated SOAP discharge note draft"],
        ["4. Virtual Engagement", "WebRTC Telemedicine & CareAI", "Conducts encrypted 72-hour virtual check-in; provides bilingual patient guidance in Hindi/English", "Real-time vital sign check, medication adherence verification"],
        ["5. Digital Identity & Sync", "3D Digital Health ID", "Generates HMAC-SHA256 encrypted QR pass; syncs encounter history to decentralized health card", "Portability across outpatient clinics, pharmacies & caregivers"]
    ]
    flowables.append(make_table(loop_headers, loop_rows, col_widths=[95, 110, 200, 117]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "THE POWER OF CLOSED-LOOP CLINICAL AI",
        "A predictive model that is not coupled to automated clinical workflows fails to improve patient outcomes. By directly connecting "
        "risk scores to triage worklists, automated appointment scheduling, and bilingual patient communication, HRP Clinical converts "
        "raw algorithmic accuracy into tangible readmission reduction.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 14: Chapter 6 (User Personas & Clinical Journeys)
    # ==========================================
    flowables.append(Paragraph("Chapter 6 — User Personas, Clinical User Journeys & Workflow Integration", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "To ensure seamless adoption within fast-paced hospital workflows without contributing to clinician burnout, HRP Clinical "
        "was engineered around four distinct user personas and tailored clinical journeys:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph("<b>Persona 1: Dr. Elena Rostova — Inpatient Hospitalist & Attending Physician</b>", styles['BodyBold']))
    flowables.append(Paragraph(
        "• <i>Workflow Context</i>: Manages 18–22 acute diabetic and cardiopulmonary inpatients daily; conducts morning discharge rounds.<br/>"
        "• <i>HRP Clinical Experience</i>: Opens the Triage Portal to review patients flagged with Readmission Risk > 40%. Inspects the "
        "TreeSHAP waterfall to immediately identify that Patient #84920's risk is propelled by high glycemic load and an inpatient insulin "
        "titration change. Accepts the AI-drafted SOAP discharge summary, adjusts the home insulin regimen, and orders a 72h nurse check-in.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 3))

    flowables.append(Paragraph("<b>Persona 2: Sarah Jenkins, RN — Post-Discharge Nurse Care Coordinator</b>", styles['BodyBold']))
    flowables.append(Paragraph(
        "• <i>Workflow Context</i>: Responsible for coordinating post-discharge follow-ups for 60+ discharged patients weekly.<br/>"
        "• <i>HRP Clinical Experience</i>: Interacts with the 'High-Risk Priority Worklist', where patients are automatically ranked by "
        "risk severity. Clicks 'Launch Telemedicine' to initiate an encrypted WebRTC video call with Patient #84920 on Day 2 post-discharge. "
        "Verifies that the patient picked up their new glargine insulin prescription and confirms no hypoglycemic episodes.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 3))

    flowables.append(Paragraph("<b>Persona 3: Rajesh Sharma — Discharged Diabetic Patient (Age 64)</b>", styles['BodyBold']))
    flowables.append(Paragraph(
        "• <i>Workflow Context</i>: Discharged home after a 5-day stay for diabetic ketoacidosis; speaks conversational Hindi and basic English.<br/>"
        "• <i>HRP Clinical Experience</i>: Scans the QR code on his 3D Digital Health ID card using his smartphone. Opens the CareAI "
        "bilingual portal in Hindi. Asks CareAI: <i>'क्या मैं अपनी मेटफॉर्मिन की खुराक रात को ले सकता हूँ?'</i> CareAI confirms his discharge "
        "instructions in clear Hindi audio and text, alerting him to take it with his evening meal.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "COGNITIVE ERGONOMICS IN HEALTHCARE UI",
        "Physicians spend up to 4.5 hours daily navigating cumbersome EHR interfaces. HRP Clinical's interface delivers full risk "
        "stratification, SHAP attribution, and one-click actions in under <b>3 clicks and less than 15 seconds</b> per patient review.",
        kind="info"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 15: Chapter 7 (CareAI Conversational Core)
    # ==========================================
    flowables.append(Paragraph("Chapter 7 — CareAI Agent Core & Multilingual Conversational Triaging", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "<b>CareAI</b> is the intelligent conversational agent embedded directly into the patient portal and telemedicine suite. "
        "Engineered with a hybrid architecture combining rule-based clinical safety guardrails and transformer-based natural language "
        "understanding, CareAI provides 24/7 symptom triaging, medication guidance, and multilingual translation.", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph("<b>Core Capabilities of the CareAI Agent:</b>", styles['BodyBold']))
    flowables.append(Paragraph("1. <b>Bilingual Natural Language Processing (English & Hindi)</b>: Supports seamless code-switching between English, standard Hindi, and Hinglish, ensuring complete linguistic accessibility for diverse patient populations.", styles['Bullet']))
    flowables.append(Paragraph("2. <b>Clinical Intent Classification & Slot Filling</b>: Identifies medical inquiries spanning dosage instructions, drug interactions, red-flag symptoms (chest pain, shortness of breath, hypoglycemia), and appointment rescheduling.", styles['Bullet']))
    flowables.append(Paragraph("3. <b>Automated Emergency Escalation</b>: If a patient reports acute red-flag symptoms (e.g., blood glucose < 50 mg/dL or severe crushing chest pain), CareAI immediately overrides normal chatbot flow, displays a high-priority red alert, and prompts the patient to dial 911 / emergency services.", styles['Bullet']))
    flowables.append(Paragraph("4. <b>Text-to-Speech (TTS) Voice Synthesis</b>: Utilizes the browser Web Speech API to provide warm, clear auditory readouts of discharge instructions for visually impaired or elderly patients.", styles['Bullet']))
    flowables.append(Spacer(1, 6))

    careai_headers = ["User Prompt / Clinical Scenario", "Detected Intent", "CareAI Response & Safety Action"]
    careai_rows = [
        ["'I feel dizzy and my glucose meter shows 48 mg/dL'", "Hypoglycemia Emergency (Critical Red-Flag)", "<b>CRITICAL ALERT:</b> Consume 15g fast-acting carbs (fruit juice/glucose tabs) immediately. Recheck in 15 mins. If symptoms persist, call Emergency."],
        ["'मुझे अपनी दवाइयों की सूची देखनी है'", "Medication List Query (Hindi)", "आपके डिस्चार्ज के अनुसार: 1. मेटफॉर्मिन 500mg (दिन में 2 बार भोजन के साथ), 2. इंसुलिन ग्लार्गिन 20 यूनिट (रात को)."],
        ["'When is my next doctor appointment?'", "Schedule Query", "Your follow-up telemedicine consultation with Dr. Rostova is scheduled for tomorrow at 2:00 PM EST."],
        ["'Can I eat grapefruit with my statin?'", "Drug-Food Interaction", "Caution: Grapefruit inhibits CYP3A4 metabolism of Atorvastatin, increasing drug toxicity risk. Avoid consuming grapefruit."]
    ]
    flowables.append(make_table(careai_headers, careai_rows, col_widths=[140, 120, 262]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "CLINICAL SAFETY GUARDRAILS IN CONVERSATIONAL AI",
        "CareAI enforces deterministic medical boundary checking. It is programmatically prevented from prescribing new medications, "
        "altering physician-ordered dosages, or offering unverified herbal alternatives.",
        kind="alert"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 16: Chapter 8 (End-to-End System Blueprint)
    # ==========================================
    flowables.append(Paragraph("Chapter 8 — End-to-End System Architecture Blueprint & Microservices", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "The Hospital Readmission Predictor is structured as a decoupled, event-driven, 4-tier microservices architecture "
        "designed for sub-second inference latency, horizontal scalability, and enterprise-grade clinical reliability:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    # Embed the architecture diagram
    arch_img_path = os.path.join(ASSETS_DIR, "system_microservices_arch.png")
    if os.path.exists(arch_img_path):
        flowables.append(Image(arch_img_path, width=520, height=230))
        flowables.append(Spacer(1, 6))

    flowables.append(Paragraph("<b>Detailed Breakdown of the 4 Architectural Layers:</b>", styles['BodyBold']))
    flowables.append(Paragraph(
        "• <b>Layer 1 (Ingestion & Normalization)</b>: FastAPI endpoints receive JSON/FHIR payloads; validates clinical types via Pydantic; "
        "imputes missing laboratory telemetry and computes derived polypharmacy features.<br/>"
        "• <b>Layer 2 (AI Inference & Explainability Core)</b>: Houses serialized XGBoost booster binaries (0.9794 AUC) and PyTorch "
        "FT-Transformer weights. Computes exact TreeSHAP attribution matrices in under 12 milliseconds.<br/>"
        "• <b>Layer 3 (Data Orchestration & Caching)</b>: PostgreSQL 16 database storing patient encounters, audit logs, and SOAP notes; "
        "Redis 7.2 distributed cache managing JWT session tokens and rate-limiting counters.<br/>"
        "• <b>Layer 4 (Clinical Frontend & Engagement)</b>: Responsive web application providing the Physician Triage Portal, WebRTC "
        "video consultation engine, CareAI bilingual chatbot, and Three.js 3D cryptographic health card renderer.",
        styles['Body']
    ))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "SCALABILITY & THROUGHPUT CAPABILITIES",
        "The FastAPI asynchronous inference core delivers <b>> 1,200 inferences/second</b> on standard 4-core cloud instances, "
        "capable of serving enterprise health systems processing hundreds of simultaneous hospital discharges.",
        kind="info"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 17: Part II Synthesis & Transition to Data Engineering
    # ==========================================
    flowables.append(Paragraph("Part II Synthesis: Architectural Synergy & Next Steps", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "The architectural synergy of HRP Clinical resides in the frictionless harmony between predictive precision and operational execution. "
        "The table below details how data flows across components during a live hospital discharge event:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    flow_headers = ["Time Offset", "Originating Component", "Target Component", "Operational Payload & Action"]
    flow_rows = [
        ["T - 24 Hours", "Inpatient Lab / EHR", "FastAPI Ingestion", "Daily blood panel, vital sign log & medication adjustment pushed to HRP API"],
        ["T - 4 Hours", "HRP Inference Core", "Physician Dashboard", "Dual XGBoost + TreeSHAP run; Risk Score: 0.68 (High); Top driver: Insulin titration"],
        ["T - 2 Hours", "Attending Physician", "Document Engine", "Physician reviews SHAP waterfall, accepts SOAP note draft, prescribes 72h tele-visit"],
        ["T - 0 Hours (Discharge)", "QR Cryptographic Engine", "Patient Portal / Card", "Issues 3D Digital Health ID card containing HMAC-SHA256 encrypted discharge token"],
        ["T + 48 Hours", "Care Coordinator", "WebRTC Telemedicine", "Conducts virtual follow-up; CareAI logs adherence status; risk downgraded to 0.18"]
    ]
    flowables.append(make_table(flow_headers, flow_rows, col_widths=[85, 110, 115, 212]))
    flowables.append(Spacer(1, 8))

    flowables.append(make_callout(
        "ENTERING THE DATA FOUNDATION",
        "With the complete product blueprint established, we now transition to <b>Part III: Clinical Data Engineering & EHR Ingestion</b> "
        "to deconstruct the 101,766 inpatient encounter dataset, explore missingness strategies, and detail our mathematical feature engineering.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    return flowables

print("sec04_part02_product loaded.")
