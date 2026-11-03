# Stage 1: physical-asset arbitrage and logistics lens (agent 04)

3 Nov 2026. Lens: the Fulfilio pattern. Find physical capacity that is under-used or mispriced, consolidate it, and sell it as a product to whoever is short of it. 17 web searches. Labels: **[verified: source]** means confirmed in search results, usually trade press. **[estimate]** means my own figure. **[unverified]** means a single or conflicting source.

## The 2026 thesis in one paragraph

In 2016 Fulfilio's scarce input was **warehouse space near customers**. In 2026 Melbourne's scarce physical input is **grid connection capacity on land that can be used**. Here is the evidence:
- AusNet reportedly holds an 8–10 GW queue of data-centre connection requests, and AEMO's figure for large-load enquiries is reportedly >18 GW **[unverified: RenewEconomy, conflicting figures]**.
- Land bought for data centres in Melbourne's north is reported at **70–100% above industrial land rates**. PGIM paid roughly **A$8M/ha** at Epping **[verified: commercialrealestate.com.au and others, trade-press figures]**.
- Hardstand let to data-centre contractors exceeded 210,000 m² in H1 2026 **[verified: commercialrealestate.com.au citing Colliers]**.
- Heavy fleets are electrifying. Australia Post received A$40.5M for 100+ electric trucks plus depot electrical upgrades **[verified: minister.infrastructure.gov.au, Jul 2026]**, and Zenobē closed a A$400M AU/NZ fleet-electrification platform **[verified: thedriven.io, Jun 2026]**.

Grid capacity is unevenly allocated. Many existing industrial connections sit half-used at sites that were sized for old loads, so the arbitrage is to find that capacity, aggregate it and sell it. The skill this needs is **pricing the probability that a site will get power, and when**, which is the founder's statistician/underwriter edge. It isn't a logistics skill.

## Ideas generated and discarded

- **Returns and reverse-logistics hub for cross-border marketplaces.** This is ops-heavy density work with the same failure shape as the grocery round. Global platforms are forecast to hold ~36% of AU e-commerce in 2026 **[verified: Shippit report via ecommercenews]**, but they own the returns flow and will commoditise it. Killed.
- **Cross-border fulfilment into Asia/US for AU brands.** The margin is thin, and freight forwarders and Shopify partners already do it. Killed.
- **Parcel-locker or kerb-space network.** Australia Post and the councils own the scarce input, so the founder would be a vendor rather than an arbitrageur. Killed.
- **Home-battery VPP aggregator.** The capacity is real: >500k batteries installed under Cheaper Home Batteries, only ~10% enrolled in VPPs **[verified: energy-storage.news; GloBird estimate]**. But Amber claims >50% of automated home batteries and has just raised ~€49M **[verified: thenextweb, 2026]**, and retailers own the customer. Too late for a new entrant.
- **Converting idle CBD offices (logistics, storage, compute).** The capex per m² is high and the buildings have the wrong power and floor loads. Killed.

Kept: four ideas, all built on grid-connected land or capacity, from most bold to most conservative.

---

## Idea 1 (bold): Grid-ready land originator ("powered land" development)

