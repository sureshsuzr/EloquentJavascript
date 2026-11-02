# Regulatory, Labour & Food-Safety Counsel: red-team report

*Date: 2 November 2026. Not legal advice. Primary-source sites (fairwork.gov.au and others) were blocked in this session, so "verified" figures rest on official pages and law-firm summaries seen through search results. Check the instruments themselves before acting.*

## Verdict

**Survives, provided the platform is a disclosed agent that doesn't employ anyone in the delivery chain.** No law prohibits a multi-merchant grocery marketplace in Australia. What the law changes is the economics and the structure. The biggest issue is labour. Since 17 August 2026 the FWC's *Interim On-Demand Delivery Employee-like Worker Minimum Standards Order* has applied to app-engaged delivery of supermarket groceries. It sets a floor of about **$31.30 per engaged hour**, counted from when the rider accepts the job to when it is delivered. Multi-stop pickup is exactly what that clock counts. Add the "whole relationship" employment test, and an Instacart-style model (contractor shoppers picking inside merchant stores) is the highest legal risk on the table. Merchants pick, a third-party logistics provider (3PL) delivers, and the platform is a licensed-nothing agent. That structure is lawful. "Global from day 1" is not credible from a regulatory standpoint.

## Verdict on the business model

From a regulatory lens, ranked best to worst:

1. **Software only** (shelf-scan inventory, universal catalogue and data feeds sold to merchants or existing marketplaces). Lowest exposure. The live issues are privacy (faces in shelf video), IP in images, and unfair-contract terms with small merchants. No labour, food-safety, liquor or payments perimeter.
2. **Marketplace as disclosed agent.** Merchants sell, pick and hold every licence. Payments run through a PSP's connected accounts (Stripe Connect or Adyen for Platforms). Delivery is bought from 3PLs (Uber Direct, DoorDash Drive, Sherpa, Zoom2u), or later done by an employed fleet. Compliant and buildable in about 3 months for about $60–120k of legal and set-up cost **[estimate: AU counsel on structure, terms, privacy, liquor and food advice]**. The platform still owns all ACL pricing representations and the privacy duties.
3. **Marketplace as merchant of record with its own gig couriers or in-store shoppers.** This brings in liquor licensing in every state, GST classification of every SKU, possible food-business registration, MSO and employee-like obligations, unfair-deactivation claims, and sham-contracting risk. Don't start here.

## Attacks on the thesis

**1. The minimum standards order prices multi-stop aggregation per minute (High).** The interim order covers employee-like workers engaged through an app who mainly deliver food, drinks, liquor or **supermarket groceries**. The draft defined "grocery items" as anything bought from a supermarket. Pay is at least $31.30/hr ($31.50 on a motorbike or scooter, $32.00 in a car or van, per secondary sources) for "engaged time", from acceptance to completion. Stationary periods of more than 5 minutes unrelated to the delivery are excluded **[verified: FWO media release 17 Aug 2026; FWC; WorkPro and Peninsula summaries]**.

Waiting at a deli counter for an order to be bagged is related to the delivery, so it is paid. Estimated cost per order:
- Single-merchant delivery, about 25 engaged minutes: about $13.
- Three-merchant aggregated basket, about 50–60 minutes: about **$26–32 in courier floor cost alone**, before the 3PL's margin, insurance and payment costs.

**[estimate: $31.30 × engaged minutes; durations assumed]**

The order is **interim** and will be reviewed after the "last mile" cases (MS2024/1–2). The TWU filed amended proposed orders in March and May 2026, and no final order is confirmed **[verified: FWC documents list]**. If you run car or van couriers on scheduled routes, expect a second order on top. The founder's "physical arbitrage" relies on free merchant capacity, but the labour in the delivery leg is now regulated at a floor that roughly matches casual retail award rates.

