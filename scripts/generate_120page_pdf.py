"""
Master Compiler for 120-Page Hospital Readmission Predictor Complete eBook PDF
Generates publication-grade, fully filled, rich, and detailed 120-page document.
"""
import os
import sys

# Add scripts and scripts/ebook_pages to path
SCRIPTS_DIR = os.path.dirname(__file__)
PAGES_DIR = os.path.join(SCRIPTS_DIR, "ebook_pages")
sys.path.insert(0, SCRIPTS_DIR)
sys.path.insert(0, PAGES_DIR)

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from ebook_core import NumberedCanvas, OUTPUT_PDF

from sec01_frontmatter import get_pages_001_004
from sec02_toc import get_pages_005_007
from sec03_part01_intro import get_pages_008_012
from sec04_part02_product import get_pages_004_008_part2
from sec05_part03_data import get_pages_018_023_part3
from sec06_part04_ml import get_pages_024_030_part4
from sec07_part05_dl import get_pages_031_036_part5
from sec08_part06_xai import get_pages_037_042_part6
from sec09_part07_rl import get_pages_043_048_part7
from sec10_part08_docs import get_pages_049_053_part8
from sec11_part09_telemed import get_pages_054_058_part9
from sec12_part10_healthid import get_pages_059_063_part10
from sec13_part11_auth import get_pages_064_068_part11
from sec14_part12_analytics import get_pages_069_073_part12
from sec15_part13_responsive import get_pages_074_078_part13
from sec16_part14_sound import get_pages_079_082_part14
from sec17_part15_network import get_pages_083_086_part15
from sec18_part16_arch import get_pages_087_091_part16
from sec19_part17_dev import get_pages_092_096_part17
from sec20_part18_ethics import get_pages_097_101_part18
from sec21_part19_cases import get_pages_102_107_part19
from sec22_part20_conclusion import get_pages_108_111_part20
from sec23_appendices import get_pages_112_120_appendices

def build_complete_120page_ebook():
    print("=" * 70)
    print("STARTING 120-PAGE MASTER EBOOK PDF COMPILATION")
    print("Output target:", OUTPUT_PDF)
    print("=" * 70)

    # Document Template with exact printable margins (Letter: 612 x 792 pt, margins: 45pt)
    # Printable area: Width = 522 pt, Height = 702 pt
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    story = []

    # Assemble all 23 structured sections
    sections = [
        ("Pages 1–4: Front Matter & Legal", get_pages_001_004),
        ("Pages 5–7: Table of Contents", get_pages_005_007),
        ("Pages 8–12: Part I — Introduction", get_pages_008_012),
        ("Pages 13–17: Part II — Product Blueprint", get_pages_004_008_part2),
        ("Pages 18–23: Part III — Data Engineering", get_pages_018_023_part3),
        ("Pages 24–30: Part IV — Machine Learning", get_pages_024_030_part4),
        ("Pages 31–36: Part V — Deep Learning", get_pages_031_036_part5),
        ("Pages 37–42: Part VI — Explainable AI", get_pages_037_042_part6),
        ("Pages 43–48: Part VII — Reinforcement Learning", get_pages_043_048_part7),
        ("Pages 49–53: Part VIII — Medical Documents", get_pages_049_053_part8),
        ("Pages 54–58: Part IX — Telemedicine", get_pages_054_058_part9),
        ("Pages 59–63: Part X — Digital Health ID", get_pages_059_063_part10),
        ("Pages 64–68: Part XI — Healthcare Security & RBAC", get_pages_064_068_part11),
        ("Pages 69–73: Part XII — Clinical Analytics", get_pages_069_073_part12),
        ("Pages 74–78: Part XIII — Responsive UI/UX", get_pages_074_078_part13),
        ("Pages 79–82: Part XIV — Clinical Audio Engineering", get_pages_079_082_part14),
        ("Pages 83–86: Part XV — Network Resilience", get_pages_083_086_part15),
        ("Pages 87–91: Part XVI — Microservices Architecture", get_pages_087_091_part16),
        ("Pages 92–96: Part XVII — Developer Guide & SDK", get_pages_092_096_part17),
        ("Pages 97–101: Part XVIII — Bioethics & Governance", get_pages_097_101_part18),
        ("Pages 102–107: Part XIX — Clinical Case Studies", get_pages_102_107_part19),
        ("Pages 108–111: Part XX — Future Horizons & 2030", get_pages_108_111_part20),
        ("Pages 112–120: Appendices A through H", get_pages_112_120_appendices),
    ]

    for label, func in sections:
        print(f"Loading: {label}...")
        elements = func()
        story.extend(elements)

    print("\nCompiling PDF via ReportLab NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Compilation finished: {OUTPUT_PDF}")

    # Validate with PyMuPDF
    import fitz
    doc_fitz = fitz.open(OUTPUT_PDF)
    total_pages = len(doc_fitz)
    print(f"\nVALIDATION CHECK: Total Pages Generated = {total_pages}")
    
    if total_pages == 120:
        print(">>> SUCCESS: Exact 120 pages achieved perfectly!")
    else:
        print(f">>> PAGE COUNT NOTICE: Generated {total_pages} pages (Target: 120)")

if __name__ == '__main__':
    build_complete_120page_ebook()
