"""
Test Suite for CareAI Multilingual Female Voice & Chatbot Engine
Validates language support, speech prosody parameters, intent classification,
emergency guardrails, and model fine-tuning across 18 languages.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_careai_supported_languages():
    resp = client.get("/api/careai/languages")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert data["total_languages"] >= 16
    assert "en" in data["languages"]
    assert "hi" in data["languages"]
    assert "es" in data["languages"]
    assert "bn" in data["languages"]
    assert "ta" in data["languages"]

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

def test_careai_emergency_guardrail_hindi():
    resp = client.post("/api/careai/chat", json={
        "message": "सीने में तेज दर्द हो रहा है और सांस फूल रही है",
        "lang": "hi"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "EMERGENCY_RED_FLAG"
    assert data["urgency"] == "CRITICAL_RED"
    assert "112" in data["response"] or "108" in data["response"]

def test_careai_medication_guidance_spanish():
    resp = client.post("/api/careai/chat", json={
        "message": "¿Cuándo debo tomar mi dosis de Metformina e insulina?",
        "lang": "es"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["intent"] == "MEDICATION_GUIDANCE"
    assert "Metformina" in data["response"] or "insulina" in data["response"]

def test_careai_model_training_endpoint():
    resp = client.post("/api/careai/train", json={})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert "metrics" in data
    assert data["metrics"]["intent_accuracy"] >= 0.95

def test_careai_studio_page():
    resp = client.get("/careai")
    assert resp.status_code == 200
    assert "CareAI" in resp.text
    assert "Female Voice" in resp.text or "Dr. Sophia" in resp.text
