"""
Comprehensive Account, Profile, Settings, Privacy, Device & Identity Manager
Unifies Profile, Role Switching, Emergency Contacts, CareAI Permissions, and Data Export.
"""

import uuid
import json
from datetime import datetime, timedelta

class AccountManager:
    def __init__(self):
        # Master User Profile State (Eleanor Vance - Featured Patient)
        self.profile = {
            "id": "PT-84729",
            "health_id": "HRP-2026-0001042",
            "full_name": "Eleanor Vance",
            "initials": "EV",
            "email": "eleanor.vance@patient.org",
            "phone": "+1 (555) 382-9104",
            "dob": "1952-10-14",
            "age": 71,
            "gender": "Female",
            "blood_group": "O+",
            "address": "452 Elmwood Terrace, Apt 3B, New York, NY 10024",
            "hospital": "Metro General Hospital",
            "preferred_doctor": "Dr. J. Aris (Cardiology)",
            "preferred_language": "en", # 'en' or 'hi'
            "account_type": "Patient",
            "active_role": "Patient",
            "available_roles": ["Patient"],
            "verification_status": {
                "email_verified": True,
                "phone_verified": True,
                "identity_verified": True,
                "doctor_verified": False,
                "organization_verified": True,
                "overall": "Verified"
            },
            "security": {
                "mfa_enabled": True,
                "passkeys_count": 2,
                "last_password_change": "2023-09-10",
                "password_strength": "Strong (98/100)"
            }
        }

        # Doctor Profile (Dr. Ranjeet Kumar)
        self.doctor_profile = {
            "id": "DR-88219",
            "health_id": "HRP-DOC-2026-088219",
            "full_name": "Dr. Ranjeet Kumar, FACC",
            "first_name": "Dr. Ranjeet Kumar",
            "initials": "RK",
            "title": "Chief Attending Physician & Lead Clinical AI Fellow",
            "email": "rajranjeet7680@gmail.com",
            "phone": "+91 98765 43210",
            "department": "Inpatient Cardiology, Critical Care & AI Medicine",
            "specialty": "Cardiology, Precision Medicine & Predictive AI",
            "sub_specialties": "Heart Failure Triage, Post-Discharge Surveillance, Arrhythmia & Machine Learning Informatics",
            "license_number": "MD-7680-LUMINIX",
            "npi_number": "1849207680",
            "hospital": "Metro General Heart Institute • Team Nexora",
            "clinic_location": "Healthcare Innovation Suite 402, AI Medical Center",
            "office_hours": "Mon–Fri: 08:00 AM – 05:00 PM EST",
            "telehealth_enabled": True,
            "emergency_consult_enabled": True,
            "experience": "18+ Years",
            "education": "Harvard Medical School (MD), Brigham & Women's Hospital (Fellowship) • LUMINIX'26",
            "languages": ["English", "हिन्दी (Hindi)", "Sanskrit"],
            "bio": "Lead solutions architect & attending physician dedicated to reducing 30-day preventable readmissions using predictive ML risk models, explainable AI, and connected care for LUMINIX'26.",
            "account_type": "Doctor",
            "active_role": "Doctor",
            "available_roles": ["Doctor", "Care Coordinator", "Administrator"],
            "verification_status": {
                "email_verified": True,
                "phone_verified": True,
                "identity_verified": True,
                "doctor_verified": True,
                "organization_verified": True,
                "overall": "Verified Healthcare Professional"
            }
        }

        # Emergency Contacts List
        self.emergency_contacts = [
            {
                "id": "EMG-01",
                "name": "Robert Vance",
                "relationship": "Spouse",
                "phone": "+1 (555) 234-5678",
                "email": "robert.vance@email.com",
                "is_primary": True,
                "authorized_for_medical_updates": True
            },
            {
                "id": "EMG-02",
                "name": "Clara Vance-Miller",
                "relationship": "Daughter",
                "phone": "+1 (555) 891-2345",
                "email": "clara.miller@email.com",
                "is_primary": False,
                "authorized_for_medical_updates": False
            }
        ]

        # Privacy & Consent Settings
        self.privacy_settings = {
            "doctor_access": True,
            "care_team_sharing": True,
            "document_sharing_auto_expire": True,
            "ai_context_access": True,
            "research_data_anonymized": False,
            "telehealth_recording_consent": True,
            "public_qr_masked_name": True
        }

        # Granular CareAI Permissions Matrix
        self.careai_permissions = {
            "access_profile": True,
            "access_lab_reports": True,
            "access_prediction_results": True,
            "access_consultation_transcripts": True,
            "access_medication_list": True,
            "auto_draft_notes": True,
            "voice_interaction_enabled": True
        }

        # Notification Channels & Category Matrix
        self.notification_settings = {
            "appointments": {"push": True, "email": True, "sms": True, "in_app": True},
            "risk_alerts": {"push": True, "email": True, "sms": False, "in_app": True},
            "document_updates": {"push": True, "email": True, "sms": False, "in_app": True},
            "security_logins": {"push": True, "email": True, "sms": True, "in_app": True},
            "quiet_hours_enabled": True,
            "quiet_hours_start": "22:00",
            "quiet_hours_end": "07:00"
        }

        # Language, Voice & Audio Settings
        self.voice_settings = {
            "recognition_language": "en-US",
            "speech_to_text": True,
            "text_to_speech": True,
            "auto_play_responses": False,
            "voice_speed": "1.0x",
            "speech_voice": "Samantha (Natural Healthcare)"
        }

        # Accessibility, Theme & Sound Settings
        self.appearance_settings = {
            "theme": "light", # 'light', 'dark', 'system', 'healthcare_blue'
            "motion_mode": "full", # 'full', 'reduced', 'minimal'
            "text_scale": "default", # 'default', 'large', 'xlarge'
            "contrast_mode": "standard", # 'standard', 'high_contrast'
            "captions_enabled": True,
            "sound_effects_enabled": True,
            "notification_sounds_enabled": True,
            "video_call_ringtone_enabled": True,
            "master_volume": 85
        }

        # Active Devices List
        self.active_devices = [
            {
                "id": "DEV-01",
                "device_name": "Apple iPhone 14 Pro",
                "device_type": "mobile",
                "browser": "Safari Mobile 17.1",
                "os": "iOS 17.4",
                "ip_address": "192.168.1.104 (Home Wi-Fi)",
                "location": "New York, USA",
                "last_active": "Just now",
                "is_current": True
            },
            {
                "id": "DEV-02",
                "device_name": "MacBook Air M2",
                "device_type": "desktop",
                "browser": "Chrome 122.0",
                "os": "macOS Sonoma",
                "ip_address": "192.168.1.108 (Home Wi-Fi)",
                "location": "New York, USA",
                "last_active": "2 hours ago",
                "is_current": False
            },
            {
                "id": "DEV-03",
                "device_name": "Hospital Inpatient iPad Pro",
                "device_type": "tablet",
                "browser": "Mobile Safari",
                "os": "iPadOS 16.5",
                "ip_address": "10.24.8.19 (Hospital Private)",
                "location": "Cardiology Ward 4B",
                "last_active": "Oct 24, 2023",
                "is_current": False
            }
        ]

        # Connected Institutional & Cloud Services
        self.connected_services = [
            {
                "id": "SVC-GCAL",
                "name": "Google Calendar",
                "description": "Synchronize doctor appointments and follow-up clinical visits.",
                "icon": "calendar_month",
                "status": "Connected",
                "connected_account": "eleanor.vance@gmail.com",
                "connected_date": "2023-08-14"
            },
            {
                "id": "SVC-FHIR",
                "name": "Metro Hospital EHR / Epic FHIR Connector",
                "description": "Secure bi-directional clinical health record synchronization.",
                "icon": "local_hospital",
                "status": "Connected",
                "connected_account": "Hospital ID: #PT-84729",
                "connected_date": "2023-10-24"
            },
            {
                "id": "SVC-GDRIVE",
                "name": "Google Drive Encrypted Vault",
                "description": "Backup downloaded medical certificates and lab PDF reports.",
                "icon": "cloud_upload",
                "status": "Not Connected",
                "connected_account": None,
                "connected_date": None
            }
        ]

        # User Activity & Security Event Audit Stream
        self.user_activity_stream = [
            {
                "id": "ACT-01",
                "timestamp": "Today, 10:45 AM",
                "event_type": "QR_GENERATED",
                "title": "Health ID QR Viewed & Verified",
                "icon": "qr_code",
                "color": "text-primary",
                "ip": "192.168.1.104"
            },
            {
                "id": "ACT-02",
                "timestamp": "Today, 09:30 AM",
                "event_type": "PREDICTION_EVALUATED",
                "title": "Readmission Assessment Evaluated (68% Score)",
                "icon": "analytics",
                "color": "text-error",
                "ip": "10.24.8.19"
            },
            {
                "id": "ACT-03",
                "timestamp": "Yesterday, 14:15 PM",
                "event_type": "DOCUMENT_UPLOADED",
                "title": "Metabolic Panel & CBC Lab Report Uploaded",
                "icon": "upload_file",
                "color": "text-secondary",
                "ip": "192.168.1.104"
            },
            {
                "id": "ACT-04",
                "timestamp": "Oct 24, 2023 09:12 AM",
                "event_type": "MFA_LOGIN_SUCCESS",
                "title": "Successful Login with 6-Digit MFA OTP",
                "icon": "verified_user",
                "color": "text-[#146c2e]",
                "ip": "192.168.1.104"
            }
        ]

    def update_profile(self, data: dict):
        for key in ["full_name", "phone", "dob", "gender", "blood_group", "address", "preferred_language"]:
            if key in data and data[key] is not None:
                self.profile[key] = data[key]
        return self.profile

    def update_doctor_profile(self, data: dict) -> dict:
        for field in [
            "full_name", "title", "email", "phone", "department", "specialty",
            "sub_specialties", "license_number", "npi_number", "hospital",
            "clinic_location", "office_hours", "experience", "education", "bio"
        ]:
            if field in data and data[field] is not None:
                self.doctor_profile[field] = str(data[field]).strip()
        
        # Languages parsing
        if "languages" in data:
            if isinstance(data["languages"], list):
                self.doctor_profile["languages"] = data["languages"]
            elif isinstance(data["languages"], str):
                self.doctor_profile["languages"] = [lang.strip() for lang in data["languages"].split(",") if lang.strip()]
        
        # Boolean toggles
        if "telehealth_enabled" in data:
            self.doctor_profile["telehealth_enabled"] = data.get("telehealth_enabled") in [True, "true", "True", "on", "1"]
        if "emergency_consult_enabled" in data:
            self.doctor_profile["emergency_consult_enabled"] = data.get("emergency_consult_enabled") in [True, "true", "True", "on", "1"]

        # Recalculate initials
        raw_name = self.doctor_profile["full_name"].replace("Dr.", "").replace("MD", "").replace("FACC", "").replace(",", "").strip()
        parts = raw_name.split()
        if len(parts) >= 2:
            self.doctor_profile["initials"] = f"{parts[0][0]}{parts[-1][0]}".upper()
        elif len(parts) == 1 and len(parts[0]) >= 2:
            self.doctor_profile["initials"] = parts[0][:2].upper()
        else:
            self.doctor_profile["initials"] = "DS"

        return self.doctor_profile

    def update_privacy(self, data: dict):
        for key in self.privacy_settings.keys():
            if key in data:
                self.privacy_settings[key] = bool(data[key])
        return self.privacy_settings

    def update_careai_permissions(self, data: dict):
        for key in self.careai_permissions.keys():
            if key in data:
                self.careai_permissions[key] = bool(data[key])
        return self.careai_permissions

    def update_appearance(self, data: dict):
        for key in self.appearance_settings.keys():
            if key in data:
                self.appearance_settings[key] = data[key]
        return self.appearance_settings

    def add_emergency_contact(self, contact_data: dict):
        contact_id = f"EMG-{str(uuid.uuid4())[:4].upper()}"
        new_c = {
            "id": contact_id,
            "name": contact_data.get("name", "Emergency Contact"),
            "relationship": contact_data.get("relationship", "Family"),
            "phone": contact_data.get("phone", ""),
            "email": contact_data.get("email", ""),
            "is_primary": bool(contact_data.get("is_primary", False)),
            "authorized_for_medical_updates": bool(contact_data.get("authorized_for_medical_updates", False))
        }
        if new_c["is_primary"]:
            for c in self.emergency_contacts:
                c["is_primary"] = False
        self.emergency_contacts.append(new_c)
        return new_c

    def remove_emergency_contact(self, contact_id: str):
        self.emergency_contacts = [c for c in self.emergency_contacts if c["id"] != contact_id]
        return True

    def revoke_device(self, device_id: str):
        self.active_devices = [d for d in self.active_devices if d["id"] != device_id]
        return True

    def revoke_service(self, service_id: str):
        for s in self.connected_services:
            if s["id"] == service_id:
                s["status"] = "Not Connected"
                s["connected_account"] = None
        return True

    def switch_role(self, target_role: str):
        valid_roles = ["Patient", "Doctor", "Care Coordinator", "Administrator"]
        if target_role in valid_roles:
            self.profile["active_role"] = target_role
            return True
        return False

    def generate_data_export_archive(self):
        """
        Creates comprehensive JSON dump of personal health records & settings.
        """
        return {
            "export_id": f"EXP-{str(uuid.uuid4())[:8].upper()}",
            "generated_at": datetime.now().isoformat(),
            "patient_profile": self.profile,
            "emergency_contacts": self.emergency_contacts,
            "privacy_and_consent": self.privacy_settings,
            "careai_permissions": self.careai_permissions,
            "active_devices": self.active_devices,
            "activity_audit_logs": self.user_activity_stream,
            "legal_notice": "Official Electronic Export under HIPAA Privacy Rule 45 CFR 164.524."
        }

account_manager = AccountManager()
