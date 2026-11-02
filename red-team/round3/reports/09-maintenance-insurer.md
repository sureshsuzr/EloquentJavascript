# Maintenance & Insurance Data Product Specialist: red-team report

## Verdict
**As a standalone business, C is fatal. As a feature inside A/B, it survives.** Insurers don't price maintenance, because their policies exclude wear and tear and gradual damage. The PM-side job data already sits with Tapi (160k–400k properties, free quarterly maintenance index), PropertyMe and hipages, not with the founder. The insurer buyer set is fewer than ~10 firms. Enterprise sales cycles of 12–18 months and APRA vendor-risk obligations make it incompatible with a part-time start. **Biggest issue:** the data advantage runs *against* the founder. A few agencies' invoice exports can't out-benchmark a platform that sees hundreds of thousands of jobs a quarter. The one defensible C asset is **maintenance-shock → landlord-sale → lost management**, which is a retention variable. That makes C an input to A, not a business of its own.

## Verdict on the software business
- **From this lens, the business is A (rent-roll intelligence), with C as a differentiating module.** The module is a "capex & compliance liability" score per property and per roll, plus maintenance-shock as a feature in the retention model.
- **Selling C alone:**
  - *To PM agencies:* a ~$1–3 per property per month add-on competing with free benchmarks.
  - *To insurers:* a consulting-shaped, 1–3-customer, $50–250k/yr niche [estimate].
  - **Neither beats a $500k salary plus equity**, and the exit buyers (Cotality, Nearmap, Tapi, hipages) would pay acqui-hire prices.
- **Where C does create value:**
  - Pricing rolls before the **1 Mar 2027** Victorian energy standards hit landlords who own old gas-heated, uninsulated stock.
  - Helping lenders and roll buyers see which managements sit on landlords most likely to sell.
- That is A/B with a sharper risk flag, and it is a real edge: brokers price on multiples and don't model landlord capex exposure.

## Attacks on the thesis

**1. Landlord insurers don't need maintenance cost prediction. Severity: High.**
- Landlord policies cover defined events: malicious damage, loss of rent, liability, escape of liquid.
- They exclude wear and tear, gradual deterioration and lack of maintenance. AFCA has upheld insurers on "long-term tenant neglect and wear and tear" where 30 months passed with no repairs (IAG landlord case) [verified: insuranceNEWS AFCA summaries].
- Insurers already rate risk with address hazard, building attributes and rebuild cost:
  - Cotality: Cordell rebuild costs, "tracks individual building components over time" [verified: cotality.com/au].
  - Geoscape Buildings: 15M+ buildings [verified: geoscape.com.au].
  - Nearmap: AI roof condition, Betterview acquired Dec 2023 [verified: Thoma Bravo release].
- A maintenance cost forecast predicts the *excluded* cost line. What an insurer *would* value is narrower: signals that a property's maintenance hygiene predicts **covered** claims (escape of liquid from flexi-hoses, malicious damage, rent default).
  - That needs **their claims data joined to your maintenance data**: a partnership, not a product you can build first.

**2. The PM-side benchmark is already commoditised and free. Severity: High.**
- Tapi publishes a quarterly **Australian Property Maintenance Index** with state editions (NSW/VIC/QLD/WA/SA). It is built from "100,000's of real jobs" and gives trade-level cost bands, e.g. plumbing $179–398, appliances $183–789 (Q1 2025) [verified: Tapi/Elite Agent/Clark Realty summaries].
- Tapi claims 160k (PropertyMe profile) to 400k+ (Elite Agent) properties and 300+ agencies. It integrates with PropertyMe, PropertyTree, Palace and Reapit, and is backed by REACH and Second Century Ventures [verified: company/PitchBook].
- hipages has FY26 revenue of $90.6M and owns Proptech Labs (PM productivity software) and Tradiecore (tradie job management) [verified: HPG FY26 results 24 Aug 2026; product descriptions secondary].
- A founder starting from 3–5 agency exports is two orders of magnitude behind on job volume.

