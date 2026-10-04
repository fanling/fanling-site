"""Loads the site and portfolio text from ../content.md (the file Ling edits).
Only layout settings that are not text live here."""

import os
from mdcontent import TODO, parse, paras, text, facts, rows, items  # noqa: F401  (TODO used by site/portfolio)

_D = parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content.md"))


def _sec(prefix):
    for k, v in _D.items():
        if k == prefix or k.startswith(prefix + " |") or k.startswith(prefix + " "):
            return k, v
    raise KeyError(f"content.md has no section '# {prefix}'")


def _f(sec, prefix):
    for k, v in sec.items():
        if k == prefix or k.startswith(prefix + " (") or k.startswith(prefix + " "):
            return v
    return []


# Layout settings per work, keyed by its content.md section. Text for each work is in content.md.
# "group" splits current work from past work; "label" is how the work is named on the page.
_WORK_SETTINGS = {
    "Work 01": {"no": "01", "group": "current", "slug": "subjective-world-model", "diagram": "world_model",
                "figure_fn": "said_vs_did", "media": [
                    {"video": "atypica.mp4", "poster": "atypica-layers.jpg", "pdf": False,
                     "caption": "atypica.AI in use: building personas, interviewing them and writing up the findings (film, 4 min)."},
                    {"image": "atypica-layers.jpg", "web": False,
                     "caption": "Each persona is built from four layers of evidence: expression, story, cognition and behavior."},
                    {"image": "atypica-report.jpg", "web": False,
                     "caption": "A research report atypica.AI wrote from its simulated interviews."}]},
    "Work 02": {"no": "02", "group": "current", "slug": "creative-reasoning-model", "diagram": "creative_reasoning",
                "figure_fn": "diverge_example", "dia_w": "80%", "fig_side": "right", "media": [
                    {"image": "cr-four-step.png",
                     "caption": "Four-step tree-structured divergence: extract, diverge, expand, converge."},
                    {"video": "cr.mp4", "poster": "cr-video-frame.jpg", "pdf_image": "cr-video-frame.jpg",
                     "caption": "The model turning one intent into several scored directions (film, 30 s)."}]},
    "Work 03": {"no": "03", "group": "current", "slug": "agentic-creativity", "diagram": "agent", "media": [
                    {"image": "agent-loop.png", "opener": True,
                     "caption": "The agent's loop: intent becomes a signal, then a plan, new work and evaluations, "
                                "bounded by a consumer world model and a company world model."},
                    {"image": "agent-timeline.png",
                     "caption": "Five days of one long-running task, moving between signal, plan, create and evals."}]},
    "Past work 01": {"no": "", "group": "past", "label": "Past research", "sheet": "PW-01",
                     "slug": "computability-of-creativity", "diagram": "computability", "media": [
                         {"video": "pw-colour.mp4", "poster": "pw-colour.jpg", "part": "a",
                          "caption": "Palette generation and colorization for Chinese youth subcultures (film, 43 s)."},
                         {"video": "pw-blindbox.mp4", "poster": "pw-blindbox.jpg", "part": "b",
                          "caption": "New blind-box figures, outfits and scenes generated in 3D (film, 50 s)."},
                         {"video": "pw-craft.mp4", "poster": "pw-craft.jpg", "part": "c",
                          "caption": "A visitor's sketch painted in the Jinshan farmer-painting style (film, 3.5 min; interface in Chinese)."},
                         {"video": "pw-prometheus.mp4", "poster": "pw-prometheus.jpg", "part": "d",
                          "caption": "Asking Prometheus about design (film, 77 s; interface in Chinese)."}]},
    "Past work 02": {"no": "", "group": "past", "label": "Past research", "sheet": "PW-02",
                     "slug": "brain-machine-ratio", "diagram": "bmr_quadrant", "dia_w": "74%", "diagram_extra": "bmr_versions",
                     "parts_first": True, "diagram_label": "(a) Quantitative study · the BMR quadrant", "extra_label": "(a) Quantitative study · three versions", "gallery_label": "(b) Qualitative study · the nine timeline panels",
                     "media_label": "(b) Qualitative study · exhibition and timeline", "media": [
                         {"part": "a", "diagram": "bmr_quadrant", "caption": ""},
                         {"image": "wdcc-entrance.jpg", "part": "b",
                          "caption": "WDCC 2026 Theme Exhibition, \u201cDesigning Generation: From AI-Driven Design to Designing AI\u201d, Shanghai."},
                         {"image": "wdcc-hall.jpg",
                          "caption": "The timeline of creative tools on the exhibition walls, WDCC 2026."},
                         {"gallery": [f"tools-timeline-{i}.jpg" for i in range(1, 10)],
                          "caption": "The nine timeline panels, 1400 to 2026, each in three threads: technology, tools and ideas (second edition, 2026; in Chinese)."}],
                     "diagram_source": "Redrawn from Ling Fan, <i>From Universality of Computation to the Universality of Imagination: "
                                       "A Catalog on Design and Artificial Intelligence</i> (Tongji University Press, 2019)."},
}