**2. In-store contractor shoppers create sham-contracting and reclassification risk (High).** Since 26 August 2024, s15AA of the Fair Work Act requires employment status to be judged on the whole real relationship, not the contract **[verified: Closing Loopholes No. 2, from my existing knowledge]**. A person told by an app what to pick, when, in which store, with performance metrics and deactivation, looks like an employee. Instacart's US shopper model is the template, and copying it here invites Fair Work Ombudsman (FWO) and class-action risk. Workers who are employee-like but not employees also have unfair-deactivation rights before the FWC (from about February 2025, Digital Labour Platform Deactivation Code) **[unverified: commencement date from memory]**. Mitigation: merchant staff pick (the merchant is the employer under the General Retail Industry Award). If you ever run your own pickers or couriers, employ them (Milkrun employed its riders).

**3. Food safety: aggregation stretches the cold chain (Med–High).** Standard 3.2.2 requires potentially hazardous food in transport to be kept at ≤5 °C or ≥60 °C. The 2-hour/4-hour rule governs cumulative time out of temperature control. Standard 3.2.2A (in force 8 Dec 2023) adds a food safety supervisor, food handler training and records for category 1 and 2 businesses handling unpackaged potentially hazardous food **[verified: from existing knowledge of FSANZ standards; not re-checked this session]**.

The butchers, delis and bakeries on the target merchant list are already category 2 businesses. If your couriers or pickers handle *unpackaged* potentially hazardous food, you become a food handler too. A route that picks up meat first and then visits two more stores breaches temperature control in summer without insulated, cooled carriage.

Victoria registers mobile premises and transport vehicles through the FoodTrader portal. **Whether an aggregator that only arranges transport must register is not settled in public guidance** **[unverified; search found no ruling]**. Get a written view from the Department of Health (Food Safety Unit) before launch.

**4. Shelf-scan prices create ACL price-accuracy liability for the platform (High).** The platform is the party showing prices to consumers. A stale or misread shelf price that is lower than the merchant's till price leaves you three choices:
- Honour the displayed price yourself, which is a margin leak.
- Charge more than displayed, which risks a false or misleading price representation under ACL s29(1)(i) and s18.
- Cancel the item, which hurts customers if it is systematic.

Scan freshness becomes a legal control, not just a product metric. "In stock" claims and substitution defaults are representations too.

Random-weight goods (meat, deli, produce) must be charged on actual measured weight under National Measurement Act trade-measurement rules. You need an estimate-then-reconcile payment flow with authorisation headroom **[verified: general trade-measurement principle; existing knowledge]**.

**5. Drip pricing, service fees and marked-up item prices (Med; dated).** The *Competition and Consumer Amendment (Unfair Trading Practices) Act 2026* passed on 2 July 2026 and **commences 1 July 2027**. It requires mandatory transaction-based charges to be disclosed with the headline price. Optional charges, payment surcharges and government charges are excluded. It also creates a general prohibition on unfair trading practices and adds subscription rules **[verified: Allens, McCullough Robertson, Clayton Utz (Oct 2026)]**.

An Instacart-style "service fee" added at checkout, or a silent mark-up on merchant shelf prices, falls within the targeted conduct. Build all-in pricing from day one. Whether delivery fees are carved out depends on the final text **[unverified]**.

**6. Unit pricing (Med; dated).** The current Unit Pricing Code already binds **online retailers** that sell the minimum range of food-based grocery items, regardless of size **[verified: legislation.gov.au explanatory statement; Treasury]**. A multi-merchant basket with a full grocery range plausibly meets the test. Whether an *agent* marketplace counts as the "retailer" is unclear: the ARC submission argues obligations should follow whoever controls the display. Treasury's May 2026 consultation proposed cutting the category threshold from 11 to 4 and the floor area from 1,000 m² to 300 m² **[verified: NSA and ARC submissions May 2026; no final instrument found]**. Assume you're caught. The catalogue needs net quantity and unit of measure for every SKU. That's cheap to build in and expensive to retrofit.

