# 13 — Finance function for resources & energy companies (Track A × Track B intersection)

Stage-1 ideation, round 2. Lens: an outcome-priced, AI-native finance function specialised for Australian resources and energy companies. 4 Nov 2026. Australian English, AUD.

Source note: 18 web searches. The BDO and actonsoftware hosts were blocked for direct fetch, so the BDO figures below come from search-result extracts of BDO pages, not the PDFs. Labels: **[verified: source]**, **[estimate]**, **[unverified]**.

---

## 1. What the vertical looks like (facts first)

**ASX explorers are a large, uniform compliance population.**
- About **747 companies lodged an Appendix 5B** in the March 2025 quarter. In calendar 2025 the number of filers changed by a net one, after a net fall of 18 in 2024 [verified: BDO Explorer Quarterly Cash Update, Mar 2025 and Dec 2025 quarters]. The population is stable at roughly 750. Underneath that, about 10–20 companies list and 10–20 leave every quarter [estimate].
- **Aggregate explorer cash was A$12.04B in December 2025 and a record A$13.04B in June 2026.** Financing inflows were A$5.62B in the December 2025 quarter and A$3.15B in the March 2026 quarter, and the average raise was A$3.82M per company in the June 2026 quarter [verified: BDO quarterly updates, via search extracts].
- The cash is very unevenly spread. In past downturns **more than 40% of explorers had one or two quarters of runway** [verified: BDO 2015 report, via search]. The 2026 share with that little runway is not public in what I could reach [unverified].
- The Appendix 5B must be lodged **within one month of quarter end**, together with the quarterly activity report. Related-party payments (items 6.1/6.2) need an explanation, and the 5B is **not audited** [verified: ASX Listing Rules ch. 5 and the Appendix 5B form]. So the filing is a standard template, done 4 times a year, with public scrutiny and no auditor backstop. That is ideal ground for AI with a human reviewer.

**The incumbent service model is "company secretary + CFO-for-hire" boutiques, mostly in West Perth, and they are consolidating.**
- **Automic** (a registry-led platform that also does company secretarial, legal and CFO advisory work for about 1,400 companies and funds) was bought by **Advent International for a reported A$725M** in September 2025 [verified: Business News; AAP]. Automic had earlier bought **Endeavour Corporate** (Perth CoSec/CFO) and **Grange Consulting** (West Perth capital raisings, CFO and CoSec) in 2023 [verified: Automic news]. Cicero Group (corporate services to ASX-listed companies) merged into Nexia Perth in 2023. Carbon Group bought The Outsource Group (Perth bookkeeping/CFO) in July 2025 [verified: Business News Australia].
- What this proves: a strategic and PE exit path exists for "back-office services to ASX small caps", and the scaled player is registry-centric and will push CFO services into its 1,400 clients. What it doesn't prove: that the CFO/CoSec layer itself earns high multiples. Automic's price is mostly about the registry.
- In many juniors, the CFO/CoSec is a **director-associated firm** (visible in 5B item 6 disclosures). Switching therefore runs into board relationships, not just price [estimate, consistent with 5B disclosures].

**Per-client economics** [estimate, triangulated from 5B admin lines and boutique pricing; no published tariff found]: a typical explorer spends A$80–250k a year on CFO/accounting, CoSec, bookkeeping, payroll, tax and audit-prep combined, or A$1–2M on all "corporate and admin". That gives about **A$80–150M a year of addressable finance and CoSec spend** across the ~750 filers, before producers, developers, mining services and energy SPVs.

