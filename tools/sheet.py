"""Make contact sheets: tools/sheet.py OUT.png dpi cols page1.png page2.png ..."""
import sys
from PIL import Image
out, cols = sys.argv[1], int(sys.argv[2])
ims = [Image.open(p).convert("RGB") for p in sys.argv[3:]]
w = max(i.width for i in ims); h = max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (w * cols, h * rows), "white")
for k, im in enumerate(ims):
    S.paste(im, ((k % cols) * w, (k // cols) * h))
S.save(out)
print(out, S.size)
