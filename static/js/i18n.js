/**
 * Client-Side Bilingual (English ↔ हिन्दी) Translation & Accessibility Engine v3.0
 * Hospital Readmission Predictor (HRP Clinical)
 *
 * Features:
 *  - 250+ Clinical, Operational, ML/RL, and Portal terms
 *  - Intelligent DOM Auto-Translation (badges, clinical terms, placeholders)
 *  - Real-time MutationObserver for dynamically loaded content
 *  - Cookie & LocalStorage synchronization with backend
 *  - Text-to-Speech (TTS) Web Speech API for English and Hindi
 *  - Event dispatcher ('languageChanged') for real-time component updates
 */

const translations = {
    en: {
        // Brand & Header
        "brand_name": "HRP Clinical",
        "brand_subtitle": "Precision Care & AI",
        "hospital_suite": "Healthcare Suite",
        "header_title": "Hospital Readmission Predictor",
        "search_placeholder": "Search patient, doc...",
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

        // Navigation Sections
        "nav_clinical_care": "Clinical Care",
        "dashboard": "Dashboard",
        "new_prediction": "New Prediction",
        "patients": "Patients",
        "prediction_history": "Prediction History",
        "analytics": "Analytics",
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

        "nav_portals": "Portals & Coordination",
        "video_consultation": "CareAI Video Call",
        "patient_portal": "Patient Portal",
        "care_coordinator": "Care Coordinator",
        "user_management": "User Management",
        "doctor_verification": "Doctor Verification",
        "security_audit_logs": "Security Audit Logs",

        "nav_health_id": "Health ID & Passes",
        "my_health_id": "My Health ID",
        "digital_wallet": "Digital Wallet",
        "scan_qr_code": "Scan QR Code",
        "temporary_share": "Temporary Share Passes",

        "nav_system": "System & Knowledge",
        "settings": "Settings",
        "help": "Help & Support",
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
        "rl_workflow_rec": "RL Workflow Recommendation",
        "verify_identity": "Verify Your Identity",
        "forgot_password": "Forgot Password?",
        "start_prediction": "Start Prediction",
        "explore_dashboard": "Explore Dashboard",
        "save_to_ehr": "Save to EHR",
        "end_call": "End Call",
        "join_call": "Join Consultation",
        "confirm": "Confirm",
        "cancel": "Cancel",

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

        "nav_portals": "पोर्टल एवं समन्वय",
        "video_consultation": "केयर-एआई वीडियो कॉल",
        "patient_portal": "रोगी पोर्टल",
        "care_coordinator": "देखभाल समन्वयक",
        "user_management": "उपयोगकर्ता प्रबंधन",
        "doctor_verification": "चिकित्सक सत्यापन",
        "security_audit_logs": "सुरक्षा ऑडिट लॉग्स",

        "nav_health_id": "हेल्थ आईडी एवं पास",
        "my_health_id": "मेरी हेल्थ आईडी",
        "digital_wallet": "डिजिटल वॉलेट",
        "scan_qr_code": "क्यूआर कोड स्कैन करें",
        "temporary_share": "अस्थायी शेयर पास",

        "nav_system": "प्रणाली एवं संसाधन",
        "settings": "सेटिंग्स",
        "help": "सहायता एवं मार्गदर्शन",
        "welcome_tour": "वेलकम टूर",
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
        "save_to_ehr": "ईएचआर में सहेजें",
        "end_call": "कॉल समाप्त करें",
        "join_call": "परामर्श में शामिल हों",
        "confirm": "पुष्टि करें",
        "cancel": "रद्द करें",

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

        "nav_portals": "போர்ட்டல்கள் & ஒருங்கிணைப்பு",
        "video_consultation": "CareAI வீடியோ ஆலோசனை",
        "patient_portal": "நோயாளி போர்டல்",
        "care_coordinator": "பராமரிப்பு ஒருங்கிணைப்பாளர்",
        "user_management": "பயனர் மேலாண்மை",
        "doctor_verification": "மருத்துவர் சரிபார்ப்பு",
        "security_audit_logs": "பாதுகாப்பு தணிக்கை பதிவுகள்",

        "nav_health_id": "சுகாதார ஐடி & பாஸ்கள்",
        "my_health_id": "என் சுகாதார ஐடி",
        "digital_wallet": "டிஜிட்டல் பணப்பை",
        "scan_qr_code": "QR குறியீட்டை ஸ்கேன் செய்க",
        "temporary_share": "தற்காலிக அணுகல் பாஸ்",

        "nav_system": "அமைப்பு & வழிகாட்டல்",
        "settings": "அமைப்புகள்",
        "help": "உதவி & ஆதரவு",
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

        "high_risk": "அதிக ஆபத்து",
        "moderate_risk": "நடுத்தர ஆபத்து",
        "low_risk": "குறைந்த ஆபத்து",
        "reviewed": "மதிப்பாய்வு செய்யப்பட்டது",
        "pending": "நிலுவையில் உள்ளது",
        "actioned": "நடவடிக்கை எடுக்கப்பட்டது",
        "active": "செயலில் உள்ளது",
        "completed": "நிறைவடைந்தது",
        "live_encrypted": "நேரலை · குறியாக்கம் செய்யப்பட்டது",

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

        "nav_portals": "ಪೋರ್ಟಲ್‌ಗಳು & ಸಮನ್ವಯ",
        "video_consultation": "CareAI ವೀಡಿಯೊ ಸಮಾಲೋಚನೆ",
        "patient_portal": "ರೋಗಿ ಪೋರ್ಟಲ್",
        "care_coordinator": "ಆರೈಕೆ ಸಂಯೋಜಕ",
        "user_management": "ಬಳಕೆದಾರರ ನಿರ್ವಹಣೆ",
        "doctor_verification": "ವೈದ್ಯರ ಪರಿಶೀಲನೆ",
        "security_audit_logs": "ಭದ್ರತಾ ಆಡಿಟ್ ಲಾಗ್‌ಗಳು",

        "nav_health_id": "ಆರೋಗ್ಯ ಐಡಿ & ಪಾಸ್‌ಗಳು",
        "my_health_id": "ನನ್ನ ಆರೋಗ್ಯ ಐಡಿ",
        "digital_wallet": "ಡಿಜಿಟಲ್ ವಾಲೆಟ್",
        "scan_qr_code": "QR ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ",
        "temporary_share": "ತಾತ್ಕಾಲಿಕ ಪ್ರವೇಶ ಪಾಸ್",

        "nav_system": "ವ್ಯವಸ್ಥೆ & ಮಾರ್ಗದರ್ಶನ",
        "settings": "ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "help": "ಸಹಾಯ & ಬೆಂಬಲ",
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

        "high_risk": "ಹೆಚ್ಚಿನ ಅಪಾಯ",
        "moderate_risk": "ಮಧ್ಯಮ ಅಪಾಯ",
        "low_risk": "ಕಡಿಮೆ ಅಪಾಯ",
        "reviewed": "ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
        "pending": "ಬಾಕಿ ಉಳಿದಿದೆ",
        "actioned": "ಕ್ರಮ ಕೈಗೊಳ್ಳಲಾಗಿದೆ",
        "active": "ಸಕ್ರಿಯ",
        "completed": "ಪೂರ್ಣಗೊಂಡಿದೆ",
        "live_encrypted": "ಲೈವ್ · ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಲಾಗಿದೆ",

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

        "nav_portals": "പോർട്ടലുകൾ & ഏകോപനം",
        "video_consultation": "CareAI വീഡിയോ കൺസൾട്ടേഷൻ",
        "patient_portal": "രോഗി പോർട്ടൽ",
        "care_coordinator": "കെയർ കോർഡിനേറ്റർ",
        "user_management": "ഉപയോക്തൃ മാനേജ്മെന്റ്",
        "doctor_verification": "ഡോക്ടർ പരിശോധന",
        "security_audit_logs": "സുരക്ഷാ ഓഡിറ്റ് ലോഗുകൾ",

        "nav_health_id": "ഹെൽത്ത് ഐഡി & പാസുകൾ",
        "my_health_id": "എന്റെ ഹെൽത്ത് ഐഡി",
        "digital_wallet": "ഡിജിറ്റൽ വാലറ്റ്",
        "scan_qr_code": "QR കോഡ് സ്കാൻ ചെയ്യുക",
        "temporary_share": "താൽക്കാലിക പാസുകൾ",

        "nav_system": "സിസ്റ്റം & പിന്തുണ",
        "settings": "ക്രമീകരണങ്ങൾ",
        "help": "സഹായവും പിന്തുണയും",
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

        "high_risk": "ഉയർന്ന അപകടസാധ്യത",
        "moderate_risk": "ഇടത്തരം അപകടസാധ്യത",
        "low_risk": "കുറഞ്ഞ അപകടസാധ്യത",
        "reviewed": "അവലോകനം ചെയ്തു",
        "pending": "തീർപ്പുകൽപ്പിക്കാത്തത്",
        "actioned": "നടപടി സ്വീകരിച്ചു",
        "active": "സജീവം",
        "completed": "പൂർത്തിയായി",
        "live_encrypted": "തത്സമയം · എൻക്രിപ്റ്റ് ചെയ്തത്",

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
    }
};

