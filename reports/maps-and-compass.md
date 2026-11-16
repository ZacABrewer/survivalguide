# Report: maps-and-compass chapter (Part 9)
File: /home/claude/survival-site/content/maps-and-compass.html
Words: about 3,700 counting captions, tables and callouts (about 3,300 of running prose); excludes SVG text and the Sources list. Slightly over the 3,500 target because of the many tables and captions. Figures: 10 inline SVGs (map margin items; hill/ridge/valley with side views; saddle/depression/cliff with side views; rule of V's; baseplate compass parts; bearing in 3 steps; east vs west declination; triangulation; aiming off; UTM grid reading). Rendered once with qa_figures.py and spot-fixed label overlaps. Figure 6 (step 2) is the most hand-built and worth another look in the final site.
Searches used: 9 of 12. Many pages opened with WebFetch.

## Sources (22 in chapter, all opened)
USGS: quadrangle FAQ; degree/minute/second distance FAQ; Topographic Map Symbols booklet (Montana State Library copy); US Topo cartographic specs (elevation/contours). Univ. of South Carolina reprint of USGS map-reading guide (secondary). NOAA NCEI: declination page; geomagnetic calculators page; World Magnetic Model news item (node/473). US Harbors report on WMM2025 (trade news, secondary). US Army FM 3-25.26 (Internet Archive copy; chapters 3, 4, 6, 10 read) and chapter 11 text on GlobalSecurity. REI x3 (compass use, declination, choosing a compass; retailer, secondary). The Mountaineers (Olympia) declination handout. Sierra Club navigation hints. Orienteering Ireland; Orienteering ACT (Australia). MapTools (lat/long, MGRS; secondary). land-navigation.com (secondary; read, used only for basics; could drop). FGDC US National Grid standard as hosted by Missouri OA.

## Could not verify / sources disagree
- USGS pages for "how to read a topo map" and map colors, and the REI topo-map page, failed to load. Contour and color facts therefore rest on the USGS symbol booklet, the USGS elevation spec, and a university reprint of USGS text.
- Index contour frequency: USGS spec says every fifth line; the USC reprint says "usually every fourth or fifth." Chapter says to check the map legend.
- "East is least, west is best": no opened source prints the rhyme. The chapter says so. Its map-to-ground row matches the Mountaineers formula (MB = TB - declination, east positive) and REI's rule (subtract declination from true bearing to get magnetic). The Mountaineers use "True to Mag, subtract East."
- Declination change rates: NCEI (Denver, about 2.5 degrees in 22 years), Mountaineers (Olympia, about 0.12 degrees west per year), Sierra Club (LA, about 5 arcminutes per year, but also "about 1 degree per 25 years" average). These are place-specific and do not agree. The 1-degree-per-25-years figure was dropped in the trimmed version.
- Declination range in the lower 48 (about 20 E to 20 W) is from REI only. The real range today may differ somewhat. Worded as "about."
- Error per mile for 1 degree: REI says about 100 ft; Sierra Club table gives 92 ft per mile (matches 5,280 x tan 1 degree). Chapter shows both.
- WMM update: NCEI page says every five years and mentions the 2019 out-of-cycle update. A 2025 model was reported by US Harbors (secondary). Valid years of the 2025 model were not confirmed, so none are stated.
- Resection method: REI draws the line along the baseplate edge through the landmark; the Army converts to a back bearing. Both give the same line. Terminology differs (triangulation vs resection).
- Compass interference list and care are from REI only. No safe distance is given anywhere, so the chapter gives none.
- 10-degree offset for aiming off and 500 m attack-point distance are from the Army manual only. Orienteering sources describe aiming off without a number.
- Non-adjustable-compass bezel setting (for example, set 345 for 15 E) was derived by me from the formula and left out of the chapter.
- Slope example (40 ft interval, 0.1 inch spacing = 20 percent, about 11 degrees) and the scale conversions (2.64 inches per mile, 1.64 inches per km) are my arithmetic from 1:24,000 and 1 in = 2,000 ft. The chapter marks the slope example as such.
- Left out for lack of verification: Naismith's rule or any walking-speed estimate, pace counts per 100 m (varies by person), GPS accuracy claims, MGRS 100 km square letter assignment details, UTM easting false origin (500,000 m), USGS "Alaska 1:63,360" scale.
- Declination diagram "usually in the lower margin": the Army manual says so for its maps; the chapter says "margin" for USGS maps and mentions the lower margin only for the contour-interval note on Army maps.
- The sample quadrangle, numbers, and bearings in figures are invented examples.

## Memory note
Nothing from memory was used.
