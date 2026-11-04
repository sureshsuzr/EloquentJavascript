# Stage 1, lens 02: renewable and storage performance-risk underwriting (Track B)

4 Nov 2026. Lens: pricing and guaranteeing what renewable and storage assets deliver, including battery degradation and availability, workmanship and installer or manufacturer default, revenue floors for grid batteries, and warranty-backed finance. The structures considered are a managing general agent (MGA) with insurer capacity, a captive, a guarantee fund, or a licensed data and underwriting engine. The brief asked me to re-examine VoltCover on the new objective, which wants equity value, cash generation, a floor and a high P(positive).

Labels: **[verified: source]**, **[estimate]**, **[unverified]**. I used 18 web searches. Several primary pages, including Modo and CEC detail, are paywalled or thin, so the gaps are flagged where they matter.

## What changed since VoltCover was dropped

Round 1's pre-mortem gave VoltCover the lowest survival on the list (35%). Its reasoning was that "no mandate exists… installers won't pay voluntarily", and it kept VoltCover only as a watch item. Six facts change that picture, though they don't fully reverse it.

1. **Scale is now much larger than any round assumed.** The Cheaper Home Batteries Program (CHBP) passed **500,000 installations by 14 Aug 2026**, 13.5 months after launch. Australians installed **276,011 home batteries in H1 2026**, 52% more than in H2 2025 **[verified: Energy-Storage.news; pv magazine; CER June-quarter report: 111k approvals and 3.6 GWh in Q2 2026]**. The government added about **A$5B** and supports a further **~40 GWh by 2030** **[verified: RenewEconomy; Energy-Storage.news]**.
2. **The rebate is stepping down.** It was tiered by size from 1 May 2026, with further cuts on 1 Jan 2027 and through to 2030 **[verified: CER, Mar 2026; SolarQuotes]**. Installer margin compression and a shake-out follow, and that is when workmanship warranties become worthless.
3. **Failures and quality problems are now visible.**
   - More than 60% of inspected battery installs were "substandard" **[verified: secondary, Pulse/RenewEconomy]**.
   - The CER received 95 whistleblower tip-offs in Mar–Jun 2026 and introduced geotagged, time-stamped photo-evidence rules from 1 Mar 2026 **[verified: secondary, McKercher/CER-derived]**.
   - The CEC moved to suspend **seven Bytewatt/Neovolt battery models from 15 Sep 2026** after the IEC 62619 certificate they relied on was found invalid. Suspended products can't earn STCs, and the remediation deadline is 14 Dec 2026 **[verified: CEC delisting page; RenewEconomy]**.
   - Ampetus Energy, a Melbourne battery seller that marketed a 15-year warranty, went into liquidation **[verified: RenewEconomy; year not confirmed]**.
4. **There is still no insurance-backed warranty product in Australia** that I could find, and still no NETCC or SAA requirement for one **[unverified absence: 2 searches]**. The gap is still open, but so is the problem of who pays.
5. **The US comparable has matured.**
   - Solar Insure issues 30-year, transferable, insurance-backed warranties covering both installer and manufacturer default. Its carrier is rated A+ by AM Best, and Zurich North America backed the residential programme **[verified: Solar Insure site; The Insurer; Solar Power World 2024]**.
   - Installers enrol systems at no cost to the homeowner, so the installer pays. A commercial product up to 2 MW launched in Feb 2026 **[verified: Solar Power World]**.
   - Revenue is about US$16M **[unverified: Prospeo model estimate]**. More than 100 US installers have closed since 2023 **[company claim]**.
6. **MGAs have a live exit market.** Amwins (with KKR and Dragoneer) is buying Steadfast for A$7.7B and taking Steadfast's **underwriting-agency business**. Steadfast's agencies were growing gross written premium (GWP) at 19.1% against 9.1% for insurer-led capacity, and brokers cite **~10x historical acquisition multiples** **[verified: Pulse2/Insurance Business; FNArena]**.

**Conclusion on VoltCover:** the risk is real, large and growing, but the channel was wrong. Installers are the party least willing to pay for their own default cover. **OEMs, distributors and lenders** are the payers that need a credible 10–15-year promise, and they pay for it as a cost of sale. Ideas 1 and 2 below are built around that.

## Ideas generated (long list)

