#!/usr/bin/env python3
"""Build the static site in site/ from data/works.json.

Run from anywhere:  python3 scripts/build.py
Standard library only. Image resizing uses macOS `sips` and only runs for
images that are missing from site/images/works/, so the committed site keeps
working without it.
"""
import datetime
import html
import json
import os
import shutil
import subprocess
import sys
import urllib.parse

# Kevin: paste your Formspree form URL here, e.g. "https://formspree.io/f/abcdwxyz",
# then run this script again. Until then the form falls back to opening an email.
FORMSPREE_ENDPOINT = "https://formspree.io/f/YOUR_FORM_ID"

CONTACT_EMAIL = "kevin@tophandstudio.com"
SITE_NAME = "Top Hand Studio"
SITE_URL = "https://www.tophandstudio.com"  # used only in sitemap.xml and canonical links
TAGLINE = "Alaska - but not the mountains, bear, moose or fish parts."
FACEBOOK = "https://www.facebook.com/TopHandStudio"
INSTAGRAM = "https://www.instagram.com/tophand_studio/"
WORKS_DIR = "warehouse-open-edition-prints/art_print_products"  # old URL path, kept so links still work

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
e = html.escape


def rel(depth):
    return "../" * depth if depth else "./"


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def alt_text(w):
    return w["alt"] or f'"{w["title"]}", painting by Kevin Ellis'


def page(depth, path, title, description, body, current="", extra_head=""):
    r = rel(depth)
    canonical = SITE_URL + "/" + path
    nav = [("Gallery", "", "gallery"), ("About The Artist", "about-the-artist/", "about"),
           ("Contact", "contact/", "contact"), ("FAQ", "faq/", "faq")]
    here = ' aria-current="page"'
    links = "\n".join(
        f'<a href="{r}{href}"{here if key == current else ""}>{label}</a>'
        for label, href, key in nav)
    year = datetime.date.today().year
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(canonical)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;600;700&display=swap">
<link rel="stylesheet" href="{r}assets/style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{r}"><picture><source media="(max-width: 899px)" srcset="{r}assets/logo-stacked.png"><img src="{r}assets/logo.png" width="220" height="50" alt="Top Hand Studio home"></picture></a>
    <nav class="nav nav-desktop" aria-label="Main">
{links}
    </nav>
    <details class="menu">
      <summary aria-label="Menu"><span></span></summary>
      <nav class="nav" aria-label="Main menu">
{links}
      </nav>
    </details>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-cols">
    <div><h2>Info</h2><p>&copy; Copyright {year}<br>All Rights Reserved<br>Top Hand Studio<br>Seattle, WA 98102</p></div>
    <div><h2>Contact</h2><p><a href="{r}contact/">Contact Form</a><br><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p></div>
    <div><h2>Resources</h2><p><a href="{r}about-the-artist/">About the artist</a><br><a href="{r}faq/">FAQ</a></p></div>
    <div><h2>Stay Updated</h2><p><a href="{FACEBOOK}" rel="noopener">Facebook</a><br><a href="{INSTAGRAM}" rel="noopener">Instagram</a></p></div>
  </div>
  <p class="wrap footer-tagline">{e(TAGLINE)}</p>
</footer>
</body>
</html>
"""


def card(w, r, i):
    big, thumb = w["_img"]
    return f"""<a class="card" href="{r}{WORKS_DIR}/{w['slug']}/" style="order:{i}">
  <img src="{r}{thumb['src']}" srcset="{r}{thumb['src']} {thumb['w']}w, {r}{big['src']} {big['w']}w" sizes="(min-width: 900px) 380px, 92vw" width="{thumb['w']}" height="{thumb['h']}" alt="{e(alt_text(w))}" loading="{'eager' if i < 3 else 'lazy'}">
  <span class="card-title">{e(w['title'])}</span>
</a>"""


def gallery_body(works, r, heading="Gallery"):
    # Cards go into 3 columns in turn (1st, 2nd, 3rd, 1st...), the way the old site laid them out.
    cols = [[], [], []]
    for i, w in enumerate(works):
        cols[i % 3].append(card(w, r, i))
    colhtml = "\n".join('<div class="col">\n' + "\n".join(c) + "\n</div>" for c in cols)
    return f"""<div class="gallery">
<aside class="side">
  <p class="tagline">{e(TAGLINE)}</p>
  <ul class="side-links">
    <li><a href="{r}about-the-artist/">About the artist</a></li>
    <li><a href="{r}contact/">Contact</a></li>
    <li><a href="{INSTAGRAM}" rel="noopener">Instagram</a></li>
  </ul>
