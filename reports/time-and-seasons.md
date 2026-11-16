# Report: Part 9, Time & Seasons

- File: /home/claude/survival-site/content/time-and-seasons.html
- Word count: about 3,550 (prose, tables and captions; excludes SVG text and the Sources list)
- Figures: 8 (hand method, Big Dipper star clock, daylight hours by latitude chart, twilight bands, moon phases with rise/set times, notched-stick calendar, spring/neap tides, tide curve with rule of twelfths). Rendered with qa_figures.py and checked by eye; fixes made for label overlaps.
- WebSearch calls used: 10 of 10.

## Process note
WebFetch refused URLs I wrote from memory (PROVENANCE_REQUIRED, user did not answer permission request). Blocked and not retried: NOAA tides05_tidal_patterns, tides02_cause, tides03_spring. I then fetched only URLs that appeared in WebSearch results. I did not use proxies or archives to get around any page. (One UNT web-archive URL that appeared in search results returned only viewer code, so nothing came from it.)

## Sources opened (31)
NOAA tides lunar day; NOAA tide frequency; NOAA Tides & Currents lesson (restles4); NOAA Tides & Currents products; USNO rise/set/twilight definitions; NWS twilight types; NOAA GML solar equations PDF; NOAA GML calculation details; NASA moon phases; NASA Space Place moon phases; Royal Museums Greenwich sundials; RMG nocturnal; NWS Eureka beach safety brochure; NPS Point Reyes beach safety brochure; NOAA Ocean Today wave safety; Penn State solar time; British Sundial Society equation of time; timeanddate equation of time (secondary); timeanddate star clock (secondary); Sky & Telescope Big Dipper clock (secondary); OffGridWeb remaining daylight (secondary); Art of Manliness hand method (secondary, article body did not give finger values); McDonald Observatory lunar phases; NC Sea Grant tides; CCSF tidal patterns script; Offshore Blue tides (secondary); Wikipedia rule of twelfths (secondary); Safe Skipper rule of twelfths (secondary); Wikipedia tide table (secondary). Also opened but not cited: UNLV moon phases page, nordling.de sunset estimation page.

## Computed by this guide (flagged as such in the chapter)
Using NOAA's published equations (declination, equation of time, hour angle, zenith 90.833°): day-length table (2026 dates Mar 20, Jun 21, Sep 23, Dec 21; spot check 40°N June 21 = 15:01, matches known values), twilight durations, minutes per degree of sun descent at sunset, the sample solar-noon times (2.3° west of zone meridian: 11:53 early Nov, 12:23 mid-Feb), the 354-day lunar-year drift arithmetic. Equation-of-time values from the equations (-14.2, +3.9, -6.6, +16.4 min) agree with the British Sundial Society figures.

## Could not verify / sources disagree / left out
- Finger width in degrees at arm's length: no source opened gives it, so the chapter does not say how many degrees a finger covers. It gives the sunset descent table and tells readers to calibrate with a watch. The 15 min per finger rule came from OffGridWeb only (the Art of Manliness article body gave no numbers). Latitude caveats (slower sinking toward the poles, faster near the equator) are from those two sources and agree with the computed table.
- Moonrise delay of about 50 minutes per day: derived from NOAA's 24 h 50 min lunar day. No opened source states the daily moonrise delay or its range. Chapter says "average only; range varies with latitude and season" and gives no range.
- High-to-low tide interval: NOAA lunar-day page says 6 h 12.5 min; the interval of 6 h 12 min is a rounding (and the fetch of tidefrequency gave it as inference). Chapter mentions both.
- Whether NOAA tide table times are in local standard or daylight time: pages opened do not say. Chapter tells readers to check the table notes. Also, the statement that predictions exclude weather is an inference from the harmonic method (NOAA products page implies it; the page says weather drives Great Lakes level changes and that actual water can differ from predictions).
- Regional tide types come from NC Sea Grant and Offshore Blue (secondary); I could not open NOAA's own tide-pattern page (blocked).
- Big Dipper clock: two secondary sources agree (about 30 min accuracy; 2 hours per month; DST add 1 hour). RMG says a wooden nocturnal reached about 15 minutes. I checked the December 6 worked example against star coordinates (it holds). Southern-hemisphere star clock left out (no verified method).
- Hour-by-hour upright-stick or tilted-stick sundial rules: not found in sources opened, so omitted; chapter says so.
- Notched-stick calendar: practical technique with no published source; labeled that way. Statement that noon shadow is longest near the winter solstice is this guide's geometry check, not from an opened source.
- Time-and-date source conflicts: sundials.co.uk gives EoT extremes as about -14 (Feb) and +16 (Nov); RMG says "about 15 minutes" in either direction. Chapter uses the more specific figures.
- Equinox day length of 12:06 to 12:21 reflects the USNO sunrise definition (upper limb plus refraction), stated in the chapter.
- Cross-reference "Part 9 › Navigation Without Instruments" is not in the spec's internal-names list, but that chapter exists in content/.

## Memory
Nothing new learned about the user in this task.
