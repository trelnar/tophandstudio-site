# Cutover — Kevin performs the account and DNS changes

Prepared 2026-11-02. **Not executed.** Site draft: direction A. Resolve the original-image/contact/content review and verify Pages eligibility before scheduling cutover. Keep ASF active until both hostnames and old links work over HTTPS.

## 1. Record the current setup

Public DNS was checked on November 2; see [dns-before.json](dns-before.json). Kevin reported root-domain forwarding at GoDaddy. Its destination, status code and masking settings are not visible through DNS: screenshot those settings and export the zone before changing anything.

| Current record | Observed value |
|---|---|
| `www` CNAME | `www.artstorefronts.com` |
| `@` A | `15.197.225.128` |
| `@` A | `3.33.251.168` |
| `@` AAAA | None observed |
| Nameservers | `ns25.domaincontrol.com`, `ns26.domaincontrol.com` |

Record existing MX/TXT records and leave them intact. Do not change nameservers. Use a one-hour TTL for changed web records unless your cutover plan specifies otherwise.

## 2. Prepare GitHub Pages before switching DNS

In `trelnar/tophandstudio-site`, confirm the repository/account supports Pages at no added cost. Public repositories work with GitHub Free; a private repository may need an existing eligible plan. If not eligible, pause for Kevin’s decision—do not buy anything or change visibility automatically. [GitHub eligibility](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

The current Git token cannot create workflow files. First, in GitHub’s web UI, create `.github/workflows/pages.yml` on `main` using the exact contents of [the saved workflow template](pages-workflow.yml), and commit it. This account-side step is Kevin’s. Then in repository **Settings → Pages**, set the publishing source to **GitHub Actions**. The installed workflow is manual-only: **Actions → Publish approved static gallery → Run workflow → main**. It validates the committed files and uploads only `site/`, keeping the archive and documents out of the public deployment. First test the default address, `https://trelnar.github.io/tophandstudio-site/`. Ordinary pages use relative paths. The 404 page’s root links are intended for the final custom domain. [Workflow setup](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

In account **Settings → Pages → Add a domain**, verify `tophandstudio.com`. Add the exact TXT name/value GitHub gives you to GoDaddy and complete verification. Keep that TXT record. Do not invent the verification value. [Domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).

Set repository **Pages → Custom domain** to `tophandstudio.com` and save **before** changing the web DNS. There is no CNAME file in the repo (on purpose). With an Actions deployment, the Pages setting is what counts. [Custom-domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## 3. Make these GoDaddy changes

Open **Domain Portfolio → tophandstudio.com → DNS**. In **Forwarding**, remove the root-domain forwarding entry after recording it. This lets the root serve the gallery directly. If GoDaddy locks forwarding-managed A records, remove forwarding first, then refresh the DNS list. [Forwarding settings location](https://www.godaddy.com/help/edit-my-domain-forwarding-19978).

Replace the two old apex A values with the four values below. Edit the `www` CNAME. Remove any conflicting old web A/AAAA/CNAME records at those same names; leave mail and unrelated records alone. No IPv6 record is required for this IPv4 setup. [Edit an A record](https://www.godaddy.com/help/edit-an-a-record-19239), [edit a CNAME](https://www.godaddy.com/help/edit-a-cname-record-19237).

| Type | GoDaddy Name | Value | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | 1 hour |
| A | `@` | `185.199.109.153` | 1 hour |
| A | `@` | `185.199.110.153` | 1 hour |
| A | `@` | `185.199.111.153` | 1 hour |
| CNAME | `www` | `trelnar.github.io` | 1 hour |

The `www` target is the GitHub hostname—not the repository URL or a path. GitHub’s apex-domain setup with the matching `www` DNS handles the preferred-host redirect. These are GitHub’s published A values; recheck them if cutover happens substantially later. [GitHub DNS values](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## 4. Verify DNS, HTTPS and the gallery

Check the new answers:

```sh
dig +short tophandstudio.com A
dig +short www.tophandstudio.com CNAME
```

Expect the four GitHub IPs and `trelnar.github.io.`. Allow DNS caches to expire; GoDaddy notes propagation can take up to 48 hours. [GoDaddy propagation guidance](https://www.godaddy.com/help/edit-a-cname-record-19237).

In GitHub **Settings → Pages**, wait for the domain check and certificate to complete, then select **Enforce HTTPS**. Do not bypass a certificate warning. If provisioning stalls, confirm DNS first; GitHub documents re-saving the domain as a retry. No SSL purchase is needed. [HTTPS setup and troubleshooting](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

Check all four entry points: `http://tophandstudio.com`, `https://tophandstudio.com`, `http://www.tophandstudio.com`, `https://www.tophandstudio.com`. They should end on the HTTPS apex gallery. Verify the home, gallery, about, contact, an artwork inquiry, one portrait-format painting, and an unknown path/404. Confirm no asset requests go to ASF and no mixed-content errors appear. Test from a phone on cellular as well as your usual browser.

## 5. Old URLs and redirects

The complete [redirect map](redirect-map.md) and [machine-readable map](../content/redirects.json) cover 174 observed URL variants and 48 legacy paths. Each old artwork path gets its matching artwork; old gallery/warehouse/category paths go to the gallery, about goes to about, FAQ goes to the prints note, account/signup paths go to contact, and unresolved ANC goes to the gallery. Query parameters no longer select print configurations.

GitHub Pages has no per-route server redirect configuration. The generated stubs use immediate HTML redirects, canonical targets and clickable fallback links. These return a page rather than an HTTP 301. Test an old product URL with `product_gallery` and `product_id`, `/about-the-artist`, `/shop-art` and `/faq`. Never describe these as server-side 301s.

## 6. Roll back if necessary

While ASF is still active, restore `www` to `www.artstorefronts.com`, remove the four GitHub apex A records, and restore GoDaddy root forwarding using the exact saved destination/type/masking settings. Confirm GoDaddy recreates its forwarding-managed A records; compare against your pre-cutover export rather than assuming the old IPs remain permanent.

Wait for DNS caches and retest both hostnames. Leave the GitHub domain association and verification TXT in place while DNS still points there; only unlink Pages after traffic has left GitHub. Once ASF is cancelled, returning traffic to it may not work—use the GitHub fallback below instead.

For a site-content regression, revert the bad commit on `main`, regenerate/check if needed, push and manually rerun the Pages workflow. Preserve the archive. Do not reset shared history or force-push.

## 7. Cancel ASF only after successful cutover

Use [the unsent cancellation draft](asf-cancellation-email.md). Confirm the billing-period end date from the current invoice, send through ASF’s established support channel, and save their written confirmation. Keep the site archive and local originals. Kevin sends the email; nothing has been cancelled.
