# Verify report: fire

File: /home/claude/survival-site/content/fire.html
Checked: 2026-11-10/11. Body is now about 3,750 words (counting captions and tables, not SVG text or Sources). That is a little over the spec's 3,500. Eight figures. 34 sources.

## Changes made (reason → source)

### Writer's weak spots
1. **Rocks bursting in fire.** I took out the IFLScience mechanism and its list of risky rock types (sandstone, shale, limestone, pumice), since no authoritative source backs that list. The Army FM 21-76 warning now comes first. I added a U.S. Air Force (Malmstrom AFB) safety article for the reason: steam pressure in a water-soaked rock can crack it apart and throw pieces at people. "Wood rings" became "metal fire ring", because a ring of wood would burn. I removed IFLScience from Sources.
2. **Poison ivy, oak and sumac smoke.** Confirmed by CDC NIOSH twice: the "Poisonous Plants and Work" page and the NIOSH 2010-118 Fast Facts PDF. Both say the smoke can irritate the lungs and cause severe allergic breathing problems. NIOSH is now the main citation, with Alabama Extension kept for airway swelling and possible death.
3. **Oleander smoke.** Two more sources confirm it. The Missouri Poison Center says smoke from burning oleander can poison you. NC State Extension says not to burn it because the smoke is harmful. The text now names the AZ and MO poison centers plus NC State.
4. **Army manual citation.** I replaced the survivalmanual.github.io mirror with a PDF of FM 21-76 hosted on a San José State University faculty page. That mirror is an app adaptation, not the manual: it even mentions a "Power section". The Sources entry says plainly that the PDF is not an official Army site. The FAS copy of ATP 3-50.21 would not parse. FM 3-05.70 is limited to government distribution.
5. **Bow-drill woods and sizes.** The wood list matches across Wikipedia, Wilderness College and Lifesong. Each species appears in at least one of them. I added that the Army pairs a harder spindle with a softwood board, and that every size is a starting point, not an exact figure.
6. **CO and putting out fires.** Drown, stir, drown again, feel matches Smokey Bear, USFS and NPS. I rewrote "Feel" to match Smokey and USFS: if you feel any heat, add water, stir and check again, and don't leave until it is cool to the touch. The old test was "if you can't keep your hand there", which was too loose. In the CO section, the CDC was cited for something it does not say: its page never mentions tents. The CDC now covers only what it says (charcoal of any color gives off CO; never use a gas camp stove indoors). The California Poison Control System (UCSF) covers the no-tent rule and "fresh air, call 911". I added "chest pain" and "sleeping or drunk people can die before symptoms" from the CDC.
7. **SVGs.** All eight figures were rendered with qa_figures.py and checked visually and by coordinates.
   - Fig 3 (bow drill), as the coordinator asked: the long diagonal "notch" is gone. There is now a small V-notch in the board right under the spindle. The coal sits in the notch and the ember catch is directly beneath. The ember catch had been drawn below the ground line, and that is fixed. I added a top-view inset showing the pie-slice notch running from the board edge into the hole. The spindle was 4 px wide with a stray trapezoid; it is now a proper spindle with a rounded tip in the hole. I added a string wrap and moved the "String wraps" label next to it.
   - Fig 4 (lean-to), as the coordinator asked: the stick was at about 52° and is now 30°, matching the Army manual. Its raised end points toward the wind arrow, kindling leans against it on the windward side, and the tinder sits sheltered underneath. The odd vertical line is gone. The caption and table row now match the drawing.
   - Fig 6 (Dakota hole): the tunnel polygon drew a line that sealed the tunnel off from the pit. It is redrawn as one open passage. The tunnel label had no leader and sat far away; I added a leader and moved the label. The air arrow now ends inside the tunnel mouth.
   - Fig 8 (reflector): the lean-to shelter had its low back facing the fire. Its open side now faces the fire. The dashed "reflected heat" arrow ended at the fire; it now arcs over the fire to the shelter.

