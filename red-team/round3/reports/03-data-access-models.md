# Data Access & Model-Validity Lead (Statistician): red-team report

## Verdict
**Survives-if: the product is reframed from "a model that prices rolls better than the multiple" to "a ledger-native diligence and attrition engine with honest uncertainty".** Data access is workable through agency-run exports and design partners, but not through a PropertyMe API in 90 days. The bigger problem is labels. Post-sale retention outcomes, the thing a "retention-adjusted price" must be validated against, sit in perhaps a few dozen deals per acquirer and mostly in lenders' and franchise HQs' files. **The single biggest issue:** the transition shock (attrition caused by the sale itself) can't be learned from any data the founder can reach in 90 days, and 400-door rolls carry about ±5 points of irreducible binomial noise. So the claimed "$100k per deal" edge is mostly unprovable at first. The provable part is baseline landlord attrition, which can be modelled from the vendor's own ledger history.

## Verdict on the software business
- **Product A (rent-roll DD and valuation)** is the wedge, but the v1 should be a **DD report**: data quality, fee quality, landlord concentration, tenure and a survival curve, arrears, maintenance load and MEES exposure, with the price shown as a range and its assumptions spelt out. It should not be a black-box price. The model part that can be validated is landlord-level survival from the ledger. The part that can't be validated yet is the post-sale shock, which should be shown as an explicit Bayesian prior.
- **Product B (portfolio health and retention monitoring)** is where data accumulates lawfully and continuously, because the agency is the controller and you are its service provider. That makes it the **data moat that feeds A**. Round 2 judged churn propensity "a feature, not a product" for an operator. For a lender or franchise HQ watching 50–500 offices it is a product, because it monitors portfolios rather than individual landlords.
- **Product C (maintenance intelligence)** is credible as a book-level benchmark and forecast. It is not credible as per-property pricing in v1. Ledger invoices understate cost systematically (see A4).
- **Product D (agentic DD and integration)** is a delivery mechanism for A, not a separate data asset.

## Attacks on the thesis

**A1. API access won't arrive in 90 days, and it isn't designed for this use (High).** PropertyMe's API and marketplace access is discretionary. Applicants need "a reasonable mutual client base" and a "significant benefit to PropertyMe users". Fees start at **≥$1,000 + GST a month**, with a response "within 30 business days" [verified: PropertyMe API application page, via search summary]. A pre-revenue, one-person entity with no mutual clients is a weak applicant. Owner EQT (PE majority since its buyout) [verified: Business News Australia/SignalBase via search] has every reason to keep portfolio-level analytics in-house. MRI's official API "can require additional licensing" [unverified: Supergood, third-party]. Console Cloud is described as having an open REST API [unverified: directory listing]. I found no public Rex PM, Ailo or Kolmeo API terms covering third-party analytics [unverified: absence of evidence]. **Implication:** v1 ingestion must work from **agency-run report exports** (CSV/XLSX: owner, tenancy, ledger/transaction, creditor-bill, arrears and archived-property reports), which the agency pulls itself. A connector for each system is year-2 work.

**A2. "A PropertyMe export" is not one file, and history may be truncated (High).** PropertyMe's own FAQ says exporting an entire portfolio to a single file "isn't practical", because the portfolio is "a complex system with multiple databases". Cancelled portfolios are deleted after **30 days** [verified: PropertyMe FAQ via search summary]. Three consequences follow:
1. Every DD ingest is a multi-report reconciliation job: about 6–10 reports, matched on property and owner keys.
2. **Left truncation.** Agencies migrated to PropertyMe through MigrateMe or a manual migration typically carry current properties and opening balances, not the lost managements from before migration [estimate: typical migration practice; confirm on 3 agencies]. A naive survival model on such data is survivorship-biased: it sees only the landlords who stayed, so it understates attrition. A delayed-entry (left-truncated) Cox or discrete-time model fixes this, provided the migration date is known. Most "AI" tools won't handle it.
3. A vendor that leaves PropertyMe at sale loses its history after 30 days. The acquirer's data-rights clause must require the **full export before settlement**.

