#!/usr/bin/env python3
"""Build The Survival Guide static website.

Reads the outline from plan.md and written chapters from content/*.html,
then writes a complete static site to site/. Standard library only.

    python3 build.py
"""
import os
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLAN = ROOT / "plan.md"
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"
OUT = ROOT / "site"

SITE_TITLE = "The Survival Guide"
BUILD_DATE = "November 11, 2026"

# Written chapters that replace a planned chapter: (part, planned-title prefix, slug, display title)
CONTENT_MAP = [
    (0, "How to use", "how-to-use", "How to Use This Guide"),
    (0, "Disclaimer", "golden-rules", "Disclaimer & Golden Rules"),
    (0, "RED PAGES", "red-pages", "Red Pages — Emergency Quick Reference"),
    (2, "Water", "water", "Water: Finding, Collecting, Purifying & Storing"),
    (2, "Fire", "fire", "Fire: Making It, Using It & Keeping It Safe"),
    (2, "Shelter", "shelter", "Shelter & Staying Warm or Cool"),
    (4, "Foraging Principles", "foraging-principles", "Foraging Principles & Plant Identification Basics"),
    (9, "Signaling", "signaling-rescue", "Signaling, Rescue & Communication"),
    (0, "When Help Isn", "when-help-isnt-coming", "When Help Isn't Coming"),
    (7, "Patient Assessment", "patient-assessment", None),
    (7, "Bleeding, Wounds", "wounds-burns-infection", None),
    (7, "Bones, Joints", "bones-joints-head-spine", None),
    (7, "Shock & Circulation", "shock-and-circulation", None),
    (7, "Environmental Emergencies", "environmental-emergencies", None),
    (7, "Bites, Stings", "bites-stings-poisoning", None),
    (7, "Illness in the Field", "illness-in-the-field", None),
    (7, "Medical Kits", "medical-kits-and-medicines", None),
    (7, "Emergency Childbirth", "emergency-childbirth-and-long-term-care", None),
    (7, "Evacuation & Rescue", "evacuation-and-rescue-decisions", None),
    (7, "Hygiene & Sanitation", "hygiene-and-sanitation", None),
    (9, "Maps & Compass", "maps-and-compass", None),
    (9, "Travel & Movement", "travel-and-movement", None),
    (9, "Weather", "weather", None),
    (1, "Survival Mindset", "survival-mindset-and-psychology", None),
    (1, "Priorities", "priorities", None),
    (1, "Kits & Gear", "kits-and-gear", None),
    (1, "Clothing & Layering", "clothing-and-layering", None),
    (9, "Navigation Without", "navigation-without-instruments", None),
    (3, "Cordage", "cordage-knots-and-lashings", None),
    (13, "Great Plains", "na-07-great-plains-and-prairies", None),
    (13, "Eastern Deciduous", "na-08-eastern-deciduous-forest-appalachians-great-lakes-and-ozarks", None),
]
# Written pages added beside a planned chapter: (part, insert after title prefix, slug, title, summary)
EXTRA_PAGES = [
    (4, "Must-Know Deadly", "lookalikes-carrot-family", "Deadly Look-Alikes: The Carrot Family",
     "Wild carrot, poison hemlock, water hemlock, wild parsnip, giant hogweed and cow parsnip, compared feature by feature."),
    (6, "Vitamins", "vitamin-c", "Vitamin C & Scurvy",
     "What vitamin C does, how fast scurvy sets in, and where to get vitamin C from stockpiles, gardens and the wild."),
]
# Planned chapters that are already partly covered by a written page
COVERED_IN = [
    (2, "Staying Warm", ["shelter"]),
    (4, "Plant Identification", ["foraging-principles"]),
    (4, "Must-Know Deadly", ["lookalikes-carrot-family"]),
    (6, "Vitamins", ["vitamin-c"]),
    (9, "Communication", ["signaling-rescue"]),
    (9, "Navigation Without", ["signaling-rescue"]),
]