**7. Age-restricted and scheduled goods: not as simple as "IGA plus bottle shop" (Med).**
- **Liquor (Vic).** The licensee must notify Liquor Control Victoria before taking off-premises requests. It must display its licence number on the ordering interface. Same-day deliveries must not be left unattended, and recipients must be 18+. First-time orders go only to the person who ordered. Failed deliveries, including refused ID checks, must be reported. Supply to minors attracts penalties above $23,000 **[verified: vic.gov.au alcohol delivery checklist, 2026]**. NSW has separate same-day delivery rules (driver training, ID, restricted hours) **[unverified detail]**. Mixed baskets work only if the bottle shop is the seller and the courier runs a scan-ID-at-door flow. A platform that takes title needs its own licence in each state.
- **Tobacco (Vic).** A licence is needed for each location since February 2026 (enforcement dates conflict between 1 Feb and 1 Jul 2026). It covers online sales, with record-keeping and, from 1 Jan 2027, no sellers under 18 **[verified: Tobacco Licensing Victoria and vic.gov.au fact sheets]**. Exclude tobacco.
- **Vapes.** Pharmacy only since 1 Oct 2024. The TGA has had 13,700+ ads and listings removed and in Oct 2025 warned delivery platforms directly **[verified: TGA notice]**. Exclude vapes entirely.
- **Pharmacy.** Pharmacy-ownership laws and S2/S3/S4 scheduling mean the platform can't sell medicines. Pharmacy-only and pharmacist-only lines need pharmacist involvement. Limit pharmacies to unscheduled lines at launch.

**8. Privacy: shelf video captures people (Med).** Phone video of shelves will capture shoppers and staff. Collecting and uploading identifiable images is a collection of personal information. The OAIC found Bunnings breached the Privacy Act with in-store facial recognition (2024) **[verified: from existing knowledge]**. Don't rely on the $3m small-business exemption: it doesn't cover businesses that trade in personal information, tranche-2 removal is in exposure draft (reported 31 Aug 2026) **[unverified date]**, and a marketplace with consumer data will lose it quickly anyway.

Automated-decision transparency obligations start **10 December 2026** **[verified: multiple firms; one says 11 Dec]**. These cover significant decisions made by automated systems, such as courier deactivation, merchant ranking and fraud blocks. The statutory privacy tort has been in force since June 2025 **[verified: existing knowledge]**. Fix: blur faces on the device before upload, set retention limits, and disclose automated decisions in the privacy policy.

**9. Catalogue IP: photos are the risk, facts aren't (Med).** Australia has no database right (IceTV v Nine, HCA 2009), so SKU facts, prices and names are largely free to compile **[verified: summaries]**. Photographs and packaging artwork are copyright works. Scraping Woolworths or Coles product images infringes the photographer's copyright. A merchant's own photo of a pack reproduces the brand's artwork. Brands tolerate this in practice, but your licence to use it is only as good as the merchant's grant. The EU *does* have a sui generis database right, so "global" catalogue scraping is riskier there. Fix: take merchant photos under an express licence in the terms, license GS1 Australia data (GS1 is the global barcode standards body) for brand imagery, and never scrape retailer images.

**10. Payments and tax (Med).** Draft payments-licensing reform (Treasury Tranche 1 exposure draft, 12 Mar 2026, consultation closed 9 Apr 2026) will bring payment services and stored-value facilities into the AFSL regime and narrow exemptions **[verified: G+T, Allens, HSF summaries; not yet law]**. A platform that holds customer funds and settles to merchants in its own name could need a licence. Stay inside a licensed PSP's connected-account model.

GST:
- **As agent:** the merchant makes the taxable or GST-free supply. Platform commission and customer fees are taxable at 10%.
- **As principal:** you must classify every SKU as GST-free basic food or taxable (confectionery, soft drinks, prepared food). Shelf-scan misclassification then becomes your tax exposure.

The ATO sharing-economy reporting regime excludes sales of goods where ownership transfers **[verified: ATO page]**, so marketplace goods sales aren't reportable. Courier services through your app may be.

**11. Merchant terms: unfair contract terms with penalties (Med).** Most merchants are small businesses, so standard-form terms are exposed to UCT penalties (in force since 9 Nov 2023) **[verified: existing knowledge]**. Risky terms include unilateral changes to the take rate, broad termination rights, uncapped chargeback recovery and IP grabs over shelf scans. IGA and Foodworks retailers may also be bound by banner and supply agreements that restrict third-party online channels **[unverified; question for the merchant specialist]**.

## Things the brief gets wrong, misses or understates

