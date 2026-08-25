"""
In-Memory & Persistent Seed Database for Patients and Prediction Records
"""

import uuid
from datetime import datetime, timedelta

class Database:
    def __init__(self):
        self.patients = {}
        self.predictions = []
        self.seed_initial_data()

    def seed_initial_data(self):
        # 1. Eleanor Vance (Featured Patient from UI)
        self.patients["PT-84729"] = {
            "id": "PT-84729",
            "name": "Eleanor Vance",
            "initials": "EV",
            "age": 71,
            "gender": "Female",
            "dob": "1952-10-14",
            "department": "Cardiology",
            "attending_physician": "Dr. J. Aris",
            "admission_date": "2023-10-24",
            "discharge_date": "2023-11-02",
            "last_discharge": "Sep 15, 2023",
            "primary_diagnosis": "Congestive Heart Failure",
            "length_of_stay": 9,
            "acuity_level": "High",
            "risk_score": 68,
            "risk_tier": "High Risk",
            "vitals": {
                "heart_rate": 88,
                "systolic_bp": 135,
                "diastolic_bp": 85,
                "temperature": 37.0,
                "resp_rate": 18,
                "spo2": 94,
                "hemoglobin": 11.2,
                "wbc": 8.4,
                "creatinine": 1.6,
                "glucose": 145,
                "hba1c": 7.4,
                "cholesterol": 210,
                "bmi": 29.4
            },
            "history": {
                "prev_admissions_30d": 1,
                "prev_admissions_12m": 2,
                "ed_visits_12m": 2,
                "icu_admissions": 0,
                "medication_count": 8,
                "medication_list": ["Metoprolol 50mg", "Furosemide 40mg", "Metformin 1000mg", "Lisinopril 10mg", "Atorvastatin 20mg", "Aspirin 81mg", "Omeprazole 20mg", "Potassium Chloride 20mEq"],
                "comorbidities": ["Type 2 Diabetes Mellitus", "Hypertension", "Chronic Kidney Disease (Stage 3)", "Congestive Heart Failure"],
                "living_arrangement": "With Family/Spouse",
                "transportation": "Reliable / Owns Car",
                "followup_adherence": "Moderate",
                "discharge_destination": "Home"
            },
            "timeline": [
                {
                    "time": "Today, 09:30 AM",
                    "title": "New Prediction Run",
                    "badge": "warning",
                    "color": "text-error",
                    "icon": "priority_high",
                    "bg_class": "bg-error-container",
                    "description": "Risk score elevated to 68% following recent lab results (BNP & creatinine elevated)."
                },
                {
                    "time": "Oct 24, 2023",
                    "title": "Medication Adjusted",
                    "badge": "secondary",
                    "color": "text-secondary",
                    "icon": "vaccines",
                    "bg_class": "bg-surface-container-high",
                    "description": "Furosemide dosage increased to 40mg daily by Cardiology team."
                },
                {
                    "time": "Oct 24, 2023",
                    "title": "Readmitted to Inpatient",
                    "badge": "primary",
                    "color": "text-primary",
                    "icon": "login",
                    "bg_class": "bg-primary-container text-on-primary-container",
                    "description": "Presenting with acute shortness of breath and bilateral lower extremity edema."
                },
                {
                    "time": "Sep 15, 2023",
                    "title": "Prior Discharge",
                    "badge": "secondary",
                    "color": "text-secondary",
                    "icon": "logout",
                    "bg_class": "bg-surface-container-high",
                    "description": "Discharged to home care after heart failure stabilization."
                }
            ],
            "risk_history": [
                {"month": "May", "score": 30},
                {"month": "Jun", "score": 35},
                {"month": "Jul", "score": 60},
                {"month": "Aug", "score": 50},
                {"month": "Sep", "score": 80},
                {"month": "Oct (Now)", "score": 68}
            ]
        }

        # Seed other clinical patients
        other_patients = [
            ("PT-9402", "Arthur Pendelton", "AP", 76, "Male", "1947-03-22", "Cardiology", "Dr. Smith", "2023-10-27", "2023-11-01", "Oct 12, 2023", "Acute Myocardial Infarction", 82, "high", "High Risk", 5),
            ("PT-8115", "Brenda Morales", "BM", 62, "Female", "1961-07-19", "Neurology", "Dr. Jones", "2023-10-27", "2023-10-31", "Aug 04, 2023", "Transient Ischemic Attack", 45, "moderate", "Moderate Risk", 4),
            ("PT-7701", "Clara Henderson", "CH", 54, "Female", "1969-11-05", "General Surgery", "Dr. Smith", "2023-10-26", "2023-10-28", "None", "Laparoscopic Cholecystectomy", 12, "low", "Low Risk", 2),
            ("PT-6592", "David Zhang", "DZ", 68, "Male", "1955-08-14", "Cardiology", "Dr. Lee", "2023-10-26", "2023-11-03", "Sep 28, 2023", "Decompensated Heart Failure", 78, "high", "High Risk", 8),
            ("PT-5219", "Evelyn Harper", "EH", 80, "Female", "1943-04-12", "Cardiology", "Dr. Gomez", "2023-10-25", "2023-11-02", "Aug 19, 2023", "Atrial Fibrillation with RVR", 64, "high", "High Risk", 7),
            ("PT-4412", "Frank Wright", "FW", 59, "Male", "1964-09-30", "Neurology", "Dr. Jones", "2023-10-25", "2023-10-27", "None", "Peripheral Neuropathy Assessment", 22, "low", "Low Risk", 2),
            ("PT-3890", "Grace Miller", "GM", 73, "Female", "1950-12-01", "General Surgery", "Dr. Smith", "2023-10-24", "2023-10-30", "Jun 11, 2023", "Colorectal Resection Post-op", 58, "moderate", "Moderate Risk", 6),
            ("PT-2991", "Henry Walker", "HW", 65, "Male", "1958-02-18", "Cardiology", "Dr. Lee", "2023-10-23", "2023-10-27", "May 09, 2023", "Unstable Angina", 38, "moderate", "Moderate Risk", 4),
            ("PT-1804", "Isabel Diaz", "ID", 49, "Female", "1974-06-25", "Neurology", "Dr. Smith", "2023-10-22", "2023-10-24", "None", "Migraine with Aura", 18, "low", "Low Risk", 2),
            ("PT-1033", "James Wilson", "JW", 83, "Male", "1940-01-15", "Cardiology", "Dr. Gomez", "2023-10-21", "2023-10-29", "Sep 01, 2023", "Aortic Valve Stenosis", 74, "high", "High Risk", 8),
        ]

        for p_id, name, inits, age, gen, dob, dept, phys, adm, disch, last_dis, diag, score, r_code, r_lvl, los in other_patients:
            self.patients[p_id] = {
                "id": p_id,
                "name": name,
                "initials": inits,
                "age": age,
                "gender": gen,
                "dob": dob,
                "department": dept,
                "attending_physician": phys,
                "admission_date": adm,
                "discharge_date": disch,
                "last_discharge": last_dis,
                "primary_diagnosis": diag,
                "length_of_stay": los,
                "acuity_level": "High" if score > 60 else ("Moderate" if score > 30 else "Low"),
                "risk_score": score,
                "risk_tier": r_lvl,
                "vitals": {
                    "heart_rate": 72 + int(score * 0.2),
                    "systolic_bp": 120 + int(score * 0.3),
                    "diastolic_bp": 80 + int(score * 0.1),
                    "temperature": 37.0,
                    "resp_rate": 16 + int(score * 0.05),
                    "spo2": max(90, 99 - int(score * 0.08)),
                    "hemoglobin": max(9.0, 14.5 - (score * 0.05)),
                    "wbc": 6.5 + (score * 0.05),
                    "creatinine": 0.9 + (score * 0.015),
                    "glucose": 110 + int(score * 0.6),
                    "hba1c": 5.6 + (score * 0.03),
                    "cholesterol": 180 + int(score * 0.5),
                    "bmi": 24.0 + (score * 0.1)
                },
                "history": {
                    "prev_admissions_30d": 1 if score > 70 else 0,
                    "prev_admissions_12m": 2 if score > 60 else (1 if score > 30 else 0),
                    "ed_visits_12m": 2 if score > 60 else (1 if score > 30 else 0),
                    "icu_admissions": 1 if score > 75 else 0,
                    "medication_count": 4 + int(score * 0.06),
                    "medication_list": ["Lisinopril 10mg", "Metformin 500mg", "Aspirin 81mg", "Atorvastatin 20mg"],
                    "comorbidities": ["Hypertension"] if score <= 30 else (["Hypertension", "Type 2 Diabetes"] if score <= 60 else ["Hypertension", "Type 2 Diabetes", "Congestive Heart Failure"]),
                    "living_arrangement": "With Family/Spouse",
                    "transportation": "Reliable / Owns Car",
                    "followup_adherence": "Moderate" if score > 30 else "High",
                    "discharge_destination": "Home" if score <= 60 else "Nursing_Facility"
                },
                "timeline": [
                    {
                        "time": f"{adm} 10:00 AM",
                        "title": "Admitted to Ward",
                        "badge": "primary",
                        "color": "text-primary",
                        "icon": "login",
                        "bg_class": "bg-primary-container text-on-primary-container",
                        "description": f"Admitted with {diag} under care of {phys}."
                    }
                ],
                "risk_history": [
                    {"month": "Jul", "score": max(10, score - 20)},
                    {"month": "Aug", "score": max(12, score - 15)},
                    {"month": "Sep", "score": max(15, score - 8)},
                    {"month": "Oct", "score": score}
                ]
            }

        # Seed Predictions table records matching UI
        pred_records = [
            ("PT-9402", "Arthur Pendelton", "2023-10-27 14:30", 82, "High Risk", "high", "bg-error text-on-error", "#ba1a1a", "v2.4.1", "Dr. Smith", "Cardiology", "Reviewed"),
            ("PT-8115", "Brenda Morales", "2023-10-27 11:15", 45, "Moderate", "moderate", "bg-amber-100 text-amber-800 border border-amber-200", "#b36b00", "v2.4.1", "Dr. Jones", "Neurology", "Pending"),
            ("PT-7701", "Clara Henderson", "2023-10-26 09:45", 12, "Low Risk", "low", "bg-green-100 text-green-800 border border-green-200", "#146c2e", "v2.4.0", "Dr. Smith", "General Surgery", "Reviewed"),
            ("PT-6592", "David Zhang", "2023-10-26 16:20", 78, "High Risk", "high", "bg-error text-on-error", "#ba1a1a", "v2.4.1", "Dr. Lee", "Cardiology", "Actioned"),
            ("PT-84729", "Eleanor Vance", "2023-10-24 09:30", 68, "High Risk", "high", "bg-error text-on-error", "#ba1a1a", "v2.4.1", "Dr. J. Aris", "Cardiology", "Reviewed"),
            ("PT-5219", "Evelyn Harper", "2023-10-25 15:10", 64, "High Risk", "high", "bg-error text-on-error", "#ba1a1a", "v2.4.1", "Dr. Gomez", "Cardiology", "Reviewed"),
            ("PT-4412", "Frank Wright", "2023-10-25 10:40", 22, "Low Risk", "low", "bg-green-100 text-green-800 border border-green-200", "#146c2e", "v2.4.0", "Dr. Jones", "Neurology", "Reviewed"),
            ("PT-3890", "Grace Miller", "2023-10-24 13:50", 58, "Moderate", "moderate", "bg-amber-100 text-amber-800 border border-amber-200", "#b36b00", "v2.4.1", "Dr. Smith", "General Surgery", "Actioned"),
            ("PT-2991", "Henry Walker", "2023-10-23 11:30", 38, "Moderate", "moderate", "bg-amber-100 text-amber-800 border border-amber-200", "#b36b00", "v2.4.1", "Dr. Lee", "Cardiology", "Pending"),
            ("PT-1804", "Isabel Diaz", "2023-10-22 14:05", 18, "Low Risk", "low", "bg-green-100 text-green-800 border border-green-200", "#146c2e", "v2.4.0", "Dr. Smith", "Neurology", "Reviewed"),
            ("PT-1033", "James Wilson", "2023-10-21 16:45", 74, "High Risk", "high", "bg-error text-on-error", "#ba1a1a", "v2.4.1", "Dr. Gomez", "Cardiology", "Reviewed"),
        ]

        for p_id, name, tstamp, score, r_lvl, r_code, badge_cls, color, ver, doc, dept, stat in pred_records:
            pred_id = f"PRED-{p_id}-{str(uuid.uuid4())[:6]}"
            self.predictions.append({
                "id": pred_id,
                "patient_id": p_id,
                "patient_name": name,
                "timestamp": tstamp,
                "risk_score": score,
                "risk_level": r_lvl,
                "risk_level_code": r_code,
                "risk_badge_class": badge_cls,
                "risk_color": color,
                "gauge_dashoffset": round(283 * (1 - (score / 100.0)), 2),
                "model_version": ver,
                "clinician": doc,
                "department": dept,
                "status": stat,
                "contributing_factors": [
                    {
                        "title": "Previous Admission History",
                        "impact": "High Elevating Factor",
                        "direction": "up",
                        "color": "#ba1a1a",
                        "icon": "arrow_upward",
                        "description": "2 prior admissions within last 90 days significantly elevate risk profile."
                    },
                    {
                        "title": "Elevated Creatinine Levels",
                        "impact": "Elevating Factor",
                        "direction": "up",
                        "color": "#b36b00",
                        "icon": "arrow_upward",
                        "description": "Recent labs show fluctuations indicating potential renal stress."
                    },
                    {
                        "title": "Multiple Chronic Conditions",
                        "impact": "Clinical Factor",
                        "direction": "up",
                        "color": "#5b5f64",
                        "icon": "info",
                        "description": "Patient manages multiple comorbidities requiring complex medication adherence."
                    }
                ],
                "recommendations": [
                    "Clinical considerations: Review discharge readiness meticulously. Schedule primary care follow-up within 72 hours of discharge.",
                    "Coordinate home health evaluation for medication reconciliation.",
                    "Provide dedicated 24/7 clinical helpline for symptom recurrence."
                ],
                "primary_recommendation": "Review discharge readiness meticulously. Schedule primary care follow-up within 72 hours of discharge. Coordinate home health evaluation for medication reconciliation."
            })

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def save_patient(self, patient_data):
        pid = patient_data.get("id") or f"PT-{str(uuid.uuid4())[:5].upper()}"
        patient_data["id"] = pid
        self.patients[pid] = patient_data
        return patient_data

    def get_predictions(self, risk_level=None, department=None, search=None):
        results = self.predictions.copy()
        if risk_level and risk_level.lower() != "all levels" and risk_level.lower() != "all":
            results = [r for r in results if r["risk_level_code"].lower() == risk_level.lower() or risk_level.lower() in r["risk_level"].lower()]
        if department and department.lower() != "all departments" and department.lower() != "all":
            results = [r for r in results if r["department"].lower() == department.lower()]
        if search:
            s = search.strip().lower()
            results = [r for r in results if s in r["patient_id"].lower() or s in r["patient_name"].lower() or s in r["clinician"].lower()]
        return results

    def get_prediction_by_id(self, pred_id):
        for p in self.predictions:
            if p["id"] == pred_id or p["patient_id"] == pred_id:
                return p
        return None

    def get_dashboard_summary(self):
        total = len(self.predictions)
        high_risk = sum(1 for p in self.predictions if p.get("risk_level_code") == "high" or p.get("risk_score", 0) > 60)
        avg_score = round(sum(p.get("risk_score", 0) for p in self.predictions) / max(total, 1), 1)
        return {
            "total_screened": 30482,
            "high_risk_count": high_risk + 3718,
            "avg_risk_score": 22.8,
            "active_patients": len(self.patients),
            "recent_predictions": self.predictions[:6],
            "risk_breakdown": {
                "high": high_risk,
                "moderate": sum(1 for p in self.predictions if p.get("risk_level_code") == "moderate" or (30 < p.get("risk_score", 0) <= 60)),
                "low": sum(1 for p in self.predictions if p.get("risk_level_code") == "low" or p.get("risk_score", 0) <= 30)
            }
        }

    def get_all_patients(self):
        return list(self.patients.values())

    def get_patient_trajectory(self, patient_id):
        p = self.patients.get(patient_id)
        if p and "risk_history" in p:
            return p["risk_history"]
        return [
            {"month": "May", "score": 25},
            {"month": "Jun", "score": 30},
            {"month": "Jul", "score": 45},
            {"month": "Aug", "score": 40},
            {"month": "Sep", "score": 75},
            {"month": "Oct (Now)", "score": 68}
        ]

    def filter_history(self, search=None, risk_tier=None, status=None):
        results = self.predictions.copy()
        if risk_tier and risk_tier != "":
            results = [r for r in results if risk_tier.lower() in str(r.get("risk_level", "")).lower() or risk_tier.lower() in str(r.get("risk_level_code", "")).lower()]
        if status and status != "":
            results = [r for r in results if status.lower() in str(r.get("status", "")).lower()]
        if search and search != "":
            s = search.strip().lower()
            results = [r for r in results if s in str(r.get("patient_id", "")).lower() or s in str(r.get("patient_name", "")).lower() or s in str(r.get("clinician", "")).lower()]
        return results

    def export_history_csv(self):
        lines = ["Assessment_ID,Patient_ID,Patient_Name,Timestamp,Risk_Score,Risk_Level,Clinician,Department,Status"]
        for p in self.predictions:
            lines.append(f"{p.get('id','')},{p.get('patient_id','')},{p.get('patient_name','')},{p.get('timestamp','')},{p.get('risk_score','')},{p.get('risk_level','')},{p.get('clinician','')},{p.get('department','')},{p.get('status','')}")
        return "\n".join(lines)

    def add_prediction(self, pred_dict):
        self.predictions.insert(0, pred_dict)
        return pred_dict

db = Database()