PART_BLURBS = {
    0: "Start here: how the guide works, the rules that keep you alive, and the emergency quick reference.",
    1: "Mindset, priorities, kits, clothing and plans for every kind of emergency.",
    2: "The three things that keep you alive first: water, fire and shelter.",
    3: "The how-to library: cordage, tools, crafts, blacksmithing, building, machines, pottery and transport.",
    4: "Getting food from the land and water: foraging, mushrooms, fishing, hunting, tracking and trapping.",
    5: "Food safety, cooking without power, preserving food, staples from scratch and recipes.",
    6: "Calories, vitamins, minerals and the natural toxins in food.",
    7: "Wilderness first aid, hygiene, herbal medicine and psychoactive plants.",
    8: "Gardening, beekeeping, livestock, fish, insect farming and mushroom growing.",
    9: "Maps and compass, weather, natural disasters, signaling and radio.",
    10: "Woods, stones, minerals, clays, fibers, animal materials, chemicals and salvage.",
    11: "Oceans, seas, rivers, lakes, landforms and climate zones of the world.",
    12: "Plants and animals found on almost every continent.",
    13: "Field guides to 55 regions of the world: plants, animals, water and hazards.",
    14: "Conversion tables, glossary, checklists, calendars and indexes.",
}
VOLUMES = {0: "Every volume", 1: "Volume 1", 2: "Volume 1", 3: "Volume 1", 4: "Volume 2", 5: "Volume 2",
           6: "Volume 2", 7: "Volume 2", 8: "Volume 3", 9: "Volume 3", 10: "Volume 3", 11: "Volume 3",
           12: "Volume 4", 13: "Volumes 4–5", 14: "Every volume"}

ICONS = {
    0: '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 7.5v9M7.5 12h9"/>',
    1: '<path d="M9 6V4.5A1.5 1.5 0 0 1 10.5 3h3A1.5 1.5 0 0 1 15 4.5V6"/><rect x="5" y="6" width="14" height="15" rx="4"/><path d="M9 13h6v4H9z"/>',
    2: '<path d="M12 3c1 3 5 5.5 5 10a5 5 0 0 1-10 0c0-2.5 1.5-4 2.5-5 .3 1.6 1 2.6 2 3 0-3-.5-5.5.5-8z"/>',
    3: '<path d="M14.5 3.5l6 6-3 3-6-6z"/><path d="M12.5 8.5L4 17a2.1 2.1 0 0 0 3 3l8.5-8.5"/>',
    4: '<path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15z"/><path d="M5 19l9-9"/>',
    5: '<path d="M4 10h16v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M2 10h20"/><path d="M9.5 7c0-1 1-1.5 1-2.5M13.5 7c0-1 1-1.5 1-2.5"/>',
    6: '<path d="M12 7.5c-2-1.5-7-1.5-7 4 0 4 3 8.5 5 8.5 1 0 1.3-.5 2-.5s1 .5 2 .5c2 0 5-4.5 5-8.5 0-5.5-5-5.5-7-4z"/><path d="M12 7.5c0-2 1-3.5 3-4.5"/>',
    7: '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/><path d="M7.5 12h2.5l1.5-2.5 2 4.5 1.5-2h1.5"/>',
    8: '<path d="M12 21v-9"/><path d="M12 12c0-4-3-6-7-6 0 4 3 6 7 6z"/><path d="M12 10c0-3.5 2.5-6 7-6 0 4-3 6-7 6z"/><path d="M7 21h10"/>',
    9: '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    10: '<circle cx="7" cy="16" r="3"/><circle cx="17" cy="16" r="3"/><circle cx="12" cy="8" r="3"/>',
    11: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    12: '<circle cx="7" cy="9.5" r="1.8"/><circle cx="10.5" cy="6" r="1.8"/><circle cx="14.5" cy="6" r="1.8"/><circle cx="18" cy="9.5" r="1.8"/><path d="M8 17c0-3 2-5 4-5s4 2 4 5c0 2-2 2.5-4 2.5S8 19 8 17z"/>',
    13: '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
    14: '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5"/><path d="M8 7h7"/>',
}

REGION_TEMPLATE = [
    "Regional map: rivers, lakes, terrain",
    "Countries and states, climate zones (Köppen) and biomes",
    "Seasons at a glance: temperature and rainfall",
    "Top hazards: weather, terrain, animals, plants, disease",
    "Water: major rivers and lakes, where to find water, local water hazards",
    "Fire and shelter materials: best local tinder, friction-fire woods, shelter materials",
    "Checklists: top edible plants, medicinal plants, dangerous plants, fungi, mammals, birds, reptiles and amphibians, fish, invertebrates",
    "Month-by-month foraging calendar",
    "Gardening notes: what grows well here",
    "Legal and cultural notes: foraging and hunting rules, protected areas, Indigenous knowledge",
    "Full entries for the species most typical of this region",
]


