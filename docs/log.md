# Top Hand Studio migration log

## 2026-11-02 — Phase 1 content rescue (in progress)

- Kevin authorized read-only rescue of the ASF site, then a plan and approval stop before site implementation.
- Destination confirmed: https://github.com/trelnar/tophandstudio-site (main).
- Repository checkout: `outputs/tophandstudio/` in this chat workspace. Initial remote commit: a74fe7b.
- Crawled homepage, recursive internal content links, pagination and the public sitemap. 58 normalized URLs retrieved; 35 print product records plus an ANC original-art record need reconciliation.
- Saved full body text, discovered URL aliases and sanitized HTML. Scripts and CSRF/authenticity tokens removed from archival HTML; anonymous response headers/cookies are not archived.
- Downloaded 119 distinct image URLs successfully in the first pass, including linked enlargement files and supporting site images. Originals are not assumed: first artwork enlargement is 801 × 1000 pixels.
- Capturing full-page screenshots and dynamic print metadata. ASF size/style/price calculation endpoints are presentation-only; no cart, checkout, contact, newsletter, account or admin action is submitted.
- Local work only so far. No DNS, domain, hosting, account or billing changes. Phase 2 requires Kevin’s approval.

### Phase 1 result and approval stop

- First rescue committed and pushed to `origin main`: `5f9d3fc` (`Archive ASF page content and first image rescue`).
- Completed recursive crawl: 58 normalized page URLs, covering the homepage, six navigation destinations, three-page galleries, 46 sitemap entries, three template categories, two warehouse indexes, newsletter signup, 35 print products and the unresolved ANC original listing. No blog discovered. Observed URL variants are preserved, not silently discarded.
- Final download pass: 155 image URLs, 32,905,744 bytes. Every downloaded image passed decoding and SHA-256 verification. The 35 largest explicitly linked artwork enlargements are 1,000px on the long edge. Social metadata images did not provide larger artwork copies. Artwork variants are named from titles; provenance is in the manifest and inventory.
- Saved 16 usable full-page screenshots, including home, every main navigation destination, eight print-product views and ANC. Three additional screenshots record ASF's “Retry later” response. Captures are mobile-width and may include lazy-loaded gaps. Browser access subsequently became unavailable with `browser.user is unavailable`; no additional screenshot coverage is claimed.
- Detailed print calculations hit HTTP 429. Collection was interrupted rather than continuing to hammer the site. 399 partial base-price calculations were recovered; they omit optional finishing and were not validated as retail offers. Gallery starting prices and static wall-preview sizes are recorded separately. The full price matrix is incomplete.
- Original painting medium, dimensions, year and descriptions were not found in the captured product pages. `content/artworks.json` uses nulls, and ANC is held for Kevin. No titles, dates or media were inferred from filenames or preview dimensions.
- One ASF fallback metadata image (`https://www.tophandstudio.com/assets/fallback/default.jpg`, associated with ANC) was not downloaded after throttling. It is a platform placeholder, not ANC's original artwork. Stylesheet-only platform icons and dynamically generated merchandise previews were not exhaustively mirrored; explicit image URLs and owner-image URLs embedded in the captured pages were downloaded. The archive is a content rescue, not an offline executable clone of ASF.
- Created `content/inventory.md`, `content/navigation.md`, `content/artworks.json`, provenance manifests, `docs/plan.md`, and `docs/archive-verification.json`. No replacement-site code, DNS changes, account changes, cancellation email submission, cart action or checkout action.
- Proposed A: Quiet gallery (recommended), informed by Ellsworth Kelly’s work catalogue. Proposed B: Studio catalogue, informed by Alex Katz’s artist site. Kelly's page structure was read; Katz's live opening was visually reviewed. The inaccessible Hockney candidate was discarded and is not a recommendation.
- GitHub's unauthenticated repository API returned 404, although authorized Git clone/push succeeded. Repository visibility and free Pages eligibility are therefore unverified. Before hosting setup, verify whether the repo is private and whether the existing account supports Pages; do not change visibility or buy a plan without Kevin. A public repo on GitHub Free is the proposed $0 hosting path. Existing domain renewal is outside hosting costs.
- User said “go” while the archive/plan was still being prepared. Interpreted as continuing Phase 1, not approval of a design that had not yet been presented.

### Next session

