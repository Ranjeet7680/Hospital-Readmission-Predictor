/**
 * Client-Side Bilingual (English ↔ हिन्दी) Translation Engine
 * Hospital Readmission Predictor (HRP Clinical)
 */

const translations = {
    en: {
        // Brand & Navigation
        "brand_name": "HRP Clinical",
        "brand_subtitle": "Precision Care & Intelligence",
        "dashboard": "Dashboard",
        "new_prediction": "New Prediction",
        "patients": "Patients",
        "prediction_history": "Prediction History",
        "analytics": "Analytics",
        "model_insights": "Model Insights",
        "settings": "Settings",
        "help": "Help",
        "logout": "Logout",
        "sign_in": "Sign In",
        "create_account": "Create Account",
        "get_started": "Get Started",

        // Modules
        "medical_documents": "Medical Documents",
        "my_documents": "My Documents",
        "upload_report": "Upload Report",
        "medical_certificates": "Medical Certificates",
        "prescriptions": "Prescriptions",
        "lab_reports": "Lab Reports",
        "discharge_summaries": "Discharge Summaries",
        "ai_and_ml": "AI & ML Intelligence",
        "ml_dashboard": "ML Dashboard",
        "dataset_workspace": "Dataset Workspace",
        "preprocessing": "Data Preprocessing",
        "feature_engineering": "Feature Engineering",
        "model_training": "Model Training",
        "model_comparison": "Model Comparison",
        "model_evaluation": "Model Evaluation",
        "explainable_ai": "Explainable AI (XAI)",
        "patient_embeddings": "Patient Embeddings",
        "ensemble_uncertainty": "Ensemble & Uncertainty",
        "model_monitoring": "Model Monitoring",
        "model_registry": "Model Registry",
        "experiment_tracking": "Experiment Tracking",
        "ask_the_model": "Ask the Model (AI Chat)",

        // Reinforcement Learning
        "reinforcement_learning": "Reinforcement Learning",
        "rl_dashboard": "RL Dashboard",
        "patient_environment": "Patient Environment",
        "state_representation": "State Representation",
        "action_library": "Action Library",
        "reward_design": "Reward Design",
        "agent_training": "Agent Training",
        "care_pathway_opt": "Care Pathway Optimization",
        "digital_twin_sim": "Simulation & Digital Twin",
        "safety_constraints": "Safety Constraints",
        "human_review": "Human-in-the-Loop Review",
        "policy_registry": "Policy Registry",
        "rl_monitoring": "RL Monitoring",
        "stack_architecture": "8-Layer Architecture",

        // Portals & Telemedicine
        "patient_portal": "Patient Portal",
        "doctor_portal": "Doctor Portal",
        "care_coordinator": "Care Coordinator",
        "admin_portal": "Admin Portal",
        "video_consultation": "Video Consultation",
        "user_management": "User Management",
        "doctor_verification": "Doctor Verification",
        "security_audit_logs": "Security Audit Logs",

        // Actions & Buttons
        "generate_prediction": "Generate Prediction",
        "evaluating_risk": "Evaluating Risk Factors...",
        "view_assessment": "View Assessment",
        "view_profile": "View Profile",
        "export_report": "Export Report",
        "save_assessment": "Save Assessment",
        "apply_filters": "Apply Filters",
        "approve": "Approve",
        "reject": "Reject",
        "modify": "Modify",
        "view_simulation": "View Simulation",
        "human_review_required": "Human Review Required",
        "simulation_result": "Simulation Result",
        "rl_workflow_rec": "RL Workflow Recommendation",
        "verify_identity": "Verify Your Identity",
        "forgot_password": "Forgot Password?",
        "start_prediction": "Start Prediction",
        "explore_dashboard": "Explore Dashboard",
        "high_risk": "High Risk",
        "moderate_risk": "Moderate Risk",
        "low_risk": "Low Risk",
        "reviewed": "Reviewed",
        "pending": "Pending",
        "actioned": "Actioned",
        "accuracy": "Accuracy",
        "precision": "Precision",
        "recall": "Recall",
        "f1_score": "F1-Score",
        "roc_auc": "ROC-AUC"
    },
    hi: {
        // Brand & Navigation
        "brand_name": "एचआरपी क्लिनिकल",
        "brand_subtitle": "सटीक देखभाल एवं एआई बुद्धिमत्ता",
        "dashboard": "डैशबोर्ड",
        "new_prediction": "नया जोखिम पूर्वानुमान",
        "patients": "मरीज सूची",
        "prediction_history": "पूर्वानुमान इतिहास",
        "analytics": "क्लिनिकल विश्लेषण",
        "model_insights": "मॉडल अंतर्दृष्टि",
        "settings": "सेटिंग्स",
        "help": "सहायता एवं मार्गदर्शन",
        "logout": "लॉग आउट",
        "sign_in": "साइन इन करें",
        "create_account": "खाता बनाएं",
        "get_started": "शुरू करें",

        // Modules
        "medical_documents": "चिकित्सा दस्तावेज",
        "my_documents": "मेरे दस्तावेज",
        "upload_report": "रिपोर्ट अपलोड करें",
        "medical_certificates": "मेडिकल प्रमाण पत्र",
        "prescriptions": "नुस्खे (प्रिस्क्रिप्शन)",
        "lab_reports": "लैब परीक्षण रिपोर्ट",
        "discharge_summaries": "डिस्चार्ज सारांश",
        "ai_and_ml": "एआई एवं मशीन लर्निंग",
        "ml_dashboard": "एमएल डैशबोर्ड",
        "dataset_workspace": "डेटासेट कार्यक्षेत्र",
        "preprocessing": "डेटा प्रीप्रोसेसिंग",
        "feature_engineering": "फ़ीचर इंजीनियरिंग",
        "model_training": "मॉडल प्रशिक्षण",
        "model_comparison": "मॉडल तुलना",
        "model_evaluation": "मॉडल मूल्यांकन",
        "explainable_ai": "स्पष्टीकरणीय एआई (XAI)",
        "patient_embeddings": "रोगी एआई प्रतिनिधित्व (क्लस्टर)",
        "ensemble_uncertainty": "एन्सेम्बल एवं अनिश्चितता",
        "model_monitoring": "मॉडल निगरानी (ड्रिफ्ट)",
        "model_registry": "मॉडल रजिस्ट्री",
        "experiment_tracking": "प्रयोग ट्रैकिंग",
        "ask_the_model": "मॉडल से पूछें (एआई चैट)",

        // Reinforcement Learning
        "reinforcement_learning": "सुदृढ़ीकरण अधिगम (RL)",
        "rl_dashboard": "आरएल डैशबोर्ड",
        "patient_environment": "रोगी देखभाल परिवेश",
        "state_representation": "अवस्था प्रतिनिधित्व (State)",
        "action_library": "कार्य पुस्तकालय (Actions)",
        "reward_design": "इनाम फ़ंक्शन डिज़ाइन",
        "agent_training": "एजेंट प्रशिक्षण",
        "care_pathway_opt": "देखभाल पथ अनुकूलन",
        "digital_twin_sim": "डिजिटल ट्विन सिमुलेशन",
        "safety_constraints": "सुरक्षा प्रतिबंध इंजन",
        "human_review": "मानव समीक्षा (चिकित्सक सत्यापन)",
        "policy_registry": "नीति (Policy) रजिस्ट्री",
        "rl_monitoring": "आरएल निगरानी",
        "stack_architecture": "8-स्तरीय एआई संरचना",

        // Portals & Telemedicine
        "patient_portal": "रोगी पोर्टल",
        "doctor_portal": "चिकित्सक पोर्टल",
        "care_coordinator": "देखभाल समन्वयक",
        "admin_portal": "प्रशासक पोर्टल",
        "video_consultation": "वीडियो परामर्श (Telemedicine)",
        "user_management": "उपयोगकर्ता प्रबंधन",
        "doctor_verification": "चिकित्सक सत्यापन कतार",
        "security_audit_logs": "सुरक्षा ऑडिट लॉग्स",

        // Actions & Buttons
        "generate_prediction": "जोखिम पूर्वानुमान लगाएं",
        "evaluating_risk": "जोखिम कारकों का मूल्यांकन हो रहा है...",
        "view_assessment": "मूल्यांकन देखें",
        "view_profile": "प्रोफ़ाइल देखें",
        "export_report": "रिपोर्ट निर्यात करें (PDF)",
        "save_assessment": "मूल्यांकन सहेजें",
        "apply_filters": "फ़िल्टर लागू करें",
        "approve": "स्वीकृत करें",
        "reject": "अस्वीकार करें",
        "modify": "संशोधित करें",
        "view_simulation": "सिमुलेशन देखें",
        "human_review_required": "मानव समीक्षा आवश्यक है",
        "simulation_result": "सिमुलेशन परिणाम",
        "rl_workflow_rec": "RL कार्यप्रवाह अनुशंसा",
        "verify_identity": "अपनी पहचान सत्यापित करें",
        "forgot_password": "पासवर्ड भूल गए?",
        "start_prediction": "पूर्वानुमान शुरू करें",
        "explore_dashboard": "डैशबोर्ड एक्सप्लोर करें",
        "high_risk": "उच्च जोखिम",
        "moderate_risk": "मध्यम जोखिम",
        "low_risk": "कम जोखिम",
        "reviewed": "समीक्षित",
        "pending": "लंबित",
        "actioned": "कार्रवाई की गई",
        "accuracy": "सटीकता (Accuracy)",
        "precision": "परिशुद्धता (Precision)",
        "recall": "संवेदनशीलता (Recall)",
        "f1_score": "F1 स्कोर",
        "roc_auc": "आरओसी-एयूसी (ROC-AUC)"
    }
};

