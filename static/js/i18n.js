/**
 * Client-Side Multi-Lingual Translation & Accessibility Engine v4.0
 * Hospital Readmission Predictor (HRP Clinical)
 *
 * Supported Languages:
 *  - en: English (Default)
 *  - hi: हिन्दी (Hindi)
 *  - ta: தமிழ் (Tamil)
 *  - kn: ಕನ್ನಡ (Kannada)
 *  - ml: മലയാളം (Malayalam)
 *  - te: తెలుగు (Telugu)
 *  - bn: বাংলা (Bengali)
 *
 * Features:
 *  - 400+ Clinical, Operational, ML/RL, Telemedicine, and Portal terms
 *  - Intelligent DOM Auto-Translation (badges, clinical terms, placeholders, titles)
 *  - Real-time MutationObserver for dynamically loaded content
 *  - Cookie & LocalStorage synchronization with backend
 *  - Multi-language Text-to-Speech (TTS) Web Speech API
 *  - Event dispatcher ('languageChanged') for real-time component updates
 */

const translations = {
    en: {
        // Brand & Header
        "brand_name": "HRP Clinical",
        "brand_subtitle": "Precision Care & AI",
        "hospital_suite": "Healthcare Suite",
        "header_title": "Hospital Readmission Predictor",
        "search_placeholder": "Search patient, document, history...",
        "search_mobile_placeholder": "Search patient, document, history...",
        "dr_name": "Dr. Ranjeet Kumar, MD",
        "dr_title": "Lead AI Architect • St. Jude",
        "doctor_id": "Doctor Digital ID",
        "edit_profile": "Edit Doctor Profile",
        "account_settings": "Account & Settings",
        "master_ebook": "Master eBook (88 Ch)",
        "logout": "Log Out",
        "sign_out_lock": "Sign Out / Lock Session",
        "sign_out_switch": "Sign Out / Switch Role",
        "offline_banner": "Offline Mode Active — Live AI and Video calls paused. Local records available.",
        "reconnect": "Reconnect",
        "read_aloud": "Read Page Aloud (TTS)",
        "notifications": "Notifications",
        "language": "Language",

        // Navigation Sections
        "nav_clinical_care": "Clinical Care",
        "dashboard": "Dashboard",
        "new_prediction": "New Prediction",
        "patients": "Patients",
        "prediction_history": "Prediction History",
        "analytics": "Clinical Analytics",
        "model_insights": "Model Insights",

        "nav_medical_docs": "Medical Documents",
        "medical_documents": "Medical Documents",
        "my_documents": "My Documents",
        "lab_reports": "Lab & Report Analysis",
        "medical_certificates": "Medical Certificates",
        "verify_certificate": "Verify Certificate",
        "prescriptions": "Prescriptions",
        "discharge_summaries": "Discharge Summaries",

        "nav_ai_ml": "AI & ML Intelligence",
        "ai_and_ml": "AI & ML Intelligence",
        "ml_dashboard": "ML Dashboard",
        "dataset_workspace": "Dataset Workspace",
        "preprocessing": "Preprocessing (10-Stage)",
        "model_training": "Training Studio",
        "deep_learning_lab": "Deep Learning Lab",
        "model_comparison": "Model Comparison",
        "explainable_ai": "Explainable AI (SHAP)",
        "patient_embeddings": "Patient Embeddings (2D)",
        "ensemble_uncertainty": "Ensemble & Uncertainty",
        "model_monitoring": "Model Drift Monitoring",
        "model_registry": "Model Registry",
        "experiment_tracking": "Experiment Tracking",
        "ask_the_model": "Ask the Model",

        "nav_rl": "Reinforcement Learning",
        "reinforcement_learning": "Reinforcement Learning",
        "rl_dashboard": "RL Dashboard",
        "patient_environment": "Care Journey Env",
        "care_pathway_opt": "Care Pathway Optimizer",
        "digital_twin_sim": "Digital Twin Sim (What-If)",
        "safety_constraints": "Safety Constraint Engine",
        "human_review": "Human-in-the-Loop",
        "stack_architecture": "8-Layer AI Stack",

        "nav_portals": "Portals & Telehealth",
        "video_consultation": "CareAI Video Call",
        "patient_portal": "Patient Portal",
        "care_coordinator": "Care Coordinator",
        "user_management": "User Management",
        "doctor_verification": "Doctor Verification",
        "security_audit_logs": "Security Audit Logs",

        "nav_health_id": "Health ID & Passes",
        "my_health_id": "My Health ID",
        "doctor_id_card": "Doctor ID Card",
        "digital_wallet": "Digital Wallet",
        "scan_qr_code": "Scan QR Code",
        "temporary_share": "Temporary Sharing",

        "nav_system": "System & Account",
        "settings": "Settings",
        "help": "Help & Support",
        "active_sessions": "Active Sessions",
        "welcome_tour": "Welcome Tour",
        "privacy_safety": "Privacy & Safety",

        // Mobile Bottom Nav
        "nav_home": "Home",
        "nav_patients": "Patients",
        "nav_predict": "Predict",
        "nav_telehealth": "Telehealth",
        "nav_menu": "Menu",
        "nav_more": "More",

        // Actions & Buttons
        "generate_prediction": "Generate Prediction",
        "evaluating_risk": "Evaluating Risk Factors...",
        "view_assessment": "View Assessment",
        "view_profile": "View Profile",
        "export_report": "Export Report (CSV/PDF)",
        "save_assessment": "Save Assessment",
        "apply_filters": "Apply Filters",
        "approve": "Approve",
        "reject": "Reject",
        "override": "Override",
        "modify": "Modify",
        "view_simulation": "View Simulation",
        "human_review_required": "Human Review Required",
        "simulation_result": "Simulation Result",
        "rl_workflow_rec": "RL Pathway Recommendation",
        "verify_identity": "Verify Your Identity",
        "forgot_password": "Forgot Password?",
        "start_prediction": "Start Prediction",
        "explore_dashboard": "Explore Dashboard",
        "save_to_ehr": "Save Verified Notes to EHR",
        "end_call": "End Call",
        "join_call": "Join Consultation",
        "confirm": "Confirm",
        "cancel": "Cancel",
        "download_pdf": "Download PDF",
        "print_prescription": "Print Prescription",
        "talk_to_doctor": "Talk to AI Doctor (Voice)",
        "listening": "Listening... Speak now",
        "generate_rx": "Generate Prescription",
        "ai_summarize": "AI Summarize",
        "translate_notes": "Translate Notes",
        "issue_certificate": "Issue Certificate",
        "emergency_sos": "Emergency SOS",

        // Telemedicine & AI Doctor Video Call
        "ai_doctor_copilot": "CareAI Clinical Copilot",
        "ai_doctor_name": "Dr. CareAI (Lead Clinical AI)",
        "consultation_title": "AI Doctor Live Consultation",
        "device_check": "Device Readiness Check",
        "camera_ready": "Camera: Ready",
        "mic_ready": "Microphone: Ready",
        "network_excellent": "Network: Excellent (32ms)",
        "view_ai_doctor": "AI Doctor Feed",
        "view_patient": "Patient Simulation",
        "view_split": "Split Telemetry View",
        "live_ecg": "Live ECG & Vitals Monitor",
        "heart_rate": "Heart Rate",
        "blood_pressure": "Blood Pressure",
        "oxygen_sat": "SpO2 Oxygen",
        "resp_rate": "Respiratory Rate",
        "temperature": "Temperature",
        "live_captions": "Live Dual-Language Captions",
        "ai_clinical_insight": "AI Clinical Insight",
        "readmission_risk": "Readmission Risk",
        "ppo_rl_pathway": "PPO RL Care Pathway",
        "ask_ai_placeholder": "Ask AI Doctor a clinical question or speak...",
        "ehr_clinical_notes": "Clinical Notes (EHR)",
        "rx_modal_title": "Official Clinical Prescription",

        // Clinical Tiers & Badges
        "high_risk": "High Risk",
        "moderate_risk": "Moderate Risk",
        "low_risk": "Low Risk",
        "reviewed": "Reviewed",
        "pending": "Pending",
        "actioned": "Actioned",
        "active": "Active",
        "completed": "Completed",
        "live_encrypted": "LIVE · Encrypted",
        "male": "Male",
        "female": "Female",
        "other": "Other",

        // Clinical Metrics & Diagnostics
        "total_screened": "Total Screened",
        "avg_risk_score": "Average Risk Score",
        "active_patients": "Active Inpatients",
        "accuracy": "Accuracy",
        "precision": "Precision",
        "recall": "Sensitivity (Recall)",
        "f1_score": "F1-Score",
        "roc_auc": "ROC-AUC",
        "cardiology": "Cardiology",
        "general_medicine": "General Medicine",
        "endocrinology": "Endocrinology",
        "pulmonology": "Pulmonology",
        "nephrology": "Nephrology"
    },

    hi: {
        // Brand & Header
        "brand_name": "एचआरपी क्लिनिकल",
        "brand_subtitle": "सटीक देखभाल एवं एआई",
        "hospital_suite": "हेल्थकेयर सुइट",
        "header_title": "अस्पताल पुनः भर्ती जोखिम भविष्यवक्ता",
        "search_placeholder": "रोगी, डॉक्टर या रिकॉर्ड खोजें...",
        "search_mobile_placeholder": "रोगी, दस्तावेज, इतिहास खोजें...",
        "dr_name": "डॉ. रंजीत कुमार, एमडी",
        "dr_title": "प्रमुख एआई वास्तुकार • सेंट ज्यूड",
        "doctor_id": "चिकित्सक डिजिटल आईडी",
        "edit_profile": "डॉक्टर प्रोफाइल संपादित करें",
        "account_settings": "खाता एवं सेटिंग्स",
        "master_ebook": "मास्टर ई-बुक (88 अध्याय)",
        "logout": "लॉग आउट करें",
        "sign_out_lock": "साइन आउट / सत्र लॉक करें",
        "sign_out_switch": "साइन आउट / भूमिका बदलें",
        "offline_banner": "ऑफ़लाइन मोड सक्रिय — लाइव एआई और वीडियो कॉल रोकी गईं। स्थानीय रिकॉर्ड उपलब्ध हैं।",
        "reconnect": "पुनः कनेक्ट करें",
        "read_aloud": "पृष्ठ को पढ़कर सुनाएं (TTS)",
        "notifications": "सूचनाएं",
        "language": "भाषा",

        // Navigation Sections
        "nav_clinical_care": "क्लिनिकल देखभाल",
        "dashboard": "डैशबोर्ड",
        "new_prediction": "नया जोखिम मूल्यांकन",
        "patients": "मरीज सूची",
        "prediction_history": "पूर्वानुमान इतिहास",
        "analytics": "क्लिनिकल विश्लेषण",
        "model_insights": "मॉडल अंतर्दृष्टि",

        "nav_medical_docs": "चिकित्सा दस्तावेज",
        "medical_documents": "चिकित्सा दस्तावेज",
        "my_documents": "मेरे दस्तावेज",
        "lab_reports": "लैब एवं रिपोर्ट विश्लेषण",
        "medical_certificates": "मेडिकल प्रमाण पत्र",
        "verify_certificate": "प्रमाण पत्र सत्यापन",
        "prescriptions": "नुस्खे (प्रिस्क्रिप्शन)",
        "discharge_summaries": "डिस्चार्ज सारांश",

        "nav_ai_ml": "एआई एवं मशीन लर्निंग",
        "ai_and_ml": "एआई एवं मशीन लर्निंग",
        "ml_dashboard": "एमएल डैशबोर्ड",
        "dataset_workspace": "डेटासेट कार्यक्षेत्र",
        "preprocessing": "डेटा प्रीप्रोसेसिंग (10-चरण)",
        "model_training": "प्रशिक्षण स्टूडियो",
        "deep_learning_lab": "डीप लर्निंग लैब",
        "model_comparison": "मॉडल तुलना",
        "explainable_ai": "स्पष्टीकरणीय एआई (SHAP)",
        "patient_embeddings": "रोगी एआई प्रतिनिधित्व (2D)",
        "ensemble_uncertainty": "एन्सेम्बल एवं अनिश्चितता",
        "model_monitoring": "मॉडल ड्रिफ्ट निगरानी",
        "model_registry": "मॉडल रजिस्ट्री",
        "experiment_tracking": "प्रयोग ट्रैकिंग",
        "ask_the_model": "मॉडल से पूछें (एआई चैट)",

        "nav_rl": "सुदृढ़ीकरण अधिगम (RL)",
        "reinforcement_learning": "सुदृढ़ीकरण अधिगम (RL)",
        "rl_dashboard": "आरएल डैशबोर्ड",
        "patient_environment": "रोगी देखभाल परिवेश",
        "care_pathway_opt": "देखभाल पथ अनुकूलक",
        "digital_twin_sim": "डिजिटल ट्विन सिमुलेशन",
        "safety_constraints": "सुरक्षा प्रतिबंध इंजन",
        "human_review": "मानव समीक्षा (चिकित्सक सत्यापन)",
        "stack_architecture": "8-स्तरीय एआई संरचना",

        "nav_portals": "पोर्टल एवं टेलीहेल्थ",
        "video_consultation": "केयर-एआई वीडियो कॉल",
        "patient_portal": "रोगी पोर्टल",
        "care_coordinator": "देखभाल समन्वयक",
        "user_management": "उपयोगकर्ता प्रबंधन",
        "doctor_verification": "चिकित्सक सत्यापन",
        "security_audit_logs": "सुरक्षा ऑडिट लॉग्स",

        "nav_health_id": "हेल्थ आईडी एवं पास",
        "my_health_id": "मेरी हेल्थ आईडी",
        "doctor_id_card": "डॉक्टर आईडी कार्ड",
        "digital_wallet": "डिजिटल वॉलेट",
        "scan_qr_code": "क्यूआर कोड स्कैन करें",
        "temporary_share": "अस्थायी शेयर पास",

        "nav_system": "प्रणाली एवं खाता",
        "settings": "सेटिंग्स",
        "help": "सहायता एवं मार्गदर्शन",
        "active_sessions": "सक्रिय सत्र",
        "welcome_tour": "स्वागत टूर",
        "privacy_safety": "गोपनीयता एवं सुरक्षा",

        // Mobile Bottom Nav
        "nav_home": "होम",
        "nav_patients": "मरीज",
        "nav_predict": "पूर्वानुमान",
        "nav_telehealth": "टेलीहेल्थ",
        "nav_menu": "मेनू",
        "nav_more": "अधिक",

        // Actions & Buttons
        "generate_prediction": "जोखिम पूर्वानुमान लगाएं",
        "evaluating_risk": "जोखिम कारकों का मूल्यांकन हो रहा है...",
        "view_assessment": "मूल्यांकन देखें",
        "view_profile": "प्रोफ़ाइल देखें",
        "export_report": "रिपोर्ट निर्यात करें (CSV/PDF)",
        "save_assessment": "मूल्यांकन सहेजें",
        "apply_filters": "फ़िल्टर लागू करें",
        "approve": "स्वीकृत करें",
        "reject": "अस्वीकार करें",
        "override": "ओवरराइड करें",
        "modify": "संशोधित करें",
        "view_simulation": "सिमुलेशन देखें",
        "human_review_required": "मानव समीक्षा आवश्यक है",
        "simulation_result": "सिमुलेशन परिणाम",
        "rl_workflow_rec": "RL कार्यप्रवाह अनुशंसा",
        "verify_identity": "अपनी पहचान सत्यापित करें",
        "forgot_password": "पासवर्ड भूल गए?",
        "start_prediction": "पूर्वानुमान शुरू करें",
        "explore_dashboard": "डैशबोर्ड एक्सप्लोर करें",
        "save_to_ehr": "सत्यापित नोट्स ईएचआर में सहेजें",
        "end_call": "कॉल समाप्त करें",
        "join_call": "परामर्श में शामिल हों",
        "confirm": "पुष्टि करें",
        "cancel": "रद्द करें",
        "download_pdf": "पीडीएफ डाउनलोड करें",
        "print_prescription": "प्रिस्क्रिप्शन प्रिंट करें",
        "talk_to_doctor": "एआई डॉक्टर से बोलें (आवाज)",
        "listening": "सुन रहे हैं... कृपया बोलें",
        "generate_rx": "नुस्खा बनाएं",
        "ai_summarize": "एआई सारांश",
        "translate_notes": "नोट्स अनुवाद करें",
        "issue_certificate": "प्रमाण पत्र जारी करें",
        "emergency_sos": "आपातकालीन एसओएस",

        // Telemedicine & AI Doctor Video Call
        "ai_doctor_copilot": "केयर-एआई क्लिनिकल कोपायलट",
        "ai_doctor_name": "डॉ. केयर-एआई (प्रमुख एआई विशेषज्ञ)",
        "consultation_title": "एआई डॉक्टर लाइव वीडियो परामर्श",
        "device_check": "उपकरण तत्परता जांच",
        "camera_ready": "कैमरा: तैयार",
        "mic_ready": "माइक्रोफ़ोन: तैयार",
        "network_excellent": "नेटवर्क: उत्कृष्ट (32ms)",
        "view_ai_doctor": "एआई डॉक्टर दृश्य",
        "view_patient": "रोगी सिमुलेशन",
        "view_split": "विभाजित टेलीमेट्री दृश्य",
        "live_ecg": "लाइव ईसीजी एवं वाइटल्स मॉनिटर",
        "heart_rate": "हृदय गति (HR)",
        "blood_pressure": "रक्तचाप (BP)",
        "oxygen_sat": "ऑक्सीजन स्तर (SpO2)",
        "resp_rate": "श्वसन दर",
        "temperature": "तापमान",
        "live_captions": "लाइव द्विभाषी उपशीर्षक",
        "ai_clinical_insight": "एआई क्लिनिकल अंतर्दृष्टि",
        "readmission_risk": "पुनः भर्ती जोखिम",
        "ppo_rl_pathway": "PPO RL देखभाल मार्ग",
        "ask_ai_placeholder": "एआई डॉक्टर से क्लिनिकल प्रश्न पूछें या बोलें...",
        "ehr_clinical_notes": "क्लिनिकल नोट्स (ईएचआर)",
        "rx_modal_title": "आधिकारिक चिकित्सा नुस्खा (प्रिस्क्रिप्शन)",

        // Clinical Tiers & Badges
        "high_risk": "उच्च जोखिम",
        "moderate_risk": "मध्यम जोखिम",
        "low_risk": "कम जोखिम",
        "reviewed": "समीक्षित",
        "pending": "लंबित",
        "actioned": "कार्रवाई की गई",
        "active": "सक्रिय",
        "completed": "पूर्ण",
        "live_encrypted": "लाइव · एन्क्रिप्टेड",
        "male": "पुरुष",
        "female": "महिला",
        "other": "अन्य",

        // Clinical Metrics & Diagnostics
        "total_screened": "कुल मूल्यांकित मरीज",
        "avg_risk_score": "औसत जोखिम स्कोर",
        "active_patients": "सक्रिय भर्ती मरीज",
        "accuracy": "सटीकता (Accuracy)",
        "precision": "परिशुद्धता (Precision)",
        "recall": "संवेदनशीलता (Recall)",
        "f1_score": "F1-स्कोर",
        "roc_auc": "आरओसी-एयूसी",
        "cardiology": "हृदय रोग विभाग (Cardiology)",
        "general_medicine": "सामान्य चिकित्सा",
        "endocrinology": "एंडोक्रिनोलॉजी",
        "pulmonology": "श्वसन रोग विभाग",
        "nephrology": "गुर्दा रोग विभाग (Nephrology)"
    },

    ta: {
        "brand_name": "எச்ஆர்பி கிளினிக்கல்",
        "brand_subtitle": "துல்லிய சிகிச்சை & AI",
        "hospital_suite": "மருத்துவ தளம்",
        "header_title": "மறுஅனுமதி ஆபத்து கணிப்பான்",
        "search_placeholder": "நோயாளி, மருத்துவர் தேடவும்...",
        "search_mobile_placeholder": "நோயாளி, ஆவணங்களை தேடவும்...",
        "dr_name": "டாக்டர் ரஞ்சீத் குமார், MD",
        "dr_title": "தலைமை AI வடிவமைப்பாளர்",
        "doctor_id": "மருத்துவர் டிஜிட்டல் ஐடி",
        "edit_profile": "சுயவிவரத்தை திருத்துக",
        "account_settings": "கணக்கு & அமைப்புகள்",
        "master_ebook": "முழு மருத்துவ மின்புத்தகம்",
        "logout": "வெளியேறு",
        "sign_out_lock": "வெளியேறு / அமர்வை பூட்டு",
        "sign_out_switch": "வெளியேறு / பங்கை மாற்று",
        "offline_banner": "ஆஃப்லைன் பயன்முறை செயலில் உள்ளது — நேரலை AI மற்றும் வீடியோ அழைப்புகள் இடைநிறுத்தப்பட்டுள்ளன.",
        "reconnect": "மீண்டும் இணைக்கவும்",
        "read_aloud": "பக்கத்தை வாசிக்கவும் (TTS)",
        "notifications": "அறிவிப்புகள்",
        "language": "மொழி",

        "nav_clinical_care": "மருத்துவ பராமரிப்பு",
        "dashboard": "டாஷ்போர்டு",
        "new_prediction": "புதிய கணிப்பு",
        "patients": "நோயாளிகள் பட்டியல்",
        "prediction_history": "கணிப்பு வரலாறு",
        "analytics": "சிகிச்சை பகுப்பாய்வு",
        "model_insights": "மாதிரி நுண்ணறிவு",

        "nav_medical_docs": "மருத்துவ ஆவணங்கள்",
        "medical_documents": "மருத்துவ ஆவணங்கள்",
        "my_documents": "என் ஆவணங்கள்",
        "lab_reports": "ஆய்வக அறிக்கைகள்",
        "medical_certificates": "மருத்துவ சான்றிதழ்கள்",
        "verify_certificate": "சான்றிதழ் சரிபார்ப்பு",
        "prescriptions": "மருந்து பரிந்துரைகள்",
        "discharge_summaries": "டிஸ்சார்ஜ் சுருக்கம்",

        "nav_ai_ml": "AI & இயந்திர கற்றல்",
        "ai_and_ml": "AI & இயந்திர கற்றல்",
        "ml_dashboard": "ML டாஷ்போர்டு",
        "dataset_workspace": "தரவுத்தொகுப்பு பணியிடம்",
        "preprocessing": "தரவு முன்செயலாக்கம்",
        "model_training": "பயிற்சி அரங்கம்",
        "deep_learning_lab": "டீப் லேர்னிங் லேப்",
        "model_comparison": "மாதிரி ஒப்பீடு",
        "explainable_ai": "விளக்கக்கூடிய AI (SHAP)",
        "patient_embeddings": "நோயாளி பிரதிநிதித்துவம் (2D)",
        "ensemble_uncertainty": "குழு & நிச்சயமற்ற தன்மை",
        "model_monitoring": "மாதிரி கண்காணிப்பு",
        "model_registry": "மாதிரி பதிவேடு",
        "experiment_tracking": "சோதனை கண்காணிப்பு",
        "ask_the_model": "மாதிரியிடம் கேளுங்கள்",

        "nav_rl": "வலுவூட்டல் கற்றல் (RL)",
        "reinforcement_learning": "வலுவூட்டல் கற்றல் (RL)",
        "rl_dashboard": "RL டாஷ்போர்டு",
        "patient_environment": "நோயாளி சூழல்",
        "care_pathway_opt": "பராமரிப்பு பாதை தேர்வு",
        "digital_twin_sim": "டிஜிட்டல் இரட்டை உருவகப்படுத்துதல்",
        "safety_constraints": "பாதுகாப்பு கட்டுப்பாடுகள்",
        "human_review": "மருத்துவர் நேரடி மதிப்பாய்வு",
        "stack_architecture": "8-அடுக்கு AI கட்டமைப்பு",

        "nav_portals": "போர்ட்டல்கள் & டெலிஹெல்த்",
        "video_consultation": "CareAI வீடியோ ஆலோசனை",
        "patient_portal": "நோயாளி போர்டல்",
        "care_coordinator": "பராமரிப்பு ஒருங்கிணைப்பாளர்",
        "user_management": "பயனர் மேலாண்மை",
        "doctor_verification": "மருத்துவர் சரிபார்ப்பு",
        "security_audit_logs": "பாதுகாப்பு தணிக்கை பதிவுகள்",

        "nav_health_id": "சுகாதார ஐடி & பாஸ்கள்",
        "my_health_id": "என் சுகாதார ஐடி",
        "doctor_id_card": "மருத்துவர் அடையாள அட்டை",
        "digital_wallet": "டிஜிட்டல் பணப்பை",
        "scan_qr_code": "QR குறியீட்டை ஸ்கேன் செய்க",
        "temporary_share": "தற்காலிக அணுகல் பாஸ்",

        "nav_system": "அமைப்பு & கணக்கு",
        "settings": "அமைப்புகள்",
        "help": "உதவி & ஆதரவு",
        "active_sessions": "செயலில் உள்ள அமர்வுகள்",
        "welcome_tour": "வரவேற்பு சுற்றுலா",
        "privacy_safety": "தனியுரிமை & பாதுகாப்பு",

        "nav_home": "முகப்பு",
        "nav_patients": "நோயாளிகள்",
        "nav_predict": "கணிப்பு",
        "nav_telehealth": "டெலிஹெல்த்",
        "nav_menu": "மெனு",
        "nav_more": "மேலும்",

        "generate_prediction": "கணிப்பை உருவாக்கவும்",
        "evaluating_risk": "ஆபத்து காரணிகள் மதிப்பீடு செய்யப்படுகின்றன...",
        "view_assessment": "மதிப்பீட்டை காண்க",
        "view_profile": "சுயவிவரத்தை காண்க",
        "export_report": "அறிக்கையை ஏற்றுமதி செய்",
        "save_assessment": "மதிப்பீட்டை சேமிக்கவும்",
        "apply_filters": "வடிகட்டிகளைப் பயன்படுத்து",
        "approve": "ஒப்புதல் அளிக்கவும்",
        "reject": "நிராகரி",
        "override": "மேலெழுதவும்",
        "modify": "மாற்றியமைக்க",
        "view_simulation": "உருவகப்படுத்துதலை காண்க",
        "human_review_required": "மருத்துவர் மதிப்பாய்வு தேவை",
        "simulation_result": "உருவகப்படுத்துதல் முடிவு",
        "rl_workflow_rec": "RL பரிந்துரை",
        "verify_identity": "அடையாளத்தை சரிபார்க்கவும்",
        "forgot_password": "கடவுச்சொல்லை மறந்துவிட்டீர்களா?",
        "start_prediction": "கணிப்பை தொடங்கவும்",
        "explore_dashboard": "டாஷ்போர்டை பார்க்கவும்",
        "save_to_ehr": "EHR-ல் சேமிக்கவும்",
        "end_call": "அழைப்பை முடிக்கவும்",
        "join_call": "ஆலோசனையில் சேரவும்",
        "confirm": "உறுதி செய்",
        "cancel": "ரத்து செய்",
        "download_pdf": "PDF பதிவிறக்குக",
        "print_prescription": "மருந்து சீட்டை அச்சிடுக",
        "talk_to_doctor": "AI மருத்துவரிடம் பேசுக (குரல்)",
        "listening": "கேட்கிறது... இப்போது பேசுங்கள்",
        "generate_rx": "மருந்து பரிந்துரை உருவாக்குக",
        "ai_summarize": "AI சுருக்கம்",
        "translate_notes": "மொழிபெயர்க்க",
        "issue_certificate": "சான்றிதழ் வழங்குக",
        "emergency_sos": "அவசர SOS",

        "ai_doctor_copilot": "CareAI மருத்துவ வழிகாட்டி",
        "ai_doctor_name": "டாக்டர் CareAI",
        "consultation_title": "AI மருத்துவர் நேரலை வீடியோ ஆலோசனை",
        "device_check": "சாதன தயார்நிலை சரிபார்ப்பு",
        "camera_ready": "கேமரா: தயார்",
        "mic_ready": "மைக்ரோஃபோன்: தயார்",
        "network_excellent": "நெட்வொர்க்: சிறந்தது (32ms)",
        "view_ai_doctor": "AI மருத்துவர் காட்சி",
        "view_patient": "நோயாளி உருவகப்படுத்துதல்",
        "view_split": "பிரித்த டெலிமெட்ரி பார்வை",
        "live_ecg": "நேரலை ECG & உடல் அளவீடுகள்",
        "heart_rate": "இதய துடிப்பு",
        "blood_pressure": "இரத்த அழுத்தம்",
        "oxygen_sat": "ஆக்ஸிஜன் அளவு",
        "resp_rate": "சுவாச விகிதம்",
        "temperature": "வெப்பநிலை",
        "live_captions": "நேரலை இருமொழி தலைப்புகள்",
        "ai_clinical_insight": "AI மருத்துவ நுண்ணறிவு",
        "readmission_risk": "மறுஅனுமதி ஆபத்து",
        "ppo_rl_pathway": "PPO RL பராமரிப்பு வழிமுறை",
        "ask_ai_placeholder": "மருத்துவ கேள்விகளைக் கேளுங்கள் அல்லது பேசுங்கள்...",
        "ehr_clinical_notes": "மருத்துவ குறிப்புகள் (EHR)",
        "rx_modal_title": "அதிகாரப்பூர்வ மருத்துவ மருந்து சீட்டு",

        "high_risk": "அதிக ஆபத்து",
        "moderate_risk": "நடுத்தர ஆபத்து",
        "low_risk": "குறைந்த ஆபத்து",
        "reviewed": "மதிப்பாய்வு செய்யப்பட்டது",
        "pending": "நிலுவையில் உள்ளது",
        "actioned": "நடவடிக்கை எடுக்கப்பட்டது",
        "active": "செயலில் உள்ளது",
        "completed": "நிறைவடைந்தது",
        "live_encrypted": "நேரலை · குறியாக்கம் செய்யப்பட்டது",
        "male": "ஆண்",
        "female": "பெண்",
        "other": "மற்றவை",

        "total_screened": "மொத்த நோயாளிகள்",
        "avg_risk_score": "சராசரி ஆபத்து மதிப்பெண்",
        "active_patients": "தற்போதைய உள்நோயாளிகள்",
        "accuracy": "துல்லியம்",
        "precision": "துல்லியத்தன்மை",
        "recall": "நினைவுகூர்தல்",
        "f1_score": "F1 மதிப்பெண்",
        "roc_auc": "ROC-AUC",
        "cardiology": "இதயவியல் துறை (Cardiology)",
        "general_medicine": "பொது மருத்துவம்",
        "endocrinology": "நாளமில்லா சுரப்பி துறை",
        "pulmonology": "நுரையீரல் துறை",
        "nephrology": "சிறுநீரகவியல் துறை (Nephrology)"
    },

    kn: {
        "brand_name": "ಎಚ್‌ಆರ್‌ಪಿ ಕ್ಲಿನಿಕಲ್",
        "brand_subtitle": "ನಿಖರ ಆರೈಕೆ & AI",
        "hospital_suite": "ಆರೋಗ್ಯ ರಕ್ಷಣಾ ಸೂಟ್",
        "header_title": "ಆಸ್ಪತ್ರೆ ಮರುದಾಖಲಾತಿ ಅಪಾಯ ಮುನ್ಸೂಚಕ",
        "search_placeholder": "ರೋಗಿ, ವೈದ್ಯರನ್ನು ಹುಡುಕಿ...",
        "search_mobile_placeholder": "ರೋಗಿ, ದಾಖಲೆಗಳನ್ನು ಹುಡುಕಿ...",
        "dr_name": "ಡಾ. ರಂಜೀತ್ ಕುಮಾರ್, MD",
        "dr_title": "ಮುಖ್ಯ AI ವಾಸ್ತುಶಿಲ್ಪಿ",
        "doctor_id": "ವೈದ್ಯರ ಡಿಜಿಟಲ್ ಐಡಿ",
        "edit_profile": "ಪ್ರೊಫೈಲ್ ಸಂಪಾದಿಸಿ",
        "account_settings": "ಖಾತೆ & ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "master_ebook": "ಸಂಪೂರ್ಣ ಇ-ಬುಕ್",
        "logout": "ಲಾಗ್ ಔಟ್",
        "sign_out_lock": "ಲಾಗ್ ಔಟ್ / ಸೆಷನ್ ಲಾಕ್ ಮಾಡಿ",
        "sign_out_switch": "ಲಾಗ್ ಔಟ್ / ಪಾತ್ರ ಬದಲಾಯಿಸಿ",
        "offline_banner": "ಆಫ್‌ಲೈನ್ ಮೋಡ್ ಸಕ್ರಿಯವಾಗಿದೆ — ಲೈವ್ AI ಮತ್ತು ವೀಡಿಯೊ ಕರೆಗಳನ್ನು ವಿರಾಮಗೊಳಿಸಲಾಗಿದೆ.",
        "reconnect": "ಮರುಸಂಪರ್ಕಿಸಿ",
        "read_aloud": "ಪುಟವನ್ನು ಓದಿ (TTS)",
        "notifications": "ಅಧಿಸೂಚನೆಗಳು",
        "language": "ಭಾಷೆ",

        "nav_clinical_care": "ಕ್ಲಿನಿಕಲ್ ಆರೈಕೆ",
        "dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "new_prediction": "ಹೊಸ ಮುನ್ಸೂಚನೆ",
        "patients": "ರೋಗಿಗಳ ಪಟ್ಟಿ",
        "prediction_history": "ಮುನ್ಸೂಚನೆ ಇತಿಹಾಸ",
        "analytics": "ಕ್ಲಿನಿಕಲ್ ವಿಶ್ಲೇಷಣೆ",
        "model_insights": "ಮಾದರಿ ಒಳನೋಟಗಳು",

        "nav_medical_docs": "ವೈದ್ಯಕೀಯ ದಾಖಲೆಗಳು",
        "medical_documents": "ವೈದ್ಯಕೀಯ ದಾಖಲೆಗಳು",
        "my_documents": "ನನ್ನ ದಾಖಲೆಗಳು",
        "lab_reports": "ಪ್ರಯೋಗಾಲಯ ವರದಿಗಳು",
        "medical_certificates": "ವೈದ್ಯಕೀಯ ಪ್ರಮಾಣಪತ್ರಗಳು",
        "verify_certificate": "ಪ್ರಮಾಣಪತ್ರ ಪರಿಶೀಲನೆ",
        "prescriptions": "ಔಷಧಿ ಚೀಟಿಗಳು",
        "discharge_summaries": "ಡಿಸ್ಚಾರ್ಜ್ ಸಾರಾಂಶ",

        "nav_ai_ml": "AI & ಯಂತ್ರ ಕಲಿಕೆ",
        "ai_and_ml": "AI & ಯಂತ್ರ ಕಲಿಕೆ",
        "ml_dashboard": "ML ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "dataset_workspace": "ಡೇಟಾಸೆಟ್ ಕಾರ್ಯಕ್ಷೇತ್ರ",
        "preprocessing": "ಡೇಟಾ ಪೂರ್ವ ಸಂಸ್ಕರಣೆ",
        "model_training": "ತರಬೇತಿ ಸ್ಟುಡಿಯೋ",
        "deep_learning_lab": "ಡೀಪ್ ಲರ್ನಿಂಗ್ ಲ್ಯಾಬ್",
        "model_comparison": "ಮಾದರಿ ಹೋಲಿಕೆ",
        "explainable_ai": "ವಿವರಿಸಬಹುದಾದ AI (SHAP)",
        "patient_embeddings": "ರೋಗಿ ಪ್ರಾತಿನಿಧ್ಯ (2D)",
        "ensemble_uncertainty": "ಸಮಗ್ರ & ಅನಿಶ್ಚಿತತೆ",
        "model_monitoring": "ಮಾದರಿ ಮೇಲ್ವಿಚಾರಣೆ",
        "model_registry": "ಮಾದರಿ ನೋಂದಣಿ",
        "experiment_tracking": "ಪ್ರಯೋಗ ಟ್ರ್ಯಾಕಿಂಗ್",
        "ask_the_model": "ಮಾದರಿಯನ್ನು ಕೇಳಿ",

        "nav_rl": "ಬಲವರ್ಧನೆ ಕಲಿಕೆ (RL)",
        "reinforcement_learning": "ಬಲವರ್ಧನೆ ಕಲಿಕೆ (RL)",
        "rl_dashboard": "RL ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "patient_environment": "ರೋಗಿ ಪರಿಸರ",
        "care_pathway_opt": "ಆರೈಕೆ ಮಾರ್ಗ ಆಪ್ಟಿಮೈಜರ್",
        "digital_twin_sim": "ಡಿಜಿಟಲ್ ಟ್ವಿನ್ ಸಿಮ್ಯುಲೇಶನ್",
        "safety_constraints": "ಸುರಕ್ಷತಾ ನಿರ್ಬಂಧಗಳು",
        "human_review": "ವೈದ್ಯರ ನೇರ ವಿಮರ್ಶೆ",
        "stack_architecture": "8-ಪದರದ AI ವಾಸ್ತುಶಿಲ್ಪ",

        "nav_portals": "ಪೋರ್ಟಲ್‌ಗಳು & ಟೆಲಿಹೆಲ್ತ್",
        "video_consultation": "CareAI ವೀಡಿಯೊ ಸಮಾಲೋಚನೆ",
        "patient_portal": "ರೋಗಿ ಪೋರ್ಟಲ್",
        "care_coordinator": "ಆರೈಕೆ ಸಂಯೋಜಕ",
        "user_management": "ಬಳಕೆದಾರರ ನಿರ್ವಹಣೆ",
        "doctor_verification": "ವೈದ್ಯರ ಪರಿಶೀಲನೆ",
        "security_audit_logs": "ಭದ್ರತಾ ಆಡಿಟ್ ಲಾಗ್‌ಗಳು",

        "nav_health_id": "ಆರೋಗ್ಯ ಐಡಿ & ಪಾಸ್‌ಗಳು",
        "my_health_id": "ನನ್ನ ಆರೋಗ್ಯ ಐಡಿ",
        "doctor_id_card": "ವೈದ್ಯರ ಗುರುತಿನ ಚೀಟಿ",
        "digital_wallet": "ಡಿಜಿಟಲ್ ವಾಲೆಟ್",
        "scan_qr_code": "QR ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ",
        "temporary_share": "ತಾತ್ಕಾಲಿಕ ಪ್ರವೇಶ ಪಾಸ್",

        "nav_system": "ವ್ಯವಸ್ಥೆ & ಖಾತೆ",
        "settings": "ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "help": "ಸಹಾಯ & ಬೆಂಬಲ",
        "active_sessions": "ಸಕ್ರಿಯ ಸೆಷನ್‌ಗಳು",
        "welcome_tour": "ಸ್ವಾಗತ ಪ್ರವಾಸ",
        "privacy_safety": "ಗೌಪ್ಯತೆ & ಸುರಕ್ಷತೆ",

        "nav_home": "ಮುಖಪುಟ",
        "nav_patients": "ರೋಗಿಗಳು",
        "nav_predict": "ಮುನ್ಸೂಚನೆ",
        "nav_telehealth": "ಟೆಲಿಹೆಲ್ತ್",
        "nav_menu": "ಮೆನು",
        "nav_more": "ಹೆಚ್ಚು",

        "generate_prediction": "ಮುನ್ಸೂಚನೆ ರಚಿಸಿ",
        "evaluating_risk": "ಅಪಾಯದ ಅಂಶಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲಾಗುತ್ತಿದೆ...",
        "view_assessment": "ಮೌಲ್ಯಮಾಪನ ವೀಕ್ಷಿಸಿ",
        "view_profile": "ಪ್ರೊಫೈಲ್ ವೀಕ್ಷಿಸಿ",
        "export_report": "ವರದಿ ರಫ್ತು ಮಾಡಿ (CSV/PDF)",
        "save_assessment": "ಮೌಲ್ಯಮಾಪನ ಉಳಿಸಿ",
        "apply_filters": "ಫಿಲ್ಟರ್‌ಗಳನ್ನು ಅನ್ವಯಿಸಿ",
        "approve": "ಅನುಮೋದಿಸಿ",
        "reject": "ತಿರಸ್ಕರಿಸಿ",
        "override": "ಓವರ್‌ರೈಡ್ ಮಾಡಿ",
        "modify": "ಮಾರ್ಪಡಿಸಿ",
        "view_simulation": "ಸಿಮ್ಯುಲೇಶನ್ ವೀಕ್ಷಿಸಿ",
        "human_review_required": "ವೈದ್ಯರ ವಿಮರ್ಶೆ ಅಗತ್ಯವಿದೆ",
        "simulation_result": "ಸಿಮ್ಯುಲೇಶನ್ ಫಲಿತಾಂಶ",
        "rl_workflow_rec": "RL ಶಿಫಾರಸು",
        "verify_identity": "ಗುರುತನ್ನು ಪರಿಶೀಲಿಸಿ",
        "forgot_password": "ಪಾಸ್‌ವರ್ಡ್ ಮರೆತಿರಾ?",
        "start_prediction": "ಮುನ್ಸೂಚನೆ ಪ್ರಾರಂಭಿಸಿ",
        "explore_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಅನ್ವೇಷಿಸಿ",
        "save_to_ehr": "EHR ನಲ್ಲಿ ಉಳಿಸಿ",
        "end_call": "ಕರೆ ಮುಕ್ತಾಯಗೊಳಿಸಿ",
        "join_call": "ಸಮಾಲೋಚನೆಗೆ ಸೇರಿ",
        "confirm": "ಖಚಿತಪಡಿಸಿ",
        "cancel": "ರದ್ದುಮಾಡಿ",
        "download_pdf": "PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "print_prescription": "ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ ಮುದ್ರಿಸಿ",
        "talk_to_doctor": "AI ವೈದ್ಯರೊಂದಿಗೆ ಮಾತನಾಡಿ (ಧ್ವನಿ)",
        "listening": "ಆಲಿಸಲಾಗುತ್ತಿದೆ... ಮಾತನಾಡಿ",
        "generate_rx": "ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ ರಚಿಸಿ",
        "ai_summarize": "AI ಸಾರಾಂಶ",
        "translate_notes": "ಟಿಪ್ಪಣಿಗಳನ್ನು ಅನುವಾದಿಸಿ",
        "issue_certificate": "ಪ್ರಮಾಣಪತ್ರ ನೀಡಿ",
        "emergency_sos": "ತುರ್ತು SOS",

        "ai_doctor_copilot": "CareAI ವೈದ್ಯಕೀಯ ಸಹಾಯಕ",
        "ai_doctor_name": "ಡಾ. CareAI",
        "consultation_title": "AI ವೈದ್ಯರ ಲೈವ್ ವೀಡಿಯೊ ಸಮಾಲೋಚನೆ",
        "device_check": "ಸಾಧನ ಸಿದ್ಧತೆ ಪರಿಶೀಲನೆ",
        "camera_ready": "ಕ್ಯಾಮೆರಾ: ಸಿದ್ಧವಾಗಿದೆ",
        "mic_ready": "ಮೈಕ್ರೊಫೋನ್: ಸಿದ್ಧವಾಗಿದೆ",
        "network_excellent": "ನೆಟ್‌ವರ್ಕ್: ಅತ್ಯುತ್ತಮ (32ms)",
        "view_ai_doctor": "AI ವೈದ್ಯರ ವೀಕ್ಷಣೆ",
        "view_patient": "ರೋಗಿ ಸಿಮ್ಯುಲೇಶನ್",
        "view_split": "ವಿಭಜಿತ ಟೆಲಿಮೆಟ್ರಿ ವೀಕ್ಷಣೆ",
        "live_ecg": "ಲೈವ್ ECG & ದೇಹದ ಅಳತೆಗಳು",
        "heart_rate": "ಹೃದಯ ಬಡಿತ",
        "blood_pressure": "ರಕ್ತದೊತ್ತಡ",
        "oxygen_sat": "ಆಮ್ಲಜನಕ ಮಟ್ಟ",
        "resp_rate": "ಉಸಿರಾಟದ ದರ",
        "temperature": "ತಾಪಮಾನ",
        "live_captions": "ಲೈವ್ ಉಪಶೀರ್ಷಿಕೆಗಳು",
        "ai_clinical_insight": "AI ಕ್ಲಿನಿಕಲ್ ಒಳನೋಟ",
        "readmission_risk": "ಮರುದಾಖಲಾತಿ ಅಪಾಯ",
        "ppo_rl_pathway": "PPO RL ಆರೈಕೆ ಮಾರ್ಗ",
        "ask_ai_placeholder": "ಪ್ರಶ್ನೆ ಕೇಳಿ ಅಥವಾ ಮಾತನಾಡಿ...",
        "ehr_clinical_notes": "ಕ್ಲಿನಿಕಲ್ ಟಿಪ್ಪಣಿಗಳು (EHR)",
        "rx_modal_title": "ಅಧಿಕೃತ ವೈದ್ಯಕೀಯ ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್",

        "high_risk": "ಹೆಚ್ಚಿನ ಅಪಾಯ",
        "moderate_risk": "ಮಧ್ಯಮ ಅಪಾಯ",
        "low_risk": "ಕಡಿಮೆ ಅಪಾಯ",
        "reviewed": "ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "pending": "ಬಾಕಿ ಉಳಿದಿದೆ",
        "actioned": "ಕ್ರಮ ಕೈಗೊಳ್ಳಲಾಗಿದೆ",
        "active": "ಸಕ್ರಿಯ",
        "completed": "ಪೂರ್ಣಗೊಂಡಿದೆ",
        "live_encrypted": "ಲೈವ್ · ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಲಾಗಿದೆ",
        "male": "ಪುರುಷ",
        "female": "ಮಹಿಳೆ",
        "other": "ಇತರೆ",

        "total_screened": "ಒಟ್ಟು ರೋಗಿಗಳು",
        "avg_risk_score": "ಸರಾಸರಿ ಅಪಾಯದ ಸ್ಕೋರ್",
        "active_patients": "ಹಾಲಿ ಒಳರೋಗಿಗಳು",
        "accuracy": "ನಿಖರತೆ",
        "precision": "ಖಚಿತತೆ",
        "recall": "ನೆನಪು",
        "f1_score": "F1 ಸ್ಕೋರ್",
        "roc_auc": "ROC-AUC",
        "cardiology": "ಹೃದ್ರೋಗ ಶಾಸ್ತ್ರ (Cardiology)",
        "general_medicine": "ಸಾಮಾನ್ಯ ಔಷಧ",
        "endocrinology": "ಎಂಡೋಕ್ರೈನಾಲಜಿ",
        "pulmonology": "ಶ್ವಾಸಕೋಶ ಶಾಸ್ತ್ರ",
        "nephrology": "ಮೂತ್ರಪಿಂಡ ಶಾಸ್ತ್ರ (Nephrology)"
    },

    ml: {
        "brand_name": "എച്ച്ആർപി ക്ലിനിക്കൽ",
        "brand_subtitle": "കൃത്യതയാർന്ന പരിചരണവും AI യും",
        "hospital_suite": "ഹെൽത്ത് കെയർ സ്യൂട്ട്",
        "header_title": "ആശുപത്രി പുനഃപ്രവേശന അപകടസാധ്യത പ്രവചനം",
        "search_placeholder": "രോഗി, ഡോക്ടറെ തിരയുക...",
        "search_mobile_placeholder": "രോഗി, രേഖകൾ തിരയുക...",
        "dr_name": "ഡോ. രഞ്ജിത് കുമാർ, MD",
        "dr_title": "ലീഡ് AI ആർക്കിടെക്റ്റ്",
        "doctor_id": "ഡോക്ടർ ഡിജിറ്റൽ ഐഡി",
        "edit_profile": "പ്രൊഫൈൽ തിരുത്തുക",
        "account_settings": "അക്കൗണ്ട് & ക്രമീകരണങ്ങൾ",
        "master_ebook": "മാസ്റ്റർ ഇ-ബുക്ക്",
        "logout": "ലോഗ് ഔട്ട്",
        "sign_out_lock": "ലോഗ് ഔട്ട് / സെഷൻ ലോക്ക് ചെയ്യുക",
        "sign_out_switch": "ലോഗ് ഔട്ട് / റോൾ മാറ്റുക",
        "offline_banner": "ഓഫ്‌ലൈൻ മോഡ് സജീവമാണ് — ലൈവ് AI, വീഡിയോ കോളുകൾ താൽക്കാലികമായി നിർത്തിവച്ചു.",
        "reconnect": "വീണ്ടും ബന്ധിപ്പിക്കുക",
        "read_aloud": "പേജ് വായിക്കുക (TTS)",
        "notifications": "അറിയിപ്പുകൾ",
        "language": "ഭാഷ",

        "nav_clinical_care": "ക്ലിനിക്കൽ പരിചരണം",
        "dashboard": "ഡാഷ്‌ബോർഡ്",
        "new_prediction": "പുതിയ പ്രവചനം",
        "patients": "രോഗികളുടെ പട്ടിക",
        "prediction_history": "പ്രവചന ചരിത്രം",
        "analytics": "ക്ലിനിക്കൽ വിശകലനം",
        "model_insights": "മോഡൽ സ്ഥിതിവിവരക്കണക്കുകൾ",

        "nav_medical_docs": "മെഡിക്കൽ രേഖകൾ",
        "medical_documents": "മെഡിക്കൽ രേഖകൾ",
        "my_documents": "എന്റെ രേഖകൾ",
        "lab_reports": "ലാബ് റിപ്പോർട്ടുകൾ",
        "medical_certificates": "മെഡിക്കൽ സർട്ടിഫിക്കറ്റുകൾ",
        "verify_certificate": "സർട്ടിഫിക്കറ്റ് പരിശോധന",
        "prescriptions": "കുറിപ്പടികൾ",
        "discharge_summaries": "ഡിസ്ചാർജ് സംഗ്രഹം",

        "nav_ai_ml": "AI & മെഷീൻ ലേണിംഗ്",
        "ai_and_ml": "AI & മെഷീൻ ലേണിംഗ്",
        "ml_dashboard": "ML ഡാഷ്‌ബോർഡ്",
        "dataset_workspace": "ഡാറ്റാസെറ്റ് വർക്ക്‌സ്‌പേസ്",
        "preprocessing": "ഡാറ്റ പ്രീപ്രോസസ്സിംഗ്",
        "model_training": "ട്രെയിനിംഗ് സ്റ്റുഡിയോ",
        "deep_learning_lab": "ഡീപ് ലേണിംഗ് ലാബ്",
        "model_comparison": "മോഡൽ താരതമ്യം",
        "explainable_ai": "വിശദീകരിക്കാവുന്ന AI (SHAP)",
        "patient_embeddings": "രോഗി പ്രാതിനിധ്യം (2D)",
        "ensemble_uncertainty": "എൻസെംബിൾ & അനിശ്ചിതത്വം",
        "model_monitoring": "മോഡൽ നിരീക്ഷണം",
        "model_registry": "മോഡൽ രജിസ്ട്രി",
        "experiment_tracking": "പരീക്ഷണ ട്രാക്കിംഗ്",
        "ask_the_model": "മോഡലിനോട് ചോദിക്കുക",

        "nav_rl": "റീഇൻഫോഴ്‌സ്‌മെന്റ് ലേണിംഗ് (RL)",
        "reinforcement_learning": "റീഇൻഫോഴ്‌സ്‌മെന്റ് ലേണിംഗ് (RL)",
        "rl_dashboard": "RL ഡാഷ്‌ബോർഡ്",
        "patient_environment": "രോഗി പരിചരണ പരിസ്ഥിതി",
        "care_pathway_opt": "പരിചരണ പാത ഒപ്റ്റിമൈസർ",
        "digital_twin_sim": "ഡിജിറ്റൽ ഇരട്ട സിമുലേഷൻ",
        "safety_constraints": "സുരക്ഷാ നിയന്ത്രണങ്ങൾ",
        "human_review": "ഡോക്ടർ നേരിട്ടുള്ള അവലോകനം",
        "stack_architecture": "8-ലെയർ AI ഘടന",

        "nav_portals": "പോർട്ടലുകൾ & ടെലിഹെൽത്ത്",
        "video_consultation": "CareAI വീഡിയോ കൺസൾട്ടേഷൻ",
        "patient_portal": "രോഗി പോർട്ടൽ",
        "care_coordinator": "കെയർ കോർഡിനേറ്റർ",
        "user_management": "ഉപയോക്തൃ മാനേജ്മെന്റ്",
        "doctor_verification": "ഡോക്ടർ പരിശോധന",
        "security_audit_logs": "സുരക്ഷാ ഓഡിറ്റ് ലോഗുകൾ",

        "nav_health_id": "ഹെൽത്ത് ഐഡി & പാസുകൾ",
        "my_health_id": "എന്റെ ഹെൽത്ത് ഐഡി",
        "doctor_id_card": "ഡോക്ടർ തിരിച്ചറിയൽ കാർഡ്",
        "digital_wallet": "ഡിജിറ്റൽ വാലറ്റ്",
        "scan_qr_code": "QR കോഡ് സ്കാൻ ചെയ്യുക",
        "temporary_share": "താൽക്കാലിക പാസുകൾ",

        "nav_system": "സിസ്റ്റം & അക്കൗണ്ട്",
        "settings": "ക്രമീകരണങ്ങൾ",
        "help": "സഹായവും പിന്തുണയും",
        "active_sessions": "സജീവ സെഷനുകൾ",
        "welcome_tour": "സ്വാഗത ടൂർ",
        "privacy_safety": "സ്വകാര്യതയും സുരക്ഷയും",

        "nav_home": "ഹോം",
        "nav_patients": "രോഗികൾ",
        "nav_predict": "പ്രവചനം",
        "nav_telehealth": "ടെലിഹെൽത്ത്",
        "nav_menu": "മെനു",
        "nav_more": "കൂടുതൽ",

        "generate_prediction": "പ്രവചനം തയ്യാറാക്കുക",
        "evaluating_risk": "അപകടസാധ്യത ഘടകങ്ങൾ വിലയിരുത്തുന്നു...",
        "view_assessment": "വിലയിരുത്തൽ കാണുക",
        "view_profile": "പ്രൊഫൈൽ കാണുക",
        "export_report": "റിപ്പോർട്ട് ഡൗൺലോഡ് ചെയ്യുക (CSV/PDF)",
        "save_assessment": "വിലയിരുത്തൽ സംരക്ഷിക്കുക",
        "apply_filters": "ഫിൽട്ടറുകൾ പ്രയോഗിക്കുക",
        "approve": "അംഗീകരിക്കുക",
        "reject": "നിരസിക്കുക",
        "override": "മാറ്റിയെഴുതുക",
        "modify": "തിരുത്തുക",
        "view_simulation": "സിമുലേഷൻ കാണുക",
        "human_review_required": "ഡോക്ടറുടെ അവലോകനം ആവശ്യമാണ്",
        "simulation_result": "സിമുലേഷൻ ഫലം",
        "rl_workflow_rec": "RL ശുപാർശ",
        "verify_identity": "തിരിച്ചറിയൽ പരിശോധിക്കുക",
        "forgot_password": "പാസ്‌വേഡ് മറന്നോ?",
        "start_prediction": "പ്രവചനം ആരംഭിക്കുക",
        "explore_dashboard": "ഡാഷ്‌ബോർഡ് കാണുക",
        "save_to_ehr": "EHR-ൽ സംരക്ഷിക്കുക",
        "end_call": "കോൾ അവസാനിപ്പിക്കുക",
        "join_call": "കൺസൾട്ടേഷനിൽ ചേരുക",
        "confirm": "സ്ഥിരീകരിക്കുക",
        "cancel": "റദ്ദാക്കുക",
        "download_pdf": "PDF ഡൗൺലോഡ് ചെയ്യുക",
        "print_prescription": "പ്രിസ്‌ക്രിപ്ഷൻ പ്രിന്റ് ചെയ്യുക",
        "talk_to_doctor": "AI ഡോക്ടറോട് സംസാരിക്കുക (ശബ്ദം)",
        "listening": "കേൾക്കുന്നു... ഇപ്പോൾ സംസാരിക്കൂ",
        "generate_rx": "കുറിപ്പടി തയ്യാറാക്കുക",
        "ai_summarize": "AI സംഗ്രഹം",
        "translate_notes": "കുറിപ്പുകൾ വിവർത്തനം ചെയ്യുക",
        "issue_certificate": "സർട്ടിഫിക്കറ്റ് നൽകുക",
        "emergency_sos": "അടിയന്തര SOS",

        "ai_doctor_copilot": "CareAI ക്ലിനിക്കൽ കോപൈലറ്റ്",
        "ai_doctor_name": "ഡോ. CareAI",
        "consultation_title": "AI ഡോക്ടർ ലൈവ് വീഡിയോ കൺസൾട്ടേഷൻ",
        "device_check": "ഡിവൈസ് പരിശോധന",
        "camera_ready": "ക്യാമറ: തയ്യാറാണ്",
        "mic_ready": "മൈക്രോഫോൺ: തയ്യാറാണ്",
        "network_excellent": "നെറ്റ്‌വർക്ക്: മികച്ചത് (32ms)",
        "view_ai_doctor": "AI ഡോക്ടർ ഫീഡ്",
        "view_patient": "രോഗി സിമുലേഷൻ",
        "view_split": "ടെലിമെട്രി സ്പ്ലിറ്റ് വ്യൂ",
        "live_ecg": "ലൈവ് ഇസിജി & വൈറ്റൽസ്",
        "heart_rate": "ഹൃദയമിടിപ്പ്",
        "blood_pressure": "രക്തസമ്മർദ്ദം",
        "oxygen_sat": "ഓക്സിജൻ അളവ്",
        "resp_rate": "ശ്വസന നിരക്ക്",
        "temperature": "താപനില",
        "live_captions": "ലൈവ് സബ്ടൈറ്റിലുകൾ",
        "ai_clinical_insight": "AI ക്ലിനിക്കൽ സ്ഥിതിവിവരക്കണക്ക്",
        "readmission_risk": "പുനഃപ്രവേശന അപകടസാധ്യത",
        "ppo_rl_pathway": "PPO RL പരിചരണ പാത",
        "ask_ai_placeholder": "ചോദ്യം ചോദിക്കുക അല്ലെങ്കിൽ സംസാരിക്കുക...",
        "ehr_clinical_notes": "ക്ലിനിക്കൽ കുറിപ്പുകൾ (EHR)",
        "rx_modal_title": "ഔദ്യോഗിക മെഡിക്കൽ കുറിപ്പടി",

        "high_risk": "ഉയർന്ന അപകടസാധ്യത",
        "moderate_risk": "ഇടത്തരം അപകടസാധ്യത",
        "low_risk": "കുറഞ്ഞ അപകടസാധ്യത",
        "reviewed": "അവലോകനം ചെയ്തു",
        "pending": "തീർപ്പുകൽപ്പിക്കാത്തത്",
        "actioned": "നടപടി സ്വീകരിച്ചു",
        "active": "സജീവം",
        "completed": "പൂർത്തിയായി",
        "live_encrypted": "തത്സമയം · എൻക്രിപ്റ്റ് ചെയ്തത്",
        "male": "പുരുഷൻ",
        "female": "സ്ത്രീ",
        "other": "മറ്റുള്ളവ",

        "total_screened": "ആകെ പരിശോധിച്ചവർ",
        "avg_risk_score": "ശരാശരി അപകടസാധ്യത സ്കോർ",
        "active_patients": "നിലവിലെ ഇൻപേഷ്യന്റുകൾ",
        "accuracy": "കൃത്യത",
        "precision": "സൂക്ഷ്മത",
        "recall": "ഓർമ്മപ്പെടുത്തൽ",
        "f1_score": "F1 സ്കോർ",
        "roc_auc": "ROC-AUC",
        "cardiology": "ഹൃദ്രോഗ വിഭാഗം (Cardiology)",
        "general_medicine": "ജനറൽ മെഡിസിൻ",
        "endocrinology": "എൻഡോക്രൈനോളജി",
        "pulmonology": "ശ്വാസകോശ രോഗ വിഭാഗം",
        "nephrology": "വൃക്കരോഗ വിഭാഗം (Nephrology)"
    },

    te: {
        "brand_name": "హెచ్‌ఆర్‌పి క్లినికల్",
        "brand_subtitle": "ఖచ్చితమైన సంరక్షణ & AI",
        "hospital_suite": "హెల్త్‌కేర్ సూట్",
        "header_title": "ఆసుపత్రి రీఅడ్మిషన్ రిస్క్ ప్రిడిక్టర్",
        "search_placeholder": "రోగి, వైద్యుడిని శోధించండి...",
        "search_mobile_placeholder": "రోగి, పత్రాలు శోధించండి...",
        "dr_name": "డా. రంజీత్ కుమార్, MD",
        "dr_title": "ప్రధాన AI ఆర్కిటెక్ట్",
        "doctor_id": "డాక్టర్ డిజిటల్ ID",
        "edit_profile": "ప్రొఫైల్ సవరించండి",
        "account_settings": "ఖాతా & సెట్టింగ్‌లు",
        "master_ebook": "మాస్టర్ ఈ-బుక్ (88 అధ్యాయాలు)",
        "logout": "లాగ్ అవుట్",
        "sign_out_lock": "లాగ్ అవుట్ / సెషన్ లాక్ చేయండి",
        "sign_out_switch": "లాగ్ అవుట్ / పాత్ర మార్చండి",
        "offline_banner": "ఆఫ్‌లైన్ మోడ్ సక్రియంగా ఉంది — లైవ్ AI & వీడియో కాల్స్ నిలిపివేయబడ్డాయి.",
        "reconnect": "తిరిగి కనెక్ట్ చేయండి",
        "read_aloud": "పేజీని బిగ్గరగా చదవండి (TTS)",
        "notifications": "నోటిఫికేషన్‌లు",
        "language": "భాష",

        "nav_clinical_care": "క్లినికల్ సంరక్షణ",
        "dashboard": "డ్యాష్‌బోర్డ్",
        "new_prediction": "కొత్త అంచనా",
        "patients": "రోగుల జాబితా",
        "prediction_history": "అంచనా చరిత్ర",
        "analytics": "క్లినికల్ విశ్లేషణ",
        "model_insights": "మోడల్ అంతర్దృష్టులు",

        "nav_medical_docs": "వైద్య పత్రాలు",
        "medical_documents": "వైద్య పత్రాలు",
        "my_documents": "నా పత్రాలు",
        "lab_reports": "ల్యాబ్ రిపోర్టులు",
        "medical_certificates": "వైద్య ధృవీకరణ పత్రాలు",
        "verify_certificate": "ధృవీకరణ పత్రం తనిఖీ",
        "prescriptions": "ప్రిస్క్రిప్షన్లు",
        "discharge_summaries": "డిశ్చార్జ్ సారాంశం",

        "nav_ai_ml": "AI & మెషిన్ లెర్నింగ్",
        "ai_and_ml": "AI & మెషిన్ లెర్నింగ్",
        "ml_dashboard": "ML డ్యాష్‌బోర్డ్",
        "dataset_workspace": "డేటాసెట్ వర్క్‌స్పేస్",
        "preprocessing": "డేటా ప్రీప్రాసెసింగ్",
        "model_training": "ట్రైనింగ్ స్టూడియో",
        "deep_learning_lab": "డీప్ లెర్నింగ్ ల్యాబ్",
        "model_comparison": "మోడల్ పోలిక",
        "explainable_ai": "వివరణాత్మక AI (SHAP)",
        "patient_embeddings": "రోగి ప్రాతినిధ్యం (2D)",
        "ensemble_uncertainty": "ఎన్సెంబుల్ & అనిశ్చితి",
        "model_monitoring": "మోడల్ డ్రిఫ్ట్ మానిటరింగ్",
        "model_registry": "మోడల్ రిజిస్ట్రీ",
        "experiment_tracking": "ప్రయోగ ట్రాకింగ్",
        "ask_the_model": "మోడల్‌ను అడగండి",

        "nav_rl": "రీఇన్‌ఫోర్స్‌మెంట్ లెర్నింగ్ (RL)",
        "reinforcement_learning": "రీఇన్‌ఫోర్స్‌మెంట్ లెర్నింగ్ (RL)",
        "rl_dashboard": "RL డ్యాష్‌బోర్డ్",
        "patient_environment": "రోగి సంరక్షణ వాతావరణం",
        "care_pathway_opt": "సంరక్షణ మార్గం ఆప్టిమైజర్",
        "digital_twin_sim": "డిజిటల్ ట్విన్ సిమ్యులేషన్",
        "safety_constraints": "భద్రతా పరిమితులు",
        "human_review": "వైద్యుడి ప్రత్యక్ష సమీక్ష",
        "stack_architecture": "8-పొరల AI ఆర్కిటెక్చర్",

        "nav_portals": "పోర్టల్స్ & టెలిహెల్త్",
        "video_consultation": "CareAI వీడియో సంప్రదింపులు",
        "patient_portal": "రోగి పోర్టల్",
        "care_coordinator": "కేర్ కోఆర్డినేటర్",
        "user_management": "వినియోగదారుల నిర్వహణ",
        "doctor_verification": "డాక్టర్ ధృవీకరణ",
        "security_audit_logs": "భద్రతా ఆడిట్ లాగ్‌లు",

        "nav_health_id": "హెల్త్ ID & పాస్‌లు",
        "my_health_id": "నా హెల్త్ ID",
        "doctor_id_card": "డాక్టర్ ID కార్డ్",
        "digital_wallet": "డిజిటల్ వాలెట్",
        "scan_qr_code": "QR కోడ్ స్కాన్ చేయండి",
        "temporary_share": "తాత్కాలిక యాక్సెస్ పాస్",

        "nav_system": "వ్యవస్థ & ఖాతా",
        "settings": "సెట్టింగ్‌లు",
        "help": "సహాయం & మద్దతు",
        "active_sessions": "యాక్టివ్ సెషన్‌లు",
        "welcome_tour": "స్వాగత టూర్",
        "privacy_safety": "గోప్యత & భద్రత",

        "nav_home": "హోమ్",
        "nav_patients": "రోగులు",
        "nav_predict": "అంచనా",
        "nav_telehealth": "టెలిహెల్త్",
        "nav_menu": "మెనూ",
        "nav_more": "మరిన్ని",

        "generate_prediction": "అంచనా వేయండి",
        "evaluating_risk": "రిస్క్ కారకాల మూల్యాంకనం జరుగుతోంది...",
        "view_assessment": "మూల్యాంకనం చూడండి",
        "view_profile": "ప్రొఫైల్ చూడండి",
        "export_report": "నివేదికను ఎగుమతి చేయండి",
        "save_assessment": "మూల్యాంకనం సేవ్ చేయండి",
        "apply_filters": "ఫిల్టర్‌లను వర్తింపజేయండి",
        "approve": "ఆమోదించండి",
        "reject": "తిరస్కరించండి",
        "override": "ఓవర్‌రైడ్ చేయండి",
        "modify": "సవరించండి",
        "view_simulation": "సిమ్యులేషన్ చూడండి",
        "human_review_required": "వైద్యుల సమీక్ష అవసరం",
        "simulation_result": "సిమ్యులేషన్ ఫలితం",
        "rl_workflow_rec": "RL సిఫార్సు",
        "verify_identity": "గుర్తింపును ధృవీకరించండి",
        "forgot_password": "పాస్‌వర్డ్ మర్చిపోయారా?",
        "start_prediction": "అంచనా ప్రారంభించండి",
        "explore_dashboard": "డ్యాష్‌బోర్డ్ చూడండి",
        "save_to_ehr": "EHR లో సేవ్ చేయండి",
        "end_call": "కాల్ ముగించండి",
        "join_call": "సంప్రదింపులలో చేరండి",
        "confirm": "నిర్ధారించండి",
        "cancel": "రద్దు చేయండి",
        "download_pdf": "PDF డౌన్‌లోడ్ చేయండి",
        "print_prescription": "ప్రిస్క్రిప్షన్ ప్రింట్ చేయండి",
        "talk_to_doctor": "AI డాక్టర్‌తో మాట్లాడండి (వాయిస్)",
        "listening": "వింటోంది... మాట్లాడండి",
        "generate_rx": "ప్రిస్క్రిప్షన్ సృష్టించండి",
        "ai_summarize": "AI సారాంశం",
        "translate_notes": "నోట్స్ అనువదించండి",
        "issue_certificate": "సర్టిఫికేట్ జారీ చేయండి",
        "emergency_sos": "అత్యవసర SOS",

        "ai_doctor_copilot": "CareAI క్లినికల్ కోపైలట్",
        "ai_doctor_name": "డా. CareAI",
        "consultation_title": "AI డాక్టర్ లైవ్ వీడియో సంప్రదింపులు",
        "device_check": "పరికరం సంసిద్ధత తనిఖీ",
        "camera_ready": "కెమెరా: సిద్ధంగా ఉంది",
        "mic_ready": "మైక్రోఫోన్: సిద్ధంగా ఉంది",
        "network_excellent": "నెట్‌వర్క్: అద్భుతం (32ms)",
        "view_ai_doctor": "AI డాక్టర్ వీక్షణ",
        "view_patient": "రోగి సిమ్యులేషన్",
        "view_split": "విభజిత టెలిమెట్రీ వీక్షణ",
        "live_ecg": "లైవ్ ECG & వైటల్స్",
        "heart_rate": "గుండె వేగం",
        "blood_pressure": "రక్తపోటు",
        "oxygen_sat": "ఆక్సిజన్ స్థాయి",
        "resp_rate": "శ్వాస రేటు",
        "temperature": "ఉష్ణోగ్రత",
        "live_captions": "లైవ్ ఉపశీర్షికలు",
        "ai_clinical_insight": "AI క్లినికల్ అంతర్దృష్టి",
        "readmission_risk": "రీఅడ్మిషన్ రిస్క్",
        "ppo_rl_pathway": "PPO RL సంరక్షణ మార్గం",
        "ask_ai_placeholder": "ప్రశ్న అడగండి లేదా మాట్లాడండి...",
        "ehr_clinical_notes": "క్లినికల్ నోట్స్ (EHR)",
        "rx_modal_title": "అధికారిక వైద్య ప్రిస్క్రిప్షన్",

        "high_risk": "అధిక ప్రమాదం",
        "moderate_risk": "మధ్యస్థ ప్రమాదం",
        "low_risk": "తక్కువ ప్రమాదం",
        "reviewed": "సమీక్షించబడింది",
        "pending": "పెండింగ్‌లో ఉంది",
        "actioned": "చర్య తీసుకోబడింది",
        "active": "సక్రియంగా ఉంది",
        "completed": "పూర్తయింది",
        "live_encrypted": "లైవ్ · గుప్తీకరించబడింది",
        "male": "పురుషుడు",
        "female": "స్త్రీ",
        "other": "ఇతర",

        "total_screened": "మొత్తం రోగులు",
        "avg_risk_score": "సగటు రిస్క్ స్కోర్",
        "active_patients": "ప్రస్తుత ఇన్‌పేషెంట్లు",
        "accuracy": "ఖచ్చితత్వం",
        "precision": "ఖచ్చితత్వ రేటు",
        "recall": "గుర్తుచేసుకోవడం",
        "f1_score": "F1 స్కోర్",
        "roc_auc": "ROC-AUC",
        "cardiology": "కార్డియాలజీ",
        "general_medicine": "జనరల్ మెడిసిన్",
        "endocrinology": "ఎండోక్రినాలజీ",
        "pulmonology": "పల్మోనాలజీ",
        "nephrology": "నెఫ్రాలజీ"
    },

    bn: {
        "brand_name": "এইচআরপি ক্লিনিক্যাল",
        "brand_subtitle": "নির্ভুল যত্ন ও এআই",
        "hospital_suite": "হেলথকেয়ার স্যুট",
        "header_title": "হাসপাতাল রিঅ্যাডমিশন ঝুঁকি পূর্বাভাস",
        "search_placeholder": "রোগী, ডাক্তার বা রেকর্ড খুঁজুন...",
        "search_mobile_placeholder": "রোগী, নথি খুঁজুন...",
        "dr_name": "ডা. রঞ্জিত কুমার, এমডি",
        "dr_title": "প্রধান এআই স্থপতি",
        "doctor_id": "ডাক্তার ডিজিটাল আইডি",
        "edit_profile": "প্রোফাইল সম্পাদনা করুন",
        "account_settings": "অ্যাকাউন্ট ও সেটিংস",
        "master_ebook": "মাস্টার ই-বুক (৮৮ অধ্যায়)",
        "logout": "লগ আউট",
        "sign_out_lock": "লগ আউট / সেশন লক করুন",
        "sign_out_switch": "লগ আউট / ভূমিকা পরিবর্তন করুন",
        "offline_banner": "অফলাইন মোড সক্রিয় — লাইভ এআই ও ভিডিও কল স্থগিত।",
        "reconnect": "পুনরায় সংযোগ করুন",
        "read_aloud": "পৃষ্ঠাটি পড়ে শুনুন (TTS)",
        "notifications": "বিজ্ঞপ্তি",
        "language": "ভাষা",

        "nav_clinical_care": "ক্লিনিক্যাল যত্ন",
        "dashboard": "ড্যাশবোর্ড",
        "new_prediction": "নতুন পূর্বাভাস",
        "patients": "রোগীদের তালিকা",
        "prediction_history": "পূর্বাভাস ইতিহাস",
        "analytics": "ক্লিনিক্যাল বিশ্লেষণ",
        "model_insights": "মডেল অন্তর্দৃষ্টি",

        "nav_medical_docs": "চিকিৎসা সংক্রান্ত নথি",
        "medical_documents": "চিকিৎসা সংক্রান্ত নথি",
        "my_documents": "আমার নথি",
        "lab_reports": "ল্যাব রিপোর্ট বিশ্লেষণ",
        "medical_certificates": "মেডিকেল সার্টিফিকেট",
        "verify_certificate": "সার্টিফিকেট যাচাই",
        "prescriptions": "প্রেসক্রিপশন",
        "discharge_summaries": "ডিসচার্জ সারসংক্ষেপ",

        "nav_ai_ml": "এআই ও মেশিন লার্নিং",
        "ai_and_ml": "এআই ও মেশিন লার্নিং",
        "ml_dashboard": "এমএল ড্যাশবোর্ড",
        "dataset_workspace": "ডেটাবেস ওয়ার্কস্পেস",
        "preprocessing": "ডেটা প্রিপ্রসেসিং",
        "model_training": "প্রশিক্ষণ স্টুডিও",
        "deep_learning_lab": "ডিপ লার্নিং ল্যাব",
        "model_comparison": "মডেল তুলনা",
        "explainable_ai": "ব্যাখ্যামূলক এআই (SHAP)",
        "patient_embeddings": "রোগীর এআই উপস্থাপনা (2D)",
        "ensemble_uncertainty": "এনসেম্বল ও অনিশ্চয়তা",
        "model_monitoring": "মডেল ড্রিফ্ট পর্যবেক্ষণ",
        "model_registry": "মডেল রেজিস্ট্রি",
        "experiment_tracking": "পরীক্ষা ট্র্যাকিং",
        "ask_the_model": "মডেলকে জিজ্ঞাসা করুন",

        "nav_rl": "রিইনফোর্সমেন্ট লার্নিং (RL)",
        "reinforcement_learning": "রিইনফোর্সমেন্ট লার্নিং (RL)",
        "rl_dashboard": "आरএল ড্যাশবোর্ড",
        "patient_environment": "রোগীর পরিবেশ",
        "care_pathway_opt": "যত্ন পথ অপ্টিমাইজার",
        "digital_twin_sim": "ডিজিটাল টুইন সিমুলেশন",
        "safety_constraints": "সুরক্ষা সীমাবদ্ধতা",
        "human_review": "চিকিৎসকের পর্যালোচনা",
        "stack_architecture": "৮-স্তরীয় এআই কাঠামো",

        "nav_portals": "পোর্টাল ও টেলিহেলথ",
        "video_consultation": "CareAI ভিডিও পরামর্শ",
        "patient_portal": "রোগীর পোর্টাল",
        "care_coordinator": "কেয়ার সমন্বয়ক",
        "user_management": "ব্যবহারকারী ব্যবস্থাপনা",
        "doctor_verification": "ডাক্তার যাচাইকরণ",
        "security_audit_logs": "নিরাপত্তা অডিট লগ",

        "nav_health_id": "স্বাস্থ্য আইডি ও পাস",
        "my_health_id": "আমার স্বাস্থ্য আইডি",
        "doctor_id_card": "ডাক্তার আইডি কার্ড",
        "digital_wallet": "ডিজিটাল ওয়ালেট",
        "scan_qr_code": "QR কোড স্ক্যান করুন",
        "temporary_share": "অস্থায়ী শেয়ার পাস",

        "nav_system": "সিস্টেম ও অ্যাকাউন্ট",
        "settings": "সেটিংস",
        "help": "সহায়তা ও সমর্থন",
        "active_sessions": "সক্রিয় সেশন",
        "welcome_tour": "স্বাগত সফর",
        "privacy_safety": "গোপনীয়তা ও নিরাপত্তা",

        "nav_home": "হোম",
        "nav_patients": "রোগী",
        "nav_predict": "পূর্বাভাস",
        "nav_telehealth": "টেলিহেলথ",
        "nav_menu": "মেনু",
        "nav_more": "আরও",

        "generate_prediction": "পূর্বাভাস তৈরি করুন",
        "evaluating_risk": "ঝুঁকি মূল্যায়ন করা হচ্ছে...",
        "view_assessment": "মূল্যায়ন দেখুন",
        "view_profile": "প্রোফাইল দেখুন",
        "export_report": "রিপোর্ট এক্সপোর্ট করুন",
        "save_assessment": "মূল্যায়ন সংরক্ষণ করুন",
        "apply_filters": "ফিল্টার প্রয়োগ করুন",
        "approve": "অনুমোদন করুন",
        "reject": "প্রত্যাখ্যান করুন",
        "override": "ওভাররাইড করুন",
        "modify": "পরিবর্তন করুন",
        "view_simulation": "সিমুলেশন দেখুন",
        "human_review_required": "চিকিৎসকের পর্যালোচনা প্রয়োজন",
        "simulation_result": "সিমুলেশন ফলাফল",
        "rl_workflow_rec": "RL সুপারিশ",
        "verify_identity": "পরিচয় যাচাই করুন",
        "forgot_password": "পাসওয়ার্ড ভুলে গেছেন?",
        "start_prediction": "পূর্বাভাস শুরু করুন",
        "explore_dashboard": "ড্যাশবোর্ড অন্বেষণ করুন",
        "save_to_ehr": "EHR-এ সংরক্ষণ করুন",
        "end_call": "কল শেষ করুন",
        "join_call": "পরামর্শে যোগ দিন",
        "confirm": "নিশ্চিত করুন",
        "cancel": "বাতিল করুন",
        "download_pdf": "PDF ডাউনলোড করুন",
        "print_prescription": "প্রেসক্রিপশন প্রিন্ট করুন",
        "talk_to_doctor": "এআই ডাক্তারের সাথে কথা বলুন (ভয়েস)",
        "listening": "শুনছি... এখন বলুন",
        "generate_rx": "প্রেসক্রিপশন তৈরি করুন",
        "ai_summarize": "এআই সারসংক্ষেপ",
        "translate_notes": "নোট অনুবাদ করুন",
        "issue_certificate": "সার্টিফিকেট প্রদান করুন",
        "emergency_sos": "জরুরি এসওএস",

        "ai_doctor_copilot": "CareAI ক্লিনিক্যাল কোপাইলট",
        "ai_doctor_name": "ডা. CareAI",
        "consultation_title": "এআই ডাক্তার লাইভ ভিডিও পরামর্শ",
        "device_check": "ডিভাইস প্রস্তুতি পরীক্ষা",
        "camera_ready": "ক্যামেরা: প্রস্তুত",
        "mic_ready": "মাইক্রোফোন: প্রস্তুত",
        "network_excellent": "নেটওয়ার্ক: চমৎকার (32ms)",
        "view_ai_doctor": "এআই ডাক্তার দৃশ্য",
        "view_patient": "রোগী সিমুলেশন",
        "view_split": "বিভক্ত টেলিমেট্রি দৃশ্য",
        "live_ecg": "লাইভ ইসিজি ও ভাইটালস",
        "heart_rate": "হৃদস্পন্দন",
        "blood_pressure": "রক্তচাপ",
        "oxygen_sat": "অক্সিজেন মাত্রা",
        "resp_rate": "শ্বাসপ্রশ্বাসের হার",
        "temperature": "তাপমাত্রা",
        "live_captions": "লাইভ সাবটাইটেল",
        "ai_clinical_insight": "এআই ক্লিনিক্যাল অন্তর্দৃষ্টি",
        "readmission_risk": "রিঅ্যাডমিশন ঝুঁকি",
        "ppo_rl_pathway": "PPO RL যত্ন পথ",
        "ask_ai_placeholder": "প্রশ্ন জিজ্ঞাসা করুন বা কথা বলুন...",
        "ehr_clinical_notes": "ক্লিনিক্যাল নোটস (EHR)",
        "rx_modal_title": "অফিসিয়াল মেডিকেল প্রেসক্রিপশন",

        "high_risk": "উচ্চ ঝুঁকি",
        "moderate_risk": "মাঝারি ঝুঁকি",
        "low_risk": "কম ঝুঁকি",
        "reviewed": "পর্যালোচিত",
        "pending": "মুলতুবি",
        "actioned": "পদক্ষেপ নেওয়া হয়েছে",
        "active": "সক্রিয়",
        "completed": "সম্পন্ন",
        "live_encrypted": "লাইভ · এনক্রিপ্ট করা",
        "male": "পুরুষ",
        "female": "মহিলা",
        "other": "অন্যান্য",

        "total_screened": "মোট মূল্যায়নকৃত রোগী",
        "avg_risk_score": "গড় ঝুঁকি স্কোর",
        "active_patients": "বর্তমান অন্তর্বিভাগ রোগী",
        "accuracy": "নির্ভুলতা",
        "precision": "যথার্থতা",
        "recall": "স্মরণক্ষমতা",
        "f1_score": "F1 স্কোর",
        "roc_auc": "ROC-AUC",
        "cardiology": "কার্ডিওলজি",
        "general_medicine": "জেনারেল মেডিসিন",
        "endocrinology": "এন্ডোক্রিনোলজি",
        "pulmonology": "পালমোনোলজি",
        "nephrology": "নেফ্রোলজি"
    }
};

