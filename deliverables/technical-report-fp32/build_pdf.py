#!/usr/bin/env python3
"""Render report.md to report.pdf with reportlab (no LaTeX/pandoc needed).
Supports the Markdown subset used in the report: #/##/### headings, paragraphs,
bullet/numbered lists, pipe tables, fenced code, **bold**, *italic*, `code`, links.
    pip install reportlab && python3 build_pdf.py
"""
import re, sys, pathlib
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, ListFlowable, ListItem, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = pathlib.Path(__file__).parent
SRC = HERE / 'report.md'; OUT = HERE / 'report.pdf'
FD = pathlib.Path('/usr/share/fonts/truetype/dejavu')
for name, f in [('Serif', 'DejaVuSerif.ttf'), ('Serif-Bold', 'DejaVuSerif-Bold.ttf'), ('Sans', 'DejaVuSans.ttf'), ('Sans-Bold', 'DejaVuSans-Bold.ttf'), ('Mono', 'DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FD / f)))
pdfmetrics.registerFontFamily('Serif', normal='Serif', bold='Serif-Bold', italic='Serif', boldItalic='Serif-Bold')

S = {
    'title': ParagraphStyle('t', fontName='Sans-Bold', fontSize=17, leading=22, spaceAfter=6, alignment=1),
    'meta': ParagraphStyle('m', fontName='Serif', fontSize=9.5, leading=13, alignment=1, textColor=colors.HexColor('#333333'), spaceAfter=3),
    'h2': ParagraphStyle('h2', fontName='Sans-Bold', fontSize=12.5, leading=16, spaceBefore=12, spaceAfter=4),
    'h3': ParagraphStyle('h3', fontName='Sans-Bold', fontSize=10.5, leading=14, spaceBefore=8, spaceAfter=2),
    'p': ParagraphStyle('p', fontName='Serif', fontSize=9.8, leading=13.6, spaceAfter=5, alignment=4),
    'abs': ParagraphStyle('abs', fontName='Serif', fontSize=9.2, leading=12.6, leftIndent=10*mm, rightIndent=10*mm, spaceAfter=5, alignment=4),
    'li': ParagraphStyle('li', fontName='Serif', fontSize=9.8, leading=13.4, spaceAfter=2),
    'cell': ParagraphStyle('c', fontName='Serif', fontSize=8.6, leading=11),
    'code': ParagraphStyle('code', fontName='Mono', fontSize=8, leading=10, backColor=colors.HexColor('#f4f4f4'), borderPadding=4, leftIndent=4, spaceBefore=3, spaceAfter=7),
    'foot': ParagraphStyle('f', fontName='Serif', fontSize=8.5, leading=11, textColor=colors.HexColor('#444444')),
}

def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'`([^`]+)`', r'<font face="Mono" size="8.6">\1</font>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<![*\w])\*([^*]+)\*(?!\w)', r'<i>\1</i>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" color="#1a4f9c">\1</a>', t)
    t = re.sub(r'(?<![">])(https?://[^\s<]+)', r'<a href="\1" color="#1a4f9c">\1</a>', t)
    return t

def build():
    lines = SRC.read_text(encoding='utf-8').split('\n')
    story, i, in_abstract = [], 0, False
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('# '):
            story.append(Paragraph(inline(ln[2:]), S['title'])); i += 1
            while i < len(lines) and not lines[i].strip(): i += 1
            while i < len(lines) and lines[i].strip():          # author/meta block
                story.append(Paragraph(inline(lines[i]), S['meta'])); i += 1
            story.append(HRFlowable(width='100%', thickness=0.6, color=colors.grey, spaceBefore=6, spaceAfter=6)); continue
        if ln.startswith('## '):
            in_abstract = ln[3:].strip().lower() == 'abstract'
            story.append(Paragraph(inline(ln[3:]), S['h2'])); i += 1; continue
        if ln.startswith('### '):
            story.append(Paragraph(inline(ln[4:]), S['h3'])); i += 1; continue
        if ln.startswith('```'):
            buf = []; i += 1
            while i < len(lines) and not lines[i].startswith('```'): buf.append(lines[i]); i += 1
            story.append(Preformatted('\n'.join(buf), S['code'])); i += 1; continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells): rows.append(cells)
                i += 1
            data = [[Paragraph(inline(c), S['cell']) for c in r] for r in rows]
            t = Table(data, repeatRows=1, hAlign='LEFT')
            t.setStyle(TableStyle([('FONT', (0, 0), (-1, 0), 'Sans-Bold'), ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e8e8e8')),
                ('LINEBELOW', (0, 0), (-1, 0), 0.8, colors.black), ('LINEBELOW', (0, -1), (-1, -1), 0.5, colors.black),
                ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#bbbbbb')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
            story += [t, Spacer(1, 6)]; continue
        if re.match(r'^(\*|\d+\.)\s', ln):
            items, numbered = [], ln[0].isdigit()
            while i < len(lines) and re.match(r'^(\*|\d+\.)\s', lines[i]):
                txt = re.sub(r'^(\*|\d+\.)\s+', '', lines[i]); i += 1
                while i < len(lines) and lines[i].startswith('   ') and lines[i].strip(): txt += ' ' + lines[i].strip(); i += 1
                items.append(ListItem(Paragraph(inline(txt), S['li']), leftIndent=14))
            story.append(ListFlowable(items, bulletType='1' if numbered else 'bullet', start='1' if numbered else None, bulletFormat='%s.' if numbered else None, leftIndent=14, bulletFontName='Serif', bulletFontSize=9)); story.append(Spacer(1, 4)); continue
        if ln.strip() == '---':
            story.append(HRFlowable(width='100%', thickness=0.5, color=colors.grey, spaceBefore=8, spaceAfter=4)); i += 1; continue
        if not ln.strip(): i += 1; continue
        para = [ln]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|\*\s|\d+\.\s|---)', lines[i]): para.append(lines[i]); i += 1
        text = ' '.join(para)
        style = S['abs'] if in_abstract else (S['foot'] if text.startswith('*Licence') else S['p'])
        story.append(Paragraph(inline(text), style))
    def footer(canvas, doc):
        canvas.saveState(); canvas.setFont('Serif', 8); canvas.setFillColor(colors.grey)
        canvas.drawCentredString(A4[0] / 2, 12 * mm, f'S. Amouzadeh — Bit-exact binary32 arithmetic model — Technical Report v1.0 — page {doc.page}')
        canvas.restoreState()
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=20*mm, bottomMargin=20*mm,
                            title='Bit-Exact Software Modelling of IEEE 754 binary32 Arithmetic', author='Shayan Amouzadeh', subject='Technical report')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print('written', OUT, OUT.stat().st_size, 'bytes')

if __name__ == '__main__':
    build()