**A3. The transition-shock label scarcity is fatal to "beats the multiple" as a 90-day claim (High).** Decompose post-sale loss into (i) **baseline attrition**: landlords selling, self-managing or switching for ordinary reasons, and (ii) the **transition shock** caused by the sale (brand change, PM departure, fee change).
- (i) is learnable from the vendor's ledger without any transaction labels. Every archived management with an end date is an event. A 400-door book losing about 12–15% a year yields about 250–300 events over 5 years. At 10–20 events per parameter that supports a 15–25-feature model [estimate]. Pooled across 10 agencies it gives about 2,500–3,000 events.
- (ii) needs past-deal outcomes. If the shock varies across deals with SD ≈4 points, estimating its **mean** to ±2 points at 95% needs about **15 deals** with 12-month outcomes. **Showing that a model cuts deal-level pricing error by 1.5 points**, with paired-difference SD ≈3 points at 80% power, needs about **30 deals with 12–36-month outcomes** [estimate: standard power calculation]. No single acquirer has that, and brokers know prices but not outcomes. Retention clawbacks cover only 3–6 months [verified in round 1: REIQ/API Magazine].

**A4. Realised retention on one roll is noisy, so the "$100k" edge is an expectation, not a promise (High).** For a 400-door roll with true 3-year loss of 40%, the 95% band of realised loss is **±4.8 points** from binomial noise alone. It is ±6.8 points at 200 doors and ±3.4 points at 800 [estimate: √(p(1−p)/n)]. Landlord clustering (multi-property owners) and macro shocks widen it. **A perfect model still has a ±5-point error on a typical roll.** The edge can only show up as reduced **bias** averaged over many deals.

**A5. Expected lift over a good multiple is modest (Med–High).** Brokers' multiples already price average attrition, and the round-1 red-flag rule (−0.2× per flag) captures obvious variation. Suppose true 3-year retention varies across rolls with SD ≈8 points, and a ledger model explains half the variance. Then mean absolute pricing error falls from about 6.4 to about 4.5 points, roughly **1.9 points ≈ $38k on a $2M roll** (using the brief's $20k per point). Against a disciplined red-flag checklist, the incremental gain is probably **~1 point ≈ $15–25k a deal** [estimate]. That is still worth a $5–15k DD fee, but it is a fifth of the headline, and the honest pitch is "we cut the tail risk of a bad roll", not "we price better".

**A6. Ledger maintenance data under-records cost, in a biased way (High for Product C).** Creditor bills paid from trust capture only agency-arranged jobs. They miss:
- jobs landlords arrange and pay directly;
- owners-corporation-covered repairs (common property) in apartments;
- insurer-paid claims;
- capex done between tenancies by the landlord's own builder.

They include non-maintenance items that need filtering, such as rates, strata levies, water and insurance premiums. Free-text descriptions need classification. Property attributes (age, construction, heating type) are usually absent and must be joined from Cotality or Land Use Victoria [estimate: typical PM data]. The round-2 sample sizes are arithmetically right: n = (1.96·CV/0.10)² gives **864** property-years at CV 1.5 and **2,401** at CV 2.5 for ±10% per cell at 95%. But they assume the measured cost is the true cost. If capture varies 60–95% by agency and property type, between-agency bias exceeds the ±10% target. **Capture rate is the first thing to measure.**

