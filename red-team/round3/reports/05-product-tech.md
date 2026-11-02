# Product & Agentic-AI Engineering Lead: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives-if.** The build is not the hard part. A PropertyMe-only, concierge-style DD report is about 5–6 founder-weeks of work, which fits in 12 calendar weeks part-time. A productised multi-system v1 is about 12–14 founder-weeks, which is 6–8 months part-time. **The biggest issue is that the only defensible output, a calibrated retention-adjusted price, has no ground truth on day one.** Post-acquisition losses are driven largely by the acquirer's integration choices, which are invisible in the vendor's export. Everything else in the report (arrears, concentration, fee quality, compliance gaps) is being commoditised right now by PropertyMe AiMe Connect plus a general LLM. The product survives only if it is designed around collecting **outcome data** (post-settlement exports), not around generating reports.

## Verdict on the software business (which product, if any, is the business, from your lens)
- **A (DD report) is the wedge, not the business.** It pays for data access and should be sold concierge-style: the founder runs the pipeline and signs every report.
- **The asset is a pooled, de-identified dataset of roll histories linked to post-sale outcomes.** That dataset powers a retention/price model and later **C (maintenance cost benchmarks)**, because every DD'd roll brings 2–4 years of job and invoice history.
- **B (monitoring for lenders and franchise HQs) is the recurring revenue.** But it needs a live connection to PropertyMe or Console, which those vendors control. Treat B as dependent on platform permission, not as a given.
- **D (agentic integration tooling) is a services business.** Skip it, except for the trust-indicator module, which A needs anyway.
- From an engineering lens, this is a **data-rights business with a report-shaped front end**. The two clauses that matter most are (1) the right to retain de-identified derived features and (2) a 12- and 24-month post-settlement outcome export. Without them, A stays a low-margin consulting product.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

1. **The generic report layer is already commoditised (High).**
   - AiMe Connect lets any agency user link Claude or ChatGPT to live PropertyMe data over read-only MCP. It has been available from about 8 Oct 2026 on Manage PM Advanced tier and above [verified: eliteagent.com; proptechconnect.com]. PropertyMe has said "Agentic AiMe" is next [verified: same coverage].
   - A vendor can give a broker a seat, and in an afternoon the broker can get arrears ageing, landlord concentration, effective fee %, and overdue compliance jobs.
   - Roughly 60–70% of a typical DD pack's content is therefore a prompt away [estimate: share of a standard DD checklist that is plain aggregation].
   - The differentiated residue is: (a) a calibrated retention and price model; (b) evidence-grade tie-outs, where every number links to a source row; (c) a format lenders accept.
   - **Implication:** build (a) and (b) first and keep the report shell thin.

