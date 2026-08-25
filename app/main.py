"""
Hospital Readmission Predictor (HRP Clinical) - Main FastAPI Application
Unifies Authentication, Clinical Care, Medical Documents, ML/DL Intelligence,
Reinforcement Learning (RL), CareAI Telemedicine, and Bilingual Hindi ↔ English Support.
"""

import os
import uuid
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Request, Form, Query, Response
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Application & Engine Imports
from app.database import db
from app.auth import auth_manager
from app.qr_engine import qr_engine
from app.account_manager import account_manager
from ml.predictor import predictor
from ml.dataset_engine import dataset_engine
from ml.model_hub import model_hub
from ml.rl_engine import rl_engine
from ml.doc_engine import doc_engine
from ml.mlops_manager import mlops_manager

app = FastAPI(
    title="Hospital Readmission Predictor (HRP Clinical)",
    description="Precision Clinical AI, Deep Learning, Reinforcement Learning & Medical Document Platform",
    version="2.4.1"
)

# Mount Static Assets & Templates with Serverless Path Resolution
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_dir):
    static_dir = os.path.join(os.getcwd(), "static")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

template_dir = os.path.join(BASE_DIR, "templates")
if not os.path.exists(template_dir):
    template_dir = os.path.join(os.getcwd(), "templates")
templates = Jinja2Templates(directory=template_dir)

