# Verification report: when-help-isnt-coming

Checked: /home/claude/survival-site/content/when-help-isnt-coming.html (verifier pass, November 11, 2026).
Method: I opened every cited source again with WebFetch, plus new authoritative pages. I used 3 of the 10 allowed WebSearch calls. I rendered the figures with qa_figures.py and checked the PNG sheets before and after the edits.

## Changes made (reason and source)

### 911 without your own carrier
- I rewrote the two opening paragraphs to say exactly what is verified. The FCC "911 Wireless Services" guide says carriers must transmit all 911 calls to a PSAP "regardless of whether the caller subscribes to the provider's service or not," and that this covers phones with no contract (the callback catch is kept). 47 CFR 9.10(b) (Cornell LII) defines "all wireless 911 calls" as calls made on a phone using a compliant radio protocol of the serving carrier. The duty sits with the carrier. Nothing promises that the handset will pick another network, so the chapter now says to try 911 anyway but to treat another network as a possible bonus.
- The myth callout now matches that wording: no plan and not a customer, yes; reaching another network, not guaranteed.
- The text bullet was wrong. "Text messages can go through when a call cannot" (FCC/FEMA) refers to texts to other phones, not to 911. It now says: text 911 where accepted, or text someone who can get help. I removed "delivery may be slow," which no source supports.
- Signal steps. The NPS line now matches its source: stay in the spot if a call-back is expected. The FCC/FEMA phone-off tip is reworded to "when it cannot find a usable signal."
- Figure 1, no-signal branch: it now starts with "Try 911 anyway," which follows from the FCC rule. I also made the 4-line boxes taller (66 to 72) because the text touched the borders.

### Satellite and beacons
- Apple: I added "in the countries where Apple offers it" and that messages go to a dispatcher or relay center. Timing now reads "30 seconds or more in ideal conditions, up to several minutes under trees" (Apple support 105097).
- The NOAA PLB facts were confirmed unchanged: 406 MHz only, manual activation, at least 24 h, GNSS to about 100 m, registration required and free.
- The messenger line now says "paid subscription; make sure it's active." This is not safety-critical. It still rests on the sibling chapter (REI) and was not re-sourced.

### CPR stopping guidance
- I removed the NAEMSP item. It is a slide in a certification review course ("Termination of CPR after 30 minutes," with exceptions), with no source tied to the claim. I also took it out of Sources.
- Drowning: the wording is now closer to WMS. The 25 minutes is "continuous" CPR, it is framed as "based on context and resources, it might be reasonable," and compression-only CPR is only for bystanders not trained in rescue breathing.
- Avalanche: the WMS exception is now stated: buried more than 60 min with a clear airway (possible hypothermia). I added that WMS allows withholding CPR when the arrest was clearly caused by trauma.
- Hypothermia: "continue as long as you can" is not in the AFP/WMS text, so it now reads "Cold is the main reason to keep going longer than usual." The 5-on/5-off rule is now tied to when nonstop CPR is impossible. I added "slow pulse," and changed "signs of death" to "can appear in people who can still be revived" (AFP/WMS).
- Added a lightning bullet, which is correct and important:
  - A strike stops heart and breathing at the same time, and a second arrest can occur if no one ventilates: EurekAlert/Elsevier release of the WMS lightning guideline.
  - The heart often restarts but breathing does not, and reverse triage applies because victims are often easily resuscitated: Emergency Care BC.
  - Victims carry no charge and are safe to touch, but beware the ongoing storm: NWS Lightning Myths.
- New closing sentence: "about 25 to 30 minutes ... except for cold victims." It sums up the two WMS summaries and is not a new rule.

### Hypothermia and heat stroke
- "Warm, sweet" is now "warm, high-calorie," and "shivering well" is now "can swallow safely" (AFP: "warmed, high-calorie liquid or food").
- Chemical packs now follow AFP: they cannot rewarm the core but can be used on hands and feet.
- Heat stroke, which was dangerous and contradicted the Red Pages. "Keep cooling for as long as it takes" risked overcooling, and "give fluids to anyone awake" broke the Red Pages no-drinks rule. It now says:
  - immerse for about 15 minutes or until no longer confused (Red Cross);
  - watch for changes;
  - cool again if confusion returns;
  - no drinks while heat-stroke signs are present, and small sips only once fully alert.

