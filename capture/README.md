# Capture of tophandstudio.com (Art Storefronts), 2026-11-23

A record of the public site before it goes dark on 12/2/2026. Captured with headless Chromium, one request at a time with pauses. Public pages only, no login.

| Path | What |
|---|---|
| `site-map.md` | Every URL found, its title, and whether it was captured |
| `works.json` | One record per artwork. Fields not shown on the site are `null` |
| `design-notes.md` | Fonts, colors, logo, layout, nav structure |
| `content/` | Verbatim text: about, contact, FAQ (shipping and returns policies), footer, newsletter and coupon popup |
| `pages/<slug>.html` | Rendered HTML after JavaScript ran |
| `pages/<slug>.txt` | Visible text of the page |
| `screenshots/desktop/` | Full page, 1440 wide |
| `screenshots/phone/` | Full page, 390 wide (iPhone 13, 3x pixels) |
| `images/works/` | Largest image of each artwork the site serves, named by URL slug |
| `images/all/` | Every image seen on any page, named by a hash of its URL. Index: `raw/images-all.json` (URL, pages, pixel size) |
| `logo/` | Wordmark files |
| `raw/` | Crawl data: links, image lists, meta tags, computed styles |

## Notes

- Artwork images top out at 1000px on the long side. The CDN URLs are encrypted tokens, and adding resize parameters returns the same file. Full-resolution originals will replace these later.
- Per-session tokens and public keys (CSRF tokens, form tokens, reCAPTCHA site key, Stripe publishable key) were replaced with `[removed]` in the saved HTML and crawl data.
- Screenshots have the "Save 20%" popup hidden, except `home__popup.png`.