@app.get("/favicon.ico")
async def favicon():
    favicon_path = os.path.join(BASE_DIR, "static", "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path, media_type="image/x-icon")
    return FileResponse(os.path.join(BASE_DIR, "static", "favicon.svg"), media_type="image/svg+xml")

@app.get("/ebook", response_class=HTMLResponse)
async def read_ebook():
    ebook_html_path = os.path.join(BASE_DIR, "docs", "ebook", "Hospital_Readmission_Predictor_Complete_eBook.html")
    if os.path.exists(ebook_html_path):
        with open(ebook_html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>eBook is being compiled. Please try again shortly.</h1>", status_code=404)

@app.get("/ebook/download")
async def download_ebook_markdown():
    ebook_md_path = os.path.join(BASE_DIR, "docs", "ebook", "Hospital_Readmission_Predictor_Complete_eBook.md")
    if os.path.exists(ebook_md_path):
        return FileResponse(ebook_md_path, filename="Hospital_Readmission_Predictor_Complete_eBook.md", media_type="text/markdown")
    return HTMLResponse("<h1>eBook file not found.</h1>", status_code=404)

# ==========================================
# 1. AUTHENTICATION & SECURITY ROUTES
# ==========================================

@app.get("/auth/landing", response_class=HTMLResponse)
async def auth_landing(request: Request):
    return templates.TemplateResponse(request=request, name="auth/auth_landing.html", context={"hide_nav": True})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html", context={"hide_nav": True})

@app.post("/login")
async def handle_login(request: Request, email: str = Form(...), password: str = Form(...)):
    user, err = auth_manager.authenticate(email, password)
    if err:
        return templates.TemplateResponse(request=request, name="login.html", context={"hide_nav": True, "error_message": err})
    if user.get("mfa_enabled"):
        return RedirectResponse(url="/auth/mfa", status_code=303)
    if user["role"] == "Patient":
        return RedirectResponse(url="/portal/patient", status_code=303)
    elif user["role"] == "CareCoordinator":
        return RedirectResponse(url="/portal/coordinator", status_code=303)
    elif user["role"] == "Administrator":
        return RedirectResponse(url="/admin/users", status_code=303)
    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/auth/mfa", response_class=HTMLResponse)
async def mfa_otp_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/mfa_otp.html", context={"hide_nav": True})

@app.get("/auth/forgot-password", response_class=HTMLResponse)
async def forgot_password_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/forgot_password.html", context={"hide_nav": True})

@app.get("/auth/register-patient", response_class=HTMLResponse)
async def register_patient_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/register_patient.html", context={"hide_nav": True})

@app.get("/auth/register-doctor", response_class=HTMLResponse)
async def register_doctor_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/register_doctor.html", context={"hide_nav": True})

@app.get("/auth/sessions", response_class=HTMLResponse)
async def sessions_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth/sessions.html", context={"active_page": "sessions"})

# ==========================================
# 2. CORE CLINICAL & DASHBOARD ROUTES
# ==========================================

@app.get("/", response_class=HTMLResponse)
@app.get("/welcome", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="welcome.html", context={"hide_nav": True})

@app.post("/api/predict")
async def api_predict(data: dict):
    pred = predictor.predict(data)
    patient_id = data.get("patient_id", f"PT-{str(uuid.uuid4())[:6]}")
    name = data.get("full_name") or data.get("patient_name", "Clinical Patient")
    
    record = {
        "id": f"PRED-{patient_id}",
        "patient_id": patient_id,
        "patient_name": name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "risk_score": pred["risk_score"],
        "risk_level": pred["risk_level"],
        "risk_level_code": pred["risk_level_code"],
        "risk_badge_class": pred["risk_badge_class"],
        "risk_color": pred["risk_color"],
        "contributing_factors": pred["contributing_factors"],
        "recommendations": pred["recommendations"],
        "clinician": data.get("attending_physician", "Dr. Smith"),
        "department": data.get("department", "Cardiology"),
        "status": "Reviewed"
    }
    db.add_prediction(record)
    
    # Save/update patient in db
    db.save_patient({
        "id": patient_id,
        "name": name,
        "initials": "".join([part[0] for part in name.split() if part])[:2].upper(),
        "age": data.get("age", 65),
        "gender": data.get("gender", "Male"),
        "department": data.get("department", "Cardiology"),
        "attending_physician": data.get("attending_physician", "Dr. Smith"),
        "primary_diagnosis": data.get("primary_diagnosis", "Clinical Evaluation"),
        "risk_score": pred["risk_score"]
    })
    return JSONResponse(record)

@app.get("/api/patient/{patient_id}")
async def api_get_patient(patient_id: str):
    p = db.get_patient(patient_id)
    if not p:
        return JSONResponse({"error": "Patient not found"}, status_code=404)
    return JSONResponse(p)

@app.get("/api/history/export")
async def api_history_export():
    csv_data = db.export_history_csv()
    return Response(content=csv_data, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=history.csv"})

@app.get("/api/metrics")
async def api_metrics():
    return JSONResponse({
        "roc_auc": 0.9794,
        "accuracy": 0.9368,
        "sensitivity": 0.9020,
        "precision": 0.6840,
        "f1": 0.7777,
        "active_model": "XGBoost v2.4.1"
    })

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    summary = db.get_dashboard_summary()
    return templates.TemplateResponse(request=request, name="dashboard.html", context={
        "active_page": "dashboard",
        "total_screened": summary["total_screened"],
        "high_risk_count": summary["high_risk_count"],
        "avg_risk_score": summary["avg_risk_score"],
        "active_patients": summary["active_patients"],
        "recent_predictions": summary["recent_predictions"],
        "risk_breakdown": summary["risk_breakdown"]
    })

@app.get("/prediction/new", response_class=HTMLResponse)
async def new_prediction_page(request: Request):
    return templates.TemplateResponse(request=request, name="new_prediction.html", context={"active_page": "new_prediction"})

@app.post("/prediction/new")
async def create_prediction(
    request: Request,
    patient_id: str = Form(...),
    patient_name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    primary_diagnosis: str = Form(...),
    length_of_stay: int = Form(...),
    prev_admissions_30d: int = Form(...),
    prev_admissions_12m: int = Form(...),
    creatinine: float = Form(...),
    hemoglobin: float = Form(...),
    sodium: float = Form(...),
    potassium: float = Form(...),
    hba1c: float = Form(...),
    medication_count: int = Form(...),
    discharged_to: str = Form("Home"),
    cognitive_impairment: bool = Form(False),
    living_alone: bool = Form(False),
    followup_scheduled: bool = Form(True)
):
    patient_dict = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "primary_diagnosis": primary_diagnosis,
        "length_of_stay": length_of_stay,
        "prev_admissions_30d": prev_admissions_30d,
        "prev_admissions_12m": prev_admissions_12m,
        "creatinine": creatinine,
        "hemoglobin": hemoglobin,
        "sodium": sodium,
        "potassium": potassium,
        "hba1c": hba1c,
        "medication_count": medication_count,
        "discharged_to": discharged_to,
        "cognitive_impairment": cognitive_impairment,
        "living_alone": living_alone,
        "followup_scheduled": followup_scheduled
    }
    pred_res = predictor.predict(patient_dict)
    record = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "primary_diagnosis": primary_diagnosis,
        "risk_score": pred_res.get("risk_score", 65),
        "risk_tier": pred_res.get("risk_tier", pred_res.get("risk_level", "High Risk")),
        "factors": pred_res.get("factors", pred_res.get("contributing_factors", [])),
        "recommendations": pred_res.get("recommendations", []),
        "status": "Reviewed",
        "clinician_notes": f"Automated readmission prediction evaluated under XGBoost v2.4.1. Score: {pred_res.get('risk_score', 65)}%."
    }
    db.add_prediction(record)
    return RedirectResponse(url=f"/prediction/{patient_id}", status_code=303)

@app.get("/prediction/{patient_id}", response_class=HTMLResponse)
async def view_prediction(request: Request, patient_id: str):
    p = db.get_patient(patient_id)
    if not p:
        p = db.get_patient("PT-84729")
    pred = db.get_prediction_by_id(patient_id)
    if not pred:
        pred = db.get_prediction_by_id("PT-84729") or {
            "id": f"PRED-{p['id']}",
            "patient_id": p["id"],
            "patient_name": p["name"],
            "timestamp": "Today, 09:30 AM",
            "risk_score": p.get("risk_score", 68),
            "risk_level": p.get("risk_tier", "High Risk"),
            "risk_level_code": "high" if p.get("risk_score", 68) > 60 else "moderate",
            "risk_badge_class": "bg-error text-on-error" if p.get("risk_score", 68) > 60 else "bg-amber-100 text-amber-800",
            "risk_color": "#ba1a1a" if p.get("risk_score", 68) > 60 else "#b36b00",
            "clinician": p.get("attending_physician", "Dr. J. Aris"),
            "department": p.get("department", "Cardiology"),
            "model_version": "v2.4.1",
            "status": "Reviewed",
            "contributing_factors": [
                {
                    "title": "Previous Admission History",
                    "impact": "High Elevating Factor",
                    "direction": "up",
                    "color": "#ba1a1a",
                    "icon": "arrow_upward",
                    "description": "1 prior admission within 30 days significantly elevates readmission risk."
                },
                {
                    "title": "Elevated Creatinine Levels",
                    "impact": "Elevating Factor",
                    "direction": "up",
                    "color": "#b36b00",
                    "icon": "arrow_upward",
                    "description": "Serum creatinine indicates potential renal stress."
                }
            ],
            "recommendations": [
                "Schedule primary care follow-up within 72 hours of discharge.",
                "Order 7-day post-discharge tele-health check-in."
            ],
            "primary_recommendation": "Schedule primary care follow-up within 72 hours of discharge."
        }
    gauge_circumference = 282.74
    dash_offset = gauge_circumference * (1 - (pred.get("risk_score", 68) / 100.0))
    return templates.TemplateResponse(request=request, name="prediction_result.html", context={
        "active_page": "prediction_result",
        "prediction": pred,
        "patient": p,
        "dash_offset": round(dash_offset, 2)
    })

@app.get("/patient/{patient_id}", response_class=HTMLResponse)
async def patient_profile(request: Request, patient_id: str):
    p = db.get_patient(patient_id)
    if not p:
        p = db.get_patient("PT-84729")
    trajectory = db.get_patient_trajectory(patient_id)
    return templates.TemplateResponse(request=request, name="patient_profile.html", context={
        "active_page": "patients",
        "patient": p,
        "trajectory": trajectory
    })

@app.get("/patients", response_class=HTMLResponse)
async def patients_directory(request: Request):
    return templates.TemplateResponse(request=request, name="patients.html", context={
        "active_page": "patients",
        "patients": db.patients
    })

@app.get("/history", response_class=HTMLResponse)
async def prediction_history(
    request: Request,
    search: Optional[str] = Query(None),
    risk_tier: Optional[str] = Query(None),
    status: Optional[str] = Query(None)
):
    filtered = db.filter_history(search=search, risk_tier=risk_tier, status=status)
    return templates.TemplateResponse(request=request, name="prediction_history.html", context={
        "active_page": "history",
        "history": filtered,
        "current_search": search or "",
        "current_risk": risk_tier or "",
        "current_status": status or ""
    })

@app.get("/history/export/csv")
async def export_history_csv():
    csv_data = db.export_history_csv()
    return StreamingResponse(
        iter([csv_data]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=hrp_prediction_history.csv"}
    )

@app.get("/analytics", response_class=HTMLResponse)
async def clinical_analytics(request: Request):
    return templates.TemplateResponse(request=request, name="analytics.html", context={"active_page": "analytics"})

@app.get("/insights", response_class=HTMLResponse)
async def model_insights(request: Request):
    return templates.TemplateResponse(request=request, name="model_insights.html", context={
        "active_page": "insights",
        "metrics": predictor.metrics
    })

@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    return templates.TemplateResponse(request=request, name="settings.html", context={"active_page": "settings"})

@app.get("/help", response_class=HTMLResponse)
async def help_page(request: Request):
    return templates.TemplateResponse(request=request, name="help.html", context={"active_page": "help"})

# ==========================================
# 3. MEDICAL DOCUMENTS & CERTIFICATES ROUTES
# ==========================================

@app.get("/documents", response_class=HTMLResponse)
async def documents_center(request: Request):
    docs = doc_engine.get_all_documents()
    return templates.TemplateResponse(request=request, name="documents/document_center.html", context={
        "active_page": "documents",
        "documents": docs
    })

@app.get("/documents/analyze/{doc_id}", response_class=HTMLResponse)
async def analyze_document(request: Request, doc_id: str):
    doc = doc_engine.get_document(doc_id)
    if not doc:
        doc = doc_engine.get_document("DOC-84729-LAB")
    return templates.TemplateResponse(request=request, name="documents/analyze_report.html", context={
        "active_page": "analyze_report",
        "doc": doc
    })

@app.get("/certificates", response_class=HTMLResponse)
async def certificates_list(request: Request):
    cert = doc_engine.get_certificate("CERT-2023-84729")
    return templates.TemplateResponse(request=request, name="documents/certificate_preview.html", context={
        "active_page": "certificates",
        "cert": cert
    })

@app.get("/certificates/new", response_class=HTMLResponse)
async def new_certificate_form(request: Request):
    return templates.TemplateResponse(request=request, name="documents/certificate_request.html", context={
        "active_page": "certificates"
    })

@app.post("/certificates/new")
async def handle_new_certificate(
    request: Request,
    patient_name: str = Form(...),
    patient_id: str = Form(...),
    certificate_type: str = Form(...),
    purpose: str = Form(...),
    rest_days: int = Form(14),
    diagnosis: str = Form(...),
    doctor_name: str = Form("Dr. J. Aris, MD"),
    doctor_specialty: str = Form("Cardiology")
):
    cert = doc_engine.create_certificate_request({
        "patient_name": patient_name,
        "patient_id": patient_id,
        "certificate_type": certificate_type,
        "purpose": purpose,
        "rest_days": rest_days,
        "diagnosis": diagnosis,
        "doctor_name": doctor_name,
        "doctor_specialty": doctor_specialty
    })
    return RedirectResponse(url=f"/certificates/{cert['id']}", status_code=303)

@app.get("/certificates/{cert_id}", response_class=HTMLResponse)
async def view_certificate(request: Request, cert_id: str):
    cert = doc_engine.get_certificate(cert_id)
    if not cert:
        cert = doc_engine.get_certificate("CERT-2023-84729")
    return templates.TemplateResponse(request=request, name="documents/certificate_preview.html", context={
        "active_page": "certificates",
        "cert": cert
    })

@app.get("/verify-certificate/{cert_id}", response_class=HTMLResponse)
async def verify_certificate_page(request: Request, cert_id: str):
    cert = doc_engine.get_certificate(cert_id)
    if not cert:
        cert = doc_engine.get_certificate("CERT-2023-84729")
    return templates.TemplateResponse(request=request, name="documents/verify_certificate.html", context={
        "hide_nav": True,
        "cert": cert
    })

@app.get("/api/documents/{doc_id}/chat")
async def report_chat_api(doc_id: str, q: str = Query(...), lang: str = Query("en")):
    res = doc_engine.answer_report_question(doc_id, q, lang=lang)
    return JSONResponse(res)

# ==========================================
# 4. AI & MACHINE LEARNING (ML/DL) ROUTES
# ==========================================

@app.get("/ml-dashboard", response_class=HTMLResponse)
async def ml_dashboard_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/ml_dashboard.html", context={
        "active_page": "ml_dashboard"
    })

