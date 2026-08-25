# Authentication & Role-Based Access Control (RBAC)

Implemented in `app/auth.py`, the security subsystem manages user identity, multi-factor authentication, active sessions, and least-privilege permission boundaries.

---

## 1. Role-Based Access Control (RBAC) Matrix

| Resource / Endpoint | Patient | Doctor | Care Coordinator | Administrator |
| :--- | :---: | :---: | :---: | :---: |
| **View Personal EHR & Risk** | ✅ | ✅ | ✅ | ✅ |
| **Execute New ML Prediction** | ❌ | ✅ | ✅ | ✅ |
| **PPO RL Pathway Decision** | ❌ | ✅ (Authorize) | ✅ (View) | ✅ (Audit) |
| **Sign Medical Certificates** | ❌ | ✅ | ❌ | ❌ |
| **Video Telemedicine Call** | ✅ | ✅ | ✅ | ❌ |
| **Doctor License Verification**| ❌ | ❌ | ❌ | ✅ |
| **User Account & Role Admin** | ❌ | ❌ | ❌ | ✅ |
| **Institutional Audit Logs** | ❌ | ❌ | ❌ | ✅ |
| **Emergency Break-Glass** | ❌ | ✅ | ❌ | ❌ |

---

## 2. Seeded Institutional Accounts

| Role | Email | Password | Permissions |
| :--- | :--- | :--- | :--- |
| **Patient** | `eleanor.vance@patient.org` | `Patient@2026!` | Personal health records, lab reports, video consult |
| **Doctor** | `dr.smith@hospital.org` | `Doctor@2026!` | Full clinical evaluation, prediction wizard, sign certs |
| **Care Coordinator**| `sarah.coordinator@hospital.org` | `Coord@2026!` | Transition care queue, appointment follow-ups |
| **Administrator** | `admin@hospital.org` | `Admin@2026!` | User management, doctor approvals, audit log explorer |

---

## 3. Multi-Factor Authentication (MFA)

- **Workflow**: Upon entering valid credentials, users receive a 6-digit Time-Based One-Time Password (TOTP) prompt (`/auth/mfa`).
- **Test OTP**: `742891` (5-minute expiration window with countdown UI).

---

## 4. Emergency Break-Glass Access

In acute clinical situations where standard consent workflows cannot be fulfilled:
- Clinicians initiate emergency break-glass by providing a clinical rationale (e.g., *Acute decompensated heart failure triage*).
- Access is granted immediately while creating an immutable audit log entry flagged as `SECURITY_ALERT_BREAK_GLASS`.
