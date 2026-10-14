# idiosync.site

GitHub Pages + Jekyll. Push to `main` = live in ~1 min. No local build needed.
Always `git pull` before starting — Shep edits and commits from his own machine.

Marketing site for **idiosync**, a Shopify email app. Same setup as
`therealheroesofecommerce.com` (`~/heroes-github`) — look there for the
pattern on anything this file doesn't cover yet.

## The product, and therefore the site

idiosync is **the most toned-down email app for Shopify** — no bells, no
whistles, nothing but the core functions you need to do email (Shep's
framing, 2026-10-13).

That pitch constrains the site, not just the copy. **A page that oversells
contradicts the product on sight.**

As of 2026-10-13 the homepage is **one letter from Shep and one text link**.
It is not a marketing page any more — the feature cards, the not-list and
the pricing panel were all deleted, because the letter argues for an app you
leave as fast as you can and a page of cards to compare would be arguing
back. Anything you want to add has to beat *nothing*, which is a higher bar
than it sounds. Concretely, the homepage has:

- one column, and one piece of art: `paper-plane.png`, left-justified at
  half the measure in the hero. Half-width is the constraint that keeps it
  a mark rather than a banner — don't let it grow.
- white page, white header. `--bg` is #ffffff, not the app's grey, so
  nothing floats on a backdrop. The header carries no fill, only a rule on
  `.bar` — inside the wrap's gutter, so it starts and stops where the
  headline does. A rule on `.site-header` would run window-wide and read as
  a toolbar; that is the thing this page is avoiding.
