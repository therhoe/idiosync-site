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
- **one text colour, site-wide** (Shep's call, 2026-10-14). #303030, with
  no muted grey anywhere. `--text-sub` and `--text-dim` are gone, not
  merely unused — the hero sub, the signoff and the footer were all lighter
  and are not now. The only other text colour on the page is the white
  inside the black header pill, which has to stay legible. If something
  needs to recede, it recedes by size or position, never by going grey.
- **the headline and the body are one block, not two.** The sub under the
  headline is the letter's opening line: same ink, same 62ch measure, and
  one paragraph space (22px) between it and the first `.letter p` — the
  same gap the paragraphs have with each other. It used to be 72px, which
  read as a section break between two separate things. `.letter` has no
  mobile padding override for the same reason. Don't put the air back.
- one typeface: **Bryndan Write**, self-hosted. See "Type" below.
- nothing animated beyond hover transitions
- exactly two things to click in the body: the header pill and the text
  link under the letter, both pointing at the same place. The link is a
  text link on purpose — a second black pill under the letter would be the
  page raising its voice the moment the writing stops.

Before adding anything to this site, ask whether the thing you're adding is
the kind of thing the product refuses to ship. If it is, don't.

## Hosting — live on the apex (2026-10-23)

The site is served from GitHub Pages at **https://idiosync.site**, the
apex. The temporary project URL,
`https://therhoe.github.io/idiosync-site/`, still answers and is not worth
removing.

**DNS is at Hostinger**, on its own nameservers (`atlas.dns-parking.com`,
`hyperion.dns-parking.com`) — the domain was never moved to another
registrar, only repointed. The zone is:

- `@` → GitHub's four apex A records, `185.199.108.153` through
  `185.199.111.153`. All four; one is a single point of failure.
- `www` → CNAME to `therhoe.github.io` (not to the apex, and never to a
  path — a CNAME points at a host). Pages 301s `www` to the apex itself.
- nothing else. No MX, no TXT, no CAA. Hostinger's own parking records —
  an `@` A record at `2.57.91.91` and a `www` CNAME to the apex — were
  deleted, not left alongside; a leftover `@` A record would have split
  traffic between Hostinger and GitHub at random.

Zone TTL is 600s, so a DNS change here shows up in about ten minutes.

**Don't press "Reset to Hostinger defaults"** in hPanel's DNS editor, and
if `idiosync.site` ever appears under hPanel → Websites, disconnect it —
a website connection can silently re-add the parking records over these.

**`CNAME` is back** (committed by GitHub itself, `6f95b37`, when the custom
domain was saved in Settings → Pages). It contains `idiosync.site`.
Deleting it hands the site back to the project URL and breaks every link
anyone has.

**Paths in the HTML are still relative** (`assets/...`, `logo.png`, `./`).
On the apex a leading `/` would now work, so this is no longer load-bearing
— but relative paths are what keep the project URL working as a fallback,
and there's no reason to churn them.

`canonical` in both HTML files, `url:` in `_config.yml` and the sitemap
line in `robots.txt` all point at the apex, and now match reality.

## Type

The site is set in **Bryndan Write** (Shep's pick, 2026-10-13),
self-hosted at `assets/fonts/bryndan-write.woff2`. It replaced the system
stack the scaffold shipped with.

**One exception, as of 2026-10-23:** the calculator panels on
`pricing.html` are in a system sans. See the Pricing section for why and
for where exactly the boundary sits. Everything else — every page, all
the chrome, both other pages entirely — is Bryndan.

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
- **Pricing is on its own page, not the homepage** (2026-10-23). The old
  placeholder panel went with the cards and did not come back; what came
  back instead is a real calculator on `pricing.html`. The letter still
  doesn't name a price and the homepage still doesn't ask — that was the
  point of deleting the panel, and it survives.
- **"Install on Shopify" links go to `#install`**, a dead anchor, because
  the app has no App Store listing URL yet. Four places now (header pill,
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

- `index.html` — homepage. Inline `<style>` with the token block at the
  top. Sections: hero (drawing, headline, sub), the letter, the install
  link, footer.
- `templates.html` — "A little inspo" (2026-10-14). Six example emails,
  each with a *Copy prompt* button. See below. The **file name stays
  `templates.html`** even though the page is no longer called that — the
  URL is accurate either way and renaming it would break the link the day
  anyone shares it.
- `pricing.html` — "One-size-fits-noone" (2026-10-23). The credit
  calculator, rebuilt from the one in the Shopify app. See below.
- `templates/*.html` — the six emails themselves, one file each. **No
  front matter, on purpose**: a file without it is a Jekyll static file,
  copied verbatim. Add front matter and Liquid eats every `{{ variable }}`
  in the email.

The letter runs at a 62ch measure in `.letter` and is set a notch larger
than body copy — this is reading, not scanning. Shep's one-line beats
("Together.") are their own `<p>`, not `<br>`s, so they keep their air on a
phone.

## The beta box

Added 2026-10-23, Shep's call. A fixed panel at the top right of the
homepage — "I wanna be a beta tester" and an email field — that stays put
once the letter scrolls past.

It sits one header-padding (14px) below the header rule, which is the same
gap the install pill has above it, so at the top of the page the two are
evenly spaced either side of the line. That number is `--header-h` plus
14px in `index.html`. **`--header-h` is hardcoded** (14 + the 44px pill +
14 + the 1px rule = 73px, and 67px below 420px where the pill shrinks). If
the bar's padding or the pill's height ever changes, this has to change
with it or the box drifts off the line.

**It is not a second black pill, deliberately.** One filled button is this
site's whole allowance for raising its voice and it belongs to install, so
the box is white with a hairline border and the submit is underlined text.
A fixed panel is already the loudest thing added to this page since the
cards came off it. It does not also need a fill — and if it ever gets one,
the install pill stops being the one loud thing and the header starts
reading as a toolbar.

**Below 920px it collapses** to "beta tester?" and a chevron, and opens on
tap. 920 is not a phone breakpoint, it is where the letter's 62ch measure
and a 300px panel stop fitting side by side — at 930px there is 38px of
clearance and that is as tight as it gets. Don't raise it.

The open/close is a `0fr` → `1fr` grid row (so it animates to the panel's
real height, never a max-height guess) plus a width transition from 150px
to 268px. **150px is measured** — "beta tester?" and the chevron set in
Bryndan, rounded up. Change that label and it has to be remeasured; there
is no CSS way to animate from a content-sized width, which is why the
number is there at all.

**Signups go to a Google Sheet**, through an Apps Script web app (Shep's
call, 2026-10-23, after weighing Formspree — free tier caps at 50/month
and the list would live on someone else's server). The script is
`.claude/scripts/beta-signups.gs`; that file is the source of record and
carries the setup steps in its header, but **the copy that runs lives in
Google**, so editing the file here changes nothing until it is pasted in
and redeployed as a new version. A plain Save in the Apps Script editor
does not update what the deployed URL serves — that is the most common
way this looks broken when it isn't.

**It is live and collecting** (2026-10-23). `BETA_ENDPOINT` in
`index.html` holds the deployed `/exec` URL; a signup appends a row and
the page says so. Emptying the constant falls back to opening the
visitor's mail client, which works and collects nothing.

**Getting there took a detour worth recording.** The deployment read
"Who has access: Anyone" and still returned 403 Access Denied to every
anonymous request, because the Workspace domain
(therealheroesofecommerce.com, Google MX) blocks public access above the
script's own setting — nothing inside Apps Script can override it. If this
ever returns, the symptom is a 403 with `<title>Access Denied</title>` on
a plain GET of the `/exec` URL, and the fix is in the Workspace admin
console under Drive and Docs → Sharing settings, not in the script. The
fallback, if that is ever locked down again, is to own the script from a
personal Google account instead.

**The POST sends `Content-Type: text/plain` and that is deliberate.** It
is JSON in the body, and the Apps Script parses it itself. A real
`application/json` header makes the browser send a CORS preflight, Apps
Script does not answer `OPTIONS`, and the request dies before the data
leaves. Don't "fix" the header.

**Failure is visible, not swallowed.** If the post fails — Google down, a
redeploy in progress, the URL archived — the box says so and offers a
mailto link rather than claiming success. The typed address is kept so
nobody retypes it. Worth preserving: the tempting shortcut here is
`mode: 'no-cors'`, which makes every response opaque and so makes every
failure look like a success.

**The endpoint is public and there is a honeypot because of it.** A static
page cannot hold a secret, so anyone who views source can post to the
sheet. The form carries a hidden, un-tabbable `company` field; anything
that fills it gets the success message and is silently dropped. The script
also shape-checks the address and dedupes case-insensitively. If it ever
does get flooded, archive the deployment and deploy a fresh URL.

**The homepage only.** `templates.html` does not have the box, which is a
real inconsistency given the two pages otherwise share their chrome — see
the note in the inspo section about the duplication. Adding it means
copying the CSS, the markup and the script into the second file.

## A little inspo

The second page (2026-10-14). Shep's plan: the app makes you paste in your
own HTML, so the site shows you six emails worth copying and hands you a
prompt that gets you one.

**The name and the body copy are Shep's**, replaced 2026-10-14. Nav link
"A little inspo", h1 "A little inspiration never hurts...", and the
paragraph running from "These templates cover the most common email
layouts" to "by the truckload". Kept verbatim; the only edit was
"Idiosync" → "idiosync" per the brand rule. The three-period "never
hurts..." is his and matches the "Yeah... that." precedent in the letter,
so it is not an ellipsis waiting to be fixed. It is one paragraph because
that is how he wrote it — the beats ("Or best. Or both.") hold up inside
the block.

The working title through the build was "Fun with templates"; it survives
in git history and nowhere else.

**Why this doesn't contradict the product.** It is documentation, not a
feature — it removes the hurdle the app deliberately keeps, rather than
adding a whistle. That reading holds at **six, flat: no filters, no
categories, no counts, no "more coming soon", no tiers.** Add any one of
those and it becomes the template library the product is supposed to not
have. The name is Shep's and the jokiness fits the letter's voice.

**Copy prompt copies instructions *plus* the template's entire HTML.**
Decided 2026-10-14, Claude's recommendation, Shep's call. Prose alone —
"single column, cream, big serif headline" — gets the user their AI's guess
at an email, not the one they clicked, and the gallery's whole promise is
*that* email. It also splits the work correctly: email HTML (nested tables,
inline styles, Outlook quirks) is what an AI is worst at from scratch, and
rewriting copy is what it is best at. So the clipboard carries working
markup and asks the AI to change only words, colours and images.

The prompt text lives in `buildPrompt()` in `templates.html`. The three
things it forbids are the three an AI "improves" unasked: tables → divs,
inline styles → a `<style>` block, and tidying up merge variables it
doesn't recognise. Each breaks the email somewhere between Outlook and send
time. It also tells the AI to ask what the email is for before writing.

**Thumbnails are the real emails in scaled-down iframes, not screenshots.**
So a template can never drift from its picture, and there are no image
assets to maintain. The cost is that the scale factor has to be measured
(`setScale()`, plus a `ResizeObserver`), because it depends on the column
width `auto-fill` lands on. Clicking one opens the same file full size in a
`<dialog>`.

**The variables are placeholders and MUST be swapped before launch.**
`{{ first_name }}`, `{{ shop_name }}`, `{{ unsubscribe_url }}`,
`{{ view_in_browser_url }}` are stand-ins — idiosync's real merge syntax
wasn't to hand when this was built (Shep: "i can find later"). They are in
all six files and named in the prompt text. `grep -rn "{{" templates/
templates.html` finds every one. **Shipping these as-is means every email a
user pastes back renders literal braces**, so this is a launch blocker, not
a nicety. The unsubscribe variable is also what a Shopify listing review
will look for.

**Copying is verified up to the clipboard handoff, not through it.** The
fetch and the prompt build were confirmed in the preview (3,446 chars of
HTML → a 4,400 char prompt, variables intact), but both
`navigator.clipboard.writeText` and the `execCommand` fallback need a
focused document, and the preview pane never has focus. Click a button in a
real browser once before trusting it. There are two routes (`toClipboard()`
falls back to `legacyCopy()`) because the async API refuses on a secure
context, a stale gesture *and* an unfocused document, all as
`NotAllowedError`. Neither works over `file://` — `fetch` is blocked there
too, so this page needs the preview server, unlike `index.html`.

**The emails are not set in Bryndan.** They use Georgia and Helvetica
stacks, because an email client can't load a self-hosted webfont and these
are templates for other people's brands, not for idiosync. The site chrome
around them is Bryndan as usual.

**Chrome styles are duplicated across `index.html`, `templates.html` and
`pricing.html`** — tokens, header, footer, the narrow-header fixes. A
Jekyll layout is the right fix and the Jekyll section already says so, but
the local preview server doesn't run Jekyll, so a layout can't be
eyeballed before it ships. Do that refactor when there's a way to verify
it; until then, **a change to the header or the tokens has to be made in
all three files.** See "The header, now that there are four things in it"
below.

**The homepage now has a third thing to click** (2026-10-14, Shep's call:
header nav, beside the pill). That is a real amendment to the "exactly two
things, both pointing at install" rule above. It is plain underlined text,
not a second pill — one black button is the site's whole allowance for
raising its voice and it belongs to install. Below 520px the text link
drops out so the pill survives the narrow header; the footer carries the
link as well, which is what keeps the page reachable on a phone.

## Pricing

`pricing.html`, added 2026-10-23 at Shep's request, rebuilt from the
pricing screen in the Shopify app so the two agree on sight.

**Why this doesn't contradict "no pricing anywhere".** That rule was about
the homepage: the panel that got deleted was a placeholder with no number
behind it, sitting on a page whose argument is "leave as fast as you can",
and it was arguing back. This is a real number on its own page, found by
someone who went looking for it. The homepage still names no price.

**The headline is Shep's: "One-size-fits-noone".** He finds it funny and
it is kept exactly as he spelled it. Standard English would be "no one",
two words; per the Style rule this is a creative spelling, so it is
flagged here and left verbatim rather than quietly corrected. The joke
also does real work — it is the pay-as-you-go argument in four words.

**The paragraph under it is Claude's placeholder and should be replaced.**
Everything else on this site is in Shep's voice and this is the one block
that isn't. It says the plain facts (no subscription, no plan to outgrow,
rate drops as you buy more) and nothing more, deliberately, so there is
less to unpick when his version arrives.

**The pricing is graduated, not flat.** 25,000 emails is 10,000 at $5 plus
15,000 at $4 = **$110**, not 25,000 at $4 = $100. This is the one thing to
get right in the calculator: the flat reading is the intuitive one and it
is wrong. The page says so in the app's own words — "Lower rates apply
only to credits in each band of this purchase."

The bands, as of 2026-10-23:

| band | rate |
| --- | --- |
| First 10,000 | $5 / 1,000 |
| Next 40,000 | $4 / 1,000 |
| Above 50,000 | $3 / 1,000 |

Sold in 1,000-email increments, 1,000 minimum, 300,000 maximum per
purchase. Below the minimum or above the cap, the field snaps on blur;
a non-multiple of 1,000 rounds to the nearest.

**The rates live in two places and both have to change together**: the
`BANDS` array in the inline script, and the hand-written Pricing guide
table in the markup. The table is typed out rather than generated because
three static rows are easier to read in the source than a loop that
produces them; the cost of that is this note. There are comments on both.

**The amount field is `type="text"`, not `type="number"`**, so the resting
value can show "25,000" the way the app's does — a number input refuses a
thousands separator. `inputmode="numeric"` still gets the number pad on a
phone, and the min/max/step are enforced in `snap()`. The field reformats
on blur, not on every keystroke: snapping as you type rewrites "2" into
"1,000" before you reach the 5.

**Verbatim from the app**, and worth keeping that way so the site and the
app don't drift: "Credits are sold in 1,000-email increments, up to
300,000 per purchase", "Lower rates apply only to credits in each band of
this purchase", "USD, before any applicable tax", and the three rows of
the pricing guide.

**The calculator is NOT set in Bryndan** (Shep's call, 2026-10-23: "since
we are mathing on this, lets make the font less fun"). Everything inside
the two panels — headings, labels, figures, the install link — is in
`--font-ui`, the machine's own UI sans. A drawn face is right for a
letter and wrong for a column of prices: it is wide, it has one weight,
and its digits are not tabular, so figures in a list don't line up under
each other. The panels set `font-variant-numeric: tabular-nums` for the
same reason.

**The split is panel / not-panel**, and that is the whole rule. The
headline, the paragraph and the site chrome stay in Bryndan, so the page
still sounds like the rest of the site; the calculator reads like the app
it mirrors. Don't let the boundary drift — a Bryndan heading sitting over
system-sans figures looks like two pages stitched together.

**No webfont was added for this.** `--font-ui` is a plain system stack,
which costs nothing to load and keeps the site's zero-external-requests
property. Self-hosting Open Sans would pin the look across machines at
the cost of another font file; judged not worth it, but that is the move
if the rendering differences ever matter.

**No checkout.** The app's screen has a disabled "Purchases are not
enabled yet" button; the site has a text link to `#install` instead.
Buying happens in Shopify, so a button here would be a second black pill
promising something this page cannot do.

## The header, now that there are four things in it

Mark, "Pricing", "A little inspo", and the install pill. Bryndan is wide
and this is the row where that costs something, so **both text links drop
out together below 640px** (it was 520px when there was one link). They go
together on purpose — dropping one and keeping the other leaves a lopsided
header that reads as a bug. The footer carries both links on every page,
which is what keeps the site navigable on a phone.

That breakpoint and the whole chrome block are now duplicated in **three**
files: `index.html`, `templates.html`, `pricing.html`. A Jekyll layout is
still the right fix and still can't be eyeballed on the static preview
server. Until then, a change to the header or the tokens is a change to
three files.

## Link previews (2026-10-24)

All three pages had a `<title>` and a meta description and nothing else, so
a pasted link came out as grey text with no image — X showed none at all.
Every page now carries a full Open Graph + Twitter block, inserted right
after `canonical`.

- **`og:title` / `og:description` mirror the page's own `<title>` and meta
  description, word for word.** They are duplicated on purpose rather than
  written fresh: two descriptions of the same page drift. Change one,
  change the other.
- **URLs in the block are absolute** (`https://idiosync.site/...`) — the
  opposite of the rule for everything else on the page. A scraper has no
  base to resolve a relative path against. Now correct, since the apex is
  live; on the old project URL these would have pointed at a 404.
- **One card for the whole site**: `assets/social-card.png`, 1200×630,
  drawn by `.claude/scripts/build-social-card.py` (needs `pillow`). White
  ground, the hero plane bottom-right, the mark and wordmark top-left, and
  Shep's headline set in the source Bryndan TTF — the page's own furniture,
  one ink, nothing added. A card with a gradient or a badge on it would be
  the page selling harder in the one place it does not control, which is
  the mistake the homepage already deleted once.
- The plane is **small and low in the card on purpose** — its dashed trail
  climbs up and left out of the nose and lands in the headline at any
  larger size. Re-render and look at the PNG after touching either.
- PNG, composited onto opaque white, not the transparent `paper-plane.png`
  and not SVG: scrapers don't render SVG, and X in dark mode would draw the
  black strokes on near-black.
- Per-page cards were considered and skipped — three images to keep in sync
  for a thumbnail nobody studies.

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
- `index.html` and `templates.html` carry empty front matter (`---` /
  `---`) so Jekyll processes them. Keep it, even with no Liquid in the
  file — drop it and the file ships unprocessed. The opposite is true of
  `templates/*.html`: those must NOT have front matter, or Liquid eats the
  `{{ variable }}` tags in the emails.
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