1. Read `docs/plan.md` and the summary at the top of `content/inventory.md`.
2. Ask Kevin one question: approve direction A or B. Do not start site implementation until he approves the presented plan.
3. Next ask for the local originals folder, then metadata/ANC and contact details in separate turns.
4. Revisit detailed ASF prices only if Kevin needs them and the service is no longer throttling; use much slower requests and stop immediately on 429. They are not needed to publish a non-selling gallery.
5. Implement the approved static site, then prepare `docs/cutover.md`, the redirect map and an unsent cancellation-email draft. Kevin performs DNS and sends the email.


## 2026-11-02 — Direction A approved; static draft implemented

- Kevin selected A. Asked for the local-originals folder, one question only; answer is pending.
- Built `site/`: home with International, Taxico and Flat Top; a 35-piece gallery; 35 artwork pages; about; contact; custom 404; sitemap; robots; favicon; CNAME. ANC remains unpublished.
- Plain HTML/CSS; 8 lines of optional JS preserve artwork context on contact. No frontend framework, runtime data fetch, store, tracking, external fonts, account system or database.
- Authored content remains in `content/artworks.json`. `scripts/prepare_images.py` creates JPG/WebP derivatives with Pillow; `scripts/generate.py` uses only Python’s standard library. Neither is needed to view the committed pages.
- Missing painting metadata is omitted, not invented. Image descriptions were drafted from a visual review of all 35 paintings. Hero selection and editorial headline remain reviewable.
- Existing Instagram profile is the functional contact destination until Kevin confirms a public email. The data supports mailto inquiry subjects and a future external print link. Shopify has an explicitly empty data/markup hook; no script is loaded.
- 174 legacy URL variants map to 48 static redirect routes, covering every crawled old content URL and observed account link. These are HTML redirects with canonical links, not server-side 301s. The root remains the homepage.
- Checks: 88 HTML documents passed the local-link/fragment/image-attribute/canonical/redirect checks. Browser tested home, gallery, artwork, about and contact at 320px (305px content width after scrollbar); no horizontal overflow or broken loaded images. Navigation resolved to all 35 gallery links. Desktop homepage visually reviewed at 1440px. Saved draft screenshots in `docs/previews/`.
- Browser preview launch stalled for approximately nine minutes, then succeeded. Later checks were responsive.
- Draft is not deployed. Original-image folder, public email, painting metadata, ANC identification and repository Pages eligibility remain unresolved. Do not change DNS, repo visibility, account settings or ASF billing.

### Deployment preparation and final verification

- Static draft committed and pushed: `fa2e4dc` (`Build approved quiet gallery with generated artwork pages`).
- Prepared a manual-only Pages workflow using GitHub's current documented action versions. It checks and uploads only `site/`; it does not enable Pages or run on push. No workflow was dispatched.
- Wrote `docs/cutover.md` with exact GoDaddy/GitHub record values, pre-cutover capture, custom domain verification, HTTPS, tests and rollback. Public DNS independently confirmed `www` still points to ASF and the root has GoDaddy forwarding addresses. Saved `docs/dns-before.json`; no DNS changed.
- Wrote the full redirect map and an unsent cancellation draft. Kevin must confirm the current billing-period date and support recipient; no contract assumptions or messages sent.
- Added `docs/editing.md` and updated README with local viewing, data editing, image preparation and publication steps.
- Additional browser checks: three-column desktop gallery, working legacy artwork redirect with ASF query parameters, correct inquiry title reminder, and keyboard skip-link focus. Deterministic regeneration passed. See `docs/validation.md` for evidence and limitations.
- Readiness: implemented draft, not launched. Next user input remains the folder path for the local originals (asked once this turn). After that, ask for the public inquiry email, then painting metadata and ANC as separate questions. Resolve Pages eligibility before any account action. No additional design-direction approval is needed: A is approved.


### GitHub workflow-permission limit resolved without requesting broader access

- GitHub rejected the preparation commit because the existing Personal Access Token lacks `workflow` scope. The static site commit `fa2e4dc` had already pushed successfully.
- Moved the workflow to `docs/pages-workflow.yml` as a reviewed template, and added a concrete GitHub web-UI installation step to the cutover guide. No workflow file is activated, no token scope was expanded, and no account setting was changed.
- Amended only the local, rejected/unpushed preparation commit to contain the template at its new location, then pushed normally (no force push). This supersedes the earlier note that a workflow is installed; it is prepared, not installed.
- Local preview server was stopped after verification. Saved screenshots and directly viewable HTML remain available.