### Tourniquets
- The numbers are now attributed exactly:
  - TCCC Proposed Change 25-2 (J Spec Oper Med, 2026, abstract only): it "affirms a reassessment window within 2 hours for nonmedical personnel" and "limits conversion beyond 2 hours to medical personnel." It is labeled as a proposal, and the numbers are labeled as "for trained military staff, not for you."
  - Australian Army COVE: under 2 h is safe. From 2 to 6 h, conversion depends on hospital-level capability (continuous ECG, electrolytes, hyperkalaemia treatment) and is generally unsuitable in field care. Over 6 h is unwarranted.
- Added that "re-check" means look, not loosen; if it seeps, tighten or add a second tourniquet (Red Pages). Added the honest limb-loss cost: more than 6 h is a strong predictor of limb loss (COVE). The core advice is unchanged: untrained people leave it on and mark the time.
- Sips of fluid: these conflicted with the Red Pages shock rule ("no food or drink"). The text now gives the Red Pages rule first. Sips are allowed only after a day or more without help in a fully alert, non-vomiting patient, and are labeled as the guide's judgment.
- The training line was corrected. Stop the Bleed teaches applying a tourniquet, not converting one.

### Anaphylaxis
- I removed "Antihistamines are not a replacement for epinephrine." No source I opened says it: Red Cross, MedlinePlus, NHS, and AAAAI do not; ACAAI was blocked. It now says that none of the sources checked offers any substitute, not to count on allergy pills or home remedies, and that without epinephrine a person may die.
- The second-dose wording matches Red Cross: 5 to 10 minutes after the first dose, if EMS has not arrived, auto-injector or nasal spray.
- Positioning now follows NHS: lie down, legs raised; sit up slowly if breathing is hard; "do not stand or walk, even if you feel better." MedlinePlus adds: no leg raise with head, neck, back, or leg injury, and nothing by mouth if breathing is hard.

### ORS
- Recipe confirmed on WHO directly (WHO EMRO public ORS sheet): half a teaspoon of salt and six teaspoons of sugar in one liter of clean water. WHO does not say "level." The Rehydration Project does, and the text now says so.
- Intake now comes from WHO first (WHO Pocket Book of Hospital Care for Children, 2013, Plan A): 50 to 100 ml after each loose stool under age 2, 100 to 200 ml at 2 and older. After vomiting, wait 10 minutes and go on more slowly. Breastfed babies get ORS or water in addition to breast milk. The Rehydration Project's larger amounts and "at least 3 L/day for adults" are kept and attributed.
- The 24-hour fresh-batch rule, "no saltier than tears," and the salt/sugar/water error statements are confirmed (Rehydration Project). "Extra water" is softened to "a little extra water" to match "a little too diluted."
- The "Limits of ORS" callout is now sourced. WHO's severe-dehydration signs (two or more of the listed signs) are given, and the CDC cholera page notes that some severely dehydrated people need IV fluids.

### Latrines
- The old figure showed 100 ft from a well or spring and 200 ft from surface water. That was not the conservative choice: Leave No Trace's 200 ft applies to "water," and a spring is water.
- Text and Figure 7 now use 200 ft (60 m) from every water source (Leave No Trace). They state that humanitarian manuals use 15 to 30 m (SSWM citing Harvey/WEDC) and at least 30 m from surface water (WEDC Emergency Sanitation, Ch. 5). The pit bottom must be at least 1.5 m above the wet-season water table (WEDC; SSWM).
- Added the WEDC long-stay point: a shared latrine should be at most about 50 m walk from shelters, with handwashing nearby. This conflicts with Leave No Trace's 200 ft from camp (a backcountry trip rule), and both are now stated. The figure's camp arrow reads "Trips: 200 ft (60 m)."
- The two arrowheads that collided at the latrine are now separated.
- I could not open Sphere or the CDC sanitation pages, so they are not cited.

### Medicine expiration
- FDA wording made exact:
  - stability means strength, quality, and purity under labeled storage;
  - degraded drugs may have lower strength and "may yield toxic compounds";
  - SLEP covers certain federal stockpiles in environmentally controlled locations;
  - consumer storage varies, which makes general testing difficult.
