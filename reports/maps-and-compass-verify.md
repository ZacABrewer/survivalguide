# Verification report: maps-and-compass (Part 9 › Maps & Compass)

Verifier: independent fact-check, November 16, 2026. Searches used: 2 of 10. File: /home/claude/survival-site/content/maps-and-compass.html

## Changes made
1. **Lower-48 declination range.** The chapter said "about 20 E (WA) to 20 W (ME)" as current fact, based only on REI. That range is outdated. The 2025 Mountaineers handout gives Olympia, WA as 15.04 E, changing 0.12 W per year. The sentence now credits REI for the older extremes, says values have shrunk in many places, gives the 2025 Olympia figure, and tells readers to look up their own value. No authoritative current figure for Maine was found, so none is stated.
2. **"East is least, west is best."** The writer said no source prints the rhyme. The NWCG Firefighter Math page (federal) does print it, and uses it the same way the chapter does: Magnetic = True − east, Magnetic = True + west, and the reverse for the other direction. The paragraph now cites NWCG, and NWCG was added to Sources.
3. **WMM.** NCEI's "World Magnetic Model 2025 Released" (Dec 17, 2024) replaces the US Harbors trade-news citation, which no text in the chapter used. Added one sentence: WMM2025 was released in December 2024. No validity years are stated because the page does not give them.
4. **Triangulation step 4.** Added: turn the whole compass, not the bezel, and point the bezel's N to map north. This prevents a 180-degree plotting error and matches REI.
5. **Take-a-bearing step 2 and Figure 6 label.** "North-south grid lines" is now "map north-south lines (meridians, or lines parallel to the map's side edge)". UTM grid lines give a grid bearing, while the declination math in the chapter is true-based. The chapter already covers grid-magnetic separately.
6. **"(This example is my own arithmetic.)"** is now neutral wording. The math was rechecked: 40 ft over 200 ft = 20%, atan 0.2 = 11.3°.
7. **Figure 6 geometry.** In steps 1 and 2 the bezel (60 px wide) hung off a 40 px plate and covered the travel arrow. I widened the plate to 60 and moved the arrow above a smaller bezel. Step 1 now shows the bezel unturned and step 2 shows it turned with N up. The long edge still passes exactly through You and Goal at a 60° bearing. In step 3 the "Reads 60°" label ran past the plate and viewBox edge, so I moved it to the left of the arrow.
8. **Figure 3 saddle.** The "high" labels were cut by the hilltop ellipses. They now sit above the ellipses, inside the outer contour.

## Claims verified
- **Declination, priority 1.**
  - NOAA: declination is positive when east and negative when west, and true = magnetic + declination. The Mountaineers give MB = TB − δ and TB = MB + δ, and their example (15 E, MB 285 → TB 300) is correct. NWCG gives the same rules.
  - Table check: map to ground, subtract east and add west. Ground to map, add east and subtract west. Both rows are correct.
  - Sierra Club grid example: 12°25' − 0°23' = 12°02', set 12°. Correct.
  - The 10° figure (about 0.5 mile off after 3 mi) is correct.
  - Figure 7: both lines measure exactly 15° (46.6/174), the arcs end on the MN lines, and the labels are on the right sides. East shows MN right of TN and west shows MN left. Correct. Figure 1's mini diagram also shows MN east of TN.
  - Denver: "just over 2.5° in 22 years" (NCEI node/473). WMM updated about every five years, with the 2019 out-of-cycle update (NCEI). Unreliable near the poles (NCEI). Olympia 15.04 E, −0.12°/yr (Mountaineers). LA about 5'/yr (Sierra Club).
- **Contours, priority 2.**
  - From the Army FM 3-25.26 text: cliff contours touch or converge, with ticks toward low ground. Depression ticks point to low ground, and depressions are usually shown only if at least one interval deep. Ridge and spur: closed end points away from high ground. Draw and valley: closed end points toward high ground or upstream. Saddle: hourglass. One contour per 100 m = 10% slope.
  - From the USC reprint of USGS: flat areas 10 ft or less, mountains 100 ft or more. Index contours every fourth or fifth line. Close spacing means steep. Colors as listed.
  - Figures 2–4 checked by coordinates: V directions, inner/outer contours and cross-section profiles are all consistent.
- **UTM/MGRS/USNG, priority 3.**
  - MapTools example "10S GJ 06832 44683" confirmed, along with its reading. Truncate, don't round (southwest corner). MGRS and USNG use the same lines.
  - Army: "read RIGHT and then UP" (quote under 15 words).
  - Figure 10 checked by coordinates: easting (186−150)/90 = 0.4 → 584 and northing (230−167)/90 = 0.7 → 387. Correct.
  - Digits and precision table is correct. Zones 10–19 and bands R–U for the lower 48 are correct.
- **Lat/long, priority 4.**
  - USGS at 38°N: 69 mi per degree, 1.15 mi per minute, 101 ft per second of latitude, and 54.6 mi per degree of longitude. All confirmed.
  - DMS ↔ DDM ↔ DD conversions recomputed and exact.
- **Scale, priority 5.**
  - USGS: 7.5-minute quad since 1947. 1:24,000 for the lower 48 and Hawaii, 1:25,000 for Alaska.
  - Recomputed: 2.64 in per mile, 1.640 in (4.17 cm) per km, 1 cm = 240 m, 6 × 40 ft = 240 ft (73 m), 100 m = 328 ft.
  - Sierra Club 1° table: 46 / 92.4 / 185 / 277 ft, matching 5,280 × tan 1°. UTM lines 1 km apart. NAD27/WGS84 datum note.
- **Aiming off and attack points, priority 6.**
  - FM 3-25.26 ch. 11: offset "about 10 degrees", and attack point "500 meters or less is most desirable".
  - Figure 9's offset measures 10.1° and the turn direction is correct (aimed left, so turn right).
  - Figure 8 bearings recomputed: 315°, 40.6° (shown as 41), and 249°. All lines pass through "You."
- **Other checks.**
  - Back azimuth rule matches the Army (add if 180 or less).
  - REI: landmarks at least 60° apart, about 100 ft per mile per degree, and orienting steps. All confirmed.

## Format
- Well-formed, with tag counts balanced.
- No hard-coded colors, style, script or h1.
- All 13 h2 have ids, and SVG ids are prefixed with the slug.
- Cross-references use the allowed names.
- The Sources and verified paragraphs are present.
- No copied sentences found, and quotes are under 15 words.

## Still uncertain
- No authoritative current (WMM2025) declination value was fetched for Maine, so the chapter gives no current east-side figure. A NOAA calculator lookup for a Maine point could add one later.
- The FM 3-25.26 chapter 10 page on GlobalSecurity was blocked (permission timeout). Contour facts were confirmed from the Internet Archive PDF text instead.
- Index contour spacing ("every fifth", or "fourth or fifth") is left hedged as the writer had it.
- land-navigation.com (secondary) is still listed. It is not relied on for any safety-critical fact.

VERDICT: PASS WITH NOTES
