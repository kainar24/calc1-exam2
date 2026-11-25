#!/usr/bin/env python3
"""Render .pptx slides to PNG without PowerPoint/Keynote.

Text boxes are drawn with PIL; pictures (and the PNG fallbacks that PowerPoint stores
for equations) are pasted at their positions. Good enough to read lecture slides.

    .venv/bin/python -I tools/render_pptx.py OUT_DIR file.pptx [...]
"""
import io
import pathlib
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
}
RID = "{%s}embed" % NS["r"]
WIDTH = 1600
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def q(tag):
    p, t = tag.split(":")
    return "{%s}%s" % (NS[p], t)


class Renderer:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        pres = ET.fromstring(self.z.read("ppt/presentation.xml"))
        sz = pres.find(q("p:sldSz"))
        self.cx, self.cy = int(sz.get("cx")), int(sz.get("cy"))
        self.s = WIDTH / self.cx
        self.fonts = {}

    def font(self, px, bold=False):
        key = (max(8, int(px)), bold)
        if key not in self.fonts:
            try:
                self.fonts[key] = ImageFont.truetype(FONT_B if bold else FONT, key[0])
            except OSError:
                self.fonts[key] = ImageFont.load_default()
        return self.fonts[key]

    def slides(self):
        names = [n for n in self.z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        return sorted(names, key=lambda n: int(re.findall(r"\d+", n)[0]))

    def rels(self, slide):
        rp = slide.replace("slides/", "slides/_rels/") + ".rels"
        out = {}
        if rp in self.z.namelist():
            for r in ET.fromstring(self.z.read(rp)):
                out[r.get("Id")] = r.get("Target")
        return out

    def image(self, target):
        path = "ppt/" + target.replace("../", "")
        try:
            return Image.open(io.BytesIO(self.z.read(path))).convert("RGBA")
        except Exception:
            return None

    def render(self, slide):
        img = Image.new("RGB", (WIDTH, int(self.cy * self.s)), "white")
        d = ImageDraw.Draw(img)
        rels = self.rels(slide)
        root = ET.fromstring(self.z.read(slide))
        tree = root.find(".//" + q("p:spTree"))
        self.walk(tree, img, d, rels, (0, 0, 1, 1))
        return img

    def xf(self, el):
        x = el.find(".//" + q("a:off")); e = el.find(".//" + q("a:ext"))
        if x is None or e is None:
            return None
        return int(x.get("x")), int(x.get("y")), int(e.get("cx")), int(e.get("cy"))

    def walk(self, node, img, d, rels, tr):
        ox, oy, sx, sy = tr
        for ch in list(node):
            tag = ch.tag
            if tag == q("mc:AlternateContent"):
                fb = ch.find(q("mc:Fallback"))
                if fb is not None:
                    self.walk(fb, img, d, rels, tr)
                continue
            if tag == q("p:grpSp"):
                g = ch.find(q("p:grpSpPr")).find(q("a:xfrm"))
                if g is None:
                    self.walk(ch, img, d, rels, tr); continue
                off, ext = g.find(q("a:off")), g.find(q("a:ext"))
                coff, cext = g.find(q("a:chOff")), g.find(q("a:chExt"))
                gx, gy, gw, gh = int(off.get("x")), int(off.get("y")), int(ext.get("cx")), int(ext.get("cy"))
                cx_, cy_, cw, chh = int(coff.get("x")), int(coff.get("y")), int(cext.get("cx")) or 1, int(cext.get("cy")) or 1
                nsx, nsy = sx * gw / cw, sy * gh / chh
                self.walk(ch, img, d, rels, (ox + sx * gx - nsx * cx_, oy + sy * gy - nsy * cy_, nsx, nsy))
                continue
            if tag not in (q("p:sp"), q("p:pic"), q("p:cxnSp")):
                continue
            spPr = ch.find(q("p:spPr"))
            box = self.xf(spPr) if spPr is not None else None
            if box is None:
                continue
            X = (ox + sx * box[0]) * self.s; Y = (oy + sy * box[1]) * self.s
            W = sx * box[2] * self.s; H = sy * box[3] * self.s
            blip = ch.find(".//" + q("a:blip"))
            if blip is not None and blip.get(RID) in rels:
                im = self.image(rels[blip.get(RID)])
                if im is not None and W > 2 and H > 2:
                    im = im.resize((max(1, int(W)), max(1, int(H))))
                    img.paste(im, (int(X), int(Y)), im)
            tx = ch.find(q("p:txBody"))
            if tx is not None:
                self.text(tx, d, X, Y, W, H)

    def text(self, tx, d, X, Y, W, H):
        y = Y + 4
        for para in tx.findall(q("a:p")):
            runs = []
            for r in para:
                if r.tag == q("a:r"):
                    t = r.find(q("a:t")); rp = r.find(q("a:rPr"))
                    sz = int(rp.get("sz")) if rp is not None and rp.get("sz") else 2000
                    bold = rp is not None and rp.get("b") == "1"
                    col = rp.find(".//" + q("a:srgbClr")) if rp is not None else None
                    runs.append((t.text or "", sz, bold, "#" + col.get("val") if col is not None else "#111111"))
                elif r.tag == q("a:br"):
                    runs.append(("\n", 2000, False, "#111"))
            if not runs:
                y += 14
                continue
            sz = max(r[1] for r in runs)
            px = sz / 100 * 12700 * self.s
            x = X + 6
            line_h = px * 1.25
            for txt, rsz, bold, col in runs:
                f = self.font(rsz / 100 * 12700 * self.s, bold)
                for word in re.split(r"(\s+)", txt):
                    if word == "\n":
                        x = X + 6; y += line_h; continue
                    wlen = d.textlength(word, font=f)
                    if x + wlen > X + W and x > X + 6 and word.strip():
                        x = X + 6; y += line_h
                    d.text((x, y), word, font=f, fill=col)
                    x += wlen
            y += line_h


def main():
    out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for path in sys.argv[2:]:
        r = Renderer(path)
        stem = pathlib.Path(path).stem.replace(" ", "")
        for i, s in enumerate(r.slides(), 1):
            r.render(s).save(out / f"{stem}_s{i:02d}.png", optimize=True)
        print(stem, len(r.slides()), "slides")


if __name__ == "__main__":
    main()