- "Not home medicine cabinets" was the writer's inference. It now says what FDA says.
- Harvard Health Publishing (Shmerling): I added aspirin to the list of drugs that decayed, separated EpiPens ("held up poorly"), and kept the heart-rhythm-drug warning as Harvard's. It stays secondary and attributed.

### Management of the dead
- PAHO wording made exact:
  - bodies from natural disasters "do not cause epidemics";
  - victims did not have epidemic diseases such as cholera or typhoid when they died;
  - the public risk is small (diarrhea from fouled water, which routine disinfection prevents);
  - disinfectant or lime is not effective;
  - handlers face a small risk from TB, hepatitis B and C, HIV, and diarrheal disease, reduced by rubber gloves, boots, and handwashing.
- "PAHO says the real risk to survivors is diarrhea" overstated the source and was fixed.
- Added Ebola: WHO says contact with the body during burial spreads it, and outbreaks need "safe and dignified burial."
- The 12 to 48 h decomposition figure is now attributed to UN News reporting on the WHO/PAHO/ICRC manual (hot climates, facial recognition).
- Mass burial: PAHO's exact claim is that it is "not justified on public health grounds." The "harms families" reason was not confirmed and was reworded.
- Replaced "I could not verify grave depth." WEDC sets graves at least 1.5 m deep and says burial must not pollute ground or surface water. It gives no distance, so none is given.

### Other
- Removed first-person "I" statements and used "this guide."
- The honest-limits note now reads "this guide's judgment." Each row was checked for sense, and nothing is wrong. Rows match the CDC sepsis page, NIOSH (antivenom only), and Red Cross (epinephrine).
- Figure 3: panel titles aligned at the same height.
- The verified date is now November 11, 2026.
- Sources:
  - removed: NAEMSP;
  - added (all opened): EurekAlert WMS lightning release, Emergency Care BC lightning, NWS lightning myths, Red Cross heat stroke, MedlinePlus anaphylaxis, NHS anaphylaxis, WHO Pocket Book ch. 5 (NCBI), CDC cholera treatment, WEDC Emergency Sanitation ch. 5, WHO Ebola fact sheet.
  - The WHO EMRO title was corrected to the document's real title.

## Claims verified (brief)
- FCC: location accuracy 50 to 300 m, with forestation exclusions; give your number; say your location first. Text-to-911 available only in some areas, voice preferred, bounce-back required. FCC/FEMA: wait 10 s before redialing.
- NPS Olympic: ridge tops; a foot or two; stay put; creeks are "often the most dangerous routes." NPS Outdoor Emergency Plan: send two or more; alone, stabilize then go; move only for an imminent threat to life. American Hiking Society: leave only for water, then return. The NZ Wilderness magazine trail signs are low-stakes and kept attributed.
- CDC NIOSH snakebite do and do-not lists match. The CDC sepsis signs, sources, and treatment match.
- WHO EMRO hygiene list (boiled water, ice, washing away from water sources) matches.
- AFP/WMS: afterdrop causes, gentle handling, horizontal position, 20 to 30 min skin checks, one-minute pulse check.

## Still uncertain / notes
- No source says whether a US handset will actually use another carrier's tower. The chapter now says exactly that.
- TCCC 25-2 was read from the abstract only, and its adoption status is unknown. The COVE article has no named author or date.
- The lightning guidance rests on a publisher news release about the WMS guideline plus Emergency Care BC. The WMS lightning PDF and PubMed abstract were blocked.
- "Satellite messengers mostly need a paid subscription" still comes only from the sibling chapter's REI source.
- Harvard Health was opened at harvardhealth.org, which says it is Harvard Health Publishing. The canonical health.harvard.edu URL failed.
- Fluid sips in prolonged bleeding or shock care are marked as the guide's judgment.
- Length: about 5,400 words of body text, including captions, the table, and the notes my edits added. That is above the spec's 3,500. The writer's draft was already about 4,500. I did not cut content. An editor may want to trim the Radios, Community, or Medicines sections.
- Format: XML well-formed; no h1, style, or script; no hard-coded colors; every h2 has an id; SVG ids are prefixed; only spec classes; 7 figures; 36 sources.

VERDICT: PASS WITH NOTES