# ---------------------------------------------------------------- helpers
def slugify(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:64].rstrip("-") or "page"


def strip_md(s):
    return re.sub(r"[*`]", "", s).strip()


def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def plain(s):
    s = re.sub(r"<svg\b.*?</svg>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- parse plan
TITLE_FIX = {"World Physical Map": "World Physical & Political Maps"}


def parse_head(content):
    m = re.match(r"\*\*(.+?)\*\*\s*(.*)$", content)
    if m:
        head, rest = m.group(1), m.group(2)
    else:
        head, rest = content, ""
        m2 = re.match(r"^(.+?)\s+\(([^()]*(?:\([^()]*\)[^()]*)*)\)$", content)
        if m2:
            head, rest = m2.group(1), m2.group(2)
        elif ":" in content:
            head, rest = content.split(":", 1)
    head, rest = head.strip(), rest.strip()
    if rest.startswith(":"):
        rest = rest[1:].strip()
    info = {"num": None, "code": None, "pages": None}
    mm = re.match(r"^Ch\s*(\d+)?\.\s*", head)
    if mm:
        info["num"] = mm.group(1)
        head = head[mm.end():]
    mm = re.match(r"^(\d+[A-Z])\.\s*", head)
    if mm:
        info["code"] = mm.group(1)
        head = head[mm.end():]
    mm = re.search(r"\s*\(~(\d+)\s*pp\)", head)
    if mm:
        info["pages"] = int(mm.group(1))
        head = head[:mm.start()] + head[mm.end():]
    head = re.sub(r"\s*\(~[^)]*\)", "", head)
    head = TITLE_FIX.get(strip_md(head.rstrip(":")), head)
    info["raw_title"] = strip_md(head.rstrip(":"))
    info["title"] = info["raw_title"]
    info["summary"] = rest
    return info


def parse_subs(lines, base=0):
    items = []
    for ln in lines:
        indent = len(ln) - len(ln.lstrip(" "))
        text = re.sub(r"^\s*-\s+(\[ \]\s+)?", "", ln).strip()
        if not text or "ZAC:" in text:
            continue
        level = max(0, indent // 2 - 1) + base
        items.append((level, text))
    return items


def block_chapters(block):
    tops = []
    for ln in block["lines"]:
        if re.match(r"^- ", ln):
            tops.append([re.sub(r"^- (\[ \] )?", "", ln).strip(), []])
        elif tops:
            tops[-1][1].append(ln)
    g = block["group"]
    if g and not any(t[0].startswith("**Ch") or re.match(r"\*\*\d+[A-Z]\.", t[0]) for t in tops):
        items = []
        for c, subs in tops:
            items.append((0, c))
            items += parse_subs(subs, base=1)
        return [{"title": g["title"], "raw_title": g["title"], "code": g["code"], "num": None,
                 "pages": g["pages"], "summary": " ".join(block["intro"]), "items": items, "group": None}]
    chapters = []
    for c, subs in tops:
        info = parse_head(c)
        info["items"] = parse_subs(subs)
        info["group"] = g
        chapters.append(info)
    return chapters


def parse_plan():
    text = PLAN.read_text(encoding="utf-8")
    outline = text.split("## 4. Detailed Book Outline", 1)[1].split("\n## 5.", 1)[0]
    regions_txt = text.split("### Region list", 1)[1].split("### Species targets", 1)[0]

    parts = []
    for line in outline.splitlines():
        if not line.strip() or line.lstrip().startswith(">") or line.strip() == "---":
            continue
        m = re.match(r"^### PART (\d+) — (.+?) \(~(\d+) pp\)\s*$", line)
        if m:
            parts.append({"num": int(m.group(1)), "title": m.group(2).strip(), "pages": int(m.group(3)),
                          "intro": [], "blocks": [{"group": None, "intro": [], "lines": []}]})
            continue
        if not parts:
            continue
        part = parts[-1]
        m = re.match(r"^#### (\S+?)\. (.+?)(?: \(~(\d+) pp\))?\s*$", line)
        if m:
            part["blocks"].append({"group": {"code": m.group(1), "title": m.group(2).strip(),
                                             "pages": int(m.group(3)) if m.group(3) else None},
                                   "intro": [], "lines": []})
            continue
        block = part["blocks"][-1]
        if re.match(r"^\s*- ", line):
            block["lines"].append(line)
        else:
            t = line.strip()
            (block["intro"] if (block["group"] or block["lines"]) else part["intro"]).append(t)

    # regions
    regions, rgroup = [], None
    for ln in regions_txt.splitlines():
        m = re.match(r"^\*\*(.+?) \((\d+)\)\*\*", ln.strip())
        if m:
            rgroup = m.group(1)
            continue
        m = re.match(r"^- \[ \] ([A-Z]{2}-\d{2}) (.+?)(?: \((.+)\))?\s*$", ln.strip())
        if m:
            regions.append({"code": m.group(1), "name": m.group(2).strip(),
                            "detail": (m.group(3) or "").strip(), "group": rgroup})

    for part in parts:
        chs = []
        for b in part["blocks"]:
            chs += block_chapters(b)
        if part["num"] == 13:
            for r in regions:
                chs.append({"title": r["name"], "raw_title": r["name"], "code": r["code"], "num": None,
                            "pages": None, "summary": r["detail"],
                            "items": [(0, t) for t in REGION_TEMPLATE],
                            "group": {"code": "", "title": r["group"], "pages": None}, "region": True})
        part["chapters"] = chs
        part["groups_info"] = [b["group"] | {"intro": b["intro"]} for b in part["blocks"] if b["group"]]
    return parts


# ---------------------------------------------------------------- assemble model
def title_match(raw, prefix):
    return re.match(re.escape(prefix) + r"(\b|$)", raw) is not None


def load_status():
    p = CONTENT / "_status.json"
    return json.loads(p.read_text()) if p.exists() else {}


def assemble():
    parts = parse_plan()
    status = load_status()
    used = set()

    def unique(slug):
        base, n = slug, 2
        while slug in used:
            slug = f"{base}-{n}"
            n += 1
        used.add(slug)
        return slug

    for s in ["index", "search"]:
        used.add(s)

    for part in parts:
        part["slug"] = unique(f"part-{part['num']:02d}")
        new_list = []
        for ch in part["chapters"]:
            ch["part"] = part
            ch["covered"] = []
            for pn, prefix, slug, title in CONTENT_MAP:
                if pn == part["num"] and title_match(ch["raw_title"], prefix):
                    ch["content_slug"] = slug
                    if title:
                        ch["title"] = title
            for pn, prefix, slugs in COVERED_IN:
                if pn == part["num"] and title_match(ch["raw_title"], prefix):
                    ch["covered"] += slugs
            if ch.get("region"):
                ch["slug"] = unique(f"{ch['code'].lower()}-{slugify(ch['title'])}")
            else:
                ch["slug"] = unique(ch.get("content_slug") or slugify(ch["title"]))
            new_list.append(ch)
            for pn, prefix, slug, title, summary in EXTRA_PAGES:
                if pn == part["num"] and title_match(ch["raw_title"], prefix):
                    new_list.append({"title": title, "raw_title": title, "code": None, "num": None, "pages": None,
                                     "summary": summary, "items": [], "group": ch["group"], "part": part,
                                     "covered": [], "content_slug": slug, "slug": unique(slug)})
        part["chapters"] = new_list

    for part in parts:
        for ch in part["chapters"]:
            cs = ch.get("content_slug")
            f = CONTENT / f"{cs}.html" if cs else None
            # Unchecked drafts stay off the site unless INCLUDE_DRAFTS=1 is set.
            publishable = cs in status or os.environ.get("INCLUDE_DRAFTS") == "1"
            if f and f.exists() and publishable:
                ch["html"] = f.read_text(encoding="utf-8")
                ch["state"] = status.get(cs, {}).get("status", "draft")
                ch["checked"] = status.get(cs, {}).get("checked")
            else:
                ch["html"] = None
                ch["state"] = "outline"
        part["written"] = sum(1 for c in part["chapters"] if c["state"] in ("verified", "guide"))
    return parts


# ---------------------------------------------------------------- rendering
FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&amp;'
             'family=IBM+Plex+Mono&amp;family=Public+Sans:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">')

STATE_PILL = {
    "verified": '<span class="pill ok">Researched &amp; fact-checked</span>',
    "guide": '<span class="pill guide">Guide page</span>',
    "draft": '<span class="pill draft">Draft — fact-check pending</span>',
    "outline": '<span class="pill outline">Planned — not written yet</span>',
}
SHORT_PILL = {
    "verified": '<span class="pill ok">Written</span>',
    "guide": '<span class="pill guide">Guide</span>',
    "draft": '<span class="pill draft">Draft</span>',
    "outline": '<span class="pill outline">Planned</span>',
}


def icon(num, size=24):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[num]}</svg>')