- **"Global from day 1" is regulatorily false.** The EU Platform Work Directive must be transposed by **2 Dec 2026**, with a rebuttable presumption of employment where a platform directs or controls work and limits on algorithmic management. Transposition is patchy (NL draft June 2026, DE moving, ES already has its Riders' Law) **[verified: Littler, Ius Laboris, DLA Piper]**. In New York City, grocery delivery apps have had to pay **US$21.44/hr (≈A$33) from Jan 2026**, rising to about US$22.13 from April 2026. Instacart responded with a US$5.99 fee and is suing **[verified: abc7, Fox Business, NYC DCWP page via search]**. California Prop 22 survives (2024) **[existing knowledge]**. Each country means separate labour, food, liquor, tax and privacy regimes, at roughly $50–150k in counsel cost to launch each **[estimate]**. Software can be sold globally. A marketplace cannot.
- **Merchants as dark stores** shifts compliance onto merchants (food safety, liquor licences, picking labour). That is the right allocation, but the platform still makes every price and stock representation the consumer relies on.
- **"Take a clip"**: the take rate is lawful, but a hidden mark-up or a checkout-only service fee won't be from 1 Jul 2027.
- The brief omits **trade measurement** for random-weight goods, **unit pricing**, **recalls** (the platform needs SKU-to-order traceability to notify customers) and **merchant UCT exposure**.

## Numbers checked

| Claim | Finding | Status / source |
|---|---|---|
| Gig delivery minimum standards in force | Interim On-Demand Delivery order, effective 17 Aug 2026; covers groceries | verified: FWO media release; FWC |
| Minimum rate | ≥$31.30/hr engaged time; about $31.50 motorbike, $32.00 car/van | verified (base), unverified (vehicle split: secondary sources) |
| Last-mile order | MS2024/1–2 pending; TWU amended drafts Mar/May 2026 | verified: FWC docs; no final order found |
| Unfair-deactivation jurisdiction | Employee-like workers, from about Feb 2025 | unverified (memory) |
| Drip pricing ban | Unfair Trading Practices Act 2026; passed 2 Jul 2026, starts 1 Jul 2027 | verified: Allens, McCullough Robertson |
| Unit pricing reform | Proposed category threshold 11→4, floor area 1,000→300 m²; not final | verified: NSA/ARC submissions May 2026 |
| Vic same-day liquor rules | Notify LCV, no unattended drop, first-order ID, report failures | verified: vic.gov.au checklist (2026) |
| Vic tobacco licence | Covers online sales; enforcement Feb 2026 (sources conflict with Jul 2026) | verified with conflict |
| Vapes | Pharmacy-only since 1 Oct 2024; TGA warnings to delivery apps Oct 2025 | verified: Health/TGA |
| Privacy ADM transparency | Starts 10 Dec 2026 | verified: multiple firms |
| Small-business privacy exemption | Still in force; exposure draft reported Aug 2026 | verified (in force) / unverified (draft) |
| Payments licensing | Exposure draft Mar 2026; not law | verified: G+T, Allens |
| EU PWD deadline | 2 Dec 2026 | verified |
| NYC grocery delivery minimum pay | US$21.44/hr from Jan 2026 → about US$22.13 in Apr 2026 | verified: search summary of DCWP and press |
| Online food labelling | Food Regulation Standing Committee guideline consultation closed 12 Dec 2025; no FSANZ standard yet | verified: health.gov.au consultation |
| 3-merchant courier floor cost | About $26–32 per order | estimate: $31.30 × 50–60 min |

## Improvements (ranked by impact)

1. **Agent structure, written down.** Merchant is seller of record, licensee, food business and picking employer. The platform is a disclosed commercial agent with a PSP connected-account flow. This avoids liquor, tobacco, GST-classification and payments licensing in one move.
2. **Buy delivery, don't engage couriers.** At launch, use 3PL APIs, so the 3PL is the platform operator for MSO and deactivation purposes. Model the $31.30/hr floor into the 3PL price. Move to an employed fleet only at density.
3. **Constrain multi-stop baskets legally as well as operationally.** Cap at 2–3 merchants within a radius. Route chilled and frozen items last. Require insulated, cooled bags. Set a hard time-out-of-temperature budget (for example ≤60 min from first chilled pickup). Exclude hot food and unpackaged potentially hazardous food not sealed by the merchant.
4. **Price protection by design.** Every price carries a scan timestamp. Charge the lower of displayed and till price, with the platform absorbing the difference and charging back merchants for errors above a threshold under the contract. All-in pricing (no checkout-only fees) now, ahead of 1 Jul 2027. Show unit price for every SKU.
5. **Restricted-category roadmap.** Phase 1 excludes liquor, tobacco, vapes and scheduled medicines. Phase 2 adds liquor in Victoria with the bottle shop as licensee, a 3PL with ID-scan-at-door, and its licence number shown in the app.
6. **Privacy by default in the scanner.** Blur faces on the device, upload no audio, keep video for 30 days or less, and publish an ADM disclosure before 10 Dec 2026.
7. **Catalogue IP hygiene.** Take an image licence in merchant terms, license GS1 data for brand imagery, and never scrape retailer images.
8. **Merchant terms reviewed for unfair contract terms:** 30-day notice on fee changes, mutual termination and capped chargebacks.

## Tests & kill criteria

| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| Ask 2 Victorian councils and Dept of Health whether an aggregator using 3PLs needs food registration | Written view | Any "register each vehicle or class the platform" answer means rethink before launch | 30 days |
| Quote Uber Direct, DoorDash Drive and Sherpa for 1-, 2- and 3-stop jobs, post-MSO | $/order | 3-stop above about $22 kills multi-merchant at AU basket sizes; go single-merchant | 30 days |
| Price-accuracy audit: scan 5 stores, compare 300 SKUs to till price at 0, 3 and 7 days | % mismatch | Above 2% at 3 days means the scan cadence fails the ACL. Fix or pivot to POS integration | 45 days |
| Cold-chain trial: data-logger in 3-stop runs, Melbourne in summer | Minutes above 5 °C | Any run over 120 min cumulative fails | 60 days |
| Merchant contract test: 10 merchants review the UCT-safe terms | Signed | Fewer than 5 sign means the problem is the commercial model, not law | 60 days |
| Privacy: scan 3 stores, count frames with identifiable faces | Frames with faces after on-device blur | Above 0 at upload is a blocker | 30 days |

## Answers to the brief's questions in my domain

**Q7 (legal constraints).** Nothing is fatal under the agent, 3PL and merchant-picks structure. The binding constraints, in order:
1. Delivery labour: the MSO at $31.30/hr engaged time, plus a pending last-mile order and deactivation rights.
2. ACL price accuracy and the 1 Jul 2027 drip-pricing ban.
3. Cold-chain rules on multi-stop routes.
4. Restricted goods (liquor licensee-only, tobacco and vapes excluded).
5. Privacy in shelf video and ADM transparency from 10 Dec 2026.
6. Unit pricing and trade measurement.
7. UCT in merchant terms.
8. A PSP-only payments flow ahead of licensing reform.

**Q6 (global).** Labour, food, liquor and privacy rules are local. The EU presumption of employment from Dec 2026 and NYC/California pay floors make marketplace expansion a jurisdiction-by-jurisdiction exercise. Software and the catalogue can be global, though EU database rights and copyright limit image scraping.

**Q8 (which business).** Software only has the lowest regulatory cost. An agent marketplace is viable in one city. A merchant-of-record or gig-fleet model is the wrong starting point.

**Q10 (90-day test).** Run the six tests above alongside the commercial pilot. They cost about $10–20k in total **[estimate]**.

## Questions I'd hand to other specialists

- **Unit economics:** rerun the multi-stop model with courier cost at $31.30–32/hr engaged time plus a 25–35% 3PL margin, and with platform-absorbed price errors at 1–3% of GMV.
- **Merchant specialist:** do IGA, Foodworks and Metcash banner agreements restrict third-party marketplaces or delivery? Will merchants accept chargebacks for price errors?
- **Tech:** can scan cadence keep price mismatch below 2% at 3 days? Can face blurring run on the device in real time?
- **Competitor analyst:** how did Milkrun, Voly and Uber Eats price the Victorian liquor ID-at-door flow? Is any AU marketplace treated as "retailer" under the Unit Pricing Code?
- **Founder fit:** does a regulation-heavy, labour-intensive marketplace fit the founder's risk limits, compared with a software-only path?
