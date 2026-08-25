# Security & Privacy Documentation

HRP Clinical adheres to strict data minimization, role segregation, and tamper-evident audit logging principles.

---

## 1. Core Security Safeguards

1. **Role-Based Access Control (RBAC)**: Enforces least-privilege access; patients can only view their own health records and verified certificates.
2. **Multi-Factor Authentication (MFA)**: Enforces 6-digit TOTP validation for all clinician and administrative logins.
3. **Session Management**: Session tokens are cryptographically generated and tied to client IP and User-Agent headers (`/auth/sessions`).
4. **Emergency Break-Glass Audit**: Emergency overrides bypass access control only after recording mandatory clinical justification and triggering immutable audit entries (`/admin/audit-logs`).
5. **No Exposure of Sensitive Keys**: Wi-Fi network diagnostics and local device telemetry do not store or expose plaintext credentials.
6. **Public QR Verifier Privacy**: Certificate verification gateway (`/verify-certificate/{id}`) only reveals validity metadata and never exposes underlying diagnoses or private patient health identifiers.
