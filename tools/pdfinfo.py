import sys, fitz, pathlib
for p in sys.argv[1:]:
    d = fitz.open(p)
    txt = "".join(pg.get_text() for pg in d)
    print(f"== {pathlib.Path(p).name}: {d.page_count} pages, text chars={len(txt)}, images={sum(len(pg.get_images()) for pg in d)}")
