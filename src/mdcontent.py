"""Read and write content.md, the editable text source for the site and the portfolio PDF.

Format: '# ' starts a section, '## ' a field inside it. A field holds paragraphs (separated by a
blank line), '- Label: value' facts, or '- a | b | c' rows. '[To add: ...]' marks a gap and
*text* is italic. Anything before the first '# ' is a note for editors and is ignored."""

import re

TODO_RE = re.compile(r'<span class="todo">To add: (.*?)</span>')


def TODO(s):
    return f'<span class="todo">To add: {s}</span>'


# ---- text <-> markdown inline -------------------------------------------------

def to_md(s):
    s = TODO_RE.sub(lambda m: f"[To add: {m.group(1)}]", s)
    return re.sub(r"<em>(.*?)</em>", r"*\1*", s)


def from_md(s):
    s = re.sub(r"\[To add: (.*?)\]", lambda m: TODO(m.group(1)), s)
    return re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)


# ---- parsing ------------------------------------------------------------------

def parse(path):
    """Return {section: {field: [lines]}}; text before the first field is stored under ''."""
    doc, sec, field = {}, None, None
    src = re.sub(r"<!--.*?-->", "", open(path, encoding="utf-8").read(), flags=re.S)   # hidden lines
    for raw in src.splitlines():
        line = re.sub(r"\\([\[\]*_|#.!()\-+`])", r"\1", raw.rstrip())   # undo escapes added by a doc export
        if line.startswith("# "):
            sec = line[2:].strip(); field = ""
            doc[sec] = {"": []}
        elif line.startswith("## ") and sec is not None:
            field = line[3:].strip()
            doc[sec][field] = []
        elif sec is not None:
            doc[sec][field].append(line)
    return doc


def paras(lines):
    out, cur = [], []
    for l in lines + [""]:
        if l.strip():
            cur.append(l.strip())
        elif cur:
            out.append(from_md(" ".join(cur))); cur = []
    return out


def text(lines):
    return " ".join(paras(lines))


def _items(lines):
    items = []
    for l in lines:
        if l.startswith("- "):
            items.append(l[2:].strip())
        elif l.strip() and items:           # a wrapped list line continues the item above
            items[-1] += " " + l.strip()
    return items


def facts(lines):
    out = []
    for it in _items(lines):
        k, _, v = it.partition(": ")
        out.append((from_md(k.strip()), from_md(v.strip())))
    return out


def rows(lines, n=None, none_if_empty=()):
    out = []
    for it in _items(lines):
        cells = [from_md(c.strip()) for c in it.split("|")]
        cells = ["" if c == "\u2014" else c for c in cells]   # an em dash alone marks an empty cell
        if n:
            cells = (cells + [""] * n)[:n]
        cells = [None if (i in none_if_empty and c == "") else c for i, c in enumerate(cells)]
        out.append(tuple(cells))
    return out


def items(lines):
    return [from_md(i) for i in _items(lines)]
