# Design notes: tophandstudio.com (captured 2026-11-23)

Measured from the live site with a headless browser (computed styles), plus pixel sampling of the logo file. Raw numbers are in `raw/design.json`.

## Logo / wordmark

The gold "TOP HAND STUDIO" wordmark is an image, not live text. Black italic condensed letters on gold slanted tiles. The "I" in STUDIO is a "1" on a darker tile.

| File | Size | Notes |
|---|---|---|
| `logo/wordmark-1567x355.png` | 1567 x 355 | Largest version. One line. White background (not transparent). |
| `logo/wordmark-1000x227.webp` | 1000 x 227 | The one shown in the header (`#logo_image`). |
| `logo/wordmark-500x113.webp` | 500 x 113 | Smaller copy, also used in the header markup. |
| `logo/wordmark-stacked-901x355.webp` | 901 x 355 | Two lines: TOP HAND / STUD1O. Shown on the coupon popup. |

Header display size on desktop: 220 x 50 px, placed at x=112, y=10.

## Colors (hex)

| Use | Hex |
|---|---|
| Wordmark gold tile | `#dbc47c` |
| Wordmark dark gold tile (the "1") | `#bea55c` |
| Wordmark letters | `#000000` |
| Page background | `#ffffff` |
| Main text | `#000000` |
| Headings, artwork titles on product page | `#333333` |
| Filter list text | `#303030` |
| Top nav links (desktop) | `#999999` |
| Secondary text (product tools, captions) | `#666666`, `#757575` |
| Buttons ("ADD TO CART") | white text on `#000000` |
| Footer and "TRUSTED" bar | white text on black (`#000000` / `#1a1a1a`) |
| Small accent seen on badges | `#ff5e00` (Art Storefronts badge, not Kevin's brand) |

The colored swatches in the "Colors" filter (`#cd6155`, `#17202a`, etc.) are the platform's filter palette, not site colors.

## Fonts

- Everything is **Raleway** (Google Fonts), weights loaded: 200, 300, 400, 500, 600, 700, plus 300 italic.
- Icons: Font Awesome 6 Free (search, heart, cart, account icons in the header).

| Element | Size | Weight | Letter spacing | Case | Color |
|---|---|---|---|---|---|
| Body | 14.44px desktop, 16px phone | 400 | normal | | `#000000` |
| Top nav (desktop) | 11.25px | 300 | 1.6875px | UPPERCASE | `#999999` |
| Gallery heading "Fine Art Prints" | 18.77px desktop, 28px phone | 400 | 1px | as typed | `#333333` |
| Grid card title (PARKING) | about 13px | 400 | 1px | UPPERCASE | `#000000` |
| Grid card price ("from $43.00") | 13px | 400 | 1px | | `#000000` |
| Product page title | 26 to 28px | 400 to 700 | 1px | UPPERCASE | `#333333` |
| Product page price | 26px | 600 | | | `#333333` |
| Buttons | 13px | 700 | 0.5px | UPPERCASE | white on black |
| Footer links | 13px | 400 | 1px | | `#ffffff` |
| "TRUSTED" footer banner | 200px | 800 | 15px | UPPERCASE | white, faint on dark |

## Layout

- Content area on desktop: starts at x=114, about 1212px wide (at a 1440 window). Header logo left aligned with the content.
- **Header (desktop):** logo on the left, then nav links in a row right after it (SHOP PRINTS, ABOUT THE ARTIST, CONTACT, FAQ). Icons on the right: search, favorites (heart), cart with count, account.
- **Header (phone):** 45px white bar. Logo, then cart and menu icons on the right. Nav is in a slide-out menu.
- **Home page** is the gallery "Fine Art Prints": left sidebar filter (Colors swatches, Mediums checkboxes) and a three column masonry grid of artwork cards. Each card: image with a thin light gray border and shadow, title in caps, "from $XX.00", a heart icon. On phone the grid is one column and the filters move above it.
- **Product page:** large image on the left (about 7/12 width), title, price, buy options on the right (Medium, Size, Styles tabs, ADD TO CART, INSTANT CHECKOUT). Below the image: Live Preview AR, Wall Preview, 360 Viewing Tool, Save to Favorites, Email a Friend, Share.
- **Footer:** black. A huge faint "TRUSTED" word with two Art Storefronts badges, then five columns: Info (copyright, Top Hand Studio, Seattle, WA 98102), Contact (Contact Form), Resources (About the artist), Stay Updated (Facebook, Instagram), News (email signup).
- A "SAVE 20% ON YOUR FIRST ORDER!" email popup with the stacked logo appears a few seconds after page load. It is in `screenshots/*/home__popup.png`. All other screenshots have it hidden.
- A round accessibility widget button sits at the bottom left of every page (third party).

## Navigation structure

```
Shop Prints         /shop-art          (links to Best Sellers and Fine Art Prints)
  Best Sellers      /best-sellers
  Fine Art Prints   /fine-art-prints   (same gallery as the home page)
About The Artist    /about-the-artist
Contact             /contact
FAQ                 /faq
```

Footer adds: Contact Form (/contact), About the artist, Facebook (https://www.facebook.com/TopHandStudio), Instagram (https://www.instagram.com/tophand_studio/), newsletter sign-up (/newsletter-sign-up).

Artwork URLs follow `/warehouse-open-edition-prints/art_print_products/<slug>`.

## Favicon

None. The site sets no `<link rel="icon">`, and `/favicon.ico` redirects to an HTML page.

## Things not found on the live site

- The tagline "Alaska - but not the mountains, bear, moose or fish parts." does not appear on any captured page, in the HTML, the visible text, or the image alt text. It may live only in an image or have been removed. The brief asks for it, so the rebuild will add it.
- No email address or phone number is shown anywhere. The only contact path is the form. The only location shown is "Seattle, WA 98102" in the footer.