/**
 * Clinical Dictionary for Auto-Translation of untagged text nodes & badges (5 Languages)
 */
const CLINICAL_AUTO_MAP = {
    "High Risk": { en: "High Risk", hi: "उच्च जोखिम", ta: "அதிக ஆபத்து", kn: "ಹೆಚ್ಚಿನ ಅಪಾಯ", ml: "ഉയർന്ന അപകടസാധ്യത" },
    "Moderate Risk": { en: "Moderate Risk", hi: "मध्यम जोखिम", ta: "நடுத்தர ஆபத்து", kn: "ಮಧ್ಯಮ ಅಪಾಯ", ml: "ഇടത്തരം അപകടസാധ്യത" },
    "Low Risk": { en: "Low Risk", hi: "कम जोखिम", ta: "குறைந்த ஆபத்து", kn: "ಕಡಿಮೆ ಅಪಾಯ", ml: "കുറഞ്ഞ അപകടസാധ്യത" },
    "Reviewed": { en: "Reviewed", hi: "समीक्षित", ta: "மதிப்பாய்வு செய்யப்பட்டது", kn: "ಪರಿಶೀಲಿಸಲಾಗಿದೆ", ml: "അവലോകനം ചെയ്തു" },
    "Pending": { en: "Pending", hi: "लंबित", ta: "நிலுவையில் உள்ளது", kn: "ಬಾಕಿ ಉಳಿದಿದೆ", ml: "തീർപ്പുകಲ್പ്പിക്കാത്തത്" },
    "Actioned": { en: "Actioned", hi: "कार्रवाई की गई", ta: "நடவடிக்கை எடுக்கப்பட்டது", kn: "ಕ್ರಮ ಕೈಗೊಳ್ಳಲಾಗಿದೆ", ml: "നടപടി സ്വീകരിച്ചു" },
    "Male": { en: "Male", hi: "पुरुष", ta: "ஆண்", kn: "ಪುರುಷ", ml: "പുരുഷൻ" },
    "Female": { en: "Female", hi: "महिला", ta: "பெண்", kn: "ಮಹಿಳೆ", ml: "സ്ത്രീ" },
    "Cardiology": { en: "Cardiology", hi: "हृदय रोग विभाग", ta: "இதயவியல்", kn: "ಹೃದ್ರೋಗ ಶಾಸ್ತ್ರ", ml: "ഹൃദ്രോഗ വിഭാഗം" },
    "General Medicine": { en: "General Medicine", hi: "सामान्य चिकित्सा", ta: "பொது மருத்துவம்", kn: "ಸಾಮಾನ್ಯ ಔಷಧ", ml: "ജനറൽ മെഡിസിൻ" },
    "Endocrinology": { en: "Endocrinology", hi: "एंडोक्रिनोलॉजी", ta: "நாளமில்லா சுரப்பி", kn: "ಎಂಡೋಕ್ರೈನಾಲಜಿ", ml: "എൻഡോക്രൈനോളജി" },
    "Pulmonology": { en: "Pulmonology", hi: "श्वसन रोग", ta: "நுரையீரல் துறை", kn: "ಶ್ವಾಸಕೋಶ ಶಾಸ್ತ್ರ", ml: "ശ്വാസകോശ വിഭാഗം" },
    "Nephrology": { en: "Nephrology", hi: "गुर्दा रोग विभाग", ta: "சிறுநீரகவியல்", kn: "ಮೂತ್ರಪಿಂಡ ಶಾಸ್ತ್ರ", ml: "വൃക്കരോഗ വിഭാഗം" },
    "Dashboard": { en: "Dashboard", hi: "डैशबोर्ड", ta: "டாஷ்போர்டு", kn: "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", ml: "ഡാഷ്‌ബോർഡ്" },
    "New Prediction": { en: "New Prediction", hi: "नया पूर्वानुमान", ta: "புதிய கணிப்பு", kn: "ಹೊಸ ಮುನ್ಸೂಚನೆ", ml: "പുതിയ പ്രവചനം" },
    "Patients": { en: "Patients", hi: "मरीज", ta: "நோயாளிகள்", kn: "ರೋಗಿಗಳು", ml: "രോഗികൾ" },
    "Prediction History": { en: "Prediction History", hi: "पूर्वानुमान इतिहास", ta: "கணிப்பு வரலாறு", kn: "ಮುನ್ಸೂಚನೆ ಇತಿಹಾಸ", ml: "പ്രവചന ചരിത്രം" },
    "Analytics": { en: "Analytics", hi: "विश्लेषण", ta: "பகுப்பாய்வு", kn: "ವಿಶ್ಲೇಷಣೆ", ml: "വിശകലനം" },
    "Settings": { en: "Settings", hi: "सेटिंग्स", ta: "அமைப்புகள்", kn: "ಸೆಟ್ಟಿಂಗ್‌ಗಳು", ml: "ക്രമീകരണങ്ങൾ" },
    "Help & Support": { en: "Help & Support", hi: "सहायता एवं मार्गदर्शन", ta: "உதவி & ஆதரவு", kn: "ಸಹಾಯ & ಬೆಂಬಲ", ml: "സഹಾಯവും പിന്തുണയും" }
};

