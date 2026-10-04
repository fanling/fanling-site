"""Builds the GSD portfolio as print HTML (US Letter, landscape) for Chromium to turn into PDF."""
import content as C
import diagrams as D

TOKENS = """
:root{--paper:#F5F6F3;--ink:#16191D;--muted:#5D6570;--rule:#B9BFC6;--accent:#2B4BC8;--tint:rgba(43,75,200,.06);
--serif:'Newsreader',Georgia,serif;--sans:'IBM Plex Sans',Helvetica,Arial,sans-serif;--mono:'IBM Plex Mono',Menlo,monospace;
--cjk:'Noto Serif SC',serif}
"""

CSS = TOKENS + D.SVG_CSS + """
@page{size:11in 8.5in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:11in;height:8.5in;position:relative;padding:.6in .7in .95in;overflow:hidden;page-break-after:always;background:var(--paper)}
.pg:last-child{page-break-after:auto}
.tb{position:absolute;left:.7in;right:.7in;bottom:.42in;border-top:1px solid var(--ink);padding-top:7px;display:grid;
grid-template-columns:1.4fr 2fr .6fr;font-family:var(--mono);font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.tb span:last-child{text-align:right;color:var(--ink)}
.eyebrow{font-family:var(--mono);font-size:9pt;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
.eyebrow b{color:var(--accent);font-weight:500}
h1,h2,h3{font-family:var(--serif);font-weight:400;margin:0;text-wrap:balance}
h1{font-size:64pt;line-height:1;letter-spacing:-.01em}
h2{font-size:34pt;line-height:1.05;letter-spacing:-.005em}
h3{font-size:15pt;line-height:1.2}
p{font-size:10.5pt;line-height:1.55;margin:0 0 10px;max-width:62ch}
.lede{font-family:var(--serif);font-size:17pt;line-height:1.35;font-style:italic;max-width:40ch;margin:18px 0 0}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:.45in}
.facts{border-top:1px solid var(--ink);margin:0;padding:0}
.facts div{break-inside:avoid;display:grid;grid-template-columns:1.6in 1fr;gap:12px;border-bottom:1px solid var(--rule);padding:7px 0;font-size:9.5pt;line-height:1.4}
.facts dt{font-family:var(--mono);font-size:8pt;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:2px}
.facts dd{margin:0}
.stack div{grid-template-columns:1fr;gap:2px}
.ph{border:1px dashed var(--accent);display:flex;align-items:flex-end;padding:12px;font-family:var(--mono);font-size:8.5pt;
letter-spacing:.06em;color:var(--accent);text-transform:uppercase;background:var(--tint)}
.todo{color:var(--accent);font-family:var(--mono);font-size:.82em;letter-spacing:.02em;border-bottom:1px dashed var(--accent)}
.num{font-family:var(--serif);font-size:120pt;line-height:.8;color:var(--accent)}
table{border-collapse:collapse;width:100%;font-size:9.2pt;line-height:1.38}
td{border-bottom:1px solid var(--rule);padding:6px 10px 6px 0;vertical-align:top}
td.y{font-family:var(--mono);font-size:8.5pt;color:var(--muted);width:.95in;white-space:nowrap}
a{color:inherit;text-decoration:none;border-bottom:1px solid var(--accent)}
.zh{font-family:var(--cjk);font-weight:500}
"""


def tb(left, sheet, n):
    return f'<div class="tb"><span>Ling Fan · Design AI</span><span>{left}</span><span>{sheet} · {n:02d}</span></div>'


