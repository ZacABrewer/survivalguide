# Verification report: patient-assessment

Checked: /home/claude/survival-site/content/patient-assessment.html (verifier pass, November 11, 2026)
Method: I re-opened the writer's key sources with WebFetch and added authoritative ones. Searches used: 5 of 10. Figures were rendered with qa_figures.py and checked by eye before and after the fixes.

## Changes made (reason and source)

### Writer's weak spots
- **Pediatric vital-sign table.** I re-read SF EMSA Protocol 14.1, which cites AHA PALS 2020. The old row "Infant (under 1 year) 100-190" was mislabeled. In the source, 100-190 is for 1-12 months, and newborns under 28 days are 100-205. The row now reads "Infant (1-12 months)". I added the asleep heart-rate column (90-160, 80-120, 65-100, 58-90, 58-90) because a sleeping child is normally below the awake range. Newborn values (100-205 awake, 90-160 asleep) are now in the text. The breathing rates (30-53, 22-37, 20-28, 18-25, 12-20) match. Adult 60-100 and 12-18 match MedlinePlus Vital Signs. The MedlinePlus resting table matches exactly. Both tables are kept, with a short note saying which is awake/asleep and which is resting, and that a rate outside both ranges, or one that keeps climbing, is a warning sign.
- **Infant pulse site.** Confirmed: the brachial pulse is used for infants and the carotid for children (Red Cross Scientific Advisory Council: Pediatric CPR techniques, and Pulse check accuracy). The AHA pediatric BLS page does not name a site. The WebMD citation was replaced. The infant step was reworded: move the arm a little away from the body and feel the inner upper arm between shoulder and elbow. The writer's "hand near the ear" detail came only from WebMD and was dropped.
- **Pulse-check callout.** It said "untrained rescuers often miss a pulse". AHA actually says lay rescuers cannot reliably tell whether a pulse is present or absent, so the callout now says that. Red Cross added: no pulse check for lay rescuers, and do not delay CPR for one.
- **Primary survey order (X first).** Added the American College of Surgeons ATLS 11th edition (2025), which put "x" in front of ABCDE for heavy external bleeding (facs.org). Also kept: SF EMSA (ABC by default, X-ABC for life-threatening trauma bleeding, and CAB for cardiac arrest, which is new in the text), World Extreme Medicine S-CABCDE(g), and Stop the Bleed's three actions. "A person can bleed to death faster than they can suffocate" was unsourced. It is replaced with Stop the Bleed's statement that bleeding is the top cause of preventable death after injury.
- **Spine.** I fetched the full WMS 2024 guideline PDF from SAGE. Changes:
  - The criteria are now identified as the NEXUS checks, which WMS names as a tool for trained rescuers. NC Protocol 90 also uses mechanism and is more cautious with older adults (verified). I added "Making that call takes training; if untrained or unsure, protect the spine."
  - The text now states WMS positions accurately. Rigid collars should not be used in wilderness care (strong recommendation). Backboards are only for brief or temporary moves. The goal is limiting motion, not immobilization.
  - Added the WMS stop rule for alignment: do not keep moving the head into line if that meets resistance, raises pain, or causes new or worse neurologic signs.
  - Added WMS support for self-extrication by an alert, reliable patient.
  - Airway priority over spine is now attributed to AHA (cardiac arrest) and WMS.
  - The back check in the secondary survey and in Figure 6 said "roll as one unit". WMS 2024 prefers lift-and-slide over a log roll when spine motion must be limited. The text and Figure 6 now say "keep spine in line", and the text cites the WMS preference.
- **Airway maneuvers.** Added the AHA rule: with a suspected spine injury use a jaw thrust, and if that fails, use head tilt-chin lift (AHA adult and pediatric BLS).
- **"Look, listen, and feel for no more than 10 seconds."** AHA dropped "look, listen, feel". This now reads: take no more than 10 seconds to decide whether an unresponsive patient is breathing normally, and gasping is not normal breathing (AHA adult BLS, Red Cross 10-second limit).
- **START triage.** CHEMM confirms the five parameters, the RR cutoff of 30, the 1983 Newport Beach origin, and "most commonly used in the US". I corrected the category wording to CHEMM's text: Minor "may be able to assist in own care", Immediate "within minutes (up to 60 minutes)", Expectant "palliative care and pain relief". The step-by-step branches are not in CHEMM's text, and its PDF is robots-blocked. I verified them against a peer-reviewed Cureus 2020 triage table on PMC, matching StatPearls. I added a short branch list: walk → Minor; apneic → open airway once → still apneic Expectant, breathes Immediate; RR >30 Immediate; no radial pulse or CRT >2 s Immediate; cannot follow commands Immediate; otherwise Delayed. I added the REMM note that the 1996 revision swapped radial pulse for capillary refill, with better accuracy in the cold. "Spending under a minute each" was unsourced and now reads "as fast as you can".
- **Reassessment interval (15 min stable / 5 min unstable).** Verified in the Montgomery County MD EMT ch.14 slides. It is now attributed by name ("One EMT training text (Montgomery County, Maryland)"). The existing softening about long field stays is kept.
- **General-teaching items.**
  - Skin signs are now backed by MedlinePlus Shock: pale, cool, clammy skin and a rapid, weak pulse.
  - The breathing-effort list was aligned with MedlinePlus Breathing difficulties - first aid: rapid breathing, odd chest movement, difficulty speaking, and bluish lips and nails. Retractions, nasal flaring and grunting are kept as standard teaching.
  - Covert breath counting and temperature by touch are kept as general teaching. They are correct and low-stakes.
  - SOAP is kept. It is correct and universal.
  - The SAMPLE "output" line was reworded from "many wilderness courses ask" (unverified) to plain advice.
  - "Hard to compare between two observers" (AVPU) was not on LITFL and was removed.
  - "Often one to two minutes" for the primary survey was unsourced and was removed.
