"""
Automated Test Suite for Hospital Readmission Predictor (HRP Clinical)
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from ml.predictor import predictor_instance

client = TestClient(app)

def test_model_inference_high_risk():
    patient_data = {
        "patient_id": "TEST-HIGH",
        "full_name": "High Risk Test",
        "age": 78,
        "gender": "Female",
        "systolic_bp": 145,
        "diastolic_bp": 92,
        "creatinine": 2.1,
        "haemoglobin": 9.8,
        "hba1c": 8.5,
        "prev_admissions_30d": 2,
        "prev_admissions_12m": 3,
        "ed_visits_12m": 3,
        "medication_count": 9,
        "primary_diagnosis": "Congestive Heart Failure",
        "comorbidities": ["Congestive Heart Failure", "Type 2 Diabetes", "Chronic Kidney Disease"]
    }
    result = predictor_instance.predict(patient_data)
    assert result["risk_score"] > 60
    assert result["risk_level_code"] == "high"
    assert len(result["contributing_factors"]) > 0
    assert len(result["recommendations"]) > 0

def test_model_inference_low_risk():
    patient_data = {
        "patient_id": "TEST-LOW",
        "full_name": "Low Risk Test",
        "age": 32,
        "gender": "Male",
        "systolic_bp": 115,
        "diastolic_bp": 75,
        "creatinine": 0.9,
        "haemoglobin": 15.0,
        "hba1c": 5.2,
        "prev_admissions_30d": 0,
        "prev_admissions_12m": 0,
        "ed_visits_12m": 0,
        "medication_count": 1,
        "primary_diagnosis": "Laparoscopic appendectomy",
        "comorbidities": []
    }
    result = predictor_instance.predict(patient_data)
    assert result["risk_score"] <= 50
    assert result["risk_level_code"] in ["low", "moderate"]

def test_page_routes():
    pages = [
        "/",
        "/welcome",
        "/login",
        "/dashboard",
        "/prediction/new",
        "/prediction/PT-84729",
        "/patient/PT-84729",
        "/patients",
        "/history",
        "/analytics",
        "/insights",
        "/settings",
        "/help"
    ]
    for route in pages:
        response = client.get(route)
        assert response.status_code == 200, f"Route {route} failed with {response.status_code}"

def test_api_predict_and_persistence():
    payload = {
        "patient_id": "PT-AUTOTEST-99",
        "full_name": "Automation Test Patient",
        "age": 70,
        "gender": "Female",
        "department": "Cardiology",
        "attending_physician": "Dr. Smith",
        "primary_diagnosis": "Heart Failure",
        "heart_rate": 88,
        "systolic_bp": 135,
        "diastolic_bp": 85,
        "creatinine": 1.6,
        "prev_admissions_30d": 1,
        "prev_admissions_12m": 2,
        "medication_count": 8
    }
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["patient_id"] == "PT-AUTOTEST-99"
    assert data["risk_score"] > 0
    assert "contributing_factors" in data

    # Verify patient was persisted
    p_response = client.get("/api/patient/PT-AUTOTEST-99")
    assert p_response.status_code == 200
    assert p_response.json()["name"] == "Automation Test Patient"

def test_history_csv_export():
    response = client.get("/api/history/export")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    content = response.text
    assert "Assessment_ID,Patient_ID,Patient_Name" in content
    assert "Eleanor Vance" in content

def test_metrics_api():
    response = client.get("/api/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "roc_auc" in data
    assert data["roc_auc"] > 0.90