def facts(rows):
    return '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def build():
    pages = []
    n = [0]

    def page(inner, left, sheet, extra_cls=""):
        n[0] += 1
        pages.append(f'<section class="pg {extra_cls}">{inner}{tb(left, sheet, n[0])}</section>')

    # Cover
    page(f"""
<div style="display:grid;grid-template-rows:auto 1fr auto;height:100%">
 <p class="eyebrow">Portfolio · R. Buckminster Fuller Professor in Practice of Design Science · Harvard Graduate School of Design</p>
 <div style="align-self:center;display:grid;grid-template-columns:1fr 2.9in;gap:.45in;align-items:center">
  <div><h1>Ling Fan <span class="zh" style="font-size:40pt;color:var(--muted)">{C.NAME_ZH}</span></h1>
  <p class="lede" style="font-size:24pt;max-width:30ch">{C.HEADLINE}</p></div>
  <img src="media/portrait.jpg" alt="" style="display:block;width:2.9in;height:3.62in;object-fit:cover">
 </div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in;align-items:end">
  <p style="max-width:56ch">{C.SHORT_BIO}</p>
  <p class="eyebrow" style="text-align:right;margin:0">October 2026</p>
 </div>
</div>""", "Portfolio", "A-00")

    # Contents
    toc = [("Statement", "Design AI"), ("Overview", "The body of work")]
    toc += [(w["label"], w["title"]) for w in C.WORKS]
    toc += [("Entrepreneurship", "Tezign"), ("Research", "Design AI Lab, Tongji University"), ("Student advising", "Doctoral and master's students"),
            ("Talks", "Selected talks and keynotes"), ("Publications", "Selected"), ("Record", "Appointments, education, recognition")]
    rows = "".join(f'<tr><td class="y">{a}</td><td style="font-family:var(--serif);font-size:13pt">{b}</td></tr>' for a, b in toc)
    page(f"""<p class="eyebrow">Contents</p><div class="cols"><div><h2>The works in this portfolio are models, datasets, agents and institutions.</h2>
<p style="margin-top:18px">Each is presented as an architect presents a project: the question it answers, its structure, how it performs in use. Links in this document are live.</p></div>
<table>{rows}</table></div>""", "Contents", "A-01")

    # Statement
    paras = "".join(f"<p>{p}</p>" for p in C.STATEMENT)
    page(f"""<div style="display:grid;grid-template-columns:auto 1fr;gap:.5in;align-items:end;margin-bottom:22px"><div><p class="eyebrow">Statement</p><h2>Design AI</h2></div>
<p class="lede" style="margin:0;max-width:none">{C.THESIS}</p></div>
<div style="columns:3;column-gap:.35in;font-size:0">{paras.replace('<p>','<p style="font-size:9.8pt">')}</div>
<div style="position:absolute;left:.7in;right:.7in;bottom:1.05in">{D.lineage()}</div>""", "Statement", "A-02")

    # Overview
    page(f"""<div style="display:grid;grid-template-columns:auto 1fr;gap:.5in;align-items:end;margin-bottom:18px"><div><p class="eyebrow">Overview</p><h2>One body of work</h2></div>
<p style="margin:0">A computable ground of data and knowledge, built in past research, supports three current works (01–03). Tezign and atypica.AI put them into use, and use returns evidence and new questions to the Lab.</p></div>
<div style="width:92%;margin:0 auto">{D.overview()}</div>""", "Overview", "A-03")

    # Works
    for w in C.WORKS:
        sheet = w["sheet"]
        _n = iter(range(1, 20))
        nx = lambda: f"{sheet}.{next(_n)}"
        def series_page():
            pm = {m["part"]: m for m in w.get("media", []) if m.get("part")}
            def still(k, t):
                m = pm.get(k)
                if m and "diagram" in m:
                    return f'<div class="stl" style="height:1.7in;border:1px solid var(--rule);background:#fff;padding:.06in;overflow:hidden"><style>.stl svg{{display:block;width:100%;height:100%}}</style>{getattr(D, m["diagram"])()}</div>'
                if m:
                    return f'<img src="media/{m.get("poster") or m["image"]}" alt="" style="display:block;width:100%;height:1.7in;object-fit:cover;border:1px solid var(--rule)">'
                return f'<div class="ph" style="height:1.7in">Image: {t}</div>'
            n = len(w["parts"])
            fs = "9.5pt" if n > 2 else "9pt"
            tiles = "".join(f"""<div>{still(k, t)}
<p class="eyebrow" style="margin:10px 0 4px"><b>({k})</b></p><h3>{t}</h3><p style="font-size:{fs};margin-top:6px">{d}</p></div>""" for k, t, d in w["parts"])
            page(f"""<p class="eyebrow"><b>{w['label']}</b> · {"Two studies" if n == 2 else "The series"}</p>
<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:{'.45in' if n == 2 else '.25in'}">{tiles}</div>""", w["title"], nx())
        body = "".join(f"<p>{p}</p>" for p in w["body"])
        if "figure" in w:
            fn, cap = w["figure"]
            img = (f'<div style="margin-top:auto;padding:16px 0 .04in">{getattr(D, fn)()}'
                   f'<p class="cap" style="margin-top:8px;font-size:7.5pt;color:var(--muted)">{cap}</p></div>')
        elif any(m.get("opener") for m in w.get("media", [])):
            m = next(m for m in w["media"] if m.get("opener"))
            img = (f'<div style="margin-top:auto;padding:16px 0 .04in"><img src="media/{m["image"]}" alt="" style="display:block;width:100%;max-height:2.2in;object-fit:contain;object-position:left">'
                   f'<p class="cap" style="margin-top:8px;font-size:7.5pt;color:var(--muted)">{m["caption"]}</p></div>')
        else:
            img = "" if "parts" in w or not w["images"] else f'<div class="ph" style="flex:1;min-height:1.3in;margin:22px 0 .1in">Image to add: {w["images"][0]}</div>'
        page(f"""<div style="display:grid;grid-template-columns:1.1fr 1.4fr;gap:.45in;height:100%">
<div style="display:flex;flex-direction:column"><p class="eyebrow"><b>{w['label']}</b> · {w['sub']}</p>{f'<div class="num">{w["no"]}</div>' if w['no'] else '<div style="height:.4in"></div>'}
<h2 style="margin-top:22px">{w['title']}</h2><p class="lede">{w['question']}</p>{img if w.get('fig_side') != 'right' else ''}</div>
<div style="padding-top:28px;display:flex;flex-direction:column;gap:14px">{body}{facts(w['facts']) if w.get("parts_first") or not (w["diagram"] or w.get("media_label")) else ''}{'<div style="margin-top:-14px">' + img + '</div>' if w.get('fig_side') == 'right' else ''}</div></div>""", w["title"], nx())
        if "parts" in w and w.get("parts_first"):
            series_page()
        if w["diagram"]:
            page(f"""<p class="eyebrow"><b>{w['label']}</b> · {w.get("diagram_label", "Structure")}</p>
<div style="width:{w.get('dia_w', '90%')};margin:0 auto">{getattr(D, w["diagram"])()}</div>
{'' if w.get("parts_first") else '<div style="position:absolute;left:.7in;right:.7in;bottom:1.05in;columns:2;column-gap:.35in">' + facts(w['facts']) + '</div>'}""", w["title"], nx())
        if w.get("diagram_extra"):
            page(f"""<p class="eyebrow"><b>{w['label']}</b> · {w.get('extra_label', 'Three versions')}</p>
<div style="width:96%;margin:.2in auto 0">{getattr(D, w["diagram_extra"])()}</div>
<p class="cap" style="position:absolute;left:.7in;bottom:1.1in;font-size:8.5pt;color:var(--muted);max-width:none">{w.get("diagram_source", "")}</p>""", w["title"], nx())
        shown = [m for m in w.get("media", []) if m.get("pdf", True) and not m.get("opener") and not m.get("part") and "gallery" not in m]
        if shown:
            figs = "".join(f'<figure style="margin:0;min-width:0"><img src="media/{m.get("pdf_image") or m.get("image")}" alt="" '
                           f'style="display:block;{"width:auto;max-width:100%" if len(shown) == 1 else "width:100%"};max-height:4.6in;object-fit:contain;object-position:left top;border:1px solid var(--rule)">'
                           f'<p class="cap" style="margin-top:8px;font-size:8pt;color:var(--muted)">{m["caption"].replace(" (film, 30 s)", " (still from a 30-second film)")}</p></figure>'
                           for m in shown)
            cols = f"repeat({len(shown)},minmax(0,1fr))"
            if not w["diagram"]:
                figs += f'<div>{facts(w["facts"])}</div>'
                cols = "1.5fr 1fr"
            page(f"""<p class="eyebrow"><b>{w['label']}</b> · {w.get("media_label", "In use")}</p>
<div style="display:grid;grid-template-columns:{cols};gap:.35in;align-items:start;margin-top:.15in">{figs}</div>""", w["title"], nx())
        for m in w.get("media", []):
            if "gallery" in m:
                tiles = "".join(f'<img src="media/{f}" alt="" style="display:block;width:100%;border:1px solid var(--rule)">' for f in m["gallery"])
                page(f"""<p class="eyebrow"><b>{w['label']}</b> · {w.get('gallery_label', 'The timeline')}</p>
<div style="display:grid;grid-template-columns:repeat(3,2.05in);gap:.12in;justify-content:start">{tiles}</div>
<p class="cap" style="position:absolute;left:7.6in;right:.7in;top:1.0in;font-size:9pt;color:var(--muted)">{m["caption"]}</p>""", w["title"], nx())
        if "parts" in w and not w.get("parts_first"):
            series_page()

    # Tezign
    tb_ = "".join(f"<p>{p}</p>" for p in C.TEZIGN["body"] + C.TEZIGN["company"])
    def ptile(name, link, desc, img):
        if img and img.startswith("diagram:"):
            vis = f'<div class="stl" style="height:1.75in;border:1px solid var(--rule);background:#fff;padding:.06in;overflow:hidden"><style>.stl svg{{display:block;width:100%;height:100%}}</style>{getattr(D, img[8:])()}</div>'
        elif img:
            vis = f'<img src="media/{img}" alt="" style="display:block;width:100%;height:1.75in;object-fit:cover;object-position:top;border:1px solid var(--rule)">'
        else:
            vis = f'<div class="ph" style="height:1.75in">Image to add: {name}</div>'
        host = link.split("//")[1].split("/")[0].replace("www.", "")
        return f'<div>{vis}<h3 style="margin-top:10px">{name}</h3><p style="font-size:9pt;margin-top:4px">{desc}</p><p style="font-size:9pt;margin-top:4px"><a href="{link}">{host}</a></p></div>'
    page(f"""<p class="eyebrow"><b>Entrepreneurship</b> · {C.TEZIGN['sub']}</p>
<div class="cols" style="grid-template-columns:1fr 2.2fr;align-items:start"><h2>Tezign</h2><div>{tb_}</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.3in;margin-top:.25in">{"".join(ptile(*p_) for p_ in C.TEZIGN["products"])}</div>""", "Tezign", "E-01")

    # Lab and teaching
    lab = "".join(f"<p>{p}</p>" for p in C.LAB["body"])
    fund = "".join(f'<tr><td class="y">{y}</td><td>{t}<br><span style="color:var(--muted)">{s}</span></td></tr>' for y, t, s in C.LAB["funded"])
    adv = "".join(f"<p>{p}</p>" for p in C.ADVISING["body"])
    advw = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{n}</b><br>{t}</td></tr>' for y, n, t in C.ADVISING["doctoral"])
    page(f"""<p class="eyebrow"><b>Research</b></p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in">
<div><h3>{C.LAB['title']}</h3><div style="margin-top:10px">{lab}</div>{facts(C.LAB['facts']).replace('class="facts"','class="facts stack"')}</div>
<div><h3>Representative funded projects</h3><table style="margin-top:10px">{fund}</table></div>
</div>""", "Research", "R-01")
    page(f"""<p class="eyebrow"><b>Research</b> · Student advising</p>
<div class="cols" style="grid-template-columns:1fr 1.5fr"><div><h2>Student advising</h2>
<div style="margin-top:18px">{adv}</div></div><div><h3>Doctoral students</h3><p style="font-size:9pt;color:var(--muted);margin-top:4px">By year of entry, with dissertation titles.</p><table style="margin-top:8px">{advw}</table></div></div>""", "Student advising", "R-02")

    # Talks
    talks = "".join(
        f'<tr><td class="y" style="width:.45in">{y}</td><td><b style="font-weight:500">{t}</b>{"" if t[-1] in "?!" else "."} {v}'
        + (f' · <a href="{u}">{"summary" if "sohu.com" in u else "video"}</a>' if u else "") + "</td></tr>" for y, v, t, u in C.TALKS)
    page(f"""<p class="eyebrow"><b>Talks</b> · Selected talks and keynotes</p>
<div class="pubcols" style="columns:2;column-gap:.35in;column-fill:auto;height:5.75in"><style>.pubcols tr{{break-inside:avoid}}.pubcols td{{padding-top:2px;padding-bottom:2px}}</style><table style="font-size:7.4pt;line-height:1.25">{talks}</table></div>""",
         "Talks", "T-01")

    # Book
    for y, t, p in C.WRITING["books"]:
        if y not in C.BOOK_PHOTOS:
            continue
        cover, spreads = C.BOOK_PHOTOS[y]
        span = "grid-column:1/-1;max-width:5.2in;" if len(spreads) == 1 else ""
        sp = "".join(f'<figure style="margin:0;{span}"><img src="media/{f}" alt="" style="display:block;width:100%;border:1px solid var(--rule)">'
                     f'<p class="cap" style="margin-top:5px;font-size:7.5pt;color:var(--muted)">{c}</p></figure>' for f, c in spreads)
        page(f"""<p class="eyebrow"><b>Book</b> · {y} · {p}</p>
<div style="display:grid;grid-template-columns:2.3in 1fr;gap:.4in">
<div><img src="media/{cover}" alt="" style="display:block;width:100%"><h3 style="margin-top:16px;font-size:13pt"><i>{t}</i></h3></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.18in .25in;align-content:start">{sp}</div></div>""", "Book", "T-01.1")

    # Publications
    def pub_block(cat, rs):
        trs = "".join(f'<tr><td class="y" style="width:.55in">{y}</td><td>{a} {t} <i>{v}</i>'
                      + (f' <a href="{d}">{d.replace("https://doi.org/", "doi:").replace("https://arxiv.org/abs/", "arXiv:")}</a>' if d else "") + "</td></tr>" for y, a, t, v, d in rs)
        return f'<h3 style="font-size:10.5pt;margin:0 0 4px;break-after:avoid">{cat}</h3><table style="font-size:7pt;line-height:1.25;margin-bottom:10px">{trs}</table>'
    pats = "".join(f'<tr><td class="y" style="width:1.6in">{no}</td><td>{t}</td></tr>' for t, no in C.PATENTS)
    groups = [C.PUBLICATIONS[:2], C.PUBLICATIONS[2:]]
    for gi, grp in enumerate(groups):
        extra = (f'<div style="break-inside:avoid-column"><h3 style="font-size:10.5pt;margin:0 0 4px">Patents (selected)</h3><table style="font-size:7.6pt">{pats}</table></div>' if gi == len(groups) - 1 else "")
        page(f"""<p class="eyebrow"><b>Publications</b> · More than 100 articles and papers{" (continued)" if gi else ""}</p>
<div style="columns:2;column-gap:.35in;column-fill:auto;height:5.75in;margin-top:0" class="pubcols"><style>.pubcols tr{{break-inside:avoid}}.pubcols td{{padding-top:3px;padding-bottom:3px}}</style>{"".join(pub_block(c, r) for c, r in grp)}{extra}</div>""", "Publications", f"T-02.{gi + 1}")

    # Record
    appts = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{i}</b><br>{r}</td></tr>' for y, i, r in C.APPOINTMENTS)
    edu = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{i}</b>, {d}</td></tr>' for y, i, d in C.EDUCATION)
    hon = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.HONORS)
    svc = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.SERVICE)
    sm = 'class="rec" style="margin-top:8px;font-size:8.2pt;line-height:1.25"'
    page(f"""<p class="eyebrow"><b>Record</b></p>
<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:.45in">
<div><h3>Academic appointments</h3><table style="margin-top:10px">{appts}</table></div>
<div><h3>Education</h3><table style="margin-top:10px">{edu}</table></div></div>""", "Record", "T-03.1")
    page(f"""<style>.rec td{{padding-top:4px;padding-bottom:4px}}</style><p class="eyebrow"><b>Record</b> · Service and recognition</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in">
<div><h3>Service</h3><table {sm}>{svc}</table></div>
<div><h3>Recognition</h3><table {sm}>{hon}</table></div></div>""", "Record", "T-03.2")

    # Back
    page(f"""<div style="display:grid;align-content:center;height:100%;gap:18px">
<h2>Ling Fan</h2><p class="lede" style="margin:0">{C.HEADLINE}</p>
<p class="eyebrow" style="margin-top:20px">{C.CONTACT}</p><p class="eyebrow" style="margin-top:6px;text-transform:none">{" · ".join(u.replace("https://", "").replace("www.", "").rstrip("/") for n, u in C.PROFILES)}</p></div>""", "Contact", "Z-00")

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ling Fan — Portfolio</title>
<link rel="stylesheet" href="fonts.css"><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w").write(build())
