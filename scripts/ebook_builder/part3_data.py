# Part III: Dataset & Data Engineering (Chapters 11 - 15)

def get_part3():
    return """
# PART III — DATASET & CLINICAL DATA ENGINEERING

---

## Chapter 11 — The Healthcare Dataset: Diabetes 130-US Hospitals Cohort

### 11.1 Benchmark Dataset Provenance & Scope
To build a clinically grounded readmission prediction engine, the platform utilizes the seminal **Diabetes 130-US Hospitals for Years 1999–2008** dataset (UCI Repository #296 / Strack et al.). This longitudinal clinical dataset comprises **101,766 verified inpatient diabetic admissions** across 130 medical centers over a 10-year period.

```
┌────────────────────────────────────────────────────────────────────────────┐
│                  DATASET COHORT SPECIFICATIONS & METRICS                   │
├────────────────────────────────────────────────────────────────────────────┤
│  • Total Encounter Records: 101,766 Unique Hospitalizations                │
│  • Unique Individual Patients: ~71,518 Patients (Longitudinal Returns)     │
│  • Participating Hospital Facilities: 130 Medical Centers                  │
│  • Total Raw Clinical Dimensions: 50 Structured Attributes                 │
│  • Target Outcome: 30-Day Readmission (<30 Days: Positive Class)           │
│  • Positive Class Prevalence (<30d): 11,357 encounters (11.16%)            │
│  • Historical Study Window: 1999 to 2008 (10-Year Observation)             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 11.2 The 50 Clinical Features Breakdown
The features are structured across five primary clinical categories:
1. **Patient Demographics**: `race`, `gender`, `age` (10-year brackets: [0-10) to [90-100)), `weight`.
2. **Admission & Discharge Context**: `admission_type_id` (Emergency, Urgent, Elective), `discharge_disposition_id` (Home, SNF, Rehab, Expired), `admission_source_id` (ED, Referral, Transfer), `time_in_hospital` (Length of Stay in days: 1 to 14).
3. **Clinical Diagnostics**: `medical_specialty` (84 specialties), `primary_diagnosis` (ICD-9), `secondary_diagnosis` (ICD-9), `additional_diagnosis` (ICD-9), `number_diagnoses` (1 to 16).
4. **Laboratory & Utilization Metrics**: `num_lab_procedures` (1 to 132), `num_procedures` (0 to 6), `num_medications` (1 to 81), `number_outpatient`, `number_emergency`, `number_inpatient` in preceding 12 months.
5. **Diabetic Medications (23 Agents)**: `metformin`, `repaglinide`, `nateglinide`, `chlorpropamide`, `glimepiride`, `acetohexamide`, `glipizide`, `glyburide`, `tolbutamide`, `pioglitazone`, `rosiglitazone`, `acarbose`, `miglitol`, `troglitazone`, `tolazamide`, `examide`, `citoglipton`, `insulin`, `glyburide-metformin`, `glipizide-metformin`, `glimepiride-pioglitazone`, `metformin-rosiglitazone`, `metformin-pioglitazone`, `change` (Medication dosage adjusted), `diabetesMed` (Prescribed any diabetic drug).

---

### 11.3 Key Takeaways
1. The 101,766-encounter dataset provides real-world statistical power across 130 hospitals.
2. The 30-day positive class represents 11.16% of encounters, creating a realistic class imbalance challenge.
3. Incorporating 23 specific medication adjustments enables true pharmacological modeling.

---

## Chapter 12 — High-Throughput Data Ingestion & Schema Validation

### 12.1 Schema Definition & Type Enforcement
Healthcare telemetry must undergo strict schema validation before model ingestion. The ingestion engine enforces Pydantic schemas validating value ranges, units, and missingness flags:

```python
from pydantic import BaseModel, Field
from typing import Optional

class PatientInferencePayload(BaseModel):
    patient_id: str = Field(..., description="Unique alphanumeric patient ID")
    age: float = Field(..., ge=0, le=120, description="Age in years")
    gender: str = Field(default="Male", regex="^(Male|Female|Other)$")
    systolic_bp: float = Field(default=120.0, ge=60, le=260)
    diastolic_bp: float = Field(default=80.0, ge=30, le=160)
    creatinine: float = Field(default=1.0, ge=0.1, le=20.0)
    blood_glucose: float = Field(default=100.0, ge=30, le=800)
    hba1c: float = Field(default=5.5, ge=3.0, le=20.0)
    length_of_stay: int = Field(default=3, ge=1, le=90)
    medication_count: int = Field(default=5, ge=0, le=80)
    prev_admissions_30d: int = Field(default=0, ge=0, le=20)
    prev_admissions_12m: int = Field(default=0, ge=0, le=50)
    primary_diagnosis: str = Field(default="Diabetes Mellitus")
```

---

### 12.2 Key Takeaways
1. Rigorous Pydantic schema validation rejects malformed inputs before model evaluation.
2. Boundary checks on physiological vitals prevent out-of-distribution hallucinations.
3. Ingestion pipelines maintain consistent data lineage across clinical versions.

---

## Chapter 13 — Clinical Data Cleaning & Outlier Management

### 13.1 Missing Value Treatment
In the raw UCI dataset, several columns exhibit high missingness represented as `'?'`:
* `weight`: **96.8% Missing** $\to$ Dropped entirely to avoid introducing severe imputation noise.
* `payer_code`: **39.5% Missing** $\to$ Dropped as non-clinical administrative metadata.
* `medical_specialty`: **49.0% Missing** $\to$ Imputed with a separate category `'Missing/Not_Recorded'` to preserve potential signal regarding admission type.

```
   ┌─────────────────────────────────────────────────────────────┐
   │               MISSING VALUE CLEANING STRATEGY               │
   ├──────────────────────────┬──────────────┬───────────────────┤
   │ Feature Name             │ % Missing    │ Treatment Policy  │
   ├──────────────────────────┼──────────────┼───────────────────┤
   │ weight                   │ 96.8%        │ Drop column       │
   │ payer_code               │ 39.5%        │ Drop column       │
   │ medical_specialty        │ 49.0%        │ Add 'Unspecified' │
   │ race                     │ 2.2%         │ Mode imputation   │
   │ diagnosis ICD-9 (diag_3) │ 1.4%         │ Impute 'V-code'   │
   └──────────────────────────┴──────────────┴───────────────────┘
```

### 13.2 Terminal Encounters & Leakage Filtering
Patients whose `discharge_disposition_id` corresponds to **Expired / Hospice** (codes 11, 13, 14, 19, 20, 21) cannot theoretically be readmitted. Including these records would create false negatives and severe evaluation leakage. **All terminal and hospice records are strictly filtered out of the cohort.**

---

### 13.3 Key Takeaways
1. Dropping features with $>90\%$ missingness prevents noise injection into decision trees.
2. Filtering out hospice and deceased encounters eliminates artificial negative-class leakage.
3. Categorical missingness indicators (e.g. `'Unspecified'`) preserve valuable triage context.

---

## Chapter 14 — Domain-Specific Healthcare Feature Engineering

### 14.1 Derived Clinical Predictors
Raw EHR fields alone do not capture non-linear physiological complexity. We engineer several high-impact domain features:

$$\text{Prior Utilization Index} = 3.0 \times \text{Inpatient}_{30\text{d}} + 1.5 \times \text{Inpatient}_{12\text{m}} + 1.0 \times \text{ED}_{12\text{m}} + 0.5 \times \text{Outpatient}_{12\text{m}}$$

$$\text{Polypharmacy Severity Score} = \begin{cases} 
0 & \text{if } \text{num\_meds} < 5 \text{ (Normal)} \\
1 & \text{if } 5 \le \text{num\_meds} < 10 \text{ (Moderate)} \\
2 & \text{if } \text{num\_meds} \ge 10 \text{ (Severe Polypharmacy)}
\end{cases}$$

### 14.2 Clinical Comorbidity ICD-9 Mapping
Raw ICD-9 diagnostic codes (e.g., 250.02, 428.0, 585.9) are grouped into 9 standardized diagnostic clusters using the Clinical Classifications Software (CCS):
1. **Circulatory System** (ICD-9: 390–459, 785) $\to$ CHF, AMI, Hypertension
2. **Endocrine & Metabolic** (ICD-9: 250.xx) $\to$ Diabetes Mellitus type I/II
3. **Respiratory System** (ICD-9: 460–519, 786) $\to$ COPD, Pneumonia
4. **Digestive System** (ICD-9: 520–579, 787)
5. **Genitourinary & Renal** (ICD-9: 580–629, 788) $\to$ CKD, ESRD
6. **Musculoskeletal** (ICD-9: 710–739)
7. **Neoplasms** (ICD-9: 140–239)
8. **Injury & Poisoning** (ICD-9: 800–999)
9. **Other Conditions** (All remaining ICD-9 and V/E codes)

---

### 14.3 Key Takeaways
1. Prior utilization indices weight acute recent returns higher than distant outpatient visits.
2. Polypharmacy scores flag drug-interaction risks for patients on 10+ concurrent medications.
3. Grouping ICD-9 codes into 9 clinical categories reduces dimensional sparsity while preserving diagnostic power.

---

## Chapter 15 — The 10-Stage Leakage-Free Preprocessing Pipeline

### 15.1 Pipeline Topology & Architecture
To guarantee zero data leakage between training, validation, and holdout partitions, all scaling parameters, target encodings, and imputer statistics are fit **strictly on the training partition**:

```
[Raw Encounter CSV] 
       │
       ▼  (Stage 1: Terminal Record Exclusion - Discharged to Hospice/Died)
[Active Cohort Records]
       │
       ▼  (Stage 2: Target Binary Encoding: '<30' -> 1, 'NO'/'>30' -> 0)
[Binary Labeled Dataset]
       │
       ▼  (Stage 3: High-Missingness Column Pruning: weight, payer_code)
[Pruned Feature Table]
       │
       ▼  (Stage 4: Stratified Train / Test Holdout Split: 80% Train / 20% Test)
       ├─────────────────────────────────────────┐
       ▼ (Fit & Transform on Train)              ▼ (Transform Only on Test)
[Stage 5: Categorical Missingness Imputation]
       │
       ▼ (Stage 6: ICD-9 Comorbidity Mapping to 9 CCS Categories)
       │
       ▼ (Stage 7: Pharmacological Dosage Encoding: No/Down/Steady/Up -> 0,1,2,3)
       │
       ▼ (Stage 8: Interaction & Domain Features: Utilization, Polypharmacy)
       │
       ▼ (Stage 9: StandardScaler Fitting on Continuous Features)
       │
       ▼ (Stage 10: Stratified 5-Fold Cross-Validation Matrix Generation)
[Model-Ready Tensors & Arrays]
```

---

### 15.2 Key Takeaways
1. The 10-stage pipeline enforces strict separation between training transformations and testing holdouts.
2. Stratified splitting preserves the 11.16% class distribution across all training and evaluation folds.
3. Standardized preprocessing pipelines are serialized with Joblib to ensure identical runtime transformations.
"""