/**
 * Clinical Dictionary for Auto-Translation of untagged text nodes & badges (7 Languages)
 */
const CLINICAL_AUTO_MAP = {
    "High Risk": { en: "High Risk", hi: "उच्च जोखिम", ta: "அதிக ஆபத்து", kn: "ಹೆಚ್ಚಿನ ಅಪಾಯ", ml: "ഉയർന്ന അപകടസാധ്യത", te: "అధిక ప్రమాదం", bn: "উচ্চ ঝুঁকি" },
    "Moderate Risk": { en: "Moderate Risk", hi: "मध्यम जोखिम", ta: "நடுத்தர ஆபத்து", kn: "ಮಧ್ಯಮ ಅಪಾಯ", ml: "ഇടത്തരം അപകടസാധ്യത", te: "మధ్యస్థ ప్రమాదం", bn: "মাঝারি ঝুঁকি" },
    "Low Risk": { en: "Low Risk", hi: "कम जोखिम", ta: "குறைந்த ஆபத்து", kn: "ಕಡಿಮೆ ಅಪಾಯ", ml: "കുറഞ്ഞ അപകടസാധ്യത", te: "తక్కువ ప్రమాదం", bn: "কম ঝুঁকি" },
    "Reviewed": { en: "Reviewed", hi: "समीक्षित", ta: "மதிப்பாய்வு செய்யப்பட்டது", kn: "ಪರಿಶೀಲಿಸಲಾಗಿದೆ", ml: "അവലോകനം ചെയ്തു", te: "సమీక్షించబడింది", bn: "পর্যালোচিত" },
    "Pending": { en: "Pending", hi: "लंबित", ta: "நிலುவையில் உள்ளது", kn: "ಬಾಕಿ ಉಳಿದಿದೆ", ml: "തീർപ്പുകಲ್പ്പിക്കാത്തത്", te: "పెండింగ్‌లో ఉంది", bn: "মুলতুবি" },
    "Actioned": { en: "Actioned", hi: "कार्रवाई की गई", ta: "நடவடிக்கை எடுக்கப்பட்டது", kn: "ಕ್ರಮ ಕೈಗೊಳ್ಳಲಾಗಿದೆ", ml: "നടപടി സ്വീകരിച്ചു", te: "చర్య తీసుకోబడింది", bn: "পদক্ষেপ নেওয়া হয়েছে" },
    "Male": { en: "Male", hi: "पुरुष", ta: "ஆண்", kn: "ಪುರುಷ", ml: "പുരുഷൻ", te: "పురుషుడు", bn: "পুরুষ" },
    "Female": { en: "Female", hi: "महिला", ta: "பெண்", kn: "ಮಹಿಳೆ", ml: "സ്ത്രീ", te: "స్త్రీ", bn: "মহিলা" },
    "Cardiology": { en: "Cardiology", hi: "हृदय रोग विभाग", ta: "இதயவியல்", kn: "ಹೃದ್ರೋಗ ಶಾಸ್ತ್ರ", ml: "ഹൃദ്രോഗ വിഭാഗം", te: "కార్డియాలజీ", bn: "কার্ডিওলজি" },
    "General Medicine": { en: "General Medicine", hi: "सामान्य चिकित्सा", ta: "பொது மருத்துவம்", kn: "ಸಾಮಾನ್ಯ ಔಷಧ", ml: "ജനറൽ മെഡിസിൻ", te: "జనరల్ మెడిసిన్", bn: "জেনারেল মেডিসিন" },
    "Endocrinology": { en: "Endocrinology", hi: "एंडोक्रिनोलॉजी", ta: "நாளமில்லா சுரப்பி", kn: "ಎಂಡೋಕ್ರೈನಾಲಜಿ", ml: "എൻഡോക്രൈനോളജി", te: "ఎండోక్రినాలజీ", bn: "এন্ডোক্রিনোলজি" },
    "Pulmonology": { en: "Pulmonology", hi: "श्वसन रोग", ta: "நுரையீரல் துறை", kn: "ಶ್ವಾಸಕೋಶ ಶಾಸ್ತ್ರ", ml: "ശ്വാസകോശ വിഭാഗം", te: "పల్మోనాలజీ", bn: "পালমোনোলজি" },
    "Nephrology": { en: "Nephrology", hi: "गुर्दा रोग विभाग", ta: "சிறுநீரகவியல்", kn: "ಮೂತ್ರಪಿಂಡ ಶಾಸ್ತ್ರ", ml: "വൃക്കരോഗ വിഭാഗം", te: "నెఫ్రాలజీ", bn: "নেফ্রোলজি" },
    "Dashboard": { en: "Dashboard", hi: "डैशबोर्ड", ta: "டாஷ்போர்டு", kn: "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", ml: "ഡാഷ്‌ബോർഡ്", te: "డ్యాష్‌బోర్డ్", bn: "ড্যাশবোর্ড" },
    "New Prediction": { en: "New Prediction", hi: "नया पूर्वानुमान", ta: "புதிய கணிப்பு", kn: "ಹೊಸ ಮುನ್ಸೂಚನೆ", ml: "പുതിയ ಪ್ರವಚನ", te: "కొత్త అంచనా", bn: "নতুন পূর্বাভাস" },
    "Patients": { en: "Patients", hi: "मरीज", ta: "நோயாளிகள்", kn: "ರೋಗಿಗಳು", ml: "രോഗികൾ", te: "రోగులు", bn: "রোগী" },
    "Prediction History": { en: "Prediction History", hi: "पूर्वानुमान इतिहास", ta: "கணிப்பு வரலாறு", kn: "ಮುನ್ಸೂಚನೆ ಇತಿಹಾಸ", ml: "പ്രവചന ചരിത്രം", te: "అంచనా చరిత్ర", bn: "পূর্বাভাস ইতিহাস" },
    "Analytics": { en: "Clinical Analytics", hi: "क्लिनिकल विश्लेषण", ta: "சிகிச்சை பகுப்பாய்வு", kn: "ಕ್ಲಿನಿಕಲ್ ವಿಶ್ಲೇಷಣೆ", ml: "ക്ലിനിക്കൽ വിശകലനം", te: "క్లినికల్ విశ్లేషణ", bn: "ক্লিনিক্যাল বিশ্লেষণ" },
    "Settings": { en: "Settings", hi: "सेटिंग्स", ta: "அமைப்புகள்", kn: "ಸೆಟ್ಟಿಂಗ್‌ಗಳು", ml: "ക്രമീകരണങ്ങൾ", te: "సెట్టింగ్‌లు", bn: "সেটিংস" },
    "Help & Support": { en: "Help & Support", hi: "सहायता एवं मार्गदर्शन", ta: "உதவி & ஆதரவு", kn: "ಸಹಾಯ & ಬೆಂಬಲ", ml: "സഹായവും പിന്തുണയും", te: "సహాయం & మద్దతు", bn: "সহায়তা ও সমর্থন" }
};

