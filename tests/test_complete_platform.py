"""
Comprehensive Test Suite for Hospital Readmission Predictor (HRP Clinical)
Tests Authentication, RBAC, Medical Documents, Certificates, ML/DL, RL, and Web Endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth import auth_manager
from ml.dataset_engine import dataset_engine
from ml.model_hub import model_hub
from ml.rl_engine import rl_engine
from ml.doc_engine import doc_engine
from ml.mlops_manager import mlops_manager
from ml.deep_models import TabularANN, TabularTransformer, PatientAutoencoder
import torch

client = TestClient(app)

# 1. Authentication & RBAC Tests
def test_authentication_success_and_failure():
    # Valid Doctor
    user, err = auth_manager.authenticate("dr.smith@hospital.org", "Doctor@2026!")
    assert err is None
    assert user["role"] == "Doctor"

    # Invalid Password
    user, err = auth_manager.authenticate("dr.smith@hospital.org", "WrongPassword!")
    assert user is None
    assert "Invalid email or password" in err

def test_mfa_otp_verification():
    otp = auth_manager.generate_otp("dr.smith@hospital.org")
    assert len(otp) == 6
    success, err = auth_manager.verify_otp("dr.smith@hospital.org", otp)
    assert success is True
    assert err is None

def test_break_glass_emergency_access():
    res = auth_manager.break_glass_access("dr.smith@hospital.org", "PT-84729", "Acute heart failure emergency triage")
    assert res["granted"] is True
    assert "AUD-" in res["audit_id"]

# 2. Medical Document & Certificate Intelligence Tests
def test_medical_documents_and_labs():
    doc = doc_engine.get_document("DOC-84729-LAB")
    assert doc is not None
    assert doc["patient_name"] == "Eleanor Vance"
    assert len(doc["extracted_labs"]) >= 5

    # Report chat Q&A
    chat_en = doc_engine.answer_report_question("DOC-84729-LAB", "What is my creatinine?")
    assert "1.60 mg/dL" in chat_en["answer"]

    chat_hi = doc_engine.answer_report_question("DOC-84729-LAB", "क्रिएटिनिन स्तर क्या है?", lang="hi")
    assert "1.60 mg/dL" in chat_hi["answer"]

def test_medical_certificate_generation_and_verification():
    cert = doc_engine.create_certificate_request({
        "patient_name": "Eleanor Vance",
        "patient_id": "PT-84729",
        "certificate_type": "Medical Fitness Certificate",
        "purpose": "Employment Verification",
        "rest_days": 14,
        "diagnosis": "Clinical Review"
    })
    assert cert["id"].startswith("CERT-")
    assert cert["verified"] is True

    # Check public verification endpoint
    resp = client.get(f"/verify-certificate/{cert['id']}")
    assert resp.status_code == 200
    assert "Valid &amp; Authorized" in resp.text or "Valid & Authorized" in resp.text

# 3. Machine Learning & PyTorch Deep Learning Tests
def test_dataset_workspace_and_profiling():
    profile = dataset_engine.get_profile()
    assert profile["dataset_info"]["records_count"] == 101766
    assert len(profile["missing_stats"]) == 10
    assert profile["class_distribution"]["imbalance_ratio"] == "1 : 7.96"

def test_pytorch_deep_learning_models():
    x = torch.randn(4, 24)
    ann = TabularANN(input_dim=24)
    out_ann = ann(x)
    assert out_ann.shape == (4, 1)

    trans = TabularTransformer(num_features=24)
    out_trans = trans(x)
    assert out_trans.shape == (4, 1)

    ae = PatientAutoencoder(input_dim=24, latent_dim=8)
    recon, latent = ae(x)
    assert recon.shape == (4, 24)
    assert latent.shape == (4, 8)

def test_model_hub_and_weighted_ensemble():
    models = model_hub.get_all_models()
    assert len(models) == 7
    xgb = model_hub.get_model("xgboost")
    assert xgb["roc_auc"] >= 0.97

    ensemble = model_hub.predict_ensemble({"length_of_stay": 4, "prev_admissions_30d": 1, "medication_count": 8})
    assert ensemble["ensemble_risk_pct"] > 0
    assert "agreement_indicator" in ensemble

def test_mlops_monitoring_and_chat():
    mon = mlops_manager.get_monitoring_metrics()
    assert "Normal" in mon["data_drift_status"]
    
    chat_res = mlops_manager.ask_model_analytics("What are the top features?")
    assert "SHAP" in chat_res["answer"] or "feature" in chat_res["answer"].lower()

# 4. Reinforcement Learning (RL) Tests
def test_reinforcement_learning_policy_and_safety():
    actions = rl_engine.env.get_action_library()
    assert len(actions) == 8

    rec = rl_engine.optimize_pathway_recommendation({"ml_risk_pct": 68, "prev_admissions_30d": 1, "medication_count": 8})
    assert rec["policy_id"] == "POL-PPO-v2.4"
    assert rec["human_review_required"] is True

    sim = rl_engine.run_digital_twin_simulation(initial_risk=68)
    assert "scenario_a" in sim
    assert "scenario_c" in sim

# 5. Digital Health ID & QR Verification Tests
def test_health_id_and_qr_verification():
    from app.qr_engine import qr_engine
    from app.account_manager import account_manager

    # 1. Verify Health ID Token
    res = qr_engine.verify_token("QRT-EV-HEALTHID-1042")
    assert res["valid"] is True
    assert "Eleanor Vance" in res["token"]["subject_name"]

    # 2. Verify Doctor Profile Token
    res_doc = qr_engine.verify_token("QRT-DOC-ARIS-88219")
    assert res_doc["valid"] is True
    assert "Dr. J. Aris" in res_doc["token"]["subject_name"]

    # 3. Create & Revoke Temporary Share
    share = qr_engine.create_temporary_share("DOC-84729-LAB", "Eleanor Vance", "Dr. Miller", duration_hours=24)
    assert share["token_id"].startswith("QRT-SHARE-")
    assert qr_engine.verify_token(share["token_id"])["valid"] is True
    
    # Revoke
    qr_engine.revoke_share(share["token_id"])
    assert qr_engine.verify_token(share["token_id"])["valid"] is False

    # 4. Account Data Export Archive
    export = account_manager.generate_data_export_archive()
    assert "export_id" in export
    assert "patient_profile" in export
    assert export["patient_profile"]["health_id"] == "HRP-2026-0001042"

# 6. Web Routes Status Codes (200 OK across 50+ endpoints)
def test_all_web_routes():
    routes = [
        "/",
        "/dashboard",
        "/login",
        "/auth/landing",
        "/auth/mfa",
        "/auth/forgot-password",
        "/auth/register-patient",
        "/auth/register-doctor",
        "/auth/sessions",
        "/health-id",
        "/doctor-id",
        "/wallet",
        "/qr/scanner",
        "/qr/temporary-share",
        "/verify-id/QRT-EV-HEALTHID-1042",
        "/verify-doctor/QRT-DOC-ARIS-88219",
        "/verify-appointment/QRT-APT-99214",
        "/verify-share/QRT-SHARE-DOC84729",
        "/prediction/new",
        "/prediction/PT-84729",
        "/patient/PT-84729",
        "/patients",
        "/history",
        "/analytics",
        "/settings",
        "/help",
        "/documents",
        "/documents/analyze/DOC-84729-LAB",
        "/certificates",
        "/certificates/new",
        "/ml-dashboard",
        "/ml/dataset",
        "/ml/profiling",
        "/ml/preprocessing",
        "/ml/training",
        "/ml/deep-learning",
        "/ml/comparison",
        "/ml/xai",
        "/ml/embeddings",
        "/ml/ensemble",
        "/ml/monitoring",
        "/ml/registry",
        "/ml/experiments",
        "/ml/chat",
        "/rl/dashboard",
        "/rl/environment",
        "/rl/care-pathway",
        "/rl/simulation",
        "/rl/safety",
        "/rl/human-review",
        "/rl/architecture",
        "/consultation/careai",
        "/notifications",
        "/loading/dashboard",
        "/auth/mfa",
        "/portal/patient",
        "/portal/coordinator",
        "/admin/users",
        "/admin/doctor-verification",
        "/admin/audit-logs"
    ]
    for r in routes:
        res = client.get(r)
        assert res.status_code == 200, f"Route {r} returned status {res.status_code}"

def test_notifications_system():
    # 1. Test get list
    res = client.get("/api/notifications/list")
    assert res.status_code == 200
    data = res.json()
    assert "notifications" in data
    assert len(data["notifications"]) >= 1

    # 2. Test mark read
    first_id = data["notifications"][0]["id"]
    res = client.post("/api/notifications/mark-read", json={"notif_id": first_id})
    assert res.status_code == 200

    # 3. Test mark all read
    res = client.post("/api/notifications/mark-all-read")
    assert res.status_code == 200
    assert res.json()["unread_count"] == 0

    # 4. Test simulate new alert
    res = client.post("/api/notifications/simulate")
    assert res.status_code == 200
    sim_data = res.json()
    assert "NOTIF-" in sim_data["id"]