</aside>
<h1 class="page-title">{e(heading)}</h1>
<div class="grid">
{colhtml}
</div>
</div>"""


def work_body(w, prev, nxt, r):
    big, _ = w["_img"]
    facts = [(k, w[k]) for k in ("year", "medium", "dimensions") if w.get(k)]
    facts_html = ("<dl class=\"facts\">" + "".join(f"<dt>{k.title()}</dt><dd>{e(str(v))}</dd>" for k, v in facts) + "</dl>") if facts else ""
    desc = f'<div class="description"><p>{e(w["description"])}</p></div>' if w.get("description") else ""
    shop = w.get("shop") or {}
    buy_hidden = "" if shop.get("enabled") and shop.get("buy_url") else " hidden"
    buy_href = e(shop.get("buy_url") or "#")
    return f"""<p class="crumbs"><a href="{r}">Gallery</a> &gt; {e(w['title'])}</p>
<article class="work">
  <div class="work-image">
    <a href="{r}{big['src']}"><img src="{r}{big['src']}" width="{big['w']}" height="{big['h']}" alt="{e(alt_text(w))}"></a>
    <p class="enlarge"><a href="{r}{big['src']}">click to enlarge</a></p>
  </div>
  <div class="work-info">
    <h1>{e(w['title'])}</h1>
    {facts_html}
    {desc}
    <!-- ============ SHOP SLOT: "Buy a print" ============
         Hidden until the shop exists. To turn it on for this work, set
         "shop": {{"enabled": true, "buy_url": "..."}} in data/works.json and rebuild. -->
    <section class="buy-print" id="buy-a-print" data-shop-slot{buy_hidden}>
      <a class="button" href="{buy_href}">Buy a print</a>
    </section>
    <!-- ============ END SHOP SLOT ============ -->
    <p><a class="button button-outline" href="{r}contact/?work={e(urllib.parse.quote(w['title']))}">Ask about this work</a></p>
    <nav class="prevnext" aria-label="More work">
      <a href="{r}{WORKS_DIR}/{prev['slug']}/">&larr; {e(prev['title'])}</a>
      <a href="{r}{WORKS_DIR}/{nxt['slug']}/">{e(nxt['title'])} &rarr;</a>
    </nav>
  </div>
</article>"""


def redirect(depth, path, target, title, label):
    r = rel(depth)
    write(path + "index.html", f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{e(title)} | {SITE_NAME}</title>
<meta name="description" content="This page moved to {e(label)} on {SITE_NAME}.">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={r}{target}">
<link rel="canonical" href="{SITE_URL}/{target}"></head>
<body><p>This page moved. <a href="{r}{target}">Continue to {e(label)}</a>.</p></body></html>
""")


def make_images(works):
    """Web copies: a 1000px version for work pages and a 600px one for the grid."""
    os.makedirs(os.path.join(OUT, "images", "works"), exist_ok=True)
    for w in works:
        src = os.path.join(ROOT, w["image"]["source"])
        out = []
        for suffix, size in (("", 1000), ("-600", 600)):
            name = f"images/works/{w['slug']}{suffix}.jpg"
            dest = os.path.join(OUT, name)
            if not os.path.exists(dest):
                if not shutil.which("sips"):
                    sys.exit(f"Missing {name} and no sips to make it. Run on a Mac, or add the file by hand.")
                subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                                "-Z", str(size), src, "--out", dest], check=True, capture_output=True)
            o = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", dest], capture_output=True, text=True).stdout if shutil.which("sips") else ""
            if o:
                wd = int(o.split("pixelWidth:")[1].split()[0]); ht = int(o.split("pixelHeight:")[1].split()[0])
            else:  # no sips: derive from the source size
                s = min(1.0, size / max(w["image"]["width"], w["image"]["height"]))
                wd, ht = round(w["image"]["width"] * s), round(w["image"]["height"] * s)
            out.append({"src": name, "w": wd, "h": ht})
        w["_img"] = out


