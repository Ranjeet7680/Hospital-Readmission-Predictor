# Frequently Asked Questions (FAQ)

---

### Q1: What does the Readmission Risk percentage mean?
The risk percentage represents the statistical likelihood that an inpatient will experience an unplanned 30-day all-cause hospital readmission based on demographic, laboratory, diagnostic, and utilization markers compared against historical training cohorts.

---

### Q2: Is this platform an autonomous medical diagnosis system?
**No.** HRP Clinical is strictly a clinical decision-support and research platform. All risk scores, SHAP factors, and RL care pathway recommendations must be reviewed by qualified clinicians.

---

### Q3: What dataset is used to benchmark the ML models?
The **Diabetes 130-US Hospitals (1999–2008)** dataset from UCI Machine Learning Repository (101,766 inpatient encounters across 130 US hospitals).

---

### Q4: How does Explainable AI work in this system?
HRP Clinical utilizes **TreeSHAP** to compute local Shapley additive values for every feature, decomposing the exact percentage shift between baseline hospital expectation and individual patient risk.

---

### Q5: What is the role of Reinforcement Learning?
The RL layer acts as an optimization research simulation for post-discharge care workflows (PPO agent), evaluating which coordination actions minimize readmission risk under cost constraints.

---

### Q6: Does the system support Hindi?
**Yes.** The platform includes real-time bilingual support (English $\leftrightarrow$ हिन्दी) for menus, risk factors, recommendations, and video consultation subtitles.

---

### Q7: Can the platform operate in offline mode?
**Yes.** The system detects offline states and allows offline browsing of local patient profiles and downloaded reports.