2. **Retention ground truth is missing or confounded (High).**
   - The model needs *lost managements*, with dates and ideally reasons. Whether exports reliably include archived or lost folios is **[unverified]**. No official PropertyMe export documentation was found, and third-party migration guides tell users to "ask support what your account can export" [verified: enterprisedna.co guides for PropertyMe and Console; vendor-marketing source].
   - Even with perfect vendor history, the post-sale loss rate depends on the acquirer's integration. Round 1 found about 66% of managements kept after a hard switch versus about 80% with a soft landing (round-1 09). That 14-point spread dwarfs the 5-point error the thesis wants to price.
   - **The model cannot be validated on vendor data alone.** It has to be conditioned on the integration plan and calibrated on outcomes that arrive 12–24 months after each sale.
   - **Fix:** run a retrospective backtest on completed acquisitions (Tests, #1).

3. **Thin per-roll samples (Med).**
   - A 300-property roll losing 12% a year yields about 108 loss events over 3 years. That is enough to estimate a base rate to roughly ±3–4 points, but too few for more than 3–4 covariates per roll [estimate: binomial on ~900 property-years].
   - **Fix:** use hierarchical shrinkage toward a cross-roll prior. The model only becomes better than rule of thumb after about 10–20 rolls with outcomes [estimate]. At 1–2 DDs a month, that is 1–2 years, not 90 days.

4. **Lenders will not swap a panel valuation for a software report (Med–High for the "price band" output).**
   - Rent-roll lending runs on panel valuers using a commission × multiple method, adjusted for arrears, vacancy and ancillary income [verified: acumentis.com.au rent-roll valuation page; Acumentis has a dedicated rent-roll valuation team].
   - Banks also run vendor-risk reviews under APRA CPS 230/234 [unverified in session: CPS 230 commenced 1 Jul 2025], with procurement cycles of 3–9 months [estimate].
   - **Position the product as an input to the valuer and the credit team, not a replacement.** Sell first to acquirers and brokers.

5. **Trust "reconciliation" creates liability (Med).**
   - Victorian agents must reconcile monthly. The principal or officer in effective control must verify within 14 days of month-end (Reg 26, Estate Agents (General, Accounts and Audit) Regulations 2018), and there is an annual audit under s 64 [verified: CAV auditor's report form and trust-account reference guide].
   - Re-performing a three-way reconciliation from exports without bank statements is impossible. Calling it a "reconciliation" invites reliance claims.
   - **Fix:** call it **"trust indicators"**, with explicit scope and PI insurance. Examples: whether reconciliations were done and signed on time, owner folios in debit, unallocated or suspense balances, bond-lodgement mismatches, ageing of unpresented items.

6. **Export heterogeneity (Med).**
   - PropertyMe is the clear first target: about 6,400+ agencies and 1.9M+ properties [verified: Software Advice listing; vendor-supplied figure].
   - Console Cloud, MRI PropertyTree and Rex PM each need their own mapping, and Console Gateway is being retired [verified: eliteagent.com]. Console has an API, but its scope is undocumented [verified at listing level: GetApp].
   - Each new system costs about 1–2 founder-weeks to map and test [estimate]. **Support one system until 10 paid reports.**

7. **Compliance flags are mostly "unknown", not "fail" (Med).**
   - Victoria requires gas and electrical safety checks every 2 years and smoke alarm checks every year [verified: VBA/BPC summaries of the Residential Tenancies Regulations 2021].
   - Energy standards: ceiling insulation (R5.0, where there is none or only partial coverage) is required **from 1 Mar 2027**, triggered by a new lease or a move to periodic. Draughtproofing follows from **1 Jul 2027**. Efficient heating is required when the existing system fails beyond repair [verified: CAV and energy.vic.gov.au guidance].
   - PM systems rarely hold insulation or heating attributes. Evidence of checks lives in job records and attachments of uneven quality.
   - **Report "compliance evidence coverage"** (the % of properties with a dated certificate or job inside the cycle) rather than a pass/fail. Also flag landlords facing a 2027 capex trigger as **churn/sell risk**. That is a genuinely new retention covariate.

8. **Cost of goods is human review, not compute (Low for viability, High for margin).** See the cost table under Numbers. LLM cost is about A$25–80 per report, while founder review is 6–12 hours. Gross margin depends entirely on cutting review hours.

## Things the brief gets wrong, misses or understates
- **The 2027 energy standards are phased, and two are event-triggered.** Ceiling insulation applies from 1 Mar 2027 on a new lease or periodic conversion. Draughtproofing applies from 1 Jul 2027. Heating applies only on failure [verified: CAV]. A DD model should treat these as a capex shock that may push landlords to sell (a retention risk), not just as a compliance checkbox.
- **MRI PropertyTree is missing** from the list of source systems. It is a major legacy system in Victorian rolls [unverified share].
- **"Ingest PropertyMe exports" assumes the exports exist and are complete.** There is no public full-export guide; partner API credentials are issued manually [verified: apis.io / API Evangelist catalogue; pypme community docs].
  - The OAuth scope list reportedly includes `transaction:read` and `activity:read` [verified: apis.io scope list, third-party]. A vendor-consented OAuth pull would therefore be far better than CSVs, but it needs partner status.
- **AU data residency is not available on Anthropic's first-party API.** `inference_geo` supports only "us" or "global" [verified: Claude API docs as packaged in the claude-api skill, cached Oct 2026]. AU residency means Amazon Bedrock's Australian geo profile (`au.`), which routes between Sydney and Melbourne [verified for Sonnet/Haiku 4.5: AWS post, Oct 2025; an `au.` ID listed for Opus 5 per AWS model-card snippet, unverified]. The newest models may reach Bedrock AU later than the first-party API.
- **Incumbent valuers already sell rent-roll valuations** (e.g. Acumentis's rent-roll team [verified]). The competition for A is a valuer plus a broker spreadsheet, not nothing. I found no Australian product that does data-driven roll DD [verified as a negative search result only].

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| PropertyMe scale | ~6,400+ agencies, 1.9M+ properties | [verified: Software Advice listing, vendor figure] |
| AiMe Connect | Read-only MCP to Claude/ChatGPT, Advanced tier+, ~8 Oct 2026; agentic AiMe "next" | [verified: eliteagent.com, proptechconnect.com] |
| PropertyMe API | Partner-gated; credentials issued manually; OIDC/PKCE; ~20 scopes incl. transaction:read/write | [verified: third-party catalogues only] |
| Claude pricing (USD per 1M tokens, in/out) | Opus 5.5 $4/$20; Sonnet 5.5 $2/$10; Haiku 5.5 $0.10/$0.50; Batch −50%; Opus 5.5 cache read $0.20 | [verified: Anthropic model table, cached 6 Oct 2026] |
| Anthropic API AU region | Not offered (us/global only; "us" at 1.1x) | [verified: API docs via skill] |
| Bedrock AU | `au.` geo profile (Sydney↔Melbourne); geo premium ~10% in Japan, unclear in AU | [verified: AWS (Sonnet/Haiku 4.5); premium unverified] |
| Vic safety checks | Gas and electrical every 2 yrs; smoke alarms yearly | [verified: VBA/BPC] |
| Electrical rule change Oct 2026 | Mentioned only in sponsored content | [unverified] |
| Energy standards | Insulation 1 Mar 2027 (new lease/periodic); draughtproofing 1 Jul 2027; heating on failure | [verified: CAV, energy.vic.gov.au] |
| Trust reconciliation | Monthly; verified ≤14 days by principal/OIEC (Reg 26, 2018 Regs); annual audit s 64; 7-yr records | [verified: CAV forms/guide] |
| SOC 2 first year | US$15–40k lean (audit + platform + time); Vanta ~US$10–20k/yr | [verified: vendor/consultant blogs, wide variance] |
| LLM cost per report (500-property, 3-yr roll) | US$15–50 → A$25–80 | [estimate: below] |
| AUD/USD | ~0.65 | [unverified] |

**Cost per report (500 properties, 3 years of history).**

LLM tasks:

| Task | Volume | Model | Cost |
|---|---|---|---|
| Maintenance job and invoice categorisation | ~5k jobs × ~350 tokens in / 60 out | Sonnet 5.5, batch | ≈ US$3 |
| PDF owner-statement and invoice extraction | ~1.5–2k pages | Sonnet 5.5, batch | ≈ US$7–15 |
| Schema mapping and narrative drafting | ~1M tokens in / 0.15M out | Opus 5.5 | ≈ US$7 |
| Re-runs and evals | | | ×2 |
| **Total** | | | **≈ US$35–50** |

Infrastructure: AWS Sydney (RDS Postgres, S3 with KMS, ECS/Fargate, logging) costs about A$400–800/month fixed [estimate].

Market-rent data:
- DFFH quarterly medians are free.
- Cotality or PropTrack feeds cost about A$15–50k/yr [unverified]. Defer them until B.

Human review: 6–12 h at v0, with a target of ≤3 h by report 20.

## Improvements (concrete changes to the plan, ranked by impact)

1. **Make outcome data the contract.** Every engagement includes:
   - (a) a licence to retain de-identified derived features;
   - (b) a 12- and 24-month post-settlement export, in exchange for a discount (around 30%) or a free retention-monitoring report.

   This builds the only moat that PropertyMe and Cotality lack: roll-level *transaction outcomes*.

2. **Backtest before building.** Start from acquirers who bought rolls 2–4 years ago. Their system holds the full pre-sale history *and* the post-sale outcomes, so every past acquisition is a labelled example available today. Ten such rolls are worth more than any feature work.

3. **Pseudonymise at source.** Ship a small open-source sanitiser that the vendor runs locally before upload:
   - It drops tenant names, contacts and bank details.
   - It replaces landlord and tenant IDs with salted hashes (salt kept by the vendor).
   - It keeps postcodes, rents, dates and amounts.

   This removes most Privacy Act and APP 8 friction, shortens vendor consent, and shrinks the breach blast radius. The models do not need identities. Concentration analysis needs only a consistent owner hash.

4. **Use a deterministic core and keep the LLM at the edges.** Architecture:
   - **Ingest.** Use a declarative mapping per source system: a YAML schema for each known PropertyMe report. The LLM proposes mappings only for unseen layouts, and a human confirms them.
   - **Canonical model.** Postgres tables: property, owner (hashed), management (start/end/reason), tenancy, rent schedule, ledger transaction, arrears snapshot, job, invoice, compliance event.
   - **Computation.** All numbers come from SQL or Python: trust indicators, flags, survival model, DCF. The LLM never computes a figure.
   - **LLM tasks.** Classify free-text jobs into trade, urgency and capex/repair. Extract PDF figures with dual extraction plus checksum ties (statement totals must reconcile, or the item goes to a human). Draft narrative constrained to computed facts, using citations or evidence IDs.
   - **Evidence links.** Every flag and figure carries `source_file#row` or `page:bbox`. The HTML/PDF report renders these as clickable appendices.
   - **Rules.** Victorian rules live in a single versioned policy file with a CAV link and a review date (round-1 05). This is the hook for NZ or other states later.
   - **Human review.** Use a checklist gate: every red flag confirmed, every number ≥$10k traced, the narrative diffed against facts. Reviewer edits are logged as eval data.

   No autonomous agent loop is needed in v1. A pipeline with two LLM steps beats an "agent" on both accuracy and auditability.

5. **Define the price as a band.** Output P10/P50/P90 of retention-adjusted value under three integration scenarios (hard switch, soft landing, soft plus earn-out), shown next to the broker multiple. The scenario conditioning is the honest answer to Attack 2.

6. **Pick the model per task by accuracy, not tokens.** Compute is about 1% of the cost of goods [estimate], so the price spread between Opus and Haiku is irrelevant. Run Sonnet 5.5 and Opus 5.5 through Bedrock's `au.` profile once AU availability is confirmed. Until then, process only pseudonymised data on the first-party API, with zero data retention if granted.

7. **Take a security posture without SOC 2 in year 1.**
   - AWS Sydney or Melbourne only.
   - Per-engagement KMS keys, so deleting a key crypto-shreds the engagement (deletion SLA: raw data within 30 days of report delivery).
   - SSO + MFA, no laptops holding raw data, CloudTrail, Essential Eight ML2 for the founder's endpoints.
   - A 2-page security pack and a pen test (about A$8–15k [estimate]) when the first lender asks.
   - Start SOC 2 Type 1, or ISO 27001 (preferred by AU enterprise buyers [verified: one consultant source]), only once B is sold to a bank.

8. **One source system until report 10.** Support PropertyMe CSV/XLSX first and apply for PropertyMe partner API access in parallel. Add Console second, then PropertyTree.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| # | Test | Metric | Continue if | Kill/pivot if | Time / cost |
|---|---|---|---|---|---|
| 1 | **Retrospective backtest.** 3–5 acquirers supply pre-sale vendor data plus 24-month outcomes for past roll purchases | Predicted vs actual 24-month management loss | Model mean absolute error ≤4 pts and beats both a constant base rate and the broker multiple's implied loss by ≥3 pts on ≥3 of 5 rolls | No better than the base rate → sell A as a fast DD service only, not a pricing edge | 60–90 days, ~A$5–10k in data fees |
| 2 | **Export completeness.** 5 PropertyMe agencies run the data-request pack | % of required fields present, especially lost managements with end dates, job and invoice amounts, and compliance events; time to export | ≥4 of 5 complete in under 1 hour | Lost-management history unavailable in ≥3 of 5 → the retention model needs an API or partner route; pause | 3–4 weeks, ~A$0–2k |
| 3 | **Commoditisation test.** Same roll: your report vs AiMe Connect + Claude with a good 2-hour prompt, rated blind by 2 brokers or acquirers | Preference and willingness to pay | Your report preferred, with a WTP gap of ≥A$2k | Parity → drop the report shell and sell only the price model / data | 2 weeks |
| 4 | **Concierge paid DDs** | Paid reports; review hours; decision impact | ≥3 paid at ≥A$3k within 90 days; ≥1 changed price or terms; review ≤12 h | <2 paid, or review >20 h each | 90 days |
| 5 | **Data-rights uptake** | Clients signing the de-identified retention clause plus the outcome-export clause | ≥2 of the first 3 | 0 of 3 → no moat; A is consulting | With #4 |
| 6 | **Lender read** | 2 bank credit or risk teams on accepting the report as a supplement, and their vendor-risk requirements | Accept as a supplement; requirements ≤SOC 2 Type 1 within 12 months | Panel valuation only and full CPS 230 onboarding → drop lenders from the year-1 plan | 6 weeks |

**Pre-build engineering kill rule:** if test 1 cannot source at least 3 labelled rolls within 60 days, do not build the price model. Ship flags only, and reassess.

## Answers to the round-3 questions in my domain

**Q2. Can the founder get the data, and do the models beat rule-of-thumb multiples?**
- **Access:** feasible deal by deal via vendor-consented exports, since a vendor in a sale process will cooperate. Ongoing access (for B) depends on PropertyMe partner API approval, which is uncertain.
- **Privacy:** most friction disappears with source-side pseudonymisation. Get counsel on APP 6 disclosure during DD and on the 10 Dec 2026 automated-decision transparency rules. Tenant-level arrears flags are low risk if they are not used for decisions about individuals.
- **Models:** they can only *demonstrably* beat multiples after outcome calibration. The retrospective backtest is the shortcut. Expect an edge on flagging (concentration, fee leakage, compliance-driven sell risk) immediately. Expect a calibrated pricing edge only after about 10–20 labelled rolls.

**Q4. Wedge vs moat.**
- The **wedge** is A, run concierge-style.
- The **moat** is the outcome-linked cross-roll dataset. It feeds the retention/price model and C (maintenance benchmarks from pooled job and invoice histories).
- B is how the moat is monetised recurrently, but it depends on PropertyMe and Console permission.
- What stops PropertyMe building it: PropertyMe holds far more data but not transaction outcomes across systems, and its customer data-use terms limit cross-customer analytics on acquisition targets [unverified]. Still, it could ship a "sale-ready pack" quickly. Cotality has market data but no ledgers.

**Q5. Part-time build, capital and timeline.**

| Component | Founder-weeks |
|---|---|
| Ingestion + canonical schema (PropertyMe) | 2 |
| PDF extraction with checksums | 1.5 |
| Trust indicators | 1.5 |
| Flags + Vic policy file | 1.5 |
| Survival model + price band | 2 |
| Report with evidence links | 1.5 |
| Review workflow | 0.5 |
| Security baseline + deletion | 1 |
| Eval harness + synthetic roll with injected defects | 1 |
| **Total productised v1** | **≈12.5** |

- These estimates already assume heavy use of AI coding tools. At 15–20 h/week, that is about **6–8 months part-time**, so not 8–12 weeks.
- A **concierge v0** fits in about 12 weeks part-time (about 5–6 founder-weeks): PropertyMe CSV only, notebooks plus a templated report, no PDFs, no UI, with the founder as reviewer.
- **Cash before revenue:** about A$15–35k. That covers AWS (~A$5k/yr), PI and cyber cover (A$5–10k [unverified]), legal templates for data rights and disclaimers (A$5–15k), backtest data fees and pen test (later).

**Q7. Smallest 90-day test.** Run tests 1, 2 and 4 together.
- **Pass:** one labelled backtest where the model beats the base rate, plus three paid concierge reports.
- **Kill:** no labelled rolls are obtainable, or no one pays A$3k.

## Questions I'd hand to other specialists
- **Legal:**
  - Liability and PI cover for a DD report relied on by lenders.
  - Does a "price band" amount to a valuation requiring a registered valuer?
  - APP 6 limits on a vendor disclosing tenant or landlord personal information during DD.
  - Enforceability of data-retention and outcome-export clauses.
  - The founder's employment-contract IP and moonlighting clauses.
- **Market sizing:** how many rent-roll transactions occur per year in Victoria and Australia, at what sizes, and what valuers and brokers charge for DD and valuation. This sets A's revenue ceiling.
- **Incumbent strategist:**
  - Do PropertyMe's customer terms allow cross-customer analytics or third-party DD products?
  - What is its partner-API approval stance toward a DD vendor?
  - Is Console now owned by Reapit, and what is its export policy?
- **Lending:** do any of the big four or non-bank lenders already use covenant metrics on rolls (loss rate, arrears) that B could automate? What are their vendor-onboarding thresholds?
- **Rent-roll M&A:** will acquirers share past pre-sale and post-sale exports for a backtest, and in exchange for what?

Sources: eliteagent.com and proptechconnect.com (AiMe Connect); softwareadvice.com.au (PropertyMe scale); apis.io / API Evangelist / pypme docs (PropertyMe API); enterprisedna.co (export guides); consumer.vic.gov.au and energy.vic.gov.au (energy standards, trust accounts); vba.vic.gov.au / bpc.vic.gov.au (safety checks); acumentis.com.au (rent-roll valuation); AWS Bedrock docs and blog (AU cross-region); Anthropic model and pricing table (via claude-api skill); soc2auditors.org, scrut.io, spendhound.com (SOC 2 / Vanta costs).