const SUPPORTED_LANGS = ['en', 'hi', 'ta', 'kn', 'ml', 'te', 'bn'];
const LANG_LABELS = {
    en: 'English',
    hi: 'हिन्दी (Hindi)',
    ta: 'தமிழ் (Tamil)',
    kn: 'ಕನ್ನಡ (Kannada)',
    ml: 'മലയാളം (Malayalam)',
    te: 'తెలుగు (Telugu)',
    bn: 'বাংলা (Bengali)'
};

const SHORT_CODES = {
    en: 'EN',
    hi: 'हिन्दी',
    ta: 'தமிழ்',
    kn: 'ಕನ್ನಡ',
    ml: 'മലയാളം',
    te: 'తెలుగు',
    bn: 'বাংলা'
};

class I18nEngine {
    constructor() {
        this.currentLang = this.getSavedLanguage();
        this.observer = null;
        this.phraseMap = null;
    }

    getSavedLanguage() {
        const match = document.cookie.match(/(?:^|;\s*)hrp_lang=([^;]*)/);
        if (match && SUPPORTED_LANGS.includes(match[1])) {
            return match[1];
        }
        const stored = localStorage.getItem('hrp_lang');
        return SUPPORTED_LANGS.includes(stored) ? stored : 'en';
    }

    getPhraseMap() {
        if (this.phraseMap) return this.phraseMap;
        const map = new Map();

        // 1. Index CLINICAL_AUTO_MAP
        if (typeof CLINICAL_AUTO_MAP !== 'undefined') {
            for (const [key, langMap] of Object.entries(CLINICAL_AUTO_MAP)) {
                map.set(key.toLowerCase().trim(), langMap);
                for (const [, val] of Object.entries(langMap)) {
                    if (val) map.set(val.toLowerCase().trim(), langMap);
                }
            }
        }

        // 2. Index all translation keys from translations object
        const enDict = translations['en'] || {};
        for (const [k, enVal] of Object.entries(enDict)) {
            if (typeof enVal === 'string' && enVal.trim()) {
                const norm = enVal.toLowerCase().trim();
                const phraseLangs = {};
                for (const l of SUPPORTED_LANGS) {
                    phraseLangs[l] = translations[l]?.[k] || translations['en']?.[k] || enVal;
                }
                map.set(norm, phraseLangs);
                map.set(k.toLowerCase().trim(), phraseLangs);
            }
        }

        this.phraseMap = map;
        return map;
    }

