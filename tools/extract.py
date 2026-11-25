"""Dump text and page PNGs of every PDF under materials/ into work/ (originals untouched)."""
import fitz, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
for pdf in sorted((ROOT / "materials").rglob("*.pdf")):
    if "textbook" in pdf.parts: continue
    stem = pdf.stem.replace(" ", "_").replace(",", "")
    d = fitz.open(pdf)
    txt = []
    for i, pg in enumerate(d):
        txt.append(f"--- page {i+1} ---\n" + pg.get_text())
        out = ROOT / "work/png" / f"{stem}_p{i+1}.png"
        if not out.exists():
            pg.get_pixmap(dpi=110).save(out)
    (ROOT / "work/text" / f"{stem}.txt").write_text("\n".join(txt))
    print(stem, d.page_count)
