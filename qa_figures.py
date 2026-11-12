#!/usr/bin/env python3
"""QA helper: render every illustration in a chapter to PNG sheets for visual review.

    python3 qa_figures.py <slug> [per_sheet]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
slug = sys.argv[1]
per = int(sys.argv[2]) if len(sys.argv) > 2 else 4
html = (ROOT / "content" / f"{slug}.html").read_text(encoding="utf-8")
figs = re.findall(r'<figure class="illus">.*?</figure>', html, flags=re.S)
outdir = Path("/tmp/qa") / slug
outdir.mkdir(parents=True, exist_ok=True)
css = (ROOT / "assets" / "style.css").as_uri()
sheets = []
for i in range(0, len(figs), per):
    chunk = figs[i:i + per]
    page = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{css}">'
            '<style>body{padding:10px;font-size:15px} .illus{margin:6px 0;padding:8px} .illus svg{min-width:0}'
            ' .grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}</style></head><body><div class="grid">'
            + "".join(chunk) + "</div></body></html>")
    f = outdir / f"sheet{i // per + 1}.html"
    f.write_text(page, encoding="utf-8")
    png = outdir / f"sheet{i // per + 1}.png"
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=1400,1100", f"--screenshot={png}", f.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    sheets.append(str(png))
print(f"{len(figs)} figures → {len(sheets)} sheets")
print("\n".join(sheets))