    init() {
        this.getPhraseMap();
        this.applyLanguage(this.currentLang, false);
        this.initMutationObserver();
    }

    setLanguage(lang, showNotification = true) {
        if (!SUPPORTED_LANGS.includes(lang)) lang = 'en';
        this.currentLang = lang;

        localStorage.setItem('hrp_lang', lang);
        document.cookie = `hrp_lang=${lang};path=/;max-age=31536000;SameSite=Lax`;

        this.applyLanguage(lang, showNotification);
        
        fetch('/api/i18n/set-language', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ lang })
        }).catch(() => {});

        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }

    toggle() {
        const idx = SUPPORTED_LANGS.indexOf(this.currentLang);
        const next = SUPPORTED_LANGS[(idx + 1) % SUPPORTED_LANGS.length];
        this.setLanguage(next, true);
    }

    t(key) {
        return translations[this.currentLang]?.[key] || translations['en']?.[key] || key;
    }

    applyLanguage(lang, notify = false) {
        document.documentElement.lang = lang;
        const dict = translations[lang] || translations['en'];
        const phraseMap = this.getPhraseMap();

        // 1. Direct [data-i18n] Tags
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    if (el.placeholder) el.placeholder = dict[key];
                } else {
                    el.textContent = dict[key];
                }
            }
        });

        // 2. Direct [data-i18n-placeholder]
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) el.placeholder = dict[key];
        });

        // 3. Topbar indicator text
        document.querySelectorAll('.lang-indicator-text').forEach(el => {
            el.textContent = SHORT_CODES[lang] || 'English';
        });

        // 4. Dropdown checkmarks & active states
        document.querySelectorAll('[data-lang-check]').forEach(el => {
            const target = el.getAttribute('data-lang-check');
            el.classList.toggle('hidden', target !== lang);
        });
        document.querySelectorAll('[data-lang-select]').forEach(btn => {
            const target = btn.getAttribute('data-lang-select');
            if (target === lang) {
                btn.classList.add('bg-primary/10', 'text-primary', 'font-bold');
                btn.classList.remove('text-secondary', 'text-slate-800');
            } else {
                btn.classList.remove('bg-primary/10', 'text-primary', 'font-bold');
                btn.classList.add('text-slate-800');
            }
        });

        // 5. Universal End-to-End DOM Text Translation
        this.universalTranslateDOM(lang, phraseMap);

        if (notify) {
            window.soundEngine?.click();
            const msg = `🌐 Language Switched: ${LANG_LABELS[lang] || lang}`;
            if (typeof window.showToast === 'function') {
                window.showToast(msg, 'info');
            }
        }
    }

    universalTranslateDOM(lang, phraseMap) {
        const selectors = 'h1, h2, h3, h4, h5, h6, button, a, span, p, label, td, th, li, dt, dd, option, .btn, .badge, .chip, [class*="risk-badge"]';
        
        document.querySelectorAll(selectors).forEach(el => {
            // Ignore icons or dropdown menu items to preserve layouts
            if (el.classList.contains('material-symbols-outlined') || el.closest('#lang-dropdown-menu')) return;

            // Only translate leaf nodes (elements with direct text and no inner markup trees)
            if (el.children.length === 0 && el.textContent) {
                const currentText = el.textContent.trim();
                if (!currentText || currentText.length > 250 || /^[0-9\s.,%:+/-]+$/.test(currentText)) return;

                // Stash initial English text
                if (!el.hasAttribute('data-orig-text')) {
                    el.setAttribute('data-orig-text', currentText);
                }

                const origText = el.getAttribute('data-orig-text');
                const normOrig = origText.toLowerCase().trim();
                const normCurrent = currentText.toLowerCase().trim();

                const entry = phraseMap.get(normOrig) || phraseMap.get(normCurrent);

                if (entry) {
                    const translated = entry[lang] || entry['en'];
                    if (translated && el.textContent !== translated) {
                        el.textContent = translated;
                    }
                } else if (lang === 'en' && origText) {
                    el.textContent = origText;
                }
            } else if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                if (el.placeholder) {
                    if (!el.hasAttribute('data-orig-placeholder')) {
                        el.setAttribute('data-orig-placeholder', el.placeholder);
                    }
                    const origPh = el.getAttribute('data-orig-placeholder');
                    const entry = phraseMap.get(origPh.toLowerCase().trim());
                    if (entry) {
                        el.placeholder = entry[lang] || entry['en'] || origPh;
                    }
                }
            }
        });
    }

    initMutationObserver() {
        if (this.observer) return;
        this.observer = new MutationObserver((mutations) => {
            let hasNewNodes = false;
            for (const mutation of mutations) {
                if (mutation.addedNodes.length > 0) {
                    hasNewNodes = true;
                    break;
                }
            }
            if (hasNewNodes && this.currentLang !== 'en') {
                this.applyLanguage(this.currentLang, false);
            }
        });
        this.observer.observe(document.body, { childList: true, subtree: true });
    }

    speak(text, lang = null) {
        if (!('speechSynthesis' in window)) return null;
        window.speechSynthesis.cancel();

        const targetLang = lang || this.currentLang;
        const localeMap = {
            en: 'en-US',
            hi: 'hi-IN',
            ta: 'ta-IN',
            kn: 'kn-IN',
            ml: 'ml-IN',
            te: 'te-IN',
            bn: 'bn-IN'
        };
        const targetLocale = localeMap[targetLang] || 'en-US';

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = targetLocale;
        utterance.rate = targetLang === 'en' ? 1.0 : 0.92;
        utterance.pitch = 1.0;

        const voices = window.speechSynthesis.getVoices();
        const matchingVoice = voices.find(v => v.lang.startsWith(targetLang) || v.lang === targetLocale);
        if (matchingVoice) utterance.voice = matchingVoice;

        window.speechSynthesis.speak(utterance);
        return utterance;
    }
}

// Global instance
window.i18n = new I18nEngine();
document.addEventListener('DOMContentLoaded', () => {
    window.i18n.init();
});
