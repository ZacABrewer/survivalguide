# Verify report: navigation-without-instruments (Part 9, Navigation Without Instruments)

Re-checked the whole file (a previous verifier's partial edits were present: watch-error table, star-plot captions, EarthSky "90 minus latitude" note). Searches used: 0 WebSearch; WebFetch only.

## Changes made
1. **Shadow-tip accuracy paragraph**: own geometry (ground-plane shadow-tip line vs true E-W, 15-min interval, lat 10-50 N/S) shows solstice errors of 20-35 degrees early/late in the day and ~17-21 degrees even 1 hour from noon in midwinter at 50 N. Changed "20 to 30" to "20 to 35" and added the high-latitude winter caveat and "within half an hour of noon is better". Sources: NPS P&VP-62 (usually within 15 degrees; practically no error at equinoxes; failures near solstices) plus own calculation.
2. **Daylight saving**: FM 21-76 text itself gives both options (true local time, or bisect to 1 o'clock); GTA 05-02-013 and TC 3-25.26 give the 1300 rule. Reworded so the two ways are not attributed as conflicting.
3. **Watch error table, 30 degrees summer**: own calculation gives about 55 degrees max (was "about 50"). Other cells match my calculation (50 N: 4.7/7.6/24.6; 40 N: 7.0/12.6/36.3; 30 N: 9.6/19.5/54.8; 20 N summer: sun passes north, 180 degrees).
4. **Southern Cross miss distance**: computed from J2000 coordinates: long axis misses the pole by 2.7 degrees, pointer perpendicular bisector by 2.9 degrees, intersection is 2.9 degrees from the pole. Changed "about 3 to 4 degrees" to "about 3 degrees". Acrux-to-pole = 4.47 Cross-lengths (5.47 from Gacrux) confirms the text's 4.5.
5. **Figure 5**: added an x marking the actual pole position (computed fit: the figure's six stars match a real projection within 0.4 px; true pole lies at (299,372), inside the circle but not at its center). Caption updated.
6. **Orion timing**: EarthSky says Orion is in the east around 9 p.m. in late November; the belt actually rises ~7:15 p.m. local mean time (computed). Reworded to "up in the east by about 9 p.m., highest around 1 to 2 a.m., low in the west by 5 to 6 a.m." (matches EarthSky and the computed culmination ~1:15 a.m.).
7. **Figure 9**: row "Stars: Polaris, Southern Cross = Good" contradicted the overview table (Southern Cross = Fair). Relabeled "Polaris (Southern Cross: fair)".

## Claims verified
- Shadow-tip: 1 m stick, 10-15 min, first mark always west "everywhere on earth", first mark on left = facing north (FM 21-76 ch. 18 p1; GTA 05-02-013). Equal-shadow method "more accurate but requires more time" (FM 21-76). Geometry of both hemispheres confirmed by calculation.
- Watch method NH/SH procedures, before-6-a.m./after-6-p.m. reversal note, 15 degrees per hour / 1 degree per 4 min clock error (geometry); FM 21-76: more accurate farther from equator; TC 3-25.26: temperate zones, check with shadow clock after an hour, errs at lower latitudes; NPS: ~70 degrees at Big Bend, worst in warm months, never use in tropics.
- Polaris: <1 degree from true north, useless above 70 N, star near north horizon serves ~30 min, check every 15 min going south (TC 3-25.26); pointer extension ~5x (computed 5.34x from Dubhe; line misses Polaris by 1.9 degrees); Cassiopeia center-star rule and confusion warning (FM 21-76); altitude ~ latitude (ESO). Big Dipper fully circumpolar only north of ~40.7 N (Alkaid dec +49.3) — text's "about 40" is right. Figure 4 star positions fit a real projection with correct chirality (mean error a few px).
- Orion: Mintaka on celestial equator, rises due east/sets due west, 12 h up (EarthSky). Figure 6 belt orientation checked at 40 N: nearly vertical with Mintaka on top at rising, ~38 degree tilt at culmination (figure ~28, acceptable schematic), nearly horizontal at setting — matches.
- Moon lit-side rule (FM 21-76). Crescent method rated poor (secondary sources only; appropriately hedged).
- Pace: 30-in pace, 100-600 m courses, factors, 120->130+ uphill (TC 3-25.26); 116/148 paces per 100 m and pebble per 100 m (GTA 05-02-013).
- Format: no hard-coded colors, no h1/style/script, all h2 have ids, all SVG ids slug-prefixed, tags balanced, sources and verified paragraph present. All 9 figures rendered and inspected; no overlaps or orientation errors remaining.

## Still uncertain
- Watch-method error table and shadow-tip solstice figures are this guide's own calculations (flagged as such in text); no source tabulates them.
- Southern Cross multiple: sources differ (4, 4.5, 5); text states this and our computation supports 4.5.
- Crescent-moon method, ranger-bead layout, satellite-dish and stump-ring clues rest on secondary sources or reasoning; all are rated poor/fair and flagged.
- Army documents are read via third-party hosts (aircav.com, armywriter.com, Internet Archive, npshistory.com).

VERDICT: PASS WITH NOTES
