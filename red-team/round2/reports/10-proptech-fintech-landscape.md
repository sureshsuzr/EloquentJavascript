# PropTech/FinTech Competitive Landscape Analyst: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives if the bundle is cut to landlord-side services tied to transactions.** Every proposed service already has a well-funded Australian owner except two: (a) a PM-bundled, fixed-price maintenance plan and (b) sales-independent investment advice delivered by the manager. The biggest issue is that the US template the thesis resembles (Second Nature's resident benefits package, Belong's resident-facing bundle) makes its money by **charging renters**, and Victoria has largely banned that since 25 Nov 2025. The tenant side of the "super app" is a cost centre and a retention tool in Melbourne, not a revenue line. Tenant products survive only if third parties (lenders, insurers) pay for them. That brings s 48A, the conflict rules and Privacy Act exposure, so they belong in a separate entity, later.

## Verdict on the platform thesis (which services carry the economics, from your lens)
- **They carry it: investment support that ends in a transaction.** That means buying the next property (buyers' agency, which needs the same estate agent licence), hold/sell advice and finance referral. The market already pays here: InvestorKit, a pure investor buyers' agency, reports ~$7.6m revenue and claims 1,850+ clients and 2,600+ purchases. Its revenue roughly doubled in FY24 **[unverified: SmartCompany Smart50 snapshot, year unclear; Business News Australia]**. No PM-only agency in Melbourne sells it with sales independence. This is also the only service that feeds new managements.
- **Second, mainly for retention: a fixed-fee *preventive* maintenance plan.** It is genuine white space in Australia, but it is white space for a reason. Pricing the variance is close to insurance, and old stock selects in. It earns its place by cutting churn (the master variable), not by its margin.
- **They don't carry it:**
  - Priced tenant evaluation: commoditised by Snug, 2Apply, REA Ignite and Domain, and the landlord expects it inside the letting fee.
  - Tenant rent reporting and equity-building: structurally blocked in Australia (see below).
  - Tenant first-home-buyer broking: 81.6% of loans already go through brokers, and Aussie, Mortgage Choice/REA and Domain own the funnel.
  - Moving within the portfolio: a feature, not a product.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

**A1. The US bundle that inspired the thesis is funded by renter fees, which Victoria bans. (High)**
- Second Nature's resident benefits package (RBP) adds services to the lease: renters' insurance, credit building, air-filter delivery, pest control, ID protection and move-in concierge.
- Residents pay **US$20–80/month**, and Second Nature bills the PM only after collection **[verified: secondnature.com/pricing]**. It claims 2,500+ PM customers **[unverified: 2026 aggregator profile]** and has raised ~US$35.9m **[unverified: simplify.jobs]**.
- AppFolio partnered with it in April 2025 and sells "Resident Onboarding Lift, powered by Second Nature" as a **new revenue stream for PMs** **[verified: AppFolio/Nasdaq release]**. US vendor case studies claim +12% PM revenue **[unverified: vendor]**.
- That is the economic engine of the "rental relationship as distribution" idea, and it is under attack even in the US:
  - The FTC fee rule took effect 12 May 2025 **[verified via Clark Hill summary]**.
  - 20+ states had rental junk-fee laws by September 2025 **[unverified: law-firm commentary]**.
  - Colorado HB25-1090 (effective 1 Jan 2026) bars landlords requiring tenants to pay for pest control and common-area utilities, and requires all-in pricing **[verified: KOAA/Otten Johnson]**.
  - Greystar settled for US$24m in Colorado **[verified: Kiowa County Press]**.
- In Victoria, the Housing Statement reforms (in force 25 Nov 2025) ban application fees, background-check fees and rent-payment fees **[verified: CAV news release via search]**. They also create an offence for renters being charged fees by rent-tech platforms. Its commencement is reported as 31 Mar 2026 by one MP **[unverified date; confirm on consumer.vic.gov.au]**.
- **Consequence:** any priced tenant service sold through the PM relationship (the "tenant pays part of the maintenance fee" idea in the brief) must be truly optional. It must not be a condition of the tenancy or of applying, and it should be sold by a separate entity. Once it is optional, take-up falls from ~100% (US mandatory bundles) to low single digits **[estimate: opt-in fintech conversion]**.

**A2. "Rent history as credit evidence" has no rails in Australia. (High)**
- Esusu raised US$50m at a **US$1.2bn** valuation in Dec 2025 on rent reporting **[verified: FinTech Futures/CNBC via search]**. Bilt raised US$250m at **US$10.75bn** in July 2025 **[verified: Reuters/Bloomberg Law]**.
- Both depend on US bureaus accepting rent tradelines, and the UK equivalent (Experian Rental Exchange, CreditLadder) depends on UK bureaus.
- In Australia, a landlord receiving rent is **excluded from the "credit provider" definition** under the Privacy Regulation (2014). Comprehensive credit reporting (CCR) under Part IIIA has no rent field **[verified in part: Bright Law summary of the regulations; confirm on current legislation.gov.au]**.
- I found no Australian bureau product that takes positive rent data **[unverified absence]**. The only rental data in circulation is negative: tenancy databases such as TICA and NTD.
- So the US "credit-builder" product can't be built. What can be built is a **verified rent ledger accepted by lenders as genuine savings**. That is a niche broker feature, already informally available from any PM's ledger.

**A3. Tenant equity and the first-home pathway: rent-to-own failed here, and the government ate the deposit gap. (High)**
- **OwnHome** raised ~$31m (Square Peg, CBA x15) for rent-to-own. It **pivoted in 2022–23 to a Deposit Boost loan** and reported only ~$5m of deposit loans approved **[verified: Forbes AU/OwnHome release; date of the $5m figure unclear]**. That is the closest Australian test of "help renters build equity", and the market rejected the equity-building version.
- From **1 Oct 2025** the 5% Deposit Scheme is uncapped, has no income caps and has higher price caps **[verified: Treasury/JLL/Finder]**. Help to Buy (shared equity) opened in December 2025 in participating states **[unverified year/state participation; Victoria's status needs checking]**. A 5% deposit with no LMI is now free from government via any broker, which removes most of the reason for a private "deposit pathway".
- Distribution is owned:
  - Brokers write **81.6%** of new home loans (June 2026 quarter) **[verified: MFAA/Cotality via MPA, Banking Day]**.
  - Aussie (Lendi) took back the No. 1 brokerage spot from Mortgage Choice (REA-owned) in 2026 **[verified: The Adviser Top 25]**.
  - REA also runs realestate.com.au Home Loans/Smartline **[verified, older]**.
  - CoStar completed its ~US$1.6bn Domain takeover on 27 Aug 2025 **[verified: SEC 8-K/10-K]** and will bring Apartments.com-style renter monetisation.
- **The tenant-to-buyer funnel is the most crowded lane in the brief.**

**A4. Priced tenant evaluation is commoditised and the payer is wrong. (Med–High)**
- Snug (bought PMS Rentbook, ~4,000 properties) **[unverified date: CB Insights]**, 2Apply, REA Ignite and Domain all give agents free application and screening flows, funded by renter-side upsells or listing revenue.
- Victoria bans screening fees on renters, and the March 2026 standard application form limits the data collected (round 1).
- A landlord-paid "risk score" competes with services landlords believe are already in the letting fee. Its value is real (reducing arrears and VCAT), but it should be bundled into the management offer and priced through the letting fee, not sold as a SKU. There is also an ADM transparency risk from 10 Dec 2026.

**A5. Fixed-fee maintenance: white space, but white for a reason. (Med)**
- I found **no Australian PM offering a fixed annual maintenance fee that absorbs repair variance**. Australian "home warranty" activity is limited to appliance-warranty retailers and small subscription operators like HomeKeep (Sydney, ~$500–1,500/yr indicated) **[unverified: vendor blogs]**.
- In the US, home warranties are a large, low-NPS category. Belong deliberately chose **"no markup, pay actual cost"** plus a capped rent guarantee (Standard tier 5% management, 55% placement), not fixed-fee maintenance **[verified: belonghome.com, self-reported]**. Belong is a 2017-era, ~US$105–138m-funded company **[conflicting: CB Insights / others]**, and it still didn't take maintenance variance onto its own balance sheet. That is telling.
- Incumbents are moving towards risk products. hipages bought 51% of **VIZ Insurance** for $1.4m (Apr 2026) and flagged insurance for its homeowner base **[verified: ASX/Business News Australia]**. It already holds 25% of Bricks + Agent (agency maintenance workflow) **[verified: iTnews 2021]**.
- The fastest-moving competitor for a maintenance plan is therefore a tradie marketplace with an insurance arm, not another PM.

**A6. US full-stack tech-PM economics are weak; the Australian D2C version pivoted. (Med)**
- **Mynd** raised ~US$205m and was **folded into Roofstock in May 2024** at an undisclosed price **[verified: Roofstock release/Moomoo]**.
- Belong has no round since its May 2022 Series C (US$50m equity in an US$80m debt+equity package) **[verified: TechCrunch]**. It reports 20 states/56 metros **[self-reported]** and 68 BBB complaints in three years **[unverified]**.
- Australia's :Different (~$100/month flat fee) launched **"Different for Agencies"** and a rent-roll management partner programme **[verified: Elite Agent; date unclear]**, which is a B2B pivot.
- The pattern: tech-PM D2C acquisition is expensive. Survivors monetise **owners' transactions and risk products**, not tenants.

**A7. Incumbents will copy whatever is software. (Med)**
- PropertyMe launched AiMe Connect (Claude/ChatGPT on live data) on 8 Oct 2026, with "agentic AiMe coming next" **[verified: Elite Agent/PropTech Connect]**.
- MRI bought Melbourne's Proptech Labs in Oct 2025 **[verified: Mann Report]**.
- Ailo has LJ Hooker (Mar 2025) and Ray White network partnerships **[verified]**.
- Snug is moving into PMS. Cotality and PropTrack already sell portfolio monitoring and investment reports to agencies **[verified: cotality.com]**.
- **Portfolio analytics as a dashboard is copyable in under 12 months.** Advice given by a licensed person without a sales conflict is not.

## Things the brief gets wrong, misses or understates
1. **It treats the tenant side as revenue.** In Victoria it is a cost and a retention lever. US benchmarks (Second Nature, Bilt, Esusu) don't transfer because the fee rails (A1) and credit rails (A2) aren't there.
2. **It omits buyers' agency, the obvious monetiser of "buying the next property".** A Victorian estate agent licence covers it. Fees typically run 1.5–2.5% or $10–25k per purchase **[estimate: Melbourne market norms]**. One purchase is worth ~5–10 years of management fees on one property.
3. **"Help them find another place within the portfolio" is a feature, not a product.** At 250–2,500 managements in a six-postcode core, the chance a moving tenant's needs match a vacancy you control in the right week is small: maybe 5–10% of moves **[estimate: vacancy count × match rate]**. Its value is cutting letting days, not revenue.
4. **It misses Victoria's investor exodus.** Higher land tax and the 2025 reforms push "sell" decisions. Independent hold/sell advice will often recommend selling, which kills a management. The investment service has to own the *recycling*: sell, then buy elsewhere and stay managed (including interstate via partner PMs), or it accelerates churn.
5. **"Openn?" and "Propell?" in the role brief:**
   - Openn is an online auction/offers platform for sales, irrelevant to PM **[verified: openn.com]**.
   - I could not verify any "Propell" property-investment app **[unverified: treat as non-existent]**.
   - Tic:Toc is now **Tiimely Home**, a direct lender funded by Bendigo, not a renter product **[verified: Canstar]**.
6. **Rent.com.au is the closest Australian "renter fintech" comparable, and it is tiny:**
   - FY25 revenue ~A$3.3m, loss ~A$3.7m **[unverified: aggregator summary of FY25 report]**.
   - RentPay had ~10k active users (Sep 2024 quarter) **[verified: Online Marketplaces]**.
   - It pivoted towards RentBond.
   - It is a decade-old public company, and its renter payments model now faces the fee ban.

## Numbers checked (table: claim | finding | status/source)
| Claim | Finding | Status/source |
|---|---|---|
| US resident-bundle pricing | Residents pay US$20–80/mo; PM billed after collection | verified: secondnature.com/pricing |
| Second Nature scale | 2,500+ PM customers; ~US$35.9m raised; "US$121.7m revenue" | unverified (aggregators) |
| Belong funding | US$80m (US$50m Series C + debt), May 2022; no later round found | verified: TechCrunch; later rounds unverified absence |
| Belong fees | 5% mgmt / 55% placement (Standard); rent guarantee capped (US$9k–15k) | verified, self-reported (belonghome.com) |
| Mynd | ~US$205m raised; merged into Roofstock May 2024 | verified: Roofstock release; funding total unverified |
| Bilt | US$250m at US$10.75bn, July 2025; pushing into mortgages | verified: Reuters/Bloomberg Law |
| Esusu | US$50m Series C at US$1.2bn, Dec 2025 | verified: FinTech Futures/CNBC |
| AU rent reporting | Landlords excluded from "credit provider"; no positive rent data in CCR | verified in part (Bright Law on regs); no AU product found |
| OwnHome | ~$31m Series A (Square Peg, CBA x15); pivoted from rent-to-own to Deposit Boost | verified (Forbes AU, OwnHome) |
| 5% Deposit Scheme | Uncapped, no income caps, from 1 Oct 2025 | verified: Treasury/JLL/Finder |
| Broker share | 81.6% of new home loans, June 2026 qtr | verified: MFAA/Cotality via MPA |
| Top brokerage | Aussie (Lendi) No. 1 in 2026, displacing Mortgage Choice | verified: The Adviser |
| Domain ownership | CoStar 100%, closed 27 Aug 2025, ~US$1.6bn | verified: SEC 8-K/10-K |
| Victorian fee bans | Application, background-check, rent-payment fees banned from 25 Nov 2025; rent-tech fee offence (31 Mar 2026?) | verified (CAV via search); platform-offence date unverified |
| hipages → insurance | 51% of VIZ for $1.4m, Apr 2026 | verified: ASX / BNA |
| MRI in Melbourne | Acquired Proptech Labs, Oct 2025 | verified: Mann Report |
| PropertyMe AI | AiMe Connect live 8 Oct 2026; agentic "next" | verified: Elite Agent |
| :Different | ~$100/mo flat; launched agency/rent-roll partner programme | verified (Domain, Elite Agent); PUM unknown |
| InvestorKit | ~$7.6m revenue; 2,600+ purchases claimed | unverified (Smart50, self-reported) |
| Rent.com.au | FY25 rev ~A$3.3m, loss ~A$3.7m; RentPay ~10k actives | partly verified |
| Tic:Toc | Now Tiimely Home, Bendigo-funded direct lender | verified: Canstar |
| "Propell" | No such AU investor app found | unverified |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Rebuild the offer as "PM + Landlord Wealth Desk", not a super app.** The desk sells:
   - annual hold/sell/refinance reviews, free to managed landlords (retention);
   - **buyers' agency** on a fixed fee ($8–15k, below the market's 2% norm) **[estimate]**;
   - managed referral to a *separately licensed* broker (Australian credit licence), with consent and disclosure, and any s 48A-caught benefit rebated.
   
   Unit economics: per 1,000 landlords, a 3% purchase rate × 40% capture ≈ 12 purchases × $12k ≈ **$144k/yr**, plus 12 new managements and broker share **[estimate]**. That is worth more than the whole referral-fee line in round 1 (~$75k).
2. **Turn "sell" into "recycle".** Pair every sell recommendation with a reinvest plan (buyers' agency, possibly interstate, managed through partner PMs on a referral basis). Then the independence edge stops being churn-accretive. Track "management retained or replaced within 6 months of sale".
3. **Launch maintenance as a capped *preventive* plan, not a variance-absorbing fee.**
   - Fixed annual fee for scheduled servicing: smoke alarms, gas/electrical safety checks (Victorian minimum standards), gutters, HVAC, hot water service.
   - Repairs at no markup, with a per-event cap and exclusions.
   - Property-condition entry gate.
   - Don't split it with the tenant.
   - Revisit full variance only after 24 months of your own cost data, and with an insurer partner. Don't self-insure, because of APRA risk.
4. **Drop priced tenant evaluation as a SKU.** Embed the scoring in the letting fee and market it as "lower arrears, fewer VCAT days", reporting those numbers in the landlord's statement.
5. **Tenant side: one free, low-cost product.**
   - "Your verified rent ledger + 5% Deposit Scheme checklist", with an opt-in hand-off to a third-party broker.
   - No renter fees, no credit-builder promise.
   - Its purpose is tenant NPS, fewer vacancies and longer tenancies, and a list of future buyers.
6. **Don't chase US analogues' capital structures.** Mynd and Belong show that VC-funded full-stack PM struggles. Stay owner-operator funded, as round 1 recommended.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)
| Test | Metric | Threshold to proceed | Timeframe |
|---|---|---|---|
| Wealth Desk demand: offer a free hold/sell/refinance review to 200 landlords in the acquired book or the corridor investor list | Review uptake; % with a transaction intent in 12 months | ≥25% uptake; ≥8% intend to buy within 12 months. Kill if <10% / <3% | 90 days |
| Buyers' agency conversion | Paid mandates per 100 reviews | ≥3. Kill if <1 | 6 months |
| Sell-advice churn | Managements lost to sale vs retained/replaced via recycle | ≥40% replaced. Kill independence-advice framing if <15% | 12 months |
| Preventive maintenance plan | Landlord take-up at ~$600–900/yr **[estimate price]**; loss ratio | ≥20% take-up; claims+servicing ≤75% of fees. Kill if take-up <8% or loss ratio >100% | 12 months, 100+ plans |
| Tenant ledger + FHB hand-off | Opt-in rate; broker settlements | ≥15% opt-in; ≥1 settlement per 200 tenancies/yr. Else keep only as a retention feature | 12 months |
| Copy-speed watch | PropertyMe/Ailo/Snug release of investor-review or maintenance-plan features | If shipped free within 12 months, don't build software; compete on licensed advice | Quarterly |

## Answers to the round-2 questions in my domain
1. **The one or two services, and in what order:**
   - First, **investment support that ends in a buyers' agency/finance transaction**: market-proven willingness to pay, the same licence, feeds managements, and the independence edge applies.
   - Second, a **preventive maintenance plan** as a churn reducer.
   - Everything tenant-side comes later, free, and as retention.
2. **LTV:**
   - A managed landlord is worth ~$1.86k/yr ex-GST in fees **[round 1]**, plus ~$140–180/yr expected transaction margin averaged across the book (from the Improvement 1 estimate), plus retention value from the maintenance plan. That is ~+10–20% per-landlord value **[estimate]**.
   - It lowers the $500k-draw scale from ~2,000–2,500 to perhaps ~1,700–2,100 properties. It **doesn't change the order of magnitude**.
   - A tenant relationship is worth ~$0–50/yr in direct revenue in Victoria **[estimate]**. Its value is shorter vacancies and lower arrears, which accrue to the landlord fee.
3. **Regulated services and conflicts:**
   - Credit licence for broking. Use a separate licensee; don't have the PM give credit assistance.
   - Insurance/APRA for variance-absorbing maintenance or rent guarantees (Belong's model).
   - Victoria's renter fee bans apply to any priced tenant service sold through the tenancy.
   - **Disqualifying:** a mandatory resident bundle (US RBP) in Victoria, and rent-reporting-for-credit claims.
   - **Manageable:** buyers' agency for the same landlord with disclosure; broker referral with consent and rebate.
4. **Autonomy:** outside my lane. Note only that PropertyMe's agentic layer is "next" and AiMe Connect is read-only; autonomy is becoming vendor-supplied and will not differentiate.
5. **Founder edge:**
   - **Decisive** in landlord investment analytics: hold/sell/refinance with tax, land tax and yield maths, explained by a CFO. Also in pricing maintenance risk from own data.
   - **Irrelevant** in tenant fintech, where rails, not models, are the constraint.
6. **Smallest test:** the 200-landlord Wealth Desk review above. If fewer than 3% of reviewed landlords commit to a paid transaction within six months, the platform thesis reduces to round 1's PM specialist.

## Questions I'd hand to other specialists
- **Lawyer:** Does s 48A or the conflict rules catch (a) a buyers' agency fee from your own managed landlord, and (b) a broker commission share for a *tenant* referral? The tenant isn't the agent's client. Does the Vic rent-tech fee offence catch an optional, separately contracted tenant product?
- **Insurance/regulatory:** At what design point does a fixed-fee maintenance plan become insurance (Insurance Act / APRA, or a financial product under the Corporations Act)?
- **Credit specialist:** Will any Australian lender formally accept a PM-verified rent ledger as genuine savings? Is any bureau piloting positive rent data under the Credit Reporting Code?
- **Market analyst:** What is the Melbourne inner-north investor purchase and sale rate per 1,000 landlords (2024–26)? What share of sellers reinvest?
- **CFO/modeller:** Re-run the $500k-draw scale with the Wealth Desk revenue and a 1–2 point churn reduction from maintenance plans.
