# Master Compiler for Complete 88-Chapter eBook: Hospital Readmission Predictor
import os
import sys

# Ensure local scripts/ directory is in sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ebook_builder"))

from part1_introduction import get_part1
from part2_product import get_part2
from part3_data import get_part3
from part4_ml import get_part4
from part5_dl import get_part5
from part6_xai import get_part6
from part7_rl import get_part7
from part8_documents import get_part8
from part9_telemedicine import get_part9
from part10_health_id import get_part10
from part11_auth import get_part11
from part12_analytics import get_part12
from part13_responsive import get_part13
from part14_sound import get_part14
from part15_network import get_part15
from part16_architecture import get_part16
from part17_dev import get_part17
from part18_ethics import get_part18
from part19_case_studies import get_part19
from part20_conclusion import get_part20
from appendices import get_appendices

def compile_master_ebook():
    output_dir = os.path.join(os.getcwd(), "docs", "ebook")
    os.makedirs(output_dir, exist_ok=True)

    print("Building 88-Chapter Master eBook...")

    # Front Matter
    front_matter = """# Hospital Readmission Predictor
## AI-Powered Healthcare Intelligence, Readmission Prediction & Connected Care

**Author & Organization:** Team Nexora (*Intelligence • Automation • Impact*)  
**Team Leader & Lead Architect:** Ranjeet Kumar (`rajranjeet7680@gmail.com`)  
**Hackathon Initiative:** LUMINIX'26 Innovation Track  
**Platform Version:** v2.4.1 Production  
**Publication Date:** August 2026  
**Repository:** [https://github.com/Ranjeet7680/Hospital-Readmission-Predictor](https://github.com/Ranjeet7680/Hospital-Readmission-Predictor)  
**Live Application:** [https://hospital-readmission-predictor-mauve.vercel.app](https://hospital-readmission-predictor-mauve.vercel.app)  

---

### Copyright & Intellectual Property Notice
© 2026 Nexora Team. All rights reserved.  
Permission is hereby granted for educational, academic, and clinical research evaluation. The algorithmic concepts, architecture blueprints, data engineering pipelines, and source implementations contained in this work are developed under open healthcare innovation standards.

---

### Dataset Attribution
This research and platform demonstration utilizes the **Diabetes 130-US Hospitals for Years 1999–2008** dataset, originally contributed by Strack et al. (Center for Clinical and Translational Research, Virginia Commonwealth University) and hosted by the UC Irvine Machine Learning Repository and Kaggle. We gratefully acknowledge the clinical data contribution of over 101,766 inpatient encounters across 130 medical facilities.

---

### Strict Medical & Clinical AI Disclaimer
> ⚠️ **MANDATORY CLINICAL DISCLAIMER**: The Hospital Readmission Predictor (HRP Clinical) platform, including its Machine Learning (ML), Deep Learning (DL), Explainable AI (XAI), Reinforcement Learning (RL), and CareAI conversational agents, is strictly engineered as an **assistive decision-support system (CDSS)**. It is **NOT** an autonomous diagnostic device, prescriptive medical engine, or replacement for board-certified clinical judgment. All risk scores, biomarker interpretations, care pathway simulations, and digital medical certificate drafts must undergo independent review and verification by licensed healthcare practitioners before clinical action.

---

### Preface: The Quest for Proactive Healthcare Intelligence
Modern hospitals face a persistent paradox: while electronic health records (EHR) generate billions of gigabytes of diagnostic telemetry, post-discharge patient care remains surprisingly fragmented. Once a patient walks out of the hospital doors, clinicians lose continuous visibility, creating a high-risk transition window where physiological deterioration goes unnoticed until an acute emergency room readmission occurs.

This eBook serves as the definitive technical manual, clinical architectural guide, and foundational treatise for the **Hospital Readmission Predictor** platform. Whether you are a machine learning engineer, physician executive, healthcare informatics specialist, or software architect, this volume will walk you through the end-to-end design of a closed-loop healthcare intelligence platform that combines gradient boosted trees, deep tabular transformers, interpretable TreeSHAP attribution, reinforcement learning digital twins, encrypted WebRTC telemedicine, and cryptographic digital health identity cards.

---
"""

    parts = [
        ("part_01_introduction.md", get_part1()),
        ("part_02_product.md", get_part2()),
        ("part_03_data.md", get_part3()),
        ("part_04_ml.md", get_part4()),
        ("part_05_dl.md", get_part5()),
        ("part_06_xai.md", get_part6()),
        ("part_07_rl.md", get_part7()),
        ("part_08_documents.md", get_part8()),
        ("part_09_telemedicine.md", get_part9()),
        ("part_10_health_id.md", get_part10()),
        ("part_11_auth.md", get_part11()),
        ("part_12_analytics.md", get_part12()),
        ("part_13_responsive.md", get_part13()),
        ("part_14_sound.md", get_part14()),
        ("part_15_network.md", get_part15()),
        ("part_16_architecture.md", get_part16()),
        ("part_17_dev.md", get_part17()),
        ("part_18_ethics.md", get_part18()),
        ("part_19_case_studies.md", get_part19()),
        ("part_20_conclusion.md", get_part20()),
        ("appendices.md", get_appendices())
    ]

    # 1. Save Modular Markdown Files
    for filename, content in parts:
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved: {filename}")

    # 2. Save Master Markdown Book
    master_md_path = os.path.join(output_dir, "Hospital_Readmission_Predictor_Complete_eBook.md")
    with open(master_md_path, "w", encoding="utf-8") as f:
        f.write(front_matter + "\n\n")
        for _, content in parts:
            f.write(content + "\n\n")
    print(f"Master Markdown Book compiled: {master_md_path}")

    # 3. Generate Styled HTML Book
    generate_html_book(master_md_path, os.path.join(output_dir, "Hospital_Readmission_Predictor_Complete_eBook.html"))

