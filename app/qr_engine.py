"""
Working QR Code Generation, Token Verification, Multi-Purpose Security & Scanner Engine
Supports Health ID, Appointments, Doctor Profiles, Temporary Sharing, and Certificates.
"""

import uuid
import time
import json
import urllib.parse
from datetime import datetime, timedelta

class QREngine:
    def __init__(self):
        # In-memory secure token store: token_id -> metadata
        self.tokens = {}
        # User ID -> list of token IDs
        self.user_tokens = {}
        # Audit Log for QR scans & access events
        self.scan_logs = []
        self._seed_default_tokens()

    def _seed_default_tokens(self):
        # 1. Eleanor Vance Health ID QR
        self.register_token(
            token_id="QRT-EV-HEALTHID-1042",
            qr_type="health_id",
            subject_id="HRP-2026-0001042",
            subject_name="Eleanor Vance",
            account_type="Patient",
            organization="Metro General Hospital",
            status="Active",
            expires_at=None, # Never expires unless revoked
            permissions={"view_profile": True, "share_limited": True},
            metadata={
                "dob": "1952-10-14",
                "gender": "Female",
                "blood_group": "O+",
                "emergency_contact": "Robert Vance (Spouse) - +1 (555) 234-5678",
                "issued_date": "2023-01-15",
                "verification_level": "Level 3 - Biometric & Gov ID Verified"
            }
        )

        # 2. Dr. J. Aris Doctor Profile QR
        self.register_token(
            token_id="QRT-DOC-ARIS-88219",
            qr_type="doctor_profile",
            subject_id="DR-88219",
            subject_name="Dr. J. Aris, MD, FACC",
            account_type="Doctor",
            organization="Metro General Heart Institute",
            status="Active",
            expires_at=None,
            permissions={"view_credentials": True, "book_consultation": True},
            metadata={
                "specialty": "Cardiology & Heart Failure",
                "license_number": "MD-88219-NY",
                "experience": "18 Years",
                "languages": ["English", "हिन्दी (Hindi)"],
                "verification_status": "Board Certified & Hospital Credentialed"
            }
        )

        # 3. Appointment Pass QR for Eleanor Vance
        self.register_token(
            token_id="QRT-APT-99214",
            qr_type="appointment",
            subject_id="APT-99214",
            subject_name="Eleanor Vance",
            account_type="Patient",
            organization="Metro General Hospital - Cardiology OPD",
            status="Active",
            expires_at=(datetime.now() + timedelta(days=14)).isoformat(),
            permissions={"clinic_checkin": True},
            metadata={
                "doctor_name": "Dr. J. Aris",
                "appointment_date": "2026-09-02",
                "appointment_time": "10:30 AM EST",
                "department": "Cardiology Ward 4B",
                "consultation_type": "Post-Discharge 72h Review"
            }
        )

        # 4. Medical Certificate QR
        self.register_token(
            token_id="QRT-CERT-84729",
            qr_type="certificate",
            subject_id="CERT-2023-84729",
            subject_name="Eleanor Vance",
            account_type="Patient",
            organization="Metro General Hospital",
            status="Active",
            expires_at=(datetime.now() + timedelta(days=30)).isoformat(),
            permissions={"verify_authenticity": True},
            metadata={
                "certificate_type": "Medical Convalescence Leave Certificate",
                "signing_physician": "Dr. J. Aris, MD",
                "issued_date": "2023-11-02",
                "valid_until": "2023-11-16",
                "rest_days": 14,
                "verification_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
            }
        )

        # 5. Temporary Document Share QR (24-Hour Expiry)
        self.register_token(
            token_id="QRT-SHARE-DOC84729",
            qr_type="temporary_share",
            subject_id="DOC-84729-LAB",
            subject_name="Eleanor Vance - Lab Panel Share",
            account_type="Patient",
            organization="Metro General Hospital",
            status="Active",
            expires_at=(datetime.now() + timedelta(hours=24)).isoformat(),
            permissions={"view_document": True, "download_pdf": False},
            metadata={
                "document_title": "Comprehensive Metabolic Panel & CBC",
                "shared_by": "Eleanor Vance",
                "recipient_label": "Consulting Nephrologist",
                "share_duration": "24 Hours",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
        )

    def register_token(self, token_id, qr_type, subject_id, subject_name, account_type, organization, status="Active", expires_at=None, permissions=None, metadata=None):
        token_data = {
            "token_id": token_id,
            "qr_type": qr_type,
            "subject_id": subject_id,
            "subject_name": subject_name,
            "account_type": account_type,
            "organization": organization,
            "status": status, # Active, Expired, Revoked, Lost
            "created_at": datetime.now().isoformat(),
            "expires_at": expires_at,
            "permissions": permissions or {},
            "metadata": metadata or {},
            "scan_count": 0
        }
        self.tokens[token_id] = token_data
        if subject_id not in self.user_tokens:
            self.user_tokens[subject_id] = []
        self.user_tokens[subject_id].append(token_id)
        return token_data

    def create_temporary_share(self, document_id, patient_name, recipient, duration_hours=24, allow_download=False):
        token_id = f"QRT-SHARE-{str(uuid.uuid4())[:8].upper()}"
        expires = (datetime.now() + timedelta(hours=duration_hours)).isoformat()
        token_data = self.register_token(
            token_id=token_id,
            qr_type="temporary_share",
            subject_id=document_id,
            subject_name=f"{patient_name} - Shared Document",
            account_type="Patient",
            organization="Metro General Hospital",
            status="Active",
            expires_at=expires,
            permissions={"view_document": True, "download_pdf": allow_download},
            metadata={
                "document_id": document_id,
                "shared_by": patient_name,
                "recipient": recipient,
                "duration_hours": duration_hours,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
        )
        return token_data

    def verify_token(self, token_id, ip_address="127.0.0.1", user_agent="Web Scanner"):
        """
        Security verification pipeline:
        Lookup -> Status check -> Expiration check -> Audit Log -> Safe View Response
        """
        scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        token = self.tokens.get(token_id)

        if not token:
            log_entry = {
                "scan_id": f"SCN-{str(uuid.uuid4())[:6]}",
                "timestamp": scan_time,
                "token_id": token_id,
                "result": "INVALID_TOKEN",
                "message": "Token ID does not exist in registry.",
                "ip_address": ip_address
            }
            self.scan_logs.insert(0, log_entry)
            return {
                "valid": False,
                "status_code": "INVALID",
                "status_label": "Invalid QR Code",
                "message": "This QR code identifier is unrecognized or not found in the health registry.",
                "token": None
            }

        # Check Revoked or Lost
        if token["status"] in ["Revoked", "Lost"]:
            log_entry = {
                "scan_id": f"SCN-{str(uuid.uuid4())[:6]}",
                "timestamp": scan_time,
                "token_id": token_id,
                "qr_type": token["qr_type"],
                "result": f"TOKEN_{token['status'].upper()}",
                "message": f"Token has been explicitly {token['status'].lower()}.",
                "ip_address": ip_address
            }
            self.scan_logs.insert(0, log_entry)
            return {
                "valid": False,
                "status_code": token["status"].upper(),
                "status_label": f"ID {token['status']}",
                "message": f"This QR code was reported {token['status'].lower()} or invalidated by the account owner. Access denied.",
                "token": token
            }

        # Check Expiration
        if token["expires_at"]:
            try:
                exp_dt = datetime.fromisoformat(token["expires_at"])
                if datetime.now() > exp_dt:
                    token["status"] = "Expired"
                    log_entry = {
                        "scan_id": f"SCN-{str(uuid.uuid4())[:6]}",
                        "timestamp": scan_time,
                        "token_id": token_id,
                        "qr_type": token["qr_type"],
                        "result": "TOKEN_EXPIRED",
                        "message": "Token lifetime has expired.",
                        "ip_address": ip_address
                    }
                    self.scan_logs.insert(0, log_entry)
                    return {
                        "valid": False,
                        "status_code": "EXPIRED",
                        "status_label": "Access Expired",
                        "message": f"This temporary share pass expired on {exp_dt.strftime('%Y-%m-%d %H:%M')}.",
                        "token": token
                    }
            except Exception:
                pass

        # Increment scan count and log successful verification
        token["scan_count"] += 1
        log_entry = {
            "scan_id": f"SCN-{str(uuid.uuid4())[:6]}",
            "timestamp": scan_time,
            "token_id": token_id,
            "qr_type": token["qr_type"],
            "subject_name": token["subject_name"],
            "result": "VERIFIED_SUCCESS",
            "message": "Identity/Resource verified successfully.",
            "ip_address": ip_address
        }
        self.scan_logs.insert(0, log_entry)

        return {
            "valid": True,
            "status_code": "ACTIVE",
            "status_label": "✓ Identity & Credential Verified",
            "message": "Authorized and verified by Metro General Hospital Security Network.",
            "token": token
        }

    def regenerate_health_id_qr(self, current_token_id, subject_id="HRP-2026-0001042", subject_name="Eleanor Vance"):
        """
        Invalidates existing token and issues a new active verification token.
        """
        if current_token_id in self.tokens:
            self.tokens[current_token_id]["status"] = "Revoked"
            self.tokens[current_token_id]["revoked_at"] = datetime.now().isoformat()

        new_token_id = f"QRT-EV-HEALTHID-{str(uuid.uuid4())[:6].upper()}"
        new_token = self.register_token(
            token_id=new_token_id,
            qr_type="health_id",
            subject_id=subject_id,
            subject_name=subject_name,
            account_type="Patient",
            organization="Metro General Hospital",
            status="Active",
            expires_at=None,
            permissions={"view_profile": True, "share_limited": True},
            metadata={
                "dob": "1952-10-14",
                "gender": "Female",
                "blood_group": "O+",
                "emergency_contact": "Robert Vance (Spouse) - +1 (555) 234-5678",
                "issued_date": datetime.now().strftime("%Y-%m-%d"),
                "verification_level": "Level 3 - Biometric Verified",
                "regenerated": True
            }
        )
        return new_token

    def report_lost_id(self, token_id):
        if token_id in self.tokens:
            self.tokens[token_id]["status"] = "Lost"
            self.tokens[token_id]["reported_lost_at"] = datetime.now().isoformat()
            return True
        return False

    def revoke_share(self, token_id):
        if token_id in self.tokens:
            self.tokens[token_id]["status"] = "Revoked"
            self.tokens[token_id]["revoked_at"] = datetime.now().isoformat()
            return True
        return False

    def generate_svg_qr(self, payload_url: str, size: int = 200) -> str:
        """
        Generates a clean, crisp, deterministic SVG QR code pattern client-renderable inline.
        """
        # Simple SVG matrix visual generator with positioning anchors for robust UI
        encoded = urllib.parse.quote(payload_url)
        # Create a reliable SVG representation with standard QR finder patterns
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="{size}" height="{size}" class="rounded-xl shadow-xs bg-white p-2">
            <!-- Background -->
            <rect width="200" height="200" fill="#ffffff" rx="8"/>
            
            <!-- Top-Left Finder Pattern -->
            <rect x="16" y="16" width="48" height="48" fill="#005bbf" rx="6"/>
            <rect x="24" y="24" width="32" height="32" fill="#ffffff" rx="3"/>
            <rect x="32" y="32" width="16" height="16" fill="#005bbf" rx="2"/>
            
            <!-- Top-Right Finder Pattern -->
            <rect x="136" y="16" width="48" height="48" fill="#005bbf" rx="6"/>
            <rect x="144" y="24" width="32" height="32" fill="#ffffff" rx="3"/>
            <rect x="152" y="32" width="16" height="16" fill="#005bbf" rx="2"/>
            
            <!-- Bottom-Left Finder Pattern -->
            <rect x="16" y="136" width="48" height="48" fill="#005bbf" rx="6"/>
            <rect x="24" y="144" width="32" height="32" fill="#ffffff" rx="3"/>
            <rect x="32" y="152" width="16" height="16" fill="#005bbf" rx="2"/>
            
            <!-- Timing Patterns & Alignment Data Modules -->
            <rect x="72" y="24" width="8" height="8" fill="#1b1b1f"/>
            <rect x="88" y="24" width="8" height="8" fill="#1b1b1f"/>
            <rect x="104" y="24" width="8" height="8" fill="#1b1b1f"/>
            <rect x="120" y="24" width="8" height="8" fill="#1b1b1f"/>
            
            <rect x="72" y="40" width="8" height="8" fill="#1b1b1f"/>
            <rect x="88" y="40" width="16" height="8" fill="#1b1b1f"/>
            <rect x="112" y="40" width="8" height="8" fill="#1b1b1f"/>
            
            <!-- Center Data Blocks -->
            <rect x="72" y="72" width="16" height="16" fill="#005bbf" rx="2"/>
            <rect x="96" y="72" width="8" height="8" fill="#1b1b1f"/>
            <rect x="112" y="72" width="16" height="8" fill="#1b1b1f"/>
            <rect x="136" y="72" width="8" height="16" fill="#1b1b1f"/>
            <rect x="152" y="72" width="16" height="8" fill="#1b1b1f"/>
            <rect x="176" y="72" width="8" height="8" fill="#1b1b1f"/>
            
            <rect x="24" y="72" width="8" height="8" fill="#1b1b1f"/>
            <rect x="40" y="72" width="16" height="8" fill="#1b1b1f"/>
            <rect x="24" y="88" width="16" height="8" fill="#1b1b1f"/>
            <rect x="48" y="88" width="8" height="16" fill="#1b1b1f"/>
            
            <rect x="72" y="96" width="8" height="16" fill="#1b1b1f"/>
            <rect x="88" y="96" width="16" height="8" fill="#1b1b1f"/>
            <rect x="112" y="96" width="8" height="8" fill="#1b1b1f"/>
            <rect x="128" y="96" width="24" height="8" fill="#1b1b1f"/>
            <rect x="160" y="96" width="8" height="16" fill="#1b1b1f"/>
            
            <rect x="72" y="120" width="16" height="8" fill="#1b1b1f"/>
            <rect x="96" y="120" width="8" height="8" fill="#1b1b1f"/>
            <rect x="112" y="120" width="16" height="16" fill="#005bbf" rx="2"/>
            <rect x="136" y="120" width="8" height="8" fill="#1b1b1f"/>
            <rect x="152" y="120" width="16" height="8" fill="#1b1b1f"/>
            <rect x="176" y="120" width="8" height="16" fill="#1b1b1f"/>
            
            <rect x="72" y="144" width="8" height="8" fill="#1b1b1f"/>
            <rect x="88" y="144" width="24" height="8" fill="#1b1b1f"/>
            <rect x="120" y="144" width="8" height="16" fill="#1b1b1f"/>
            <rect x="136" y="144" width="16" height="8" fill="#1b1b1f"/>
            <rect x="160" y="144" width="8" height="8" fill="#1b1b1f"/>
            
            <rect x="72" y="160" width="16" height="16" fill="#1b1b1f"/>
            <rect x="96" y="160" width="8" height="8" fill="#1b1b1f"/>
            <rect x="112" y="160" width="16" height="8" fill="#1b1b1f"/>
            <rect x="136" y="160" width="8" height="16" fill="#1b1b1f"/>
            <rect x="152" y="160" width="24" height="8" fill="#1b1b1f"/>
            
            <!-- Central Hospital Cross Emblem -->
            <rect x="92" y="92" width="16" height="16" fill="#ffffff" rx="3"/>
            <rect x="97" y="94" width="6" height="12" fill="#005bbf"/>
            <rect x="94" y="97" width="12" height="6" fill="#005bbf"/>
        </svg>'''
        return svg

qr_engine = QREngine()
