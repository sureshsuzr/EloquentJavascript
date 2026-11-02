# Business-Model Alternatives Strategist: red-team report

FX used throughout: US$1 = A$1.52, €1 = A$1.75 [estimate: late-2026 working rate; re-check]. 19 web searches; several trade-press sites (SmartCompany) were blocked from the session, so some figures rest on search summaries.

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)

**The full aggregated marketplace (a) is fatal. A data-and-catalogue business (c), collected through free merchant software (b), survives only if certain conditions hold.** The biggest issue is that the founder has the customer wrong. The valuable output of shelf scanning is a **matched catalogue plus live availability for long-tail, non-barcoded, ethnic and specialty stock**. The parties that pay for that are the marketplaces that already own grocery demand (Uber Eats, DoorDash, HungryPanda) and the brands and importers that cannot see that channel. Merchants and consumers are the wrong payers. Treat merchants as *data suppliers* you may have to pay, not as customers. Even then, the AU ceiling is a ~A$5–15M revenue business. A venture outcome needs the same engine sold offshore, where traditional trade is most of FMCG.

## Verdict on the business model (which version, if any, is the business, from your lens)

| Variant | Who pays | Revenue potential (AU, yr 5) | Capital intensity | Defensibility | Founder fit | Global day 1? | Verdict |
|---|---|---|---|---|---|---|---|
| (a) Full marketplace, multi-merchant basket, take rate | Consumer fees + merchant clip | A$2–8M net revenue in 1–2 cities if it works; loss-making until high density [estimate] | Very high (riders, CAC, ops per city) | Low. Uber/DoorDash already list IGA, Drakes and independents | Partial (Fulfilio ops), but pure local-ops grind | No. City by city | **Kill** |
| (b) Merchant SaaS: scan → sync to Uber/DoorDash/Google/Shopify | Merchant, A$50–300/store/month | A$1–4M ARR (≈500–1,500 paying stores) [estimate] | Low | Low–medium. Deliverect Retail, Shopify POS→Google, Uber's own catalogue team | Good | Yes as software, but SMB churn and channel sales | **Not a business alone; it is the data-collection front end for (c)** |
| (c) Catalogue / availability / shelf-data as a service | Marketplaces (onboarding + availability accuracy), FMCG brands/importers (distribution intelligence), later retail media | AU A$3–10M; global multiples of that [estimate] | Medium (data ops, scan incentives) | **Medium–high if** the cross-merchant matched catalogue for non-barcoded/ethnic SKUs and a panel history accumulate | **Best**: CS + stats (panel design, matching) + ex-BCG selling into FMCG | **Most credible**: software + data, sells to multinationals | **The business, if tests pass** |
| (d) Niche marketplace (diaspora grocery, or premium fresh from butchers/bakers) | Consumer + merchant | A$3–9M net revenue on A$20–60M GMV in Melb/Syd [estimate] | Medium–high | Low–medium. HungryPanda already aggregates Asian merchants; Umall runs warehouses | Medium | No | **Optional later demand-side proof, not the start** |
| (e) B2B: cafés/restaurants supplied by local retailers | Venue | <A$1M. Retail prices sit above wholesale | Medium | Low. Ordermentum (A$55M raise May 2026), Choco | Low | No | **Kill** |

**Sequence:** (1) concierge catalogue and availability service for **one marketplace** across ~50 Melbourne specialty and ethnic stores, with merchant software free; (2) a **distribution-intelligence panel** for brands and importers in the ethnic/independent channel; (3) export the engine offshore (traditional-trade markets) or license it to a marketplace; (4) retail media only once (2) has an audience-linked dataset. Never build delivery.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