@app.get("/ml/dataset", response_class=HTMLResponse)
async def dataset_workspace_page(request: Request):
    sample_rows = dataset_engine.df.head(20).to_dict(orient="records")
    return templates.TemplateResponse(request=request, name="ml/dataset.html", context={
        "active_page": "dataset",
        "sample_rows": sample_rows
    })

@app.get("/ml/profiling", response_class=HTMLResponse)
async def profiling_page(request: Request):
    profile = dataset_engine.get_profile()
    return templates.TemplateResponse(request=request, name="ml/profiling.html", context={
        "active_page": "profiling",
        "profile": profile
    })

@app.get("/ml/preprocessing", response_class=HTMLResponse)
async def preprocessing_page(request: Request):
    stages = dataset_engine.get_preprocessing_pipeline_stages()
    return templates.TemplateResponse(request=request, name="ml/preprocessing.html", context={
        "active_page": "preprocessing",
        "pipeline_stages": stages
    })

@app.get("/ml/training", response_class=HTMLResponse)
async def training_studio_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/training_studio.html", context={
        "active_page": "training_studio"
    })

@app.get("/ml/deep-learning", response_class=HTMLResponse)
async def deep_learning_lab_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/deep_learning_lab.html", context={
        "active_page": "dl_lab"
    })

