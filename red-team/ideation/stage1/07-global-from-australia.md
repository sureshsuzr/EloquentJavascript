# Stage 1: Global-from-Australia Software Scout (07)

Agent lens: problems where Australia regulates or adopts first, so a product can be proven in Melbourne and then sold into the UK, US, EU or Asia as they follow. 3 Nov 2026. Australian English, AUD unless marked. 16 web searches; many figures rest on search summaries, labelled.

## How I searched

I screened ~14 "Australia-first" shifts against three filters: (1) does Australia genuinely lead by 2–5 years, with a named follower market; (2) does the founder's demonstrated edge (pricing/underwriting under uncertainty, capital allocation, data layers sold to whoever owns capital, physical-asset arbitrage) matter more than domain contacts he lacks; (3) is the buyer pool deep enough to be venture-scale (earlier rounds died on thin niches: 250–900 rent-roll deals/yr).

**Screened out (one line each):**
- *Payday super (live 1 Jul 2026; ATO small-business clearing house closed 30 Jun 2026)* [verified: Business NSW, Hall & Wilcox]: real pain, but it's a payroll feature owned by Xero/Employment Hero/clearing houses and not exportable.
- *Age assurance (under-16 social-media ban from Dec 2025; extended to AI chatbots, app stores, gaming in 2026)* [verified: biometricupdate.com]: Australia leads, but it's a crowded, sub-US$1-per-check biometric market (Yoti, Persona, k-ID, Veriff), and the founder has no identity edge. An independent *statistical test lab* is interesting but small.
- *Consumer Data Right:* stalled; action initiation deferred; little buyer pull.
- *Privacy ADM disclosure (10 Dec 2026):* compliance tooling commoditised by OneTrust-type vendors.
- *My Health Record share-by-default:* the incumbent clinical-software vendors own it.
- *METS/mining and agtech:* real Australian leadership, but no founder edge and long hardware cycles.
- *Grid-scale battery trading:* crowded (Tesla Autobidder, Fluence, Habitat, Gridcog).

**Kept:** four ideas where Australia is ahead and the founder's edge is the core of the product.

---

## Idea 1: "Mark": daily valuation and liquidity engine for private assets held by defined-contribution (DC) pension funds

**One-liner.** Independent, model-based daily valuation estimates, revaluation triggers and liquidity stress-testing for the unlisted assets (infrastructure, property, private equity, private credit) held inside daily-priced DC funds. Super funds pay first, then custodians and asset consultants. After that come UK master trusts and US target-date and 401(k) managers, which are now being pushed into private markets.

**Why now (2026).** Australia is the world's first large DC system to put heavy private-markets allocations behind daily-switchable member balances. Regulators are on it:
- APRA's Dec 2024 review found **12 of 23 trustees needed material improvement** in valuation governance or liquidity frameworks, with revaluation frequency and triggers named as weak spots [verified: APRA information paper, Investor Daily].
- ASIC REP 841 (14 Oct 2026) says the findings persist and that trustees **and auditors** must act further [verified: ASIC REP 841 summary].

The followers are a step behind:
- **US:** EO 14330 (Aug 2025) and a DOL safe-harbour proposal (comments closed ~1 Jun 2026; final rule expected late 2026, live 2027). Follow-on work covers valuation harmonisation [verified: NAPA, Mondaq, law-firm alerts].
- **UK:** Mansion House Accord commitments to private markets in DC by 2030 [unverified, not searched this round].

Every one of these systems runs into the problem Australia hit first: **stale marks let switching members arbitrage other members**.

**Unfair inputs.**
- **Fit:** statistician plus computer scientist; the product is a Bayesian nowcast of an unobserved price (comparable listed proxies, transaction comps, cash-flow models, manager marks), which is the "pricing under uncertainty" edge earlier rounds identified.
- **CFO-level fluency** in audit, valuation policy and board reporting: he can talk to a fund CFO, the chief risk officer and the auditor in their own language.
- **BCG alumni** are thick in super-fund strategy and risk teams.
- **Melbourne** is the super capital: AustralianSuper, ART's Melbourne operations, Aware, UniSuper, HESTA, Cbus, ISPT and IFM are all within a few kilometres.
- **Weak spots:** no buy-side valuation or asset-consultant track record; no existing relationships with CIOs; APRA CPS 230 vendor onboarding takes 6–18 months (round 3).

