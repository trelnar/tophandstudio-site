# Top Hand Studio

Kevin Ellis's art site, rebuilt as plain HTML and CSS so he owns it. It replaces the Art Storefronts site at tophandstudio.com, which shuts down on 12/2/2026.

The look follows the old site: gold wordmark, Raleway, gray caps nav, bordered artwork cards, black footer. It is a portfolio for now. A shop can be added later without a rewrite.

## What's where

| Path | What |
|---|---|
| `site/` | The website. This folder is what gets published. Open `site/index.html` in a browser to view it. |
| `data/works.json` | One record per artwork. The only file to edit for content changes. |
| `scripts/build.py` | Makes the pages in `site/` from `data/works.json`. Python 3, nothing to install. |
| `site/assets/` | Stylesheet, contact form script, logo, about photo. Edited by hand. |
| `capture/` | Full capture of the old site from 11/23/2026: every page, screenshots, images, text. See `capture/README.md`. |
| `content/`, `docs/` | Earlier archive and planning notes from 11/2/2026. `docs/cutover.md` has the DNS steps. |
| `.github/workflows/pages.yml` | Publishes `site/` to GitHub Pages on every push to main. |

## Common changes

**Turn on the contact form.** Make a form at formspree.io. Open `scripts/build.py`, set `FORMSPREE_ENDPOINT` near the top to your form's URL, then run `python3 scripts/build.py`. Until then, the form opens the visitor's email app addressed to kevin@tophandstudio.com.

**Edit an artwork** (title, year, medium, dimensions, description): change it in `data/works.json`, then run `python3 scripts/build.py`. Fields left `null` are hidden on the page.

**Swap in full-size images.** Put the new file anywhere in the repo, point that work's `image.source`, `width` and `height` at it, delete `site/images/works/<slug>.jpg` and `<slug>-600.jpg`, then rebuild. The build makes the web copies (needs a Mac for `sips`).

**Add the shop later.** Every work page has a hidden "Buy a print" slot, marked `SHOP SLOT` in the HTML. Set `"shop": {"enabled": true, "buy_url": "..."}` on a work and rebuild to show the button.

## URLs

Old addresses keep working. Each artwork lives at its old path, `/warehouse-open-edition-prints/art_print_products/<slug>/`. `/about-the-artist/`, `/contact/`, `/faq/` and `/fine-art-prints/` are real pages. `/shop-art/`, `/best-sellers/`, `/warehouse-open-edition-prints/` and `/newsletter-sign-up/` forward to the closest page.

All links are relative, so the site works at the GitHub preview address and at the domain root. There is no CNAME file. Kevin sets the custom domain and DNS himself.
