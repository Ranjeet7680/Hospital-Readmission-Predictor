# Responsible AI & Clinical Limitations

HRP Clinical is built upon Responsible AI principles for healthcare decision-support systems.

---

## 1. Core Clinical Safety Principles

1. **Human-in-the-Loop Authority**: The platform does not alter prescriptions, modify dosages, or diagnose disease autonomously. Attending clinicians have full authority over all patient management decisions.
2. **Model-Associated Factors**: SHAP feature values indicate statistical correlation within training data, not verified biological causality.
3. **Medical Certificate Verification**: Official certificates require explicit review, convalescence rest period setting, and digital authorization by an authorized physician.
4. **Historical Dataset Boundaries**: The primary training dataset reflects hospital practices from 1999–2008. While valuable for research and algorithmic benchmarking, clinicians should evaluate results in context with contemporary clinical protocols.
5. **Data Minimization & Privacy**: No confidential patient data is transmitted to unauthorized external APIs.