**A7. Lawful DD disclosure is narrower than "send us the export" (Med–High).** OAIC guidance on selling a business: vendors must comply with the APPs during DD. Purchasers must protect privacy, honour confidentiality-agreement privacy clauses, and **destroy or return** personal information after DD [verified: OAIC "Selling a business" via search summary; the OAIC site was not reachable from this session]. Secondary commentary says OAIC accepts most DD disclosures as standard business practice, but recommends aggregated data where possible [unverified: law-firm summary]. Separately, Victoria's Estate Agents (Professional Conduct) Regulations 2018 bar an agent from using or disclosing a client's confidential information unless the client authorises it or the law requires it [verified: CAV professional-conduct page via search; exact regulation number unconfirmed]. Landlord identities, rents, arrears and fee deals are the landlord-client's confidential information. Four consequences follow:
1. Pre-contract DD should run on **pseudonymised data**: hashed owner IDs, addresses held back or tokenised.
2. Identified data should be released only after exchange, under conditions.
3. **You cannot keep DD data to train models** unless the vendor's agreement and landlord authorities permit de-identified retention.
4. The DD product does not accumulate a dataset by default. That is the strongest argument for B (an ongoing service-provider relationship) as the data engine.

The $3M small-business exemption still stands as at Oct 2026. It is not being removed on 10 Dec 2026 [verified: Solway Oct 2026; tranche 2 has no commencement date]. Many small agencies are still APP-exempt, but **a data business that pools agency data is not** if it trades in personal information (s 6D). Build to APP standard from day 1.

**A8. The data moat sits with PropertyMe, not the founder (High, strategic).** PropertyMe hosts about 1–2M properties across thousands of agencies. It can see management archives, portfolio-to-portfolio transfers (i.e. **roll-sale outcomes**) and every creditor bill. It already exposes read-only live data to Claude and ChatGPT through AiMe Connect, from 8 Oct 2026, on the Manage PM Advanced tier and above [verified: Elite Agent / Proptech Connect]. It is the one party that could build A, B and C with labels at scale. The founder's defensible assets are (a) statistical method (truncation, censoring, credibility pooling, honest uncertainty), (b) **cross-platform** coverage (PropertyMe + Console + Rex + MRI in one acquisition, which PropertyMe can't do) and (c) **deal-outcome labels** gathered from lenders and acquirers.

## Things the brief gets wrong, misses or understates
- **The "5-point retention error ≈ $100k" framing confuses noise with bias.** About ±5 points is irreducible on a 400-door roll. The model's value is average bias reduction, which is smaller (A4–A5).
- **Survival models on the ledger need no transaction labels**, and this is the cold-start answer the brief only hints at. Only the transition shock needs deal labels.
- **Reason for loss is usually not coded.** Archived managements seldom carry a structured reason. Sale vs switch vs self-manage must be inferred by matching addresses to sale records (Cotality/Domain/Land Use Victoria) within ±6 months of the end date. VGV publishes only aggregate sales statistics under CC-BY. Address-level data comes through LANDATA or Cotality licences [verified: land.vic.gov.au via search; pricing unknown]. Budget for this.
- **The attrition prior may be stale.** Round 1 used "12–20% annual roll attrition", built on the 2024 bond fall: −21,712 active bonds in the year to June 2024, 732,125 bonds at 30 June 2024 [verified: RTBA annual report 2023–24/PropTrack]. A May 2026 PAEC hearing transcript puts active bonds at **"over 745,000"** [verified: PAEC 2026–27 budget estimates transcript, via search summary]. That suggests the rental stock recovered, which conflicts with the June-2026 "more refunds than lodgements" claim [unverified, investor press]. **Industry attrition priors must be re-derived** (RTBA quarterly data, or design-partner ledgers), not carried forward. The only published "typical" figure I found is about 15% a year, from an Elite Agent opinion piece [unverified: no survey]. There is **no published Australian benchmark of lost managements**. Macquarie's benchmarking report exists (2024 edition) but its PM-loss figures weren't retrievable [unverified].
- **Tenancy turnover ≠ management loss.** Label = *management agreement ended*, with date and inferred reason.
- **AiMe Connect is an agency-operated query surface, not a pipeline.** It is useful for an agency to answer DD questions itself. Routing identified landlord data through a third-party LLM chat is a disclosure decision for the agency, not for you.

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| PropertyMe partner API obtainable | Discretionary; ≥$1,000+GST/mo; reply within 30 business days; needs mutual clients | verified: PropertyMe API page (search summary) |
| A PropertyMe export ingests cleanly | Whole-portfolio single export "isn't practical"; cancelled data deleted after 30 days | verified: PropertyMe FAQ (search summary) |
| AiMe Connect read-only | Read-only, MCP, Advanced tier+, from 8 Oct 2026, follows agency permissions | verified: Elite Agent / Proptech Connect |
| PropertyMe scale | "Over 5,000 agencies" (vendor-sourced); round 2 had ~6,500 agencies / ~2M properties | unverified, inconsistent |
| PropertyMe ownership | EQT majority | verified: Business News Australia (search) |
| DD disclosure lawful | Allowed with APP compliance; purchaser to destroy/return PI after DD | verified: OAIC guidance (summary; site blocked) |
| Agent confidentiality | Can't use/disclose client confidential info without authority or legal requirement | verified: CAV (reg number unconfirmed) |
| Small-business exemption ends Dec 2026 | No; still in force; tranche 2 has no start date | verified: Solway Oct 2026; AGD statements |
| Annual roll attrition 12–20% | Only an anecdotal ~15% found; Vic active bonds ~745k (May 2026) vs 732k (Jun 2024) | estimate / verified (PAEC transcript) |
| Maintenance n per cell 860–2,400 | 864 (CV 1.5), 2,401 (CV 2.5) for ±10% at 95% | verified arithmetic; CV assumed |
| Roll multiple ~2.9x historically | Macquarie 2012: 2.9× recurring PM commissions | verified: trade press via search |
| Noise on a 400-door roll | ±4.8 pts (95%) on 3-yr loss at p=0.4 | estimate: binomial |
| Deals needed to prove lift | ~15 (mean shock ±2 pts); ~30 (1.5-pt MAE gain) | estimate: power calculation |

