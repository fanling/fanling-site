"""Builds the fanling.ai static site from content.py.
python3 site.py <outdir>            -> full static site (each page a complete HTML document)
python3 site.py <outdir> --artifact -> same, but index.html without the document wrapper (for Claude preview)"""
import json
import os
import re
import shutil
import sys
from html import escape

import content as C
import diagrams as D

MEDIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400'
         '&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Noto+Serif+SC:wght@500&text=&display=swap">')
FONTS = FONTS.replace("&text=", "")

CSS = """
/* Layout: a drawing set. Left-aligned sheets, mono sheet numbers, one blue accent for what Ling designed. */
:root{--paper:#F5F6F3;--ink:#16191D;--muted:#5B636E;--rule:#C3C8CE;--accent:#2B4BC8;--tint:rgba(43,75,200,.06);
--serif:'Newsreader',Georgia,'Times New Roman',serif;--sans:'IBM Plex Sans','Helvetica Neue',Arial,sans-serif;
--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;--cjk:'Noto Serif SC','Songti SC',serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#121418;--ink:#E7E9EC;--muted:#9AA2AD;--rule:#3A4049;--accent:#8EA2FF;--tint:rgba(142,162,255,.09);color-scheme:dark}}
:root[data-theme="dark"]{--paper:#121418;--ink:#E7E9EC;--muted:#9AA2AD;--rule:#3A4049;--accent:#8EA2FF;--tint:rgba(142,162,255,.09);color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.6}
.wrap{max-width:1120px;margin:0 auto;padding-inline:clamp(16px,4vw,40px);padding-block:0 64px}
header.top{display:flex;flex-wrap:wrap;gap:12px 28px;align-items:baseline;justify-content:space-between;padding-block:22px;border-bottom:1px solid var(--ink);margin-bottom:48px}
.brand{font-family:var(--serif);font-size:22px;text-decoration:none;color:var(--ink)}
.brand .zh{font-family:var(--cjk);font-size:17px;color:var(--muted);margin-left:6px}
nav{display:flex;flex-wrap:wrap;gap:6px 20px}
nav a{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-decoration:none;padding:4px 0;border-bottom:1px solid transparent}
nav a:hover,nav a[aria-current]{color:var(--ink);border-bottom-color:var(--accent)}
a{color:inherit;text-decoration-color:var(--accent);text-underline-offset:3px}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
.eyebrow b{color:var(--accent);font-weight:500}
h1,h2,h3{font-family:var(--serif);font-weight:400;margin:0;text-wrap:balance}
h1{font-size:clamp(40px,7vw,84px);line-height:1;letter-spacing:-.015em}
h2{font-size:clamp(30px,4.4vw,48px);line-height:1.08}
h3{font-size:22px;line-height:1.25}
p{margin:0 0 14px;max-width:66ch}
.lede{font-family:var(--serif);font-style:italic;font-size:clamp(21px,2.6vw,30px);line-height:1.3;max-width:34ch;margin:22px 0 0}
section{margin-block:72px}
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:clamp(24px,5vw,64px)}
.split>*{min-width:0}
@media (max-width:760px){.split{grid-template-columns:minmax(0,1fr)!important}}
.worklist{border-top:1px solid var(--ink);margin-top:20px}
.workrow{display:grid;grid-template-columns:90px minmax(0,1fr) minmax(0,1.2fr);gap:24px;padding-block:22px;border-bottom:1px solid var(--rule);text-decoration:none;color:inherit;align-items:start}
.workrow:hover h3{color:var(--accent)}
.workrow .n{font-family:var(--serif);font-size:44px;line-height:.9;color:var(--accent)}
.workrow p{margin:0;color:var(--muted)}
@media (max-width:760px){.workrow{grid-template-columns:56px minmax(0,1fr)}.workrow p{grid-column:2}.workrow .n{font-size:32px}}
.num{font-family:var(--serif);font-size:clamp(90px,14vw,170px);line-height:.8;color:var(--accent)}
.dia-box{overflow-x:auto;margin-block:28px;padding-block:8px}
.dia-box svg{min-width:640px}
@media (max-width:600px){td.y{width:64px!important;font-size:12px;padding-right:10px;white-space:normal!important}.workrow.nonum{grid-template-columns:minmax(0,1fr)}.workrow.nonum .n{display:none}.workrow.nonum p{grid-column:1}.dia-box::before{content:"Swipe to see the full diagram →";display:block;font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--muted);margin-bottom:8px;position:sticky;left:0}}
dl.facts{border-top:1px solid var(--ink);margin:0}
dl.facts div{display:grid;grid-template-columns:minmax(0,180px) minmax(0,1fr);gap:16px;border-bottom:1px solid var(--rule);padding-block:10px}
dl.facts dt{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:3px}
dl.facts dd{margin:0}
@media (max-width:520px){dl.facts div{grid-template-columns:minmax(0,1fr);gap:2px}}
.ph{border:1px dashed var(--accent);background:var(--tint);aspect-ratio:16/9;max-width:100%;display:flex;align-items:flex-end;padding:14px;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.cols3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,3vw,40px);margin-top:56px}.cols3>div{min-width:0}.wcard{display:block;border-top:1px solid var(--ink);padding-block:18px 28px;text-decoration:none;color:inherit}.wcard:hover h3{color:var(--accent)}.wcard .n{display:block;font-family:var(--serif);font-size:34px;line-height:1;color:var(--accent);margin-bottom:12px}.wcard .eyebrow{display:block;margin:8px 0 0;font-size:11px}.wcard p{margin:12px 0 0;color:var(--muted);font-size:15px}@media (max-width:900px){.cols3{grid-template-columns:minmax(0,1fr)}}.stile{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;background:#fff;border:1px solid var(--rule);padding:0;box-sizing:border-box}div.stile{padding:10px}div.stile svg{display:block;width:100%;height:100%}.series{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:48px 32px}@media (max-width:760px){.series{grid-template-columns:minmax(0,1fr)}}.book{display:grid;grid-template-columns:minmax(0,220px) minmax(0,1fr);gap:clamp(20px,4vw,48px);border-top:1px solid var(--ink);padding-block:24px 40px}.book>img{display:block;width:100%;height:auto}@media (max-width:640px){.book{grid-template-columns:minmax(0,1fr)}.book>img{max-width:220px}}.gal{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.gal img{display:block;width:100%;height:auto;border:1px solid var(--rule)}.fig{margin:0}.fig img,.fig video{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--rule)}.portrait{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}.fig figcaption{font-size:13px;line-height:1.5;color:var(--muted);margin-top:10px}
.grid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,320px),1fr));gap:24px}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:24px}
.todo{color:var(--accent);font-family:var(--mono);font-size:.82em;border-bottom:1px dashed var(--accent)}
table{border-collapse:collapse;width:100%;font-size:15px;line-height:1.45}
.tbl{overflow-x:auto}
td{border-bottom:1px solid var(--rule);padding:12px 16px 12px 0;vertical-align:top}
td.y{font-family:var(--mono);font-size:13px;color:var(--muted);white-space:nowrap;width:120px;font-variant-numeric:tabular-nums}
td .sub{color:var(--muted)}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}.btns a{font-family:var(--mono);font-size:13px;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;border:1px solid var(--ink);padding:10px 18px}.btns a:hover{border-color:var(--accent);color:var(--accent)}
.talk{display:block;border:1px solid var(--ink);padding:22px;text-decoration:none;color:inherit;max-width:640px}
.talk:hover{border-color:var(--accent)}
.talk .go{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
footer{border-top:1px solid var(--ink);padding-top:14px;display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between;font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--muted);text-transform:uppercase}
.draft{font-family:var(--mono);font-size:12px;letter-spacing:.06em;color:var(--accent);border:1px dashed var(--accent);padding:8px 12px;margin-bottom:28px;display:inline-block}
@media (prefers-reduced-motion:no-preference){.workrow,.talk,nav a{transition:color .15s,border-color .15s}}
""" + D.SVG_CSS