- **Prescription-drug doses.** None present: I searched for mg, mcg, dose, dosage and tablet. Beta blockers are mentioned only as something that slows the pulse (AHA).

### Other fixes
- **Pupils.** Sources disagree. MedlinePlus Pupils - different sizes says the difference is usually under 0.5 mm and at most about 1 mm. RACGP says no more than 2 mm. Both are now stated. I added MedlinePlus "unequal pupils after an eye or head injury need medical help right away". "Plants" as a cause was not supported, so the text now says "eye drops and some medicines" (MedlinePlus). All About Vision (weak) was removed. In Figure 5, the label "often normal" became "may be normal for them", and the caption adds the head-injury warning.
- **Capillary refill.** MedlinePlus says to hold the hand above heart level, so the Figure 4 caption was corrected (it said "about heart level"). The myth callout now cites a peer-reviewed study: Anderson et al., Am J Emerg Med 2008, 1,000 healthy adults. A 2-second cutoff misclassified 45% of them, and refill was slower with age, in women, and in the cold. Crisis Medicine is kept only as the summary for the child room-temperature and lighting studies.
- **CDC wording.** It now matches the page: PPE whenever exposure to infectious material is possible.
- **Adult fever.** Added the MedlinePlus threshold: above 99-99.5°F (37.2-37.5°C) by mouth.
- **Sources.**
  - Removed: WebMD, All About Vision, MedlinePlus Infant CPR (supported nothing in the text).
  - Added: MedlinePlus Pupils, Shock, and Breathing difficulties - first aid; ACS ATLS 11 news; the WMS full-text PDF; AHA Adult BLS; two Red Cross guideline pages; REMM START; the Cureus/PMC triage table; Anderson 2008.
- **Verified date.** Updated to November 11, 2026.

### Figures (rendered and inspected)
- **Fig 2:** the label "Less and less responsive" sat on its arrow. The arrow was moved down 4 px.
- **Fig 3:** the neck was a single line, so the carotid dot floated. I drew a neck and put the dot on its side. The radial dot was moved to the thumb (lateral) edge of the wrist.
- **Fig 5:** the two bottom labels ran together ("...often normalEmergency..."). They are now split into two lines each, with no overlap.
- **Fig 6:** I drew a neck and moved marker 2 onto it; it had floated over the shoulder. "Roll as one unit" became "Back: last, keep spine in line", per WMS.
- **Fig 7:** added legend line swatches, so the legend no longer relies on color words alone, and a U gridline.
- **Figs 1 and 4:** OK.
- All labels are inside the viewBox. Every SVG id is prefixed `patient-assessment-`.

## Claims verified (brief)
- Scene safety steps (SF EMSA).
- Pulse technique, timing (60/30/15/10 s), and carotid cautions: sit or lie first, one side only, may cause fainting or slow heartbeat (MedlinePlus).
- AHA resting 60-100, athletes, beta blockers.
- MedlinePlus pediatric resting table, athletes 40-60.
- Adult temp 97.7-99.1°F, RR 12-18, BP 90/60-120/80 (MedlinePlus Vital Signs).
- Child fever thresholds 100.4°F rectal, 99.5°F oral, 99°F axillary (MedlinePlus Fever).
- Hypothermia below 95°F (35°C) is a medical emergency (MedlinePlus).
- CRT <2 s and the causes of slow refill (MedlinePlus).
- AVPU definitions and painful stimuli: ear pinch, pen on nail bed (LITFL).
- DCAP-BTLS, exam order, SAMPLE, OPQRST, "do not rock the pelvis", 15/5-min reassessment (Montgomery County).
- Stop the Bleed three actions.
- WEM S-CABCDE(g) order.
- NC Protocol 90 criteria.
- CHEMM START history and categories.
- Pupil prevalence "up to 1 in 5" (MedlinePlus); RACGP 20% and 2 mm.
- Cross-references use spec names. HTML parses cleanly, with no h1, style or script, no hard-coded colors, every h2 has an id, and only spec classes are used.
- Copyright: no copied sentences found, and no quotes over 15 words.

## Still uncertain
- Pediatric rate tables: SF EMSA/PALS (awake) and MedlinePlus (resting) differ. Both are shown with a note. The SF EMSA PDF text extraction was scrambled in places (the fetch tool warned of this). The rows I used were consistent and match the published AHA PALS 2020 values as I know them. The newborn breathing-rate cell was illegible, so it is not given.
- START branch logic comes from a peer-reviewed paper (Cureus 2020, PMC) rather than CHEMM, whose algorithm PDF is robots-blocked. It matches StatPearls and the CHEMM parameters.
- Retractions, nasal flaring and grunting, covert breath counting, and judging temperature by touch remain general teaching without an opened source. They are correct and low-stakes.
- Prose is about 3,740 words, not counting tables, figures and sources. That is slightly over the 3,500 guide because of the safety additions above.

VERDICT: PASS WITH NOTES