**Market & model.**
- *AU:* ~A$4T+ super (brief); unlisted share ~15–25% → ~A$0.6–1.0T [estimate]. ~20 large funds hold most of it. Pricing A$150–600k/yr per large fund; custodian/OEM licences A$0.5–2M. **AU ceiling ~A$8–20M ARR** [estimate].
- *Global:* UK DC/master trusts, US recordkeepers and TDF managers, Canadian and Dutch DC → **US$100M+ ARR potential** if it becomes the reference "DC mark" [estimate].
- *Comparables:* MSCI bought the remaining 66% of Burgiss (private-markets data) for US$697M, implying ~US$1.05B total [verified: Investing.com, Business Wire, Aug 2023]. Chronograph and Canoe are portfolio-monitoring comps [unverified valuations].
- *Revenue model:* SaaS licence per AUM band, plus a validation/audit-support tier sold to the auditors.

**Capital & structure.** VC. Pre-seed/seed A$3–5M after a 90-day proof; Series A A$12–20M on 3+ AU funds and one offshore pilot. Founder puts in A$0.2–0.4M. **Founder ownership ~60% after seed, ~40–45% after A, ~25–35% at exit** [estimate]. No personal guarantees.

**Outcome distribution (10 yrs, founder cumulative after-tax wealth incl. salary, A$).** Bar for comparison: staying employed ≈ A$3.0–3.5M over 10 years (extrapolated from the brief's A$2.0–2.4M over 7 years) [estimate].

| Outcome | P | Founder wealth | What it looks like |
|---|---|---|---|
| Fail | 40% | A$1.3M | Funds keep valuers + in-house; shut yr 3, back to a CFO role |
| Modest | 30% | A$3.5M | A$3–5M ARR AU-only; sold to a custodian/data vendor for A$20–40M |
| Good | 22% | A$10M | A$15–25M ARR incl. UK; exit A$150–250M |
| Great | 8% | A$35M | Reference DC mark in US/UK; exit A$600M+ |

**EV ≈ A$6.6M; median ≈ A$3.5M** (the modest band).

**Time to replace $500k.**
- Seed salary ~A$250k from month 6–9. A$500k-equivalent cash only from Series B (~yr 4–5) or a secondary.
- Discovery and data-licence conversations can start while employed, provided he has employer consent under the outside-interests clause. Building and selling needs the jump; target month 6 after the 90-day test.

**Job satisfaction.** High. Every day mixes modelling (state-space and Bayesian nowcasts, liquidity Monte Carlo), selling to CFOs and CROs, and regulator-grade rigour. It's closest to his statistician, CFO and BCG core, and it's intellectually deep. Less of the scrappy physical building he loved at Fulfilio.

**Key risks.**
1. **Buyers prefer "trusted names":** funds and auditors default to Kroll/Duff & Phelps-type valuers plus MSCI/Burgiss and custodians (State Street, JPMorgan). *Kill:* a custodian bundles a "good enough" daily estimate free.
2. **Ground-truth scarcity:** you need fund-level holdings and revaluation histories to show your model beats stale marks; funds may not share them.
3. **Sales cycle and CPS 230 onboarding** burn the seed before ARR arrives.

**90-day test (≤A$40k).**
- Run 15 interviews (CIO, CRO, head of valuations, fund CFO, 2 custodians, 1 Big-4 super audit partner).
- Build a backtest on public proxies plus one fund's de-identified 5-year unlisted revaluation history.
- **Proceed if:** ≥1 fund shares data; the model cuts the error versus the next quarterly revaluation by ≥40% against the "stale mark"; and ≥2 written paid-pilot offers at ≥A$75k.
- **Kill if:** <3 of 15 say the gap is unmet by their valuer or custodian.

---

## Idea 2 (bold): "Reserve": battery-fleet underwriting and flexibility capital, a Fulfilio-style arbitrage on idle home batteries

**One-liner.** Australia has installed home batteries faster than anywhere: **500k+ systems / ~11–14 GWh in ~12 months** under Cheaper Home Batteries [verified: energy-storage.news, CER June-qtr 2026 report: 111k installs, 3.6 GWh in Q2 2026 alone]. Most of them sit idle at the moments that matter: VPP enrolment is optional and low ("400,000 home batteries installed but barely a VPP in sight") [verified: Energy Magazine, May 2026].

Reserve does two things:
- **Leases dispatch rights** on existing batteries: households get a guaranteed A$150–250/yr; Reserve earns wholesale, FCAS and network-support revenue.
- **Finances new batteries** with $0 upfront as rebates taper, using its own 10-year cash-flow underwriting model (degradation, price volatility, household load, default).

Who pays: the NEM (wholesale/FCAS), distribution networks (flexibility services), and lenders and insurers who license the underwriting model. Later it exports the model and capital product to the UK, Germany, California and Japan.

**Why now (2026).**
- A one-off stock of ~0.5–1M under-utilised batteries has appeared within 18 months.
- Rebates step down each year, so the upfront-cost gap that finance fills widens.
- Australia's NEM is the world's most volatile, solar-saturated grid: the global test case for residential flexibility.
- Capital is pouring into the category: Kraken spun out of Octopus at **US$8.65B** (Origin holds 22.7%) [verified: Skadden, Proactive]; Amber raised a **€49M Series E** (Sept 2026, Morgan Stanley 1GT, E.ON) [verified: capital.com, thesaasnews].

**Unfair inputs.**
- **The Fulfilio pattern exactly:** consolidate fragmented, idle physical capacity into a network and sell it to whoever needs it. He has done this before.
- **Underwriting 10-year asset cash flows** is his stats/CFO edge.
- **Credible to raise both equity and warehouse debt:** CEFC, green lenders, family offices.
- **Weak spots:** no energy-market background, no AEMO registration or retail/market-participant licence, and no installer network.

**Market & model.**
- *Household economics:* VPP value is ~A$200–1,000/yr per 10 kWh battery depending on market and mode [verified range, installer guides, low quality].
- *Margin:* Reserve keeps a net ~A$100–250/battery/yr after paying the household [estimate].
- *Scale:* 100k batteries → **A$10–25M gross margin**; finance book spread 2–4% on A$7–10k assets [estimate].
- *Comparables:* Sunrun (US residential solar/storage leasing, public); Amber; Reposit; Evergen; Tesla Energy Plan; Brighte (AU green-loan finance) [funding unverified].

**Capital & structure.** Two layers:
- **Opco (software/aggregator):** VC seed A$4–6M, Series A A$20M+.
- **Asset layer:** off-balance-sheet warehouse facility (CEFC / green bank) A$50–200M, securitised later.

Founder ownership in opco ~25–35% at exit [estimate]; founder cash at risk A$0.3–0.5M.

**Outcome distribution (10 yrs, A$).**

| Outcome | P | Founder wealth | What it looks like |
|---|---|---|---|
| Fail | 55% | A$1.0M | Amber/retailers/OEMs (Tesla, Sigenergy) lock in orchestration; can't win enrolments |
| Modest | 25% | A$2.5M | 20–40k batteries, acqui-hired by a retailer/network |
| Good | 14% | A$8M | 100k+ batteries; finance book; exit A$150–300M |
| Great | 6% | A$30M | Exported underwriting + capital platform; Kraken/Sunrun-class category leader |

**EV ≈ A$4.1M; median ≈ A$1.0M** (the fail band: highest variance of the four).

**Time to replace $500k.** 4–6 years. It can't really start while employed past research: it needs market registrations, installer partners and capital raising.

**Job satisfaction.** Very high energy: physical-plus-financial arbitrage, capital raising, a big mission, and the most "Fulfilio-like" of the four. But it's also ops-heavier (installers, customer support, device integrations), which earlier rounds flagged as his weak pattern.

**Key risks.**
1. **Orchestration is being captured upstream:** Amber self-reports running >70% of automated home batteries [unverified, company claim]; OEMs ship native VPPs; retailers bundle. *This alone may kill it.*
2. **Revenue compression:** as GWh floods in, FCAS and evening-peak spreads compress; the 10-year cash flows underwrite badly.
3. **Device access/interoperability:** OEM API lock-in ("closed ecosystems" warning) and installer-configured faults (Reposit CEO: batteries VPP-capable at install, then "something breaks"; "colossal wasted opportunity") [verified: RenewEconomy].

**90-day test (≤A$50k).**
- Backtest 2023–26 NEM prices for a 10 kWh battery in VIC/SA/QLD: **net arbitrage + FCAS ≥ A$400/yr** after degradation, otherwise kill.
- Offer a flexibility lease via one installer to 300 unenrolled owners: **≥15% sign at ≤A$200/yr guaranteed**.
- Get one indicative warehouse term sheet at ≤9% all-in.
- **Kill if** two of the three fail, or no OEM grants API access on commercial terms.

---

## Idea 3: "Drawdown": retirement-income engine for DC funds, proven in super and sold into the UK's 2027 guided-retirement mandate

**One-liner.** A white-labelled retirement-income engine that super funds embed for members in the decumulation phase. It covers stochastic drawdown, Age Pension and means-test integration, longevity pooling and annuity blending, and AI-guided "personal advice-lite" within the scope of intrafund and Delivering Better Financial Outcomes (DBFO) advice. Funds pay per retiree or per licence. After that come UK master trusts, which must offer default retirement solutions.

**Why now (2026).**
- **Australia:** Retirement Income Covenant (2022); in Feb 2026 Treasury released a Retirement Reporting Framework and Best Practice Principles for retirement income solutions, with regulations from 1 Jul 2026 enabling new product types (instalment, money-back guarantees) [verified: Treasury ministers' release 23 Feb 2026]. Decumulation is exempt from the performance test for now [verified: Investment Magazine May 2026]. The baby-boomer wave means ~A$1T+ shifting into the retirement phase over the decade [estimate].
- **UK:** the Pension Schemes Act 2026 obliges DC trustees to offer default pension benefit solutions. Master trusts start in **2027**, group personal pensions and single-employer schemes in 2028; longevity protection is a core DWP expectation [verified: Corporate Adviser, Lexis, WTW; one source says 2029, so treat timing as uncertain].

**Unfair inputs.**
- **Fit:** stochastic modelling, longevity and sequencing risk are textbook statistician territory; LLM agents for guided conversations are his hands-on strength.
- **BCG/CFO credibility** with fund executives.
- **Weak spots:** no financial-advice licence experience; it's a crowded field of in-house fund teams, consultants (Milliman, Mercer), product providers (Challenger, Allianz Retire+) and adviser-AI startups (Marloo's A$10M seed led by Blackbird [verified: financialit.net]).

**Market & model.**
- *AU:* ~2.5–3M members aged 60+ in APRA funds [estimate]; A$3–8 per retiree per year, or A$0.3–1.5M per fund licence → **~A$10–25M ARR ceiling AU**.
- *UK:* master trusts, then GPPs → a similar or larger market from 2027–29 [estimate].
- *Comparables:* Income Lab (US, adviser tool), Guiide (UK), Smart Pension (UK master-trust tech; raised >US$400M historically) [unverified figures].

**Capital & structure.** VC seed A$3–4M. Founder ~30–40% at exit. Possible strategic investor (a fund or annuity provider) at the cost of neutrality.

**Outcome distribution (10 yrs, A$).**

| Outcome | P | Founder wealth |
|---|---|---|
| Fail | 45% | A$1.2M |
| Modest | 30% | A$3.0M |
| Good | 18% | A$8M |
| Great | 7% | A$25M |

**EV ≈ A$4.6M; median ≈ A$3.0M.**

**Time to replace $500k.** 4–5 years (VC salary ~A$250k earlier). Discovery can happen while employed.

**Job satisfaction.** Good: meaningful (people's retirement), modelling plus product. But it's slow enterprise selling into risk-averse funds, and much of the work is compliance wording.

**Key risks.**
1. **Large funds build in-house.** AustralianSuper and ART have teams; the engine becomes a feature.
2. **Advice-law perimeter:** DBFO tranche 2 timing and the scope of the new adviser class are unclear [unverified]; a wrong call means you need an AFSL.
3. **UK timing slips** (2027 vs 2029), and UK buyers want local players.

**90-day test.**
- Pitch to 10 mid-tier funds (A$20–100B, without in-house build capacity).
- **Proceed if:** ≥2 commit to a paid pilot ≥A$100k, and one UK master trust takes a discovery call.
- **Kill if:** funds say "our consultant already provides this."

---

## Idea 4: "Apportion": multi-sector scam-liability evidence and apportionment platform under the Scams Prevention Framework

**One-liner.** A shared evidence ledger and decision engine for scam cases that cross banks, telcos and digital platforms. It records each regulated entity's "reasonable steps", scores contribution to loss, and produces AFCA-ready apportionment files. It also automates actionable scam-intelligence reporting under the Scams Prevention Framework (SPF). Mid-tier banks, mutuals, MVNO telcos and digital platforms pay per case or per seat. After that come the UK (APP reimbursement), EU (PSR, which shares liability with platforms) and Singapore (Shared Responsibility Framework).

**Why now (2026).**
- The SPF Act passed Feb 2025.
- Draft common, bank, telco and digital-platform codes and rules were released 28 May 2026, with full effect slipping to **31 Mar 2027** [verified: Ashurst, HSF Kramer, Treasury].
- In-scope entities had to join AFCA by 1 Sep 2026; AFCA is the single dispute scheme across all three sectors [verified: ASIC].
- **Multi-sector liability with one external dispute-resolution scheme is a world first.** The UK's regime is bank-to-bank.
- 2025 scam losses: A$2.18B, up 7.8% [verified: ACCC/NASC Targeting Scams 2025].

**Unfair inputs.**
- Statistics/ML for loss attribution; CFO view of provisioning and reimbursement liability; first-principles regulatory reading.
- **Weak spots:** no fraud/telco network; the incumbent utility AFCX already runs the intelligence loop with banks, telcos and platforms [verified: iTnews, Treasury]; global fraud platforms are well funded (BioCatch, majority-bought by Permira at **US$1.3B**, ~US$100M revenue [verified: Permira, TechCrunch; revenue an estimate]).

**Market & model.**
- ~60–100 regulated banks/ADIs, ~30–80 telcos/MVNOs, ~10–20 digital platforms in scope.
- A$50–500k/yr each → **AU ceiling ~A$10–20M ARR** [estimate].
- Global follower markets are larger, but there incumbents (BioCatch, Featurespace/Visa [price unverified], Mastercard) own the bank side.

**Capital & structure.** VC seed A$2–4M; founder ~30–40% at exit.

**Outcome distribution (10 yrs, A$).**

| Outcome | P | Founder wealth |
|---|---|---|
| Fail | 55% | A$1.1M |
| Modest | 25% | A$3.0M |
| Good | 14% | A$8M |
| Great | 6% | A$25M |

**EV ≈ A$4.0M; median ≈ A$1.1M.**

**Time to replace $500k.** 4–6 years; rule slippage pushes revenue to after March 2027.

**Job satisfaction.** Moderate: worthy mission, but the day-to-day is compliance workflows, legal ambiguity and selling to risk/legal teams. That's less energising for a builder.

**Key risks.**
1. **AFCX or AFCA itself becomes the shared ledger** (an industry utility beats a startup).
2. **Codes slip or soften** (already slipped 9 months).
3. **Big vendors add an "SPF module".**

**90-day test.**
- Interview 12 heads of fraud/compliance across mid-tier banks, MVNOs and platforms.
- **Proceed if:** ≥3 LOIs at ≥A$50k, and AFCX confirms it won't build apportionment.
- **Kill otherwise.**

---

## Comparison

| # | Idea | EV (10-yr, A$) | Median | P(beat staying ≈A$3.0–3.5M) | Founder fit | Exportability |
|---|---|---|---|---|---|---|
| 1 | Mark: DC private-asset valuation | **6.6M** | 3.5M | ~45–55% | Very high | High (US/UK DC pushed into privates) |
| 2 | Reserve: battery-fleet flexibility capital | 4.1M | 1.0M | ~25% | High (arbitrage), weak (energy ops) | Medium |
| 3 | Drawdown: retirement-income engine | 4.6M | 3.0M | ~30–35% | High | Medium-high (UK 2027+) |
| 4 | Apportion: SPF liability ledger | 4.0M | 1.1M | ~25% | Medium-low | Medium |

All probabilities and values are agent estimates for comparing ideas, not forecasts. EVs carry wide error bars (±40%). Compare with rounds 1–3: the rent-roll hybrid scored ~A$3.0–3.4M over 7 years, which is roughly A$4.5–5M on a 10-year basis [estimate, rough conversion].

## Top pick: Idea 1, "Mark" (daily valuation and liquidity for private assets in DC pensions)

Why:
1. **It is the purest expression of the founder's proven edge:** pricing an unobserved asset under uncertainty, sold as a data layer to whoever owns capital. Here the capital owners are the A$4T super system, not a thin roll-broker niche.
2. **Australia genuinely leads by 3–5 years.** It's the only giant DC system already heavy in unlisted assets with daily member switching, and the regulators (APRA 2024, ASIC REP 841 Oct 2026) have made it a board-level problem. The US (EO 14330 / DOL 2026–27) and the UK are walking into the same problem. **Melbourne is an advantage**: the funds are down the road.
3. **The exit route is proven:** Burgiss went to MSCI at ~US$1.05B, and custodians, index providers and audit networks are natural acquirers. Even a modest outcome sells.
4. **Cheap, sharp kill test:** the 90-day proof turns on whether one fund shares data and whether the model beats the stale marks.

**Bold alternative:** if he wants Fulfilio-style physical arbitrage and is willing to accept a ~55% failure rate for a big upside, Idea 2 is the one, but only after its NEM-revenue backtest and an OEM API check pass.

**Ranked list**
1. **Mark** (DC private-asset valuation & liquidity engine). EV ≈ A$6.6M.
2. **Drawdown** (retirement-income engine, AU → UK 2027). EV ≈ A$4.6M.
3. **Reserve** (battery-fleet flexibility capital; bold). EV ≈ A$4.1M.
4. **Apportion** (SPF multi-sector scam-liability ledger). EV ≈ A$4.0M.

## Sources used (search summaries; verify before acting)
- APRA, Governance of unlisted asset valuation and liquidity risk management (Dec 2024); Investor Daily / Super Review coverage; ASIC REP 841 (14 Oct 2026).
- MSCI–Burgiss: Investing.com, Business Wire (Aug 2023).
- EO 14330 and DOL proposal: NAPA-net (Jan/Mar 2026), Mondaq, InvestmentNews.
- Cheaper Home Batteries: energy-storage.news; CER quarterly carbon market report, June qtr 2026; Energy Magazine (May 2026); RenewEconomy (Reposit CEO).
- Kraken spin-out: Skadden, BusinessGreen, Proactive Investors. Amber Series E: capital.com, thesaasnews.
- Treasury retirement-phase release (23 Feb 2026); Investment Magazine (May 2026); UK Pension Schemes Act 2026: Corporate Adviser, Lexis, WTW, Travers Smith.
- SPF: Ashurst, HSF Kramer (Jun 2026), Treasury release 28 May 2026, ASIC SPF page. ACCC/NASC Targeting Scams 2025. BioCatch/Permira: Permira release, TechCrunch.
- Payday super: Business NSW, Hall & Wilcox. Age assurance: biometricupdate.com, Mordor/Liminal (market-size marketing figures).
