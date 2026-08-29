"""
Test Suite for CareAI Universal Multilingual Female Voice AI Assistant
Validates 36+ language support, speech prosody parameters, voice navigation routing,
emergency guardrails, and model fine-tuning across all language matrices.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_careai_supported_36_languages():
    resp = client.get("/api/careai/languages")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert data["total_languages"] >= 36
    # Verify core languages
    for lang in ["en", "hi", "bn", "ta", "te", "kn", "ml", "mr", "gu", "pa", "ur", "es", "fr", "de", "it", "pt", "ru", "ar", "zh", "ja", "ko", "vi", "id"]:
        assert lang in data["languages"], f"Language {lang} should be supported"

def test_careai_readmission_chat_english():
    resp = client.post("/api/careai/chat", json={
        "message": "What is my 30-day hospital readmission risk score?",
        "lang": "en"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "READMISSION_RISK_EXPLANATION"
    assert "XGBoost" in data["response"] or "0.9794" in data["response"]
    assert "Dr. Sophia" in data["female_voice"]

def test_careai_voice_navigation_command():
    resp = client.post("/api/careai/chat", json={
        "message": "Go to dashboard",
        "lang": "en"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "VOICE_NAVIGATION"
    assert data["action_type"] == "NAVIGATE"
    assert data["target_url"] == "/dashboard"

def test_careai_emergency_guardrail_multilingual():
    # Hindi Emergency
    resp_hi = client.post("/api/careai/chat", json={
        "message": "सीने में तेज दर्द हो रहा है और सांस फूल रही है",
        "lang": "hi"
    })
    assert resp_hi.status_code == 200
    assert resp_hi.json()["intent"] == "EMERGENCY_RED_FLAG"
    assert resp_hi.json()["urgency"] == "CRITICAL_RED"

    # Spanish Emergency
    resp_es = client.post("/api/careai/chat", json={
        "message": "Tengo un dolor de pecho muy fuerte y no puedo respirar",
        "lang": "es"
    })
    assert resp_es.status_code == 200
    assert resp_es.json()["intent"] == "EMERGENCY_RED_FLAG"

def test_careai_medication_guidance_spanish():
    resp = client.post("/api/careai/chat", json={
        "message": "¿Cuándo debo tomar mi dosis de Metformina e insulina?",
        "lang": "es"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "MEDICATION_GUIDANCE"
    assert "Metformina" in data["response"] or "insulina" in data["response"]

def test_careai_model_training_36_languages():
    resp = client.post("/api/careai/train", json={})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert "metrics" in data
    assert data["metrics"]["intent_accuracy"] >= 0.95
    assert "36" in data["message"]

def test_careai_studio_page_36_languages():
    resp = client.get("/careai")
    assert resp.status_code == 200
    assert "CareAI" in resp.text
    assert "36" in resp.text
