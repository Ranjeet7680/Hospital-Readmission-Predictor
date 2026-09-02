"""
Model Intelligence & Explainability Verification Test Suite
Tests Platt calibration, 95% Confidence Intervals, TreeSHAP breakdowns,
Counterfactual What-If interventions, and Subgroup Fairness auditing.
"""

import pytest
from ml.predictor import predictor
from ml.model_hub import model_hub

def test_model_prediction_and_confidence_intervals():
    patient = {
        "age": 71,
        "gender": "Female",
        "creatinine": 1.60,
        "prev_admissions_30d": 1,
        "medication_count": 8,
        "primary_diagnosis": "Congestive Heart Failure (CHF)",
        "spo2": 94
    }
    res = predictor.predict(patient)
    assert res["risk_score"] >= 60
    assert "confidence_interval_95" in res
    assert res["confidence_interval_95"]["lower"] < res["confidence_interval_95"]["upper"]
    assert "Cardiorenal Metabolic Syndrome" in res["clinical_phenotype"]
    assert len(res["shap_breakdown"]) >= 5

def test_counterfactual_what_if_simulator():
    patient = {
        "age": 71,
        "creatinine": 1.60,
        "prev_admissions_30d": 1,
        "medication_count": 8,
        "primary_diagnosis": "CHF"
    }
    adjustments = {
        "creatinine": 1.10,
        "medication_count": 4,
        "follow_up_72h": True
    }
    cf = predictor.predict_counterfactual(patient, adjustments)
    assert cf["simulated_risk_score"] < cf["baseline_risk_score"]
    assert "-" in cf["risk_reduction_delta"]
    assert len(cf["applied_interventions"]) == 3

def test_subgroup_fairness_audit():
    audit = predictor.audit_fairness()
    assert audit["status"] == "Certified Fair & Unbiased"
    assert audit["metrics"]["demographic_parity_ratio"] > 0.80
    assert audit["metrics"]["equalized_odds_ratio"] > 0.80
    assert len(audit["subgroups"]) >= 3

def test_model_hub_promotion_and_ensemble():
    models = model_hub.get_all_models()
    assert len(models) >= 7
    promo = model_hub.promote_to_champion("xgboost")
    assert promo["new_status"] == "Active Champion"
    assert promo["roc_auc"] >= 0.97
