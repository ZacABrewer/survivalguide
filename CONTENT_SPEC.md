# Content Spec — Survival Guide Website (read fully before writing)

You are writing ONE chapter of a large survival-guide website. Your chapter is an **HTML fragment** saved to
`/home/claude/survival-site/content/<slug>.html`. A build script wraps it in the site layout, so:

- **No** `<html>`, `<head>`, `<body>`, `<style>`, `<script>`, `<link>`, or external images. No `<h1>` (the build adds the title).
- Use only the elements and classes below. Do not invent new classes.
- Do **not** hard-code any colors anywhere (no `fill="#..."`, no `style="color:..."`).

## 1. Research & verification (most important)
- Use the **WebSearch** and **WebFetch** tools to research. (The shell has no internet; do not use curl/wget.)
- Every safety-critical fact (first aid steps, doses of bleach/iodine, temperatures, times, numbers, toxicity, edibility, phone numbers) must be checked against an **authoritative source you actually opened**: CDC, NIH (ODS, NCCIH, MedlinePlus), EPA, WHO, American Red Cross, American Heart Association, Wilderness Medical Society guidelines, NOAA/NWS, FEMA/Ready.gov, USDA, NPS, US Forest Service, university extension services, poison control centers, peer-reviewed papers, the US Army survival manual (ATP 3-50.21 / FM 21-76).
- Prefer two independent sources for anything that could injure or kill if wrong.
- If sources disagree, say so plainly and give the more conservative advice.
- If you cannot verify something, **leave it out**. Never guess numbers.
- **Never invent URLs.** Only cite URLs you opened with WebFetch or that appeared in WebSearch results.
- Minimum 5 distinct sources per chapter (Red Pages: 8+).

## 2. Writing rules
- **Original wording only.** Facts are free; other people's sentences are not. Never copy sentences. If you quote at all, keep it under 15 words, in quotation marks, max one quote per source.
- Reading level: about 8th grade. Short sentences. Active voice. Talk to the reader ("you").
- Units: imperial first, metric in parentheses — e.g., "1 gallon (3.8 L)", "212°F (100°C)".
- Scientific names in `<i>` on first mention.
- Numbered steps for procedures, one action per step.
- Call out myths and common deadly mistakes.
- Recommend real training where it matters (CPR, first aid, foraging with an expert).
- Cross-references to other chapters: plain text only, e.g. "(see Part 2 › Fire)". No internal links.
- Length: 1,800–3,500 words for a normal chapter (Red Pages: concise cards, ~2,000–3,000 words total).

## 3. HTML building blocks

**Opening summary (required, first element):**
```html
<p class="lede">Two or three sentences on what this chapter covers and why it matters.</p>
```

**Sections (each h2 needs a unique id; the build makes a table of contents from h2s):**
```html
<section id="purify">
  <h2 id="purify-h">Purifying Water</h2>
  <p>…</p>
  <h3>Boiling</h3>
  <ol class="steps"><li>…</li></ol>
</section>
```
(Put the id on the `<h2>`; the section id is optional.)

**Callouts:**
```html
<aside class="callout warn"><h4>Warning</h4><p>Could injure or kill.</p></aside>
<aside class="callout donot"><h4>Do not</h4><ul><li>…</li></ul></aside>
<aside class="callout tip"><h4>Tip</h4><p>…</p></aside>
<aside class="callout myth"><h4>Myth vs. fact</h4><p><strong>Myth:</strong> … <strong>Fact:</strong> …</p></aside>
<aside class="callout law"><h4>Legal note</h4><p>…</p></aside>
```

**Tables:**
```html
<div class="table-wrap"><table>
  <thead><tr><th>…</th></tr></thead>
  <tbody><tr><td>…</td></tr></tbody>
</table></div>
```
Use `<table class="compare">` for side-by-side look-alike comparisons.

**Key facts list:**
```html
<dl class="facts"><dt>Habitat</dt><dd>…</dd><dt>Season</dt><dd>…</dd></dl>
```

**Rating badges (plants/fungi):**
```html
<span class="rate r-E" title="Edible">● E</span>
<span class="rate r-P" title="Edible only with preparation">◐ P</span>
<span class="rate r-M" title="Medicinal / caution">◇ M</span>
<span class="rate r-T" title="Toxic">▲ T</span>
<span class="rate r-D" title="Deadly">✖ D</span>
<span class="rate r-L" title="Dangerous look-alikes">⚠ L</span>
<span class="rate r-S" title="Skin hazard">☐ S</span>
<span class="rate r-X" title="Psychoactive">✱ X</span>
```

**Species card (plants/animals):**
```html
<article class="species" id="poison-hemlock">
  <header>
    <h3>Poison Hemlock <i>Conium maculatum</i></h3>
    <div class="ratings"><span class="rate r-D" title="Deadly">✖ D</span></div>
  </header>
  <dl class="facts">…</dl>
  <p>…</p>
</article>
```

**Emergency card (Red Pages only):**
```html
<section class="redcard" id="bleeding">
  <h2 id="bleeding-h">Severe Bleeding</h2>
  <p class="when"><strong>When:</strong> blood is spurting, pooling, or soaking through.</p>
  <ol class="steps">…</ol>
  <aside class="callout donot">…</aside>
</section>
```

## 4. Illustrations (original inline SVG — required)
You must draw your own illustrations as inline SVG. No photos, no external images, no copied artwork.
Target: **4–8 figures per chapter**. Simple, clear, labeled line art, like a field manual.