def label(ch):
    if ch.get("code"):
        return f"{ch['code']} · {ch['title']}"
    return ch["title"]


def sidebar(parts, current_slug=None, current_part=None):
    out = ['<nav class="sidebar" id="sidebar" aria-label="Table of contents">',
           '<button class="nav-close" id="nav-close" type="button">Close menu</button>',
           '<a class="side-home" href="index.html">Home &amp; all parts</a>']
    for p in parts:
        is_open = " open" if (current_part is not None and p["num"] == current_part) else ""
        total = len(p["chapters"])
        out.append(f'<details{is_open}><summary><span class="pnum">{p["num"]:02d}</span>'
                   f'<span>{esc(p["title"])}</span><span class="pcount">{p["written"]}/{total}</span></summary><ul>')
        cur_attr = ' aria-current="page"' if current_slug == p["slug"] else ""
        out.append(f'<li><a href="{p["slug"]}.html"{cur_attr}><span class="dot" style="border-style:dotted"></span>'
                   f'<span>Part overview</span></a></li>')
        last_group = None
        for ch in p["chapters"]:
            g = ch["group"]["title"] if ch.get("group") else None
            if g and g != last_group:
                out.append(f'<li class="group-label">{esc(g)}</li>')
            last_group = g
            cls = ' class="done"' if ch["state"] in ("verified", "guide") else ""
            cur = ' aria-current="page"' if ch["slug"] == current_slug else ""
            out.append(f'<li><a href="{ch["slug"]}.html"{cls}{cur}><span class="dot"></span>'
                       f'<span>{esc(label(ch))}</span></a></li>')
        out.append("</ul></details>")
    out.append("</nav>")
    return "\n".join(out)