| Field | Assessment |
|---|---|
| **One-liner** | Option under-used industrial sites in Melbourne's north/west/south-east that have, or can credibly get, large grid connections. Take them through planning and a connection offer, then sell or lease them "powered and entitled" to data-centre operators, BESS developers and fleet-depot investors. Buyers pay the land premium; the founder keeps development profit plus a carried interest. |
| **Why now (2026)** | Connection capacity, not land, is the binding constraint for data centres and large batteries. Powered/entitled land trades at a 70–100% premium to industrial **[verified, trade press]**. Victoria's Development Facilitation Program now fast-tracks BESS approvals **[verified: energy-storage.news]**, so planning risk is shrinking while connection risk is growing, and connection risk is a pricing problem. A speculative "gold rush" in the queue (Bruce Mountain's phrase **[verified: quoted in RenewEconomy]**) means buyers can't tell which sites are real. Someone who can underwrite site × substation × timing gets paid for that information. |
| **Unfair inputs** | (1) Statistician/underwriter: build a site-scoring model from DNSP Distribution Annual Planning Reports (zone-substation headroom), AEMO connection data, zoning, flood/heritage overlays and land sales. This is the same muscle as the rent-roll pricing engine, aimed at a much larger ticket. (2) Real-estate and agency network from LocalAgentFinder for off-market industrial landowners. (3) Fulfilio taught him to find under-used industrial sites and negotiate with their owners. (4) Credible to family offices and super funds as GP. **Weak spots:** no power-engineering or planning background (needs a co-founder or partner who is an ex-DNSP connections engineer); no track record in property development; competes with well-capitalised players (Stockland, NEXTDC, Keppel, PGIM) who buy direct. |
| **Market & model** | **Size:** Melbourne data-centre pipeline is 24 projects in planning, 37 operating **[verified: RenewMap, May 2026]**; BESS approvals are in the multi-GWh range annually. **Per-deal maths [estimate]:** a 10 ha site at ~A$2.5M/ha industrial = A$25M. Powered and entitled at A$4.5–8M/ha = A$45–80M, so the gross uplift is A$20–55M. Option fees, studies, planning and connection deposits cost A$1.5–4M over 2–4 years. Even at 30–50% of the uplift after paying landowners a share (in options with profit share), net development profit is ~A$6–20M per successful site. **Model:** option and profit-share agreements with landowners, rather than buying the land. Sell RTB or lease long term. GP fee of 1.5–2% plus 20% carry on a site-origination fund. **Comparables:** US powered-land premiums (~US$6M+/acre powered vs ~US$4M unpowered in N. Virginia **[verified: datacenterknowledge]**); ready-to-build BESS sales such as ACE Power's Kerang to Banpu and ACEnergy's Yanco to BW ESS (prices undisclosed **[verified]**). |
| **Capital & structure** | Phase 1: founder A$0.4–0.6M plus co-founder sweat for the model and first 3 options. Phase 2: A$15–30M site-origination fund from family offices and one strategic (a data-centre developer or super fund with a right of first refusal). Founder co-invests A$0.5M. Founder owns ~55–65% of the GP/developer company after a co-founder and early hires, plus a share of the fund's carry. No personal guarantees; options keep the balance sheet light. |
| **Outcome distribution (10 yrs, founder after-tax wealth from the path incl. any salary)** | P(fail) 35% → A$1.2M (2–3 years of option fees written off, return to an exec role). P(modest) 30% → A$3.0M (2–3 sites sold, small premium). P(good) 25% → A$8M (a repeatable platform, 6–10 sites, fund II). P(great) 10% → A$25M (carry on a A$100M+ programme or a strategic buy-out of the platform). **EV ≈ A$5.8M; median ≈ A$3.0M.** Bar: staying employed ≈ A$3.0–3.4M over 10 years **[estimate, extrapolated from the brief's 7-yr A$2.0–2.4M]**. |
| **Time to replace $500k** | Lumpy. First site sale in ~24–40 months, so a $500k-equivalent from about year 3. GP fees (A$300–600k/yr on a A$20–30M fund) partly bridge from year 2. **Can start while employed:** yes for the model and landowner conversations, if the employer consents to the outside interest. It's a non-competing field, so IP risk is low. |
| **Job satisfaction** | High. Pricing under uncertainty, deal-making, capital raising and physical assets: a Fulfilio rerun with bigger tickets. Ops load is low. The downside is long waits on DNSPs and planners, which tested patience in rounds 1–3. |
| **Key risks** | (1) **Connection reform:** AEMO/DNSPs move to "first-ready" queue rules or require deposits that crowd out option-holders, or the State reserves capacity in precincts. (2) **Big players go direct:** hyperscalers and REITs build their own origination teams, so the premium compresses. (3) **Data-centre bubble deflates** (AI capex cycle) and the premium falls back to industrial. **What kills it:** DNSPs say no headroom is likely in under 5 years at the sites the model ranks top, or buyers won't pay ≥40% over industrial for entitled sites with a connection offer. |
| **90-day test** | Cost ~A$40–60k. (1) Build v0 of the site screen from public DAPR/AEMO data and land sales, and shortlist 30 sites. (2) Interview 8 buyers (data centres, BESS developers, IOS funds) for price per hectare at three stages: optioned; with a connection enquiry response; with a connection offer plus permit. (3) Get indicative option terms from 5 landowners. (4) Lodge one DNSP pre-application enquiry. **Proceed if:** ≥2 buyers state a ≥50% premium for a connection-offer-stage site, ≥3 landowners accept options at ≤2% p.a. of value with profit share, and the DNSP signals plausible capacity on ≥1 site. **Kill if** none of these holds. |

---

## Idea 2: Host-site distributed batteries ("spare amps" fleet)

| Field | Assessment |
|---|---|
| **One-liner** | Sign warehouses, cold stores, logistics depots and Australia Post facilities to host 1–5 MW batteries on their existing connections and spare hardstand. Aggregate them into a fleet, earn wholesale arbitrage, FCAS and network-support revenue, and pay hosts rent plus a bill share. Develop to ready-to-build and sell to infrastructure buyers, or own with project debt. |
| **Why now (2026)** | Sub-5 MW distribution-connected BESS is now an asset class with buyers. KKR-backed CleanPeak bought SEI (42 MW BESS across 11 sites, 71 MW solar) **[verified: energy-storage.news, Apr 2026]**. Enervest/Billion Watts are developing 10 sub-5 MW sites (50 MW/200 MWh) across NSW and Victoria **[verified: ess-news, Jun 2026]**. SEI/ACEnergy have a 27-project, 135 MW pipeline **[verified]**. Battery energy-basis capex fell from ~A$990 to ~A$480/kWh **[verified: Modo summary, Feb 2026]**. Existing industrial connections save months of queueing. |
| **Unfair inputs** | Fulfilio was literally a network of warehouse-owner relationships, and this is the same customer with a new product. The Australia Post relationship could open depot and facility hosting. Statistics for revenue forecasting and hedging. **Weak spots:** competitors with an 18–36 month head start; no electrical-engineering team; host-site connections may be too small (often <1 MW of headroom). |
| **Market & model** | **Revenue [verified, Modo]:** NEM-wide battery revenue was A$44k/MW/yr in Aug 2026, Victoria A$53k in Jul 2026, a 12-month trailing average of ~A$85k/MW/yr, and a low of A$29k in May 2026 (it was A$142k in the 12 months to Sep 2025). Four-hour assets earn ~2x per MW. **Unit economics, 5 MW/10 MWh [estimate]:** capex ~A$5.5–6.5M including connection. Revenue A$85k/MW market plus A$20–40k/MW network support or host bill savings = A$525–625k/yr. Opex plus host rent ~A$150k. EBITDA ~A$400–475k, about a **7% unlevered yield, which is marginal**. The money is therefore in **development margin**: RTB sales at ~A$50–100k/MW **[estimate; no disclosed AU per-MW prices found]**. 30–50 MW/yr developed gives A$1.5–5M/yr gross. |
| **Capital & structure** | Development company: A$1.5–3M seed (founder A$0.5M plus angels/family offices) covers ~40 site agreements and ~15 connection applications. Project capex comes from the buyer or a CEFC-style lender. Founder owns ~50–60% after seed and co-founder. |
| **Outcome distribution (10 yrs)** | Fail 30% → A$1.4M. Modest 35% → A$3.5M. Good 25% → A$7M. Great 10% → A$15M (sold to CleanPeak-type consolidator or an infrastructure fund). **EV ≈ A$4.9M; median ≈ A$3.5M.** |
| **Time to replace $500k** | ~3 years (first RTB sales in ~18–30 months). Host signing can start while employed; connection applications and site work need full-time effort from ~month 9. |
| **Job satisfaction** | Good. Site deals, modelling and capital work. More engineering/contractor management than he'd want, and less "big idea" than Idea 1. |
| **Key risks** | (1) **Revenue compression:** batteries are cannibalising spreads (the record low in May 2026), so buyers cut their bids. (2) **Crowded field** (CleanPeak/KKR, Enervest, ACEnergy, DNSP community-battery programs). (3) Host-site headroom is smaller than hoped and each site becomes a bespoke engineering project. **What kills it:** buyers' RTB bids for sub-5 MW projects are below A$40k/MW, or the median host site offers <1.5 MW. |
| **90-day test** | ~A$25k. Call 40 warehouse/cold-store owners from the Fulfilio network and get 10 to share connection size and interval data. Get DNSP hosting-capacity maps for those sites. Ask 3 buyers (CleanPeak, Enervest, an infrastructure fund) for indicative RTB pricing. **Proceed if** ≥5 sites have ≥2 MW headroom and buyers bid ≥A$60k/MW. |

---

## Idea 3: Electrified fleet yards (industrial outdoor storage + depot charging)

| Field | Assessment |
|---|---|
| **One-liner** | Lease or buy hardstand in Melbourne's west and north, upgrade the connection, add a battery and chargers, and license secure, charged bays per month (energy included) to electric van and truck fleets: Australia Post contractors, couriers, construction and data-centre contractors. Sell stabilised yards to IOS/infrastructure funds. |
| **Why now (2026)** | IOS is now an institutional asset class: Realterm/Partners Group are targeting a multi-billion-dollar east-coast portfolio, yields reach up to 7.5% **[verified: commercialrealestate.com.au]**, and a Melbourne west hardstand leased at a record **A$80/m² net** **[verified: propertymarkets.news, Sep 2026; single data point]**. E-trucks are scaling: Australia Post has 100+ trucks funded, and Zenobē has A$100M for e-truck adoption and an off-site truck hub at Mascot **[verified]**. Depots without power become stranded, and charged yards close to the city are scarce. |
| **Unfair inputs** | Australia Post relationship (a plausible anchor customer, or introductions to its contractor base). Fulfilio experience of local-hub geography. Capital-markets credibility for a yard fund. **Weak spots:** fleet-operations depth; Zenobē bundles vehicles, finance and charging, so it can out-compete a yard-only offer. |
| **Market & model** | **Unit economics, 2 ha yard with 70 bays (40 truck, 30 van) [estimate]:** ground rent ~A$50–70/m² → A$1.0–1.4M/yr. Electrification capex (connection upgrade, 3–4 MW of chargers, 2 MWh battery) ~A$5–7M. Bay licence A$1,800/truck-month and A$600/van-month → ~A$1.08M/yr. Energy margin of A$0.12/kWh on ~5 GWh → A$0.6M. Opex ~A$0.4M. **EBITDA ~A$0.3–0.5M on A$6M capex is thin while leasing the land.** It works when the site is owned at a 6.5–7.5% yield and valued as an electrified IOS asset, or when the anchor contract is take-or-pay. |
| **Capital & structure** | Infrastructure/PE capital: A$20–40M per 3–4 yards, with a CEFC debt layer likely. Founder as GP/developer, ~30–40% of the opco plus a promote. A$0.5M personal. |
| **Outcome distribution (10 yrs)** | Fail 40% → A$1.2M. Modest 35% → A$3.0M. Good 18% → A$7M. Great 7% → A$18M. **EV ≈ A$4.1M; median ≈ A$3.0M.** |
| **Time to replace $500k** | ~3–4 years. Can't really operate while employed beyond the 90-day test. |
| **Job satisfaction** | Medium. Real-asset building he'd enjoy, but it drifts toward the ops-heavy, utilisation-dependent businesses that scored badly in earlier rounds. |
| **Key risks** | (1) E-truck adoption is slower than funded pilots imply, so bays sit unused. (2) Fleets prefer to electrify their own depots (Australia Post is doing exactly that with its grant). (3) Zenobē and OEM-financed bundles capture the customer. **What kills it:** no anchor willing to sign a ≥5-year take-or-pay for ≥50% of bays. |
| **90-day test** | ~A$15k. Get 10 fleet operator interviews plus Australia Post network/property. Test a letter of intent for 20+ bays at ≥A$1,500/truck-month. Get IOS fund appetite for buying an electrified yard on stabilisation. **Kill if** there are fewer than 2 LOIs. |

---

## Idea 4 (most conservative, smallest): Cold-chain flexibility aggregator

| Field | Assessment |
|---|---|
| **One-liner** | Software plus a "flex retail" partnership that treats cold stores' thermal mass as a virtual battery: pre-cool in cheap or negative-price hours and coast through price spikes. Paid as a share of savings and demand-response revenue. Doubles as a host-signing channel for Idea 2. |
| **Why now (2026)** | Victoria hit the A$16,000/MWh price cap in winter 2025, and refrigerated warehousing was a key responder **[verified: Enel X]**. Solar duck curves give midday prices near zero. Proof points exist: Enel X/Lineage (13 warehouses, 5.4 MW, ARENA-funded to Mar 2027) and Flow Power/Harbourside **[verified]**. |
| **Unfair inputs** | Fulfilio's relationships with warehouse and cold-store owners; strong fit with statistics and optimisation. **Weak spot:** incumbents (Enel X, Flow Power) are already in the space with retail licences. |
| **Market & model** | ARENA estimates **up to ~500 MW** of flexible refrigeration demand nationally **[verified: ARENA/pv-magazine]**. At A$50–100k/MW/yr of value created **[estimate]**, the pool is ~A$25–50M/yr. A 25% share at 30% penetration gives ~A$2–4M revenue. **Thin niche, the same trap as the rent-roll engine as a standalone business.** |
| **Capital & structure** | Bootstrap A$150–300k, or an ARENA grant. Founder owns 80%+. |
| **Outcome distribution (10 yrs)** | Fail 35% → A$2.2M (can stay employed longer). Modest 45% → A$3.0M. Good 15% → A$4.5M. Great 5% → A$9M (bought by a retailer or Enel X-type firm). **EV ≈ A$3.3M; median ≈ A$3.0M.** |
| **Time to replace $500k** | 4–6 years, possibly never. Can start while employed. |
| **Job satisfaction** | Good intellectually (optimisation), small in scale; likely to under-stretch him. |
| **Key risks** | (1) Small market. (2) Incumbents already sell it, bundled with supply. (3) Food-safety and insurance limits on how far temperature can drift. **What kills it:** pilot savings below A$30k/MW/yr. |
| **90-day test** | ~A$10k. Get 12 months of interval and temperature data from 3 cold stores, backtest against NEM prices, and pitch the result. **Proceed if** the backtest shows ≥A$50k/MW/yr and 2 sites sign a pilot. |

---

## Cross-cutting notes and honest caveats

- **One engine, several exits.** Ideas 1, 2 and 3 share a core asset: a **site-and-connection underwriting model** that combines DNSP headroom, zoning, land value, planning pathway and buyer demand. That is the "data layer sold to whoever owns the capital" pattern, which earlier rounds found to be the founder's edge, joined to the physical arbitrage that made Fulfilio work. The best-ranked site goes to the highest-value use: a data centre if the capacity is large, a battery if it is mid-sized, a fleet yard if it is near the city with a moderate connection.
- **Pricing evidence is weak.** No Australian per-MW price for a ready-to-build battery project and no per-MW price for powered land was found in public sources (most deals don't disclose consideration). The 90-day buyer interviews are therefore the critical test, not an optional one.
- **Battery revenues are falling fast** (A$142k → ~A$85k trailing, low of A$29k/MW/yr). Any idea that relies on owning merchant batteries looks worse in 2026 than in 2024. Development margin and land premium are more robust than operating yield.
- **Grid-queue speculation cuts both ways.** It creates the information gap Idea 1 profits from, but a reform that clears speculative applications could also strand option-holders.
- **Employment:** none of the four competes with a SaaS employer, so the IP and confidentiality risk is low. Outside-interest consent is still needed for anything beyond research.

## Top pick and ranking

**Top pick: Idea 1, the grid-ready land originator, with Idea 2 as its cash-flow sibling run by the same team and model.** It has the highest EV (≈A$5.8M against a ≈A$3.0–3.4M staying-employed bar). It applies the founder's demonstrated edge (pricing an uncertain physical asset) to the scarcest, most mispriced input in Melbourne in 2026. It is mostly off-balance-sheet (options, not land), so it stays within the founder's ~A$1M risk budget without personal guarantees, and the 90-day test is cheap and decisive. Its weakness is lumpy, slow income in years 1–3. That is partly mitigated by starting while employed and by GP fees once a fund is raised.

Ranked:
1. **Grid-ready land originator:** EV ≈ A$5.8M, median ≈ A$3.0M.
2. **Host-site distributed batteries:** EV ≈ A$4.9M, median ≈ A$3.5M.
3. **Electrified fleet yards (IOS + charging):** EV ≈ A$4.1M, median ≈ A$3.0M.
4. **Cold-chain flexibility aggregator:** EV ≈ A$3.3M, median ≈ A$3.0M.

## Sources (from searches, 3 Nov 2026)

- commercialrealestate.com.au: data-centre land premium; IOS yields up to 7.5% and Colliers H1 2026 hardstand take-up
- datacenterknowledge.com: US powered vs unpowered land premium
- RenewEconomy: data-centre connection queue (AusNet 8–10 GW; AEMO >18 GW; Bruce Mountain "gold rush")
- RenewMap: Victorian data-centre project counts
- energy-storage.news: Cheaper Home Batteries 500k installs; ACE Power Kerang sale; CleanPeak/SEI; Victorian DFP approvals
- ess-news / pv-magazine-australia: Enervest–Billion Watts sub-5 MW portfolio; BW ESS Yanco
- Modo Energy research summaries: NEM battery revenues (Jul/Aug 2026, Sep 2025); capex Feb 2026
- minister.infrastructure.gov.au / thedriven.io: Australia Post A$40.5M e-fleet
- thedriven.io / cfotech: Zenobē A$400M platform, A$100M e-truck program
- propertymarkets.news: A$80/m² Melbourne west hardstand record
- Enel X, ARENA, Flow Power: cold-store demand response, 500 MW estimate, Lineage 5.4 MW
- thenextweb / Forbes AU: Amber Electric raises
- Shippit report via ecommercenews.com.au: marketplace share
