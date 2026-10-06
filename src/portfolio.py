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
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-print-color-adjust:exact;print-color-adjust:exact;text-rendering:geometricPrecision;font-kerning:normal}
.pg{width:11in;height:8.5in;position:relative;padding:.6in .7in .95in;overflow:hidden;page-break-after:always;background:var(--paper)}
.pg:last-child{page-break-after:auto}
.bleed .tb{left:4.35in!important}
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

    def eb(w, label):
        return f'<p class="eyebrow"><b>{w["label"]}</b> · {label}</p>'

    def ps(xs, size=None):
        st = f' style="font-size:{size}"' if size else ""
        return "".join(f"<p{st}>{x}</p>" for x in xs)

    def C_TODO(t):
        return t.replace("[To add:", '<span class="todo">To add:').replace("]", "</span>") if "[To add:" in t else t

    links = " · ".join(u.replace("https://", "").replace("www.", "").rstrip("/") for _, u in C.PROFILES)

    # Cover
    page(f"""
<div style="display:grid;grid-template-rows:auto 1fr auto;height:100%">
 <p class="eyebrow">Portfolio · R. Buckminster Fuller Professor in Practice of Design Science · Harvard Graduate School of Design</p>
 <div style="align-self:center;display:grid;grid-template-columns:1fr auto;gap:.5in;align-items:center"><div><h1 style="font-size:84pt">Ling Fan</h1>
  <p class="lede" style="font-size:26pt;max-width:30ch">{C.HEADLINE}</p></div>
  <img src="media/portrait.jpg" alt="" style="display:block;width:2.7in;height:2.7in;border-radius:50%;object-fit:cover;object-position:50% 30%"></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in;align-items:end">
  <div><p class="eyebrow" style="margin:0 0 6px">Contact</p><p style="font-size:12pt;margin:0">{C.CONTACT}</p>
  <p style="font-size:12pt;margin:2px 0 0"><a href="https://fanling.ai">fanling.ai</a></p>
  <p style="font-size:12pt;margin:2px 0 0">{links}</p></div>
  <p class="eyebrow" style="text-align:right;margin:0">October 2026</p>
 </div>
</div>""", "Portfolio", "A-00")

    # Contents
    toc = [("Statement", "Design AI"), ("Overview", "One body of work")]
    toc += [(w["label"], w["title"]) for w in C.WORKS]
    toc += [("Research", "Design AI Lab"), ("Entrepreneurship", "Tezign"), ("Biography", "Biography")]
    rows = "".join(f'<tr><td class="y" style="width:1.4in">{a}</td><td style="font-family:var(--serif);font-size:13pt">{b}</td></tr>' for a, b in toc)
    page(f"""<p class="eyebrow">Contents</p><div class="cols"><div><h2>The works in this portfolio are models, datasets, agents and institutions.</h2>
<p style="margin-top:18px">Each is presented as an architect presents a project: the question it answers, its structure, how it performs in use. Links in this document are live.</p></div>
<table>{rows}</table></div>""", "Contents", "A-03")

    # Statement
    paras = "".join(f"<p>{p}</p>" for p in C.STATEMENT)
    page(f"""<div style="display:grid;grid-template-columns:auto 1fr;gap:.5in;align-items:end;margin-bottom:22px"><div><p class="eyebrow">Statement</p><h2>Design AI</h2></div>
<p class="lede" style="margin:0;max-width:none">{C.THESIS}</p></div>
<div style="columns:3;column-gap:.35in;font-size:0">{paras.replace('<p>','<p style="font-size:9.8pt">')}</div>
<div style="position:absolute;left:.7in;right:.7in;bottom:1.05in">{D.lineage()}</div>""", "Statement", "A-04")

    # Overview
    page(f"""<div style="display:grid;grid-template-columns:auto 1fr;gap:.5in;align-items:end;margin-bottom:10px"><div><p class="eyebrow">Overview</p><h2>One body of work</h2></div>
<p style="margin:0;font-size:11pt;max-width:none">The computability of creativity asks how creativity can be represented, reasoned through and enacted by machines while keeping the subjectivity and plurality it depends on. Each work answers one part of that question and is carried into one product: the Design AI Lab builds the models and data, and Tezign deploys them at scale.</p></div>
<div style="width:96%;margin:0 auto">{D.body_of_work()}</div>""", "Overview", "A-05")

    # Works
    for w in C.WORKS:
        sheet = w["sheet"]
        _n = iter(range(1, 20))
        nx = lambda: f"{sheet}.{next(_n)}"
        slug = w["slug"]
        body = "".join(f"<p>{p}</p>" for p in w["body"])
        img = ""
        if "figure" in w and slug != "creative-reasoning-model":
            fn, cap = w["figure"]
            img = (f'<div style="margin-top:auto;padding:16px 0 .04in">{getattr(D, fn)()}'
                   f'<p class="cap" style="margin-top:8px;font-size:7.5pt;color:var(--muted)">{cap}</p></div>')
        show_facts = not w["diagram"] or slug == "subjective-world-model"
        if slug == "computability-of-creativity":
            page(f"""<p class="eyebrow"><b>{w['label']}</b> · {w['sub']}</p>
<div style="display:grid;grid-template-columns:1fr 1.35fr;gap:.45in;align-items:start">
<div><h2 style="margin-top:8px">{w['title']}</h2><p class="lede" style="font-size:14pt">{w['question']}</p></div>
<div style="padding-top:10px">{body.replace("<p>", '<p style="font-size:9.4pt">')}</div></div>
<div style="width:74%;margin:.15in auto 0">{getattr(D, w["diagram"])()}</div>""", w["title"], nx())
        else:
          page(f"""<div style="display:grid;grid-template-columns:1.1fr 1.4fr;gap:.45in;height:100%">
<div style="display:flex;flex-direction:column"><p class="eyebrow"><b>{w['label']}</b> · {w['sub']}</p>{f'<div class="num">{w["no"]}</div>' if w['no'] else '<div style="height:.4in"></div>'}
<h2 style="margin-top:22px">{w['title']}</h2><p class="lede">{w['question']}</p>{img}</div>
<div style="padding-top:28px;display:flex;flex-direction:column;gap:14px">{body}{facts(w['facts']) if (w.get("parts_first") or show_facts) and slug != "subjective-world-model" else ''}</div></div>""", w["title"], nx())

        if slug == "subjective-world-model":
            page(f"""{eb(w, "Training the model")}
<h2 style="margin-bottom:.15in">How the model is trained</h2>
<div style="width:96%;margin:0 auto .25in">{D.swm_training()}</div>
<div style="columns:3;column-gap:.35in;font-size:0">{ps(w["training"], "9.2pt")}</div>""", w["title"], nx())
            page(f"""{eb(w, "atypica.AI · a subjective-world simulation agent")}
<div style="display:grid;grid-template-columns:2.6in 1fr;gap:.4in;align-items:start">
<div><h2>atypica.AI</h2><p class="lede" style="font-size:14pt">A subjective-world simulation agent</p><p style="margin-top:8px"><a href="https://atypica.ai">atypica.ai</a></p></div>
<div style="columns:2;column-gap:.35in">{ps(w["atypica"], "9.2pt")}</div></div>
<figure style="margin:.22in auto 0;width:94%"><p class="eyebrow" style="margin-bottom:6px">An agentic research studio for businesses</p>{D.atypica_studio()}
<p class="cap" style="margin-top:6px;font-size:8pt;color:var(--muted)">Business questions are answered by AI personas, panels and interviews built on the Subjective World Model.</p></figure>""", w["title"], nx())
            feats = [("Research studio", "Runs a study end to end: brief, personas, interview guide, sessions and synthesis."),
                     ("Persona library", "Each persona is built in four layers of real evidence, with its sources open to inspection."),
                     ("Human validation", "Persona answers are compared with real respondents, question by question."),
                     ("Human control", "People confirm the brief, the questions and the participants before anything runs."),
                     ("Playbooks and memory", "Proven studies become playbooks; validated findings return to project memory."),
                     ("Continuous insight", "Panels keep their memory, so a team can return to the same people weeks later.")]
            fg = "".join(f'<figure style="margin:0"><img src="media/atypica-f{i + 1}.jpg" alt="" style="display:block;width:100%;border:1px solid var(--rule)">'
                         f'<p style="font-size:8.4pt;margin-top:6px;line-height:1.3"><b style="font-weight:500">{a}.</b> {b}</p></figure>' for i, (a, b) in enumerate(feats))
            page(f"""{eb(w, "atypica.AI in use")}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.16in .25in;margin-top:.05in">{fg}</div>""", w["title"], nx())
            vis = ['<img src="media/case-food.jpg" alt="" style="display:block;width:100%;height:1.9in;object-fit:cover;border:1px solid var(--rule)">',
                   '<img src="media/case-tools.jpg" alt="" style="display:block;width:100%;height:1.9in;object-fit:cover;border:1px solid var(--rule)">',
                   '<img src="media/case-families.jpg" alt="" style="display:block;width:100%;height:1.9in;object-fit:cover;object-position:50% 50%;border:1px solid var(--rule)">']
            def figs(x):
                return "".join(f'<div style="border-top:1px solid var(--ink);padding-top:5px;font-size:9.5pt;line-height:1.25">{f.strip()}</div>' for f in x.split(";"))
            cases = "".join(f'<div>{vis[i]}<p class="eyebrow" style="margin:12px 0 4px">Case {i + 1} · {k}</p><h3 style="font-size:12pt">{t_}</h3>'
                            f'<p style="font-size:8.6pt;margin-top:8px;line-height:1.38">{C_TODO(d)}</p>'
                            f'<div style="display:grid;grid-template-columns:repeat({len(fg.split(";"))},1fr);gap:.1in;margin-top:8px">{figs(fg)}</div></div>'
                            for i, (k, t_, d, fg) in enumerate(w["cases"]))
            page(f"""{eb(w, "Typical cases")}
<h2 style="margin-bottom:.22in">What atypica.AI is used to simulate</h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.32in">{cases}</div>""", w["title"], nx())
            continue

        if slug == "brain-machine-ratio":
            pm = {m["part"]: m for m in w.get("media", []) if m.get("part")}
            pt = {k: (t, d) for k, t, d in w["parts"]}
            page(f"""{eb(w, "(a) Quantitative study")}
<div style="display:grid;grid-template-columns:2.6in 1fr;gap:.4in;align-items:start;margin-bottom:.15in"><h2 style="font-size:22pt">{pt["a"][0]}</h2><p style="font-size:9.2pt;margin:0">{pt["a"][1]}</p></div>
<div class="bq" style="width:86%;margin:.1in auto 0"><style>.bq svg{{display:block;width:100%;height:auto;max-height:4.1in}}</style>
<p class="eyebrow" style="margin-bottom:6px">Three versions</p>{D.bmr_versions()}</div>
<p class="cap" style="position:absolute;left:.7in;bottom:1.1in;font-size:8pt;color:var(--muted);max-width:none">{w.get("diagram_source", "")}</p>""", w["title"], nx())
            hall = next(m for m in w["media"] if m.get("image") == "wdcc-hall.jpg")
            gal = next(m for m in w["media"] if "gallery" in m)
            gt = "".join(f'<img src="media/{f}" alt="" style="display:block;width:100%;border:1px solid var(--rule)">' for f in gal["gallery"])
            page(f"""{eb(w, "(b) Qualitative study")}
<div style="display:grid;grid-template-columns:2.6in 1fr;gap:.4in;align-items:start;margin-bottom:.18in"><h2 style="font-size:22pt">{pt["b"][0]}</h2><p style="font-size:9.2pt;margin:0">{pt["b"][1]}</p></div>
<div style="display:grid;grid-template-columns:1.15fr 1fr;gap:.35in;align-items:start">
<figure style="margin:0"><img src="media/wdcc-hall.jpg" alt="" style="display:block;width:100%;border:1px solid var(--rule)"><p class="cap" style="margin-top:6px;font-size:8pt;color:var(--muted)">{hall["caption"]}</p></figure>
<figure style="margin:0"><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.07in">{gt}</div><p class="cap" style="margin-top:6px;font-size:8pt;color:var(--muted)">{gal["caption"]}</p></figure></div>""", w["title"], nx())
            continue

        if slug == "agentic-creativity":
            page(f"""{eb(w, "Structure · the agent's loop and a long-horizon agent")}
<div style="display:grid;grid-template-columns:1fr 2.3in;gap:.4in;align-items:start">
<div><p class="eyebrow" style="margin:0 0 4px">The agent's loop</p>{D.agent_loop()}
<p class="eyebrow" style="margin:.18in 0 4px">A long-horizon agent: five days of one task</p><div style="width:92%">{D.agent_timeline()}</div></div>
<div style="padding-top:.2in">{facts(w['facts']).replace('class="facts"','class="facts stack"')}</div></div>""", w["title"], nx())
            continue

        if w["diagram"] and slug != "computability-of-creativity":
            fl = "" if w.get("parts_first") else '<div style="position:absolute;left:.7in;right:.7in;bottom:1.05in;columns:2;column-gap:.35in">' + facts(w['facts']) + '</div>'
            page(f"""{eb(w, w.get("diagram_label", "Structure"))}
<div style="width:{'78%' if slug == 'agentic-creativity' else w.get('dia_w', '90%')};margin:0 auto">{getattr(D, w["diagram"])()}</div>{fl}""", w["title"], nx())

        if slug == "computability-of-creativity":
            pm = {m["part"]: m for m in w.get("media", []) if m.get("part")}
            im_ = lambda f: f'<img src="media/{f}" alt="" style="display:block;width:100%;height:100%;object-fit:cover;border:1px solid var(--rule)">'
            def half(k, t, d):
                m = pm.get(k)
                text_ = w.get("projects", {}).get(k) or [d]
                fs = m.get("shots") or [f for f, _ in m.get("dataset", [])] or [m["poster"]]
                cap = m.get("shots_cap") or "; ".join(f"({j + 1}) {c}" for j, (_, c) in enumerate(m.get("dataset", []))) or m["caption"]
                cols = 3 if len(fs) in (3, 6) else 2
                rh = 2.3 / ((len(fs) + cols - 1) // cols)
                grid = "".join(f'<div style="height:{rh - .06:.2f}in">{im_(f)}</div>' for f in fs)
                return f"""<div><p class="eyebrow" style="margin:0 0 4px"><b>({k})</b></p><h3 style="font-size:15pt">{t}</h3>
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:.06in;margin-top:8px">{grid}</div>
<p class="cap" style="margin-top:4px;font-size:7pt;color:var(--muted);line-height:1.3">{cap}</p>
<div style="columns:2;column-gap:.22in;margin-top:6px">{"".join(f'<p style="font-size:7.6pt;line-height:1.36;margin:0 0 5px">{C_TODO(x)}</p>' for x in text_)}</div></div>"""
            ps_ = w["parts"]
            for i in range(0, len(ps_), 2):
                pair = ps_[i:i + 2]
                page(f"""{eb(w, " and ".join(f"({k}) {t}" for k, t, _ in pair))}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.4in;align-items:start">{"".join(half(*x) for x in pair)}</div>""", w["title"], nx())
            continue

        shown = [m for m in w.get("media", []) if m.get("pdf", True) and not m.get("opener") and not m.get("part") and "gallery" not in m]
        for m in shown:
            vis = getattr(D, m["svg"])() if "svg" in m else f'<img src="media/{m.get("pdf_image") or m.get("image")}" alt="" style="display:block;max-width:100%;max-height:4.8in;border:1px solid var(--rule)">'
            page(f"""{eb(w, m.get("pdf_label", w.get("media_label", "In use")))}
<figure style="margin:.2in auto 0;width:92%">{vis}<p class="cap" style="margin-top:10px;font-size:8.5pt;color:var(--muted)">{m["caption"]}</p></figure>""", w["title"], nx())

    # Research: the Lab and student advising
    lab = "".join(f"<p>{p}</p>" for p in C.LAB["body"])
    fund = "".join(f'<tr><td class="y">{y}</td><td>{t}<br><span style="color:var(--muted)">{s}</span></td></tr>' for y, t, s in C.LAB["funded"])
    adv = "".join(f"<p>{p}</p>" for p in C.ADVISING["body"])
    advw = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{nm}</b><br>{t}</td></tr>' for y, nm, t in C.ADVISING["doctoral"])
    page(f"""<p class="eyebrow"><b>Research</b> · The Lab</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in">
<div><h2>{C.LAB['title']}</h2><div style="margin-top:18px">{lab}</div>{facts([f for f in C.LAB['facts'] if 'ntellectual' not in f[0]]).replace('class="facts"','class="facts stack"')}</div>
<div><h3>Representative funded projects</h3><table style="margin-top:10px">{fund}</table></div>
</div>""", "Research", "R-01")
    page(f"""<p class="eyebrow"><b>Research</b> · Student advising</p>
<div class="cols" style="grid-template-columns:1fr 1.5fr"><div><h2>Student advising</h2>
<div style="margin-top:18px">{adv}</div></div><div><h3>Doctoral students</h3><p style="font-size:9pt;color:var(--muted);margin-top:4px">By year of entry, with dissertation titles.</p><table style="margin-top:8px">{advw}</table></div></div>""", "Student advising", "R-02")

    # Entrepreneurship
    tb_ = "".join(f"<p>{p}</p>" for p in C.TEZIGN["body"] + C.TEZIGN["company"])
    prod = {p_[0]: p_ for p_ in C.TEZIGN["products"]}
    def ptile(name, kind, text_):
        _, link, _, img = prod[name]
        host = link.split("//")[1].split("/")[0].replace("www.", "")
        return (f'<div><img src="media/{img}" alt="" style="display:block;width:100%;height:1.9in;object-fit:cover;object-position:top;border:1px solid var(--rule)">'
                f'<h3 style="margin-top:10px">{"Tezign GEA" if name == "Tezign" else name}</h3><p class="eyebrow" style="margin:3px 0 6px">{kind}</p><p style="font-size:8.4pt;line-height:1.36">{text_}</p>'
                f'<p style="font-size:8.4pt"><a href="{link}">{host}</a></p></div>')
    page(f"""<p class="eyebrow"><b>Entrepreneurship</b> · Tezign</p>
<div style="display:grid;grid-template-columns:3.3in 1fr;gap:.45in;align-items:start">
<div><h2>Tezign</h2><div style="margin-top:16px">{tb_.replace("<p>", '<p style="font-size:9.6pt">')}</div>
<p style="font-size:9.6pt"><a href="https://www.tezign.com">tezign.com</a></p></div>
<figure style="margin:0"><img src="media/tezign-office.jpg" alt="" style="display:block;width:100%;border:1px solid var(--rule)">
<p class="cap" style="margin-top:6px;font-size:8pt;color:var(--muted)">Tezign, Shanghai.</p></figure></div>""", "Entrepreneurship", "E-01")
    page(f"""<p class="eyebrow"><b>Entrepreneurship</b> · Products</p>
<h2 style="margin-bottom:.2in">Three products</h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.3in">{"".join(ptile(*p_) for p_ in C.TEZIGN["product_pages"])}</div>""", "Entrepreneurship", "E-02")

    # Biography: section opener for who Ling is
    page(f"""<p class="eyebrow"><b>Biography</b> · Ling Fan</p>
<div style="display:grid;grid-template-columns:3.2in 1fr;gap:.45in;align-items:start">
<img src="media/ling-talk.jpg" alt="" style="display:block;width:3.2in;height:4.8in;object-fit:contain;margin-top:6px">
<div><h3>Biography</h3>
<div style="columns:2;column-gap:.35in;margin-top:8px">{"".join(f'<p style="font-size:9pt;line-height:1.42">{x}</p>' for x in C.BIOGRAPHY)}</div></div></div>""", "Biography", "V-00")

    # About: the record, at the end
    appts = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{i}</b><br>{r}</td></tr>' for y, i, r in C.APPOINTMENTS)
    edu = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{i}</b><br>{d}</td></tr>' for y, i, d in C.EDUCATION)
    hon = "".join(f'<tr><td class="y">{y or "—"}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.HONORS)
    svc = "".join(f'<tr><td class="y">{y}</td><td><b style="font-weight:500">{o}</b><br>{t}</td></tr>' for y, o, t in C.SERVICE)
    sm = 'class="rec" style="margin-top:8px;font-size:8.2pt;line-height:1.25"'
    for sub, (h1, t1), (h2, t2), sheet in (("Appointments and education", ("Academic appointments", appts), ("Education", edu), "V-01"),
                                           ("Service and recognition", ("Service", svc), ("Recognition", hon), "V-02")):
        page(f"""<style>.rec td{{padding-top:4px;padding-bottom:4px}}</style><p class="eyebrow"><b>Biography</b> · {sub}</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:.45in">
<div><h3>{h1}</h3><table {sm}>{t1}</table></div>
<div><h3>{h2}</h3><table {sm}>{t2}</table></div></div>""", "Biography", sheet)

    # Talks
    talks = "".join(
        f'<tr><td class="y" style="width:.45in">{y}</td><td><b style="font-weight:500">{t}</b>{"" if t[-1] in "?!" else "."} {v}'
        + (f' · <a href="{u}">{"summary" if "sohu.com" in u else "video"}</a>' if u else "") + "</td></tr>" for y, v, t, u in C.TALKS)
    page(f"""<p class="eyebrow"><b>Biography</b> · Talks and keynotes</p><h3 style="margin-bottom:8px">Talks and keynotes</h3>
<div class="pubcols" style="columns:2;column-gap:.35in;column-fill:auto;height:5.45in"><style>.pubcols tr{{break-inside:avoid}}.pubcols td{{padding-top:2px;padding-bottom:2px}}</style><table style="font-size:7.2pt;line-height:1.22">{talks}</table></div>""",
         "Biography", "V-03")

    # Books, both on one page
    picks = {"2019": ["book-2019-timeline.jpg", "book-2019-hcml.jpg"], "2014": ["book-2014-spread.jpg"]}
    halves = ""
    for y, t, p in C.WRITING["books"]:
        if y not in C.BOOK_PHOTOS:
            continue
        cover, spreads = C.BOOK_PHOTOS[y]
        sp = "".join(f'<figure style="margin:0"><img src="media/{f}" alt="" style="display:block;width:100%;border:1px solid var(--rule)">'
                     f'<p class="cap" style="margin-top:4px;font-size:7pt;color:var(--muted)">{c}</p></figure>' for f, c in spreads if f in picks.get(y, []))
        halves += f"""<div style="display:grid;grid-template-columns:1.45in 1fr;gap:.2in;align-content:start">
<div><img src="media/{cover}" alt="" style="display:block;width:100%"><p class="eyebrow" style="margin:10px 0 4px">{y} · {p}</p><h3 style="font-size:11pt"><i>{t}</i></h3></div>
<div style="display:grid;gap:.12in;align-content:start">{sp}</div></div>"""
    page(f"""<p class="eyebrow"><b>Biography</b> · Books</p><h3 style="margin-bottom:10px">Books</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:.4in">{halves}</div>""", "Biography", "V-04")

    # Publications
    def pub_block(cat, rs):
        trs = "".join(f'<tr><td class="y" style="width:.55in">{y}</td><td>{a} {t} <i>{v}</i>'
                      + (f' <a href="{d}">{d.replace("https://doi.org/", "doi:").replace("https://arxiv.org/abs/", "arXiv:")}</a>' if d else "") + "</td></tr>" for y, a, t, v, d in rs)
        return f'<p class="eyebrow" style="margin:0 0 4px;break-after:avoid">{cat}</p><table style="font-size:7pt;line-height:1.25;margin-bottom:10px">{trs}</table>'
    groups = [C.PUBLICATIONS[:2], C.PUBLICATIONS[2:]]
    for gi, grp in enumerate(groups):
        page(f"""<p class="eyebrow"><b>Biography</b> · Publications{" (continued)" if gi else ""}</p><h3 style="margin-bottom:8px">Publications</h3>
<div style="columns:2;column-gap:.35in;column-fill:auto;height:5.45in;margin-top:0" class="pubcols"><style>.pubcols tr{{break-inside:avoid}}.pubcols td{{padding-top:3px;padding-bottom:3px}}</style>{"".join(pub_block(c, r) for c, r in grp)}</div>""", "Biography", f"V-05.{gi + 1}")

    # Back
    page(f"""<div style="display:grid;align-content:center;height:100%;gap:18px">
<h2>Ling Fan</h2><p class="lede" style="margin:0">{C.HEADLINE}</p>
<p class="eyebrow" style="margin-top:20px">{C.CONTACT}</p><p class="eyebrow" style="margin-top:6px;text-transform:none"><a href="https://fanling.ai">fanling.ai</a> · {links}</p></div>""", "Contact", "Z-00")

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ling Fan — Portfolio</title>
<link rel="stylesheet" href="fonts.css"><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w").write(build())