_b = _sec("Basics")[1]
NAME = text(_f(_b, "Name"))
NAME_ZH = text(_f(_b, "Chinese name"))
THESIS = text(_f(_b, "Thesis"))
SHORT_BIO = text(_f(_b, "Short bio"))
CONTACT = text(_f(_b, "Contact email"))
PROFILES = facts(_f(_b, "Profiles"))
SUBSTACK = rows(_f(_b, "Substack"), 2)[0]

STATEMENT = paras(_f(_sec("Statement")[1], "Text"))

WORKS = []
for key, cfg in _WORK_SETTINGS.items():
    head, s = _sec(key)
    no = cfg["no"]
    w = {"slug": cfg["slug"], "no": no, "group": cfg["group"], "label": cfg.get("label", f"Work {no}"),
         "sheet": cfg.get("sheet", f"W-{no}"), "title": head.split("|", 1)[1].strip(),
         "sub": text(_f(s, "Subtitle")), "question": text(_f(s, "Question")), "body": paras(_f(s, "Text")),
         "facts": facts(_f(s, "Facts")), "links": facts(_f(s, "Links")), "images": items(_f(s, "Images to add")),
         "diagram": cfg["diagram"]}
    if _f(s, "Series"):
        w["parts"] = rows(_f(s, "Series"), 3)
    if "figure_fn" in cfg:
        w["figure"] = (cfg["figure_fn"], text(_f(s, "Figure caption")))
    for k in ("dia_w", "fig_side", "media", "diagram_extra", "diagram_source", "media_label", "parts_first", "diagram_label", "extra_label", "gallery_label"):
        if k in cfg:
            w[k] = cfg[k]
    WORKS.append(w)

CURRENT_WORKS = [w for w in WORKS if w["group"] == "current"]
PAST_WORKS = [w for w in WORKS if w["group"] == "past"]

_t = _sec("Tezign")[1]
TEZIGN = {"title": "Tezign", "sub": text(_f(_t, "Subtitle")), "body": paras(_f(_t, "Text")), "facts": facts(_f(_t, "Facts"))}

_l = _sec("Lab")[1]
LAB = {"title": text(_f(_l, "Title")), "body": paras(_f(_l, "Text")), "facts": facts(_f(_l, "Facts")),
       "funded": rows(_f(_l, "Funded projects"), 3)}

_e = _sec("Teaching")[1]
TEACHING = {"body": paras(_f(_e, "Text")), "supervision": paras(_f(_e, "Supervision and programs")),
            "todo": text(_f(_e, "Still to add"))}

_w = _sec("Writing")[1]
WRITING = {"books": rows(_f(_w, "Books"), 3)}
BOOK_PHOTOS = {"2019": ("book-2019-cover.jpg", [
    ("book-2019-timeline.jpg", "Data and computation in design, from the 1960s to the 2010s."),
    ("book-2019-research.jpg", "AI research in design, by field, 2016–2018."),
    ("book-2019-hcml.jpg", "Human-centered machine learning: human in the loop and machine in the loop."),
    ("book-2019-enterprise.jpg", "Why companies adopt design AI: efficiency, quality and team structure.")]),
               "2014": ("book-2014-cover.jpg", [
    ("book-2014-spread.jpg", "Inside the book: readings of Kenneth Frampton and Rem Koolhaas.")])}

NEWS = rows(_f(_sec("News")[1], "News"), 3, none_if_empty=(2,))
TALKS = rows(_f(_sec("Talks")[1], "Talks"), 4, none_if_empty=(3,))
PUBLICATIONS = rows(_f(_sec("Publications")[1], "Publications"), 5, none_if_empty=(4,))
PATENTS = rows(_f(_sec("Patents")[1], "Patents"), 2)
APPOINTMENTS = rows(_f(_sec("Appointments")[1], "Appointments"), 3)
EDUCATION = rows(_f(_sec("Education")[1], "Degrees"), 3)
HONORS = rows(_f(_sec("Honors")[1], "Honors"), 2)
SERVICE = rows(_f(_sec("Service")[1], "Service"), 2)
MEDIA = items(_f(_sec("Media")[1], "Media"))