1. **(a) has no gap to fill, and that kills it (High).** The thesis is that merchants "get an additional sales channel". They already have it. IGA has been on DoorDash since 2021. DoorDash added Drakes and local grocers such as Yuen's, added 150 more Woolworths stores in July 2026, and has a 32-market regional rollout to end-2026 [verified: Inside Retail; Medianet Jul 2026; Food Magazine]. Uber Eats runs an independent/specialty grocery marketplace and launched SME grocery tools [verified: SmartCompany headline; Uber newsroom]. The multi-merchant basket is the only new feature. It adds a stop per merchant, which is exactly the cost that killed Milkrun: wound down 14 Apr 2023 after ~A$86M, 400 redundancies, reportedly losing ≥A$10 per delivery, bought out of administration by Woolworths for ~A$10M [verified: Startup Daily, SmartCompany, Forbes AU]. Voly, Send and Deliveroo had already exited [verified: same].
2. **(b) is a feature that both sides of the market already supply (High).** Shopify POS syncs local inventory to Google, and Lightspeed has Google integrations [verified: Shopify changelog; tech.co]. Deliverect Retail syncs price and inventory to Uber/DoorDash/Deliveroo, from ~US$1,428/yr [verified: Deliverect site; TrustRadius listing, unverified price]. Instacart's Catalog Engine builds AI catalogues for grocers [verified: Mass Market Retailers, Nov 2025]. Uber enriches merchant catalogues with images and descriptions [verified: Uber merchant pages]. A per-store SaaS fee competes with free tools offered by the marketplace itself. The Pointy precedent cuts both ways. A device-based (A$1,370) "get independent inventory online" product did reach "thousands of stores" and sold to Google for a reported ~US$160M (~A$245M), but only because Google wanted the data [verified: Irish Times, tech.eu; price conflicting, ">US$80M" for 51%]. **The exit was a data sale to a demand owner, not a SaaS outcome.** That is the template.
3. **Shelf scans have the most value where POS data is weakest, and that is a narrower set of stores than the brief assumes (Med–High).** Most of Metcash's ~1,600 IGA/Foodland stores [verified: Metcash] have scanning POS. Their SKU data already exists and flows to Metcash and to DoorDash/Uber integrations. Shelf scans add real value only for: (i) non-barcoded or loose fresh items (butcher, bakery, deli, produce); (ii) ethnic grocers with imported, inconsistently barcoded SKUs and weak POS; (iii) on-shelf availability, which POS stock-on-hand regularly overstates. Make that the beachhead and drop "all merchants".
4. **Shelf-image data is a hard, capital-hungry business globally (High for (c)).** Trax raised ~US$1.06B (~A$1.6B). It was valued at ~US$2B in 2021 and reached only ~US$170M (~A$260M) trailing revenue before being merged into FORM in Feb 2026 at an undisclosed price, with its IR business reportedly carved out [verified: CB Insights, multiples.vc; carve-out detail unverified]. FMCG brands do pay for shelf data, but in-store image recognition commoditised: Trax now runs on reps' own devices. **The data has value. The image-recognition technology is not a moat.** The moat has to be coverage of stores nobody else sees, plus a statistically valid panel.
5. **Willingness to pay for independent-store shelf data in AU is thin at the top and real at the edges (Med).** In AU, independents supplied by Metcash have ~7% of supermarket sales against Woolworths 38%, Coles 29%, Aldi 9% [verified: ACCC final report 21 Mar 2025, via SBS/AAP]. Large FMCG suppliers decide budgets on Woolworths/Coles data (Quantium/Cartology, Coles 360), plus Metcash wholesale and scan data. A 7% channel gets 7% attention. Ethnic and specialty grocers are the real blind spot. Circana/NIQ do not measure them well [unverified: no public channel-coverage documents found]. That channel matters to Asian/Indian/Middle-Eastern importers, challenger brands, and multinationals pushing "world foods" lines. Those buyers are many, small and price-sensitive: ~A$20–80k/yr each [estimate], not Nielsen-sized contracts.
6. **Retail media without an audience is not a product (Med).** Cartology/Woolworths digital & media earned ~A$675M (2024), and Coles 360 ~A$450M (Morgan Stanley est.) [verified: AdNews]. Cartology grew 19.5% and Coles 360 13.5% in FY25 [verified: Mediaweek, AdNews]. That money pays for *logged-in shopper reach plus closed-loop sales*. A shelf-scan catalogue has neither. Instacart's ad business (>US$1B run-rate; Carrot Ads across 310+ retailer sites) [verified: Instacart Q2/Q4 2025 calls] shows the route: retail media only follows owning the transaction or powering retailers' e-commerce. Retail media is year 4+, if ever.
7. **The diaspora niche is already aggregated (Med for (d)).** HungryPanda reports 45,000 AU merchants and 3.5M users, including Asian grocery [verified: HungryPanda press release Feb 2026, self-reported]. Umall (Sydney, automated warehouse, 20k SKUs, absorbed Asian Grocer Online Jul 2025) runs the first-party model [verified: Umall site, self-reported]. Weee! (~US$1.0B revenue 2024, US$4.1B 2022 valuation) [verified: Sacra estimate; 2022 round] proves diaspora grocery scales, but on **owned inventory and warehouses, not local stores as dark stores**. Weee! is the strongest evidence *against* the aggregation mechanic, not for it.
8. **B2B is wholesale, and retailers sit at the wrong price point (High for (e)).** Cafés buy at wholesale on account from distributors. Ordermentum (28k venues and suppliers, ~A$700M orders processed at an earlier round, A$55M from Five V May 2026) and Choco (US$1.2B 2022 valuation, layoffs 2023) own the ordering layer [verified: Business News Australia, Startup Daily, multiples.vc, TechCrunch]. Local retail supply is a top-up market only.

