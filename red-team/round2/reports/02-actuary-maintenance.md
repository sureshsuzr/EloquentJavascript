# Actuary & Insurance-Product Designer: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**As written (operator takes on repair-cost variance for a flat fee, split with the tenant): fatal on two counts.** First, a third party promising to fix breakdowns for a fixed fee is very likely **insurance in kind**. Without APRA authorisation that is an offence under the Insurance Act, and without an AFSL it is a financial-services breach. Second, the tenant split is unlawful in Victoria unless it is passed through rent.
**Survives-if** it is rebuilt as a **non-risk "maintenance reserve + preventive plan"** sold at cost-plus. Any true risk transfer should come later, from an insurer's product that the agency distributes, priced from the acquired agency's own invoice history.
**Biggest issue:** the danger is not variance. At 500 properties, process risk is about 5% of expected cost. The danger is **adverse selection plus parameter error**: old, run-down houses opt in, and a 20% pricing miss costs about $170k a year at 500 properties. A risk-bearing plan is a small-margin product (about $100–300 per policy) carrying capital risk worth more than the founder's whole personal limit. It is not an economics carrier.

## Verdict on the platform thesis (which services carry the economics, from your lens)
- **Carries economics: no risk-bearing product.** The two products that do pay are distribution plays with no balance sheet behind them: (1) **maintenance coordination at cost-plus** (a transparent coordination fee plus a preventive plan), which earns money from trade density and service quality rather than from underwriting; and (2) **distributing insurers' landlord/rent-default products** as an authorised representative, with commission treatment confirmed against s 48A first.
- **The flat maintenance fee** works as a retention and data product. Its value is lower churn, which round 1 identified as the master variable, plus a cost model that feeds the investment-advice product. Its standalone margin is small and its tail risk is large.
- **Rent guarantee / arrears product:** an agency-issued guarantee of rent is insurance. The lawful, cheap version is a **guarantee on your own service** (letting-fee refund and free re-let if a tenant you placed is evicted for arrears within 12 months). It costs about $15–30 per property per year and markets the tenant-evaluation product. Lost rent itself should be left to insurers.
- **Order:** (1) mine the acquired ledger for 3 years of invoices (month 0–3); (2) cost-plus preventive plan and maintenance reserve (month 4–12); (3) authorised-representative distribution of insurer landlord/rent-default cover; (4) only beyond about 3,000 properties with 3+ years of own data, a binder/MGA arrangement with an insurer's capacity. A captive is a 10,000+ property question, not a 2027 one.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)
1. **It is insurance (High).** In Australia, carrying on insurance business needs APRA authorisation, and insurance contracts are financial products (Corporations Act s 764A(1)(d)). ASIC says a third-party warranty provider "is likely to need an AFS licence", and that the s 763E incidental-product exemption "does not apply when the extended warranty is a general insurance product" and generally won't apply to third parties with no interest in the goods [verified: ASIC extended-warranties guidance page]. The UK Supreme Court treated breakdown-repair warranties, repaired in kind, as insurance (*Re Digital Satellite Warranty Cover*, 2013) [verified: HSF commentary; persuasive only]. The agency has no interest in the landlord's hot-water unit, so the plan is a fixed premium for a fortuitous breakdown, indemnified in kind. A lawyer would have to show that the dominant obligation is service and that the risk element is incidental. That argument weakens with every uncapped replacement the plan promises. If it is insurance, Victorian insurance duty (about 10%) [unverified: SRO Vic rate as I understand it] plus GST also land on the premium.
2. **The tenant split is unlawful (High).** The rental provider must keep the premises in good repair. Urgent repairs: the renter may arrange them up to $2,500 and must be reimbursed within 7 days of written notice. Non-urgent repairs: 14 days [verified: CAV urgent/non-urgent repairs pages; Tenants Vic]. The Act prohibits charges to renters beyond rent and bond (ss 51, 51A as amended) [verified: CAV / Tenants Vic summaries; exact current numbering unverified]. The 2025 Housing Reform Act adds bans on fees charged through third-party platforms [verified: CAV summary; commencement around 25 Nov 2025, check status]. Bond replacements and guarantees that a renter pays for are illegal in Victoria [verified: CAV "Illegal bond replacements"]. Making a renter pay towards the landlord's statutory repair duty is a prohibited charge if required, and is exposed even if called "optional". **The only lawful split is economic, through the advertised rent.**
3. **Adverse selection is structural (High).** Landlords know their asset (age of hot-water unit, roof, slow drain) far better than any rating cell does. Under opt-in at a cell-average price, the worst properties join. Round 1 already found "a maintenance cap attracts old stock". Because the Victorian minimum energy standards start on 1 Mar 2027 (heater failure triggers an efficient replacement; ceiling insulation required at a new lease), landlords will want to buy the plan just before a known capex event [verified: CAV/Energy Vic guidance].
4. **Moral hazard runs three ways (Med).**
   - *Landlord:* stops replacing at end of life and lets the plan carry it.
   - *Tenant:* already reports at zero cost, so little changes, except that renter-caused damage gets relabelled as wear.
   - *Operator:* this is the serious one. As the landlord's agent, the PM must act in the principal's interest. As the risk bearer, it profits from patching rather than replacing and from slow-walking repairs. That is a fiduciary conflict under the Estate Agents Act duties, and it creates VCAT exposure for the landlord, who stays legally liable to the renter whatever the plan says.
