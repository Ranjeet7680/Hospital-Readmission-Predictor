"""
Extended Backend & API Verification Test Suite for HRP Clinical Platform
Tests Digital Twin Sandbox, PPO RL Pathways, FHIR R4 Interoperability,
Batch Ingestion, MLOps Telemetry, Drift Detection, and 36-Language APIs.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rl_simulate_digital_twin():
    resp = client.post("/api/rl/simulate", json={
        "initial_risk": 72.5,
        "patient_id": "PT-84729",
        "interventions": ["pharmacist_review", "pcp_followup_72h"]
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert data["patient_id"] == "PT-84729"
    assert "scenario_a" in data["simulation"]
    assert "scenario_c" in data["simulation"]
    assert data["recommended_pathway"]["policy_id"] == "POL-PPO-v2.4"

def test_rl_policy_catalog_and_action_approval():
    # Policies Catalog
    resp_pol = client.get("/api/rl/policies")
    assert resp_pol.status_code == 200
    data_pol = resp_pol.json()
    assert len(data_pol["policies"]) >= 3
    assert len(data_pol["action_library"]) == 8

    # Clinician Approval Gate
    resp_app = client.post("/api/rl/approve-action", json={
        "action_id": 3,
        "patient_id": "PT-84729",
        "clinician": "Dr. J. Aris, MD"
    })
    assert resp_app.status_code == 200
    assert resp_app.json()["status"] == "success"
    assert "approved" in resp_app.json()["message"]

def test_batch_prediction_cohort():
    cohort = [
        {"id": "PT-001", "name": "Patient 1", "age": 70, "creatinine": 1.8, "p30": 1, "meds": 9},
        {"id": "PT-002", "name": "Patient 2", "age": 52, "creatinine": 0.8, "p30": 0, "meds": 3}
    ]
    resp = client.post("/api/predict/batch", json={"patients": cohort})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert data["total_patients"] == 2
    assert len(data["predictions"]) == 2
    assert data["predictions"][0]["risk_tier"] == "High"
    assert data["predictions"][1]["risk_tier"] in ["Low", "Moderate"]

def test_fhir_r4_interoperability():
    # Patient Resource
    resp_pt = client.get("/api/fhir/Patient/PT-84729")
    assert resp_pt.status_code == 200
    pt_data = resp_pt.json()
    assert pt_data["resourceType"] == "Patient"
    assert pt_data["id"] == "PT-84729"
    assert pt_data["gender"] == "female"

    # Observation Bundle
    resp_obs = client.get("/api/fhir/Observation/PT-84729")
    assert resp_obs.status_code == 200
    obs_data = resp_obs.json()
    assert obs_data["resourceType"] == "Bundle"
    assert len(obs_data["entry"]) >= 2

    # Encounter Resource
    resp_enc = client.get("/api/fhir/Encounter/PT-84729")
    assert resp_enc.status_code == 200
    assert resp_enc.json()["resourceType"] == "Encounter"

def test_mlops_drift_and_telemetry():
    # Drift Check
    resp_drift = client.post("/api/mlops/drift-check", json={})
    assert resp_drift.status_code == 200
    drift_data = resp_drift.json()
    assert drift_data["status"] == "success"
    assert "population_stability_index" in drift_data
    assert drift_data["evaluated_features"] == 24

    # Production Telemetry
    resp_telem = client.get("/api/mlops/telemetry")
    assert resp_telem.status_code == 200
    assert resp_telem.json()["roc_auc"] >= 0.97
    assert resp_telem.json()["avg_inference_latency_ms"] < 25.0

    # Model Promotion
    resp_promo = client.post("/api/mlops/promote-model", json={"model_id": "xgboost"})
    assert resp_promo.status_code == 200
    assert resp_promo.json()["status"] == "success"

def test_notifications_dispatch():
    resp = client.post("/api/notifications/dispatch", json={
        "patient_id": "PT-84729",
        "type": "CLINICAL_RISK_ALERT",
        "message": "High readmission risk detected (68.4%). 72h PCP scheduled."
    })
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"
    assert "notification_id" in resp.json()

def test_i18n_36_languages_sync():
    # Set Language to Telugu
    resp_set = client.post("/api/i18n/set-language", json={"lang": "te"})
    assert resp_set.status_code == 200
    assert resp_set.json()["lang"] == "te"
    assert "Dr. Kavya" in resp_set.json()["voice_persona"]

    # Get Translations Metadata
    resp_trans = client.get("/api/i18n/translations?lang=te")
    assert resp_trans.status_code == 200
    assert resp_trans.json()["total_supported"] >= 36
    assert resp_trans.json()["metadata"]["locale"] == "te-IN"

def test_health_and_security_headers():
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json()["status"] == "healthy"
    assert resp.json()["models_ready"] is True
    assert "X-Content-Type-Options" in resp.headers
    assert resp.headers["X-Content-Type-Options"] == "nosniff"

def test_patient_search_and_pagination():
    resp = client.get("/api/patients/search?q=Eleanor&page=1&page_size=5")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert data["data"]["total_count"] >= 1
    assert "Eleanor Vance" in data["data"]["patients"][0]["name"]

def test_audit_logs_api():
    resp = client.get("/api/admin/audit-logs")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert "logs" in data

def test_cds_hooks_discovery_and_patient_view():
    # Discovery
    resp_disc = client.get("/api/cds-services")
    assert resp_disc.status_code == 200
    assert len(resp_disc.json()["services"]) >= 1
    assert resp_disc.json()["services"][0]["hook"] == "patient-view"

    # Patient-View Hook Handler
    resp_hook = client.post("/api/cds-services/patient-view", json={
        "hook": "patient-view",
        "context": {"patientId": "PT-84729"}
    })
    assert resp_hook.status_code == 200
    assert len(resp_hook.json()["cards"]) >= 1
    assert "warning" in resp_hook.json()["cards"][0]["indicator"]

def test_database_backup_and_restore():
    # Export Snapshot
    resp_exp = client.get("/api/admin/backup/export")
    assert resp_exp.status_code == 200
    assert "patients" in resp_exp.json()
    assert "signature" in resp_exp.json()

    # Restore Snapshot
    resp_res = client.post("/api/admin/backup/restore", json={
        "patients": {"PT-BACKUP-01": {"id": "PT-BACKUP-01", "name": "Backup Patient"}}
    })
    assert resp_res.status_code == 200
    assert resp_res.json()["status"] == "success"

def test_patient_clinical_summary_and_system_diagnostics():
    # Clinical Summary
    resp_sum = client.get("/api/patient/PT-84729/summary")
    assert resp_sum.status_code == 200
    assert resp_sum.json()["status"] == "success"
    assert "clinical_summary" in resp_sum.json()

    # System Diagnostics
    resp_diag = client.get("/api/system/diagnostics")
    assert resp_diag.status_code == 200
    assert resp_diag.json()["status"] == "operational"
    assert resp_diag.json()["serverless_ready"] is True

def test_clinical_rules_guidelines_and_pdf_export():
    # Clinical Rules Evaluation
    resp_rules = client.post("/api/clinical-rules/evaluate", json={
        "patient_id": "PT-84729",
        "age": 71,
        "gender": "Female",
        "creatinine": 1.60,
        "systolic_bp": 135,
        "diastolic_bp": 85,
        "hba1c": 7.4,
        "chf_history": 1
    })
    assert resp_rules.status_code == 200
    eval_data = resp_rules.json()["evaluation"]
    assert eval_data["egfr_ckd_epi"] < 60.0
    assert len(eval_data["guideline_flags"]) >= 1
    assert "KDIGO" in eval_data["guideline_flags"][0]["guideline"]

    # PDF / HTML Report Export
    resp_pdf = client.get("/api/reports/clinical-summary-pdf/PT-84729")
    assert resp_pdf.status_code == 200
    assert "HRP Clinical AI" in resp_pdf.text
    assert "Eleanor Vance" in resp_pdf.text

def test_backend_hub_pages():
    resp_hub1 = client.get("/admin/backend-hub")
    assert resp_hub1.status_code == 200
    assert "Backend Architecture &amp; API Control Hub" in resp_hub1.text or "Backend Architecture & API Control Hub" in resp_hub1.text

    resp_hub2 = client.get("/portal/backend-hub")
    assert resp_hub2.status_code == 200




