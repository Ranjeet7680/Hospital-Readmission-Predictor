"""
Data Models and Schemas for Hospital Readmission Predictor (HRP Clinical)
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Demographics(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    patient_id: str = "PT-84729"
    full_name: str = "Eleanor Vance"
    age: int = 71
    gender: str = "Female"
    dob: str = "1952-10-14"
    department: str = "Cardiology"
    attending_physician: str = "Dr. J. Aris"
    primary_diagnosis: str = "Congestive Heart Failure"
    admission_date: str = "2023-10-24"
    discharge_date: Optional[str] = "2023-11-02"
    length_of_stay: int = 9
    acuity_level: str = "High"

class ClinicalVitals(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    heart_rate: float = 88.0
    systolic_bp: float = 135.0
    diastolic_bp: float = 85.0
    temperature: float = 37.0
    resp_rate: float = 18.0
    spo2: float = 94.0
    hemoglobin: float = 11.2
    wbc: float = 8.4
    creatinine: float = 1.6
    glucose: float = 145.0
    hba1c: float = 7.4
    cholesterol: float = 210.0
    bmi: float = 29.4

class MedicalHistory(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    prev_admissions_30d: int = 1
    prev_admissions_12m: int = 2
    ed_visits_12m: int = 2
    icu_admissions: int = 0
    medication_count: int = 8
    medication_classes: List[str] = ["Cardiovascular", "Endocrine", "Diuretics"]
    comorbidities: List[str] = ["Congestive Heart Failure", "Type 2 Diabetes Mellitus", "Hypertension", "Chronic Kidney Disease (Stage 3)"]
    living_arrangement: str = "With Family/Spouse"
    transportation: str = "Reliable / Owns Car"
    followup_adherence: str = "Moderate"
    discharge_destination: str = "Home"

class PredictionRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    patient_id: Optional[str] = "PT-84729"
    full_name: Optional[str] = "Eleanor Vance"
    age: Optional[int] = 71
    gender: Optional[str] = "Female"
    department: Optional[str] = "Cardiology"
    attending_physician: Optional[str] = "Dr. Smith"
    primary_diagnosis: Optional[str] = "Congestive Heart Failure"
    admission_date: Optional[str] = "2023-10-24"
    discharge_date: Optional[str] = "2023-11-02"
    length_of_stay: Optional[int] = 9
    acuity_level: Optional[str] = "High"
    
    # Vitals & Labs
    heart_rate: Optional[float] = 88.0
    systolic_bp: Optional[float] = 135.0
    diastolic_bp: Optional[float] = 85.0
    temperature: Optional[float] = 37.0
    resp_rate: Optional[float] = 18.0
    spo2: Optional[float] = 94.0
    hemoglobin: Optional[float] = 11.2
    wbc: Optional[float] = 8.4
    creatinine: Optional[float] = 1.6
    glucose: Optional[float] = 145.0
    hba1c: Optional[float] = 7.4
    cholesterol: Optional[float] = 210.0
    bmi: Optional[float] = 29.4

    # History & Social
    prev_admissions_30d: Optional[int] = 1
    prev_admissions_12m: Optional[int] = 2
    ed_visits_12m: Optional[int] = 2
    icu_admissions: Optional[int] = 0
    medication_count: Optional[int] = 8
    medication_classes: Optional[List[str]] = ["Cardiovascular", "Endocrine"]
    comorbidities: Optional[List[str]] = ["Congestive Heart Failure", "Type 2 Diabetes Mellitus", "Hypertension", "Chronic Kidney Disease"]
    living_arrangement: Optional[str] = "With Family/Spouse"
    transportation: Optional[str] = "Reliable / Owns Car"
    followup_adherence: Optional[str] = "Moderate"
    discharge_destination: Optional[str] = "Home"

class ContributingFactor(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    title: str
    impact: str
    direction: str
    color: str
    icon: str
    description: str

class PredictionResult(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    id: str
    patient_id: str
    patient_name: str
    timestamp: str
    risk_score: int
    risk_level: str
    risk_level_code: str
    risk_badge_class: str
    risk_color: str
    gauge_dashoffset: float
    model_version: str = "v2.4.1"
    clinician: str = "Dr. Smith"
    department: str = "Cardiology"
    status: str = "Reviewed"
    contributing_factors: List[ContributingFactor]
    recommendations: List[str]
    primary_recommendation: str
    raw_payload: Optional[dict] = None