5. **Weak demand for insuring frequency losses (Med).** Average landlord maintenance spend is about $2,370 a year [verified (secondary): CPRC *Renting in reality – landlords' insights*, Nov 2025, via search summary]. It is tax-deductible and is not ruinous for someone who owns a $700k asset. Rational landlords self-insure small, frequent losses. That is why US home warranties need about a 46% claims-cost ratio to make money (Frontdoor FY2024: cost of services $852m on revenue $1.84bn; gross margin 54%; service fee paid on each claim) [verified: Frontdoor FY2024 10-K/earnings]. Customers buy them at the moment of a home purchase. No meaningful Australian landlord home-warranty market exists [estimate: none surfaced in search], which is itself a demand signal.
6. **Thin margin, fat capital (High, see table).** Expected profit is about 8–12% of price before selection erodes it. Capital: about $350k at 500 properties and about $1.0–1.2m at 2,000. The founder's limit is ≤$1.2m cash at risk in total.
7. **Trade-cost inflation (Med).** UK landlord repair-damage costs reportedly rose 121% from 2022 to 2024 (Towergate) [unverified: trade press]. A fixed annual price lags trade cost inflation by up to 12 months, and a correlated cost shock is what drives the capital need at scale (see model).

## Things the brief gets wrong, misses or understates
- **"Absorbs repair-cost variance" names the wrong risk.** Variance diversifies away fast. The risks that matter are **mean error** (pricing) and **selection**.
- **"The fee could be split between landlord and tenant":** it cannot be split as a fee in Victoria (attack 2). It can only be priced into rent, subject to the market and to the once-in-12-months limit on increases.
- **The plan does not move legal liability.** The landlord remains the "rental provider" for repair duty and compensation orders, so the plan must specify response times that keep the landlord compliant (urgent repairs immediately, 7-day reimbursement), otherwise it adds legal risk.
- **Missed asset:** an acquired agency's **trust-ledger invoices**, 3–5 years per property in PropertyMe, are a ready-made loss dataset. The founder can price from real frequency and severity before selling anything. This is where the stats edge is decisive.
- **Missed: being the principal resolves the trade-rebate problem.** If the operator buys repairs on its own account under a plan, trade volume discounts are the operator's procurement margin, not a s 48A rebate owed to the client. But being principal is exactly what makes it insurance. That is the central legal question for counsel.
- **Rent guarantee:** besides the APRA problem, longer arrears tails reduce the value of any guarantee and push up insurer pricing. Two points need checking: the removal of no-grounds terminations from 25 Nov 2025 [unverified: practitioner site], and the move of some disputes to Rental Dispute Resolution Victoria [verified: Tenants Vic mention; scope unverified].
- **Compliance work is not risk.** Biennial gas and electrical safety checks and annual smoke-alarm checks (2021 Vic reforms) [estimate: from regulation knowledge; costs about $100–200 each] are fixed costs. Bundle them as a priced service, not as "cover".

## Numbers checked (table: claim | finding | status/source)
| Claim | Finding | Status/source |
|---|---|---|
| Landlord maintenance spend | ~$2,370/yr average; 26% spend ≤$500 | verified (secondary): CPRC Nov 2025 via search (site blocked) |
| House vs unit repairs | ~$2,661 house / $1,677 unit per year | unverified: YIP magazine, undated |
| ATO repairs claims | 2011-12: $2.07bn across 2.02m claimants ≈ $1,026 per claimant; FY2019-20 total ~$2.84bn | estimate (derived) from Urban/ATO tables; rebase for inflation to ~$1.6–2.0k |
| Work orders per unit | ~4.8 per unit-year (US platform data); 3–5 rule of thumb | verified: Property Meld PM25 benchmark (US, multifamily-heavy) |
| US home-warranty claims cost | 46% of revenue, gross margin 54%, retention 79.9% (Frontdoor 2024) | verified: Frontdoor 10-K FY2024 |
| Urgent repair cap | renter may spend up to $2,500 incl. GST; reimbursement within 7 days of notice | verified: CAV, Tenants Vic |
| Non-urgent repairs | 14 days | verified: CAV |
| Bond replacement products | illegal in Victoria | verified: CAV |
| Energy standards | ceiling insulation (R5.0) at new lease from 1 Mar 2027; heater-failure trigger; draughtproofing 1 Jul 2027 | verified: CAV/Energy Vic guidance |
| Landlord insurance premium | ~$800–2,500/yr; rent-default component ~$300–800 | unverified: Mozo/Roopon/Collings |
| Rent-default caps | e.g. Allianz $10k lost rent per period; typical 12–26 week caps, 14–30 day waiting | verified: Allianz page; others unverified |
| Third-party warranty = financial product | likely needs AFSL; incidental exemption unlikely | verified: ASIC guidance |
| APRA minimum capital for a new general insurer | ~$5m (captive lower) | unverified: from memory; GPS 110 framework verified, figure not |
| Insurance Regulations | 2002 Regs repealed; Insurance Regulations 2024 from 1 Mar 2024 (s 8 "not insurance business" is about unauthorised foreign insurers, not warranties) | verified: explanatory statement via search |

**Pricing table (annual, AUD ex GST, risk-bearing version, for comparison only).** Covered scope: reactive repair or replacement of landlord-supplied plumbing, electrical, hot water, fixed heating/cooling, cooktop/oven, and doors/locks. Item cap $3,000; 90-day pre-existing exclusion; excluded: structure, roof replacement, insured perils, renter damage, cosmetic work, and mandated upgrades. Price = (E × 1.15 selection/parameter load + preventive pack + coordination $120) ÷ 0.88.

| Cell | Expected covered loss E | Preventive pack | Price | Expected margin* |
|---|---|---|---|---|
| Apartment <20 yrs (OC handles common) | $650 | $150 | **$1,150** ($96/mth) | ~$140 |
| Unit/townhouse 20+ yrs | $1,100 | $180 | **$1,780** | ~$210 |
| House <20 yrs | $1,000 | $200 | **$1,670** | ~$200 |
| House 20–50 yrs | $1,700 | $220 | **$2,600** | ~$310 |
| House 50+ yrs / weatherboard | $2,400 | $250 | **$3,550** or inspection-gated decline | ~$430 |
| Condition modifier (entry inspection) | A ×0.85, B ×1.0, C ×1.3, D decline until remediated | | | |

*Margin before adverse selection. If the selection load is fully consumed, margin roughly halves. [All E values: estimate, triangulated from CPRC $2,370 total spend with about 60–70% in covered scope, the age gradient from US data, and Melbourne trade rates. Replace them with ledger data.]

**Capital buffer (Monte Carlo, compound Poisson with lognormal severities, E ≈ $1,690 per property; 99.5% one-year).** Scratch model at `/tmp/claude-0/-home-user-EloquentJavascript/621a72f7-b5df-50eb-a3aa-f2fd0cb413be/scratchpad/mc.py`.

| Properties | Process risk only | + 8% correlated cost shock | + ±20% parameter risk (yr 1) | Recommended buffer |
|---|---|---|---|---|
| 100 | ~$58k (~$580/prop) | ~$66k | +$34k | **~$100k** |
| 500 | ~$120k | ~$220k | +$170k | **~$350k** |
| 2,000 | ~$240k | ~$780k | +$680k (falls with data) | **~$1.0–1.2m** |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Rebuild the product as "Maintenance Reserve + Preventive Plan" (no risk transfer).** The landlord pays a flat monthly amount, for example $150–220, into their own ring-fenced trust sub-ledger. Bills are paid from it at **pre-agreed, published trade rates with no agency markup**. Any surplus stays with the landlord, and a shortfall is topped up or carried forward. On top of that, a **fixed-price preventive pack** ($150–250/yr: HWS check, gutter and drain clean, heater/split service, the compliance checks) and an **SLA guarantee backed by fee refunds** (urgent repairs attended within 4 hours, reimbursement handled within 7 days). The landlord gets the "flat bill" experience and the agency carries no insurance risk. Revenue is the preventive margin plus a transparent coordination fee.
2. **Price from the ledger before selling anything.** Pull 3 years of invoices from the acquired book and fit frequency and severity by dwelling type, age, construction and condition. Publish each landlord's own "expected annual repair cost" as part of the investment-advice product.
3. **Distribute rather than underwrite.** Become an authorised representative of an insurer or AFSL holder for landlord insurance including rent default, and later a capped "repair cover" if an insurer will write it. Get advice on s 48A treatment of commission. The commission on general insurance may sit outside the conflicted-remuneration ban, but DDO/TMD duties and the anti-hawking rules apply [unverified: confirm with counsel].
4. **Replace "rent guarantee" with a placement guarantee:** if a tenant we placed is evicted for arrears within 12 months, the letting fee is refunded and the re-let is free. Expected cost is about 1–2% eviction probability × ~$1,500 ≈ $15–30 per property per year [estimate]. It is a warranty on the agency's own service, not on rent.
5. **If risk transfer is ever offered**, make it the opt-out default inside the management agreement rather than opt-in, so selection is weaker. Also require an entry inspection rating, a 2-year minimum term, per-item caps, a 90-day pre-existing exclusion, and an explicit exclusion for energy-standard upgrades. The issuer has to be a licensed insurer.
6. **Tenant side:** offer a renter contents and liability policy (insurer-issued, voluntary, never a condition of the lease) and nothing that touches the landlord's repair duty.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)
| Test | Metric | Kill threshold | Time |
|---|---|---|---|
| Ledger desk study (acquired book) | Calibration of predicted vs actual cost by cell; out-of-sample decile lift | Cells are calibrated to within ±15% **and** top-to-bottom decile cost ratio is ≥3x; if not, there is no underwriting edge, so drop the "priced on condition" claim | Month 0–3 |
| Legal opinion (insurance characterisation + s 48A + RTA fees) | Written advice | Reserve plan is not insurance and needs no AFSL; if it does, run the plan as a pure service | Month 0–2, ~$15–25k [estimate] |
| Reserve + preventive offer to 150 landlords | Take-up at full price | <20% take-up means kill. Opt-in cohort's prior-3-year cost >20% above non-takers means selection is real, so never move to risk transfer on opt-in | Month 4–9 |
| Preventive effect | Reactive spend, plan vs matched controls (difference-in-differences) | <10% reduction at 12 months means the preventive pack is a cost and not a saving, so reprice or drop it | Month 4–16 |
| Retention | Landlord churn, plan vs non-plan | <2 percentage-point churn reduction means it is not a retention product | 12–18 months |
| Insurer appetite | Term sheet from ≥1 insurer/MGA for capped repair cover or rent default with AR distribution | No appetite at ≥30% commission or quota share means don't build risk products | Month 6–12 |

**Pilot design:** 150 landlords from the acquired book, stratified by cell, randomised offer timing (to give a clean control), no risk transfer, published trade rates, a monthly ledger statement and a 12-month review. Success means ≥25% take-up, ≥10% lower reactive spend, ≥2 percentage points lower churn and zero RTA fee complaints. If it succeeds, take the data to an insurer for a capped product in year 2.

## Answers to the round-2 questions in my domain
1. **Which services carry the economics:** none of the risk-bearing products. From my lens: (a) maintenance coordination and preventive service at cost-plus, worth about $150–300 per property per year in margin at 30–40% take-up [estimate], and more for its effect on churn; (b) insurance distribution commissions, subject to s 48A. Order: ledger → reserve plan → AR distribution → MGA binder much later.
2. **LTV:** the maintenance plan adds about $60–120 of margin per managed property per year averaged across the book [estimate: $200 margin × 30–40% take-up, minus selection]. Its larger effect is on churn: cutting 12% to 10% lengthens expected landlord life from ~8.3 to 10 years, which is worth more than the plan's own margin. **It does not materially change the 2,000–2,500-property scale for a $500k draw.** A risk-bearing version raises capital needs, so effectively it raises the scale required.
3. **Regulated vs disqualifying:**
   - **Disqualifying:** risk-bearing repair cover issued by the agency without APRA authorisation and an AFSL; any rent guarantee paying lost rent; tenant-paid contributions to repairs or guarantees, and bond replacements.
   - **Manageable:** cost-plus reserve plan (trust-account handling under the Estate Agents Act; disclosure of trade-rate arrangements); AR distribution of insurance (AFSL holder, DDO, s 48A counsel); placement guarantee on the agency's own fees.
5. **Founder's edge:** decisive in loss modelling from ledger data, condition-based rating, CFO handling of trust-account reserve mechanics, and negotiating with insurers using real loss triangles. Irrelevant to the legal characterisation, and no help against the structural adverse selection of an opt-in product.
6. **Smallest test:** the 3-month ledger desk study plus the legal opinion, for under $30k. If the cell-level model cannot separate cost by about 3x across deciles, the "priced maintenance" pillar is dead before any customer sees it.

## Questions I'd hand to other specialists
- **Victorian property lawyer:** Is a landlord-funded maintenance reserve held in the trust account permitted under the Estate Agents Act trust rules, and what audit treatment applies? Is an insurer's commission to the agency a "rebate" under s 48A? Is a renter-optional repair contribution a prohibited charge under ss 51/51A as amended in 2025?
- **Financial-services lawyer:** Does a capped bundle of "first $X of repairs included" inside a management fee fall within s 763E as incidental? Where does the line sit between a maintenance contract and insurance in kind under Australian authority?
- **Tax specialist:** GST and insurance-duty treatment of the reserve vs a premium; landlord deductibility timing of reserve deposits (likely deductible only when spent).
- **Trades/operations specialist:** Can a dense corridor network deliver the 4-hour urgent SLA and 10–15% below-market rates without exclusivity that would raise ACCC concerns?
- **Credit/data specialist:** Does the standard application form allow enough data for the tenant model behind the placement guarantee to beat agency judgement?
