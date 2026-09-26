#!/usr/bin/env python3
"""Builds index.html (English) and fr/index.html (French) from one template,
plus sitemap.xml. Run from the repository root: python3 build.py"""
import json, os, html

BASE = "https://arthurpierrey.github.io/cadence/"
STORE = "https://apps.apple.com/app/id6788449816"
MAIL = "arthur.pierrey@gmail.com"

T = {
 "en": dict(
  path="", lang="en",
  title="Cadence: Focus Timer & App Blocker for iPhone and Mac",
  desc="A focus timer with a living woodblock-print tide. Blocks distracting apps and websites during focus and at night, reminds you to stand up, and syncs iPhone and Mac. No subscription.",
  h1="Cadence", tag="Focus timer and app blocker for iPhone, iPad and Mac.",
  lede="Thirty minutes of deep work, then three on your feet. The sea rises while you focus and recedes while you move, under a living woodblock-print sky that follows your real day and your local weather.",
  cta="Download on the App Store", free="Free download. Blocking is free for three focus sessions, then one purchase unlocks it for good on all your devices. No subscription.",
  feats_h="What it does",
  feats=[
   ("A focus timer that makes you move", "Thirty minutes of focus and a three-minute movement break by default, adjustable from 10 to 50 minutes. The break is a tenth of the time you worked, and it starts on its own so you actually stand up."),
   ("Blocks distracting apps and websites", "Pick the apps to block during a focus with Apple's Screen Time picker. The websites of the social apps on your phone are blocked too, in Safari and in other browsers."),
   ("A curfew for your nights", "Choose two hours, say 11 pm to 7 am, and the apps you picked lock themselves every night, even when Cadence is closed. A countdown on the Mac warns you ten minutes before."),
   ("Deep work mode", "When you turn it on, a focus cannot be ended early. The bell decides."),
   ("iPhone, iPad and Mac, in sync", "A native Mac app with its menu bar timer, hiding the apps you choose. Your sessions, settings and curfew follow you through iCloud."),
   ("Siri, widgets, Live Activity", "Start or end a focus with Siri or the Control Center, and watch the tide in the Dynamic Island."),
  ],
  why_h="Why stand up every half hour",
  why="Sitting is not the whole problem; sitting without a break is. Studies on uninterrupted sedentary time (Diaz et al., 2017; Duran et al., 2023) and the WHO 2020 guidelines point the same way: break it up often. Cadence is built around that rhythm.",
  shots_alt=("A focus at dusk: the tide rises under a setting sun", "A movement break at dawn", "Statistics: focus time by day and by type"),
  mac_alt="Cadence on the Mac: the tide in a resizable window",
  priv_h="Private by design",
  priv="No account, no ads, no tracking. Cadence collects no data: your history stays on your devices and in your own iCloud.",
  faq_h="Questions",
  faq=[
   ("How do I block apps at night on iPhone?", "Turn on the curfew in Cadence, set its hours and choose the apps to block. Every night, at the time you set, iOS locks those apps until the morning, even if Cadence is not open."),
   ("Is Cadence a Pomodoro timer?", "It works like one, with a health twist: thirty minutes of focus, then a short break spent on your feet. The length of the focus is adjustable."),
   ("Does it block websites in Chrome, not only Safari?", "Yes. During a focus, the websites of the social apps installed on your phone are blocked in every browser on iOS, Chrome included."),
   ("Is there a subscription?", "No. Cadence is free to download. Blocking is free for three focus sessions; after that, Cadence Premium is a single one-time purchase that covers your iPhone, iPad and Mac."),
   ("Does it work on the Mac?", "Yes, as a native Mac app from the Mac App Store. It hides the apps you choose during a focus and can cover the whole screen during your curfew."),
  ],
  lang_link=("Français", "fr/"), privacy="Privacy Policy", contact="Contact",
 ),
 "fr": dict(
  path="fr/", lang="fr",
  title="Cadence : minuteur de focus et blocage d'apps pour iPhone et Mac",
  desc="Un minuteur de focus avec une marée vivante façon estampe. Bloque les apps et les sites qui distraient pendant le focus et la nuit, rappelle de se lever, synchronise iPhone et Mac. Sans abonnement.",
  h1="Cadence", tag="Minuteur de focus et blocage d'apps pour iPhone, iPad et Mac.",
  lede="Trente minutes de travail profond, puis trois debout. La mer monte pendant le focus et redescend pendant que tu bouges, sous un ciel d'estampe vivant qui suit ta vraie journée et la météo locale.",
  cta="Télécharger dans l'App Store", free="Téléchargement gratuit. Le blocage est gratuit pendant trois focus, puis un seul achat le débloque pour toujours sur tous tes appareils. Sans abonnement.",
  feats_h="Ce que fait Cadence",
  feats=[
   ("Un minuteur de focus qui fait bouger", "Trente minutes de focus et trois minutes de pause debout par défaut, réglable de 10 à 50 minutes. La pause vaut un dixième du temps travaillé, et elle démarre seule pour que tu te lèves vraiment."),
   ("Bloque les apps et les sites qui distraient", "Choisis les apps à bloquer pendant le focus avec le sélecteur Temps d'écran d'Apple. Les sites des réseaux sociaux installés sur ton iPhone sont bloqués aussi, dans Safari et dans les autres navigateurs."),
   ("Un couvre-feu pour tes nuits", "Choisis deux heures, par exemple 23 h et 7 h : les apps choisies se verrouillent chaque nuit, même Cadence fermée. Sur Mac, un compte à rebours prévient dix minutes avant."),
   ("Mode travail profond", "Une fois activé, un focus ne peut plus être arrêté avant la fin. C'est la cloche qui décide."),
   ("iPhone, iPad et Mac, synchronisés", "Une vraie app Mac avec son minuteur dans la barre des menus, qui masque les apps choisies. Sessions, réglages et couvre-feu te suivent par iCloud."),
   ("Siri, widgets, Live Activity", "Lance ou termine un focus avec Siri ou le Centre de contrôle, et suis la marée dans la Dynamic Island."),
  ],
  why_h="Pourquoi se lever toutes les demi-heures",
  why="Être assis n'est pas tout le problème ; rester assis sans interruption, si. Les études sur le temps sédentaire ininterrompu (Diaz et al., 2017 ; Duran et al., 2023) et les recommandations 2020 de l'OMS vont dans le même sens : le couper souvent. Cadence est construit autour de ce rythme.",
  shots_alt=("Un focus au crépuscule : la marée monte sous le soleil couchant", "Une pause debout à l'aube", "Statistiques : temps de focus par jour et par type"),
  mac_alt="Cadence sur Mac : la marée dans une fenêtre redimensionnable",
  priv_h="Confidentiel par conception",
  priv="Pas de compte, pas de publicité, pas de pistage. Cadence ne collecte aucune donnée : ton historique reste sur tes appareils et dans ton propre iCloud.",
  faq_h="Questions",
  faq=[
   ("Comment bloquer des apps la nuit sur iPhone ?", "Active le couvre-feu dans Cadence, règle ses heures et choisis les apps à bloquer. Chaque nuit, à l'heure dite, iOS verrouille ces apps jusqu'au matin, même si Cadence n'est pas ouverte."),
   ("Cadence est-il un minuteur Pomodoro ?", "Il en reprend le principe, avec un parti pris santé : trente minutes de focus, puis une courte pause debout. La durée du focus est réglable."),
   ("Les sites sont-ils bloqués dans Chrome, pas seulement Safari ?", "Oui. Pendant un focus, les sites des réseaux sociaux installés sur ton iPhone sont bloqués dans tous les navigateurs iOS, Chrome compris."),
   ("Y a-t-il un abonnement ?", "Non. Cadence est gratuit au téléchargement. Le blocage est gratuit pendant trois focus ; ensuite Cadence Premium est un achat unique qui vaut pour l'iPhone, l'iPad et le Mac."),
   ("Cadence marche-t-il sur Mac ?", "Oui, en app Mac native sur le Mac App Store. Elle masque les apps choisies pendant un focus et peut couvrir tout l'écran pendant le couvre-feu."),
  ],
  lang_link=("English", "../"), privacy="Confidentialité", contact="Contact",
 ),
}

