#!/usr/bin/env python
"""Draw assets/social-card.png -- the og:image for every page on the site.

A link preview is the one place the site shows up somewhere it does not
control, so the card is the page's own furniture and nothing else: white
ground, the hero plane, the headline in Bryndan Write, #303030 ink. No
gradient, no badge, no second colour -- a card that sells harder than the
page would be the same mistake the homepage already deleted once.

1200x630 is the size every scraper crops to (1.91:1, Facebook/LinkedIn/X).
Text sits inside a 100px margin because X and Slack round the corners and
LinkedIn trims a few pixels off the edge.

PNG not SVG: no scraper renders SVG. The plane is composited onto opaque
white here on purpose -- it is transparent line art, and X in dark mode
would otherwise draw black strokes on near-black.

Run with `python .claude/scripts/build-social-card.py` after any change to
the headline or the drawing. Needs `pillow`; draws text with the source
TTF beside this script, not the subset woff2 the page loads.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONT = Path(__file__).resolve().parent / "BryndanWriteBook-source.ttf"
W, H = 1200, 630
INK = (48, 48, 48)          # --ink, #303030. The only colour on the card.
MARGIN = 100

card = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(card)

# The plane, bottom-right, bled off the right edge so the dashed trail
# reads as motion across the card rather than as a logo parked in a corner.
# It is small and low for one reason: the trail climbs up and to the LEFT
# out of the nose, straight into the headline if the drawing is any bigger
# or any higher. Check the render after changing either.
plane = Image.open(ROOT / "paper-plane.png").convert("RGBA")
pw = 440
ph = round(plane.height * pw / plane.width)
plane = plane.resize((pw, ph), Image.LANCZOS)
card.paste(plane, (W - pw + 50, H - ph + 20), plane)

wordmark = ImageFont.truetype(str(FONT), 40)
headline = ImageFont.truetype(str(FONT), 76)

# Mark beside the wordmark, same pairing as the header: the logo carries no
# lettering, so the name has to be set.
logo = Image.open(ROOT / "logo.png").convert("RGBA")
lh = 44
lw = round(logo.width * lh / logo.height)
logo = logo.resize((lw, lh), Image.LANCZOS)
card.paste(logo, (MARGIN, MARGIN), logo)
draw.text((MARGIN + lw + 18, MARGIN + lh / 2), "idiosync",
          font=wordmark, fill=INK, anchor="lm")

# Shep's headline, wrapped by hand -- two lines, broken where he would
# pause. Measured, not guessed: the face is wide and a third line would
# collide with the plane.
for i, line in enumerate(["An under-complicated", "email service"]):
    draw.text((MARGIN, 250 + i * 92), line, font=headline, fill=INK)

out = ROOT / "assets" / "social-card.png"
card.save(out, optimize=True)
print(f"{out} {out.stat().st_size // 1024}KB")
