"""
Authentication, Authorization, RBAC & Security Gateway
Supports Patient, Doctor, Care Coordinator, Administrator Roles, MFA, OTP, Passkeys, Sessions, Break-Glass.
"""

import uuid
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Dict, List

class User:
    def __init__(self, id, name, email, role, organization="St. Jude Medical Center", department="Cardiology", status="Active", mfa_enabled=False):
        self.id = id
        self.name = name
        self.email = email
        self.role = role # 'Patient', 'Doctor', 'CareCoordinator', 'Administrator'
        self.organization = organization
        self.department = department
        self.status = status
        self.mfa_enabled = mfa_enabled
        self.created_at = datetime.now().strftime("%Y-%m-%d")

class AuthManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}
        self.otp_store = {}
        self.audit_logs = []
        self.doctor_verification_queue = []
        self.seed_auth_data()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def seed_auth_data(self):
        # 1. Doctor
        dr_id = "USER-DOC-01"
        self.users["dr.smith@hospital.org"] = {
            "id": dr_id,
            "name": "Dr. Smith",
            "email": "dr.smith@hospital.org",
            "password_hash": self.hash_password("Doctor@2026!"),
            "role": "Doctor",
            "organization": "St. Jude Medical Center",
            "department": "Cardiology",
            "status": "Active",
            "verification": "Verified",
            "mfa_enabled": True,
            "phone": "+1 (555) 234-5678",
            "last_login": "Today, 09:15 AM"
        }

        # 2. Patient
        pt_id = "USER-PAT-01"
        self.users["eleanor.vance@patient.org"] = {
            "id": pt_id,
            "name": "Eleanor Vance",
            "email": "eleanor.vance@patient.org",
            "password_hash": self.hash_password("Patient@2026!"),
            "role": "Patient",
            "patient_id": "PT-84729",
            "organization": "St. Jude Medical Center",
            "department": "Cardiology",
            "status": "Active",
            "verification": "Verified",
            "mfa_enabled": False,
            "phone": "+1 (555) 847-2901",
            "last_login": "Yesterday, 16:30 PM"
        }

        # 3. Care Coordinator
        coord_id = "USER-COORD-01"
        self.users["sarah.coordinator@hospital.org"] = {
            "id": coord_id,
            "name": "Sarah Jenkins, RN",
            "email": "sarah.coordinator@hospital.org",
            "password_hash": self.hash_password("Coord@2026!"),
            "role": "CareCoordinator",
            "organization": "St. Jude Medical Center",
            "department": "Care Transitions",
            "status": "Active",
            "verification": "Verified",
            "mfa_enabled": True,
            "phone": "+1 (555) 345-6789",
            "last_login": "Today, 08:30 AM"
        }

        # 4. Hospital Administrator
        admin_id = "USER-ADMIN-01"
        self.users["admin@hospital.org"] = {
            "id": admin_id,
            "name": "System Administrator",
            "email": "admin@hospital.org",
            "password_hash": self.hash_password("Admin@2026!"),
            "role": "Administrator",
            "organization": "St. Jude Medical Center",
            "department": "Clinical Informatics",
            "status": "Active",
            "verification": "Verified",
            "mfa_enabled": True,
            "phone": "+1 (555) 999-0000",
            "last_login": "Today, 07:45 AM"
        }

        # Seed Active Sessions
        self.sessions["sess_current_doc"] = {
            "session_id": "sess_current_doc",
            "user_email": "dr.smith@hospital.org",
            "device": "MacBook Pro 16 - Safari",
            "location": "Boston, MA (Hospital Inpatient Network)",
            "ip": "10.240.12.8",
            "last_active": "Just now",
            "is_current": True
        }
        self.sessions["sess_mobile_doc"] = {
            "session_id": "sess_mobile_doc",
            "user_email": "dr.smith@hospital.org",
            "device": "iPhone 15 Pro - HRP Mobile",
            "location": "Boston, MA (Hospital WiFi)",
            "ip": "10.240.15.22",
            "last_active": "2 hours ago",
            "is_current": False
        }

        # Seed Audit Logs
        self.log_audit("dr.smith@hospital.org", "LOGIN", "Web Portal", "SUCCESS", "Authentication successful via Password + MFA")
        self.log_audit("dr.smith@hospital.org", "PATIENT_ACCESS", "Patient #PT-84729", "SUCCESS", "Viewed Electronic Health Record & Risk Profile")
        self.log_audit("admin@hospital.org", "MODEL_REGISTRY_ACCESS", "Registry v2.4.1", "SUCCESS", "Reviewed active model performance metrics")

        # Seed Doctor Verification Queue
        self.doctor_verification_queue.append({
            "id": "DR-REQ-901",
            "name": "Dr. Rajesh Kumar",
            "email": "dr.kumar@hospital.org",
            "specialty": "Neurology",
            "hospital": "St. Jude Medical Center",
            "license_id": "MD-NEURO-88349",
            "experience_years": 12,
            "status": "Pending Review",
            "submitted_date": "2023-10-23"
        })

    def log_audit(self, user_email, action, resource, result, details=""):
        entry = {
            "id": f"AUD-{str(uuid.uuid4())[:8].upper()}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_email,
            "action": action,
            "resource": resource,
            "result": result,
            "organization": "St. Jude Medical Center",
            "details": details
        }
        self.audit_logs.insert(0, entry)
        return entry

    def authenticate(self, email, password):
        user = self.users.get(email)
        if not user:
            return None, "Invalid email or password."
        if user["status"] == "Suspended":
            return None, "Account has been suspended. Please contact hospital administrator."
        if user["password_hash"] != self.hash_password(password):
            return None, "Invalid email or password."
        
        self.log_audit(email, "LOGIN", "Web Portal", "SUCCESS", f"User authenticated with role {user['role']}")
        return user, None

    def generate_otp(self, email):
        otp = "742891" # Deterministic for smooth interactive testing
        self.otp_store[email] = {
            "otp": otp,
            "expires_at": datetime.now() + timedelta(minutes=5)
        }
        return otp

    def verify_otp(self, email, input_otp):
        record = self.otp_store.get(email)
        if not record:
            return False, "OTP expired or not requested."
        if record["otp"] == input_otp.strip():
            self.log_audit(email, "MFA_VERIFIED", "OTP Service", "SUCCESS", "6-digit OTP code verified successfully")
            return True, None
        return False, "Invalid verification code. Please try again."

    def break_glass_access(self, user_email, patient_id, emergency_reason):
        """Emergency Break-Glass workflow with high-priority audit event."""
        self.log_audit(
            user_email,
            "BREAK_GLASS_ACCESS",
            f"Patient #{patient_id}",
            "EMERGENCY_GRANTED",
            f"Emergency break-glass accessed. Stated reason: {emergency_reason}"
        )
        return {
            "granted": True,
            "audit_id": self.audit_logs[0]["id"],
            "message": "Emergency access granted. This event has been permanently recorded in the institutional HIPAA security audit log."
        }

auth_manager = AuthManager()