**3. Agencies don't bear the cost, so their willingness to pay is weak. Severity: Med–High.**
- Maintenance is the landlord's money. The agency earns coordination time, not margin; markups are a s 48A/disclosure hazard, as round 2 flagged.
- A capex forecast is a retention or "trusted adviser" feature. Agencies pay for features like that at add-on prices [estimate: $1–3/property/month, in line with PM add-on pricing].
- Sizing: Victoria has ~736k bonds at 30 Jun 2025 and >745k in May 2026 [verified: RTBA AR 2024-25; PAEC hearing May 2026]. Assume ~65–75% agency-managed, ≈480–560k managements [estimate].
  - **10% penetration at $24/yr ≈ $1.2–1.3M ARR in Victoria** [estimate]. National might be ~4x, but Tapi and PropertyMe would bundle it.

**4. The insurer market is small, concentrated, slow and in a soft cycle. Severity: High for part-time.**
- Only ~56% of landlords hold landlord-specific cover [verified: Mozo 2026].
- Specialist distribution is concentrated in a handful of firms:
  - Terri Scheer (a Vero/Suncorp subsidiary) [verified: insuranceNEWS].
  - EBM RentCover: distributes through 1,800+ property professionals and pays agents **20–35% commission plus profit share** [verified: EBM RentCover FSG].
  - Direct lines: Suncorp/AAMI/GIO, IAG/NRMA/CGU, Allianz, QBE, RACV.
- Australian property insurance pricing fell 11–20% in Q1 2026 and GWP fell for the first time in a decade [verified: Business Insurance, 2026]. A soft market cuts discretionary analytics budgets and lengthens procurement.
- Any insurer integrating a data vendor into pricing or claims must do APRA CPS 230 (operational risk/material service providers, in force 1 Jul 2025) and CPS 234 (information security) assessments [unverified in session; known APRA standards]. A one-person company won't pass those quickly.

**5. Per-property maintenance prediction is statistically weak. Book-level is easy and unremarkable. Severity: Med.**
- Annual maintenance cost per property is heavy-tailed: a few hot-water, roof or plumbing events dominate. Round 2 set the kill line at book-level error >35%.
- At book level (1,000+ properties) a simple tariff (age × type × trade frequency) will probably land within ±10–15%. Anyone with the data can match that.
- At property level, expect weak discrimination [estimate: R² ~0.1–0.25 on next-year spend from 3-year history plus attributes]. The useful output is **ranking** (top-decile exposure), not a dollar point estimate.
- That ranking is exactly what helps A (which landlords are likely to face a shock and sell). It is not what a maintenance platform or insurer would pay a premium for.