CUR = ' aria-current="page"'
NAV = [("works.html", "Research"), ("works/tezign.html", "Entrepreneurship"), ("talks.html", "Talks"), ("writing.html", "Writing"), ("about.html", "About"), ("news.html", "News")]


def facts(rows):
    return '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


SITE = "https://www.fanling.ai"
_plain = lambda t: re.sub(r"<[^>]+>", "", t).strip()
DESC = {
    "index.html": C.SHORT_BIO,
    "works.html": " ".join(C.RESEARCH["body"]),
    "lab.html": "The Design AI Lab at Tongji University, founded by Ling Fan in 2017: research on creative reasoning, subjective world models and agentic creativity, research funding and doctoral and master's advising.",
    "works/tezign.html": " ".join(C.TEZIGN["body"]),
    "talks.html": "Talks and lectures by Ling Fan on Design AI and the computability of creativity, agentic transformation for business, and subjective world models.",
    "writing.html": "Books and publications by Ling Fan on design, artificial intelligence and the computability of creativity.",
    "about.html": "Ling Fan (范凌): education, academic appointments, service and recognition.",
    "news.html": "News about Ling Fan (范凌): talks, exhibitions, papers and press coverage.",
}
PERSON = {
    "@context": "https://schema.org", "@type": "Person",
    "name": "Ling Fan", "alternateName": ["范凌", "Fan Ling"],
    "url": SITE + "/", "image": SITE + "/media/portrait.jpg", "email": "mailto:lfan@tongji.edu.cn",
    "jobTitle": ["Professor in Design AI", "Founder and Chairman of Tezign"],
    "description": None,
    "affiliation": {"@type": "CollegeOrUniversity", "name": "Tongji University", "url": "https://www.tongji.edu.cn/"},
    "worksFor": [{"@type": "CollegeOrUniversity", "name": "Tongji University"}, {"@type": "Organization", "name": "Tezign", "url": "https://www.tezign.com/en"}],
    "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Harvard University Graduate School of Design"}, {"@type": "CollegeOrUniversity", "name": "Princeton University"}, {"@type": "CollegeOrUniversity", "name": "Tongji University"}],
    "knowsAbout": ["Design AI", "Computability of creativity", "Creative reasoning", "Subjective world models", "Agentic creativity", "Agentic transformation", "Design research", "Architecture"],
    "sameAs": None,
}