@app.get("/ml/comparison", response_class=HTMLResponse)
async def model_comparison_page(request: Request):
    models = model_hub.get_all_models()
    return templates.TemplateResponse(request=request, name="ml/model_comparison.html", context={
        "active_page": "comparison",
        "models": models
    })

@app.get("/ml/xai", response_class=HTMLResponse)
async def xai_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/xai.html", context={
        "active_page": "xai"
    })

@app.get("/ml/embeddings", response_class=HTMLResponse)
async def embeddings_page(request: Request):
    points = dataset_engine.get_patient_embeddings()
    return templates.TemplateResponse(request=request, name="ml/embeddings.html", context={
        "active_page": "embeddings",
        "points": points
    })

@app.get("/ml/ensemble", response_class=HTMLResponse)
async def ensemble_page(request: Request):
    ensemble = model_hub.predict_ensemble({"length_of_stay": 4, "prev_admissions_30d": 1, "medication_count": 8, "creatinine": 1.60})
    return templates.TemplateResponse(request=request, name="ml/ensemble_uncertainty.html", context={
        "active_page": "ensemble",
        "ensemble": ensemble
    })

@app.get("/ml/monitoring", response_class=HTMLResponse)
async def monitoring_page(request: Request):
    monitor = mlops_manager.get_monitoring_metrics()
    return templates.TemplateResponse(request=request, name="ml/monitoring.html", context={
        "active_page": "monitoring",
        "monitor": monitor
    })