def layout(parts, *, title, body, current_slug=None, current_part=None, description="", body_class=""):
    full_title = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description[:200])}">
{FONT_LINK}
<link rel="stylesheet" href="assets/style.css">
</head>
<body class="{body_class}">
<a class="sr-only" href="#main">Skip to content</a>
<header class="topbar">
  <button class="nav-toggle" id="nav-toggle" type="button" aria-controls="sidebar" aria-expanded="false">Menu</button>
  <a class="brand" href="index.html">{SITE_TITLE}<small>working title</small></a>
  <div class="search" role="search">
    <label class="sr-only" for="q">Search the guide</label>
    <input id="q" type="search" placeholder="Search the guide…" autocomplete="off" spellcheck="false">
    <div class="search-results" id="q-results"></div>
  </div>
  <a class="red-link" href="red-pages.html">Emergency</a>
</header>
<div class="shell">
{sidebar(parts, current_slug, current_part)}
<main id="main">
{body}
</main>
</div>
<script src="assets/app.js"></script>
</body>
</html>
"""


def footer():
    return (f'<footer class="site-foot"><p>{SITE_TITLE} (working title) · Built {BUILD_DATE}. '
            'Educational only: not a substitute for training, professional medical care or local laws. '
            'In an emergency call 911 (US &amp; Canada), 112 (EU and many countries) or your local emergency number.</p></footer>')


def nested_list(items):
    out, depth = [], -1
    for level, text in items:
        if level > depth:
            for _ in range(level - depth):
                out.append("<ul><li>")
            depth = level
        else:
            out.append("</li>")
            while depth > level:
                out.append("</ul></li>")
                depth -= 1
            out.append("<li>")
        out.append(md_inline(text))
    while depth >= 0:
        out.append("</li></ul>")
        depth -= 1
    return "".join(out)


def add_heading_ids(content):
    seen = set()

    def rep(m):
        attrs, inner = m.group(1) or "", m.group(2)
        idm = re.search(r'\bid="([^"]+)"', attrs)
        if idm:
            seen.add(idm.group(1))
            return m.group(0)
        hid = base = slugify(plain(inner)) or "section"
        n = 2
        while hid in seen:
            hid = f"{base}-{n}"
            n += 1
        seen.add(hid)
        return f'<h2{attrs} id="{hid}">{inner}</h2>'

    return re.sub(r"<h2(\s[^>]*)?>(.*?)</h2>", rep, content, flags=re.S)


def toc_items(content):
    items = []
    for m in re.finditer(r'<h2[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', content, flags=re.S):
        items.append((m.group(1), plain(m.group(2))))
    return items


def crumbs(part, extra=None):
    bits = ['<a href="index.html">Home</a>', '<span aria-hidden="true">›</span>',
            f'<a href="{part["slug"]}.html">Part {part["num"]} · {esc(part["title"])}</a>']
    if extra:
        bits += ['<span aria-hidden="true">›</span>', f"<span>{esc(extra)}</span>"]
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(bits)}</nav>'


def pager(order, slug):
    i = next((k for k, c in enumerate(order) if c["slug"] == slug), None)
    if i is None:
        return ""
    out = ['<nav class="pager" aria-label="Previous and next">']
    if i > 0:
        p = order[i - 1]
        out.append(f'<a class="prev" href="{p["slug"]}.html"><small>Previous</small>{esc(label(p))}</a>')
    if i < len(order) - 1:
        n = order[i + 1]
        out.append(f'<a class="next" href="{n["slug"]}.html"><small>Next</small>{esc(label(n))}</a>')
    out.append("</nav>")
    return "".join(out)


def covered_callout(ch, by_slug):
    links = [by_slug[s] for s in ch.get("covered", []) if s in by_slug and by_slug[s]["html"]]
    if not links:
        return ""
    li = "".join(f'<li><a href="{c["slug"]}.html">{esc(c["title"])}</a></li>' for c in links)
    return f'<aside class="callout tip"><h4>Already written</h4><p>Part of this topic is covered in:</p><ul>{li}</ul></aside>'


def render_chapter(parts, ch, order, by_slug):
    part = ch["part"]
    meta = [STATE_PILL[ch["state"]]]
    if ch.get("code"):
        meta.append(f'<span class="pill plain">{esc(ch["code"])}</span>')
    if ch.get("pages"):
        meta.append(f'<span class="pill plain">~{ch["pages"]} pages planned</span>')
    if ch.get("checked") and ch["state"] == "verified":
        meta.append(f'<span class="pill plain">Checked {esc(ch["checked"])}</span>')
    head = (f'<div class="page-head">{crumbs(part)}<h1>{esc(ch["title"])}</h1>'
            f'<div class="meta-row">{"".join(meta)}</div></div>')

    if ch["html"]:
        content = add_heading_ids(ch["html"])
        toc = toc_items(content)
        toc_ol = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc)
        inline = f'<details class="toc-inline"><summary>On this page</summary><ol>{toc_ol}</ol></details>' if toc else ""
        side = f'<aside class="toc" aria-label="On this page"><h2>On this page</h2><ol>{toc_ol}</ol></aside>' if toc else "<div></div>"
        body = (f'<div class="page"><div class="page-grid"><article class="article">{head}{inline}{content}'
                f'{covered_callout(ch, by_slug)}{pager(order, ch["slug"])}{footer()}</article>{side}</div></div>')
        text = plain(content)
    else:
        if ch.get("region"):
            lede = (f'Field guide for region <strong>{esc(ch["code"])}</strong>'
                    + (f': {esc(ch["summary"])}.' if ch["summary"] else ".")
                    + " This region is planned. Each region page will follow the same layout:")
        else:
            summary = md_inline(ch["summary"]) if ch["summary"] else ""
            lede = summary or "This chapter is planned and not written yet."
        planned = ""
        if ch["items"]:
            planned = (f'<section class="planned"><h2 id="planned">What this '
                       f'{"region page" if ch.get("region") else "chapter"} will cover</h2>{nested_list(ch["items"])}</section>')
        body = (f'<div class="page"><div class="page-grid"><article class="article">{head}'
                f'<p class="lede">{lede}</p>{covered_callout(ch, by_slug)}{planned}'
                f'<p class="verified">This page is an outline from the book plan. It will be researched, written, illustrated '
                f'and fact-checked in a later batch.</p>{pager(order, ch["slug"])}{footer()}</article><div></div></div></div>')
        text = plain(ch["summary"] + " " + " ".join(t for _, t in ch["items"]))
    page_html = layout(parts, title=ch["title"], body=body, current_slug=ch["slug"], current_part=part["num"],
                       description=plain(ch["summary"]) or ch["title"],
                       body_class="red" if ch["slug"] == "red-pages" else "")
    return page_html, text


def render_part(parts, part, by_slug):
    total = len(part["chapters"])
    intro = " ".join(t for t in part["intro"] if t)
    meta = (f'<span class="pill plain">~{part["pages"]} pages planned</span>'
            f'<span class="pill plain">{part["written"]} of {total} written</span>'
            f'<span class="pill plain">{VOLUMES.get(part["num"], "")}</span>')
    out = [f'<div class="page"><article class="article" style="max-width:860px">'
           f'<div class="page-head"><nav class="crumbs"><a href="index.html">Home</a></nav>'
           f'<h1>Part {part["num"]} · {esc(part["title"])}</h1><div class="meta-row">{meta}</div></div>'
           f'<p class="lede">{esc(PART_BLURBS.get(part["num"], ""))}</p>']
    if intro:
        out.append(f"<p>{md_inline(intro)}</p>")
    last_group = object()
    ginfo = {g["title"]: g for g in part.get("groups_info", [])}
    open_list = False
    for ch in part["chapters"]:
        g = ch["group"]["title"] if ch.get("group") else None
        if g != last_group:
            if open_list:
                out.append("</ul>")
            if g:
                code = ch["group"].get("code") or ""
                gpages = ch["group"].get("pages")
                out.append(f'<h2 class="group-h">{esc(code + ". " if code else "")}{esc(g)}'
                           f'{f" <small style=\"font-size:.9rem;color:var(--muted)\">~{gpages} pp</small>" if gpages else ""}</h2>')
                gi = ginfo.get(g)
                if gi and gi.get("intro"):
                    out.append(f'<p>{md_inline(" ".join(gi["intro"]))}</p>')
            out.append('<ul class="ch-list">')
            open_list = True
            last_group = g
        summ = plain(md_inline(ch["summary"])) if ch["summary"] else ""
        if len(summ) > 190:
            summ = summ[:187].rsplit(" ", 1)[0] + "…"
        out.append(f'<li><a href="{ch["slug"]}.html"><span class="ct">{esc(label(ch))}</span>{SHORT_PILL[ch["state"]]}'
                   f'{f"<span class=cs>{esc(summ)}</span>" if summ else ""}</a></li>')
    if open_list:
        out.append("</ul>")
    out.append(footer() + "</article></div>")
    body = "".join(out)
    return layout(parts, title=f"Part {part['num']}: {part['title']}", body=body, current_slug=part["slug"],
                  current_part=part["num"], description=PART_BLURBS.get(part["num"], ""))


def render_home(parts, stats):
    cards = []
    for p in parts:
        total = len(p["chapters"])
        pct = round(100 * p["written"] / total) if total else 0
        red = " red" if p["num"] == 0 else ""
        cards.append(
            f'<a class="part-card{red}" href="{p["slug"]}.html"><span class="icon">{icon(p["num"])}</span>'
            f'<span class="pn">Part {p["num"]}</span><span class="pt">{esc(p["title"])}</span>'
            f'<span class="pm"><span>{p["written"]} of {total} written</span><span>~{p["pages"]} pp</span></span>'
            f'<span class="bar" aria-hidden="true"><span style="width:{max(pct, 2) if p["written"] else 0}%"></span></span></a>')
    written_list = "".join(
        f'<li><a href="{c["slug"]}.html"><span class="ct">{esc(c["title"])}</span>{SHORT_PILL[c["state"]]}'
        f'<span class="cs">Part {c["part"]["num"]} · {esc(c["part"]["title"])}</span></a></li>'
        for p in parts for c in p["chapters"] if c["state"] in ("verified", "draft") and c["slug"] not in ("red-pages",))
    body = f"""<div class="page"><article class="article" style="max-width:1060px">