CSS = """
:root{--paper:#f7f0e1;--ink:#22333b;--prussian:#122c44;--seal:#c34f41;--muted:#5b6b73;--card:#efe6cf}
@media (prefers-color-scheme:dark){:root{--paper:#101e30;--ink:#efe6cf;--muted:#a9b3b8;--card:#172a40}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.65}
main{max-width:980px;margin:0 auto;padding:48px 20px 24px}
header.hero{display:grid;gap:28px;align-items:center}
@media(min-width:760px){header.hero{grid-template-columns:1.2fr .8fr}}
h1{font-size:2.6rem;letter-spacing:.3em;text-transform:uppercase;font-weight:500;margin:0 0 6px}
.tag{font-size:1.25rem;margin:0 0 16px}
.lede{font-size:1.05rem}
.cta{display:inline-block;background:var(--seal);color:#f7f0e1;border-radius:999px;padding:12px 28px;text-decoration:none;font-size:1.05rem;margin:8px 0}
.free{font-size:.92rem;color:var(--muted)}
.hero img{width:100%;max-width:300px;height:auto;border-radius:28px;justify-self:center;box-shadow:0 12px 40px rgba(0,0,0,.25)}
h2{font-weight:500;font-size:1.5rem;margin:56px 0 16px}
.feats{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.feat{background:var(--card);border-radius:16px;padding:18px 20px}
.feat h3{margin:0 0 6px;font-size:1.08rem;font-weight:600}
.feat p{margin:0;font-size:.97rem}
.shots{display:flex;gap:16px;overflow-x:auto;padding-bottom:8px}
.shots img{height:420px;width:auto;border-radius:22px;flex:none}
.mac img{width:100%;height:auto;border-radius:14px}
details{border-top:1px solid rgba(127,127,127,.3);padding:12px 0}
summary{cursor:pointer;font-weight:600}
footer{max-width:980px;margin:0 auto;padding:32px 20px 56px;font-size:.88rem;color:var(--muted)}
footer a{color:inherit}
"""

