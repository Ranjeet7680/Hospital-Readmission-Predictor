"""
Hospital Readmission Predictor (HRP Clinical) - Notification & Clinical Alert Center
Manages real-time clinical alerts, high-risk triage notifications, AI/ML operational updates,
telehealth appointments, and cryptographic security events.
"""

from datetime import datetime
from typing import List, Dict, Optional

class NotificationManager:
    def __init__(self):
        self.notifications: List[Dict] = [
            {
                "id": "NOTIF-2026-001",
                "title": "High Risk Readmission Alert: Eleanor Vance (PT-84729)",
                "message": "XGBoost v2.4.1 predicted 68.4% readmission probability. Elevated serum creatinine (1.60 mg/dL) and BUN (24 mg/dL) require immediate clinical review.",
                "category": "clinical",
                "priority": "critical",
                "timestamp": "2 mins ago",
                "read": False,
                "action_url": "/patient/PT-84729",
                "action_label": "Review Patient",
                "icon": "warning"
            },
            {
                "id": "NOTIF-2026-002",
                "title": "PPO RL Pathway Recommended: Intensive Home Tele-Monitoring",
                "message": "Reinforcement Learning policy recommends daily SpO2/ECG telemetry and diuretic titration to reduce 30-day post-discharge readmission by 42%.",
                "category": "clinical",
                "priority": "warning",
                "timestamp": "12 mins ago",
                "read": False,
                "action_url": "/rl/dashboard",
                "action_label": "View RL Policy",
                "icon": "route"
            },
            {
                "id": "NOTIF-2026-003",
                "title": "CareAI Video Consultation Scheduled: Dr. CareAI",
                "message": "Interactive Tele-Consultation session initialized for PT-84729 with live Lead II ECG monitoring and full-duplex Voice AI.",
                "category": "telehealth",
                "priority": "info",
                "timestamp": "28 mins ago",
                "read": False,
                "action_url": "/consultation/careai",
                "action_label": "Join Video Call",
                "icon": "videocam"
            },
            {
                "id": "NOTIF-2026-004",
                "title": "ML Model Calibration & Health Check Passed",
                "message": "XGBoost Classifier v2.4.1 serving with 0.9794 ROC-AUC. Model drift 0.002% across 30,000 patient records within nominal bounds.",
                "category": "ai_ml",
                "priority": "success",
                "timestamp": "1 hour ago",
                "read": True,
                "action_url": "/ml-dashboard",
                "action_label": "Model Hub",
                "icon": "model_training"
            },
            {
                "id": "NOTIF-2026-005",
                "title": "Medical Certificate CERT-2023-84729 Digitally Signed",
                "message": "14-Day Medical Convalescence Certificate generated and validated with SHA-256 cryptographic signature.",
                "category": "clinical",
                "priority": "success",
                "timestamp": "2 hours ago",
                "read": True,
                "action_url": "/medical-certificates",
                "action_label": "View Certificate",
                "icon": "verified"
            },
            {
                "id": "NOTIF-2026-006",
                "title": "Security Token Rotated: Level 3 Dynamic QR Credential",
                "message": "Patient Digital Health ID verification token QRT-EV-HEALTHID-1042 rotated and activated on the public verification gateway.",
                "category": "security",
                "priority": "info",
                "timestamp": "3 hours ago",
                "read": True,
                "action_url": "/health-id",
                "action_label": "Health ID Card",
                "icon": "shield"
            },
            {
                "id": "NOTIF-2026-007",
                "title": "Polypharmacy Alert: Automated Pharmacist Review Queued",
                "message": "Patient Marcus Vance is prescribed 7 active medications (>6 cutoff). Clinical pharmacist consultation referral automatically generated.",
                "category": "clinical",
                "priority": "warning",
                "timestamp": "4 hours ago",
                "read": True,
                "action_url": "/patients",
                "action_label": "Patients List",
                "icon": "medication"
            },
            {
                "id": "NOTIF-2026-008",
                "title": "Multi-Lingual 7-Language Engine v4.0 Active",
                "message": "Neural speech synthesis and clinical terminology dictionary initialized for English, Hindi, Tamil, Kannada, Malayalam, Telugu, and Bengali.",
                "category": "ai_ml",
                "priority": "info",
                "timestamp": "5 hours ago",
                "read": True,
                "action_url": "/dashboard",
                "action_label": "Dashboard",
                "icon": "translate"
            }
        ]

    def get_all(self, category: Optional[str] = None, unread_only: bool = False) -> List[Dict]:
        res = self.notifications
        if category and category != "all":
            res = [n for n in res if n.get("category") == category]
        if unread_only:
            res = [n for n in res if not n.get("read")]
        return res

    def get_unread_count(self) -> int:
        return len([n for n in self.notifications if not n.get("read")])

    def mark_as_read(self, notif_id: str) -> bool:
        for n in self.notifications:
            if n["id"] == notif_id:
                n["read"] = True
                return True
        return False

    def mark_all_read(self):
        for n in self.notifications:
            n["read"] = True

    def delete_notification(self, notif_id: str) -> bool:
        before = len(self.notifications)
        self.notifications = [n for n in self.notifications if n["id"] != notif_id]
        return len(self.notifications) < before

    def clear_all(self):
        self.notifications = []

    def add_notification(self, title: str, message: str, category: str = "clinical", priority: str = "info", action_url: str = "", action_label: str = ""):
        nid = f"NOTIF-2026-{len(self.notifications)+1:03d}"
        icon_map = {
            "clinical": "warning",
            "ai_ml": "smart_toy",
            "telehealth": "videocam",
            "security": "security",
            "system": "info"
        }
        notif = {
            "id": nid,
            "title": title,
            "message": message,
            "category": category,
            "priority": priority,
            "timestamp": "Just now",
            "read": False,
            "action_url": action_url,
            "action_label": action_label,
            "icon": icon_map.get(category, "notifications")
        }
        self.notifications.insert(0, notif)
        return notif

notification_manager = NotificationManager()
