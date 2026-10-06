"""Render an infographic HTML file to a full-height PNG with headless Edge or Chrome.

Usage: python render_png.py <infographic.html> [output.png] [--landscape]

Pass 1 dumps the DOM to read the page height the template writes to
<body data-height>; pass 2 screenshots at that height, 2x for sharp text.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys

CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def find_browser():
    for name in ("msedge", "google-chrome", "chromium", "chromium-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    for path in CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit("No Edge or Chrome found; open the HTML in a browser and take a screenshot instead.")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mode = "landscape" if "--landscape" in sys.argv else "portrait"
    html = pathlib.Path(args[0]).resolve()
    out = pathlib.Path(args[1]).resolve() if len(args) > 1 else html.with_name(f"{html.stem}-{mode}.png")
    url = html.as_uri() + f"?still&layout={mode}"
    browser = find_browser()
    base = [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=3000"]

    wide = 1600 if mode == "landscape" else 900
    dom = subprocess.run(base + [f"--window-size={wide},1000", "--dump-dom", url], capture_output=True, text=True, encoding="utf-8").stdout
    h = re.search(r'data-height="(\d+)"', dom)
    w = re.search(r'data-width="(\d+)"', dom)
    height = int(h.group(1)) if h else 1800
    width = int(w.group(1)) if w else wide

    subprocess.run(
        base + ["--force-device-scale-factor=2", f"--window-size={width},{height}", f"--screenshot={out}", url],
        capture_output=True,
    )
    if not out.exists():
        sys.exit("Screenshot failed.")
    print(f"{out} ({mode}, {width}x{height} at 2x)")


if __name__ == "__main__":
    main()
