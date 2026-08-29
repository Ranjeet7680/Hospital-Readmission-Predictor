"""
Hospital Readmission Predictor — Complete 120-Page Master Technical & Clinical Monograph Builder
Generates a publication-grade 120-page PDF with ReportLab.
"""
import os
import sys
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "ebook_assets")
OUTPUT_PDF = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Hospital_Readmission_Predictor_Complete_eBook.pdf")

# Palette
C_PRIMARY = colors.HexColor("#002F6C")     # Deep Navy
C_SECONDARY = colors.HexColor("#005BBF")   # Medical Blue
C_ACCENT = colors.HexColor("#0EA5E9")      # Cyan Teal
C_DARK = colors.HexColor("#0F172A")        # Dark Slate Text
C_MUTED = colors.HexColor("#475569")       # Muted Grey Text
C_LIGHT_BG = colors.HexColor("#F8FAFC")    # Cool Grey Card BG
C_BORDER = colors.HexColor("#CBD5E1")      # Light Border
C_ALERT_BG = colors.HexColor("#FFFBEB")    # Amber Warning BG
C_ALERT_BORDER = colors.HexColor("#D97706")# Amber Warning Border
C_SUCCESS_BG = colors.HexColor("#F0FDF4")  # Green Callout BG
C_SUCCESS_BORDER = colors.HexColor("#16A34A")# Green Callout Border
C_CODE_BG = colors.HexColor("#0F172A")     # Code Box BG
C_CODE_TEXT = colors.HexColor("#38BDF8")   # Cyan Monospace Text
C_MATH_BG = colors.HexColor("#FAF5FF")     # Purple Math BG
C_MATH_BORDER = colors.HexColor("#9333EA") # Purple Math Border

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and stamp total page count,
    running headers, and running footers on all pages.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Cover Page: Draw uploaded cover image
            self.saveState()
            self.setFillColor(colors.HexColor("#06172E"))
            self.rect(0, 0, 612, 792, fill=1, stroke=0)
            
            cover_path = os.path.join(ASSETS_DIR, "cover_image.jpg")
            if os.path.exists(cover_path):
                # Draw high-impact cover image fitting the full page
                self.drawImage(cover_path, 0, 0, width=612, height=792, preserveAspectRatio=False)
            self.restoreState()
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(C_MUTED)

        # Running Header (Top)
        self.drawString(45, 758, "HRP CLINICAL INTELLIGENCE MONOGRAPH — LUMINIX'26 EDITION")
        self.drawRightString(567, 758, "AI & HEALTHCARE READMISSION PREDICTOR")
        
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.75)
        self.line(45, 752, 567, 752)
        
        # Running Footer (Bottom)
        self.line(45, 42, 567, 42)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_MUTED)
        self.drawString(45, 30, "Confidential • Clinical Decision Support System • Team Nexora")
        self.drawRightString(567, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def create_styles():
    base = getSampleStyleSheet()
    
    styles = {
        'CoverSuper': ParagraphStyle(
            'CoverSuper',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#38BDF8"),
            alignment=1, # Center
            spaceAfter=15
        ),
        'CoverTitle': ParagraphStyle(
            'CoverTitle',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=25,
            leading=30,
            textColor=colors.white,
            alignment=1,
            spaceAfter=12
        ),
        'CoverSubtitle': ParagraphStyle(
            'CoverSubtitle',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=13,
            leading=17,
            textColor=colors.HexColor("#93C5FD"),
            alignment=1,
            spaceAfter=25
        ),
        'CoverMeta': ParagraphStyle(
            'CoverMeta',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=9.5,
            leading=15,
            textColor=colors.HexColor("#E2E8F0"),
            alignment=1,
            spaceAfter=10
        ),
        'PartHeader': ParagraphStyle(
            'PartHeader',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=16,
            leading=20,
            textColor=C_PRIMARY,
            spaceAfter=8,
            keepWithNext=True
        ),
        'ChapterHeader': ParagraphStyle(
            'ChapterHeader',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=12.5,
            leading=16,
            textColor=C_SECONDARY,
            spaceBefore=10,
            spaceAfter=6,
            keepWithNext=True
        ),
        'SectionHeader': ParagraphStyle(
            'SectionHeader',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=10.5,
            leading=14,
            textColor=C_DARK,
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True
        ),
        'Body': ParagraphStyle(
            'Body',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8.6,
            leading=11.8,
            textColor=C_DARK,
            spaceAfter=6,
            alignment=4 # Justified
        ),
        'BodyBold': ParagraphStyle(
            'BodyBold',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=8.6,
            leading=11.8,
            textColor=C_DARK,
            spaceAfter=6
        ),
        'Bullet': ParagraphStyle(
            'Bullet',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8.4,
            leading=11.4,
            textColor=C_DARK,
            leftIndent=14,
            firstLineIndent=-9,
            spaceAfter=3
        ),
        'CalloutText': ParagraphStyle(
            'CalloutText',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8.2,
            leading=11.2,
            textColor=C_DARK
        ),
        'CodeText': ParagraphStyle(
            'CodeText',
            parent=base['Normal'],
            fontName='Courier',
            fontSize=7.5,
            leading=9.8,
            textColor=colors.HexColor("#E2E8F0")
        ),
        'TableHeader': ParagraphStyle(
            'TableHeader',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=8.2,
            leading=10.5,
            textColor=colors.white,
            alignment=0
        ),
        'TableCell': ParagraphStyle(
            'TableCell',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=7.8,
            leading=10.0,
            textColor=C_DARK,
            alignment=0
        ),
        'TableCellBold': ParagraphStyle(
            'TableCellBold',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=7.8,
            leading=10.0,
            textColor=C_DARK,
            alignment=0
        ),
        'TOCPart': ParagraphStyle(
            'TOCPart',
            parent=base['Normal'],
            fontName='Helvetica-Bold',
            fontSize=9.5,
            leading=13,
            textColor=C_PRIMARY,
            spaceBefore=5,
            spaceAfter=2
        ),
        'TOCItem': ParagraphStyle(
            'TOCItem',
            parent=base['Normal'],
            fontName='Helvetica',
            fontSize=8.2,
            leading=11.2,
            textColor=C_DARK,
            leftIndent=12,
            spaceAfter=2
        )
    }
    return styles

def make_callout(title, text, kind="alert", width=522):
    styles = create_styles()
    if kind == "alert":
        bg = C_ALERT_BG
        border_col = C_ALERT_BORDER
        icon = "⚠️ CLINICAL WARNING & GOVERNANCE: "
    elif kind == "shield":
        bg = C_SUCCESS_BG
        border_col = C_SUCCESS_BORDER
        icon = "🛡️ CLINICAL PROTOCOL & BEST PRACTICE: "
    elif kind == "math":
        bg = C_MATH_BG
        border_col = C_MATH_BORDER
        icon = "📐 MATHEMATICAL FOUNDATION: "
    else:
        bg = C_LIGHT_BG
        border_col = C_SECONDARY
        icon = "💡 ARCHITECTURE INSIGHT: "

    header_para = Paragraph(f"<b>{icon}{title}</b>", styles['CalloutText'])
    body_para = Paragraph(text, styles['CalloutText'])
    
    t = Table([[header_para], [body_para]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('BOX', (0,0), (-1,-1), 0.5, border_col),
        ('LINEBEFORE', (0,0), (0,-1), 3.5, border_col),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def make_code_box(code_str, title="SOURCE IMPLEMENTATION", width=522):
    styles = create_styles()
    lines = code_str.strip().split('\n')
    escaped_lines = [l.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;') for l in lines]
    formatted_code = "<br/>".join(escaped_lines)
    
    header_p = Paragraph(f"<b>[CODE] {title}</b>", ParagraphStyle('CHead', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=colors.HexColor("#38BDF8")))
    code_p = Paragraph(formatted_code, styles['CodeText'])
    
    t = Table([[header_p], [code_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CODE_BG),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#1E293B")),
        ('LINEBEFORE', (0,0), (0,-1), 3.0, colors.HexColor("#38BDF8")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def make_table(header_data, rows_data, col_widths=None, width=522):
    styles = create_styles()
    if col_widths is None:
        ncols = len(header_data)
        col_widths = [width / ncols] * ncols

    table_data = []
    h_row = [Paragraph(f"<b>{col}</b>", styles['TableHeader']) for col in header_data]
    table_data.append(h_row)

    for r in rows_data:
        row_cells = []
        for i, val in enumerate(r):
            if i == 0:
                row_cells.append(Paragraph(str(val), styles['TableCellBold']))
            else:
                row_cells.append(Paragraph(str(val), styles['TableCell']))
        table_data.append(row_cells)

    t = Table(table_data, colWidths=col_widths)
    ts = [
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
    ]
    for r_idx in range(1, len(table_data)):
        if r_idx % 2 == 0:
            ts.append(('BACKGROUND', (0, r_idx), (-1, r_idx), C_LIGHT_BG))
        else:
            ts.append(('BACKGROUND', (0, r_idx), (-1, r_idx), colors.white))
            
    t.setStyle(TableStyle(ts))
    return t

print("Helper definitions loaded.")