1. Insurance-backed warranty-continuity MGA (VoltCover 2.0), sold through OEMs and distributors.
2. AI install-quality audit with a rectification guarantee ("PassMark").
3. Home-battery state-of-health ledger and underwriting engine ("BatteryScore").
4. Revenue-floor or revenue-swap MGA for mid-size merchant batteries that miss out on CIS (bold).
5. Availability and degradation insurance for community and C&I batteries.
6. Orphaned-fleet run-off service, which takes over the warranty and service obligations of liquidated installers and OEMs for a fee from liquidators, OEMs or programmes.
7. Warranty-backed green loans: an insured performance warranty lowers lender loss-given-default.
8. Guaranteed-savings battery subscription for renters, ahead of Victorian rental minimum standards from 1 Mar 2027 (overlaps lens 01).
9. Solar production guarantee for C&I PPAs (kWh Analytics-style "solar revenue put").
10. A captive or mutual owned by installers for workmanship.
11. EV battery residual-value cover (round-1 VoltCover limb).
12. A degradation-indexed secondary market for used home batteries.

**Cut:**
- 5 because the market is small, and Munich Re and Hithium-style OEM reinsurance already serve large BESS.
- 7 and 6 are folded into 1 as channels.
- 8 overlaps with lens 01.
- 9 because kWh Analytics and Swiss Re are already in it and C&I is small in AU.
- 10 because installers won't capitalise it and discretionary mutual regulation is uncertain.
- 11 because the FBT phase-down shrinks the novated EV pool and residual risk is a balance-sheet bet.
- 12 because it is too early (the fleet is 1–2 years old).

## Idea 1: VoltCover 2.0, a warranty-continuity MGA sold through OEMs, distributors and lenders

