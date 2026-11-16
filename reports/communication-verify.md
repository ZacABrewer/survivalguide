# Verify report: communication (Part 9 › Communication)

## Access limits this session
- WebFetch: every fetch (ITU M.1677 PDF, FCC GMRS, FCC FRS, FCC CB) was refused with a provenance/approval error ("person may be away; do not retry"). I stopped fetching.
- WebSearch: 2 of 4 used. Results returned titles/URLs only, no text, so they could not confirm facts. No new sources added.

## Changes made
1. Fig 2: "Also: stay out of deep valleys" label overlapped the hill slope in panel B. Moved to open sky and shortened to "Avoid deep valleys" (render check).
2. Fig 4: "dash = 3" leader line stopped in empty space; extended it to touch the first O dash. Trimmed viewBox height 240 -> 180 (about 60 px of dead space removed).
3. Radio horizon text: changed "this guide's own arithmetic" to say it is a widely used line-of-sight approximation that allows for slight bending of radio waves, still noted as not an agency figure. Numbers rechecked: 1.41 x sqrt(6) = 3.5 mi (5.6 km); 1.41 x sqrt(100) = 14 mi (about 23 km). Both correct.

## Claims verified (internal checks / consistency)
- Morse table (Fig 3): decoded every SVG glyph by script and compared with the International Morse table. All 26 letters and 10 digits correct.
- Morse timing (Fig 4): unit = 16 px. Dots 1 unit, dashes 3, intra-letter gaps 1, letter gaps 3 (S->O, O->S), word gap 7 (S->E). All correct.
- Phonetic card: Alfa, Juliett, Whiskey, X-ray, and ICAO digit forms (WUN, TOO, TREE, FOW-er, FIFE, SIX, SEV-en, AIT, NIN-er, ZE-RO) match the standard ICAO spellings.
- FRS/GMRS/CB/marine/NWR facts (22 shared channels, GMRS 18+, 10-year term, family coverage, 1-25 mi, CB ch 9 = 27.065 MHz, marine ch 16, seven NWR frequencies 162.400-162.550) match signaling-rescue.html word for word in substance. Those were sourced by its writers from FCC/USCG/NWS pages. No contradictions found.
- "Over and out" is contradictory; prowords table meanings are standard. Labeled in chapter as common practice.
- ARES (ARRL) / RACES (government emergency management) description is correct in general terms and labeled introductory.
- Format: parses; tags balanced; no h1/style/script/hard-coded colors; every h2 has an id; SVG ids prefixed communication-; sources and verified paragraph present.

## Still uncertain (could not open sources this session)
- Morse gaps 1/3/7: these are the values in ITU-R M.1677-1 per my knowledge, but the ITU text could not be opened. The chapter's hedge remains. Recommend a re-check when fetch is approved; if confirmed, remove the hedge sentence and cite M.1677-1.
- Technician exam (35 questions, pass with 26, 47 CFR 97.503(a)): not added because the source could not be opened. Safe to add after a re-check.
- SAME details (6-hour max expiration, 10-second 1050 Hz tone) and NWR "more than 1,000 transmitters": from the writer's NWS fetch; not re-opened.
- Sources list unchanged; several entries were opened by the signaling-rescue writers, not by this chapter's writer or by me.

VERDICT: PASS WITH NOTES