## Things the brief gets wrong, misses or understates

- **"Additional sales channel" is stale.** Independents already have three channels (Uber Eats, DoorDash, own sites/Shopify). The real pain is **keeping catalogue and availability accurate across those channels**, shown in cancellations, substitutions and refunds. That pain is the wedge.
- **"Global from day 1"** is true only for (c), and for (b) as the data front end. Grocery delivery is city by city (see Milkrun).
- **Who owns the catalogue** is missing. GS1's barcode data, Uber's catalogue team, Instacart Catalog Engine and Metcash already hold barcoded catalogues. The open ground is **non-barcoded, imported and fresh SKUs, and cross-merchant matching of them**.
- **Who must be paid.** Data businesses pay data sources: Nielsen-style panels pay retailers or give them something of value. A continuous scan habit will need a rebate, free tools or revenue share. The brief assumes merchants pay.
- **The Fulfilio analogy is weaker than it looks.** Spare warehouse space is idle capacity with near-zero marginal cost. Merchant staff picking during trade is *not* idle: it costs labour and congests the store. The true idle asset here is **information already sitting on shelves that no system records**, which points to (c), not (a).
- Date: the brief is dated 3 Nov 2026; today is 2 Nov 2026. A trivial slip.

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status / source |
|---|---|---|
| Independents are a meaningful channel | Metcash-supplied ~7% of supermarket sales; Woolworths 38, Coles 29, Aldi 9 | verified: ACCC final report 21 Mar 2025 (via SBS/AAP) |
| IGA network size | ~1,600 independently owned stores (IGA/Foodland) + ~300 other grocers supplied | verified: Metcash site; Metcash ACCC submission |
| Merchants lack online channels | IGA on DoorDash since 2021; Drakes; 150 more Woolworths stores on DoorDash Jul 2026; Uber Eats SME grocery tools | verified: Inside Retail, Medianet, Food Mag |
| Similar AU plays | Milkrun dead Apr 2023 (~A$86M, 400 staff, ≥A$10 loss/delivery); Voly, Send exited 2022; Woolworths bought Milkrun ~A$10M | verified: Startup Daily, SmartCompany, Forbes AU |
| Shelf-image data is big business | Trax ~US$1.06B raised, ~US$170M trailing revenue, merged into FORM Feb 2026 | verified (revenue = multiples.vc estimate) |
| Independent inventory → data exit | Pointy sold to Google, reported ~US$160M (conflicting ">US$80M") | verified, price unconfirmed |
| Retail media pool AU | Woolworths digital & media ~A$675M (2024); Coles 360 ~A$450M (MS est.); FY25 growth 19.5% / 13.5% | verified: AdNews, Mediaweek |
| Marketplace take on grocery | Instacart transaction revenue 7.1–7.3% of GTV; ads >US$1B run-rate | verified: Instacart Q1/Q2 2025 calls |
| Uber/DoorDash grocery commission AU | Not published; restaurants up to ~30%; 16% for independents was a COVID-era cap | unverified for grocery |
| Measurement incumbents | NIQ FY25 revenue ~US$4.2B (~A$6.4B); Circana private | verified-ish (secondary citing NIQ release) |
| Diaspora grocery scale | Weee! ~US$1.0B revenue 2024 (first-party); HungryPanda AU 45k merchants / 3.5M users | Sacra estimate; self-reported PR |
| B2B incumbents | Ordermentum A$55M (May 2026, currency reported inconsistently); Choco US$1.2B (2022) | verified: BNA, Startup Daily; multiples.vc |
| Inventory-sync SaaS price | Deliverect from ~US$1,428/yr (~A$2,170) | unverified aggregator listing |

## Improvements (concrete changes to the plan, ranked by impact)

