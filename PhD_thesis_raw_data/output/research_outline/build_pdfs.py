from pathlib import Path
from xml.sax.saxutils import escape
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('three_outline_versions.md')
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))

body = ParagraphStyle('Body', fontName='Arial', fontSize=12, leading=14.5,
                      spaceAfter=8, alignment=TA_LEFT, allowWidows=0, allowOrphans=0)
title = ParagraphStyle('Title', parent=body, fontName='Arial-Bold', leading=16,
                       spaceAfter=12)
label = ParagraphStyle('Label', parent=body, textColor=colors.HexColor('#555555'),
                       spaceAfter=7)

text = SOURCE.read_text(encoding='utf-8')
sections = re.findall(r'## Version (\d): ([^\n]+)\n\n(.*?)(?=\n## |\Z)', text, re.S)
names = ['outline_v1_balanced', 'outline_v2_gauss_maps', 'outline_v3_characteristic_cycles']

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Arial', 12)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawRightString(A4[0] - 51, 31, str(doc.page))
    canvas.restoreState()

for (number, emphasis, content), name in zip(sections, names):
    paragraphs = content.strip().split('\n\n')
    story = [Paragraph('Outline of the topic and research project', label),
             Paragraph('The geometry of subvarieties on abelian varieties', title)]
    for p in paragraphs:
        story.append(Paragraph(escape(p).replace('Z^(m)', 'Z<super>(m)</super>'), body))
    pdf_path = OUT / (name + '.pdf')
    doc = SimpleDocTemplate(str(pdf_path), pagesize=A4,
                            leftMargin=51, rightMargin=51, topMargin=48, bottomMargin=49,
                            title='Research outline - ' + emphasis,
                            author='Xiaoxiang Zhou')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    reader = PdfReader(pdf_path)
    assert 1 <= len(reader.pages) <= 2, (pdf_path, len(reader.pages))
    for page in reader.pages:
        assert page.extract_text().strip()
    print(f'{pdf_path.name}: {len(content.split())} words, {len(reader.pages)} pages')
