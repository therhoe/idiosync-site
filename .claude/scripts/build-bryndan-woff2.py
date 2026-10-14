"""
Patch + subset + compress Bryndan Write for the web.

The shipped TTF has no curly quotes, em dash or ellipsis, and Shep's letter
is full of all three. Without this, every apostrophe in the letter falls back
to the system sans mid-word. So:

  U+2019 '  -> existing quotesingle glyph
  U+201C "  -> existing quotedbl glyph
  U+201D "  -> existing quotedbl glyph
  U+2014 em dash  -> new composite: the hyphen, stretched horizontally
  U+2026 ellipsis -> new composite: three periods, same as typing "..."

Nothing here invents letterforms; it reuses the designer's own marks.

Usage: python -I build_font.py <in.ttf> <out.woff2>
"""
import sys
from copy import deepcopy
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph, GlyphComponent

ARGS_ARE_XY_VALUES = 0x0002

src, dst = sys.argv[1], sys.argv[2]
f = TTFont(src)
glyf, hmtx = f["glyf"], f["hmtx"]

cmap = {}
for t in f["cmap"].tables:
    cmap.update(t.cmap)


def register(name, glyph, width):
    glyf.glyphs[name] = glyph
    hmtx.metrics[name] = (width, 0)
    f.setGlyphOrder(f.getGlyphOrder() + [name])


def add_composite(name, parts, width):
    """parts: list of (glyphName, xOffset). Identity transform only --
    a composite's scale is F2Dot14, which cannot reach 2x."""
    g = Glyph()
    g.numberOfContours = -1
    g.components = []
    for gname, xoff in parts:
        c = GlyphComponent()
        c.glyphName = gname
        c.x, c.y = xoff, 0
        c.flags = ARGS_ARE_XY_VALUES
        g.components.append(c)
    register(name, g, width)


hyphen_w = hmtx["hyphen"][0]
period_w = hmtx["period"][0]

# An em dash is nominally one em. A composite can't scale that far, so stretch
# the hyphen's own outline along x: stroke weight (vertical) is untouched and
# the designer's drawn ends are preserved -- only the bar gets longer.
EM_SCALE = 2.2
dash = deepcopy(glyf["hyphen"])
dash.expand(glyf)
if dash.numberOfContours <= 0:
    raise SystemExit("hyphen is not a simple glyph; cannot stretch it")
for i in range(len(dash.coordinates)):
    x, y = dash.coordinates[i]
    dash.coordinates[i] = (round(x * EM_SCALE), y)
dash.recalcBounds(glyf)
register("emdash", dash, round(hyphen_w * EM_SCALE))

# Three periods on their natural advance -- identical to typing "..." but as
# one glyph, so it can't break across a line.
add_composite(
    "ellipsis",
    [("period", 0), ("period", period_w), ("period", period_w * 2)],
    period_w * 3,
)

new_map = {
    0x2019: cmap[0x0027],   # ' -> '
    0x201C: cmap[0x0022],   # " -> "
    0x201D: cmap[0x0022],   # " -> "
    0x2014: "emdash",
    0x2026: "ellipsis",
}
for t in f["cmap"].tables:
    if t.isUnicode():
        t.cmap.update(new_map)

tmp = dst + ".patched.ttf"
f.save(tmp)
print("patched:", ", ".join(f"U+{c:04X}" for c in sorted(new_map)))

# Subset: the face ships Greek, Cyrillic, Hiragana and Katakana that this site
# will never set. Keeping Latin-1 plus the punctuation leaves room for copy
# changes without another build.
from fontTools import subset

keep = (
    list(range(0x20, 0x7F))
    + list(range(0xA0, 0x100))
    + [0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2022, 0x2026, 0x20AC, 0x2122]
)
opts = subset.Options()
opts.flavor = "woff2"
opts.desubroutinize = False
opts.layout_features = ["*"]
opts.notdef_outline = True
font = subset.load_font(tmp, opts)
subsetter = subset.Subsetter(options=opts)
subsetter.populate(unicodes=keep)
subsetter.subset(font)
subset.save_font(font, dst, opts)
print("wrote:", dst)
