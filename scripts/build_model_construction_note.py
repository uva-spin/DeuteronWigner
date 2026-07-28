#!/usr/bin/env python3
"""Build the superseded short-form model summary for historical comparison."""

from __future__ import annotations

import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "references" / "model_construction_note.md"
OUTPUT = ROOT / "output" / "pdf" / "model_construction_note_legacy_summary.pdf"


def register_fonts() -> tuple[str, str, str, str]:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    faces = {
        "NoteSans": font_dir / "Arial.ttf",
        "NoteSansBold": font_dir / "Arial Bold.ttf",
        "NoteSerif": font_dir / "Times New Roman.ttf",
        "NoteMono": font_dir / "Courier New.ttf",
    }
    for name, path in faces.items():
        pdfmetrics.registerFont(TTFont(name, str(path)))
    return tuple(faces)


SANS, SANS_BOLD, SERIF, MONO = register_fonts()


def inline(text: str) -> str:
    """Convert a conservative Markdown subset to ReportLab paragraph markup."""
    text = text.replace("–", "-").replace("—", "-").replace("−", "-")
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="NoteMono" size="7.7">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


def make_styles():
    base = getSampleStyleSheet()
    navy = colors.HexColor("#17324D")
    teal = colors.HexColor("#147D92")
    ink = colors.HexColor("#202A33")
    muted = colors.HexColor("#5C6A73")
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName=SANS_BOLD,
            fontSize=24,
            leading=28,
            alignment=TA_LEFT,
            textColor=navy,
            spaceAfter=16,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=12,
            leading=17,
            textColor=muted,
            spaceAfter=10,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName=SANS_BOLD,
            fontSize=15,
            leading=18,
            textColor=navy,
            spaceBefore=15,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName=SANS_BOLD,
            fontSize=11.3,
            leading=14,
            textColor=teal,
            spaceBefore=11,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=9.3,
            leading=12.7,
            textColor=ink,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=9.1,
            leading=12.2,
            textColor=ink,
            leftIndent=15,
            firstLineIndent=0,
            spaceAfter=2.5,
        ),
        "formula": ParagraphStyle(
            "Formula",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=9.3,
            leading=13,
            alignment=TA_CENTER,
            textColor=navy,
            leftIndent=20,
            rightIndent=20,
            spaceBefore=4,
            spaceAfter=7,
        ),
        "code": ParagraphStyle(
            "Code",
            parent=base["Code"],
            fontName=MONO,
            fontSize=7.2,
            leading=9.3,
            leftIndent=9,
            rightIndent=7,
            borderColor=colors.HexColor("#CAD6DF"),
            borderWidth=0.5,
            borderPadding=6,
            backColor=colors.HexColor("#F4F7F9"),
            textColor=ink,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "table": ParagraphStyle(
            "Table",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=7.2,
            leading=9.1,
            textColor=ink,
        ),
        "table_head": ParagraphStyle(
            "TableHead",
            parent=base["BodyText"],
            fontName=SANS_BOLD,
            fontSize=7.2,
            leading=9,
            textColor=colors.white,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName=SANS,
            fontSize=7.5,
            leading=9.5,
            textColor=muted,
        ),
        "cover": ParagraphStyle(
            "Cover",
            parent=base["BodyText"],
            fontName=SERIF,
            fontSize=11,
            leading=16,
            textColor=ink,
            spaceAfter=8,
        ),
    }


STYLES = make_styles()


def parse_table(lines: list[str], start: int):
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
        rows.append(cells)
        i += 1
    if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", c) for c in rows[1]):
        rows.pop(1)
    return rows, i