<section class="hero">
  <h1>{SITE_TITLE}</h1>
  <p>Skills, plants, animals, food, medicine and the world map in one field reference, built to work without the internet once it's saved.</p>
</section>
<div class="red-banner">
  <div><strong>In an emergency?</strong><p>Bleeding, CPR, hypothermia, snakebite, poisoning, safe water and signaling for rescue.</p></div>
  <a href="red-pages.html">Open the Red Pages</a>
</div>
<div class="stats">
  <div><b>{stats["written"]}</b>chapters written &amp; fact-checked</div>
  <div><b>{stats["chapters"]}</b>chapters &amp; regions planned</div>
  <div><b>{stats["figures"]}</b>original illustrations</div>
  <div><b>{stats["sources"]}</b>sources cited</div>
</div>
<p>New here? Read <a href="how-to-use.html">How to Use This Guide</a> and the <a href="golden-rules.html">Golden Rules</a> first.</p>
<h2 id="written">Written so far</h2>
<ul class="ch-list">{written_list}</ul>
<h2 id="parts">All parts</h2>
<div class="part-grid">{"".join(cards)}</div>
{footer()}
</article></div>"""
    return layout(parts, title=SITE_TITLE, body=body,
                  description="A complete survival reference: skills, foraging, first aid, gardening, livestock and world field guides.")


# ---------------------------------------------------------------- build
def main():
    parts = assemble()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in ASSETS.iterdir():
        if f.is_file():
            shutil.copy2(f, OUT / "assets" / f.name)

    order = [c for p in parts for c in p["chapters"]]
    by_slug = {c.get("content_slug") or c["slug"]: c for c in order}
    index = []
    figures = sources = 0
    for ch in order:
        page_html, text = render_chapter(parts, ch, order, by_slug)
        (OUT / f"{ch['slug']}.html").write_text(page_html, encoding="utf-8")
        written = ch["state"] in ("verified", "guide", "draft")
        if ch["html"]:
            figures += ch["html"].count('class="illus"')
            src = re.search(r'<section class="sources".*?</section>', ch["html"], flags=re.S)
            if src:
                sources += src.group(0).count("<li")
        index.append({"t": label(ch), "u": f"{ch['slug']}.html",
                      "p": f"Part {ch['part']['num']} · {ch['part']['title']}",
                      "x": text[:12000] if written else text[:600], "w": 1 if written else 0})
    for p in parts:
        (OUT / f"{p['slug']}.html").write_text(render_part(parts, p, by_slug), encoding="utf-8")
        index.append({"t": f"Part {p['num']}: {p['title']}", "u": f"{p['slug']}.html", "p": "Part overview",
                      "x": PART_BLURBS.get(p["num"], ""), "w": 0})
    stats = {"written": sum(p["written"] for p in parts), "chapters": len(order),
             "figures": figures, "sources": sources}
    (OUT / "index.html").write_text(render_home(parts, stats), encoding="utf-8")
    nf_body = ('<div class="page-head"><h1>Page not found</h1>'
               '<p class="lede">That page isn\'t here. It may not be written yet, or the link is wrong.</p></div>'
               '<p><a href="index.html">Go to the home page</a> or use the search box above.</p>')
    (OUT / "404.html").write_text(layout(parts, title="Page not found", body=nf_body)
                                   .replace("<head>", '<head>\n<base href="/">', 1), encoding="utf-8")
    (OUT / "assets" / "search-index.js").write_text(
        "window.SEARCH_INDEX=" + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    files = list(OUT.rglob("*"))
    print(f"Built {sum(1 for f in files if f.suffix == '.html')} pages, {len(order)} chapters, "
          f"{stats['written']} written, {figures} figures, {sources} sources → {OUT}")
    print(f"Total files: {sum(1 for f in files if f.is_file())}")


if __name__ == "__main__":
    main()