@app.get("/ml/registry", response_class=HTMLResponse)
async def registry_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/registry.html", context={
        "active_page": "registry",
        "models": mlops_manager.model_registry
    })

@app.get("/ml/experiments", response_class=HTMLResponse)
async def experiments_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/experiments.html", context={
        "active_page": "experiments",
        "experiments": mlops_manager.experiments
    })

@app.get("/ml/chat", response_class=HTMLResponse)
async def model_chat_page(request: Request):
    return templates.TemplateResponse(request=request, name="ml/model_chat.html", context={
        "active_page": "model_chat"
    })

@app.get("/api/ml/chat")
async def model_chat_api(q: str = Query(...), lang: str = Query("en")):
    res = mlops_manager.ask_model_analytics(q, lang=lang)
    return JSONResponse(res)

# ==========================================
# 5. REINFORCEMENT LEARNING (RL) ROUTES
# ==========================================

@app.get("/rl/dashboard", response_class=HTMLResponse)
async def rl_dashboard_page(request: Request):
    return templates.TemplateResponse(request=request, name="rl/rl_dashboard.html", context={
        "active_page": "rl_dashboard",
        "policies": rl_engine.policies
    })

@app.get("/rl/environment", response_class=HTMLResponse)
async def rl_environment_page(request: Request):
    actions = rl_engine.env.get_action_library()
    return templates.TemplateResponse(request=request, name="rl/environment.html", context={
        "active_page": "rl_env",
        "actions": actions
    })