### Other fixes
- **Fire piston.** "Over 400°F (260°C)" was copied from Wikipedia, and the two numbers don't match (260°C is 500°F). I removed the number. I also cut the unsourced claim that cotton won't hold an ember.
- **Treated wood.** "Pressure-treated lumber has arsenic" overstated it. Now: older CCA lumber, used in U.S. homes before 2004, contains arsenic (NPIC). NPIC says no treated wood should ever be burned.
- **Wrong attributions.** The "Army instructor handout" is really a California Cadet Corps handout, and the text now says so. The CO-in-shelters warning is now credited to the Army manual, which does say it.
- **Gathering wood.** Added "where gathering is allowed", plus the NPS points that many parks ban collecting, you should buy wood locally, and moving firewood spreads pests.
- **Legal note.** The vague "fines and a bill" now has a source. USFS (Arapaho-Roosevelt): citation and fine, plus possible billing for suppression costs that often run to hundreds of thousands of dollars.
- **Carrying fire.** The "metal can with air holes works well" line had no source. It now reads "fireproof container such as a metal tin", and Popular Science is cited for the "hour or two" duration. I reworded the warning so it no longer contradicts carrying a coal.
- **Birch bark.** "Never strip a living trunk" became "never peel bark all the way around a living trunk (girdling)", per Practical Self Reliance. Fomes is now "shaved or ground into dust for tinder", per PopSci, replacing "help a friction ember last".
- **911.** The trigger now also covers embers landing outside the ring (Smokey).
- **Cross-reference.** Fixed to "(see Part 9 › Signaling, Rescue & Communication)".
- **Sources.** Added FM 21-76 (SJSU PDF), Malmstrom AFB, Smokey "Campfire safety", USFS Arapaho-Roosevelt, CalPoison CO, NIOSH 2010-118, Missouri Poison Center, NC State Extension. Removed the GitHub mirror and IFLScience. All are URLs I opened.

## Claims verified
- **Smokey Bear:** 15 ft from tents and plants, 10 ft cleared circle, overhead clearance 3× flame height, keep fires small, no fires in dry or windy conditions, never use flammable liquids, drown/stir/drown/feel, dirt alone not enough, call 911 if it spreads.
- **NPS:** dirt can bank coals; gray or white coals hold heat for hours; spread and stir sand or dirt in if there is no water.
- **CA State Parks:** pour slowly because steam can lift ash; buried embers can burn underground for hours; never burn pressure-treated wood; list of items not to burn.
- **LNT:** wrist-size wood you can break by hand, dead and down only, mound fire on mineral soil.
- **REI:** kindling under 1 inch around.
- **CPSC:** no fuel-burning heaters or lanterns while sleeping in tents, campers or vehicles.
- **CDC CO page:** symptom list, "flu-like", charcoal, gas camp stoves.
- **CalPoison and UConn:** fresh air, 911, and Poison Control 1-800-222-1222.
- **FM 21-76:** fire triangle and practice; 30° lean-to stick with its end into the wind; Dakota hole with a large upwind vent; green-log base on snow; carbon steel for sparks (stainless won't spark well); lens works only on bright sunny days; battery wires; fire plow; wet or porous rocks; fire wall; CO in shelters; spindle about 2 × 25 cm.
- **Technique sources:** Patriot Supply (Dakota hole about 1 ft deep and wide; uses for teepee, log cabin, star and long fires). Primal Survivor (top-down lay on wet or snowy ground; ferro rod: 45°, knife spine, pull the rod back). O&G (char cloth: 10–20 min, tiny vent hole, done when smoke stops). Outdoor Life (wet-weather tips, foot-tall cone, mound not pit). Wilderness College (board and spindle sizes, hole about 1 in from the edge, notch just short of center, lubricate the socket, softball-size tinder bundle). Practical Self Reliance and PopSci (birch bark, fatwood, cattail, chaga, Fomes).

## Still uncertain
- **Lean-to direction.** FM 21-76 says to point the end of the stick "in the direction of the wind", which can be read either way. The chapter and figure use the common reading (raised end toward the wind, kindling as a windbreak). This is low risk either way. My web-search budget ran out before I could find a second source on it.
- **Low-stakes details from hobby or commercial sources only:** fire-lay uses, chaga, the carrying-fire method, the pencil/thumb size labels, and drying gear. These are consistent across sources and not dangerous.
- **"Do not run a fire in a shelter without a large vent".** Kept as written. The Army manual warns about CO from fires in shelters but gives no vent size.
- **Length.** About 3,750 words, a bit over the spec's 3,500, mostly from the added safety attributions. Not trimmed.
- **Verified date.** Left as November 10, 2026. Checking ran across midnight into Nov 11.

VERDICT: PASS WITH NOTES