1. **Change the customer.** Sell **"catalogue onboarding + availability accuracy" to a marketplace**, priced per store onboarded (A$300–1,000 setup) plus per active store per month (A$30–100) [estimate]. Offer a success fee on fewer cancellations and refunds. Uber/DoorDash spend on catalogue ops for every long-tail grocer they add. HungryPanda (ethnic, long tail, weak catalogues) is the most likely first buyer.
2. **Give merchants the software free, or pay them.** Offer free channel sync (Uber/DoorDash/Google local inventory/Shopify), a weekly "what's missing from your shelf" report, and a data rebate (e.g. A$20–50 per complete scan) [estimate]. Contract for data rights up front: a licence to aggregate, de-identify and resell.
3. **Choose the beachhead the incumbents can't see:** ~50–100 Melbourne Asian, Indian and Middle-Eastern grocers, plus butchers and delis. That gives non-barcoded and imported SKUs, weak POS, high cross-merchant overlap (matching is the moat) and a clear brand buyer (importers).
4. **Build the brand product as a designed panel, not a heap of scans.** Use stratified sampling of stores and fixed scan cadence, and publish numeric/weighted distribution and on-shelf availability with confidence intervals. This is where stats training becomes a moat; Trax-style technology alone is not one. Sell a quarterly "independent and ethnic channel distribution" report to 5–10 importers and brands.
5. **Plan the global step as license or replication of the engine, not marketplace expansion.** Target (i) marketplaces' long-tail onboarding in other countries; (ii) traditional-trade FMCG markets (SE Asia, India, LatAm), where independents are the main channel and brands already pay for audits (e.g. BeMyEye's 400k crowdsourced "Eyes" for independents [verified: BeMyEye case study]). Expect local competitors there.
6. **If a consumer front end is ever needed**, run (d) as a *demand experiment*: one scheduled weekly diaspora or premium-fresh run in one suburb. It proves the catalogue drives orders, not a q-commerce launch.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| # | Test (≤A$40k total, part-time-compatible subject to employer consent) | Metric | Continue if | Kill if | By |
|---|---|---|---|---|---|
| 1 | Scan 30 Melbourne specialty/ethnic stores (phone video), build matched catalogue | SKU ID precision on non-barcoded/imported items; cross-store match rate; human minutes/store | ≥90% precision after review; ≥40% of SKUs matched across ≥2 stores; ≤60 min human QA/store | <80% precision or >3 h/store | 31 Jan 2027 |
| 2 | Re-scan cadence with data rebate | % stores scanning weekly unprompted for 6 weeks | ≥60% at ≤A$30/scan | <30% even when paid | 28 Feb 2027 |
| 3 | Marketplace buyer: pitch HungryPanda, Uber Eats AU grocery, DoorDash AU | Paid pilot or LOI | ≥1 paid pilot (≥A$20k) or LOI for ≥100 stores | No paid interest from any of 3 | 31 Mar 2027 |
| 4 | Accuracy value: compare cancellations/substitutions before and after sync on 10 stores already on a marketplace | Item-unavailable rate | ≥30% relative reduction | <10% | 31 Mar 2027 |
| 5 | Brand/importer demand: mock distribution report for 3 categories sold to 10 importers/brands | Paid pre-orders | ≥3 paid at ≥A$10k | 0–1 | 30 Apr 2027 |
| 6 | Merchant SaaS price test (to size (b) honestly) | Conversion at A$79/month after 30-day free trial | ≥25% | <10%: keep (b) free forever | 30 Apr 2027 |

**Kill the whole idea** if tests 3 and 5 both fail. Merchants alone will not support it.

## Answers to the brief's questions in my domain

- **Q8 (which version is the business):** (c), long-tail catalogue + live availability + independent/ethnic channel distribution data, with (b) as the free collection layer. (a) and (e) are dead. (d) is a later, optional demand proof.
- **Q6 (global from day 1):** credible only for (c). A marketplace or niche delivery business is city by city.
- **Q9 (founder fit vs rent-roll path):** (c) is the best fit of the five. It needs ML matching, panel statistics, and enterprise selling to FMCG/marketplaces, all strengths of an ex-BCG CS/stats CFO. Like the rent-roll engine (round 3), it can be tested part-time for ~A$40k. Unlike the rent-roll engine, it has no ~250–900-deal ceiling, but it needs real enterprise customers before quitting. On expected value it beats (a) by a wide margin. It beats staying employed only if test 3 *and* test 5 pass: a marketplace contract plus brand revenue gives a credible A$1M ARR by year 3 [estimate]. Don't run both paths full-time. Pick after the 90-day results.
- **Q10 (smallest test):** tests 1, 3 and 5 above in 90 days. Thirty stores, one marketplace pitch, ten brand pitches.

## Questions I'd hand to other specialists

- **CV/ML specialist:** precision of recognising imported/ethnic packs and loose fresh items from phone video; can facings → stock-level estimates be trusted at all?
- **Unit-economics specialist:** what do Uber Eats/DoorDash AU spend per long-tail grocer on catalogue onboarding, and what does an item-unavailable cancellation cost them?
- **Legal/privacy:** data-licence terms with merchants. Does scanning in-store expose shoppers' faces (APP 3/5)? Does reselling price/availability data breach merchant agreements with Metcash or the marketplaces?
- **Competitor analyst:** is Pointy/Google "See what's in store" still live? Who sells shelf/OOS audits for traditional trade in SE Asia/India, and at what per-store price?
- **Brand/FMCG buyer specialist:** what do AU importers and challenger brands pay today for independent-channel distribution data (Circana/NIQ/field audits)?