```html
<figure class="illus">
  <svg viewBox="0 0 640 360" role="img" aria-labelledby="water-fig1-title">
    <title id="water-fig1-title">Cross-section of a solar still</title>
    <defs>
      <marker id="water-fig1-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" class="f"/>
      </marker>
    </defs>
    <rect x="0" y="200" width="640" height="160" class="fe"/>
    <path d="M100 200 L320 300 L540 200" class="s"/>
    <line x1="400" y1="120" x2="330" y2="280" class="s2" marker-end="url(#water-fig1-arrow)"/>
    <text x="405" y="115" class="t">Plastic sheet</text>
  </svg>
  <figcaption><strong>Figure 1.</strong> What the figure shows, in one or two sentences.</figcaption>
</figure>
```

**SVG rules**
- `viewBox` width **640**; height as needed (200–480). No `width`/`height` attributes.
- **Every** shape needs one of these color classes (never hard-code colors):

| Class | Use |
|---|---|
| `s` | main outline stroke (ink), no fill |
| `s2` | thin outline / leader line, no fill |
| `sd` | danger stroke (red), no fill |
| `ss` | safe/correct stroke (green), no fill |
| `sa` | accent stroke (blue), no fill |
| `dash` | add with a stroke class for dashed lines, e.g. `class="s2 dash"` |
| `f` | solid ink fill |
| `fp` | paper fill (background-colored) |
| `fs` | soft neutral fill (light gray/tan) |
| `fe` | earth/soil fill |
| `fw` | water fill |
| `fg` | plant/green fill |
| `ff` | fire/flame fill |
| `fd` | danger fill (light red) |
| `fk` | skin/body fill |

  Combine a fill and a stroke class on one shape like `class="fg s"`.
- Text: `<text class="t">Label</text>`; add `sm` for small, `b` for bold, `c` to center (`text-anchor: middle`), e.g. `class="t sm c"`.
- All `id`s inside SVGs must start with your slug (e.g., `water-fig1-arrow`) so they are unique on the page.
- Keep labels short; minimum text size class `sm`. Make sure labels don't overlap shapes or each other.
- Plant drawings are schematic. Caption plant figures with: "Schematic drawing — confirm identification with multiple features and an expert."

## 5. Ending (required)
```html
<section class="sources" id="sources">
  <h2 id="sources-h">Sources</h2>
  <ol>
    <li><a href="https://…">Page title</a> — Publisher</li>
  </ol>
</section>
<p class="verified">Facts checked against the sources above on November 10, 2026. This guide is educational and is not a substitute for professional training or medical care.</p>
```

## 6. Report back
When finished, reply with: the file path, word count, number of figures, your source list, and **any fact you could not verify or where sources disagreed**. Also write that report to `/home/claude/survival-site/reports/<slug>.md`.

## 7. Search budget (shared by the whole team)
Web searches are capped for the whole team. Use **at most 12 WebSearch calls**. Use **WebFetch freely**: open authoritative pages directly (agency and extension sites you know, or links found inside pages you opened). Never use third-party readers, proxies, caches or archives to get around a blocked page.

## 8. Internal names for cross-references
Use these names, e.g. "(see Part 7 › Bleeding, Wounds, Burns & Infection)":
- Part 0 › Red Pages · Part 0 › When Help Isn't Coming · Part 0 › Golden Rules
- Part 2 › Water · Part 2 › Fire · Part 2 › Shelter · Part 2 › Firewood & Woodlots
- Part 3 › Cordage, Knots & Lashings · Part 3 › Hunting & Fishing Tools · Part 3 › Animal Processing & Hides · Part 3 › Blacksmithing & Metalworking
- Part 4 › Foraging Principles · Part 4 › Deadly Look-Alikes: The Carrot Family · Part 4 › Mushrooms & Fungi · Part 4 › Hunting · Part 4 › Trapping · Part 4 › Fishing
- Part 5 › Food Safety · Part 5 › Preservation · Part 5 › Off-Grid Cooking Methods
- Part 6 › Vitamin C & Scurvy
- Part 7 › Patient Assessment & Vital Signs · Part 7 › Bleeding, Wounds, Burns & Infection · Part 7 › Bones, Joints, Head & Spine · Part 7 › Environmental Emergencies · Part 7 › Bites, Stings & Poisoning · Part 7 › Illness in the Field · Part 7 › Medical Kits & Medicines · Part 7 › Emergency Childbirth & Long-Term Care · Part 7 › Evacuation & Rescue Decisions · Part 7 › Hygiene & Sanitation · Part 7 › Herbal Medicine & Health Tonics
- Part 9 › Signaling, Rescue & Communication · Part 9 › Maps & Compass · Part 9 › Navigation Without Instruments · Part 9 › GPS & Phones · Part 9 › Travel & Movement · Part 9 › Weather · Part 9 › Natural Disasters · Part 9 › Communication · Part 9 › Time & Seasons
- Part 1 › Survival Mindset & Psychology · Part 1 › Priorities · Part 1 › Kits & Gear · Part 1 › Clothing & Layering · Part 1 › Planning
- Part 7 › Shock & Circulation
- Part 13 › NA-07 Great Plains & Prairies · Part 13 › NA-08 Eastern Deciduous Forest, Appalachians, Great Lakes & Ozarks

## 9. Medicine rules
Medical chapters are written at **wilderness first responder** level, including long-term care when no hospital is available. **Never give prescription-drug doses.** For over-the-counter medicines, say "use as directed on the label" instead of giving doses. Recommend formal training (WFA/WFR) throughout.