def _short(t, n=170):
    """Whole sentences up to about n characters, for meta descriptions."""
    out = ""
    for sent in re.split(r"(?<=[.?!])\s+", t):
        if out and len(out) + len(sent) + 1 > n:
            break
        out = (out + " " + sent).strip()
    return out if len(out) <= n + 60 else out[:n].rsplit(" ", 1)[0] + "…"


def seo_desc(path):
    if path.startswith("works/") and path != "works/tezign.html":
        w = next((w for w in C.WORKS if w["slug"] == path[6:-5]), None)
        return w["question"] if w else C.SHORT_BIO
    return DESC.get(path, C.SHORT_BIO)


def seo_head(path, title):
    url = SITE + "/" + ("" if path == "index.html" else path[:-5])
    desc = escape(_short(_plain(seo_desc(path))), quote=True)
    t = escape(title, quote=True)
    h = (f'<meta name="description" content="{desc}"><link rel="canonical" href="{url}">'
         f'<meta property="og:type" content="{"profile" if path == "index.html" else "website"}"><meta property="og:site_name" content="Ling Fan">'
         f'<meta property="og:title" content="{t}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">'
         f'<meta property="og:image" content="{SITE}/media/portrait.jpg"><meta name="twitter:card" content="summary_large_image">'
         f'<meta name="author" content="Ling Fan">')
    if path == "index.html":
        person = dict(PERSON, description=_plain(C.SHORT_BIO), sameAs=[u for _, u in C.PROFILES])
        h += '<script type="application/ld+json">' + json.dumps(person, ensure_ascii=False) + "</script>"
    return h


