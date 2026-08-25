# API Reference

The HRP Clinical platform provides a REST API built with FastAPI. All endpoints return JSON or server-rendered HTML.

---

## 1. Prediction Endpoints

### `POST /api/predict`
Calculates 30-day readmission risk, SHAP feature factors, and clinical recommendations.

**Request Body:**
```json
{
  "patient_id": "PT-84729",
  "full_name": "Eleanor Vance",
  "age": 71,
  "gender": "Female",
  "department": "Cardiology",
  "attending_physician": "Dr. J. Aris",
  "primary_diagnosis": "Congestive Heart Failure",
  "length_of_stay": 9,
  "systolic_bp": 135,
  "diastolic_bp": 85,
  "creatinine": 1.60,
  "haemoglobin": 11.2,
  "hba1c": 7.4,
  "prev_admissions_30d": 1,
  "prev_admissions_12m": 2,
  "ed_visits_12m": 2,
  "medication_count": 8
}
```

**Response (200 OK):**
```json
{
  "id": "PRED-PT-84729",
  "patient_id": "PT-84729",
  "risk_score": 68,
  "risk_level": "High Risk",
  "risk_level_code": "high",
  "contributing_factors": [
    {
      "title": "Previous Admission History",
      "impact": "High Elevating Factor",
      "direction": "up",
      "color": "#ba1a1a"
    }
  ],
  "recommendations": [
    "Schedule primary care follow-up within 72 hours of discharge."
  ]
}
```

---

## 2. Patient Endpoints

### `GET /api/patient/{patient_id}`
Returns the complete electronic record for a patient.

---

## 3. History & Export Endpoints

### `GET /api/history/export`
Exports all assessed patient risk evaluations as a CSV file attachment.

---

## 4. Document Q&A Endpoints

### `GET /api/documents/{doc_id}/chat?query={question}&lang={en|hi}`
Executes a document-grounded question answering query against an uploaded report.

---

## 5. Model Analytics Endpoints

### `GET /api/metrics`
Returns global benchmark metrics for the active champion model.

### `GET /api/ml/chat?query={question}`
Natural language assistant answering questions about model weights and data drift.