## Improvements (ranked by impact)
1. **Split the model and the claim.** Ship (a) a validated **landlord-level survival model** (discrete-time hazard or Cox with left truncation; features: tenure, owner's property count, fee rate vs market, rent-to-market gap, arrears and maintenance-dispute history, lease stage, property age/MEES exposure, owner postcode distance) and (b) an explicit **transition-shock prior**, e.g. Beta centred at 8–10% with a wide interval, shown in every report as a scenario band. Claim (a). Disclose (b).
2. **Recruit one franchise HQ or one roll lender as the label partner.** Their deal and covenant archives (≥20–30 deals with 12-month retained counts) are the only fast route to transition-shock labels. Offer free portfolio monitoring (B) in exchange for a de-identified outcomes licence.
3. **Design the data-rights stack now.** It needs:
   - a pre-contract **pseudonymisation kit** that the vendor runs locally: hashed IDs, tokenised addresses, with a salt the buyer never sees;
   - a DD template clause allowing de-identified retention for model improvement;
   - an agency service agreement for B/C that makes the founder a service provider, with de-identified pooling rights;
   - APP-grade privacy from day 1. Get a privacy lawyer to sign off before the first ingest.
4. **Build an export-normaliser for 3 systems first**: PropertyMe, Console, Rex/MRI by local share. Agencies drag in a standard set of reports and get a reconciliation check, e.g. ledger fees vs owner statements, before any modelling. The reconciliation is itself saleable DD.
5. **Infer the reason for loss** by matching addresses to sale records. Without it, baseline attrition can't be separated into "sale" (macro-driven, a hedgeable story) and "switch" (service-driven, a fixable story).
6. **Maintenance: measure capture first, then forecast at book level** with a Tweedie/log-normal GLM plus credibility shrinkage to a pooled prior. Report book-level ±% with intervals, not per-property prices. Build the MEES-capex flag (heating and hot-water age) as a separate risk line.

## Tests & kill criteria
| # | Test | Metric | Threshold | Time/cost |
|---|---|---|---|---|
| T1 | Data-access sprint: ask 10 agencies (via network, brokers) for a 5-yr report pack incl. archived managements and creditor bills | Usable packs received | ≥3 of 10 in 3 weeks → proceed; ≤1 → kill A/B as a data business | 3 wks, ~$0–3k |
| T2 | Truncation audit on those packs | Share with ≥3 yrs of archived-management history | ≥2 agencies with ≥3 yrs → survival modelling viable; else rely on partner archives | 1 wk |
| T3 | Out-of-time survival backtest (train to mid-2024, predict 24-mo loss) | Book-level absolute error vs naive trailing rate; C-index | ≥25% lower error than trailing rate and C ≥0.65 → claim baseline model; <10% gain → sell DD reporting only | Weeks 4–9, founder time |
| T4 | Label-partner hunt: lenders, franchise HQs, roll-up acquirers | Deals with ≥12-mo retained counts licensed | ≥20 deals by day 90 → estimate the shock; <10 → shock stays a prior; drop "retention-adjusted price" wording | 90 days |
| T5 | Maintenance capture check (ledger vs landlord survey on 50 properties) | Ledger share of true spend | ≥80% for houses → Product C viable; <60% → C is a benchmark only | 4–6 wks, ~$2k incentives |
| T6 | Data-rights acceptability | Brokers/vendors accepting pseudonymised pre-contract DD and a retention clause | ≥5 of 10 → A can accumulate data; ≤2 → B must be the data engine | 4 wks |

## Answers to the round-3 questions in my domain
**Q2: Can the founder get the data, and do the models beat the multiples?**
- **Access:** yes, through agency-run exports with consent and a service-provider agreement. Not through PropertyMe's API in 90 days. DD data is lawful to see but must be pseudonymised before contract and destroyed or returned afterwards unless retention is agreed. Lasting data comes from B/C service relationships and from a lender or franchise label partner, not from DD.
- **Beating the multiples:** on baseline attrition, probably yes, and this is testable in 90 days by backtest. On the full retention-adjusted price, unproven. It needs about 15–30 deals with outcomes, and the realistic lift over a disciplined checklist is about $15–40k per $2M roll, not $100k.
- **Maintenance:** sample sizes are achievable by pooling about 10 agencies (≈25k property-years), but measurement bias, not sample size, is the binding constraint.

**Can a credible v1 be built in 90 days, and on whose data?** Yes, if v1 is defined as a DD and portfolio-health report with a validated baseline survival model, a transparent transition-shock prior and book-level maintenance benchmarks. It would be built on **3–5 design-partner agencies' own exports**, plus one live acquisition the founder's network is pricing. A validated "retention-adjusted price" needs **a lender's or franchise group's deal archive**. If no such partner signs within 90 days, the pricing claim waits 12–36 months for outcomes.

**Q4: Wedge vs moat.** A (the DD report) is the wedge: paid per deal and urgent. B (ongoing monitoring with pooling rights), together with cross-platform coverage and deal-outcome labels, is the moat. On its own the model isn't a moat. PropertyMe has more data.

## Questions I'd hand to other specialists
- **Privacy/legal:** Does pre-contract disclosure of pseudonymised landlord data fall outside the Professional Conduct Regulations' confidentiality duty? Do standard REIV management authorities permit disclosure to a prospective assignee? Can a service provider pool de-identified data from APP-exempt agencies without becoming a trader in personal information?
- **Market/competition:** Would PropertyMe (EQT) license portfolio-transfer outcomes or block exports? Do Macquarie and other roll lenders have covenant-monitoring data they would license?
- **M&A/broker specialist:** How many Victorian and national roll transactions happen a year, and what share involve an outcome-tracked retention clause beyond 6 months?
- **Pricing/GTM:** Will acquirers pay $5–15k per deal for a report whose headline is a range rather than a price?