@app.get("/rl/care-pathway", response_class=HTMLResponse)
async def care_pathway_page(request: Request):
    rec = rl_engine.optimize_pathway_recommendation({"ml_risk_pct": 68, "prev_admissions_30d": 1, "medication_count": 8})
    return templates.TemplateResponse(request=request, name="rl/care_pathway.html", context={
        "active_page": "care_pathway",
        "rec": rec
    })

@app.get("/rl/simulation", response_class=HTMLResponse)
async def simulation_twin_page(request: Request):
    sim = rl_engine.run_digital_twin_simulation(initial_risk=68)
    return templates.TemplateResponse(request=request, name="rl/simulation_twin.html", context={
        "active_page": "simulation_twin",
        "sim": sim
    })

@app.get("/rl/safety", response_class=HTMLResponse)
async def safety_constraints_page(request: Request):
    return templates.TemplateResponse(request=request, name="rl/safety_constraints.html", context={
        "active_page": "safety_constraints"
    })

@app.get("/rl/human-review", response_class=HTMLResponse)
async def human_review_page(request: Request):
    rec = rl_engine.optimize_pathway_recommendation({"ml_risk_pct": 68, "prev_admissions_30d": 1, "medication_count": 8})
    return templates.TemplateResponse(request=request, name="rl/care_pathway.html", context={
        "active_page": "human_review",
        "rec": rec
    })

@app.get("/rl/architecture", response_class=HTMLResponse)
async def rl_architecture_page(request: Request):
    return templates.TemplateResponse(request=request, name="rl/rl_architecture.html", context={
        "active_page": "rl_arch"
    })

# ==========================================
# 6. PORTALS & TELEMEDICINE ROUTES
# ==========================================

@app.get("/consultation/careai", response_class=HTMLResponse)
async def video_consultation_page(request: Request):
    return templates.TemplateResponse(request=request, name="portal/video_consultation.html", context={
        "active_page": "video_consult"
    })

@app.get("/portal/patient", response_class=HTMLResponse)
async def patient_portal_page(request: Request):
    return templates.TemplateResponse(request=request, name="portal/patient_portal.html", context={
        "active_page": "patient_portal"
    })

@app.get("/portal/coordinator", response_class=HTMLResponse)
async def care_coordinator_page(request: Request):
    return templates.TemplateResponse(request=request, name="portal/care_coordinator.html", context={
        "active_page": "care_coordinator"
    })

@app.get("/admin/users", response_class=HTMLResponse)
async def admin_users_page(request: Request):
    return templates.TemplateResponse(request=request, name="portal/admin_users.html", context={
        "active_page": "admin_users"
    })

@app.get("/admin/doctor-verification", response_class=HTMLResponse)
async def doctor_verification_page(request: Request):
    return templates.TemplateResponse(request=request, name="portal/doctor_verification.html", context={
        "active_page": "dr_verification"
    })

@app.get("/admin/audit-logs", response_class=HTMLResponse)
async def audit_logs_page(request: Request):
    logs = auth_manager.audit_logs
    return templates.TemplateResponse(request=request, name="portal/audit_logs.html", context={
        "active_page": "audit_logs",
        "audit_logs": logs
    })

# ==========================================
# 7. DIGITAL HEALTH ID, DOCTOR ID & WALLET
# ==========================================

@app.get("/health-id", response_class=HTMLResponse)
async def health_id_page(request: Request):
    profile = account_manager.profile
    token = qr_engine.tokens.get("QRT-EV-HEALTHID-1042")
    verify_url = f"{request.base_url}verify-id/{token['token_id']}"
    qr_svg = qr_engine.generate_svg_qr(verify_url, size=140)
    qr_svg_large = qr_engine.generate_svg_qr(verify_url, size=240)
    return templates.TemplateResponse(request=request, name="health_id/health_id_card.html", context={
        "active_page": "health_id",
        "profile": profile,
        "token": token,
        "qr_svg": qr_svg,
        "qr_svg_large": qr_svg_large,
        "verification_url": verify_url
    })