def page(path, title, body, artifact=False):
    depth = path.count("/")
    pre = "../" * depth
    cur = path
    home = pre or "./"
    nav = "".join(f'<a href="{home if h == "index.html" else pre + h}"{CUR if h == cur or (h == "works.html" and (cur.startswith("works/") or cur == "lab.html") and cur != "works/tezign.html") else ""}>{t}</a>' for h, t in NAV)
    inner = f"""<div class="wrap"><header class="top"><a class="brand" href="{home}">Ling Fan<span class="zh">{C.NAME_ZH}</span></a><nav aria-label="Main">{nav}</nav></header>
<main>{body}</main><footer><span>Ling Fan · Design AI</span><span>{C.CONTACT}{"".join(f' · <a href="{u}" target="_blank" rel="noopener" style="color:inherit">{n}</a>' for n, u in C.PROFILES)}</span><span>© 2026 Ling Fan</span></footer></div>"""
    head = f"<title>{escape(title)}</title>{'' if artifact else seo_head(path, title)}{FONTS}<style>{CSS}</style>"
    if artifact and path == "index.html":
        return head + inner
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'{head}</head><body>{inner}</body></html>')


def work_row(w, pre=""):
    return (f'<a class="workrow" href="{pre}works/{w["slug"]}.html"><span class="n">{w["no"] or "&nbsp;"}</span>'
            f'<div><h3>{w["title"]}</h3><span class="eyebrow" style="margin:0">{w["sub"]}</span></div><p>{w["question"]}</p></a>')


TEZIGN_LINE = "Where these works are tested at production scale."
TEZIGN_ROW = (f'<a class="workrow nonum" href="works/tezign.html"><span class="n">&nbsp;</span><div><h3>Tezign</h3>'
              f'<span class="eyebrow" style="margin:0">{C.TEZIGN["sub"]}</span></div><p>{TEZIGN_LINE}</p></a>')


ADVISING_LINE = "More than US$5 million in research funding; 8 doctoral and about 15 master's students today, and 15 master's graduates."
ADVISING_STATS = "".join(f'<div style="border-top:1px solid var(--ink);padding:12px 0 20px"><span style="display:block;font-family:var(--serif);font-size:44px;line-height:1;color:var(--accent)">{n}</span><span class="eyebrow" style="margin:8px 0 0;display:block">{l}</span></div>'
                         for n, l in [("US$5M+", "Research funding"), ("8", "Doctoral students, current"), ("~15", "Master's students, current"), ("15", "Master's graduates")])


def product_tile(name, link, desc, img, pre=""):
    if img and img.startswith("diagram:"):
        vis = f'<div class="stile">{getattr(D, img[8:])()}</div>'
    elif img:
        vis = f'<img class="stile" src="{pre}media/{img}" alt="{name}">'
    else:
        vis = f'<div class="ph stile" style="display:flex;align-items:center;justify-content:center">Image to add: {name}</div>'
    host = link.split("//")[1].split("/")[0].replace("www.", "")
    return (f'<div><a href="{link}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit">{vis}</a>'
            f'<h3 style="margin-top:14px">{name}</h3><p style="margin-top:8px">{desc}</p>'
            f'<p style="margin-top:8px"><a href="{link}" target="_blank" rel="noopener">{host} ↗</a></p></div>')


def talk_card(t):
    y, venue, title, link = t
    return (f'<a class="talk" href="{link}" target="_blank" rel="noopener"><span class="eyebrow">{y} · {venue}</span>'
            f'<h3>{title}</h3><span class="go" style="display:block;margin-top:14px">Watch on YouTube ↗</span></a>')


def work_card(w):
    n = f'<span class="n">{w["no"]}</span>' if w["no"] else ""
    return (f'<a class="wcard" href="works/{w["slug"]}.html">{n}<h3>{w["title"]}</h3>'
            f'<span class="eyebrow">{w["sub"]}</span><p>{w["question"]}</p></a>')