**Energy SPVs are a fast-growing, long-tenor population.**
- **Capacity Investment Scheme** awards include Tender 3 at 4.13GW/15.37GWh of storage, Tender 4 at 6.6GW of generation (Oct 2025), Tenders 5/6 at 1.9GW plus 482MW/3.7GWh in WA (May 2026), Tender 7 at 7.8GW across 19 projects (May 2026) and Tender 8 at 4.2GW/16.1GWh across 15 projects (Jun 2026). Tenders 9 and 10 closed in Jul/Aug 2026 [verified: pv-tech, energy-storage.news, DCCEEW release via Enerdata]. **That is 60–70 contracted projects**, each a special-purpose entity with lender covenants, CIS agreement (CISA) reporting, NGER and certificate obligations.
- Third-party commercial asset managers already exist: **RES (over 3GW under management, "largest third-party asset manager in Australia")**, **OX2** (over 400MW, including invoicing, accounting, annual reports and bank/auditor coordination, on **10–15-year contracts**), Blueshore, CWP Asset Management and New Energy Management [verified: company sites, RenewEconomy, pv magazine].

**The compliance load is rising across the sector.**
- **AASB S2**: Group 2 reports from financial years starting 1 Jul 2026 and Group 3 from 1 Jul 2027. Group 3 is two of three of: ≥A$50M revenue, ≥A$25M gross assets, ≥100 employees [verified: Anthesis/BDO summaries; employee threshold from my prior knowledge]. Most explorers fall outside, because they have no revenue and few staff. Mid-tier producers, developers and mining-services contractors fall inside.
- **NGER**: 978 controlling corporations reported for 2024–25, and **207 Safeguard facilities** [verified: Clean Energy Regulator].
- **Critical Minerals Production Tax Incentive (CMPTI)**: a 10% offset on eligible processing costs from 1 Jul 2027 to 2040, with DISR registration and annual reporting obligations [verified: ATO; KPMG 2026]. Refundability details and the registration process are still being finalised [unverified].
- **JMEI** (Junior Minerals Exploration Incentive): companies such as Miramar still received FY25 credits. An extension was a costed Coalition election promise (A$25M a year cap) and was not in the 2025–26 Budget, so the scheme's status after FY25 is unclear [verified: PBO; Mining Weekly; Kalkine]. Don't build a business on it.

**Competing AI finance players**: Basis (US AI accounting agents, US$100M at a US$1.15B valuation, Feb 2026) and Digits (outcome-based pricing for accounting firms, Apr 2026) [verified: Crowdfund Insider; Accounting Today]. Neither has any ASX-resources specialisation. I found **no product that automates Appendix 5B and quarterly preparation** [searched; nothing found].

**Implication.** The resources vertical gives Track A three things a generic SME finance agency lacks:
1. a **standard public deliverable** (5B, quarterly, half-year, annual), so outcomes can be measured;
2. a **concentrated, referral-driven buyer community** (West Perth, Collins St, the brokers and auditors who serve juniors);
3. a **public data exhaust** (750 companies × 4 quarters × 10+ years of 5Bs) that can become a financing asset.

Its weaknesses: the clients are small, cash-starved and cyclical, and the market tops out at roughly A$100–150M of spend unless the business moves into energy and contractors.

---

## 2. Ideas generated (long list)

1. Explorer Finance Office: an outcome-priced 5B/quarterly/audit-ready finance function for juniors (**kept, A**).
2. Renewable SPV "Project Company Office": covenant, CISA, LGC and NGER back office priced per MW with service levels (**kept, B**).
3. Runway Capital: a 5B data layer plus financing origination (refund advances, small royalties, CMPTI monetisation) (**kept, C — bold**).
4. METS contractor cash-conversion: a finance function for mining-services contractors priced on DSO and recovered claims (**kept, D**).
5. AASB S2/NGER "assurance-ready" report factory for Group 2–3 miners and contractors (folded into A/D as a module; a crowded Big 4/Anthesis field).
6. JV and farm-in accounting utility (cash calls, operator billing audits): too narrow alone; a module of A.
7. Buy a West Perth CoSec boutique and AI-rebuild it: a distribution tactic for A, not a standalone idea (and the brief rules out generic roll-ups).
8. Rehabilitation-provision estimator and bond pricing for juniors and contractors: interesting, but a Track B underwriting play; noted as a bridge.
9. Placement and capital-raise back office (bookbuild reconciliation, Appendix 2A/3B, cleansing notices): a module of A.
10. Lithium/nickel care-and-maintenance "hibernation CFO": cyclical, and folded into A.

