# Independent Fact-Check Brief (for verifier agents)

You are an independent fact-checker. You did NOT write the chapter you are checking. Lives may depend on it.

Inputs:
- The chapter: /home/claude/survival-site/content/<slug>.html
- The writer's report (with self-flagged uncertainties): /home/claude/survival-site/reports/<slug>.md
- Format rules: /home/claude/survival-site/CONTENT_SPEC.md

Do this:
1. Read the spec, the writer's report, then the whole chapter.
2. List every safety-critical or numeric claim (first-aid steps, doses, temperatures, times, distances, toxicity, edibility, identification features, phone numbers, legal/licensing statements). Verify each against authoritative sources with WebSearch/WebFetch (CDC, NIH, EPA, WHO, Red Cross, AHA, Wilderness Medical Society, NOAA/NWS, FCC, FAA, USDA, university extension, poison centers, peer-reviewed). The shell has no internet; do not use curl.
3. Resolve every uncertainty the writer flagged. Where a safety-relevant claim rests only on a weak source (blog, Wikipedia, retailer, magazine), find an authoritative source and swap the citation, or soften/remove the claim. When sources conflict, give the more conservative advice and say sources differ.
4. Fix problems directly in the chapter file with minimal, surgical edits (Edit tool). Keep the writer's structure and voice. Update the Sources list to match (only URLs you actually opened). Do not add new sections unless something critical is missing.
5. Format check: no hard-coded colors, no h1/style/script, every h2 has an id, SVG ids prefixed with the slug, only spec classes, sources section and verified paragraph present. Run a quick well-formedness check, e.g. `python3 -c "import html.parser,sys; p=html.parser.HTMLParser(); p.feed(open(sys.argv[1]).read())" FILE` and look for unclosed tags by eye where needed.
6. SVG sanity check by reading coordinates: labels inside the viewBox, text not overlapping other text, leader lines pointing at the right part, nothing obviously wrong in the drawing (e.g., a tourniquet drawn on a joint, a vent drawn in the wrong place). Fix what you can.
7. Copyright spot-check: no sentences copied from sources; quotes under 15 words.
8. Cross-references must be plain text using these names, e.g. "(see Part 2 › Fire)":
   Part 0 › Red Pages · Part 2 › Water · Part 2 › Fire · Part 2 › Shelter · Part 4 › Foraging Principles ·
   Part 4 › Deadly Look-Alikes: The Carrot Family · Part 6 › Vitamin C & Scurvy · Part 7 › Wilderness First Aid ·
   Part 9 › Signaling, Rescue & Communication · Part 9 › Maps & Compass · Part 3 › Cordage, Knots & Lashings · Part 5 › Off-Grid Cooking Methods.
   Other parts: 1 Foundations & Preparedness, 3 Making & Building, 4 Food Procurement, 5 The Kitchen, 6 Nutrition,
   7 First Aid, Health & Herbal Medicine, 8 Gardening & Livestock, 9 Navigation, Weather, Signals & Disasters, 10 Materials, 11 World Atlas.

Search budget: use **at most 10 WebSearch calls**; use WebFetch freely on authoritative pages (and links inside them). Never use third-party readers, proxies or archives to get around a blocked page. Cross-reference names and medicine rules are in sections 8–9 of the spec.

Write your report to /home/claude/survival-site/reports/<slug>-verify.md and reply with:
- changes made (each with the reason and the source),
- claims verified (brief),
- anything still uncertain,
- final line exactly one of: `VERDICT: PASS`, `VERDICT: PASS WITH NOTES`, `VERDICT: FAIL` (FAIL only if something dangerous remains that you could not fix).