def media_html(m, pre=""):
    cap = f'<figcaption>{m["caption"]}</figcaption>'
    if "gallery" in m:
        tiles = "".join(f'<a href="{pre}media/{f}" target="_blank" rel="noopener"><img loading="lazy" src="{pre}media/{f}" alt="Timeline panel {i + 1}"></a>'
                        for i, f in enumerate(m["gallery"]))
        return f'<figure class="fig" style="grid-column:1/-1"><div class="gal">{tiles}</div>{cap}</figure>'
    if "video" in m:
        return (f'<figure class="fig" style="grid-column:1/-1"><video controls playsinline preload="none" poster="{pre}media/{m["poster"]}">'
                f'<source src="{pre}media/{m["video"]}" type="video/mp4"></video>{cap}</figure>')
    return f'<figure class="fig"><img loading="lazy" src="{pre}media/{m["image"]}" alt="">{cap}</figure>'


def build(out, artifact=False):
    pages = {}
    ps = lambda xs: "".join(f"<p>{x}</p>" for x in xs)

    pages["index.html"] = ("Ling Fan 范凌 · Researcher, Entrepreneur in Design AI", f"""
<div class="split" style="align-items:center;grid-template-columns:minmax(0,1.5fr) minmax(0,.8fr)"><div><h1 style="font-size:clamp(40px,6vw,68px)">{C.HEADLINE}</h1>
<p style="margin-top:24px">{C.SHORT_BIO}</p>
<div class="btns"><a href="works.html">Research</a><a href="works/tezign.html">Entrepreneurship</a><a href="writing.html">Writing</a></div></div>
<img class="portrait" src="media/portrait.jpg" alt="Ling Fan"></div>
<section><p class="eyebrow">Current research · {C.RESEARCH['title']}</p><div class="worklist">{''.join(work_row(w) for w in C.CURRENT_WORKS)}</div></section>
<section><p class="eyebrow">Entrepreneurship</p><div class="worklist">{TEZIGN_ROW}</div></section>
<section><p class="eyebrow">Selected talks</p><div class="grid2">{''.join(talk_card(t) for t in C.TALKS if t[3] and "youtu" in t[3])}</div></section>""")

    pages["works.html"] = ("Research · Ling Fan", f"""
<p class="eyebrow">Research</p><h1>{C.RESEARCH['title']}</h1>
{''.join(f'<p class="lede">{p}</p>' for p in C.RESEARCH['body'])}
<section><p class="eyebrow">The Lab</p><div class="worklist"><a class="workrow nonum" href="lab.html"><span class="n">&nbsp;</span><div><h3>{C.LAB['title']}</h3><span class="eyebrow" style="margin:0">Tongji University, since 2017</span></div><p>{ADVISING_LINE}</p></a></div></section>
<section><p class="eyebrow">Current research</p><div class="worklist">{''.join(work_row(w, "") for w in C.CURRENT_WORKS)}</div></section>
<section><p class="eyebrow">Past research</p><div class="worklist">{''.join(work_row(w, "") for w in C.PAST_WORKS)}</div></section>""")

    fund_rows = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{t}</b><br><span class="sub">{f}</span></td></tr>' for y, t, f in C.LAB["funded"])
    adv = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{n}</b><br>{t}</td></tr>' for y, n, t in C.ADVISING["doctoral"])
    pages["lab.html"] = ("Design AI Lab · Ling Fan", f"""
<p class="eyebrow">Research</p><h1>{C.LAB['title']}</h1>
<div class="split" style="margin-top:36px"><div>{ps(C.LAB['body'])}</div><div class="stats">{ADVISING_STATS}</div></div>
<section><p class="eyebrow">Research funding</p><p>More than US$5 million in cumulative research funding. Representative projects:</p><div class="tbl"><table>{fund_rows}</table></div></section>
<section><p class="eyebrow">Student advising · doctoral students</p><p>Listed by year of entry, with dissertation titles.</p><div class="tbl"><table>{adv}</table></div></section>""")

    for i, w in enumerate(C.WORKS):
        nxt = C.WORKS[(i + 1) % len(C.WORKS)]
        series = media_sec = ""
        if "parts" in w:
            pm = {m["part"]: m for m in w.get("media", []) if m.get("part")}
            def tile(k, t):
                m = pm.get(k)
                if not m:
                    return f'<div class="ph">Image: {t}</div>'
                if "video" in m:
                    return (f'<figure class="fig"><video controls playsinline preload="none" poster="../media/{m["poster"]}">'
                            f'<source src="../media/{m["video"]}" type="video/mp4"></video><figcaption>{m["caption"]}</figcaption></figure>')
                if "diagram" in m:
                    return f'<figure class="fig"><div class="stile">{getattr(D, m["diagram"])()}</div></figure>'
                return f'<figure class="fig"><img class="stile" src="../media/{m["image"]}" alt="{m["caption"]}"></figure>'
            series = '<section><p class="eyebrow">' + ("Two studies" if len(w["parts"]) == 2 else "The series") + '</p><div class="series">' + "".join(
                f'<div>{tile(k, t)}<p class="eyebrow" style="margin:12px 0 4px"><b>({k})</b></p><h3>{t}</h3><p style="margin-top:8px">{d}</p></div>'
                for k, t, d in w["parts"]) + "</div></section>"
        rest = [m for m in w.get("media", []) if m.get("web", True) and not m.get("part")]
        if rest or w["images"] or "figure" in w:
            web = sorted(rest, key=lambda m: "video" not in m)
            imgs = [media_html(m, "../") for m in web]
            imgs += [f'<div class="ph">Image to add: {t}</div>' for t in w["images"]]
            if "figure" in w:
                fn, cap = w["figure"]
                fig = f'<figure class="fig">{getattr(D, fn)()}' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
                nv = sum("video" in m for m in web)
                imgs = imgs[:nv] + [fig] + imgs[nv:]
            media_sec = f'<section><p class="eyebrow">{w.get("media_label", "In use")}</p><div class="grid2">' + "".join(imgs) + "</div></section>"
        links = "".join(f'<p><a href="{u}" target="_blank" rel="noopener">{t} ↗</a></p>' for t, u in w["links"])
        pages[f"works/{w['slug']}.html"] = (f"{w['title']} · Ling Fan", f"""
<p class="eyebrow"><b>{w['label']}</b> · {w['sub']}</p>
<div class="split"><div>{f'<div class="num">{w["no"]}</div>' if w['no'] else ''}<h1 style="margin-top:24px;font-size:clamp(36px,5vw,60px)">{w['title']}</h1><p class="lede">{w['question']}</p></div>
<div style="padding-top:12px">{ps(w['body'])}{links}</div></div>
{series if w.get("parts_first") else ""}
<section><p class="eyebrow">{w.get('diagram_label') or ('Structure' if w['diagram'] else 'Facts')}</p>{f'<div class="dia-box">{getattr(D, w["diagram"])()}</div>' if w['diagram'] else ''}{f'<div class="dia-box">{getattr(D, w["diagram_extra"])()}</div>' if w.get('diagram_extra') else ''}{f'<p class="eyebrow" style="text-transform:none;letter-spacing:0;font-family:var(--sans);font-size:13px">{w["diagram_source"]}</p>' if w.get('diagram_source') else ''}{'' if w.get("parts_first") else facts(w['facts'])}</section>
{"" if w.get("parts_first") else series}{media_sec}{('<section><p class="eyebrow">Facts</p>' + facts(w['facts']) + '</section>') if w.get("parts_first") else ''}
<p><a href="{nxt['slug']}.html">Next: {nxt['label']} · {nxt['title']} →</a></p>""")

    pages["works/tezign.html"] = ("Tezign · Ling Fan", f"""
<p class="eyebrow">Entrepreneurship</p><h1>{C.TEZIGN['page_title']}</h1>
{''.join(f'<p class="lede">{p}</p>' for p in C.TEZIGN['body'])}
<section><p class="eyebrow">The Company</p><div class="worklist"><a class="workrow nonum" href="https://www.tezign.com/en" target="_blank" rel="noopener"><span class="n">&nbsp;</span><div><h3>Tezign ↗</h3><span class="eyebrow" style="margin:0">{C.TEZIGN['sub']}</span></div><p>{" ".join(C.TEZIGN['company'])}</p></a></div></section>
<section><p class="eyebrow">Products</p><div class="series">{"".join(product_tile(*p_, pre="../") for p_ in C.TEZIGN["products"])}</div></section>""")

    pub_row = lambda y, a, t, v, d: (f'<tr><td class="y">{y}</td><td>{a} {t} <i>{v}</i>' + (f' <a href="{d}" target="_blank" rel="noopener">{d.replace("https://doi.org/", "doi:").replace("https://arxiv.org/abs/", "arXiv:")}</a>' if d else "") + "</td></tr>")
    pubs = "".join(f'<h3 style="margin:40px 0 8px;font-size:20px">{cat}</h3><div class="tbl"><table>{"".join(pub_row(*r) for r in rs)}</table></div>' for cat, rs in C.PUBLICATIONS)
    fund = "".join(f'<tr><td class="y">{y}</td><td>{t}<br><span class="sub">{s}</span></td></tr>' for y, t, s in C.LAB["funded"])
    pats = "".join(f'<tr><td class="y">{no}</td><td>{t}</td></tr>' for t, no in C.PATENTS)
    talks = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{v}</b><br>{t}' + (f'<br><a href="{u}" target="_blank" rel="noopener">{"Course summary ↗" if "sohu.com" in u else "Watch ↗"}</a>' if u else "") + "</td></tr>" for y, v, t, u in C.TALKS)
    pages["talks.html"] = ("Talks · Ling Fan", f"""
<p class="eyebrow">Talks</p><h1>Talks and lectures</h1>
<p class="lede">{C.TALKS_INTRO["body"]}</p>
<ol style="margin:14px 0 20px;padding-left:24px;font-size:19px;line-height:1.6">{"".join(f"<li>{t}</li>" for t in C.TALKS_INTRO["topics"])}</ol>
<p>{C.TALKS_INTRO["contact"].replace("lfan@tongji.edu.cn", '<a href="mailto:lfan@tongji.edu.cn">lfan@tongji.edu.cn</a>')}</p>
<section><div class="tbl"><table>{talks}</table></div></section>""")

    def book(y, t, p):
        if y not in C.BOOK_PHOTOS:
            return f'<div class="book"><div></div><div><p class="eyebrow">{y} · {p}</p><h3><i>{t}</i></h3></div></div>'
        cover, spreads = C.BOOK_PHOTOS[y]
        sp = "".join(f'<figure class="fig"><img loading="lazy" src="media/{f}" alt=""><figcaption>{c}</figcaption></figure>' for f, c in spreads)
        return (f'<div class="book"><img src="media/{cover}" alt="Cover of {escape(t)}"><div><p class="eyebrow">{y} · {p}</p>'
                f'<h3><i>{t}</i></h3><div class="grid2" style="margin-top:24px">{sp}</div></div></div>')
    BLOG_SECTION = (f'''<section><p class="eyebrow">Blog</p><p><a href="{dict(C.PROFILES)['Substack']}" target="_blank" rel="noopener"><i>{C.BLOG[0]}</i> ↗</a><br><span style="color:var(--muted)">{C.BLOG[1]}</span></p></section>''' if C.BLOG and 'Substack' in dict(C.PROFILES) else '')
    pages["writing.html"] = ("Writing · Ling Fan", f"""
<p class="eyebrow">Writing</p><h1>{"Blog, books and publications" if C.BLOG else "Books and publications"}</h1>
{BLOG_SECTION}
<section><p class="eyebrow">Books</p>{''.join(book(*b) for b in C.WRITING['books'])}</section>
<section><p class="eyebrow">Publications</p><p>Authored or co-authored more than 100 articles and papers in academic journals, professional magazines and conference proceedings.</p>{pubs}</section>""")

    appts = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{i}</b><br>{r}</td></tr>' for y, i, r in C.APPOINTMENTS)
    edu = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{i}</b>, {d}</td></tr>' for y, i, d in C.EDUCATION)
    hon = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.HONORS)
    svc = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.SERVICE)
    media = "".join(f"<li>{m}</li>" for m in C.MEDIA)
    pages["about.html"] = ("About · Ling Fan", f"""
<p class="eyebrow">About</p><h1>Ling Fan <span style="font-family:var(--cjk);font-size:.55em;color:var(--muted)">{C.NAME_ZH}</span></h1>
<div class="split" style="margin-top:36px"><div><img class="portrait" src="media/portrait.jpg" alt="Ling Fan"></div><div>{ps([C.SHORT_BIO])}
<p>His work has been covered by Bloomberg, Forbes and Harvard Business Review.</p>
<p>Contact: <span style="user-select:all">{C.CONTACT}</span></p><p>{" · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n} ↗</a>' for n, u in C.PROFILES)}</p></div></div>
<section class="split"><h2>Education</h2><div class="tbl"><table>{edu}</table></div></section>
<section class="split"><h2>Academic experience</h2><div class="tbl"><table>{appts}</table></div></section>
<section class="split"><h2>Other service</h2><div class="tbl"><table>{svc}</table></div></section>
<section class="split"><h2>Recognition</h2><div class="tbl"><table>{hon}</table></div></section>""")

    news = "".join(f'<tr><td class="y">{d}</td><td>{t}' + (f' <a href="{u}" target="_blank" rel="noopener">↗</a>' if u else "") + "</td></tr>" for d, t, u in C.NEWS)
    pages["news.html"] = ("News · Ling Fan", f"""
<p class="eyebrow">News</p><h1>News</h1>
<section><div class="tbl"><table>{news}</table></div></section>""")

    os.makedirs(os.path.join(out, "media"), exist_ok=True)
    for f in os.listdir(MEDIA):
        shutil.copy(os.path.join(MEDIA, f), os.path.join(out, "media", f))
    for path, (title, body) in pages.items():
        fp = os.path.join(out, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w").write(page(path, title, body, artifact))
    if not artifact:
        urls = "".join(f"<url><loc>{SITE}/{'' if p == 'index.html' else p[:-5]}</loc></url>" for p in pages)
        open(os.path.join(out, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>\n")
        open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
        open(os.path.join(out, "llms.txt"), "w").write(llms_txt(pages))
    return list(pages)


def llms_txt(pages):
    """A plain-text summary for AI search engines and assistants (llmstxt.org)."""
    L = [f"# Ling Fan (范凌)", "", f"> {_plain(C.SHORT_BIO)}", "",
         f"Research question: {_plain(' '.join(C.RESEARCH['body']))}", "",
         f"Contact: {C.CONTACT}. Talks: {_plain(C.TALKS_INTRO['body'])} " + "; ".join(C.TALKS_INTRO["topics"]) + ".", "", "## Pages", ""]
    for p, (title, _) in pages.items():
        L.append(f"- [{title}]({SITE}/{'' if p == 'index.html' else p[:-5]}): {_plain(seo_desc(p))}")
    L += ["", "## Current research", ""] + [f"- {w['title']}: {_plain(w['question'])}" for w in C.CURRENT_WORKS]
    L += ["", "## Entrepreneurship", "", _plain(" ".join(C.TEZIGN["company"]))]
    L += [f"- {n} ({u}): {_plain(d)}" for n, u, d, _ in C.TEZIGN["products"]]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    print(build(sys.argv[1], "--artifact" in sys.argv))
