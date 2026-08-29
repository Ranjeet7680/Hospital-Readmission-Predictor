"""
Pages 64 to 68: Part XI — Healthcare Security, HIPAA/HITECH & RBAC
"""
import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from ebook_core import create_styles, make_callout, make_table, make_code_box, C_PRIMARY, C_SECONDARY, C_DARK, C_LIGHT_BG

def get_pages_064_068_part11():
    styles = create_styles()
    flowables = []

    # ==========================================
    # PAGE 64: Part XI Header & Chapter 41 (Zero-Trust Healthcare Security)
    # ==========================================
    flowables.append(Paragraph("PART XI — HEALTHCARE SECURITY, HIPAA/HITECH & RBAC", styles['PartHeader']))
    flowables.append(Paragraph("Chapter 41 — Healthcare Threat Modeling & Zero-Trust Clinical Architecture", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "Healthcare data breaches cost an average of <b>$10.93 Million per incident</b>—higher than any other industry. "
        "Because HRP Clinical processes electronic Protected Health Information (ePHI) spanning diagnostic ICD codes, "
        "laboratory telemetry, and real-time video consultations, the platform is engineered under a strict <b>Zero-Trust Security Architecture</b>: "
        "<i>'Never Trust, Always Verify'</i>.", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    threat_headers = ["Potential Attack Vector", "Clinical Risk & Threat Magnitude", "HRP Zero-Trust Mitigation Defense"]
    threat_rows = [
        ["Unauthorized ePHI Access", "Data theft; violation of HIPAA Privacy Rule", "Granular Role-Based Access Control (RBAC) + JWT Claims Verification"],
        ["Man-in-the-Middle (MITM)", "Eavesdropping on live tele-triage consultations", "Mandatory TLS 1.3 for REST/WSS + DTLS-SRTP for WebRTC media streams"],
        ["Token Forgery / Tampering", "Malicious modification of patient risk scores or discharge orders", "HMAC-SHA256 digital signatures with rotating server salt keys"],
        ["Data at Rest Breach", "Direct exfiltration of database files from cloud servers", "AES-256-GCM encryption with Customer-Managed Keys (CMK) via AWS KMS / Vault"],
        ["Credential Stuffing / Brute Force", "Takeover of physician portal accounts", "Enforced Multi-Factor Authentication (MFA) + Redis Sliding-Window Rate Limiting"]
    ]
    flowables.append(make_table(threat_headers, threat_rows, col_widths=[130, 165, 227]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "ZERO-TRUST IDENTITY VERIFICATION",
        "Every incoming HTTP request and WebSocket frame is validated for active cryptographic claims, user permissions, and "
        "IP reputation before executing any model inference or database query.",
        kind="alert"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 65: Chapter 42 (Role-Based Access Control - RBAC)
    # ==========================================
    flowables.append(Paragraph("Chapter 42 — Role-Based Access Control (RBAC) & Granular Permissions", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "HRP Clinical enforces a strict 4-tier Role-Based Access Control (RBAC) matrix defining exact operational boundaries "
        "across clinical, administrative, and patient roles:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    rbac_headers = ["System Capability / Action", "Attending Physician", "Nurse Coordinator", "Discharged Patient", "Hospital Executive / CMO"]
    rbac_rows = [
        ["View Patient Risk Score & SHAP Waterfall", "FULL ACCESS", "FULL ACCESS", "SIMPLIFIED SUMMARY", "AGGREGATE METRICS ONLY"],
        ["Modify Medication & Discharge Orders", "FULL ACCESS", "READ ONLY", "NO ACCESS", "NO ACCESS"],
        ["Sign and Finalize SOAP Discharge Note", "FULL ACCESS", "DRAFT ONLY", "NO ACCESS", "NO ACCESS"],
        ["Launch Telemedicine Video Call", "FULL ACCESS", "FULL ACCESS", "RECEIVE CALL ONLY", "NO ACCESS"],
        ["Access 3D Digital Health ID Card", "VERIFY TOKEN", "VERIFY TOKEN", "FULL ACCESS (OWN CARD)", "NO ACCESS"],
        ["View Departmental Readmission Analytics", "DEPARTMENT LEVEL", "WORKLIST ONLY", "NO ACCESS", "HOSPITAL-WIDE ACCESS"],
        ["Retrain / Deploy Production ML Models", "NO ACCESS", "NO ACCESS", "NO ACCESS", "MLOps ADMIN ONLY"]
    ]
    flowables.append(make_table(rbac_headers, rbac_rows, col_widths=[142, 95, 95, 95, 95]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "LEAST PRIVILEGE PRINCIPLE (HIPAA § 164.312)",
        "By restricting ePHI visibility to the exact minimum necessary for clinical care, HRP Clinical eliminates insider data leakage "
        "and satisfies HIPAA Minimum Necessary standards.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 66: Chapter 43 (JWT Authentication & Security Code)
    # ==========================================
    flowables.append(Paragraph("Chapter 43 — Asymmetric JWT Authentication & Security Implementation", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "Below is the production FastAPI authentication middleware utilizing RS256 asymmetric JWT signing and granular role verification:",
        styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    auth_code = """from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

def require_clinical_role(allowed_roles: list[str]):
    \"\"\"Enforces granular RBAC verification on FastAPI endpoints\"\"\"
    def role_checker(credentials: HTTPAuthorizationCredentials = Security(security)):
        token = credentials.credentials
        try:
            # Decode and verify JWT with RSA Public Key
            payload = jwt.decode(token, PUBLIC_RSA_KEY, algorithms=["RS256"], audience="hrp-clinical-api")
            user_role = payload.get("role")
            
            if user_role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access forbidden: User role '{user_role}' lacks required permissions {allowed_roles}"
                )
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token signature expired")
        except jwt.PyJWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization token")
            
    return role_checker"""
    flowables.append(make_code_box(auth_code, "FastAPI Asymmetric RBAC Middleware", width=522))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "SHORT-LIVED TOKENS & SECURE REFRESH CYCLES",
        "Access tokens carry a 15-minute expiration window. Refresh tokens are stored in HttpOnly, SameSite=Strict encrypted cookies, "
        "completely neutralizing Cross-Site Scripting (XSS) and CSRF token theft.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 67: Chapter 44 (HIPAA, HITECH & Audit Logging)
    # ==========================================
    flowables.append(Paragraph("Chapter 44 — Comprehensive HIPAA, HITECH & Immutable Audit Logging", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "HIPAA § 164.312(b) mandates that health information systems record and examine all activity in systems containing or using ePHI. "
        "HRP Clinical implements an <b>Immutable Clinical Audit Log Engine</b> recording every patient record access, ML inference, "
        "and telemedicine consultation in an append-only, cryptographically chained audit ledger:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    audit_headers = ["Timestamp (UTC)", "Actor (User ID & Role)", "Patient UHID", "Action Performed", "Audit SHA-256 Hash"]
    audit_rows = [
        ["2026-08-26 09:14:02", "dr_rostova (PHYSICIAN)", "UHID-84920", "Inference & SHAP Waterfall Generated (Risk: 0.65)", "e3b0c44298fc1c14..."],
        ["2026-08-26 09:18:45", "dr_rostova (PHYSICIAN)", "UHID-84920", "SOAP Discharge Note Signed & Finalized", "8f434346648f6b96..."],
        ["2026-08-26 11:30:10", "nurse_jenkins (COORDINATOR)", "UHID-84920", "Digital Health ID QR Token Issued (TTL: 72h)", "384b0293847291aa..."],
        ["2026-08-28 14:02:15", "nurse_jenkins (COORDINATOR)", "UHID-84920", "WebRTC Tele-Triage Call Completed (Duration: 14m)", "1a8f92b7c4d5e6f1..."],
        ["2026-08-28 14:16:30", "careai_agent (SYSTEM)", "UHID-84920", "Post-Call Vital Telemetry Logged (Risk: 0.18)", "d7a8fbb307d78094..."]
    ]
    flowables.append(make_table(audit_headers, audit_rows, col_widths=[105, 115, 75, 140, 87]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "CRYPTOGRAPHIC CHAIN OF CUSTODY",
        "Each audit log entry contains a SHA-256 hash of the preceding record, creating a tamper-evident blockchain-like chain of custody "
        "that guarantees audit trail integrity during federal HIPAA compliance inspections.",
        kind="info"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 68: Part XI Summary & Transition to Analytics
    # ==========================================
    flowables.append(Paragraph("Part XI Synthesis: Security & Governance Architecture Summary", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "Part XI has detailed the comprehensive security posture of HRP Clinical, demonstrating full alignment with HIPAA, HITECH, "
        "and zero-trust cybersecurity standards. The table below summarizes our security engineering architecture:", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    sec_sum_headers = ["Security Domain", "Implemented Technical Standard", "Regulatory Compliance Mapping"]
    sec_sum_rows = [
        ["Authentication", "Asymmetric RS256 JWT with 15-minute TTL & HttpOnly Cookies", "HIPAA § 164.312(d) Person Authentication"],
        ["Authorization", "4-Tier Granular RBAC Middleware on FastAPI Endpoints", "HIPAA § 164.312(a)(1) Access Control"],
        ["Data in Transit", "TLS 1.3 for REST/WSS; DTLS-SRTP AES-256-GCM for WebRTC", "HIPAA § 164.312(e)(1) Transmission Security"],
        ["Data at Rest", "PostgreSQL Transparent Data Encryption (TDE) AES-256", "HIPAA § 164.312(a)(2)(iv) Encryption at Rest"],
        ["Audit Integrity", "SHA-256 Hash-Chained Immutable Event Ledger", "HIPAA § 164.312(b) Audit Controls & HITECH Rule"]
    ]
    flowables.append(make_table(sec_sum_headers, sec_sum_rows, col_widths=[110, 195, 217]))
    flowables.append(Spacer(1, 8))

    flowables.append(make_callout(
        "TRANSITIONING TO REAL-TIME CLINICAL ANALYTICS",
        "With clinical security and access control established, hospital leadership requires macro-level operational visibility. "
        "In <b>Part XII: Real-Time Clinical Analytics & Executive Dashboards</b>, we construct departmental readmission heatmaps, "
        "KPI tracking suites, and MLOps model drift monitors.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    return flowables

print("sec13_part11_auth loaded.")