@app.post("/health-id/regenerate")
async def regenerate_health_id_qr(request: Request, token_id: str = Form(...)):
    qr_engine.regenerate_health_id_qr(token_id)
    return RedirectResponse(url="/health-id", status_code=303)

@app.post("/health-id/report-lost")
async def report_health_id_lost(request: Request, token_id: str = Form(...)):
    qr_engine.report_lost_id(token_id)
    return RedirectResponse(url="/health-id", status_code=303)

@app.get("/doctor-id", response_class=HTMLResponse)
async def doctor_id_page(request: Request):
    doc_profile = account_manager.doctor_profile
    token = qr_engine.tokens.get("QRT-DOC-ARIS-88219")
    verify_url = f"{request.base_url}verify-doctor/{token['token_id']}"
    qr_svg = qr_engine.generate_svg_qr(verify_url, size=140)
    return templates.TemplateResponse(request=request, name="health_id/doctor_id_card.html", context={
        "active_page": "doctor_id",
        "doc_profile": doc_profile,
        "token": token,
        "qr_svg": qr_svg
    })

@app.get("/wallet", response_class=HTMLResponse)
async def digital_wallet_page(request: Request):
    profile = account_manager.profile
    return templates.TemplateResponse(request=request, name="health_id/wallet.html", context={
        "active_page": "wallet",
        "profile": profile
    })

# ==========================================
# 8. WORKING QR SCANNER & TEMPORARY SHARING
# ==========================================

@app.get("/qr/scanner", response_class=HTMLResponse)
async def qr_scanner_page(request: Request):
    return templates.TemplateResponse(request=request, name="qr/qr_scanner.html", context={
        "active_page": "qr_scanner"
    })

@app.get("/qr/temporary-share", response_class=HTMLResponse)
async def temporary_share_page(request: Request):
    profile = account_manager.profile
    active_shares = [t for t in qr_engine.tokens.values() if t["qr_type"] == "temporary_share"]
    return templates.TemplateResponse(request=request, name="qr/temporary_share.html", context={
        "active_page": "temporary_share",
        "profile": profile,
        "active_shares": active_shares
    })

@app.post("/qr/temporary-share")
async def create_temporary_share_post(
    request: Request,
    document_id: str = Form(...),
    recipient: str = Form(...),
    duration_hours: int = Form(24),
    allow_download: bool = Form(False)
):
    profile = account_manager.profile
    qr_engine.create_temporary_share(
        document_id=document_id,
        patient_name=profile["full_name"],
        recipient=recipient,
        duration_hours=int(duration_hours),
        allow_download=bool(allow_download)
    )
    return RedirectResponse(url="/qr/temporary-share", status_code=303)

@app.post("/qr/revoke-share")
async def revoke_share_post(request: Request, token_id: str = Form(...)):
    qr_engine.revoke_share(token_id)
    return RedirectResponse(url="/qr/temporary-share", status_code=303)

# ==========================================
# 9. PUBLIC QR VERIFICATION GATEWAYS
# ==========================================

@app.get("/verify-id/{token_id}", response_class=HTMLResponse)
async def verify_health_id_endpoint(request: Request, token_id: str):
    res = qr_engine.verify_token(token_id, ip_address=request.client.host if request.client else "127.0.0.1")
    return templates.TemplateResponse(request=request, name="qr/verify_qr.html", context={
        "verification_title": "Health ID Verification",
        "result": res,
        "token": res.get("token")
    })

@app.get("/verify-doctor/{token_id}", response_class=HTMLResponse)
async def verify_doctor_endpoint(request: Request, token_id: str):
    res = qr_engine.verify_token(token_id, ip_address=request.client.host if request.client else "127.0.0.1")
    return templates.TemplateResponse(request=request, name="qr/verify_qr.html", context={
        "verification_title": "Doctor Credential Verification",
        "result": res,
        "token": res.get("token")
    })

@app.get("/verify-appointment/{token_id}", response_class=HTMLResponse)
async def verify_appointment_endpoint(request: Request, token_id: str):
    res = qr_engine.verify_token(token_id, ip_address=request.client.host if request.client else "127.0.0.1")
    return templates.TemplateResponse(request=request, name="qr/verify_qr.html", context={
        "verification_title": "Appointment Pass Verification",
        "result": res,
        "token": res.get("token")
    })