def page(k):
    t = T[k]; e = html.escape
    here = BASE + t["path"]; other = {"en": BASE, "fr": BASE + "fr/"}
    root = "" if k == "en" else "../"
    ld_app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Cadence",
              "operatingSystem": "iOS, iPadOS, macOS", "applicationCategory": "ProductivityApplication",
              "description": t["desc"], "url": here, "downloadUrl": STORE, "image": BASE + "img/og.jpg",
              "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
              "author": {"@type": "Person", "name": "Arthur Pierrey"}}
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    feats = "\n".join(f'<div class="feat"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["feats"])
    shots = "\n".join(f'<img src="{root}img/{k}-{n}.jpg" width="540" height="1173" loading="lazy" alt="{e(a)}">'
                      for n, a in zip(("focus", "break", "stats"), t["shots_alt"]))
    faq = "\n".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{other['en']}">
<link rel="alternate" hreflang="fr" href="{other['fr']}">
<link rel="alternate" hreflang="x-default" href="{other['en']}">
<meta name="apple-itunes-app" content="app-id=6788449816">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{here}">
<meta property="og:image" content="{BASE}img/og.jpg">
<meta property="og:locale" content="{'en_US' if k == 'en' else 'fr_FR'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#122c44">
<script type="application/ld+json">{json.dumps(ld_app, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<main>
<header class="hero">
<div>
<h1>{e(t['h1'])}</h1>
<p class="tag">{e(t['tag'])}</p>
<p class="lede">{e(t['lede'])}</p>
<a class="cta" href="{STORE}">{e(t['cta'])}</a>
<p class="free">{e(t['free'])}</p>
</div>
<img src="{root}img/{k}-focus.jpg" width="540" height="1173" alt="{e(t['shots_alt'][0])}">
</header>
<h2>{e(t['feats_h'])}</h2>
<div class="feats">
{feats}
</div>
<h2>Mac</h2>
<div class="mac"><img src="{root}img/mac.jpg" width="1200" height="675" loading="lazy" alt="{e(t['mac_alt'])}"></div>
<h2>{e(t['why_h'])}</h2>
<p>{e(t['why'])}</p>
<div class="shots">
{shots}
</div>
<h2>{e(t['priv_h'])}</h2>
<p>{e(t['priv'])}</p>
<h2>{e(t['faq_h'])}</h2>
{faq}
</main>
<footer>&copy; 2026 Cadence &middot; <a href="{root}privacy.html">{e(t['privacy'])}</a> &middot; <a href="mailto:{MAIL}">{e(t['contact'])}</a> &middot; <a href="{t['lang_link'][1]}" hreflang="{'fr' if k == 'en' else 'en'}">{e(t['lang_link'][0])}</a></footer>
</body>
</html>
"""

os.makedirs("fr", exist_ok=True)
open("index.html", "w").write(page("en"))
open("fr/index.html", "w").write(page("fr"))
open("sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<url><loc>{BASE}</loc><xhtml:link rel="alternate" hreflang="fr" href="{BASE}fr/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}"/></url>
<url><loc>{BASE}fr/</loc><xhtml:link rel="alternate" hreflang="fr" href="{BASE}fr/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}"/></url>
<url><loc>{BASE}privacy.html</loc></url>
</urlset>
""")
print("built")
