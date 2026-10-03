"""Line drawings for the portfolio and site. Colours come from CSS classes so both
themes work: .ln (ink line), .lq (quiet line), .ac (accent), .tf (accent tint fill)."""

from html import escape


def _t(x, y, s, cls="b", anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{extra}>{escape(s)}</text>'


def _box(x, y, w, h, label=None, title=None, lines=(), accent=False, center=False, lh=17):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" class="{"bx ac-b" if accent else "bx"}"/>']
    cy = y + 22
    tx, an = (x + w / 2, "middle") if center else (x + 14, "start")
    if label:
        out.append(_t(tx, cy, label, "m", an)); cy += 22
    if title:
        out.append(_t(tx, cy, title, "h", an)); cy += 20
    for ln in lines:
        out.append(_t(tx, cy, ln, "b", an)); cy += lh
    return "".join(out)


def _arrow(d, mid="a", dashed=False):
    return f'<path d="{d}" class="ln{" dash" if dashed else ""}" fill="none" marker-end="url(#{mid})"/>'


def _svg(vb_h, body, label, mid, vb_w=1040, cls="dia"):
    defs = (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="mk"/></marker></defs>')
    return (f'<svg class="{cls}" viewBox="0 0 {vb_w} {vb_h}" role="img" aria-label="{escape(label)}" '
            f'xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>')


def overview():
    m = "a-ov"
    b = []
    b.append(_box(150, 20, 800, 96, "IN USE", "Systems built from the research",
                  ["Tezign: an agentic AI platform serving 200+ enterprises and 1M+ professional users",
                   "atypica.AI: social simulation with AI personas"]))
    xs = [150, 425, 700]
    works = [("WORK 01", "Subjective World Model", ["Models people as they differ,", "in taste and judgment"]),
             ("WORK 02", "Creative Reasoning", ["Reasons by unfolding, pruning", "and fusing possibilities"]),
             ("WORK 03", "Agentic Creativity", ["Agents that work across the", "long horizon of innovation"])]
    for x, (lab, ti, ls) in zip(xs, works):
        b.append(_box(x, 176, 250, 128, lab, ti, ls))
    b.append(_box(150, 364, 800, 110, "PAST RESEARCH · THE GROUND", "The Computability of Creativity · BMR",
                  ["Datasets of colour, blind-box toys and craft · Prometheus knowledge graph",
                   "Brain–Machine Ratio: dividing creative work between designers and AI"], accent=True))
    for x in xs:
        cx = x + 125
        b.append(_arrow(f"M{cx} 364V306", m))
        b.append(_arrow(f"M{cx} 176V118", m))
    b.append(_arrow("M950 68H995V419H952", m, dashed=True))
    b.append(f'<text x="1012" y="244" class="q" text-anchor="middle" transform="rotate(90 1012 244)">Use returns evidence and new questions</text>')
    b.append('<path d="M128 20V116M128 176V474" class="lq" fill="none"/>')
    b.append(_t(0, 60, "ENTREPRENEURSHIP", "m")); b.append(_t(0, 80, "Tezign", "b"))
    b.append(_t(0, 310, "RESEARCH", "m")); b.append(_t(0, 330, "Design AI Lab,", "b")); b.append(_t(0, 347, "Tongji University", "b"))
    return _svg(500, "".join(b), "Three current works on a computable ground built in past work, and the systems that put them to use", m)


def lineage():
    m = "a-li"
    pts = [("c. 30–15 BC", "Vitruvius", ["the architect as", "a generalist"]),
           ("15th century", "Renaissance", ["the uomo", "universale"]),
           ("1950s–60s", "Buckminster Fuller", ["comprehensive anticipatory", "design science"]),
           ("1964", "Christopher Alexander", ["Notes on the", "Synthesis of Form"]),
           ("1970", "Nicholas Negroponte", ["The Architecture", "Machine"]),
           ("Today", "Designing AI", ["the designer designs", "the intelligence"])]
    b = ['<path d="M30 70H1010" class="lq" fill="none"/>']
    for i, (yr, name, ls) in enumerate(pts):
        x = 95 + i * 170
        last = i == len(pts) - 1
        b.append(f'<circle cx="{x}" cy="70" r="{7 if last else 5}" class="{"dot-ac" if last else "dot"}"/>')
        b.append(_t(x, 48, yr, "m", "middle"))
        b.append(_t(x, 104, name, "h ac-t" if last else "h", "middle"))
        for j, ln in enumerate(ls):
            b.append(_t(x, 124 + j * 17, ln, "b", "middle"))
    return _svg(170, "".join(b), "From Vitruvius to designing AI", m)


def world_model():
    m = "a-wm"
    b = [_t(40, 30, "A PERSON", "m")]
    for i, (n, g) in enumerate([("Expression", "what they say"), ("Story", "how they tell their lives"),
                                ("Cognition", "weights inferred from choices"), ("Behavior", "what they did")]):
        b.append(_box(40, 46 + i * 58, 200, 44, None, None, [], center=True))
        b.append(_t(140, 46 + i * 58 + 19, n, "h", "middle"))
        b.append(_t(140, 46 + i * 58 + 36, g, "q", "middle"))
    b.append(_arrow("M244 157H316", m))
    b.append(_box(320, 40, 300, 236, "WORK 01", "Subjective world model",
                  ["One person per state. Keeps", "contradictions between layers", "as evidence; rolls each event", "forward many times"], accent=True))
    b.append('<circle cx="400" cy="216" r="18" class="bx"/><circle cx="400" cy="216" r="6" class="dot"/>')
    b.append('<circle cx="470" cy="216" r="18" class="bx"/><path d="M470 207L478 222H462Z" class="dot"/>')
    b.append('<circle cx="540" cy="216" r="18" class="bx"/><rect x="534" y="210" width="12" height="12" class="dot"/>')
    b.append(_t(470, 256, "distinct AI personas", "q", "middle"))
    b.append(_arrow("M622 157H696", m))
    b.append(_t(700, 30, "SOCIAL SIMULATION", "m"))
    for i, n in enumerate(["A distribution of reactions", "Simulated interviews", "Product and message tests"]):
        b.append(_box(700, 46 + i * 58, 300, 44))
        b.append(_t(714, 46 + i * 58 + 27, n, "h"))
    b.append(_arrow("M850 222V258", m))
    b.append(_box(700, 262, 300, 44))
    b.append(_t(714, 289, "Design and business decisions", "h"))
    b.append(_arrow("M850 306V318H470V280", m, dashed=True))
    b.append(_t(660, 334, "real outcomes recalibrate the personas", "q", "middle"))
    # contrast strip
    b.append('<path d="M40 340H1000" class="lq" fill="none"/>')
    b.append(_t(40, 372, "A CONVERGENT MODEL", "m"))
    b.append(_t(540, 372, "A SUBJECTIVE WORLD MODEL", "m"))
    pts = [(70, 400), (110, 440), (150, 395), (190, 450), (230, 410), (90, 470), (170, 475), (240, 465)]
    for x, y in pts:
        b.append(f'<circle cx="{x}" cy="{y}" r="5" class="dot"/><path d="M{x} {y}L380 435" class="lq" fill="none"/>')
    b.append('<circle cx="384" cy="435" r="9" class="dot-ac"/>')
    b.append(_t(402, 440, "one average user", "b"))
    for x, y in pts:
        x2 = x + 500
        b.append(f'<circle cx="{x2}" cy="{y}" r="5" class="dot"/><circle cx="{x2}" cy="{y}" r="12" class="lq" fill="none"/>')
    b.append(_t(800, 440, "many distinct people", "b"))
    return _svg(500, "".join(b), "A subjective world model keeps people distinct and simulates how each responds", m)


def creative_reasoning():
    m = "a-cr"
    b = [_t(30, 30, "CONVERGENT REASONING", "m")]
    b.append('<circle cx="60" cy="80" r="14" class="bx"/>' + _t(60, 85, "Q", "h", "middle"))
    for x in [220, 380, 540, 700]:
        b.append(f'<circle cx="{x}" cy="80" r="6" class="dot"/>')
    b.append('<path d="M74 80H214M226 80H374M386 80H534M546 80H694" class="ln" fill="none"/>')
    b.append(_arrow("M706 80H856", m))
    b.append(_box(860, 58, 150, 44, None, None))
    b.append(_t(935, 85, "One answer", "h", "middle"))
    b.append('<path d="M30 130H1010" class="lq" fill="none"/>')
    b.append(_t(30, 164, "CREATIVE REASONING · WORK 02", "m ac-t"))
    for x, n in [(230, "UNFOLD"), (430, "COMPARE"), (620, "PRUNE"), (800, "FUSE")]:
        b.append(_t(x, 200, n, "m", "middle"))
    b.append('<circle cx="60" cy="320" r="14" class="bx"/>' + _t(60, 325, "Q", "h", "middle"))
    ys = [250, 320, 390]
    for y in ys:
        b.append(_arrow(f"M74 320L196 {y}", m))
        for dx, dy in [(-14, -10), (12, -12), (0, 12)]:
            b.append(f'<circle cx="{230 + dx}" cy="{y + dy}" r="4" class="dot"/>')
        b.append(f'<circle cx="230" cy="{y}" r="28" class="lq" fill="none"/>')
        b.append(_arrow(f"M260 {y}H420", m))
        b.append(f'<circle cx="430" cy="{y}" r="6" class="dot"/>')
    b.append('<path d="M430 256V314M430 326V384" class="ln dash" fill="none"/>')
    for y in (250, 390):
        b.append(f'<path d="M436 {y}H612" class="ln" fill="none"/><circle cx="620" cy="{y}" r="6" class="dot"/>')
    b.append('<path d="M436 320H580" class="lq dash" fill="none"/>')
    b.append('<path d="M612 312L628 328M628 312L612 328" class="ln" fill="none"/>')
    b.append(_arrow("M626 250L792 318", m))
    b.append(_arrow("M626 390L792 322", m))
    b.append(f'<circle cx="800" cy="320" r="8" class="dot-ac"/>')
    b.append(_arrow("M810 320H856", m))
    b.append(_box(860, 290, 150, 60, None, None, [], accent=True))
    b.append(_t(935, 315, "A new", "h", "middle")); b.append(_t(935, 335, "possibility", "h", "middle"))
    b.append(_t(230, 440, "open several", "q", "middle")); b.append(_t(230, 456, "possibility spaces", "q", "middle"))
    b.append(_t(430, 440, "set them against", "q", "middle")); b.append(_t(430, 456, "each other", "q", "middle"))
    b.append(_t(620, 440, "drop what does", "q", "middle")); b.append(_t(620, 456, "not hold", "q", "middle"))
    b.append(_t(800, 440, "combine into what no", "q", "middle")); b.append(_t(800, 456, "single option held", "q", "middle"))
    b.append('<path d="M30 476H1010" class="lq" fill="none"/>')
    b.append(_t(30, 502, "TRAINED ON DECISIONS FROM REAL DESIGN PROJECTS", "m"))
    for i, (k, v1, v2) in enumerate([("10,000", "trajectories annotated by hand from", "180+ companies, rejected ideas kept"),
                                     ("1,000,000", "generated by a small model", "trained to force divergence"),
                                     ("Spot checks", "by practitioners who had run", "similar projects")]):
        x = 30 + i * 335
        b.append(_box(x, 514, 310, 70, None, None, [], accent=(i == 0)))
        b.append(_t(x + 14, 536, k, "h")); b.append(_t(x + 14, 555, v1, "b")); b.append(_t(x + 14, 572, v2, "b"))
        if i < 2:
            b.append(_arrow(f"M{x + 312} 549H{x + 333}", m))
    return _svg(592, "".join(b), "Convergent reasoning seeks one answer; creative reasoning unfolds, compares, prunes and fuses, trained on real design decisions", m)


def agent():
    m = "a-ag"
    b = [_t(30, 18, "ONE PRODUCT-INNOVATION PROJECT, FROM BRIEF TO DECISION", "m")]
    stages = [("Brief", "a question", "arrives"), ("Clarify", "set the bounds", "with people"),
              ("Research", "past decisions,", "public signals"), ("Diverge", "many directions", "· Work 02"),
              ("Confirm", "a person", "approves the plan"), ("Validate", "personas and", "interviews · Work 01"),
              ("Report", "every claim", "with its evidence")]
    people = {1, 4, 6}
    for i, (s, d1, d2) in enumerate(stages):
        x = 30 + i * 140
        b.append(_box(x, 62, 126, 74, accent=(i in (3, 5))))
        b.append(_t(x + 63, 86, s, "h", "middle"))
        b.append(_t(x + 63, 106, d1, "q", "middle")); b.append(_t(x + 63, 122, d2, "q", "middle"))
        if i < 6:
            b.append(_arrow(f"M{x + 127} 99H{x + 138}", m))
        if i in people:
            b.append(f'<path d="M{x + 63} 138V178" class="lq dash" fill="none"/>'
                     f'<circle cx="{x + 63}" cy="186" r="7" class="dot"/>')
    b.append(_arrow("M913 62V46H93V60", m, dashed=True))
    b.append(_t(503, 40, "decisions, including what was rejected and why, written back for the next project", "q", "middle"))
    b.append(_t(30, 214, "PEOPLE SET THE BOUNDS, APPROVE THE PLAN AND MAKE THE CALL", "m"))
    b.append(f'<rect x="30" y="232" width="980" height="222" rx="3" class="bx ac-b"/>')
    b.append(_t(46, 256, "WORK 03 · ONE AGENT ACROSS THE WHOLE ARC", "m ac-t"))
    b.append(_t(46, 280, "A long-running, proactive product-innovation agent", "h"))
    rows = [("Agent harness", "runs many agents in parallel for hours; resumes after failure; every step can be replayed"),
            ("Decision graph", "the organization's past decisions, which start new tasks and rule out rejected directions"),
            ("Models", "Subjective World Model (Work 01), Creative Reasoning Model (Work 02), and others")]
    for i, (k, v) in enumerate(rows):
        y = 300 + i * 50
        b.append(f'<rect x="46" y="{y}" width="948" height="40" rx="2" class="bx"/>')
        b.append(_t(62, y + 25, k, "h")); b.append(_t(220, y + 25, v, "b"))
    return _svg(472, "".join(b), "A long-running agent carries a product-innovation project from brief to decision, with people setting bounds, approving and deciding", m)


def computability():
    m = "a-co"
    b = [_t(30, 30, "DESIGN KNOWLEDGE, MADE COMPUTABLE", "m")]
    items = [("(a) Youth-subculture colour", "palettes from Chinese youth subcultures"),
             ("(b) Blind-box dataset", "designer toys sold as blind boxes"),
             ("(c) Chinese traditional craft", "including Jinshan farmer painting"),
             ("(d) Prometheus", "a knowledge graph of design knowledge")]
    for i, (t, d) in enumerate(items):
        y = 46 + i * 76
        b.append(_box(30, y, 330, 62, None, t, [d], accent=(i == 3)))
        b.append(f'<path d="M360 {y + 31}H400" class="ln" fill="none"/>')
    b.append('<path d="M400 77V305" class="ln" fill="none"/>')
    b.append(_t(440, 68, "WHAT BECOMES POSSIBLE", "m"))
    for i, t in enumerate(["Identify creativity", "Evaluate creativity", "Generate creative work"]):
        y = 84 + i * 76
        b.append(_arrow(f"M400 {y + 31}H438", m))
        b.append(_box(440, y, 260, 62))
        b.append(_t(570, y + 36, t, "h", "middle"))
        b.append(f'<path d="M700 {y + 31}H740" class="ln" fill="none"/>')
    b.append('<path d="M740 115V267" class="ln" fill="none"/>')
    b.append(_arrow("M740 191H778", m))
    b.append(_box(780, 136, 230, 110, "BUILT ON THIS GROUND", None,
                  ["Work 01 Subjective World Model", "Work 02 Creative Reasoning", "Work 03 Agentic Creativity"]))
    return _svg(360, "".join(b), "Datasets and a knowledge graph make it possible to identify, evaluate and generate creative work", m)


def said_vs_did():
    m = "a-sd"
    b = [_t(0, 14, "ONE PERSON, TWO RECORDS \u00b7 ILLUSTRATIVE", "m")]
    b.append(_box(0, 28, 520, 106, "WHAT THEY SAY IN A SURVEY", None,
                  ["\u201cI care about my health; I\u2019ve quit sugary drinks.\u201d",
                   "\u201cPrice doesn\u2019t matter; quality does.\u201d", "\u201cAds don\u2019t affect me.\u201d"], lh=22))
    b.append(_t(260, 162, "\u2260", "big", "middle"))
    b.append(_box(0, 174, 520, 106, "WHAT THEY DO", None,
                  ["11 orders of sweetened tea in 90 days",
                   "70%+ of orders placed after a coupon",
                   "two repeat buys within 48h of a promoted post"], accent=True, lh=22))
    b.append(_t(0, 304, "The model keeps both records and weighs them.", "q"))
    return _svg(310, "".join(b), "What a person says and what they do differ; the model keeps both", m, 520, "dia sm")


def diverge_example():
    m = "a-dx"
    b = [_t(0, 14, "ONE SUB-PROBLEM OF A GIFT-BOX BRIEF \u00b7 ILLUSTRATIVE", "m")]
    b.append('<rect x="0" y="90" width="128" height="58" rx="3" class="bx ac-b"/>')
    b.append(_t(64, 115, "How does", "h", "middle")); b.append(_t(64, 137, "the box open?", "h", "middle"))
    cands = [("Magnetic lid", "pencil case", False), ("Drawer", "jewelry box", True),
             ("Two-tier lid", "tea caddy", False), ("Tear strip", "parcel box", False),
             ("Fold-out", "envelope", True)]
    for i, (idea, src, pruned) in enumerate(cands):
        y = 28 + i * 40
        b.append(f'<path d="M128 119C142 119 142 {y + 16} 156 {y + 16}" class="lq" fill="none"/>')
        b.append(f'<rect x="156" y="{y}" width="304" height="32" rx="3" class="bx{" dash" if pruned else ""}"/>')
        b.append(_t(168, y + 22, idea, "h" if not pruned else "q")); b.append(_t(290, y + 22, "\u2190 " + src, "q"))
        if pruned:
            b.append(_t(452, y + 22, "pruned", "m", "end"))
        elif i in (0, 2):
            b.append(_arrow(f"M462 {y + 16}L498 119", m))
    b.append(_t(570, 78, "FUSED", "m", "middle"))
    b.append(_box(500, 90, 140, 58, None, None, [], accent=True))
    b.append(_t(570, 115, "magnetic lid", "h", "middle")); b.append(_t(570, 137, "\u00d7 two-tier lid", "h", "middle"))
    return _svg(232, "".join(b), "The model unfolds one sub-problem into ideas borrowed from other categories, prunes some, and fuses the rest", m, 640, "dia sm")


def tezign():
    m = "a-tz"
    b = [_t(30, 22, "TEZIGN\u2019S AGENT STACK, GEA (GENERAL-PURPOSE ENTERPRISE AGENT)", "m")]
    b.append(_box(30, 36, 730, 52))
    b.append(_t(46, 60, "Proactive agents", "h")); b.append(_t(46, 78, "start work on their own", "q"))
    for i, t in enumerate(["Insight", "Innovation", "Marketing"]):
        x = 380 + i * 126
        b.append(f'<rect x="{x}" y="48" width="114" height="28" rx="3" class="bx"/>'); b.append(_t(x + 57, 67, t, "b", "middle"))
    b.append(_box(30, 98, 730, 52))
    b.append(_t(46, 122, "Agent operating system", "h")); b.append(_t(46, 140, "skills, connectors, orchestration, evaluation", "q"))
    b.append(_t(380, 129, "long tasks run in parallel; every step can be replayed", "b"))
    b.append(_box(30, 160, 730, 52))
    b.append(_t(46, 184, "Decision graph", "h")); b.append(_t(46, 202, "the organization\u2019s context", "q"))
    b.append(_t(380, 191, "past decisions start new tasks and set their bounds", "b"))
    b.append(_box(30, 222, 200, 76))
    b.append(_t(46, 246, "Content library", "h")); b.append(_t(46, 266, "10 PB of assets,", "b")); b.append(_t(46, 284, "72 metadata dimensions", "b"))
    b.append(_box(240, 222, 520, 76))
    b.append(_t(256, 246, "Models", "h"))
    for i, (t, ac) in enumerate([("Subjective World Model \u00b7 01", True), ("Creative Reasoning \u00b7 02", True), ("Third-party", False)]):
        x, w = [(256, 190), (456, 170), (636, 110)][i]
        b.append(f'<rect x="{x}" y="258" width="{w}" height="28" rx="3" class="{"bx ac-b" if ac else "bx"}"/>')
        b.append(_t(x + w / 2, 276, t, "q" if not ac else "b", "middle"))
    b.append(_arrow("M764 167H836", m))
    b.append(_box(840, 36, 170, 262, None, None, [], accent=True))
    for i, (n, l1, l2) in enumerate([("200+", "enterprises", ""), ("1M+", "professional users", ""),
                                    ("77%", "blind-test preference", "over a base model, 2025")]):
        y = 82 + i * 80
        b.append(_t(925, y, n, "big", "middle")); b.append(_t(925, y + 20, l1, "b", "middle"))
        if l2:
            b.append(_t(925, y + 37, l2, "q", "middle"))
    return _svg(310, "".join(b), "Tezign's agent stack: proactive agents on an agent operating system, a decision graph, a content library and models", m)


SVG_CSS = """
.dia{width:100%;height:auto;display:block;font-family:var(--sans)}
.dia.sm .h{font-size:18px}.dia.sm .b{font-size:16px}.dia.sm .q{font-size:15px}.dia.sm .m{font-size:12.5px}
.dia .bx{fill:none;stroke:var(--ink);stroke-width:1.1}
.dia .ac-b{stroke:var(--accent);stroke-width:1.8;fill:var(--tint)}
.dia .ln{stroke:var(--ink);stroke-width:1.1}
.dia .lq{stroke:var(--rule);stroke-width:1}
.dia .dash{stroke-dasharray:4 4}
.dia .mk{fill:var(--ink)}
.dia .dot{fill:var(--ink)}
.dia .dot-ac{fill:var(--accent)}
.dia text{fill:var(--ink)}
.dia .h{font-size:15px;font-weight:600}
.dia .b{font-size:13px}
.dia .q{font-size:12.5px;fill:var(--muted)}
.dia .m{font-family:var(--mono);font-size:11px;letter-spacing:.08em;fill:var(--muted)}
.dia .ac-t{fill:var(--accent)}
.dia .big{font-family:var(--serif);font-size:30px}
"""


def bmr_quadrant():
    m = "a-bq"
    x0, y0, w, h = 200, 60, 560, 420
    mx, my = x0 + w / 2, y0 + h / 2
    b = [f'<rect x="{x0}" y="{y0}" width="{w / 2}" height="{h / 2}" class="ac-b" style="stroke:none"/>',
         f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" class="bx"/>',
         f'<path d="M{mx} {y0}V{y0 + h}M{x0} {my}H{x0 + w}" class="ln" fill="none" style="stroke-width:1.8"/>']
    for d in (f"M{mx} {my}L{x0 - 8} {y0 - 8}", f"M{mx} {my}L{x0 + w + 8} {y0 - 8}",
              f"M{mx} {my}L{x0 - 8} {y0 + h + 8}", f"M{mx} {my}L{x0 + w + 8} {y0 + h + 8}"):
        b.append(f'<path d="{d}" class="lq dash" fill="none" marker-end="url(#{m})"/>')
    b += [_t(mx, y0 - 16, "BRAIN · WANTS TO", "m", "middle"), _t(mx, y0 + h + 28, "BRAIN · HAS TO", "m", "middle"),
          _t(x0 - 12, my + 4, "MACHINE · UNABLE", "m", "end"), _t(x0 + w + 12, my + 4, "MACHINE · ABLE", "m"),
          _t(x0 - 14, y0 - 14, "What humans are good at", "q", "end"), _t(x0 + w + 14, y0 - 14, "What people want to do", "q"),
          _t(x0 - 14, y0 + h + 24, "What people would rather not do", "q", "end"),
          _t(x0 + w + 14, y0 + h + 24, "What machines are good at", "q")]
    q = [(x0, y0, "2 · THE BRAIN’S STRENGTHS", ["Creative ideation", "Communication"]),
         (mx, y0, "1 · HUMAN EXPERIENCE", ["Material gathering"]),
         (x0, my, "3 · MACHINE POTENTIAL", ["Management", "Non-repetitive physical work"]),
         (mx, my, "4 · MACHINE OPTIMIZATION", ["Information processing", "Repetitive physical work"])]
    for qx, qy, lab, items in q:
        b.append(_t(qx + 14, qy + 24, lab, "m"))
        for i, it in enumerate(items):
            b.append(_t(qx + w / 4, qy + 110 + i * 34, it, "h", "middle"))
    b.append(_t(x0 + 14, y0 + 52, "H.I. · the human brain", "h ac-t"))
    b.append(_t(x0 + w - 14, y0 + h - 16, "A.I. · the machine", "h", "end"))
    for i, (k, v) in enumerate([("TOP HALF", "What people should lead"), ("BOTTOM HALF", "What to hand to machines"),
                                ("LEFT HALF", "High brain–machine ratio"), ("RIGHT HALF", "Low brain–machine ratio")]):
        y = (y0 + 30 if i < 2 else my + 60) + (i % 2) * 54
        b.append(_t(x0 + w + 40, y, k, "m")); b.append(_t(x0 + w + 40, y + 20, v, "b"))
    return _svg(520, "".join(b), "The brain-machine ratio quadrant: what people want or have to do against what machines can or cannot do", m)


def bmr_versions():
    m = "a-bv"
    b = []
    pw = 330
    # 1.0 Capability: tasks, human share of time (size) and machine share (fill)
    tasks = [("Management", 11, 9), ("Creative ideation", 21, 18), ("Communication", 16, 20),
             ("Non-repetitive physical work", 10, 25), ("Material gathering", 16, 64),
             ("Information processing", 16, 69), ("Repetitive physical work", 10, 78)]
    b += [_t(0, 20, "BMR 1.0 · CAPABILITY", "m"), _t(0, 66, "BMR 1.0 =", "h"),
          _t(92, 54, "Human input", "b"), '<path d="M92 62H190" class="ln"/>', _t(92, 80, "Machine input", "b")]
    for i, (t, hs, ms) in enumerate(tasks):
        cx, cy, r = 210, 112 + i * 33, 3 + hs * 0.6
        b.append(f'<clipPath id="bv{i}"><rect x="{cx + r - 2 * r * ms / 100}" y="{cy - r}" width="{2 * r * ms / 100}" height="{2 * r}"/></clipPath>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="dot-ac" clip-path="url(#bv{i})"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="bx"/>')
        b.append(_t(186, cy + 4, t, "q", "end"))
        b.append(_t(236, cy + 4, f"{ms}%", "m ac-t"))
    b += [_t(0, 352, "Fill and %: share machines can take", "q"), _t(0, 370, "Circle size: share of the designer’s time", "q")]
    # 2.0 Subjectivity
    ox = pw + 25
    b += [_t(ox, 20, "BMR 2.0 · SUBJECTIVITY", "m"), _t(ox, 66, "BMR 2.0 = BMR 1.0 × subjectivity", "h")]
    base, c = 280, ox + pw / 2
    b.append(f'<path d="M{ox} {base}H{ox + pw}" class="ln" style="stroke-width:1.8"/>')
    for hgt, cls in ((50, "ln"), (90, "lq"), (130, "lq")):
        b.append(f'<path d="M{c - 120} {base}C{c - 50} {base} {c - 40} {base - hgt} {c} {base - hgt}'
                 f'S{c + 50} {base} {c + 120} {base}" class="{cls}" fill="none"/>')
    b.append(f'<path d="M{c} {base}V{base - 150}" class="ln dash" fill="none" marker-end="url(#{m})"/>')
    b.append(_t(c + 10, base - 148, "subjective will", "h ac-t"))
    b += [_t(ox, base + 24, "Brain: time people invest", "q"), _t(ox + pw, base + 44, "Machine: how far it can be automated", "q", "end")]
    # 3.0 Trust
    ox = 2 * (pw + 25)
    b += [_t(ox, 20, "BMR 3.0 · TRUST", "m"), _t(ox, 66, "BMR 3.0 = human-centered AI", "h")]
    cx, cy = ox + 165, 230
    b.append(f'<rect x="{cx}" y="{cy - 80}" width="70" height="80" class="ac-b" style="stroke:none"/>')
    b.append(f'<rect x="{cx - 70}" y="{cy}" width="70" height="80" class="bx dash"/>')
    b.append(f'<path d="M{cx} {cy - 90}V{cy + 90}M{cx - 75} {cy}H{cx + 75}" class="ln dash" fill="none"/>')
    b += [_t(cx, cy - 98, "Not delegable to machines", "q", "middle"), _t(cx, cy + 108, "Delegable to machines", "q", "middle"),
          _t(cx - 80, cy + 4, "Easy for humans", "q", "end"), _t(cx + 80, cy + 4, "Hard for", "q"), _t(cx + 80, cy + 20, "humans", "q"),
          _t(cx + 8, cy - 40, "Augmentation", "h ac-t"), _t(cx - 8, cy + 46, "Automation", "h", "end")]
    return _svg(380, "".join(b), "BMR 1.0 measures capability, BMR 2.0 adds subjective will, BMR 3.0 builds trust through human-centered AI", m)
