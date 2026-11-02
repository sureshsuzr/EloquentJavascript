# Vertical-SaaS Skeptic: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)

**Fatal as a standalone SaaS company; survives only as the analytical engine inside a capital vehicle (a roll-up or acquisition fund where the founder holds equity and carry), or as a maintenance-cost data asset sold to insurers.**

The biggest problem is a **thin, lumpy market**. Australia probably has only ~300–700 rent-roll transactions a year, with a median deal of ~$0.47M. Even at 100% share, deal-priced DD revenue tops out at a few million dollars nationally. The buyers who value modelled retention most (funded roll-ups, banks) are the ones most likely to build it in-house or value rolls for free. Exit comps for small Australian real-estate software are single-digit millions.

## Verdict on the software business (which product, if any, is the business, from your lens)

| Product | Verdict | One-line reason |
|---|---|---|
| **A. Rent-roll DD/valuation engine** | **Keep as the wedge, kill as the company** | It is a feature attached to a transaction. It is how you get deal flow, data and credibility, but its revenue ceiling is ~$0.5–2M/yr in Australia and New Zealand. |
| **B. Portfolio health / retention monitoring** | **Kill** (agency version); keep a lender module only if a bank pays in a pilot | PropertyMe Insights (51+ KPIs) and MRI Agora Insights already give agencies book health in the system of record. Banks value rolls with an internal multiplier "at no cost to the client". |
| **C. Maintenance cost intelligence** | **Keep: the only moat candidate**, sold to insurers, MGAs and maintenance platforms, not to agencies | Conditional on contractual rights to pool data across agencies. Tapi, PropertyMe and Cotality (via Prime) each already sit on more job data than you will. |
| **D. Agentic DD / integration tooling** | **Kill as a product**; keep as internal tooling | It is bespoke services work. PropertyMe's AiMe Connect (MCP, Oct 2026) lets any vendor or acquirer query its own ledger with Claude or ChatGPT, which commoditises the "ask the data" layer. |

From my lens, **the business is A+C feeding a principal position**: a data-led acquirer or the operating partner to a roll-up fund. That matches round 2's revised thesis. The software is the moat inside the business, not the business.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

**1. Transaction volume is too small and lumpy for SaaS (High).**
- Real Estate Dynamics, one of the largest eastern-seaboard rent-roll brokers, sold **101 rolls in FY2020/21**, with 1,292 properties transferred in Victoria in 2021–22 through its book [verified: Elite Agent / RED report summaries via search].
- Pendium Advisory cites "700+ rent rolls sold or consulted on" **cumulatively** [verified: Pendium site via search].
- Median eastern-seaboard roll value is ~$470k and average size ~309 properties [verified: RED data via search, 2021–22; stale].
- National volume is therefore ~300–700 deals/yr [estimate: brokered volumes plus unbrokered private deals], and Victoria ~60–150.
- At $5–15k per DD, the national revenue pool for A is **~$1.5–10M at 100% share**. A realistic 15–30% share gives ~$0.3–2M.
- **Cyclicality:** volume rises with retiring principals and cheap debt, and drops when banks tighten. Revenue arrives in clumps around the Feb–Jun selling season.

**2. Buyers price on multiples because the contract already handles retention risk (High).**
- Round 1 found standard deals already defer 25–40% of the price, paid per retained management at 6 and 12 months, with holdback adjustments.
- The market has **hedged retention by contract, not by data**. Your model's incremental value is only the residual risk: post-holdback losses (months 3–9 and later) and fee-quality errors. That residual is much smaller than "5 points ≈ $100k on a $2M roll".
- That $100k figure is a one-year, 5-point loss on ~$2M ≈ $100k [verified arithmetic], and it is gross of the clawback protection buyers already get.
- Typical buyers are the agency next door paying ~$470k, with a broker paid by the vendor and a lawyer/accountant doing DD. A $10k analytics fee is ~2% of price on top of DD they already think is enough.