def generate_html_book(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Basic markdown to HTML conversion with rich CSS
    import re

    # Convert headers
    html_content = md_text
    html_content = re.sub(r'^# (.*?)$', r'<h1 class="book-part-title">\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*?)$', r'<h2 class="book-chapter-title">\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.*?)$', r'<h3 class="book-section-title">\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.*?)$', r'<h4 class="book-subsection-title">\1</h4>', html_content, flags=re.MULTILINE)

    # Convert bold and italics
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)

    # Convert code blocks
    html_content = re.sub(r'```(\w*)\n(.*?)```', r'<pre class="code-block language-\1"><code>\2</code></pre>', html_content, flags=re.DOTALL)
    html_content = re.sub(r'`(.*?)`', r'<code class="inline-code">\1</code>', html_content)

    # Convert blockquotes / callouts
    html_content = re.sub(r'^> ⚠️ (.*?)$', r'<div class="callout callout-warning"><span class="icon">⚠️</span> \1</div>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^> 🛡️ (.*?)$', r'<div class="callout callout-shield"><span class="icon">🛡️</span> \1</div>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^> (.*?)$', r'<blockquote class="book-quote">\1</blockquote>', html_content, flags=re.MULTILINE)

    # Convert horizontal rules
    html_content = re.sub(r'^---$', r'<hr class="chapter-divider"/>', html_content, flags=re.MULTILINE)

    # Convert unordered lists
    lines = html_content.split('\n')
    in_list = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('* ') or line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul class="book-list">')
                in_list = True
            new_lines.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            new_lines.append(line)
    if in_list:
        new_lines.append('</ul>')
    html_content = '\n'.join(new_lines)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Readmission Predictor - Complete Master eBook (88 Chapters)</title>
    <link rel="icon" type="image/svg+xml" href="../../static/favicon.svg"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #005bbf;
            --primary-dark: #003e8a;
            --secondary: #002F6C;
            --accent: #22D3EE;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --bg-page: #f8fafc;
            --bg-card: #ffffff;
            --border: #e2e8f0;
            --warning-bg: #fffbeb;
            --warning-border: #f59e0b;
        }}
        @media print {{
            body {{ background: #fff !important; font-size: 11pt; }}
            .no-print {{ display: none !important; }}
            .book-part-title {{ page-break-before: always; }}
            .book-chapter-title {{ page-break-before: always; }}
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.7;
            color: var(--text-main);
            background: var(--bg-page);
            margin: 0;
            padding: 0;
        }}
        .book-container {{
            max-width: 960px;
            margin: 0 auto;
            background: var(--bg-card);
            padding: 60px 80px;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.05);
            border-left: 1px solid var(--border);
            border-right: 1px solid var(--border);
        }}
        .book-cover {{
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, #002F6C 0%, #005bbf 50%, #001a41 100%);
            color: white;
            border-radius: 16px;
            margin-bottom: 50px;
            box-shadow: 0 20px 25px -5px rgba(0, 47, 108, 0.3);
        }}
        .book-cover h1 {{
            font-family: 'Cinzel', serif;
            font-size: 2.8rem;
            margin: 0 0 12px 0;
            color: #ffffff;
            letter-spacing: 1px;
        }}
        .book-cover .tagline {{
            font-size: 1.25rem;
            color: var(--accent);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 24px;
        }}
        .book-cover .meta {{
            font-size: 0.95rem;
            color: #cbd5e1;
            line-height: 1.6;
        }}
        .book-part-title {{
            font-family: 'Cinzel', serif;
            font-size: 2.2rem;
            color: var(--secondary);
            border-bottom: 3px solid var(--primary);
            padding-bottom: 12px;
            margin-top: 60px;
            margin-bottom: 24px;
        }}
        .book-chapter-title {{
            font-size: 1.6rem;
            color: var(--primary-dark);
            margin-top: 40px;
            margin-bottom: 16px;
            padding-left: 12px;
            border-left: 4px solid var(--primary);
        }}
        .book-section-title {{
            font-size: 1.25rem;
            color: #0f172a;
            margin-top: 28px;
            margin-bottom: 12px;
        }}
        .code-block {{
            background: #0f172a;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88rem;
            overflow-x: auto;
            line-height: 1.5;
            margin: 20px 0;
        }}
        .inline-code {{
            background: #f1f5f9;
            color: #005bbf;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
        }}
        .callout {{
            padding: 16px 20px;
            border-radius: 8px;
            margin: 24px 0;
            font-size: 0.95rem;
            line-height: 1.6;
        }}
        .callout-warning {{
            background: var(--warning-bg);
            border-left: 5px solid var(--warning-border);
            color: #92400e;
        }}
        .callout-shield {{
            background: #f0fdf4;
            border-left: 5px solid #16a34a;
            color: #166534;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
            font-size: 0.92rem;
        }}
        th, td {{
            padding: 12px 16px;
            border: 1px solid var(--border);
            text-align: left;
        }}
        th {{
            background: #f1f5f9;
            font-weight: 600;
            color: var(--secondary);
        }}
        tr:nth-child(even) {{
            background: #f8fafc;
        }}
        .chapter-divider {{
            border: none;
            height: 1px;
            background: var(--border);
            margin: 40px 0;
        }}
        .book-list li {{
            margin-bottom: 6px;
        }}
        .nav-bar {{
            position: sticky;
            top: 0;
            background: white;
            border-bottom: 1px solid var(--border);
            padding: 12px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
        }}
        .print-btn {{
            background: var(--primary);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
        }}
        .print-btn:hover {{
            background: var(--primary-dark);
        }}
    </style>
</head>
<body>
    <div class="nav-bar no-print">
        <strong>Hospital Readmission Predictor — Complete Master eBook (88 Chapters)</strong>
        <button class="print-btn" onclick="window.print()">🖨️ Print / Save to PDF</button>
    </div>

    <div class="book-container">
        <div class="book-cover">
            <h1>HOSPITAL READMISSION PREDICTOR</h1>
            <div class="tagline">Predict Risk. Explain Insights. Connect Care.</div>
            <div class="meta">
                <strong>Comprehensive Healthcare AI, Machine Learning & Telemedicine Treatise</strong><br>
                20 Parts • 88 Full Chapters • Appendices A–H • Complete Technical Blueprint<br><br>
                <strong>Author & Solutions Architect:</strong> Team Nexora (Leader: Ranjeet Kumar)<br>
                <strong>Hackathon Track:</strong> LUMINIX'26 Innovation Initiative<br>
                <strong>Evaluated Models:</strong> 101,766 Inpatient Encounters | XGBoost 0.9794 ROC-AUC
            </div>
        </div>

        {html_content}
    </div>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Master HTML eBook generated: {html_path}")

if __name__ == "__main__":
    compile_master_ebook()
