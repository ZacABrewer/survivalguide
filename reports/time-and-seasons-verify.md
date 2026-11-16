# Verify report: time-and-seasons (Part 9, Time & Seasons)

Searches used: 4 of 4. I also opened 11 pages with WebFetch. One was refused (Sky & Telescope harvest moon) and I skipped it.

## Recomputed with the NOAA GML solar equations (Python)
- Day-length table (2026 dates, zenith 90.833°): every cell matches to within 1 minute. The equator on Mar 20 rounds to 12:06 or 12:07, so I left it. At 66°N the sun stays up on June 21, which is correct because 66° > 65.7°.
- Twilight durations: all match (21/45/69, 27/59/91, 33/75/123, 45/110/never, 107/never/never).
- Sunset descent (min per degree, 4/(cosφ cosδ sinH)): fixed equator solstice 4.3 to **4.4** and 50° equinox 6.3 to **6.2**. The other cells match. The "twice"/"three times" ratios hold.
- Equation of time: about -14.3 min (mid-Feb) and +16.4 min (early Nov). Zero crossings around Apr 15, Jun 14, Sep 1, Dec 25. The solar-noon worked example (11:53 / 12:23) is correct.
- Moon: 12 × 29.53 = 354.4 days, so the calendar drifts about 11 days a year. Correct.
- Big Dipper clock checked against sidereal time (pointer stars RA about 11.06h). At midnight on Mar 6 the hand is straight up. 10 p.m. puts it 30° right of up. The hand turns counterclockwise, the correction is 2 h per month, and the Dec 6 example (hand at the right, midnight) is correct. In Fig 2, Dubhe is closer to Polaris than Merak, which is correct.

## Changes made
1. Hand method, step 3: "bottom of your top finger" changed to "top edge of your top finger" (it was a geometry error).
2. Added an honest finger-width caveat. Three fingers cover about 5° (timeanddate, secondary). With the computed descent rates, a finger is about 7 min at the equator and about 9 min at 40° near an equinox. It reaches 15+ min only near 50° in summer or toward the poles. **The 15-min rule overestimates the daylight left at most latitudes.** This is the dangerous direction, so the text now says to plan on less. The Fig 1 caption was updated to match.
3. The two sunset-descent table values (above).
4. "At Greenwich, clock noon…" changed to "On the Greenwich meridian, solar noon falls at 12:00 GMT…". This avoids the BST ambiguity.
5. Moonrise delay range added: about 20–25 min near the September full moon to about 70 min near the March full moon at mid-northern latitudes, and less farther north. Sources: Astronomy magazine and Old Farmer's Almanac, flagged as secondary.
6. Spring/neap: removed the unverified line that the biggest tides come "a day or two after" the phase. Replaced it with NOAA facts (neap about a week after spring; perigee and apogee effect) and the advice "check the table rather than the calendar".
7. Diurnal tide row now reads "one high and one low each lunar day (about 24 h 50 min high to high)".
8. Sneaker waves: sources differ. NOAA Ocean Today says 10–20 min of small waves and runs over 150 ft. The NWS Eureka brochure says up to 30 min and over 100 yd. Both are now given, with "plan for the worst case". Added NOAA's advice to watch the water about 15 min first, "call 911 if trapped or someone is swept in", and "do not go in after them". These come from NOAA Ocean Today and the NWS brochure.
9. Tide safety step 1: added the RNLI point that a beach that was dry at this time yesterday may be underwater today.
10. Fig 7: the First quarter and Third quarter labels were swapped. Seen from above the North Pole with the sun on the left, the moon moves counterclockwise, so first quarter is at the bottom. The caption now states the viewing direction.
11. Sources: added timeanddate (measuring the sky by hand), Astronomy magazine, Old Farmer's Almanac, NOAA spring tide fact page, NOAA tide variations tutorial and RNLI tides.

## Verified (brief)
- Twilight definitions are 0–6°, 6–12° and 12–18° (USNO/NWS).
- Synodic month is 29.5 days and sidereal month is 27.3 days.
- Lunar day is 24 h 50 min, 12 h 25 min high to high and about 6 h 12.5 min high to low (NOAA).
- Spring tides come at new and full moon and neap tides at the quarters, twice a month in every season. The "springing forth" origin is from NOAA.
- The rule of twelfths table is right (1,2,3,3,2,1), and Fig 8's sine curve and dots are drawn correctly.
- The tide cut-off guidance agrees with NPS, NWS, NOAA and RNLI. That includes avoiding cliffs and logs, facing the surf, and the headland warning.

## Figures
All 8 were rendered and inspected. Fig 5 moon phases show the lit side correctly for the Northern Hemisphere: waxing on the right, waning on the left. Fig 7 shows spring tides at new and full moon and the strip is correct. After the label swap, the quarter labels in Fig 7 are correct. Twilight bar widths are to scale (2.4 px/min). There are no label overlaps. The format check passes: no colors, script or h1, SVG ids are prefixed, and the HTML parses.

## Still uncertain / notes
- The tidal-range examples (36 ft spring at Anchorage, 5 in neap in Florida) rest only on the CCSF lesson script. I did not re-verify them. They are attributed as "one tutorial" and are not safety-critical.
- Spring-tide lag (age of the tide) is now left out rather than asserted.
- The cross-reference "Part 9 › Navigation Without Instruments" is not on the spec's names list. The writer says that chapter exists, so I left it.
- The word count is now about 3,790, a bit over the 3,500 target, because of the safety additions.

VERDICT: PASS WITH NOTES