**3. Lenders don't need you and won't pay much (High for B; Medium for A).**
- **Macquarie** sets rent-roll value with an "internal Macquarie Multiplier, at no cost to the client", lends to 70% and requires amortisation to 60% within 3 years [verified: Macquarie commercial lending guide via search; undated].
- **NAB** lends at 70% LVR (flyer, 2024) or up to 80% (current page), with a 2.5x interest-cover minimum and a 100-property minimum [verified: NAB pages via search; conflicting figures, confirm with NAB].
- Banks manage risk through LVR, amortisation and interest cover, not prediction. Australia probably has ~2,000–5,000 rent-roll facilities across all lenders [estimate: ~10k+ PM agencies, a minority leveraged]. At $500–1,500 per facility per year, covenant monitoring is a **$1–7M pool if every lender bought**, and the sale cycle into the big four is 12–24 months.
- **Domain's acquisition of Insight Data Solutions** (up to $159M, 2021) shows that becoming lender-required infrastructure is valuable. But IDS sat in the **residential mortgage valuation** workflow, which runs to millions of events a year, not hundreds [verified: iTnews].

**4. Platform dependence and the copy risk is now sharper (High).**
- **EQT took majority control of PropertyMe on 4 Dec 2025**; the founders retain a minority stake. Brian Donn has been CEO since Jan 2026. PropertyMe has 6,000+ agencies, ~$40B transacted a year and 35,000 users [verified: EQT/Elite Agent/Business News Australia via search].
- A PE owner with a "global expansion" mandate is under pressure to expand revenue per agency. Book analytics, benchmarking and "rent-roll value" are obvious paid tiers.
- PropertyMe screens API partners: they need "a reasonable mutual client base" and "significant business benefit to PropertyMe users" [verified: propertyme.com.au/apiapplication via search; full terms not visible]. A data business that benchmarks PropertyMe's customers against each other is exactly what a platform owner keeps for itself.
- **AiMe Connect** (from 8 Oct 2026; read-only MCP; Advanced tier and above) lets agencies query live data with Claude or ChatGPT [verified: Elite Agent / Proptech Connect]. This **helps** A, because data comes from consented vendor access without partner approval. It **hurts** D and B, because a vendor can now ask its own AI "what's my landlord churn and fee leakage".
- **Cotality** (CoreLogic AU, rebranded Mar 2025) has PM tools (RiTA, Plezzel, Investment Reports) and acquired **Prime Ecosystem** (Jan 2025), a contractor/maintenance platform. That puts a maintenance job-data player inside the incumbent data monopoly [verified: Cotality NZ page, Business Wire via search; Prime's scope unverified].

**5. The customers who value this most will build it themselves (High).**
- In the UK, **Dwelly** raised ~£69M (Feb 2026) and ~US$170M of debt plus equity (Jul 2026). It made six lettings acquisitions in 2026 and manages 10k+ properties [verified: Goodwin, The Negotiator, PIE via search; figures vary by source].
- A funded roll-up treats acquisition pricing as **core IP** and hires two data scientists rather than renting yours. Your best customers are a handful of concentrated buyers, each a build-vs-buy risk, which is a classic feature-not-company trap.
- The Australian equivalents would be franchise groups (Ray White, LJ Hooker, which has partnered with Ailo since Mar 2025) and any PE-backed consolidator.

**6. Exit values for niche Australian real-estate software are small (Medium–High).**
- **Eagle Software** (800+ offices) sold to PropTech Group for **$7.5M** ($4.1M cash, $3.4M scrip). PropTech Group itself sold to MRI for **$93.4M** (2023) [verified: Elite Agent / Business News Australia].
- Private SaaS with under $5M ARR trades at a median of ~**3.3x ARR**, ~4–6x for strong retention [verified only as secondary blog citations of Aventis / SaaS Capital; treat as planning range].
- At a realistic A+B+C revenue of $1.5–3M in Australia and New Zealand, the exit is **~$5–15M**. The founder forgoes ~$500k/yr pre-tax plus executive equity. Over 5–6 years that is ~$2.5–3.5M pre-tax plus foregone RSUs, so a $10M exit at 70% founder ownership only roughly breaks even, before risk.

**7. Proptech failure base rates in this exact segment (Medium).**
- **:Different** (Sydney PM software + agency) went into voluntary administration in June 2023 after a $25M Series B in 2021 led by CBA's x15ventures and Antler [verified: Business News Australia / API Magazine].
- **Yabonza** (PM startup) was liquidated in 2022 owing ~$2.5M [verified: SmartCompany].
- **Ailo** has survived but its stated headcount varies, and it pivoted toward franchise partnerships [verified: LJ Hooker partnership; headcount unverified].
- The pattern: AU PM-tech raised venture money against a small TAM and couldn't make venture returns. Don't raise VC for A or B.

**8. Services creep and founder over-engineering (Medium).**
- Each DD is bespoke: different ledgers, fee schedules, trust-account quirks and missing landlord data. Gross margin will look like consulting (40–60%) for the first ~50 DDs [estimate].
- A statistician's instinct is a pooled survival model. But one roll gives ~30–45 landlord-loss events a year (309 properties × 10–14% churn) [estimate]. **The model needs dozens of rolls with post-sale outcomes before it beats a 5-variable heuristic**: fee rate, landlord tenure, multi-property owners, arrears share, recent rent-increase gaps.
- Until then, the "model" is a well-structured checklist. That is valuable, but it isn't defensible IP.

**9. Maintenance data (C) is less proprietary than round 2 assumed (Medium).**
- Agencies' invoice histories exist in PropertyMe, Tapi, Cotality/Prime and trade platforms. Those firms see **cross-agency** volumes that a single consultancy won't.
- Your edge is modelling, not data, unless you sign data-pooling rights first.

## Things the brief gets wrong, misses or understates

- **"Incumbents price on rule-of-thumb multiples"**: true, but the multiples are paired with retention clawbacks, and banks use proprietary multipliers (Macquarie). The gap your model closes is narrower than the brief implies.
- **Customer list A is too broad.** Vendors won't pay for an analysis that can only lower their price. Brokers will use it only if it raises price or speeds the sale, so pitch it as "pre-sale fee-leakage audit", not retention haircut. Pendium's 2026 PM/ONE talk is already about fixing under-charged fees to lift value [verified: Elite Agent 2026]. Banks value for free. The real payers are **acquirers doing >2 deals a year and roll-up funds**, which is a few dozen entities in Australia.
- **PropertyMe ownership change (EQT, Dec 2025)** is missing from the brief and changes the copy and cut-off risk.
- **AiMe Connect (Oct 2026)** is missing. It is both a data-access route and a commoditiser.
- **Victorian rental stock is flat.** RTBA held 736,352 bonds at 30 Jun 2025 (+0.6%) and ~745,000 per the minister in May 2026 [verified: RTBA annual report 2024–25; PAEC transcript]. Landlords are exiting, which means more distressed and sub-scale rolls for sale (good for deal flow) but not a growing pie.
- **Multiples data is stale.** The latest public Victorian figures I could find were RED 2021–22: Victorian multiplier $3.70, AAMI $1,132 [verified]. Round 1's 2.8–3.5x for 2026 is [unverified] against a public source. That gap is itself a product opportunity: a **published transaction index** (see Improvements).

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| Melbourne multiples ~2.8–3.5x (2026) | Latest public Vic data: $3.70 multiplier, AAMI $1,132 (RED 2021–22); broker quote $2.75–3.00 good rolls, $2.00–2.50 weaker (undated) | Partly verified, stale: Elite Agent / Real Estate Business |
| Size of roll market | RED sold 101 rolls FY21; median value ~$470k; avg 309 properties | Verified (RED via search), stale |
| National deal volume | ~300–700/yr; Victoria ~60–150 | Estimate (broker volumes × share) |
| Lenders need better valuations | Macquarie: internal multiplier, free, 70% LVR, amortise to 60% in 3 yrs; NAB: 70–80% LVR, 2.5x ICR, ≥100 properties | Verified via search (confirm current terms) |
| PropertyMe independent | EQT majority from 4 Dec 2025; 6,000+ agencies; ~$40B transacted/yr | Verified: EQT / Business News Australia |
| PropertyMe API open | Screened: needs mutual client base + "significant benefit"; terms not public | Verified (application page summary) |
| PropertyMe has analytics | Insights: 51+ KPIs across portfolio, trust, tenancies (2020 post); "sharper Insights" 2025 | Verified (feature existence), details unverified |
| AiMe Connect | MCP, read-only, Advanced tier, from 8 Oct 2026; agentic version next | Verified: Elite Agent / Proptech Connect |
| Cotality in maintenance | Acquired Prime Ecosystem (Jan 2025) | Verified headline; scope unverified |
| AU real-estate software exits | Eagle $7.5M; PropTech Group $93.4M (MRI); IDS up to $159M (Domain) | Verified |
| AU PM-tech failures | :Different VA Jun 2023 ($25M Series B 2021); Yabonza liquidated 2022 | Verified |
| UK roll-up capital | Dwelly ~£69M (Feb 2026) + ~US$170M (Jul 2026), 10k+ properties | Verified, figures vary by source |
| Small SaaS multiples | Median ~3.3x ARR under $5M | Secondary sources only |
| Victorian rental stock | 736,352 bonds (Jun 2025); ~745k (May 2026) | Verified: RTBA AR 2024–25 / PAEC |

## Improvements (concrete changes to the plan, ranked by impact)

1. **Make the founder a principal, not a vendor.** Use A as the engine for a roll-up vehicle: your own data-led acquirer (round 2) or an **operating partner** to a PE/family-office fund. Take 10–20% of the vehicle's equity or carry plus a fee. One $20–40M roll-up exit gives a founder 10–20% stake ≈ $2–8M, which beats any plausible A-only SaaS exit and needs no software TAM. *Highest impact.*
2. **Price A as a success fee, not SaaS:** 0.5–1.0% of deal value (~$2.5–5k on the median deal, $10–20k on $2M rolls) plus a retention-outcome bonus. **Put an outcome-tracking clause in every engagement:** 24 months of post-close landlord-loss data back to you. That is how a proprietary transaction dataset gets built, and nobody else (brokers, banks, PropertyMe) captures it.
3. **Publish a quarterly rent-roll transaction and retention index** (free, from your outcome dataset). The public data is stale (2021–22). Owning the reference number is how you become the de facto standard for lenders and brokers without selling to the big four first.
4. **Secure maintenance data-pooling rights before building C.** Use a contribute-to-receive benchmark (agencies get their percentile; you get pooled, de-identified rights). Sell the pooled model to **landlord insurers/MGAs and warranty/maintenance-plan providers**, the buyers with real budgets. Agencies won't pay.
5. **Ship nothing that duplicates PropertyMe Insights or AiMe.** Build on AiMe Connect and consented exports so you need no partner approval. Keep a Console/Rex/MRI export path so you are not single-platform.
6. **Hard cap on bespoke work:** a fixed-scope DD with a standard data request and a 10-business-day turnaround. Decline work outside scope.
7. **No VC for A, B or D.** Bootstrap or take angel money from acquirers or brokers, who are also distribution.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| # | Test | Metric | Continue if | Kill if | Time / cost |
|---|---|---|---|---|---|
| 1 | Paid DD pilots via 3 brokers and 5 multi-deal acquirers | Paid engagements | ≥4 paid at ≥$7.5k or ≥0.75% of price | ≤1 paid: A is a free sales tool, not revenue | 90 days, <$10k |
| 2 | **Outcome backtest:** 10+ historical rolls with 24-month post-sale retention (from brokers' or acquirers' files) | Retention MAE vs broker-graded multiple and a 5-variable heuristic | Model beats the heuristic by ≥3 points of 12-month retention | No better than the heuristic: the "edge" is a checklist; don't build a model company | 60–90 days, ~$5k |
| 3 | Deal-flow census with 3 brokers | Victorian and national roll transactions in the last 12 months | ≥100 Victoria / ≥400 national | <60 Victoria / <250 national: standalone A dead | 4 weeks, $0 |
| 4 | Lender pilot pitch to credit teams at 4 lenders (Macquarie, NAB, CBA, a non-bank) | Willingness to accept or require the report | ≥1 pilot (paid or written into the credit pack) | 0/4: drop B-for-lenders | 90 days |
| 5 | Maintenance data rights | Agencies signing pooling agreements; insurer/MGA paid study | ≥10 agencies and ≥1 insurer study ≥$25k | <5 agencies or no paid interest: C is just round 2's internal operator tool | 90 days |
| 6 | Capital-partner sounding | Term-sheet-level interest for an operating-partner role with equity | ≥1 fund or family office at ≥10% equity/carry | None: fall back to the round-2 own-acquirer route | 90 days |

## Answers to the round-3 questions in my domain

**Q1. Who pays, how much, how often; is it big enough?**
- Real payers are multi-deal acquirers, roll-up funds and possibly insurers (for C).
- A is per-deal and lumpy, ~$0.3–2M/yr in Australia and New Zealand. B is small, and the lender sale cycle is long. C could reach ~$0.5–2M/yr if insurers buy.
- Combined realistic ceiling: ~$1.5–3M revenue by year 4–5, which means a $5–15M exit [estimate]. **Not enough** to beat $500k plus executive equity on a risk-adjusted basis, **unless** it sits inside a capital vehicle where the founder owns equity in the rolls.

**Q3. What stops PropertyMe or Cotality?**
- Nothing structural. EQT ownership raises the incentive to monetise analytics. Cotality already has PM tools and a maintenance platform.
- Your only defence is data they lack: **post-transaction retention outcomes across platforms** and pooled maintenance data from non-PropertyMe agencies.

**Q4. Wedge vs moat.**
- **Wedge:** A, sold as a success-fee DD and pre-sale fee-leakage audit.
- **Moat:** the outcome-linked transaction dataset (from A's clauses) plus pooled maintenance cost data (C).
- B and D are features.

**Q6. Versus rounds 1–2.**
- Pure SaaS has lower capital at risk (~$50–200k) and higher job satisfaction (analytical work), but a low ceiling and a lumpy income.
- The operator route has a higher ceiling but $1M+ at risk and operational drudgery.
- **The dominant option is the hybrid:** analytics business plus equity in a roll-up vehicle.

**Q7. Smallest test.** Tests 1 and 2 together within 90 days. If no one pays ≥$7.5k for a DD **and** the model can't beat a simple heuristic on real outcomes, kill A as a business.

## Questions I'd hand to other specialists

- **Lawyer:** does the founder's employment contract (IP assignment, moonlighting, non-compete) permit paid DD work now? Does success-fee DD on a roll make you a "business broker" or require an estate agent licence under the *Estate Agents Act 1980* (Vic)?
- **Privacy:** can a vendor lawfully disclose landlord and tenant personal information in a DD export to you (APP 6 secondary use)? Can you keep de-identified outcome data after the deal?
- **Data/ML:** how many rolls with outcomes are needed before a pooled hazard model beats the heuristic? Check that against tests 2 and 3.
- **Insurance/actuarial:** will landlord insurers or MGAs pay for agency-level maintenance cost models, and at what data volume?
- **Capital markets:** are there Australian PE or family-office appetite and terms for a PM roll-up vehicle with an operating-partner structure, and what is the realistic exit multiple for a 3,000–5,000-management platform?
- **Platform strategist:** confirm PropertyMe's current API and partner terms under EQT, and whether AiMe Connect's terms allow third-party analytical use of agency data.
