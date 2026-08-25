# Medical Certificates

The Medical Certificate engine manages the generation, clinician signing, official rendering, and public verification of digital medical certificates.

> ⚠️ **Authorized Sign-off Requirement**: AI algorithms **never** independently issue official certificates. Every certificate requires review and digital authorization by a verified physician.

---

## 1. Issuance & Verification Lifecycle

```mermaid
flowchart TD
    A[Patient / Doctor Certificate Request] --> B[Doctor Clinical Review & Rest Period Selection]
    B --> C[Physician Digital Signature & Seal]
    C --> D[Generate SHA-256 Verification Hash]
    D --> E[Render Official PDF Certificate]
    E --> F[Public QR Verification: /verify-certificate/{id}]
```

---

## 2. Supported Certificate Types

1. **Medical Fitness Certificate**: Employment, fitness for duty, and general wellness verification.
2. **Medical Leave / Sick Leave Certificate**: Prescribes temporary convalescence rest (e.g., 14 days) following acute inpatient discharge.
3. **Hospitalization Certificate**: Certifies inpatient admission dates for insurance and legal documentation.

---

## 3. Public QR Verification Gateway

- **Route**: `/verify-certificate/{cert_id}`
- **Security Design**: Public verifiers (e.g., employers, insurance providers) can scan the QR code to verify authenticity, issuing physician, and validity dates without exposing confidential medical histories.