class I18nEngine {
    constructor() {
        this.currentLang = localStorage.getItem('hrp_lang') || 'en';
    }

    init() {
        this.applyLanguage(this.currentLang);
    }

    setLanguage(lang) {
        if (lang !== 'en' && lang !== 'hi') lang = 'en';
        this.currentLang = lang;
        localStorage.setItem('hrp_lang', lang);
        this.applyLanguage(lang);
        window.soundEngine?.click();
    }

    toggle() {
        this.setLanguage(this.currentLang === 'en' ? 'hi' : 'en');
    }

    t(key) {
        return translations[this.currentLang]?.[key] || translations['en']?.[key] || key;
    }

    applyLanguage(lang) {
        document.documentElement.lang = lang;
        const dict = translations[lang] || translations['en'];

        // Update all data-i18n elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                if (el.tagName === 'INPUT' && el.type === 'text') {
                    el.placeholder = dict[key];
                } else {
                    el.textContent = dict[key];
                }
            }
        });

        // Update language indicator buttons
        document.querySelectorAll('.lang-indicator-text').forEach(el => {
            el.textContent = lang === 'en' ? 'English' : 'हिन्दी';
        });
    }
}

window.i18n = new I18nEngine();
document.addEventListener('DOMContentLoaded', () => {
    window.i18n.init();
});
