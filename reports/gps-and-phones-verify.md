# Verification: Part 9, GPS & Phones (gps-and-phones)

WebSearch used: 3 of 4.

## Changes made
1. Google Maps steps: removed the unverified "look for the same entry on iPhone" line; replaced with the iPhone paths from Google's own iOS help page (place > More > Download offline map; or profile > Offline maps > Select your own map). Added manual update / auto-update note. Source: support.google.com/maps/answer/6291838 (iOS view).
2. Apple SOS table: added that the required iOS version differs by country and that iPhones bought in a few countries cannot use it. Source: Apple Support 101573.
3. Pixel SOS table: added that the feature must show as active in Settings (activation after updates/registration). Source: Google Pixel Help 15254448.
4. Power-bank math: formula restated as Wh = mAh x V / 1,000, now sourced to FAA (replaces "I did not open a source"); added "use the Wh on the label if shown". Examples recomputed: 10,000 x 3.7 / 1000 = 37 Wh; 4,000 x 3.7 / 1000 = 14.8 Wh; 37 / 14.8 = 2.5. All correct.
5. Added a Legal note callout with FAA airline limits: carry-on only; up to 100 Wh allowed; 100-160 Wh with airline approval, max two spares; over 160 Wh forbidden; airlines/other countries may be stricter. Added FAA source to the list.
6. Figure 1: moved "Satellite C" label off the dashed line; moved "You are here" below the arcs with a leader line (it overlapped an arc).

## Claims verified
- GPS.gov: smartphones ~16 ft (4.9 m) under open sky; error causes (blockage, indoor, multipath; less common jamming, solar storms); map errors often blamed on GPS.
- Apple SOS: iPhone 14+, country list matches, clear view of sky and horizon, no cell/Wi-Fi, call emergency first, free two years from activation, limited relay languages, demo mode.
- Pixel SOS: Pixel 9+ except 9a; US, Canada, Puerto Rico + 31 others ("about 30" OK); Google Messages default; clear sky; dial emergency number; replies within a few minutes; demo; cost not stated.
- FCC registry page: text-to-911 only where the PSAP is ready and has requested it. Bounce-back, no priority, imprecise location and "call if you can" verified on Missouri 911 board page (secondary; FCC consumer guide pages returned errors).
- Apple temperature ranges 32-95 F operating, -4-113 F storage, cold effects; Figure 4 is drawn to scale (checked coordinates).
- Google offline: 15-day auto-update on Wi-Fi, no transit/cycling/walking directions offline, not all countries.

## Still uncertain
- Airplane-mode GPS behavior: search found only user forums, no vendor page. Kept the "test at home" wording.
- FCC consumer text-to-911 guide (PDF and node/23971) could not be opened; bounce-back rests on a state 911 board page plus a county copy of older FCC advice.
- Cold capacity loss, solar output, GPS unit comparison remain unsourced and labeled as general guidance (unchanged).

VERDICT: PASS WITH NOTES