def table_flowable(rows: list[list[str]]):
    ncols = max(len(row) for row in rows)
    normalized = [row + [""] * (ncols - len(row)) for row in rows]
    cooked = []
    for ridx, row in enumerate(normalized):
        style = STYLES["table_head"] if ridx == 0 else STYLES["table"]
        cooked.append([Paragraph(inline(cell), style) for cell in row])
    usable = 7.15 * inch
    if ncols == 2:
        widths = [usable * 0.28, usable * 0.72]
    elif ncols == 3:
        widths = [usable * 0.20, usable * 0.36, usable * 0.44]
    else:
        widths = [usable / ncols] * ncols
    table = Table(cooked, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9C6CF")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F7F9")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def story_from_markdown(text: str):
    lines = text.splitlines()
    story = []
    paragraph = []
    bullets = []
    in_code = False
    code = []
    in_formula = False
    formula = []

    def flush_paragraph():
        if paragraph:
            story.append(Paragraph(inline(" ".join(x.strip() for x in paragraph)), STYLES["body"]))
            paragraph.clear()

    def flush_bullets():
        if bullets:
            items = [
                ListItem(Paragraph(inline(item), STYLES["bullet"]), leftIndent=9)
                for item in bullets
            ]
            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    start="circle",
                    bulletFontName=SANS,
                    bulletFontSize=6,
                    leftIndent=17,
                    bulletColor=colors.HexColor("#147D92"),
                    spaceAfter=5,
                )
            )
            bullets.clear()

    i = 0
    first = True
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped == "```":
            flush_paragraph()
            flush_bullets()
            if in_code:
                story.append(Paragraph("<br/>".join(inline(x) for x in code), STYLES["code"]))
                code.clear()
            in_code = not in_code
            i += 1
            continue
        if in_code:
            code.append(line)
            i += 1
            continue
        if stripped == r"\[":
            flush_paragraph()
            flush_bullets()
            in_formula = True
            i += 1
            continue
        if stripped == r"\]":
            story.append(Paragraph(inline(" ".join(formula)), STYLES["formula"]))
            formula.clear()
            in_formula = False
            i += 1
            continue
        if in_formula:
            formula.append(stripped)
            i += 1
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            flush_bullets()
            rows, i = parse_table(lines, i)
            story.extend([Spacer(1, 3), table_flowable(rows), Spacer(1, 7)])
            continue
        if stripped.startswith("# "):
            flush_paragraph()
            flush_bullets()
            if first:
                story.append(Spacer(1, 0.5 * inch))
                story.append(Paragraph(inline(stripped[2:]), STYLES["title"]))
                story.append(
                    Table(
                        [[""]],
                        colWidths=[1.6 * inch],
                        rowHeights=[0.06 * inch],
                        style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E08B3E"))]),
                    )
                )
                story.append(Spacer(1, 15))
                cover_box = Table(
                    [
                        [
                            Paragraph(
                                "<b>Scientific scope</b><br/>"
                                "A provenance-backed account of the complete leading-twist "
                                "forward quark, antiquark, and gluon boundary at Q = 5 GeV: "
                                "its GTMD parent, flavor and spin content, deuteron dynamics, "
                                "gauge links, OAM, nuclear mechanisms, uncertainties, "
                                "validation, refocusing history, and remaining model dependence.",
                                STYLES["cover"],
                            )
                        ]
                    ],
                    colWidths=[6.45 * inch],
                    style=TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F6F8")),
                            ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#B9CBD5")),
                            ("LEFTPADDING", (0, 0), (-1, -1), 15),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 15),
                            ("TOPPADDING", (0, 0), (-1, -1), 13),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
                        ]
                    ),
                )
                story.append(cover_box)
                story.append(Spacer(1, 16))
                story.append(
                    Paragraph(
                        "<b>Core result</b><br/>"
                        "The original GTMD-first architecture is retained. The accepted "
                        "implementation now resolves u, d, anti-u, anti-d, proton, neutron, "
                        "spin-1 vector/tensor sectors, and gluon f/d link-color channels. "
                        "All 36 declared projections pass the pre-evolution evidence gate.",
                        STYLES["cover"],
                    )
                )
                first = False
            i += 1
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            flush_bullets()
            title = stripped[3:]
            if title.startswith("1. "):
                story.append(PageBreak())
            story.append(Paragraph(inline(title), STYLES["h1"]))
            i += 1
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            flush_bullets()
            story.append(Paragraph(inline(stripped[4:]), STYLES["h2"]))
            i += 1
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            bullets.append(stripped[2:])
            i += 1
            continue
        if re.match(r"^\d+\. ", stripped):
            flush_paragraph()
            bullets.append(stripped)
            i += 1
            continue
        if not stripped:
            flush_paragraph()
            flush_bullets()
            i += 1
            continue
        if stripped.startswith("**") and stripped.endswith("  "):
            flush_paragraph()
            story.append(Paragraph(inline(stripped), STYLES["subtitle"]))
            i += 1
            continue
        paragraph.append(stripped)
        i += 1
    flush_paragraph()
    flush_bullets()
    return story


def page_header_footer(canvas, doc):
    canvas.saveState()
    width, height = letter
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#D6DFE5"))
        canvas.setLineWidth(0.5)
        canvas.line(0.7 * inch, height - 0.54 * inch, width - 0.7 * inch, height - 0.54 * inch)
        canvas.setFont(SANS, 7.2)
        canvas.setFillColor(colors.HexColor("#64737D"))
        canvas.drawString(0.7 * inch, height - 0.42 * inch, "CANONICAL SPIN-1 DEUTERON GTMD/TMD MODEL")
        canvas.drawRightString(width - 0.7 * inch, 0.42 * inch, f"{doc.page}")
        canvas.drawString(0.7 * inch, 0.42 * inch, "Pre-evolution construction note - 2026-07-27")
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    text = SOURCE.read_text(encoding="utf-8")
    story = story_from_markdown(text)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        rightMargin=0.68 * inch,
        leftMargin=0.68 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.65 * inch,
        title="Construction of the canonical spin-1 deuteron GTMD/TMD model",
        author="DeuteronWigner project",
        subject="Scientific provenance and implementation note",
    )
    doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
