# Verify report: Part 9 Natural Disasters (natural-disasters)

Searches used: 4 of 4. Several WebFetch permission requests went unanswered: ready.gov/floods, earthquakecountry.org/dropcoverholdon, and a CDC heat-symptoms page (it returned no text). None were retried.

## Changes made
1. **Tornado, caught in a car (callout).** Rewritten with the conservative wording. First choice is a sturdy building. If you can see the tornado far off, drive away at right angles to its path. As a last resort, NWS gives two options: stay buckled and get below the windows with your head covered, or lie flat in ground clearly lower than the road. SPC says to keep the seatbelt on and crouch low away from the windows. All sources agree that overpasses are deadly. Sources: weather.gov/safety/tornado-during, spc.noaa.gov/faq/tornado/car.htm. The Red Cross tornado page has no vehicle advice, so the earlier "Red Cross version" claim was removed.
2. **Flood, car in water.** Removed advice that rested only on an archived 2016 Ready.gov copy from the UNT web archive, and removed that source because archives are not allowed. The text now says to get to higher ground only if you can do it without entering moving water, and never to cross moving water. Sources: NWS summer-flood-sm, NWS OHX flooding. Depths 6 in / 12 in / 18–24 in were confirmed by both NWS pages. "More than 50% of flood deaths are vehicle-related" was confirmed by NWS and is now attributed to it.
3. **Tsunami, how long to stay.** Added: stay until officials give the all clear. Waves can keep coming for 8 hours or more, the first wave is often not the largest, and danger can last hours to days. Sources: NWS tsunami brochure, Cal OES tsunami alerts page.
4. **Triangle of life.** The wording now matches the USGS FAQ ("misguided idea", does not fit US-built structures, Red Cross names DCHO best). DCHO steps, the no-table option, and outdoor and driving actions were checked against the USGS ShakeOut 2020 page.
5. **Volcano ash.** "Dust mask" changed to a well-fitted N95, plus goggles. Children, older adults, and people with lung or heart disease should stay indoors. Drive slowly and leave extra space. Sources: USGS Volcanic Ash "Protecting against ash" page and the Alaska DPH ash fact sheet. Both added to Sources.
6. **Extreme heat** (now consistent with Part 7 › Environmental Emergencies):
   - Heat stroke now says core above about 104°F (40°C), skin may be dry *or* sweaty, and confusion in heat means heat stroke. Start cooling at once, ideally in cold water.
   - Heat exhaustion care now matches the Part 7 wording.
   - Removed the "above 95°F fans add risk" figure, which came only from a secondary university copy of a Ready.gov sheet. It now says a fan alone won't keep you safe in extreme heat.
   - Replaced the "2–3 days above 90°F" definition with CDC's definition. "More than 700 deaths/yr" was confirmed on CDC.
7. **Hurricane.** "Overexertion is a leading killer" was not supported. Changed to the NWS framing: straining can bring on a heart attack. Also confirmed against NWS hurricane-sm: nearly half of deaths happen after the storm, generators 20 ft away, food spoils in 4 h, flood insurance has a 30-day wait.
8. **Avalanche.** Prose and Figure 9 now say most slab avalanches start at 30–50°, most often 34–45°, and that slopes over about 50° shed small loose slides. Source: Avalanche.org.
9. **Figures (rendered with qa_figures.py and viewed):**
   - Fig 3: the surge arrow pointed down; it now points up. A right-edge label was clipped and has been moved and shortened.
   - Fig 5: leader lines ran through the zone labels; they were shortened and the Zone 2 label was regrouped.
   - Fig 7: the water was drawn above the "usual level" while the label said the sea drops away, and the person was drawn inside the hillside. The sea is redrawn as receded with a down arrow, the person stands on the slope, and the "go up" text no longer overlaps.
   - Fig 8: a leader went from the cracks to a label in the wrong place and crossed other text. Fixed the leaders. The floating tree base now sits on the ground. The pooled water is moved to the surface. A stray stroke was removed.
   - Fig 9: the runout text overlapped the slope line and has been moved. The angle label is now "about 40°", which matches the drawn ~40° geometry and sits next to its arc. The range bar was updated.
   - Figs 1, 2, 4 and 6 had no problems.

## Claims verified
Tornado shelter locations, mobile homes unsafe, and overpasses (NWS/SPC/Red Cross). Hurricane watch/warning timing and post-storm facts (NWS). Flood depths and vehicle deaths (NWS). DCHO and triangle of life (USGS). Tsunami natural signs and duration (NWS, Cal OES). CAL FIRE zones 0–5 / 5–30 / 30–100 ft (California only), with tree spacing, chimney clearance and the 4 in grass rule. Zone 0 rules are approved but not yet in effect. Volcano lahar, gas, ash and roof-fall guidance (USGS CVO, USGS ash). Landslide signs and the highest-floor/countertop advice (USGS). Avalanche angles (Avalanche.org). CDC heat deaths.

## Still uncertain
- The 104°F heat-stroke figure follows Part 7 and its sources. I could not open a CDC symptoms page in this pass. CDC's public pages use 103°F as a warning sign.
- Flood "stuck in car" specifics (stay in the car vs. get on the roof) could not be checked because ready.gov was blocked. The chapter now gives only the general rule.
- Extreme-heat "prepare" tips still rest partly on a secondary university copy of a Ready.gov sheet. The avalanche gear and forecast lines rest partly on REI. Both are flagged as secondary in Sources.
- Typhoon naming, blizzard and winter-car advice (Red Cross winter page) were not re-checked.

VERDICT: PASS WITH NOTES