- one accent (`--ink`, #303030) — there is no brand colour yet and the page
  does not need one
- one typeface: **Bryndan Write**, self-hosted. See "Type" below.
- nothing animated beyond hover transitions
- exactly two things to click in the body: the header pill and the text
  link under the letter, both pointing at the same place. The link is a
  text link on purpose — a second black pill under the letter would be the
  page raising its voice the moment the writing stops.

Before adding anything to this site, ask whether the thing you're adding is
the kind of thing the product refuses to ship. If it is, don't.

## Hosting — temporary URL (2026-10-13)

The site is served from GitHub Pages at
**https://therhoe.github.io/idiosync-site/**, a *project* URL, not the
apex. The custom domain comes later.

**`CNAME` was deleted on purpose.** With a `CNAME` file present, Pages sets
the custom domain and redirects the github.io URL to `idiosync.site` — which
has no DNS yet, so the site would look dead. The file comes back the same
day DNS does.

Because it is a project URL, everything under it lives at
`/idiosync-site/`, so **all paths in `index.html` must stay relative**
(`assets/...`, `logo.png`, `./`). A leading `/` points at the top of
`therhoe.github.io` and breaks. Both absolute links that existed are now
relative.

Still pointing at the apex, correct for the final site and harmless on the
temporary one: `canonical` in `index.html`, `url:` in `_config.yml`, and
the sitemap line in `robots.txt`.

**To hook up the domain later:** restore `CNAME` containing `idiosync.site`,
point DNS at GitHub's apex A records, set the custom domain in Settings →
Pages, then tick Enforce HTTPS once it verifies.

## Type

The whole page is set in **Bryndan Write** (Shep's pick, 2026-10-13),
self-hosted at `assets/fonts/bryndan-write.woff2`. It replaced the system
stack the scaffold shipped with.

**Where it came from.** A freeware TrueType upload on FontSpace
(`bryndan-write-font-f25017`), uploaded 2016 by a pseudonymous account
("123467", elsewhere "Brynda1231 Industries"). Not on Google Fonts and not
on any CDN, which is why it is self-hosted.

**The license is unresolved, and that was a decision, not an oversight.**
The page says "Freeware" and nothing more; the bundled `info.txt` says the
same. On FontSpace that word alone grants nothing specific — other fonts
there carry "Freeware, Non-Commercial". A commercial-use question on the
page went unanswered for six years. Mirror sites contradict each other
(free for commercial / public domain / designer unknown) and the embedded
copyright is `Copyright (c) 2016, root`, the FontForge default nobody
filled in.

Shep's call, 2026-10-13: ship it, on the read that it is a hobbyist font
nobody has claimed in ten years. **Don't quietly re-open this.** If a claim
ever arrives, the swap is one `@font-face` and one `--font` line, and
Shantell Sans (Google Fonts, OFL) is the closest match — upright marker
print, same rounded monolinear feel, and it has real weights.

**It had holes, and they are patched at build time.** The shipped TTF has
no curly quotes, no em dash and no ellipsis — all three are throughout
Shep's letter, so every apostrophe would have fallen back to system sans
mid-word. `.claude/scripts/build-bryndan-woff2.py` fixes that and is the
only way this file should be regenerated:

- U+2019 → the existing `quotesingle`; U+201C/U+201D → `quotedbl`
- U+2014 → the `hyphen` outline stretched 2.2× on x (a composite can't
  scale that far — F2Dot14 tops out just under 2)
- U+2026 → a composite of three `period` glyphs
- then subset to Latin-1 + punctuation, which is what takes it from 167KB
  to 23KB. The face also carries Greek, Cyrillic, Hiragana and Katakana
  this site will never set.

The source TTF and its license file are kept beside the script. Needs
`fonttools` + `brotli`.

**One weight, no italic.** Nothing may set `font-weight` above 500 — a
heavier request gets drawn by smearing the outline sideways, which on a
drawn face looks like a printing fault. `body` sets
`font-synthesis-weight: none` so it degrades to regular instead of faking
it. The h1 is 400 and leans on scale for hierarchy. **If the page ever
needs real emphasis, it needs a second font file, not a bolder number.**

**It is wide** — wider than the system stack this page was built against.
That broke the header on narrow phones (mark + wordmark + pill overflowed
and pushed the page sideways); there's a `max-width: 420px` block that
shrinks both ends to fit. Check the header at ~320px after any header
change.

## Status (2026-10-13)

The copy is Shep's now. The scaffold's draft marketing copy is gone.

- **The letter is the page.** Replaced wholesale 2026-10-14 — the
  "we used to… now we…" letter is gone; the current one runs from "Email
  marketing is an important component of ecommerce" to "Cheers." It is
  about half the length and makes the argument straight instead of by
  lament. Shep's, kept verbatim apart
  from the typo fixes listed under Style. Don't tighten it, don't break it
  into sections, don't pull a line out as a pull-quote. The voice is the
  pitch.
- **Headline and sub are Shep's**, redlined 2026-10-13: "An
  under-complicated email service" / "We left the bells and the whistles at
  home. I don't think you'll miss them." He sent the headline in Title
  Case; it was normalized to sentence case per the Style rule below, so if
  it ever reappears capitalized that is a deliberate reversal, not a
  regression. The "we / I" shift in the sub is his and is kept verbatim.
- **No pricing anywhere.** The placeholder panel went with the rest. The
  letter doesn't name a price and the page no longer asks. When Shep
  confirms a number, that is a new decision about where it goes — not a
  matter of restoring the old panel.
- **"Install on Shopify" links go to `#install`**, a dead anchor, because
  the app has no App Store listing URL yet. Two places now (header pill,
  the link under the letter); swap both when the listing exists.
- **Two images, both line art.** `paper-plane.png` (hero, 1200px wide) and
  `logo.png` — black strokes on transparency, trimmed to the artwork. Any
  future art has to be transparent line work or it needs its own handling.
- **Logo is in.** `logo.png` (486×240, the plane without its trail) sits in
  `a.brand` at 24px tall, **with the wordmark text kept beside it** — the
  mark carries no lettering, so an image alone would take the product's
  name off the page. Sized by height to sit with the type; the heroes site
  sizes its mark by width because that one *is* the lettering. `favicon.png`
  is the same mark, centred on a 180px square with 10% padding.
- **The header pill is the one loud thing left.** A solid black button on a
  page that is otherwise a letter and an underline. Kept because it is the
  only install path above the fold; worth revisiting with Shep rather than
  quietly changing.
- **The plane appears twice** — header mark and hero drawing, the same
  artwork with and without the dashed trail. Deliberate for now; if it
  starts reading as a repeat, the hero drawing is the one to cut, not the
  mark.
- **No privacy policy.** The footer links `/privacy-policy.html`, which 404s.
  A Shopify app listing needs a working privacy URL, so this is a real gap
  before submission, not cosmetic.

## Pages

- `index.html` — homepage, and the only page. Inline `<style>` with the
  token block at the top. Sections: hero (drawing, headline, sub), the
  letter, the install link, footer.

The letter runs at a 62ch measure in `.letter` and is set a notch larger
than body copy — this is reading, not scanning. Shep's one-line beats
("Together.") are their own `<p>`, not `<br>`s, so they keep their air on a
phone.

## Design tokens

Lifted from the app UI (`~/idio UI/index.html`) so the site and the app read
as one thing: Shopify-adjacent greys, #303030 ink. The shadow and
status-colour tokens went unused when the cards and the pricing panel were
deleted, and were removed with them — pull them back off the app UI if
something ever needs them again.

**This site is light only. The page is white, everywhere, on every
machine.** (Shep's call, 2026-10-13 — stated twice; the scaffold shipped
the app's dark half with the tokens and it was wrong.) There is one `:root`
block, `<meta name="color-scheme" content="light">`, and no
`prefers-color-scheme` anywhere. Same as the heroes site.

Do not reintroduce a dark theme. The drawings are black line art on
transparency and only read on white — a dark theme needs new artwork
before it needs CSS.

## Jekyll

- `_config.yml` — `jekyll-sitemap` + `jekyll-seo-tag`. No collections yet.
- `jekyll-seo-tag` is installed but **not called**: `index.html` writes its
  own `<title>`, description and canonical. If a second page type shows up,
  a layout with `{% seo %}` is the better move — that's what the heroes site
  does for its newsletter collection.
- `index.html` carries empty front matter (`---` / `---`) so Jekyll
  processes it. Keep it, even with no Liquid in the file — drop it and the
  file ships unprocessed.
- `CNAME` → `idiosync.site` (apex). DNS has to point at GitHub's A records
  and the domain has to be set in repo Settings → Pages; the file alone is
  not enough.
- `robots.txt` points the sitemap at `https://idiosync.site/sitemap.xml`,
  generated by `jekyll-sitemap`.

## Local preview

`.claude/launch.json` runs `python -m http.server 8124` (8123 is the heroes
site, so both can run at once). That serves raw files — it does **not** run
Jekyll, so Liquid tags render as literal text. Fine while the site is static
HTML; once there are layouts or collections, use `bundle exec jekyll serve`
instead.

## Style

Normal capitalization throughout — nav items, buttons, headings
("Blasts", "Install on Shopify"). Same call as the heroes marketing pages.
Sentence case for body copy. The brand name is lowercase **idiosync**,
always, including at the start of a sentence.

Shep writes with auto-capitalizing tools and pastes copy in
inconsistently — normalizing pasted copy to the destination page's pattern
is Claude's job, every time.

**Typos in Shep's copy**: fix a missing word or a mis-capitalization that
breaks the meaning. Do NOT "fix" grammatical quirks that could be
deliberate, or creative spellings — when in doubt, keep it verbatim and
flag it instead.

What that meant for the current letter (2026-10-14), as a worked example.

Fixed: "built it" → "built in" and "some built it version" → "built-in
version" (twice — the same slip, and it inverts the sentence's meaning);
"and them move on" → "and then move on"; "distrcations" → "distractions";
"whether its" → "whether it's"; "claude or gpt" → "Claude or GPT"
(companies and products); "Idiosync" → "idiosync", twice, per the brand
rule. Straight quotes and apostrophes were curled to match the page.

Left alone, deliberately: "kinda", "barebones", "a shitty version",
"Yeah... that." as three periods rather than an ellipsis, and the capital
"DO" in "What you DO gain" — that is emphasis in Shep's voice, and caps
are the right way to carry it here because the face has one weight and
cannot go bold.

**Flagged, not fixed:** "It's kinda like the legacy software are a line of
luxury cars" — "software are" is a number disagreement, but it could be
him treating the legacy apps as a plural set. Per the rule above it was
left verbatim. If Shep wants it, "the legacy software is a line of luxury
cars" or "the legacy apps are a line of luxury cars" both work.

The earlier letter's fix list (2026-10-13) is in git history at `efde2c3`
if the old copy ever needs restoring.