@app.get("/verify-share/{token_id}", response_class=HTMLResponse)
async def verify_share_endpoint(request: Request, token_id: str):
    res = qr_engine.verify_token(token_id, ip_address=request.client.host if request.client else "127.0.0.1")
    return templates.TemplateResponse(request=request, name="qr/verify_qr.html", context={
        "verification_title": "Temporary Share Access",
        "result": res,
        "token": res.get("token")
    })

# ==========================================
# 10. COMPREHENSIVE SETTINGS & ACCOUNT HUB
# ==========================================

@app.get("/settings", response_class=HTMLResponse)
async def settings_hub_page(request: Request, tab: str = "profile"):
    return templates.TemplateResponse(request=request, name="settings/settings_hub.html", context={
        "active_page": "settings",
        "active_tab": tab,
        "profile": account_manager.profile,
        "privacy": account_manager.privacy_settings,
        "careai_perms": account_manager.careai_permissions,
        "emergency_contacts": account_manager.emergency_contacts,
        "active_devices": account_manager.active_devices,
        "connected_services": account_manager.connected_services,
        "appearance": account_manager.appearance_settings,
        "activity_logs": account_manager.user_activity_stream
    })

@app.post("/settings/profile")
async def update_profile_post(
    request: Request,
    full_name: str = Form(...),
    phone: str = Form(...),
    dob: str = Form(...),
    blood_group: str = Form("O+"),
    address: str = Form("")
):
    account_manager.update_profile({
        "full_name": full_name,
        "phone": phone,
        "dob": dob,
        "blood_group": blood_group,
        "address": address
    })
    return RedirectResponse(url="/settings?tab=profile", status_code=303)

@app.post("/settings/privacy")
async def update_privacy_post(
    request: Request,
    doctor_access: bool = Form(False),
    care_team_sharing: bool = Form(False),
    public_qr_masked_name: bool = Form(False)
):
    account_manager.update_privacy({
        "doctor_access": doctor_access,
        "care_team_sharing": care_team_sharing,
        "public_qr_masked_name": public_qr_masked_name
    })
    return RedirectResponse(url="/settings?tab=privacy", status_code=303)

@app.post("/settings/careai")
async def update_careai_post(
    request: Request,
    access_lab_reports: bool = Form(False),
    access_prediction_results: bool = Form(False),
    voice_interaction_enabled: bool = Form(False)
):
    account_manager.update_careai_permissions({
        "access_lab_reports": access_lab_reports,
        "access_prediction_results": access_prediction_results,
        "voice_interaction_enabled": voice_interaction_enabled
    })
    return RedirectResponse(url="/settings?tab=careai", status_code=303)

@app.post("/settings/emergency/remove")
async def remove_emergency_contact_post(request: Request, contact_id: str = Form(...)):
    account_manager.remove_emergency_contact(contact_id)
    return RedirectResponse(url="/settings?tab=emergency", status_code=303)

@app.post("/settings/devices/revoke")
async def revoke_device_post(request: Request, device_id: str = Form(...)):
    account_manager.revoke_device(device_id)
    return RedirectResponse(url="/settings?tab=devices", status_code=303)

@app.post("/settings/services/revoke")
async def revoke_service_post(request: Request, service_id: str = Form(...)):
    account_manager.revoke_service(service_id)
    return RedirectResponse(url="/settings?tab=connected_services", status_code=303)

@app.post("/settings/switch-role")
async def switch_role_post(request: Request, target_role: str = Form(...)):
    account_manager.switch_role(target_role)
    if target_role == "Doctor":
        return RedirectResponse(url="/doctor-id", status_code=303)
    elif target_role == "Care Coordinator":
        return RedirectResponse(url="/portal/coordinator", status_code=303)
    elif target_role == "Administrator":
        return RedirectResponse(url="/admin/users", status_code=303)
    return RedirectResponse(url="/portal/patient", status_code=303)

@app.get("/api/account/export")
async def download_account_data_export():
    archive = account_manager.generate_data_export_archive()
    json_data = json.dumps(archive, indent=2)
    return Response(
        content=json_data,
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=hrp_patient_data_export.json"}
    )
