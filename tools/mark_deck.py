#!/usr/bin/env python3
"""Make a copy of the @math161nu deck with the slides that are NOT on Exam 2 marked in red.

Out-of-scope slides come from data/problems.json (paper deck-nu, out_of_scope=True),
so the marks always agree with the site.

    .venv/bin/python -I tools/mark_deck.py
"""
import json
import pathlib
import re

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Pt

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "materials/telegram/MATH161_All_Sections/MATH161 Chapters 4,5,7.pptx"
OUT = ROOT / "materials/marked/MATH161 Chapters 4,5,7 (marked for Exam 2).pptx"

RED = RGBColor(0xC6, 0x28, 0x28)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

WHY = {
    "4.3": "§4.3: асимптоты, графики рациональных функций, касп",
    "6.1": "§6.1: площадь между кривыми",
}


def out_of_scope_slides():
    probs = json.loads((ROOT / "data/problems.json").read_text())
    res = {}
    for p in probs:
        if p["paper"] == "deck-nu" and p.get("out_of_scope"):
            res[int(re.match(r"\d+", p["number"]).group())] = p["section"]
    return dict(sorted(res.items()))


def box(slide, left, top, width, height, fill, text, size, bold=True, color=WHITE, align=PP_ALIGN.CENTER):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Emu(left), Emu(top), Emu(width), Emu(height))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.shadow.inherit = False
    tf = shp.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    lines = text.split("\n")
    for i, line in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        r = para.add_run()
        r.text = line
        r.font.size = Pt(size if i == 0 else size * 0.7)
        r.font.bold = bold if i == 0 else False
        r.font.color.rgb = color
    return shp


def frame(slide, W, H, color, width_pt=10):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Emu(W), Emu(H))
    shp.fill.background()
    shp.line.color.rgb = color
    shp.line.width = Pt(width_pt)
    shp.shadow.inherit = False


def add_note(paragraph, text, color):
    r = paragraph.add_run()
    r.text = text
    r.font.color.rgb = color
    r.font.bold = True
    if paragraph.runs and paragraph.runs[0].font.size:
        r.font.size = paragraph.runs[0].font.size


def main():
    oos = out_of_scope_slides()
    pr = Presentation(str(SRC))
    W, H = pr.slide_width, pr.slide_height
    slides = list(pr.slides)

    # slide 1: legend
    box(slides[0], int(W * 0.08), int(H * 0.70), int(W * 0.84), int(H * 0.25), RED,
        "Красные слайды НЕ будут на Exam 2 (сб, 28 ноября): пропускай их",
        22)
    s = ", ".join(str(n) for n in oos)
    slides[0].shapes[-1].text_frame.add_paragraph()
    p = slides[0].shapes[-1].text_frame.paragraphs[-1]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = f"Слайды {s}: темы §4.3 и §6.1 не входят в экзамен (на экзамене: глава 4 без 4.3/4.7, глава 5, §7.2–7.3)."
    r.font.size = Pt(14)
    r.font.color.rgb = WHITE

    # slides 2 and 3: tag the topic lines
    marks = {
        "Graph Sketching": ("  ✗ §4.3 не на экзамене (только графики многочленов, §4.2)", RED),
        "Area problems": ("  ✗ §6.1 площадь между кривыми: не на экзамене", RED),
        "Integral evaluation by parts": ("  ✓ §7.2: на экзамене", GREEN),
    }
    for sl in slides[1:3]:
        for shp in sl.shapes:
            if not shp.has_text_frame:
                continue
            for para in shp.text_frame.paragraphs:
                t = "".join(r.text for r in para.runs)
                for key, (note, col) in marks.items():
                    if t.strip().startswith(key):
                        add_note(para, note, col)

    # the out-of-scope problem slides
    for n, sec in oos.items():
        sl = slides[n - 1]
        frame(sl, W, H, RED)
        box(sl, int(W * 0.05), int(H * 0.035), int(W * 0.90), int(H * 0.15), RED,
            "✗ НЕ БУДЕТ НА EXAM 2: пропускай этот слайд\n" + WHY.get(sec, "§" + sec) + " (не входит в экзамен)",
            28)

    # slide 99 repeats slide 98
    if len(slides) >= 99:
        box(slides[98], int(W * 0.2), int(H * 0.035), int(W * 0.6), int(H * 0.09), RGBColor(0x60, 0x60, 0x60),
            "Та же задача, что на слайде 98", 20)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pr.save(str(OUT))
    print("marked", len(oos), "slides:", list(oos), "->", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