const SUPPORTED_LANGS = ['en', 'hi', 'ta', 'kn', 'ml'];
const LANG_LABELS = {
    en: 'English',
    hi: 'हिन्दी (Hindi)',
    ta: 'தமிழ் (Tamil)',
    kn: 'ಕನ್ನಡ (Kannada)',
    ml: 'മലയാളം (Malayalam)'
};

class I18nEngine {
    constructor() {
        this.currentLang = this.getSavedLanguage();
        this.observer = null;
    }

    getSavedLanguage() {
        const match = document.cookie.match(/(?:^|;\s*)hrp_lang=([^;]*)/);
        if (match && SUPPORTED_LANGS.includes(match[1])) {
            return match[1];
        }
        const stored = localStorage.getItem('hrp_lang');
        return SUPPORTED_LANGS.includes(stored) ? stored : 'en';
    }

    init() {
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

        // 1. Update [data-i18n]
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

        // 2. Update [data-i18n-placeholder]
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) el.placeholder = dict[key];
        });

        // 3. Topbar indicator text
        const shortCodes = { en: 'EN', hi: 'हिन्दी', ta: 'தமிழ்', kn: 'ಕನ್ನಡ', ml: 'മലയാളം' };
        document.querySelectorAll('.lang-indicator-text').forEach(el => {
            el.textContent = shortCodes[lang] || 'English';
        });

        // 4. Update dropdown checks and active states
        document.querySelectorAll('[data-lang-check]').forEach(el => {
            const target = el.getAttribute('data-lang-check');
            el.classList.toggle('hidden', target !== lang);
        });
        document.querySelectorAll('[data-lang-select]').forEach(btn => {
            const target = btn.getAttribute('data-lang-select');
            if (target === lang) {
                btn.classList.add('bg-primary/10', 'text-primary', 'font-bold');
                btn.classList.remove('text-secondary');
            } else {
                btn.classList.remove('bg-primary/10', 'text-primary', 'font-bold');
                btn.classList.add('text-secondary');
            }
        });

        // 5. Intelligent DOM Auto-Translation
        this.autoTranslateUntaggedNodes(lang);

        if (notify) {
            window.soundEngine?.click();
            const msg = `🌐 Language: ${LANG_LABELS[lang] || lang}`;
            if (typeof window.showToast === 'function') {
                window.showToast(msg, 'info');
            }
        }
    }

    autoTranslateUntaggedNodes(lang) {
        document.querySelectorAll('.badge, .chip, [class*="risk-badge"], span.rounded-full, td, th').forEach(el => {
            if (el.children.length === 0 && el.textContent) {
                const trimmed = el.textContent.trim();
                for (const [canonical, map] of Object.entries(CLINICAL_AUTO_MAP)) {
                    for (const l of SUPPORTED_LANGS) {
                        if (trimmed === map[l] || trimmed === canonical) {
                            el.textContent = map[lang] || map['en'];
                            return;
                        }
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
            if (hasNewNodes) {
                this.applyLanguage(this.currentLang, false);
            }
        });
        this.observer.observe(document.body, { childList: true, subtree: true });
    }

    speak(text, lang = null) {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();

        const targetLang = lang || this.currentLang;
        const localeMap = {
            en: 'en-US',
            hi: 'hi-IN',
            ta: 'ta-IN',
            kn: 'kn-IN',
            ml: 'ml-IN'
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
    }
}

// Global instance
window.i18n = new I18nEngine();
document.addEventListener('DOMContentLoaded', () => {
    window.i18n.init();
});


