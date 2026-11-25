"""Print slide titles/text of .pptx files (zip + XML, no extra deps)."""
import re, sys, zipfile, html
for path in sys.argv[1:]:
    z = zipfile.ZipFile(path)
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)], key=lambda n: int(re.findall(r"\d+", n)[0]))
    print(f"##### {path.split('/')[-1]}: {len(slides)} slides")
    for n in slides:
        xml = z.read(n).decode("utf8", "ignore")
        paras = []
        for p in re.findall(r"<a:p>.*?</a:p>", xml, flags=re.S):
            t = "".join(re.findall(r"<a:t>(.*?)</a:t>", p, flags=re.S))
            if t.strip(): paras.append(html.unescape(t.strip()))
        num = re.findall(r"\d+", n)[0]
        print(f"[{num}] " + " | ".join(paras)[:220])
