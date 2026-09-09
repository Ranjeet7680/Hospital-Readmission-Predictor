import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 Widescreen (13.333" x 7.5")
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Color Palette
    DARK_NAVY = RGBColor(10, 25, 47)       # #0A192F
    CARD_DARK = RGBColor(19, 34, 56)       # #132238
    PRIMARY_BLUE = RGBColor(0, 102, 255)   # #0066FF
    ACCENT_CYAN = RGBColor(0, 210, 255)    # #00D2FF
    ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981
    ACCENT_RED = RGBColor(239, 68, 68)     # #EF4444
    ACCENT_AMBER = RGBColor(245, 158, 11)  # #F59E0B
    ACCENT_PURPLE = RGBColor(139, 92, 246) # #8B5CF6
    
    BG_LIGHT = RGBColor(248, 250, 252)     # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)      # #FFFFFF
    BORDER_LIGHT = RGBColor(226, 232, 240) # #E2E8F0
    TEXT_DARK = RGBColor(15, 23, 42)       # #0F172A
    TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B
    TEXT_WHITE = RGBColor(255, 255, 255)   # #FFFFFF
    TEXT_LIGHT_BLUE = RGBColor(186, 230, 253) # #BAE6FD

    def add_slide_background(slide, is_dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = DARK_NAVY if is_dark else BG_LIGHT
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="LUMINIX'26 HACKATHON • HEALTHCARE & AI TRACK", is_dark=False):
        # Category Tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.73), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_CYAN if is_dark else PRIMARY_BLUE

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.73), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE if is_dark else TEXT_DARK

        # Top Accent Divider
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.73), Inches(0.03))
        line.fill.solid()
        line.fill.fore_color.rgb = ACCENT_CYAN if is_dark else PRIMARY_BLUE
        line.line.fill.background()

        # Footer
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.73), Inches(0.25))
        tf_footer = footer_box.text_frame
        tf_footer.margin_left = tf_footer.margin_top = tf_footer.margin_right = tf_footer.margin_bottom = 0
        p_f = tf_footer.paragraphs[0]
        p_f.text = "Hospital Readmission Predictor  |  Team Nexora (Leader: Ranjeet Kumar)  |  LUMINIX'26 Presentation"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = RGBColor(148, 163, 184) if is_dark else TEXT_MUTED

    def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_LIGHT, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
        return card

    # =========================================================================
    # SLIDE 1: TITLE HERO SLIDE (Dark Theme)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide1, is_dark=True)

    # Accent Glow Pill
    glow_pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(0.85), Inches(4.8), Inches(0.42))
    glow_pill.fill.solid()
    glow_pill.fill.fore_color.rgb = RGBColor(15, 45, 80)
    glow_pill.line.color.rgb = ACCENT_CYAN
    glow_pill.line.width = Pt(1.5)
    p_gp = glow_pill.text_frame.paragraphs[0]
    p_gp.text = "★ LUMINIX'26 HACKATHON • HEALTHCARE TRACK"
    p_gp.font.size = Pt(11)
    p_gp.font.bold = True
    p_gp.font.color.rgb = ACCENT_CYAN
    p_gp.alignment = PP_ALIGN.CENTER

    # Hero Main Title
    t_box1 = slide1.shapes.add_textbox(Inches(0.9), Inches(1.45), Inches(11.5), Inches(2.2))
    tf1 = t_box1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Hospital Readmission Predictor"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Clinical Intelligence, TreeSHAP Explainability & Closed-Loop Care Platform"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN

    p3 = tf1.add_paragraph()
    p3.text = "A multimodal healthcare ecosystem integrating XGBoost (0.9794 AUC), Deep Learning, PPO Reinforcement Learning, Multilingual Telemedicine, and 3D Digital Health ID."
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_LIGHT_BLUE

    # Metric Badges Row
    badge_data = [
        ("0.9794", "ROC-AUC (XGBoost)", PRIMARY_BLUE),
        ("101,766", "Patient Encounters", ACCENT_CYAN),
        ("47 / 47", "Tests Passing (100%)", ACCENT_GREEN),
        ("36 Lang", "Universal Telemedicine", ACCENT_PURPLE),
        ("88 Ch", "Master Clinical eBook", ACCENT_AMBER),
    ]
    for i, (num, lbl, col) in enumerate(badge_data):
        bx = Inches(0.9 + i * 2.36)
        b_card = create_card(slide1, bx, Inches(3.75), Inches(2.2), Inches(1.1), bg_color=CARD_DARK, border_color=col, border_width=1.5)
        tb_b = slide1.shapes.add_textbox(bx, Inches(3.82), Inches(2.2), Inches(0.95))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        p_num = tf_b.paragraphs[0]
        p_num.text = num
        p_num.font.size = Pt(20)
        p_num.font.bold = True
        p_num.font.color.rgb = col
        p_num.alignment = PP_ALIGN.CENTER

        p_lbl = tf_b.add_paragraph()
        p_lbl.text = lbl
        p_lbl.font.size = Pt(10)
        p_lbl.font.color.rgb = TEXT_WHITE
        p_lbl.alignment = PP_ALIGN.CENTER

    # Team & Presentation Info Footer Card
    card_info = create_card(slide1, Inches(0.9), Inches(5.1), Inches(11.53), Inches(1.8), bg_color=CARD_DARK, border_color=PRIMARY_BLUE, border_width=1.5)
    tb_info = slide1.shapes.add_textbox(Inches(1.1), Inches(5.2), Inches(11.1), Inches(1.6))
    tf_info = tb_info.text_frame
    tf_info.word_wrap = True

    p_team = tf_info.paragraphs[0]
    p_team.text = "DEVELOPED BY TEAM NEXORA"
    p_team.font.size = Pt(16)
    p_team.font.bold = True
    p_team.font.color.rgb = ACCENT_CYAN

    p_lead = tf_info.add_paragraph()
    p_lead.text = "Team Leader: Ranjeet Kumar   |   Contact: rajranjeet7680@gmail.com"
    p_lead.font.size = Pt(13)
    p_lead.font.bold = True
    p_lead.font.color.rgb = TEXT_WHITE

    p_links = tf_info.add_paragraph()
    p_links.text = "Live Deployment: https://hospital-readmission-predictor-mauve.vercel.app\nGitHub Repository: https://github.com/Ranjeet7680/Hospital-Readmission-Predictor"
    p_links.font.size = Pt(11)
    p_links.font.color.rgb = TEXT_LIGHT_BLUE

    # =========================================================================
    # SLIDE 2: THE PROBLEM STATEMENT
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide2)
    add_header(slide2, "1. Problem Statement: The $26B+ Hospital Readmission Crisis")

    cards_p2 = [
        ("The Financial Burden", "$26+ Billion / Year", "In the US alone, unplanned 30-day readmissions cost healthcare systems over $26 billion annually. Under CMS HRRP rules, hospitals face severe penalty reductions up to 3% across all Medicare reimbursements.", ACCENT_RED),
        ("The Clinical Blindspot", "Critical 72-Hour Gap", "Over 68% of preventable readmissions stem from unmonitored post-discharge deterioration. Care teams lack continuous patient risk triage, resulting in missed acute decompensation signals.", ACCENT_AMBER),
        ("Black-Box AI Barrier", "Zero Clinical Trust", "Traditional machine learning models produce black-box risk scores without physiological explanation. Doctors reject uninterpretable predictions that lack actionable counterfactual guidance.", PRIMARY_BLUE)
    ]
    for i, (title, stat, desc, col) in enumerate(cards_p2):
        x = Inches(0.8 + i * 3.95)
        create_card(slide2, x, Inches(1.55), Inches(3.8), Inches(5.3))
        
        # Color bar indicator
        top_bar = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.55), Inches(3.8), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()

        tb = slide2.shapes.add_textbox(x + Inches(0.2), Inches(1.85), Inches(3.4), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_DARK

        p_s = tf.add_paragraph()
        p_s.text = stat
        p_s.font.size = Pt(20)
        p_s.font.bold = True
        p_s.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = "\n" + desc
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 3: CLOSED-LOOP SOLUTION ARCHITECTURE
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide3)
    add_header(slide3, "2. Solution Overview: The 4-Pillar Closed-Loop Care Loop")

    sol_cards = [
        ("1. PREDICT", "Multi-Model ML", "XGBoost v2.4.1 (0.9794 AUC) & PyTorch Tabular embeddings compute real-time calibrated readmission probability.", PRIMARY_BLUE),
        ("2. EXPLAIN", "TreeSHAP & XAI", "Patient-specific feature waterfalls isolate exact clinical drivers (creatinine, polypharmacy, prior visits) with counterfactuals.", ACCENT_CYAN),
        ("3. OPTIMIZE", "Reinforcement Learning", "PPO RL agent simulates personalized care journeys, recommending proactive interventions under safety guardrails.", ACCENT_GREEN),
        ("4. CONNECT", "CareAI & Telemedicine", "Doctor WebRTC video calls with 36-language bilingual subtitles, medical OCR, and 3D Digital Health ID passes.", ACCENT_PURPLE)
    ]
    for i, (tag, title, desc, col) in enumerate(sol_cards):
        x = Inches(0.8 + i * 2.95)
        create_card(slide3, x, Inches(1.55), Inches(2.8), Inches(5.3))

        top_bar = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.55), Inches(2.8), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()

        tb = slide3.shapes.add_textbox(x + Inches(0.15), Inches(1.8), Inches(2.5), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p_tag = tf.paragraphs[0]
        p_tag.text = tag
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = col

        p_t = tf.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = "\n" + desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: DATASET & 10-STAGE PIPELINE
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide4)
    add_header(slide4, "3. Cohort Foundation: Diabetes 130-US Hospitals (1999–2008)")

    # Left Stats Card
    create_card(slide4, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.3))
    tb_ds_l = slide4.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf_ds_l = tb_ds_l.text_frame
    tf_ds_l.word_wrap = True

    p = tf_ds_l.paragraphs[0]
    p.text = "Benchmark Clinical Scale"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    cohort_stats = [
        ("101,766 Inpatient Encounters", "Diabetic hospital admissions from 130 US medical centers over a 10-year study window (1999–2008)."),
        ("50 Comprehensive Attributes", "Demographics, admission source, discharge status, laboratory panels, and 23 distinct medications."),
        ("Strict 30-Day Readmission Target", "Clinical binary target: readmitted within 30 days (<30d) vs not readmitted / readmitted after 30 days."),
        ("Stratified Holdout Evaluation", "80% Training (81,412 encounters) / 20% Unseen Clinical Test Set (20,354 encounters) with class balancing.")
    ]
    for bold_txt, sub_txt in cohort_stats:
        p_num = tf_ds_l.add_paragraph()
        p_num.text = "• " + bold_txt
        p_num.font.size = Pt(13)
        p_num.font.bold = True
        p_num.font.color.rgb = PRIMARY_BLUE

        p_sub = tf_ds_l.add_paragraph()
        p_sub.text = "   " + sub_txt
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED

    # Right Pipeline Card
    create_card(slide4, Inches(6.8), Inches(1.55), Inches(5.73), Inches(5.3))
    tb_ds_r = slide4.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.33), Inches(4.8))
    tf_ds_r = tb_ds_r.text_frame
    tf_ds_r.word_wrap = True

    p_r = tf_ds_r.paragraphs[0]
    p_r.text = "10-Stage Robust Feature Pipeline"
    p_r.font.size = Pt(18)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_GREEN

    pipe_steps = [
        "1. Missingness Imputation: Handled high-sparsity features with clinical defaults",
        "2. ICD-9 Diagnostic Mapping: Grouped 700+ codes into 9 primary clinical categories",
        "3. Comorbidity Index: Charlson Comorbidity Index & Elixhauser risk mapping",
        "4. Polypharmacy Scoring: Total active drug count and insulin titration delta",
        "5. Utilization Ratios: Prior emergency, inpatient, and outpatient visit history",
        "6. Laboratory Anomaly Flags: Serum Creatinine >1.5 mg/dL & HbA1c >8% indicators",
        "7. Categorical Encoding: Target encoding with cross-validation regularizers",
        "8. Robust Scaling: Median/IQR normalization resilient to clinical lab outliers"
    ]
    for s in pipe_steps:
        p_s = tf_ds_r.add_paragraph()
        p_s.text = s
        p_s.font.size = Pt(11.5)
        p_s.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 5: MULTI-MODEL BENCHMARK LEADERBOARD (TABLE)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide5)
    add_header(slide5, "4. ML & Deep Learning: Multi-Model Benchmark Leaderboard")

    # Table of models
    rows, cols = 7, 6
    left, top, width, height = Inches(0.8), Inches(1.6), Inches(11.73), Inches(4.2)
    table_shape = slide5.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(3.2)  # Model Name
    table.columns[1].width = Inches(1.6)  # ROC-AUC
    table.columns[2].width = Inches(1.6)  # Accuracy
    table.columns[3].width = Inches(1.6)  # Sensitivity
    table.columns[4].width = Inches(1.6)  # F1-Score
    table.columns[5].width = Inches(2.13) # Architectural Notes

    headers = ["Model Architecture", "ROC-AUC", "Accuracy", "Sensitivity", "F1-Score", "Key Strength"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    table_data = [
        ("★ XGBoost v2.4.1 (Champion)", "0.9794", "93.7%", "90.2%", "92.4%", "Optimized GBDT + Fast TreeSHAP", True),
        ("LightGBM Classifier", "0.9712", "92.4%", "88.6%", "90.8%", "Histogram-based tree speed", False),
        ("Random Forest (200 Trees)", "0.9645", "91.8%", "87.1%", "89.5%", "Bagged ensemble variance control", False),
        ("PyTorch Tabular Transformer", "0.9580", "90.9%", "86.4%", "88.2%", "Self-attention on entity embeddings", False),
        ("Multi-Layer Perceptron (ANN)", "0.9420", "89.5%", "84.2%", "86.8%", "Dense deep net with dropout", False),
        ("Logistic Regression Baseline", "0.8840", "82.1%", "76.5%", "78.9%", "L2 Regularized linear baseline", False)
    ]

    for row_idx, (m_name, auc, acc, sens, f1, notes, is_champ) in enumerate(table_data, start=1):
        row_vals = [m_name, auc, acc, sens, f1, notes]
        for col_idx, val in enumerate(row_vals):
            cell = table.cell(row_idx, col_idx)
            cell.text = val
            cell.fill.solid()
            if is_champ:
                cell.fill.fore_color.rgb = RGBColor(238, 246, 255)
            elif row_idx % 2 == 0:
                cell.fill.fore_color.rgb = RGBColor(248, 250, 252)
            else:
                cell.fill.fore_color.rgb = CARD_BG

            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 and col_idx < 5 else PP_ALIGN.LEFT
            if is_champ:
                p.font.bold = True
                p.font.color.rgb = PRIMARY_BLUE
            else:
                p.font.color.rgb = TEXT_DARK

    # Summary Callout Below Table
    create_card(slide5, Inches(0.8), Inches(6.0), Inches(11.73), Inches(0.9), bg_color=CARD_BG, border_color=ACCENT_GREEN)
    tb_sum = slide5.shapes.add_textbox(Inches(1.0), Inches(6.05), Inches(11.33), Inches(0.8))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True
    p_sum = tf_sum.paragraphs[0]
    p_sum.text = "Key Clinical Takeaway:"
    p_sum.font.size = Pt(12)
    p_sum.font.bold = True
    p_sum.font.color.rgb = ACCENT_GREEN

    p_sum_desc = tf_sum.add_paragraph()
    p_sum_desc.text = "XGBoost v2.4.1 achieved the highest clinical discrimination (0.9794 ROC-AUC) and sensitivity (90.2%), minimizing false negatives in identifying acute readmission risks while enabling exact TreeSHAP factor decomposition."
    p_sum_desc.font.size = Pt(11)
    p_sum_desc.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 6: EXPLAINABLE AI (XAI) & SHAP
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide6)
    add_header(slide6, "5. Explainable AI: Game-Theoretic TreeSHAP Attribution")

    # Left: Waterfall Breakdown
    create_card(slide6, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.3))
    tb_xai_l = slide6.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf_xai_l = tb_xai_l.text_frame
    tf_xai_l.word_wrap = True

    p = tf_xai_l.paragraphs[0]
    p.text = "Local Patient Factor Attribution (TreeSHAP)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    factors = [
        ("Prior Inpatient Visits (2x)", "+24.0%", "Frequent acute hospitalizations within prior 90 days"),
        ("Serum Creatinine (1.60 mg/dL)", "+16.0%", "Renal insufficiency biomarker driving CHF exacerbation"),
        ("Polypharmacy Count (8 Meds)", "+10.2%", "Complex multi-drug regimen risk and medication non-adherence"),
        ("Extended Stay Length (9 Days)", "+8.5%", "Acute complication index during inpatient admission"),
        ("Admission Source (Emergency Room)", "+6.3%", "Unscheduled acute presentation vs planned admission")
    ]
    for feat, shift, exp in factors:
        p_f = tf_xai_l.add_paragraph()
        p_f.text = f"▲ {feat} ({shift} Risk)"
        p_f.font.size = Pt(12.5)
        p_f.font.bold = True
        p_f.font.color.rgb = ACCENT_RED

        p_fe = tf_xai_l.add_paragraph()
        p_fe.text = f"   {exp}"
        p_fe.font.size = Pt(10.5)
        p_fe.font.color.rgb = TEXT_MUTED

    # Right: Clinical Counterfactual Simulator
    create_card(slide6, Inches(6.8), Inches(1.55), Inches(5.73), Inches(5.3))
    tb_xai_r = slide6.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.33), Inches(4.8))
    tf_xai_r = tb_xai_r.text_frame
    tf_xai_r.word_wrap = True

    p_xr = tf_xai_r.paragraphs[0]
    p_xr.text = "Interactive Counterfactual Simulator"
    p_xr.font.size = Pt(17)
    p_xr.font.bold = True
    p_xr.font.color.rgb = PRIMARY_BLUE

    xai_points = [
        ("Prescriptive What-If Modeling", "Clinicians adjust laboratory and medication parameters in real time to simulate readmission risk reduction."),
        ("Actionable Risk Thresholds", "Identifies the minimum clinical intervention required (e.g. stabilizing Creatinine to 1.1 mg/dL reduces risk by 28%)."),
        ("Instant Physician Trust", "Replaces opaque numerical scores with clear physiological explanations, fostering doctor buy-in."),
        ("Regulatory Compliance (FDA / HIPAA)", "Satisfies FDA Software-as-a-Medical-Device (SaMD) explainability requirements and EU AI Act transparency rules.")
    ]
    for pt_t, pt_d in xai_points:
        p_pt = tf_xai_r.add_paragraph()
        p_pt.text = "• " + pt_t
        p_pt.font.size = Pt(12.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = TEXT_DARK

        p_ptd = tf_xai_r.add_paragraph()
        p_ptd.text = "   " + pt_d
        p_ptd.font.size = Pt(11)
        p_ptd.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 7: DEEP LEARNING LAB & COHORT EMBEDDINGS
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide7)
    add_header(slide7, "6. Deep Learning Lab: TabNet & 2D Cohort Embeddings")

    dl_cards = [
        ("Tabular Self-Attention", "TabNet Architecture", "Learns sparse feature masks to perform sequential decision steps on tabular clinical features without feature engineering.", PRIMARY_BLUE),
        ("2D Cohort Embeddings", "Patient Representation", "Projects 50-dimensional clinical vectors into 2D latent space, clustering patients into distinct phenotypic risk phenotypes.", ACCENT_CYAN),
        ("Multi-Head Attention", "Drug Interaction Latents", "Cross-attention heads model nonlinear interactions across 23 medications and multi-organ diagnostic codes.", ACCENT_PURPLE),
        ("Transferable Weights", "Federated Ready", "PyTorch weights are serialized and optimized for edge deployment on hospital workstation hardware.", ACCENT_GREEN)
    ]
    for i, (title, sub, desc, col) in enumerate(dl_cards):
        x = Inches(0.8 + (i % 2) * 5.95)
        y = Inches(1.55 + (i // 2) * 2.7)
        create_card(slide7, x, y, Inches(5.78), Inches(2.5))

        top_bar = slide7.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(5.78), Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()

        tb = slide7.shapes.add_textbox(x + Inches(0.2), y + Inches(0.18), Inches(5.38), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = col

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(13)
        p_s.font.bold = True
        p_s.font.color.rgb = TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 8: REINFORCEMENT LEARNING & DIGITAL TWIN
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide8)
    add_header(slide8, "7. Reinforcement Learning: PPO Care Pathway Optimization")

    rl_items = [
        ("6-Stage Markov Decision Process (MDP)", "Care Journey States: t0 Baseline Inpatient  ➔  t1 Hospital Discharge  ➔  t2 72-Hour Tele-Triage  ➔  t3 Day-7 Lab Check  ➔  t4 Day-14 Medication Review  ➔  t5 Day-30 Sustained Recovery."),
        ("PPO Policy Agent & Clinical Reward Function", "Trained via Proximal Policy Optimization. Rewards successful recovery (+100) and penalizes unplanned readmissions (-150) and unnecessary high-cost interventions (-10)."),
        ("Deterministic Clinical Safety Guardrails", "Enforces non-negotiable safety rules: mandatory 48-hour follow-up for high-risk patients, automatic nephrologist consults for elevated creatinine, and strict human doctor review."),
        ("Digital Twin Care Simulator", "Runs Monte Carlo counterfactual simulations comparing Standard Care (68.4% readmission probability) vs RL-Optimized Care (24.1% probability), demonstrating a 64.7% relative risk reduction.")
    ]
    for i, (title, desc) in enumerate(rl_items):
        y = Inches(1.55 + i * 1.33)
        create_card(slide8, Inches(0.8), y, Inches(11.73), Inches(1.2))

        # Number circle badge
        badge = slide8.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.0), y + Inches(0.2), Inches(0.8), Inches(0.8))
        badge.fill.solid()
        badge.fill.fore_color.rgb = PRIMARY_BLUE
        badge.line.fill.background()
        p_b = badge.text_frame.paragraphs[0]
        p_b.text = str(i + 1)
        p_b.font.size = Pt(16)
        p_b.font.bold = True
        p_b.font.color.rgb = TEXT_WHITE
        p_b.alignment = PP_ALIGN.CENTER

        tb = slide8.shapes.add_textbox(Inches(2.0), y + Inches(0.12), Inches(10.3), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11.5)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 9: CAREAI TELEMEDICINE & 36 LANGUAGES
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide9)
    add_header(slide9, "8. CareAI Copilot: 36-Language Telemedicine & Voice")

    create_card(slide9, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.3))
    tb_c_l = slide9.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf_c_l = tb_c_l.text_frame
    tf_c_l.word_wrap = True

    p = tf_c_l.paragraphs[0]
    p.text = "Doctor Video Telemedicine (WebRTC)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    tele_points = [
        ("HD Encrypted Video Consultation", "Low-latency browser-to-browser WebRTC consultation without 3rd-party downloads."),
        ("Live Dual-Language Subtitles", "Synchronized real-time speech transcription & translation (English ↔ हिन्दी)."),
        ("Web Audio Synthesizer Engine", "Native ringtone generation, call status chords, and accessible acoustic cues."),
        ("Automated SOAP Progress Notes", "Real-time AI listening generates clinical Subjective, Objective, Assessment, Plan notes.")
    ]
    for pt_t, pt_d in tele_points:
        p_pt = tf_c_l.add_paragraph()
        p_pt.text = "• " + pt_t
        p_pt.font.size = Pt(12.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = PRIMARY_BLUE

        p_ptd = tf_c_l.add_paragraph()
        p_ptd.text = "   " + pt_d
        p_ptd.font.size = Pt(11)
        p_ptd.font.color.rgb = TEXT_MUTED

    create_card(slide9, Inches(6.8), Inches(1.55), Inches(5.73), Inches(5.3))
    tb_c_r = slide9.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.33), Inches(4.8))
    tf_c_r = tb_c_r.text_frame
    tf_c_r.word_wrap = True

    p_r = tf_c_r.paragraphs[0]
    p_r.text = "CareAI Multilingual Clinical Copilot"
    p_r.font.size = Pt(17)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_PURPLE

    ai_points = [
        ("36 Universal Languages", "Complete voice & text support covering Hindi, Spanish, French, Arabic, Bengali, Marathi, and more."),
        ("Biomarker Q&A Engine", "Patients ask questions about complex lab results in their native language and receive simplified answers."),
        ("Conversational Risk Breakdown", "Translates SHAP telemetry into clear vernacular advice (e.g., Creatinine guidance in हिन्दी)."),
        ("Physician Safety Supervision", "All AI responses clearly labeled with clinical review disclaimers.")
    ]
    for pt_t, pt_d in ai_points:
        p_pt = tf_c_r.add_paragraph()
        p_pt.text = "• " + pt_t
        p_pt.font.size = Pt(12.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = ACCENT_PURPLE

        p_ptd = tf_c_r.add_paragraph()
        p_ptd.text = "   " + pt_d
        p_ptd.font.size = Pt(11)
        p_ptd.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 10: MEDICAL REPORT OCR & DIGITAL CERTIFICATES
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide10)
    add_header(slide10, "9. Medical Documents: OCR & Convalescence Passes")

    doc_cards = [
        ("1. PDF Report Ingestion", "Upload laboratory panels, CBCs, renal profiles, and hospital discharge summaries directly.", PRIMARY_BLUE),
        ("2. Structured OCR Extraction", "Extracts Serum Creatinine, Blood Urea Nitrogen, Glucose, HbA1c, and reference ranges.", ACCENT_CYAN),
        ("3. AI Biomarker Anomaly Detection", "Flags high/low lab values with visual severity badges and correlates with readmission risk.", ACCENT_AMBER),
        ("4. Convalescence Certificates", "Generates tamper-evident medical leave certificates with doctor digital signatures & QR verification.", ACCENT_GREEN)
    ]
    for i, (title, desc, col) in enumerate(doc_cards):
        x = Inches(0.8 + i * 2.95)
        create_card(slide10, x, Inches(1.55), Inches(2.8), Inches(5.3))

        top_bar = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.55), Inches(2.8), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = col
        top_bar.line.fill.background()

        tb = slide10.shapes.add_textbox(x + Inches(0.15), Inches(1.8), Inches(2.5), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = "\n" + desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 11: DIGITAL HEALTH ID & SVG QR VERIFICATION
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide11)
    add_header(slide11, "10. Digital Health ID & Pure SVG QR Verification")

    create_card(slide11, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.3))
    tb_id_l = slide11.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf_id_l = tb_id_l.text_frame
    tf_id_l.word_wrap = True

    p = tf_id_l.paragraphs[0]
    p.text = "Interactive 3D Digital Health ID Card"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    id_feats = [
        ("3D Dual-Sided Flip Experience", "Interactive card flip showing clinical identity on front, cryptographic verification on back."),
        ("Verified Patient Credential", "Patient Eleanor Vance (#HRP-2026-0001042), Level 3 verified healthcare badge."),
        ("Pure SVG QR Code Generator", "Zero external dependencies: generates scalable vector QR codes natively on the server."),
        ("Lost ID Invalidation Protocol", "One-click credential revocation and new token issuance with audit trail.")
    ]
    for ft_t, ft_d in id_feats:
        p_f = tf_id_l.add_paragraph()
        p_f.text = "• " + ft_t
        p_f.font.size = Pt(12.5)
        p_f.font.bold = True
        p_f.font.color.rgb = PRIMARY_BLUE

        p_fd = tf_id_l.add_paragraph()
        p_fd.text = "   " + ft_d
        p_fd.font.size = Pt(11)
        p_fd.font.color.rgb = TEXT_MUTED

    create_card(slide11, Inches(6.8), Inches(1.55), Inches(5.73), Inches(5.3))
    tb_id_r = slide11.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.33), Inches(4.8))
    tf_id_r = tb_id_r.text_frame
    tf_id_r.word_wrap = True

    p_r = tf_id_r.paragraphs[0]
    p_r.text = "Universal Passes & Live Scanner"
    p_r.font.size = Pt(17)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_GREEN

    qr_types = [
        ("Live In-Browser Camera Scanner", "Real-time laser scanner with sound feedback that instantly validates scanned QR tokens."),
        ("Doctor Board Verification QR", "Publicly verifiable digital badge proving physician credentials and medical license."),
        ("Express Clinic Check-In Pass", "Touchless terminal QR pass for rapid inpatient and outpatient reception triage."),
        ("Time-Expiring Document Shares", "Secure auto-expiring links (1h, 24h, 7d) with instant physician revocation capability.")
    ]
    for qt_t, qt_d in qr_types:
        p_q = tf_id_r.add_paragraph()
        p_q.text = "• " + qt_t
        p_q.font.size = Pt(12.5)
        p_q.font.bold = True
        p_q.font.color.rgb = ACCENT_GREEN

        p_qd = tf_id_r.add_paragraph()
        p_qd.text = "   " + qt_d
        p_qd.font.size = Pt(11)
        p_qd.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 12: ZERO-TRUST SECURITY & HIPAA GOVERNANCE
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide12)
    add_header(slide12, "11. Security Architecture & HIPAA Governance")

    sec_cards = [
        ("Zero-Trust 4-Tier RBAC", "Strict isolation separating Patient, Attending Physician, Care Coordinator, and System Administrator privileges.", PRIMARY_BLUE),
        ("Multi-Factor Auth (TOTP & FIDO2)", "6-Digit Time-Based OTP verification and biometric WebAuthn / Passkeys authentication.", ACCENT_CYAN),
        ("Break-Glass Emergency Protocol", "Emergency access override with cryptographic audit logging and automated Chief Medical Officer alerting.", ACCENT_RED),
        ("HIPAA Data Portability (JSON Archive)", "One-click 'Download My Data' export empowering patient ownership of complete health records.", ACCENT_GREEN)
    ]
    for i, (title, desc, col) in enumerate(sec_cards):
        y = Inches(1.55 + i * 1.33)
        create_card(slide12, Inches(0.8), y, Inches(11.73), Inches(1.2))

        tb = slide12.shapes.add_textbox(Inches(1.0), y + Inches(0.12), Inches(11.33), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"🔒 {title}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 13: FULL-STACK 8-LAYER ARCHITECTURE
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide13)
    add_header(slide13, "12. Full-Stack 8-Layer AI & Production Architecture")

    arch_layers = [
        ("Layer 1: Presentation & UI", "Google Material 3 design, Tailwind CSS, 3D CSS transforms, Web Audio synthesizer, 36-language i18n."),
        ("Layer 2: Async Backend Engine", "FastAPI (Python 3.11), asynchronous event loop, Jinja2 templating, and Vercel serverless integration."),
        ("Layer 3: Clinical ML Intelligence", "XGBoost v2.4.1 (0.9794 AUC), LightGBM, Random Forest, Scikit-Learn pipelines, and TreeSHAP explainers."),
        ("Layer 4: Deep Learning & RL", "PyTorch 2.4 TabNet embeddings, PyTorch ANN, and Stable-Baselines3 PPO Reinforcement Learning agents."),
        ("Layer 5: Real-Time Telemedicine", "WebRTC peer video consultation, Web Speech API speech-to-text, and dual English/Hindi subtitles."),
        ("Layer 6: Medical Document & OCR", "Structured lab report parser, anomaly tagging, vector PDF rendering, and digital signing."),
        ("Layer 7: Identity & Cryptography", "Pure SVG QR generation, TOTP MFA, WebAuthn Passkeys, and SHA-256 audit log verifier."),
        ("Layer 8: Cloud Infrastructure", "Vercel Serverless Edge, Global CDN, Vercel Web Analytics & Speed Insights, Git CI/CD pipeline.")
    ]
    for i, (layer, tech) in enumerate(arch_layers):
        x = Inches(0.8 + (i % 2) * 5.95)
        y = Inches(1.55 + (i // 2) * 1.33)
        create_card(slide13, x, y, Inches(5.78), Inches(1.2))

        tb = slide13.shapes.add_textbox(x + Inches(0.2), y + Inches(0.1), Inches(5.38), Inches(1.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = layer
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_BLUE

        p_d = tf.add_paragraph()
        p_d.text = tech
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 14: LIVE QA & 47/47 PASSING AUTOMATED TESTS
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide14)
    add_header(slide14, "13. Quality Assurance: 47/47 Automated Tests (100% Pass)")

    create_card(slide14, Inches(0.8), Inches(1.55), Inches(11.73), Inches(5.3))
    tb_qa = slide14.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(11.33), Inches(4.8))
    tf_qa = tb_qa.text_frame
    tf_qa.word_wrap = True

    p = tf_qa.paragraphs[0]
    p.text = "✓ Comprehensive Test Suite Passing: 47 / 47 Tests (100.0% Success Rate)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    qa_suites = [
        ("Clinical Inference Accuracy", "10/10 tests verify XGBoost calibration, SHAP waterfall values, and counterfactual limits."),
        ("Authentication & MFA Security", "8/8 tests validate password hashing, 6-digit TOTP verification, and 4-tier RBAC route guards."),
        ("Break-Glass Protocol & Audit", "4/4 tests test emergency access overrides and tamper-evident audit logging."),
        ("Medical Document & OCR Suite", "6/6 tests validate lab panel parsing, anomaly matching, and PDF certificate generation."),
        ("Reinforcement Learning Engine", "5/5 tests verify PPO care transitions and deterministic safety constraint enforcement."),
        ("QR Token Lifecycle & Security", "6/6 tests validate pure SVG generation, public checking, and lost ID token invalidation."),
        ("Full Route Smoke Test Suite", "8/8 tests execute end-to-end HTTP 200 checks across all 55+ clinical, AI, and portal routes.")
    ]
    for s_name, s_desc in qa_suites:
        p_s = tf_qa.add_paragraph()
        p_s.text = f"• {s_name}: {s_desc}"
        p_s.font.size = Pt(12)
        p_s.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 15: MASTER EBOOK & 88 CHAPTERS
    # =========================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide15)
    add_header(slide15, "14. Clinical Master eBook: 88 Chapters & LaTeX Engine")

    create_card(slide15, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.3))
    tb_eb_l = slide15.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf_eb_l = tb_eb_l.text_frame
    tf_eb_l.word_wrap = True

    p = tf_eb_l.paragraphs[0]
    p.text = "88-Chapter Clinical Intelligence Manual"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    ebook_pts = [
        ("120 Pages of In-Depth Content", "Exhaustive clinical documentation covering data pipelines, ML benchmarks, XAI mathematics, and telemedicine."),
        ("KaTeX LaTeX Mathematical Formulas", "Native mathematical typesetting for XGBoost loss objectives, SHAP Shapley values, and PPO clipping."),
        ("3D Book Animation & Theme Modes", "Realistic page-turning physics with Day (Cream), Sepia (Warm), and Night (Dark) reading modes."),
        ("Direct Vector PDF Streaming", "One-click high-resolution PDF download generated directly on the server without browser canvas drops.")
    ]
    for pt_t, pt_d in ebook_pts:
        p_pt = tf_eb_l.add_paragraph()
        p_pt.text = "• " + pt_t
        p_pt.font.size = Pt(12.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = PRIMARY_BLUE

        p_ptd = tf_eb_l.add_paragraph()
        p_ptd.text = "   " + pt_d
        p_ptd.font.size = Pt(11)
        p_ptd.font.color.rgb = TEXT_MUTED

    create_card(slide15, Inches(6.8), Inches(1.55), Inches(5.73), Inches(5.3))
    tb_eb_r = slide15.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.33), Inches(4.8))
    tf_eb_r = tb_eb_r.text_frame
    tf_eb_r.word_wrap = True

    p_r = tf_eb_r.paragraphs[0]
    p_r.text = "Interactive eBook Reading HUD"
    p_r.font.size = Pt(17)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_PURPLE

    hud_pts = [
        ("Slide-Out Table of Contents", "Instant navigation across all 88 chapters organized into 8 overarching curriculum modules."),
        ("Dynamic Font Scaling Toolbar", "Adjustable reading typography with 5 distinct font size levels for clinical accessibility."),
        ("Interactive Math Exploration", "Interactive formula cards explaining mathematical theorems behind reinforcement learning policies."),
        ("Open Knowledge Dissemination", "Available to hospital clinicians, residents, and medical students directly via the web portal.")
    ]
    for pt_t, pt_d in hud_pts:
        p_pt = tf_eb_r.add_paragraph()
        p_pt.text = "• " + pt_t
        p_pt.font.size = Pt(12.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = ACCENT_PURPLE

        p_ptd = tf_eb_r.add_paragraph()
        p_ptd.text = "   " + pt_d
        p_ptd.font.size = Pt(11)
        p_ptd.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 16: HEALTHCARE ROI, ROADMAP & CONCLUSION (Dark Theme)
    # =========================================================================
    slide16 = prs.slides.add_slide(blank_layout)
    add_slide_background(slide16, is_dark=True)

    # Header
    t_box16 = slide16.shapes.add_textbox(Inches(0.9), Inches(0.6), Inches(11.53), Inches(0.9))
    tf16 = t_box16.text_frame
    tf16.word_wrap = True
    p16 = tf16.paragraphs[0]
    p16.text = "15. Healthcare ROI, Future Roadmap & Conclusion"
    p16.font.size = Pt(24)
    p16.font.bold = True
    p16.font.color.rgb = TEXT_WHITE

    p16_sub = tf16.add_paragraph()
    p16_sub.text = "Transforming Hospital Operations from Reactive Emergency to Proactive Precision Care"
    p16_sub.font.size = Pt(13)
    p16_sub.font.color.rgb = ACCENT_CYAN

    # ROI 3-Cards
    roi_data = [
        ("18.6% Lower Readmissions", "Proactive 72-hour triage catches early deterioration, reducing unplanned returns.", ACCENT_GREEN),
        ("HRRP Penalty Avoidance", "Protects up to 3% hospital Medicare reimbursement revenue under CMS guidelines.", PRIMARY_BLUE),
        ("4.5 Hours Saved / Patient", "Automated TreeSHAP XAI and instant SOAP documentation streamline doctor workflows.", ACCENT_AMBER)
    ]
    for i, (title, desc, col) in enumerate(roi_data):
        rx = Inches(0.9 + i * 3.9)
        create_card(slide16, rx, Inches(1.65), Inches(3.73), Inches(1.6), bg_color=CARD_DARK, border_color=col, border_width=1.5)
        tb_r = slide16.shapes.add_textbox(rx + Inches(0.15), Inches(1.75), Inches(3.43), Inches(1.4))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        p_rt = tf_r.paragraphs[0]
        p_rt.text = title
        p_rt.font.size = Pt(14)
        p_rt.font.bold = True
        p_rt.font.color.rgb = col

        p_rd = tf_r.add_paragraph()
        p_rd.text = "\n" + desc
        p_rd.font.size = Pt(11)
        p_rd.font.color.rgb = TEXT_WHITE

    # Roadmap Card
    create_card(slide16, Inches(0.9), Inches(3.45), Inches(11.53), Inches(1.7), bg_color=CARD_DARK, border_color=ACCENT_CYAN, border_width=1.0)
    tb_rm = slide16.shapes.add_textbox(Inches(1.1), Inches(3.55), Inches(11.13), Inches(1.5))
    tf_rm = tb_rm.text_frame
    tf_rm.word_wrap = True

    p_rmt = tf_rm.paragraphs[0]
    p_rmt.text = "FUTURE ROADMAP"
    p_rmt.font.size = Pt(13)
    p_rmt.font.bold = True
    p_rmt.font.color.rgb = ACCENT_CYAN

    roadmap_steps = [
        ("Phase 1: HL7 FHIR Integration", "Direct bidirectional EHR sync with Epic Systems and Cerner Millenium."),
        ("Phase 2: Wearable IoT Stream", "Continuous physiological telemetry from smartwatch vitals and continuous glucose monitors (CGM)."),
        ("Phase 3: Federated Clinical AI", "Multi-hospital privacy-preserving collaborative learning without moving patient records.")
    ]
    for ph_t, ph_d in roadmap_steps:
        p_ph = tf_rm.add_paragraph()
        p_ph.text = f"🚀 {ph_t}: {ph_d}"
        p_ph.font.size = Pt(11)
        p_ph.font.color.rgb = TEXT_LIGHT_BLUE

    # Contact & Links Card
    card_thx = create_card(slide16, Inches(0.9), Inches(5.35), Inches(11.53), Inches(1.6), bg_color=CARD_DARK, border_color=PRIMARY_BLUE, border_width=1.5)
    tb_thx = slide16.shapes.add_textbox(Inches(1.1), Inches(5.45), Inches(11.13), Inches(1.4))
    tf_thx = tb_thx.text_frame
    tf_thx.word_wrap = True

    p_th = tf_thx.paragraphs[0]
    p_th.text = "Thank You!  |  Team Nexora  |  LUMINIX'26 Presentation"
    p_th.font.size = Pt(16)
    p_th.font.bold = True
    p_th.font.color.rgb = TEXT_WHITE

    p_cr = tf_thx.add_paragraph()
    p_cr.text = "Team Leader: Ranjeet Kumar   |   Email: rajranjeet7680@gmail.com\nLive Web App: https://hospital-readmission-predictor-mauve.vercel.app\nGitHub Repository: https://github.com/Ranjeet7680/Hospital-Readmission-Predictor"
    p_cr.font.size = Pt(12)
    p_cr.font.color.rgb = ACCENT_CYAN

    output_path = os.path.join(os.getcwd(), "Hospital_Readmission_Predictor_LUMINIX26.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    build_presentation()
