# Database Schema

The database model manages patients, historical predictions, medical documents, certificates, user identities, and security audit trails.

---

## 1. Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
    USER ||--o{ SESSION : owns
    USER ||--o{ AUDIT_LOG : triggers
    PATIENT ||--o{ PREDICTION : has
    PATIENT ||--o{ DOCUMENT : owns
    PATIENT ||--o{ CERTIFICATE : receives
    DOCTOR ||--o{ CERTIFICATE : signs
    PREDICTION ||--|{ SHAP_FACTOR : contains
    DOCUMENT ||--|{ LAB_RESULT : contains

    USER {
        string id PK
        string email UK
        string full_name
        string role
        string password_hash
        boolean mfa_enabled
    }

    PATIENT {
        string id PK
        string name
        int age
        string gender
        string department
        string primary_diagnosis
        int risk_score
        string risk_tier
    }

    PREDICTION {
        string id PK
        string patient_id FK
        string timestamp
        int risk_score
        string risk_level
        string model_version
        string clinician
    }

    CERTIFICATE {
        string id PK
        string patient_id FK
        string doctor_name
        string certificate_type
        string issue_date
        int rest_days
        string verification_hash
        boolean verified
    }

    AUDIT_LOG {
        string id PK
        string user_email
        string action
        string resource_id
        string timestamp
        string status
    }
```
