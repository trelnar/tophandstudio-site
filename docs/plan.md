# Top Hand Studio — approved direction A

**Approved 2026-11-02:** Kevin selected A (Quiet gallery). The static draft is implemented with rescued images while original files and missing metadata are pending. DNS and account changes remain Kevin’s actions.

## What is safely preserved

The archive contains 58 normalized public page URLs, 35 print listings, an unresolved original listing called ANC, and 155 image downloads with provenance and checksums. It includes the about text, contact-page copy, FAQ, navigation, sitemap, URL aliases, source HTML and full-page visual references. Read [the inventory](../content/inventory.md) for the complete record.

All 35 artwork enlargements have a 1,000-pixel long edge. They are usable web references, not verified full-resolution masters. Kevin’s local originals are needed for high-quality large images. The public pages do not supply original painting media, dimensions, years or individual artwork descriptions. These fields are null in `content/artworks.json`.

ASF’s public gallery starting prices and wall-preview sizes are preserved. A detailed print-price rescue hit HTTP 429. Partial calculation responses are saved for reference but omit finishing and are not validated sale prices. Do not reuse them as new prices. ANC has a title but no recoverable artwork photograph or useful metadata. Keep it out of the public gallery until identified.

## Two design directions

### A — Quiet gallery (recommended)

White canvas, near-black text, compact navigation and generous space around uncropped paintings. A restrained system sans serif keeps the site fast and the paintings central. Captions sit below images, with title first and medium/date only when confirmed. No decorative frames, shadows, card borders or animated carousel.

Reference: [Ellsworth Kelly’s works catalogue](https://ellsworthkelly.org/work/) for clear artwork records, medium/date/dimension labels and a browsable collection. Its extensive filtering is a reference for organization; this much smaller gallery should begin with a simple grid. The reference page’s text and structure were verified; a new screenshot could not be captured after browser access became unavailable.

Home: three curated pieces, each shown whole; a short introduction and “View all work.” Proposed candidates are International, Taxico and Flat Top, subject to Kevin’s selection. Gallery: one column on small phones, two on larger screens, three on desktop. Artwork: large image followed by a concise label and “Inquire about this work.”

### B — Studio catalogue

A very light warm background, a slightly stronger studio wordmark and an editorial rhythm of large paintings interspersed with brief notes about Anchorage. Keep the existing Top Hand Studio identity if Kevin wants continuity, but use a cleaner, smaller treatment. Captions can use a modest system serif; navigation remains plain sans serif.

Reference: [Alex Katz’s official site](https://www.alexkatz.com/) for a direct artist identity and a painting-led opening. Its live opening was visually reviewed. Borrow the directness and scale; Kevin’s wordmark should remain quieter than that reference’s large masthead.

Home: one lead painting followed by two smaller pieces and a short studio introduction. Gallery and artwork pages retain the same simple, accessible structure as A. The warmth comes from spacing and typography, with no additional visual effects.

Both are proposed directions, not finished mockups. After Kevin chooses, prepare a small home/artwork layout for review before implementing the full collection.

## Content and navigation

- **Home:** selected work and a short artist introduction.
- **Gallery:** all confirmed work; no filters at launch unless Kevin supplies meaningful series or painting-medium groups. ASF’s metal/canvas/acrylic choices describe print substrates, not painting media. Its “e.g. nature/animals/abstract” categories are template residue.
- **Artwork pages:** one stable slug per piece, large uncropped image, confirmed title/medium/size/year/description, inquiry link, previous/next work.
- **About:** preserve the Anchorage/CCA narrative and artist portrait; remove ASF sales endorsements. Kevin reviews the wording.
- **Contact:** an explicit email link, with an artwork title in the subject. Kevin supplies the public email address. No hosted form service is needed.
- **Prints note:** “For print inquiries, contact Kevin” until an Etsy or Fine Art America destination is selected. Keep the destination in data. Reserve a small optional purchase section for a later Shopify Buy Button; no Shopify script or paid dependency now.

Keep old print prices as archival evidence only. Do not carry forward cart, checkout, accounts, favorites, discount popups, newsletter form, ASF badges or shipping/refund policies into a non-selling gallery.

## Implementation after approval

Use committed plain HTML/CSS and small optional JavaScript for filters, if supported by the metadata. No framework. The committed pages must open directly without running a build or fetching JSON. A small Python standard-library generator will read `content/artworks.json` and produce those pages when content changes. Updating work means editing that file and rerunning the generator; visitors do not run it.

`content/artworks.json` is the single authored artwork record. It already contains the rescue draft; separate page/image manifests preserve archival evidence. Add fields for approved alt text, hero selection, display order, image derivatives, inquiry address and optional external print links. Preserve unknown metadata as null and omit it from public labels.

Publish from a dedicated `site/` output directory via a small GitHub Pages workflow after approval. This keeps the content archive, original downloads and planning documents out of the deployed site. The workflow uploads already generated static files; it does not require a framework or a build to view the site. The publishing root will contain `CNAME` with `tophandstudio.com`, `.nojekyll`, sitemap, robots, 404 and all page/asset files.

Create optimized responsive derivatives from Kevin’s originals, preserving originals unchanged. Target a small mobile hero, lazy-load gallery images below the first row, include intrinsic dimensions, and use local/system fonts. Avoid analytics initially. GitHub’s hosting may retain its own security logs.

Check keyboard navigation, visible focus, contrast, useful alt text, 320px layouts, zoom/reflow, reduced motion, local-file viewing, production paths and broken links. Validate generated HTML and ensure every artwork has a working inquiry link. Commit and push each meaningful completed step to `origin main`.

## Cost and cutover

Target **$0/month in new hosting or service subscriptions**. GitHub Pages is available for public repositories on GitHub Free; custom domain registration remains Kevin’s existing annual expense. Repository visibility is currently unverified: the public GitHub API returned 404 while authorized Git access worked. Before setup, verify public-repo or existing-plan eligibility; do not make a private repository public or buy a plan without Kevin. No paid form provider, font service, CMS, image CDN, analytics plan or commerce plan is needed. [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

Phase 3 will produce `docs/cutover.md` with freshly verified GoDaddy and GitHub Pages instructions: replace the current `www` CNAME to ASF, remove root forwarding in favor of GitHub’s supported apex records, configure/verify the custom domain, wait for the certificate, enforce HTTPS and test both hostnames. Kevin makes DNS/account changes. Record the current DNS first for rollback and keep ASF active through verification.

Build the redirect map from all URLs in `content/url-aliases.json`, the 58 captured pages and the excluded legacy account URLs. GitHub Pages does not offer configurable server-side 301 rules: prefer retaining valuable paths where practical; otherwise create static redirect stubs with canonical links and visible destinations. Query variants resolve to the same artwork, and a useful 404 handles unknown legacy links. Explain this limitation in the cutover document.

After verified cutover, draft Kevin’s ASF cancellation email: cancellation effective at the end of the current billing period, written confirmation, no further charges, and a request for the signed agreement if ASF asserts an annual commitment. Kevin sends it. No cancellation or DNS action has been taken.

## Kevin’s inputs, in order

1. Pick A or B and approve the plan.
2. Provide the local-originals folder and identify ANC.
3. Fill in painting medium, dimensions, year and descriptions; choose the hero pieces.
4. Confirm the public inquiry address and, when ready, the external print destination.

Ask these one at a time. The next session should read `docs/log.md` first.
