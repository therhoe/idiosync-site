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
- the system font stack, no webfont request — a deliberate absence, not an
  oversight. Don't add one without asking.
- nothing animated beyond hover transitions
- exactly two things to click in the body: the header pill and the text
  link under the letter, both pointing at the same place. The link is a
  text link on purpose — a second black pill under the letter would be the
  page raising its voice the moment the writing stops.

Before adding anything to this site, ask whether the thing you're adding is
the kind of thing the product refuses to ship. If it is, don't.

## Status (2026-10-13)

The copy is Shep's now. The scaffold's draft marketing copy is gone.

- **The letter is the page.** Shep's, pasted 2026-10-13, kept verbatim apart
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

What that meant for the letter (2026-10-13), as a worked example. Fixed:
"Now we like marketing toddlers" → "we're like"; "enable and automation" →
"an automation"; "conquereed" → "conquered"; "some times" → "sometimes";
"customers buttons" → "customers' buttons"; "meta" → "Meta" and "claude or
chatgpt" → "Claude or ChatGPT" (companies and products — and lowercase
"meta" reads as the adjective); "Idiosync" → "idiosync" per the brand rule.
Left alone: "koolaid", "agentic whats-its", "blast a blast", "f***", the
fragment "If I forgot something.", and the "we / I" shifts. Those are
voice.