| Field | Assessment |
|---|---|
| **One-liner** | An MGA issuing a **transferable, insurer-backed 10–15-year warranty** on home batteries and solar. It pays parts and labour if the **installer or the OEM's Australian entity** disappears or won't honour a claim. **Who pays:** battery OEMs and distributors, embedded in the wholesale price (~A$120–250 per system), and green lenders (Brighte, Plenti), who add it to loans to protect collateral. **Outcome priced:** the probability-weighted cost of an orphaned failure over 10–15 years. |
| **Why now (2026–28)** | Over 500k CHBP batteries installed in 13.5 months. Rebate step-downs in 2026–27 squeeze installer margins, so failures follow. Neovolt-type delistings and liquidations like Ampetus show OEM-side risk. Many new Chinese brands lack AU balance sheets and need a way to make their warranty credible against Tesla, Sigenergy, BYD and Fox. Lenders hold 7–10-year loans secured on equipment whose warranty may lapse. |
| **Why Australia / Melbourne** | Australia has the world's highest per-capita home-battery uptake, so it is the natural first market for a battery-specific product (the US is solar-led). Melbourne is an insurance and MGA hub. **Handicap:** the market is small. Expansion means NZ and later the UK, where RECC already requires insurance-backed guarantees **[verified in round 1: reonic]**. |
| **Unfair inputs** | Statistics for failure and frequency modelling; CFO skill for binder economics and the profit commission; the marketplace experience of LocalAgentFinder (a two-sided OEM-installer-consumer channel); the logistics experience of Fulfilio (claims fulfilment via a contracted service network). **Gaps:** (a) an **underwriting co-founder** with ~10 years in an MGA or specialty insurer, ideally warranty or engineering lines, and AFSL experience; (b) a carrier. Lloyd's coverholder, Zurich AU, or a specialty reinsurer fronted by a local insurer are the options. |
| **Market & model** | **[estimate]** About 250–300k batteries a year plus ~250k solar systems. At A$180 average premium and 15% penetration by year 5: ~80k policies, about **A$14M GWP**. MGA commission is 25–30% plus 5–10% profit commission, giving about **A$4–5M revenue** and **A$1.5–2.5M EBITDA**. The installed base adds an opportunity in back-book cover for the 500k+ already installed. Comparables: Solar Insure in the US (~US$16M revenue **[unverified]**) and Amwins/Steadfast agency multiples of about 10x **[verified]**. |
| **Capital & structure** | Equity of about A$1.5–2.5M seed: founder A$0.4–0.6M, plus angels or a strategic investor such as an OEM or insurer. A$4–6M Series A in year 2–3. No balance-sheet risk, because the carrier holds the reserves. An AFSL (or authorised-representative status under the carrier) is needed. Founder ownership is ~45% at year 3 and ~35% at exit. |
| **Floor and failure mode** | **Failure:** the carrier won't write it, or OEMs won't pay more than token amounts. **Floor:** the claims and installer-quality data and the distribution contracts. The book is saleable to another MGA or a broker, and run-off income continues for the life of written policies. Capital lost is limited to ~A$0.5M personal. **P(business total loss) ~35%.** |
| **Outcome distribution (10 yrs)** | Founder value = salary taken plus equity at year 10. Failure assumes a return to employment around year 3. **Total loss 38%:** ~A$1.9M. **Modest 32%:** A$12M GWP and a small agency sold for ~A$6M, giving ~A$3.6M. **Good 24%:** A$25M GWP, A$3M EBITDA, ~A$30M value, giving ~A$11M. **Great 6%:** product mandated, plus NZ, UK and commercial, ~A$100M, giving ~A$32M. **EV ≈ A$6.4M; median ≈ A$3.2M; P(positive) ≈ 45%.** |
| **Cash generation** | Commission income starts in month 9–15 once a binder is live. The business is cash-positive at about A$8–10M GWP (year 3). MGAs are capital-light and fund growth from commission. The profit commission arrives with a lag. |
| **AI leverage** | Connected batteries (CHBP requires "VPP-capable" batteries) emit telemetry, so claims can be **predicted and triaged remotely** and installer quality can be scored from install photos (CER photo rules). Each model generation improves loss ratio and claims cost. That is the moat over a generic warranty carrier. |
| **Job satisfaction** | Building a pricing model, negotiating with carriers and OEMs (including Chinese manufacturers), designing claims operations. High intellectual content, with regulatory and sales grind. |
| **Key risks** | (1) **No capacity:** carriers see a small, data-poor new line. (2) **Adverse selection:** the weak OEMs and installers buy it, and an OEM default is a correlated loss. Cap per-OEM exposure and price at the brand level. (3) **Low willingness to pay:** a manufacturer's warranty is already "free". |
| **90-day test** | Can start while employed, with employer consent. (a) Meet **5 carriers or reinsurers** (Zurich AU, Lloyd's coverholders via a broker, Munich Re, Swiss Re, Hannover Re). **Continue** if ≥1 gives an indicative term sheet or capacity appetite in writing. (b) Meet **10 OEMs and distributors and 2 lenders.** **Continue** if ≥3 sign an LOI at ≥A$100 per system. **Kill** if no carrier engages, or fewer than 2 OEM LOIs. Cost ~A$15–25k, mostly actuarial and legal. |

## Idea 2: PassMark, an AI install-quality audit with a rectification guarantee (the data wedge)

| Field | Assessment |
|---|---|
| **One-liner** | An AI service that checks **every** solar and battery install from the photos, telemetry and the paperwork the CER now requires. It certifies the install as compliant and **guarantees to pay rectification costs** if a later CER, DNSP or state inspection finds a non-fraud defect PassMark missed. **Who pays:** retailers, STC registered agents and OEMs, per job (~A$60–120), and later home insurers and state programmes. **Outcome priced:** "your install passes inspection". The fee is only charged on a pass. |
| **Why now (2026–28)** | More than 60% of inspected installs were substandard. Geotagged photo rules started 1 Mar 2026. The CER is suspending installers and companies (21 companies under fit-and-proper rules; installer bans in Jul 2026 **[verified: CER news]**). STC-creation enforcement has meant surrenders and reinspection programmes in earlier cases (Emerging Energy surrendered 15,878 STCs and reinspected **[verified: CER/SolarQuotes]**). Battery-fire worry is pushing home insurers to ask about installs. |
| **Why Australia / Melbourne** | STC-based upfront rebates with central photo evidence are particular to Australia, and so is the volume. Vision models and audit workflow can be run from Melbourne. |
| **Unfair inputs** | CS/AI (vision QA pipeline), statistics (sampling, false-negative rates priced into the guarantee), and logistics and ops (field reinspection network as a fallback). **Gap:** a CEC/SAA-accredited **electrical engineer or installer lead** to define defect taxonomies and run field checks. |
| **Market & model** | **[estimate]** About 500k qualifying jobs a year. At A$80 for 10% share, ~**A$4M revenue**. Gross margin ~70% (AI first pass, human review on exceptions); the guarantee reserve is 5–10% of fees. Upsells: OEM fleet audits (a Neovolt-type event triggers a brand-wide audit), state programmes, and home-insurer underwriting feeds. Revenue ceiling is ~A$8–12M without expansion; its value is mostly as **the data engine for Idea 1**. Comparables: US solar-QA firms and Solar Insure's installer vetting (no verified AU comparable). |
| **Capital & structure** | Founder-funded A$0.2–0.4M; profitable without outside equity. The guarantee is held as a self-funded reserve, capped per job, and structured as a service-level credit rather than insurance to avoid needing an insurer (legal check needed). Founder ownership 70–90%. |
| **Floor and failure mode** | **Failure:** CER inspection reduces the incentive, retailers won't pay, and the installs drop as rebates step down. **Floor:** a profitable audit service is easy to wind down, and the dataset is sellable to insurers or OEMs. **P(total loss) ~25%.** |
| **Outcome distribution (10 yrs)** | Founder runs it alongside employment for 12–18 months. **Total loss 28%:** ~A$2.8M (mostly stayed employed). **Modest 42%:** A$3–5M revenue and a ~A$8M sale, giving ~A$4.5M. **Good 24%:** becomes the underwriting arm of Idea 1 or is sold to an insurer or OEM for ~A$25M, giving ~A$9M. **Great 6%:** national CER/state-programme verification standard, giving ~A$22M. **EV ≈ A$6.2M; median ≈ A$4.2M; P(positive) ≈ 65%.** |
| **Cash generation** | Cash-positive in year 1–2 on ~5–10 anchor retailers or agents. Funds itself. |
| **AI leverage** | Strongest of the four. Defect detection from photos and telemetry gets cheaper and more accurate with each model release, and the guarantee's false-negative rate falls. Each claim is labelled training data. |
| **Job satisfaction** | Hands-on product and model building, operational QA, and an obvious public-interest story. Less "finance" than he may want, but it leads into Idea 1. |
| **Key risks** | (1) **Liability:** a missed defect that causes a fire, so the guarantee must be capped and fraud excluded. (2) **Willingness to pay** among low-margin installers; sell to agents, OEMs and insurers instead. (3) **Regulatory crowd-out** if the CER builds its own AI checks, which could instead become a contract. |
| **90-day test** | While employed, with consent. Build a vision prototype on 500 public or partner install photo sets, then pilot with 3 retailers or registered agents. **Continue** if ≥85% agreement with a human auditor on critical defects and ≥2 paying pilots at ≥A$50 a job. **Kill** if <70% agreement or zero paid pilots. Cost ~A$20k. |

## Idea 3: BatteryScore, a state-of-health ledger and underwriting engine for the home-battery fleet

| Field | Assessment |
|---|---|
| **One-liner** | An independent **battery state-of-health and performance rating** for each home battery, built from inverter and VPP telemetry. It is licensed to insurers (warranty and home), green lenders, VPP operators, OEMs (warranty reserving) and property transactions, with a "battery health certificate" at sale. **Who pays:** per battery per year (~A$2–5) to institutions, and A$49–99 per certificate. **Outcome priced:** remaining capacity and failure probability. |
| **Why now (2026–28)** | About 0.5M new batteries, many from new OEMs with short track records. "**No performance oversight exists**" (Reposit CEO). "VPP-capable" is undefined and self-certified, and there are proposals for an open-access battery API **[verified: Simon Hackett, May 2026; RenewEconomy]**. Batteries are now transferring with houses. OEMs need degradation curves to reserve 10–15-year warranties (FranklinWH: 12 years or 43 MWh throughput **[verified: trade press]**). |
| **Why Australia / Melbourne** | It is the largest and densest fleet per capita and becomes the global reference dataset. |
| **Unfair inputs** | Statistics (survival and degradation modelling), CS (data pipelines), and marketplace experience (LocalAgentFinder's property-transaction channel helps the certificate product). **Gap:** a battery electrochemist or BMS engineer, and data partnerships (VPP aggregators, monitoring firms). |
| **Market & model** | **[estimate]** 10% of a 1.5M battery fleet by 2030 at A$4 is A$0.6M, plus certificates and OEM reserving contracts, giving **A$2–5M revenue** by year 5. The licensing market is thin on its own, and the data is worth more inside an underwriting business. Comparables: TWAICE and ACCURE (grid BESS analytics; TWAICE has a Munich Re partnership **[verified: pv magazine webinar]**). |
| **Capital & structure** | A$0.3–1M seed. Founder 60–80%. |
| **Floor and failure mode** | **Failure:** OEMs lock data in their clouds (Hackett's "lock-in" warning), or nobody pays for ratings. **Floor:** small, and the analytics team is acqui-hirable. **P(total loss) ~40%.** |
| **Outcome distribution (10 yrs)** | **Total loss 40%:** ~A$2.9M (low capital, mostly employed). **Modest 33%:** ~A$4.0M. **Good 21%:** ~A$9M. **Great 6%:** global fleet data layer, ~A$25M. **EV ≈ A$5.9M; median ≈ A$3.5M; P(positive) ≈ 55%.** |
| **Cash generation** | Year 2–3. Data sales are slow, with long procurement cycles at insurers and OEMs. |
| **AI leverage** | High. Foundation time-series models improve degradation forecasting from sparse telemetry. |
| **Job satisfaction** | The purest stats and data role. Commercially it is a long enterprise sale. |
| **Key risks** | (1) Access to data. (2) No standalone buyer, since the value accrues to whoever carries the risk. (3) OEMs build it in-house. |
| **90-day test** | Get **2 data partners** (a VPP operator or monitoring vendor) to share 5k anonymised battery histories, fit degradation models, and show them to 3 OEMs and 2 insurers. **Continue** if ≥1 paid contract at ≥A$50k. **Kill** if there is no data partner within 60 days. |

## Idea 4 (bold): FloorCo, a revenue-floor MGA for merchant grid batteries that miss out on CIS

| Field | Assessment |
|---|---|
| **One-liner** | A 7–10-year **revenue floor or revenue swap** for 20–200 MW batteries, priced with its own NEM dispatch and price-simulation engine, with **reinsurance or ILS capacity** (Nephila, Swiss Re, Hannover, Munich Re) bearing the risk. **Who pays:** developers and owners, through a premium or by giving up upside above a cap. The floor lifts debt sizing, so lenders effectively pay. **Outcome priced:** the battery's revenue distribution. |
| **Why now (2026–28)** | Merchant revenues collapsed to a **record low of A$44k/MW/yr in Mar 2026** (A$53k in Apr; A$49k in Sep). One year can swing by up to A$400k/MW from weather and outages **[verified: Modo]**. CIS Tender 8 drew **>70 bids totalling 76.4 GW** for **4.2 GW/16.1 GWh** awarded **[verified: Energy-Storage.news; pv magazine]**. Many bankable projects missed out on a government floor. Coal closures will raise volatility again. |
| **Why Australia / Melbourne** | The NEM is the world's most volatile energy-only market, which makes it both a natural market and a hard one. Melbourne has AEMO and the super funds that own batteries. |
| **Unfair inputs** | Statistics (stochastic price modelling and tail risk), CFO structuring, and AI (bidding simulation). **Gaps:** a former trader or quant from Akaysha, Shell Energy or Macquarie; a reinsurance structurer. Capacity relationships are the binding constraint. |
| **Market & model** | **[estimate]** BNEF expects ~18 GW of utility BESS by 2035 **[verified: Energy-Storage.news]**. If 2 GW a year is merchant and 20% of that seeks floors at A$15–25k/MW/yr premium, that is about **A$6–10M a year of new premium**, written over long tenors. The MGA fee is 10–20% plus profit share. **Incumbent:** Re2 Capital (Bermuda) already wrote Akaysha's 10-year Ulinda Park swap and a **2 GWh framework with Pacific Green** **[verified: newswire; pv magazine Aug 2025]**. ZEN Energy and the gentailers offer tolls. |
| **Capital & structure** | A$3–6M of equity to build models and credibility; capacity from reinsurers. Founder ~25–35%. |
| **Floor and failure mode** | **Failure:** no capacity provider trusts a new entrant over Re2 or gentailer tolls, or the first floors are hit in a low-spread year. **Floor:** the modelling engine is licensable to lenders and developers as advisory (Modo-like). **P(total loss) ~50%.** |
| **Outcome distribution (10 yrs)** | **Total loss 50%:** ~A$1.7M. **Modest 22%:** advisory and model-licensing business, ~A$3.5M. **Good 20%:** writes 2–3 GW of floors, ~A$15M. **Great 8%:** APAC storage-risk platform, ~A$45M. **EV ≈ A$8.2M; median ≈ A$2.5M; P(positive) ≈ 35–40%.** |
| **Cash generation** | Year 3–4 at the earliest. Lumpy, deal-driven. |
| **AI leverage** | High. Simulating bidding against a changing fleet is exactly where better models help, and the edge decays if everyone has them. |
| **Job satisfaction** | Very high intellectually: quant, deal-making, capital markets. |
| **Key risks** | (1) Capacity and the head start of Re2 and gentailers. (2) Correlated tail losses (a structural spread collapse). (3) The CIS crowds out demand in the next tenders. |
| **90-day test** | Build a NEM battery revenue-distribution model; meet 6 developers that missed CIS and 3 reinsurers or ILS funds. **Continue** if ≥2 developers will pay for a floor at a price ≥1 capacity provider will write. **Kill** otherwise. Part-time is possible, but there is employer-conflict risk if the SaaS employer is in energy. |

## Scoring summary

| Idea | EV (A$M) | Median | P(positive) | P(business total loss) | Cash-positive | Start while employed? |
|---|---|---|---|---|---|---|
| 2. PassMark (AI install QA + guarantee) | 6.2 | 4.2 | **~65%** | ~25% | Year 1–2 | Yes |
| 1. VoltCover 2.0 (warranty-continuity MGA) | 6.4 | 3.2 | ~45% | ~35% | Year 3 | Tests only |
| 3. BatteryScore (state-of-health ledger) | 5.9 | 3.5 | ~55% | ~40% | Year 2–3 | Yes |
| 4. FloorCo (merchant BESS floor MGA, bold) | 8.2 | 2.5 | ~35–40% | ~50% | Year 3–4 | Partly |

All figures are **[estimate]**. Founder value is 10-year salary taken plus equity. The staying-employed benchmark is ~A$3.0–3.5M. Base rates for "great" are held at 6–8%, consistent with the round-1 stage-2 correction.

## Top pick and ranked list

**Top pick: PassMark → VoltCover 2.0, staged.**
1. **First, build PassMark while employed.** It is cash-positive early, self-funded and AI-native, and it produces the **installer- and OEM-level quality data that no carrier has**.
2. **Then take that data to carriers to launch VoltCover 2.0**, sold through OEMs, distributors and lenders rather than installers.

The combination fixes both round-1 objections. It gives a carrier a data-backed reason to write the line, and it gives a floor (a profitable audit business) if they don't. Expected EV for the staged path is about **A$6.5–7M** and P(positive) about **55–60%** **[estimate]**. That is higher than either alone, because the step into the MGA happens only after carrier appetite is confirmed.

**Ranked:**
1. PassMark (entry and floor)
2. VoltCover 2.0 (the equity-value engine)
3. BatteryScore (fold its telemetry models into 1 and 2 rather than running it standalone)
4. FloorCo (bold, highest upside; only with a quant co-founder and a reinsurer already committed, and Re2's head start is a serious obstacle)

**Decision rule for 2027:** quit only if (a) PassMark has ≥A$40k a month of recurring revenue **and** (b) a carrier has signed a binder term sheet for VoltCover 2.0 **and** (c) ≥3 OEMs or lenders have signed distribution LOIs.

## Sources (from searches this session)
- Energy-Storage.news: CHBP 500k installations; 400k and 11.2 GWh; 276,011 in H1 2026; CIS Tender 8 (4.2 GW/16.1 GWh; 76.4 GW bid); BNEF 18 GW by 2035; Munich Re battery performance insurance.
- pv magazine Australia: CIS Tender 8 (24 Jun 2026); Pacific Green–Re2 2 GWh swap (Aug 2025); Akaysha Ulinda Park.
- Clean Energy Regulator: "Battery rebates are changing 1 May 2026"; June-quarter 2026 report; installer ineligibility notices (Jul 2026).
- Clean Energy Council: Bytewatt/Neovolt 2026 delisting page. RenewEconomy: Neovolt suspension; Ampetus liquidation; extra ~A$5B for CHBP; Reposit criticism.
- Modo Energy: NEM battery revenues for Mar, Apr and Sep 2026; weather and outage volatility.
- Re2/Akaysha newswire (Jul 2023).
- Solar Insure (site; Solar Power World 2024 and Feb 2026; The Insurer).
- Simon Hackett: battery open-access API proposal (May 2026).
- Pulse2 and Insurance Business: KKR, Dragoneer and Amwins acquisition of Steadfast. FNArena: 10x acquisition multiple.
- Plenti FY26 (A$3.1B book; A$239M renewable originations).