---

## 3. Idea A — Explorer Finance Office (top pick)

| Field | Assessment |
|---|---|
| **One-liner** | An AI-native finance and company-secretarial function for ASX explorers and pre-production developers: ledger, payroll, BAS, 5B and quarterly, half-year review and annual audit packs, JV cash calls, R&D/JMEI claims, ASX lodgements. **The client pays** a fixed quarterly fee by complexity tier (A$6–25k a quarter). **The outcomes priced:** 5B and quarterly lodged by day 20 with no finance-caused ASX query; audit and review with no material adjustments (fee credit if missed); a corporate-finance cost ceiling (e.g. ≤4% of exploration spend, or fee credit); a success fee of 10–15% on R&D refunds and incentives recovered. |
| **Why now (2026–28)** | (1) Since 2025, LLM agents can reliably read bank feeds, drill invoices and JV statements and draft 5B/MD&A text. The 5B template is fixed and unaudited, so a human-reviewed AI draft is low-risk. (2) Explorers hold record cash (A$13B) and are spending it, so the volume of transactions is rising. (3) Consolidation: Automic sold to Advent, and Grange and Endeavour were absorbed, which leaves boutique clients with a mid-sized vacuum and staff churn. (4) The CMPTI (from FY28) and AASB S2 (FY27–28) add new reporting for developers moving into processing. (5) Shareholders and activists increasingly attack "admin as % of spend". A guaranteed overhead ceiling is a board-level selling point. |
| **Why Australia / Melbourne** | The ASX is the world's densest junior-explorer exchange (about 750 5B filers). Melbourne has a real but smaller cluster (Collins St juniors, the Melbourne Mining Club, VIC/NSW gold and critical-minerals juniors). **Handicap:** the centre of gravity is West Perth, where relationships and director-linked CoSec firms dominate. Mitigation: a Perth-based co-founder from day 1. An AI-native delivery model is location-agnostic for everything but the board meeting. |
| **Unfair inputs** | The founder's CFO craft (close, audit, board reporting) and statistician/CS skills (agentic pipelines and QA sampling) map directly. His marketplace background helps with referral loops (brokers, auditors, lawyers). **Gaps:** ASX listing-rule and CoSec credibility, and resources accounting (AASB 6 exploration and evaluation assets, JV accounting). **Co-founder profile:** a Perth-based chartered accountant and CoSec with 10–15 years in juniors, who currently services 10–20 listed companies and brings 3–8 of them. Offer 15–25% equity. |
| **Market & model** | About 750 explorers plus about 100 developers and small producers. Core spend is A$80–150M a year [estimate]. Target: 60 clients by year 3 and 150–200 by year 7, at A$70–110k a year each, for **A$12–20M revenue**. With AI handling about 70% of preparation, one reviewer-accountant can cover 15–20 clients (boutiques manage 6–10), so gross margin is 55–65% and EBITDA 25–35% at scale [estimate]. **Comparables:** Automic at A$725M (registry-led, 1,400 clients) [verified]; boutique CoSec/CFO firms trade at about 0.8–1.5x revenue [estimate]; AI-accounting venture comparables are Basis (US$1.15B) and Digits [verified]. |
| **Capital & structure** | Bootstrappable. A$0.3–0.6M of founder capital covers the build plus the first 2 hires. Optionally, buy one small West Perth book (10–20 listed clients, A$1–2M revenue at about 1x revenue, funded by vendor finance plus an earn-out) as distribution. Founder ownership 55–70% after the co-founder and an ESOP. Raise only if layering on Idea C. |
| **Floor and failure mode** | The floor is a profitable services practice: even 25 clients at A$80k is A$2M revenue and A$0.4–0.6M profit, which a Perth accounting firm would buy. **Failure modes:** a director-linked incumbent blocks switching; a junior bear market cuts client count and pricing at the same time (2012–16 style); one high-profile ASX error damages trust. P(total loss) is about 12%, and the loss is limited to roughly A$0.4M plus forgone salary. |
| **Outcome distribution (10 yrs)** | Founder equity: total loss 12% (~A$0.2M); modest 43% (A$1.5–4M, say A$2.5M); good 37% (A$8–20M, say A$12M; 150 clients, A$15M revenue, sold to a registry/PE platform or an accounting network); great 8% (A$40M+; becomes the resources back-office platform, adds Idea C, sells to Advent/Automic, Computershare, MUFG or PE). **EV ≈ A$8.7M; median ≈ A$3.5M; P(positive outcome) ≈ 55%**, counting about half the modest band because salary of A$150–250k a year from year 2 is taken. |
| **Cash generation** | Cash-positive at about 15–20 clients (month 12–20). It funds its own growth from there: fees are quarterly in advance and there are no receivables problems with prepaid tiers. |
| **AI leverage** | High and getting stronger as models improve. 5B preparation, variance commentary, AASB 6 capitalisation tests, JV cash-call reconciliation, related-party flagging and listing-rule checks (ASX query triggers) are all pattern work on a fixed template. Outcomes are measurable (lodgement date, ASX queries, audit adjustments), so they can be priced. Each client adds labelled data (what auditors adjust, what ASX queries), which becomes a QA model competitors lack. |
| **Job satisfaction** | Building agentic finance pipelines and selling to boards. The domain is varied (gold, lithium, uranium, JVs, capital raises), with a front-row seat to the junior capital market, which feeds Idea C. Some grind: four reporting peaks a year. |
| **Key risks** | (1) Relationship lock-in to director-associated CoSec firms; mitigate with the Perth co-founder and a book purchase. (2) Cyclicality: a commodity downturn cuts clients and price; mitigate by adding developers, energy SPVs (B) and contractors (D). (3) Automic/Advent bundles AI CFO services into 1,400 registry clients at cost. |
| **90-day test** | (a) Build the 5B data set: parse the last 8 quarters of 5Bs for all ~750 filers (public PDFs) and publish a free "overhead & runway benchmark" to 150 MDs/CFOs. **Pass:** ≥40 request their own benchmark. (b) Run 25 discovery calls. **Pass:** ≥40% say they would switch at equal or lower cost with the lodgement and audit guarantees, and ≤60% cite a director-linked provider as the blocker. (c) Sign **3 paid pilots** (one quarter's 5B, quarterly and half-year pack at A$5–8k each), delivered by a contract CA under founder supervision. **Kill** if fewer than 2 pilots, or if AI-assisted preparation takes more than 50% of boutique hours. **While employed:** yes for (a) and (b), and (c) with a contractor. Disclose to the employer; no conflict with SaaS. |

---

## 4. Idea B — Renewable SPV "Project Company Office"

| Field | Assessment |
|---|---|
| **One-liner** | An AI-native financial and compliance back office for renewable and storage project companies (CIS-contracted wind, solar and BESS SPVs, and developers before financial close). Covers SPV accounting, lender covenant certificates (DSCR, reserve accounts), CISA revenue-floor/ceiling settlement reporting, LGC creation and sale reconciliation, NGER, distributions and audit. **The client pays:** the owner/sponsor, per MW per year (A$1.5–3k/MW) [estimate]. **The outcomes priced:** covenant and CISA reports delivered by day N with no lender query; zero unreconciled certificate variance; audit with no adjustments; service credits for misses. |
| **Why now** | About 30GW of CIS awards across tenders 1–8 [verified sum from tender reports, approximate] create 60–70+ new SPVs reaching financial close and operations in 2026–30, each with CISA payment mechanics that are new and data-heavy. AASB S2 Group 2/3 reporting rolls up from these SPVs to their sponsors. Many sponsors are offshore IPPs that want local outsourcing. |
| **Why Australia / Melbourne** | Victoria and NSW host many CIS/REZ projects, and Melbourne is home to sponsors and financiers (CEFC, super funds, IFM). This is an advantage, not a handicap. |
| **Unfair inputs** | CFO plus stats skills fit covenant modelling and settlement reconciliation. **Gap:** renewables commercial asset management (PPAs, AEMO settlement, LGC registry). **Co-founder:** an ex-RES/OX2/Tilt or Edify commercial asset manager. Needs a technical asset management partner for full-service bids. |
| **Market & model** | If the CIS pipeline plus existing merchant assets puts about 15–25GW under some form of outsourced commercial and financial management by 2032, then at A$2k/MW that is A$30–50M a year [estimate]. Target 3–5GW gives A$6–12M revenue at 30–40% EBITDA. Contracts run **10–15 years** (OX2 model) [verified], so the business is annuity-like. **Comparables:** RES, OX2, Blueshore and CWP [verified]. |
| **Capital & structure** | A$0.5–1M of founder capital plus possibly a strategic partner (a technical O&M firm or a CEFC-backed platform). Founder 50–65%. |
| **Floor and failure mode** | Long contracts give a good floor once 1–2GW is signed. The risk is the cold start: nobody gives a 300MW SPV to a firm with no track record. **Failure mode:** stuck at 2–3 small clients. P(total loss) about 15%. |
| **Outcome distribution** | Total loss 15% (A$0.2M); modest 40% (A$2M); good 35% (A$10M); great 10% (A$35M; sold to a global asset manager or a super-fund platform). **EV ≈ A$7.8M; median ≈ A$3M; P(positive) ≈ 52%.** |
| **Cash generation** | Slower to start (12–24-month sales cycles), then cash-positive at about 1GW (year 2–3). Very stable afterwards. |
| **AI leverage** | Strong: settlement data, AEMO dispatch, PPA invoices and covenant models reconcile automatically. Monitoring generation against forecast is the **bridge to Track B** (pricing availability guarantees, revenue floors, warranty-backed finance). |
| **Job satisfaction** | Good: the energy transition, statistical modelling and financier relationships. Less variety than A. |
| **Key risks** | (1) Incumbents bundle financial services into technical asset management at cost. (2) Sponsors keep it in-house once they reach 1GW+. (3) Slow sales cycle versus the founder's runway. |
| **90-day test** | Interview 15 sponsors and developers with CIS awards from Tender 4/7/8. **Pass:** ≥3 identify an unmet need for CISA/covenant reporting, and ≥1 signs a paid pilot for one SPV's quarterly lender pack (A$15–30k). Can start while employed, slowly. |

---

## 5. Idea C (bold) — Runway Capital: junior-resources data layer → financing and royalty origination

| Field | Assessment |
|---|---|
| **One-liner** | A structured, continuously updated data set of every explorer's cash, burn, overhead, related-party payments, raise history and runway (public 5Bs, plus deeper ledger data from Idea A clients who consent). It is used to **originate and price capital**: (1) advances on R&D refunds, JMEI and (from FY28) CMPTI offsets; (2) small royalties and NSRs (A$0.3–5M) bought from juniors on non-core tenements or advanced projects; (3) short bridge or convertible notes timed to the financing calendar. **Who pays:** borrowers and royalty sellers (pricing spread and royalty yield); later, LPs pay management fees and carry. **The outcome priced:** the probability of the next raise and of reaching production. |
| **Why now** | Record but uneven explorer cash means a two-tier market. Royalty consolidators are hungry for Australian royalties: Vox's binding Australian copper/gold portfolio deal (Aug 2026) and its NSW gold royalty (up to A$650k), Latitude 66's royalty portfolio sale (Aug 2026), Elemental Altus–EMX (Sep 2025) and Elemental–Vizsla (A$239M, May 2026) [verified: search results; deal details partly unverified]. That gives an **exit market for aggregated small royalties**. The CMPTI creates a new refundable-offset-like asset class from FY28 [refundability unverified]. |
| **Why Australia / Melbourne** | The world's densest junior market plus a statutory incentive regime; Melbourne has family-office capital. No handicap beyond Perth relationships. |
| **Unfair inputs** | This is the founder's strongest edge: pricing and underwriting under uncertainty, data layers and capital raising. **Gaps:** a resources geologist/technical due-diligence partner and credit structuring. **Co-founder:** an ex-royalty company or resources-banking investment professional (Taurus, Tembo, Macquarie MCG). |
| **Market & model** | Explorers raise about A$13–20B a year in equity [verified quarterly figures annualised]. Even 0.5% as royalty or non-dilutive finance is A$65–100M a year of deal flow [estimate]. Model: start with A$5–10M of SPV and family-office money deal by deal (2% fee, 20% carry, plus origination fees), then a A$75–150M fund by years 4–5. Royalty portfolios are sold to Vox, Elemental, Deterra and others at a premium to entry [estimate]. |
| **Capital & structure** | GP economics plus co-investment. The founder puts A$0.3–0.5M into the first deals. Founder GP ownership 50–60%. Needs an AFSL or authorised-representative arrangement and wholesale-only investors. |
| **Floor and failure mode** | Refund advances are secured on ATO receivables, a strong floor. Royalties are "hard" contracts, but most early-stage royalties never pay out. **Failure modes:** adverse selection (only juniors that can't raise equity come to you); data that public 5Bs already make free; a downturn that hits portfolio value just as LPs want out. P(total loss) about 28%. |
| **Outcome distribution** | Total loss 28% (A$0.2M); modest 37% (A$2M); good 25% (A$12M); great 10% (A$50M; a listed royalty vehicle or a fund franchise). **EV ≈ A$8.8M; median ≈ A$2M; P(positive) ≈ 42%.** |
| **Cash generation** | Fee income from deal one, but small. Not self-funding until a fund exists (years 3–5) unless paired with A. |
| **AI leverage** | Very high. Parsing 30,000+ historic 5Bs and quarterlies plus drill results, then modelling raise probability and survival. The model improves with every quarter and every closed deal. The data asset compounds. |
| **Job satisfaction** | Highest of the four: underwriting, deal-making and markets. |
| **Key risks** | (1) Adverse selection and mispriced geology. (2) Licensing and fund-raising friction. (3) The exit market for small royalties is thinner than the headlines suggest. |
| **90-day test** | Build the 5B survival model (shared with Idea A's test). Back-test whether it predicts the next raise or a delisting at least 2 quarters ahead (**pass:** AUC ≥0.75 versus a naive cash/burn ratio). Pitch 10 family offices on a A$3M first-loss SPV for refund advances. **Pass:** ≥A$2M soft-circled and ≥3 live origination leads. Can start while employed (it is analysis), but no lending until he has left. |

---

## 6. Idea D — METS contractor cash-conversion finance function

| Field | Assessment |
|---|---|
| **One-liner** | An AI finance function for mining-services and METS contractors (drilling, civil, labour hire, maintenance; A$10–150M revenue): WIP and progress claims, variation and claim recovery, collections against tier-1 miners' payment terms, payroll and award compliance, AASB S2 for Group 3. **The client pays:** a base fee plus an **outcome share**, e.g. 10–20% of the cash value of DSO reduction or of variations recovered above baseline. |
| **Why now** | Majors stretch payment terms; contractor margins are thin and insolvencies frequent; AASB S2 Group 3 starts FY28 for larger contractors [verified thresholds]; AI can now read contracts, timesheets and site dockets to price claims. |
| **Why Australia / Melbourne** | WA/Qld-centric; Melbourne has some contractors (Downer, Ventia, smaller civil firms). Moderate handicap. |
| **Unfair inputs** | CFO and working-capital expertise; Fulfilio ops background. **Gap:** construction-contract and claims expertise. **Co-founder:** an ex-contractor commercial manager or quantity surveyor. |
| **Market & model** | Hundreds of mid-sized contractors [estimate]. A$150–400k a year per client including the outcome share. Target 40 clients gives A$8–12M revenue. Optional receivables or claims finance later. |
| **Capital & structure** | Bootstrappable; founder 60–70%. |
| **Floor and failure mode** | A profitable outsourced finance practice. Outcome shares are disputable, so there is billing friction. P(total loss) about 15%. |
| **Outcome distribution** | Total loss 15%; modest 45% (A$2M); good 32% (A$9M); great 8% (A$30M). **EV ≈ A$6.2M; median ≈ A$2.3M; P(positive) ≈ 48%.** |
| **Cash generation** | Cash-positive in years 1–2. |
| **AI leverage** | Good: contract-clause extraction, claim pricing, DSO prediction. Measurement is clean (cash collected). |
| **Job satisfaction** | Medium: practical, but commercially adversarial and with less data elegance. |
| **Key risks** | (1) Clients churn when cash pressure eases. (2) Disputes over outcome-share attribution. (3) Construction-claims consultants and ERP vendors (e.g. construction-specific ERPs) encroach. |
| **90-day test** | Run a free DSO and variation diagnostic for 5 contractors. **Pass:** ≥A$500k identifiable cash at 2 of them, and 1 signed outcome-share engagement. |

---

## 7. Does the vertical give a better wedge than generic Track A?

**Yes, modestly, and mostly because of measurability and data, not market size.**
- **Better wedge:** a uniform, public, deadline-driven deliverable (5B/quarterly) makes outcome pricing credible from day one. A generic SME finance agency has to invent its KPIs. The referral network is tight: about 10–15 audit firms, 20 brokers and a handful of law firms serve most juniors.
- **Data asset:** yes. The 5B corpus is public but unstructured. Combined with consented ledger data, it supports Idea C (financing and royalty origination). No generic finance agency has that.
- **Bridge to Track B:** A → C (underwriting juniors' outcomes: reaching production, royalties). B → Track B performance-finance products (availability, revenue floors). The bridge is real but takes 3–5 years.
- **Against:** market spend is capped at about A$100–150M in juniors; the clients are cyclical and cash-poor; Perth relationship lock-in; the scaled incumbent (Automic/Advent) has PE money behind it. A pure-junior play is a solid A$10–20M-revenue business, not a A$100M+ one, unless it expands to energy SPVs and contractors or monetises the data through C.

---

## 8. Top pick and ranking

**Top pick: A — Explorer Finance Office, sequenced as A → C.** Start as an outcome-priced AI finance and CoSec function for ASX explorers. It can be tested while employed, cash-positive within about 18 months, and has a sellable services floor. Build the 5B survival model in the same 90 days, because it doubles as A's sales tool (the free benchmark) and C's underwriting engine. Turn on Runway Capital (refund advances, then small royalties) once A has 40+ clients and 8+ quarters of ledger data. Add B as a second client segment if a renewables co-founder appears.

| Rank | Idea | EV (founder equity, 10 yrs) | Median | P(positive) | P(total loss) |
|---|---|---|---|---|---|
| 1 | A — Explorer Finance Office (→ C) | ~A$8.7M | ~A$3.5M | ~55% | ~12% |
| 2 | B — Renewable SPV Project Company Office | ~A$7.8M | ~A$3M | ~52% | ~15% |
| 3 | C — Runway Capital (bold) | ~A$8.8M | ~A$2M | ~42% | ~28% |
| 4 | D — METS contractor cash-conversion | ~A$6.2M | ~A$2.3M | ~48% | ~15% |

The distributions are stage-1 estimates using the brief's base rates (great outcome 8–10%, not 12%+). C has the highest EV but the lowest P(positive). A dominates on the brief's objective (high probability of a positive outcome, cash generation, a floor) and carries C as an option.

**Critical uncertainties to resolve first:** (1) how many juniors' CFO/CoSec roles sit with director-linked firms (from 5B item 6 disclosures in the 90-day data build); (2) real per-client fees (ask 10 juniors; no published tariff found); (3) whether Automic/Advent is already bundling AI CFO services; (4) the status of JMEI beyond FY25 and CMPTI refundability and registration.