def main():
    data = json.load(open(os.path.join(ROOT, "data", "works.json"), encoding="utf-8"))
    works = sorted(data["works"], key=lambda w: w["order"])
    make_images(works)

    # Remove old generated HTML (keep assets and images).
    for dirpath, _, files in os.walk(OUT):
        for f in files:
            if f.endswith(".html") or f in ("sitemap.xml", "robots.txt"):
                os.remove(os.path.join(dirpath, f))

    desc_home = "Paintings of everyday life in Alaska by Kevin Ellis. Top Hand Studio."
    write("index.html", page(0, "", f"{SITE_NAME} | Paintings by Kevin Ellis", desc_home,
                             gallery_body(works, rel(0)), "gallery"))
    write("fine-art-prints/index.html", page(1, "fine-art-prints/", f"Gallery | {SITE_NAME}", desc_home,
                                             gallery_body(works, rel(1)), "gallery"))

    n = len(works)
    wd = WORKS_DIR.count("/") + 2
    for i, w in enumerate(works):
        desc = w.get("description") or f'"{w["title"]}", a painting by Kevin Ellis of Top Hand Studio.'
        write(f"{WORKS_DIR}/{w['slug']}/index.html",
              page(wd, f"{WORKS_DIR}/{w['slug']}/", f"{w['title']} | {SITE_NAME}", desc[:300],
                   work_body(w, works[i - 1], works[(i + 1) % n], rel(wd)), "gallery",
                   f'<meta property="og:image" content="{SITE_URL}/{w["_img"][0]["src"]}">\n'))

    about = f"""<div class="about">
  <div class="about-text">
    <p class="kicker">About Me</p>
    <h1>I'm Kevin,</h1>
    <p>I grew up in Anchorage, Alaska where I took an early interest in making art. I studied painting at the California College of the Arts, and have maintained a focus on my hometown as a muse for my work.</p>
    <p>Growing up in Alaska, your first exposure to art tends to be depictions of Alaska's nature and wildlife. But there's more to life in Alaska, and the more I traveled outside Alaska, the more I came to appreciate the unique visual language of everyday life in my hometown. It's at once mundane, beautiful and for me, comforting.</p>
  </div>
  <img class="about-photo" src="{rel(1)}assets/kevin.jpg" width="1200" height="901" alt="Kevin Ellis holding a pencil in his teeth, in front of one of his paintings of a snowy Anchorage intersection">
</div>
<p class="connect">Let's stay connected:</p>
<p class="social"><a href="{FACEBOOK}" rel="noopener">Facebook</a> <a href="{INSTAGRAM}" rel="noopener">Instagram</a></p>"""
    write("about-the-artist/index.html", page(1, "about-the-artist/", f"About The Artist | {SITE_NAME}",
          "Kevin Ellis grew up in Anchorage, Alaska and studied painting at the California College of the Arts. His work looks at everyday life in his hometown.",
          about, "about"))

    contact = f"""<h1 class="page-title left">Contact</h1>
<p>Thank you for your interest in my art! Please fill out the form below, and I'll get back to you shortly!</p>
<form class="contact-form" id="contact-form" action="{e(FORMSPREE_ENDPOINT)}" method="POST" data-fallback-email="{CONTACT_EMAIL}">
  <label for="name">Name <span aria-hidden="true">*</span></label>
  <input id="name" name="name" type="text" autocomplete="name" required>
  <label for="email">Email <span aria-hidden="true">*</span></label>
  <input id="email" name="email" type="email" autocomplete="email" required>
  <label for="message">Message <span aria-hidden="true">*</span></label>
  <textarea id="message" name="message" rows="7" required></textarea>
  <input type="hidden" name="_subject" value="Message from tophandstudio.com">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="button" type="submit">Send</button>
  <p class="required-note"><span aria-hidden="true">*</span> = required</p>
</form>
<p class="mailto">Or email me directly: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
<script src="{rel(1)}assets/contact.js"></script>"""
    write("contact/index.html", page(1, "contact/", f"Contact | {SITE_NAME}",
          "Get in touch with Kevin Ellis at Top Hand Studio.", contact, "contact"))

    faq = f"""<h1 class="page-title left">Frequently Asked Questions</h1>
<div class="faq">
  <h2>How can I keep up with your new work?</h2>
  <p>I would love for you to be the first to know about any new work! Follow along on <a href="{INSTAGRAM}" rel="noopener">Instagram</a> and <a href="{FACEBOOK}" rel="noopener">Facebook</a>, where I post new work as it happens.</p>
  <h2>Can I buy a print or an original?</h2>
  <p>Not online right now. A print shop is coming. In the meantime, <a href="{rel(1)}contact/">send me a message</a> about any piece you like.</p>
</div>"""
    write("faq/index.html", page(1, "faq/", f"FAQ | {SITE_NAME}",
          "Questions about Kevin Ellis's work, prints and how to stay updated.", faq, "faq"))

    # Old Art Storefronts URLs that were lists or store pages: send to the closest page.
    redirect(1, "shop-art/", "", "Shop Prints", "the gallery")
    redirect(1, "best-sellers/", "", "Best Sellers", "the gallery")
    redirect(1, "warehouse-open-edition-prints/", "", "Warehouse - Open Edition Prints", "the gallery")
    redirect(1, "newsletter-sign-up/", "contact/", "Newsletter Sign-Up", "the contact page")

    # 404: GitHub serves it at any depth, so set <base> from the address first.
    nf = page(0, "404.html", f"Page not found | {SITE_NAME}", "This page does not exist.",
              '<h1 class="page-title">Page not found</h1>\n<p class="center">That page is gone or never existed. <a href="./">Go to the gallery</a>.</p>')
    nf = nf.replace("<head>\n", "<head>\n<script>document.write('<base href=\"' + (location.pathname.indexOf('/tophandstudio-site/') === 0 ? '/tophandstudio-site/' : '/') + '\">');</script>\n", 1)
    write("404.html", nf)

    paths = ["", "about-the-artist/", "contact/", "faq/"] + [f"{WORKS_DIR}/{w['slug']}/" for w in works]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{SITE_URL}/{p}</loc></url>\n" for p in paths) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    write(".nojekyll", "")
    print(f"Built {n} work pages into {os.path.relpath(OUT)}/")


if __name__ == "__main__":
    main()