**6. The 2027 replacement wave is real, but rebates shrink the per-event delta. The big lumps are one-off and predictable from attributes, not invoices. Severity: Med (reframes, doesn't kill).**
- **Hot water:** from 1 Mar 2027 a failed gas system must be replaced with efficient electric [verified: energy.vic.gov.au / CAV guide summaries]. A heat pump costs ~$3,000–6,000 installed (typical ~$4,200) against $1,200–2,200 for like-for-like gas. After VEU (~$1,000), STCs (~$400) and the Solar Victoria rebate (up to $1,000–1,400, income/property-tested; $150k household threshold from 1 Jul 2026), the net can be ~$1,000–2,500 [verified-ish: installer and cost-guide sites, figures vary]. **The incremental cost per failure is often under $1,500.**
- **Heating:** a failed gas heater must be replaced with efficient electric; VEU gives up to $1,610 off a non-ducted gas heater to reverse-cycle swap [verified: energy.vic.gov.au summary]. Ducted gas central heating is the expensive case: no cheap like-for-like and a larger electric system [estimate: $8–20k].
- **Ceiling insulation** where none or partial, R5.0+, accredited installer, from 1 Mar 2027 (CAV and Energy Vic disagree on partial coverage). **Draught-proofing** at new lease from 1 Jul 2027. **Cooling** at new lease (dates conflict across sources) [verified: CAV/Energy Vic summaries; final text unverified, legislation.vic.gov.au and consumer.vic.gov.au blocked in session].
- Exposure is driven by **property attributes**: build era, gas connection, heating type, roof space. Invoice ML adds little; an inspection-report parser plus an attributes model does the job.
- A rent-roll broker is already marketing "electrification and minimum standards affect rent-roll value" [verified: Ross Hedditch blog]. Demand exists *inside rent-roll DD*, but the insight won't stay proprietary.

**7. Data access is harder than "export the invoices". Severity: Med.**
- In PropertyMe and Console, bills are trust-ledger creditor disbursements: supplier, amount, free-text description, property. Job and work-order detail may sit in Tapi or another tool, not the PMS.
- Categorisation needs LLM normalisation and won't match across agencies [estimate: 10–20% of lines ambiguous].
- The agency holds the data as the landlords' agent. Using it to build a commercial benchmark sold to *insurers* is a secondary purpose. It needs either de-identification under APP 6 or landlord consent. The Privacy Act small-business exemption may not cover an entity trading in personal information. Agencies will ask what insurers will learn about *their* landlords.
- Insurer claims data won't be shared with a startup before a paid pilot and security review.

## Things the brief gets wrong, misses or understates
- **"hipages + VIZ Insurance" as a home-warranty or maintenance-plan entrant is wrong.**
  - hipages bought **51% of VIZ for $1.4M (Apr 2026)**. VIZ sells trade-occupation insurance (85+ trades) to tradies, not landlord warranties [verified: Business News Australia, ASX HPG Apr 2026].
  - I found no hipages, VIZ or insurer landlord maintenance plan in market [verified: absence in search].
  - The real entrants in the maintenance-data lane are **Tapi** and **hipages' Proptech Labs/Tradiecore**.
- **CHU is a strata underwriting agency, not a landlord insurer.** CHU is Steadfast-owned and QBE-underwritten [unverified in session; prior knowledge]. Drop it from the landlord-insurer list.
- **Understated:** insurers' wear-and-tear exclusion. The insurer opportunity is claim-predictive *condition* signals, not maintenance cost.
- **Understated: s 48A meets insurance commissions.** EBM pays agents 20–35% of base premium plus profit share. An agency data product linked to insurer pricing deepens the conflict (round 2 already put insurance commissions inside s 48A risk). An insurer may see an agency-sourced risk score as a distribution play, which raises conflict questions.
- **Missed buyer: community housing providers (CHPs) and BTR asset managers.** They own the asset, bear the cost and run regulated asset-management plans; social housing maintenance runs ~$2,500/property [verified: NSW parliamentary submission, Pacific Link Housing, 2010–15]. But established asset-management software (e.g. SPM Assets, Assetic) serves them [unverified], and this sits outside the founder's rent-roll edge.
- **Banks don't price residential collateral on maintenance.** Valuers handle condition at origination. The bank angle only works as **roll-lending covenant monitoring (B)**.
- **Time-sensitive:**
  - 1 Mar 2027 (heating, hot water, insulation) and 1 Jul 2027 (draught-proofing) [verified per CAV/Energy Vic summaries].
  - VEU insulation discounts expected "late 2026 / by 1 Jan 2027".
  - The Victorian election on 28 Nov 2026 could alter timing.
  - **The window to sell "2027 compliance liability" analysis runs roughly now to mid-2028.**

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| hipages + VIZ = landlord warranty/maintenance entrant | 51% of VIZ for $1.4M, Apr 2026; tradie insurance | verified: Business News Australia; ASX HPG 30 Apr 2026 |
| hipages scale | FY26 revenue $90.6M (+9%), EBITDA margin 25.3%, 2.7M connections (−4%) | verified: HPG FY26 results 24 Aug 2026 |
| Tapi scale | 160k → 400k+ properties; 300+ agencies; quarterly maintenance index with state editions | verified (company claims via PropertyMe, Elite Agent) |
| Typical maintenance cost per rental | $2,661 house / $1,677 unit per yr (BIS Oxford 2017); 1–2% of value rules of thumb | verified secondary (Your Investment Property); stale |
| Terri Scheer average claim | ~$2,500, rising; top claims $80–90k; bond short in 59% of claims | unverified date (insuranceNEWS, undated) |
| Landlords with landlord-specific cover | 56% | verified: Mozo 2026 |
| EBM agent commission | 20–35% of base premium plus profit share; 1,800+ distributors | verified: EBM RentCover FSG |
| AU property insurance cycle | Q1 2026 pricing −11–20%; GWP down for first time in a decade | verified: Business Insurance 2026 |
| Victorian active bonds | 736,352 (30 Jun 2025); >745k (May 2026) | verified: RTBA AR 2024-25; PAEC May 2026 |
| 2027 standards | Gas HW/heater can't be replaced with gas from 1 Mar 2027; ceiling insulation R5 from 1 Mar 2027; draught-proofing at new lease from 1 Jul 2027 | verified via CAV/Energy Vic summaries; source PDFs blocked |
| Heat pump net cost | $3–6k gross; ~$1–2.5k net after VEU/STC/Solar Vic | verified-ish: installer sites (vary) |
| Reverse-cycle VEU discount | Up to $1,610 replacing non-ducted gas heater | verified: energy.vic.gov.au summary |
| Insurer data incumbents | Cotality (Cordell, building components), Geoscape (15M+ buildings), Nearmap + Betterview | verified: company sites/releases |
| Nearmap ACV | ~$150M group ACV (pre-privatisation); insurance not broken out | verified (older ASX); AU insurance ACV unknown |
| ATO repairs & maintenance deductions | ~$2.84B FY2019-20 (secondary) | unverified (blog citing ATO); check ATO Taxation Statistics |

## Improvements (ranked by impact)
1. **Fold C into A as the "Capex & Compliance Liability" module.** For each property in a target roll:
   - Score 2027–2030 standards exposure: gas HW/heating, ceiling insulation, draught-proofing, cooling.
   - Model expected 3-year maintenance spend and *shock probability*.
   - Feed both into the retention model. Hypothesis: landlords facing a >$5k shock sell or switch at materially higher rates.
   - This is the one thing Tapi, PropertyMe and Cotality aren't positioned to price, because they don't value rolls.
2. **Sell the 2027 compliance audit to agencies as a one-off, not SaaS.** "Your book's electrification and insulation liability, by landlord, with a rebate-adjusted cost", at ~$5–15 per property one-off [estimate]. Agencies use it for landlord conversations and to spot landlords likely to sell. It is a cash-generating lead magnet for A/B in 2027 and builds the property-attribute dataset.
3. **Treat insurers as a research partner, not a customer, for 12 months.**
   - Propose a joint study with one specialist (Terri Scheer or EBM's underwriter): "Does agency maintenance responsiveness predict landlord loss ratio?"
   - They supply claims by agency/postcode; you supply de-identified maintenance-timeliness metrics.
   - If it works, the product is an **agency-quality factor** for landlord pricing or distributor selection, licensed at $100–300k/yr [estimate]. It is a later option, not the plan.
4. **Partner rather than compete on job data.** Approach Tapi for an anonymised cost-index feed for the A module. Tapi is a likely acquirer of any maintenance analytics anyway.
5. **Model at property level for ranking, at book level for dollars.** Report top-decile capture and calibration, never single-property dollar forecasts to landlords; that avoids the "advice" and "promise" risk round 1 raised.
6. **Privacy design up front:** de-identify at ingestion, contractually limit to agency-instructed purposes, and have no insurer-facing output that identifies a landlord or tenant.

## Tests & kill criteria (≤90 days, ~$15–25k)
| # | Test | Metric | Continue if | Kill if | Time |
|---|---|---|---|---|---|
| 1 | Backtest on 3 agency PropertyMe/Console bill exports (≥3,000 property-years) | (a) book-level next-yr error; (b) top-decile predicted share of next-yr spend; (c) landlord-loss rate after ≥$3k shock vs base | (a) ≤±15%; (b) ≥30%; (c) shock lift ≥1.5x | (b) <20% **and** (c) <1.2x → maintenance adds nothing to A; drop C | Weeks 1–6 |
| 2 | 2027 liability audit on the same books (attributes + inspection reports, 50-property ground truth) | % properties correctly classed exposed/not | ≥85% accuracy; ≥3 agencies say they'd pay ≥$5/property | <70% or 0 of 10 principals will pay | Weeks 3–8 |
| 3 | Agency WTP: 10 principals (mix of franchise and independent) | Paid pre-orders for the liability report | ≥3 paid at ≥$5/property | <2 paid | Weeks 4–10 |
| 4 | Insurer appetite: 4 meetings (Terri Scheer/Vero, EBM, one major direct insurer, one MGA) | Signed NDA + data-sharing term sheet, or paid study ≥$25k | ≥1 by day 90 | 0 → drop insurers from the plan for 2 years | Weeks 2–12 |
| 5 | Broker/acquirer check: show the liability module to 2 rent-roll brokers, 2 acquirers | Would it change their price or terms? | ≥2 say yes, with a number | All say "nice to have" | Weeks 6–12 |

**Overall C kill:** tests 1(c) and 5 fail together. Then maintenance is not a retention driver and not a pricing input, and C should be shelved entirely.

## Answers to the round-3 questions in my domain
1. **Who pays, how much:**
   - PM agencies: one-off compliance reports at $5–15/property, or an add-on at $1–3/property/month. That's roughly a $1–5M ARR national ceiling with heavy bundling pressure [estimate].
   - Insurers: 0–3 customers at $50–300k/yr, with 12–18-month cycles [estimate].
   - CHPs and BTR operators: real pain, few buyers, incumbent software.
   - **Not big enough alone** to beat $500k plus equity. As a module in A it raises A's win rate and price (+$2–5k per DD report [estimate]).
2. **Data:** obtainable from agencies (bill exports), but messy and only a fraction of Tapi's volume. Insurer claims only via partnership. Models beat rules of thumb at *ranking* shock risk, not at predicting dollars per property.
3. **Incumbents:**
   - Tapi: maintenance data and index.
   - hipages: tradie marketplace, Proptech Labs, VIZ.
   - Cotality, Geoscape, Nearmap: insurer property data.
   - PropertyMe: ledger owner.
   - What stops them is that none of them **values rent rolls**. That gap is the founder's moat, and it belongs to A.
4. **Wedge vs moat:** A is the wedge; C is a moat *component*. The proprietary join is maintenance shock, landlord behaviour and roll outcome, which accumulates with every DD engagement. The 2027 liability audit is a time-boxed door-opener.
5. **Part-time:** agency work and backtests are feasible part-time. Insurer enterprise sales and APRA vendor reviews are not. Also check the employer's IP clause covers no analytics/insurance overlap.
6. **Compared with rounds 1–2:** a C-led business is lower capital and lower risk than the operator route, but lower upside than A. The round-2 idea of a maintenance *risk book* (flat-fee plans) needs balance sheet and APRA/AFSL. That should stay dead until an insurer carries the risk.
7. **Smallest test:** tests 1 and 5 above, about 6–8 weeks and under $15k, show whether maintenance belongs in the retention model at all.

## Questions I'd hand to other specialists
- **Privacy/legal:** can an agency share de-identified landlord maintenance histories with a vendor that licenses derived scores to insurers (APP 6, small-business exemption, s 48A where the agency also earns EBM commission)?
- **Rent-roll M&A:** do brokers already adjust multiples for property age or gas/insulation exposure? Is there any 2026 evidence of price chips in Victorian roll sales tied to the 2027 standards?
- **Retention modeller:** in available data, do landlord sale/exit rates spike after large repair bills or compliance notices? This is the single assumption that makes C valuable.
- **Incumbent strategist:** would Tapi or PropertyMe license job-level data or an index feed to a DD vendor, and is Tapi a natural acquirer?
- **Data engineer:** what fraction of PropertyMe bill lines can be auto-classified to trade and asset (HW, heating, roof) with acceptable accuracy?
