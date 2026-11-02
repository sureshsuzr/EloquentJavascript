# Go-to-Market & Distribution Lead: red-team report

## Verdict
**Survives-if.** A per-report due-diligence product (A) sold to Australian roll buyers is a real wedge but a **small market**: roughly 250–500 brokered roll transactions a year nationally [estimate, below], which supports about **$0.5–1.5M of revenue at a dominant share**. That's a good consultancy, not a business that beats $500k plus equity. It only survives if A is used to (1) collect **post-acquisition outcome data** nobody else has, and (2) open a **recurring** channel: retention monitoring for multi-office acquirers and franchise HQs (B), then the UK, where lettings-book M&A is far deeper. **Biggest issue:** demand is triggered by transactions, so it's lumpy and gatekept by a handful of rent-roll brokers paid on % of price. A tool that marks prices *down* is a threat to them. The way through is to sell **vendor-side certification** ("prove your roll is clean"), not buyer-side discounting.

## Verdict on the software business
- **Wedge: A, repositioned as a two-sided "Verified Roll" report.** Vendors and brokers pay for it to justify a top-of-range multiple and shorten the settlement/retention dispute. Buyers pay for a deeper version on live deals. The decision is founder-sellable in 1–4 weeks by a single principal.
- **Business: B, retention and book-health monitoring sold by subscription** to serial acquirers, then franchise HQs. It's the only recurring line with enough property count to reach $3M+ ARR.
- **Moat: the outcome dataset.** Each report is followed by 12–24 months of tracking what actually churned after transfer. Neither brokers (who have anecdotes) nor PropertyMe (who sees one side of the migration) holds that labelled set.
- **C (maintenance)** is a second-phase data product for insurers and maintenance platforms. It isn't the entry point, because GTM into insurers takes 6–12+ months and needs volume we won't have in year 1.
- **D (agentic integration)** is a services upsell after A. StaffLink already sells an "Acquisitions Base" offshore integration team [verified: stafflink.com.au search result]. Don't lead with it.
- **Banks are not an entry channel** (see attacks). Reach them through panel valuers.

## Attacks on the thesis

**1. The Australian transaction market is too thin for a per-report business (High).** Real Estate Dynamics, probably the largest broker, transferred **10,264 properties in a year** across NSW/Qld/Vic, and only **1,292 in Victoria** (FY22). The median Victorian roll was worth **$310,001**, and **44% of portfolios sold had fewer than 80 properties** [verified: Elite Agent coverage of RED 2021–22 report, via search summary]. At Victoria's $1,132 average annual management income and a ~2.8x multiple, the median roll is ~100 properties [estimate]. So RED's Victorian volume is ~13 brokered deals a year. Grossing up for other brokers, off-market and in-network franchise sales gives perhaps **250–500 transactions/yr nationally** [estimate; no current public count exists, the most recent public data is FY22]. At $5k average and 40% share, that's **$0.5–1.0M revenue**. Market volume is also falling: brokers describe 40–50% downturns for some businesses, and 2026 commentary says new-management pipelines are slower [unverified dates]. Small rolls (<80 PUM) can't bear a $5k report on a ~$250k deal. Willingness to pay is concentrated in the top quartile of deals.

**2. Broker channel conflict (High).** Brokers are paid by the vendor on a % of price [estimate: business brokers 5–12%, and no published rent-roll broker rate found; likely lower, ~3–6%, unverified]. They control the information memorandum and data-room access. A buyer-side tool that knocks 0.3x off a multiple costs the broker commission and the vendor relationship, so brokers will delay data, steer buyers away from it, or build a lite version themselves. RED-type firms already sell "benchmarking" and valuations.

**3. Contracts already partly hedge retention risk (Med).** Standard deals hold back **5–10% of price for a 3–6 month retention period** [verified: legal guide via search, described as a rough guide]. The buyer's marginal question isn't "what is retention?" but "what is attrition *after* the retention period, and is the clawback correctly calculated?". The brief's "$100k on a $2M roll" ignores that part of the error is already contractually shifted. The real value lies in months 6–36 and in mis-specified clawbacks. That's still real, but the pitch must be sharper.

**4. Bank "per-loan pull" is a mirage in year 1–2 (High for that channel).** Rent-roll lending is a niche (NAB lends to 70% LVR against "suitable" rolls) [verified: nab.com.au]. Credit-policy changes to mandate a third-party report take 9–18 months. Vendor onboarding drags in CPS 234 info-sec and, since the CPS 230 transition ended (**pre-existing contracts caught from the earlier of renewal or 1 July 2026; amended CPS 230 commenced 1 July 2026**) [verified: APRA and law-firm summaries via search], operational-risk and third-party due diligence. A model used in credit decisions also triggers bank model-risk validation. A two-person startup won't clear that within 12 months. Banks already rely on panel valuers (Acumentis applies **~2.0–3.3x** to management fees using sales evidence [verified: acumentis.com.au]). **Workaround:** license the engine to a panel valuer, who carries the bank relationship and liability.

**5. PropertyMe can own B, not A (Med).** PropertyMe's AiMe sits on the trust account, tenancies and workflows, and **AiMe Connect** exposes PropertyMe data through MCP prompts [verified: propertyme.com.au]. Single-agency book-health dashboards (arrears, vacating landlords) are a natural feature for them. B sold to single agencies will be commoditised within 18–24 months. A is episodic, works across systems (vendor on Console, buyer on PropertyMe), and needs post-transfer outcomes, so it's a poor fit for a PM-software roadmap. **Implication:** B must be sold where PM software doesn't sit, to *multi-office groups and franchise HQs* that run mixed systems and need cross-office comparison.

**6. Franchise HQ sales are slow and politically fraught (Med).** Network scale is large: Ray White ~1,000 offices AU/NZ [verified: raywhite.com]; LJ Hooker ~480–700; Harcourts 400+; Belle ~80–200 [unverified, conflicting]. But offices are independent businesses. They will resist HQ visibility into book health, because HQ could use it to push sales, roll mergers or royalty audits. Expect 6–12 months to a paid pilot, office-level opt-in, and an HQ demand for white-label or revenue share. This is a year-2 revenue line, not a first-10-customers line.

**7. Founder network fit is partial (Med).** LocalAgentFinder relationships are with **sales** agents and principals. Roll decisions sit with principals and BDMs/heads of PM, which overlaps but isn't the same. Some principals saw LAF as a referral-fee intermediary, so its reputation may cut both ways [unverified]. Round 1 also flagged a possible **LAF restraint** that must be checked before using that network.

**8. Possible licensing trap in pricing (Med, legal to confirm).** In Victoria, negotiating the sale of a business (a rent roll is one) for reward is estate-agent work. A **success fee as % of transaction** could look like acting as agent. Price per report or subscription, never contingent on completion.

## Things the brief gets wrong, misses or understates
- **It misses the sell side.** Vendors preparing for sale (listed as a customer type, but under-weighted) are the *easiest* payer. Clean rolls want a signal (positive selection), and once enough clean rolls certify, non-certified rolls get discounted. That turns broker conflict into broker alignment.
- **Retention holdbacks** (5–10%, 3–6 months) change the value proposition (attack 3).
- **Transaction volume is unknown and possibly falling.** The brief assumes a market. The latest public count is FY22. A deal-flow count is the first test.
- **"Lenders create pull" is overstated** for Australia within 24 months (attack 4).
- **Panel valuers** are an unnamed channel and probably the best route to lenders.
- **The UK is understated.** It may be the larger A market, not an "expansion". Dwelly has done ~8 acquisitions in 2026 after a **£69m** raise. Lomond made 6 London deals in 11 months. LSL and Foxtons buy lettings books (Foxtons paid £2.2m for one west London agency) [verified: lettingagenttoday.co.uk, thenegotiator.co.uk, primeresi.com headlines via search]. The **Renters' Rights Act phase 1 started 1 May 2026** (s21 abolished, periodic tenancies), with the Landlord Database and Ombudsman due from late 2026 [verified: Propertymark/IFA via search]. That raises compliance cost and pushes small agents to sell. UK buyers are PE-backed and already pay accountants for financial DD, so budgets exist. A UK broker-built valuation tool already exists, back-tested within 10% on £1.1–8.7m deals [verified: The Negotiator headline/snippet], so price-only tools are not novel there either. Retention outcome modelling is the differentiator.

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| Melbourne multiples ~2.8–3.5x mgmt income | Valuer range 2.0–3.3x; Sydney example 3.05x; regional NSW low-to-high 2s | [verified: acumentis.com.au; search summaries]. Brief's top end (3.5x) looks high for typical Vic rolls |
| Vic AAMI | $1,132 (FY22, lowest of three eastern states) | [verified: RED via Elite Agent search summary], stale |
| AU roll transaction volume | RED: 10,264 properties in a year (3 states), 1,292 Vic; 44% of rolls <80 PUM; median Vic roll $310k | [verified, FY22]; national 250–500 deals/yr is [estimate] |
| Retention holdback | 5–10% of price, 3–6 months | [verified: legal guide, rough] |
| Bank rent-roll LVR | NAB up to 70% | [verified: nab.com.au] |
| CPS 230 timing | In force 1 Jul 2025; legacy contracts by earlier of renewal or 1 Jul 2026; amendments commenced 1 Jul 2026 | [verified: APRA/law firms via search] |
| Managed stock AU | ~2.7M rentals × ~80% agent-managed ≈ 2.2M (c.2021); other quotes 3.25–3.3M rentals | [verified quote: REIA via search]; current figure [estimate 2.2–2.6M managed] |
| Ray White offices | ~1,000 AU/NZ | [verified: raywhite.com]; PUM 200k claim [unverified, blog] |
| PropertyMe AI | AiMe + AiMe Connect (MCP) on PM data | [verified: propertyme.com.au] |
| UK consolidation | Dwelly £69m, ~8 deals 2026; Lomond 6 in 11 months; RRA from 1 May 2026 | [verified: trade press headlines via search] |
| UK book multiples | Not found publicly | [unverified] |

Several trade sites (eliteagent.com, console.com.au, thenegotiator.co.uk, propertyindustryeye.com) were blocked from this session. Figures from them come from search summaries.

## Improvements (ranked by impact)
1. **Lead with the vendor-paid "Verified Roll" report, distributed through 1–2 brokers.** Price $2–4k, paid by the vendor and bundled into the information memorandum. Brokers get faster deals and fewer clawback disputes, and the founder gets data from every listed roll, including ones that don't sell. This turns the biggest channel conflict into the main channel.
2. **Instrument every report for outcomes.** Contract the right, with buyer consent, to track the acquired book at 6/12/24 months for a reduced-price monitoring tier. That data is the moat and the bridge to B.
3. **Sell B to serial acquirers first, franchise HQs second.** Target the ~20–40 groups buying 2+ rolls a year [estimate]. Bundle: unlimited screening + buyer DD + 24-month post-acquisition retention monitoring at **$15–40k/yr**. Franchise HQ enterprise tier: **$50–150k/yr**, paid pilot at $25–50k, office opt-in.
4. **Use panel valuers as the lender channel.** License the engine to one rent-roll valuer ($10–25k/yr plus per-use). The valuer carries bank panel status and professional indemnity.
5. **Price per report or subscription, never as a success fee** (licensing). Tier by roll size: $2.5k (<150 PUM), $5k (150–500), $9k+ (>500). Offer a $500 quick screen to capture top-of-funnel data.
6. **Build ingestion for UK systems (Reapit, Alto, Street, Arthur) by month 9** and test UK demand with 2–3 consolidators remotely. If a UK PE-backed buyer pays £5–15k per report, the UK becomes the main A market.
7. **Founder-led content, not booths.** Publish a quarterly "Roll Retention Index" (anonymised outcome data) through Elite Agent / Real Estate Business, and speak at PM-specific events rather than AREC (sales-agent-heavy and expensive). The 2027 dates weren't verifiable.
8. **Integration partnerships:** become a listed PropertyMe/Console/Rex integration partner for authorised exports (DD needs only one-off exports, not live write access).

## Tests & kill criteria

| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| Deal-flow count via 3 brokers + 10 serial acquirers | Brokered AU transactions/yr; share >150 PUM | ≥250 deals/yr and ≥40% >150 PUM, else A is a consultancy | Days 0–30 |
| Paid concierge DD on live deals | Paid reports at ≥$3k | ≥5 paid in 90 days; 0–2 = kill A as buyer-side product | Days 0–90 |
| Broker pilot | Top-4 broker signs vendor-certification pilot | ≥1 broker, ≥5 listings certified | Days 30–90 |
| Back-test | Historic rolls with 24-month post-transfer outcomes; model vs multiple-based expectation | ≥8 rolls; model cuts 12–24m attrition error by ≥3 pts | Days 30–90 |
| Serial-acquirer subscription | Annual contract ≥$15k | ≥2 by month 6, else B via acquirers is dead | Month 6 |
| Franchise HQ | Paid pilot ≥$25k | ≥1 by month 9–12, else drop HQ channel | Month 12 |
| UK signal | Paid UK report or LOI | ≥1 by month 9 | Month 9 |

## Answers to the round-3 questions in my domain

**Q1. Who pays, how much, how often, is it big enough?**
- Year-1 payers:
  - roll buyers and vendors: $2.5–9k per deal, episodic;
  - serial acquirers: $15–40k/yr;
  - one valuer licence: $10–25k.
- Year-2+: franchise HQs at $50–150k/yr.
- Realistic AU ceiling from A + B to acquirers ≈ **$1.5–3M ARR** [estimate].
  - Beating $500k + equity needs B at network scale (e.g. 300k PUM × $0.40/month ≈ $1.4M) plus the UK.
- Year-1 plan:
  - 12 DD/certification reports (~$50k)
  - 3 acquirer subscriptions (~$75k)
  - 1 valuer licence (~$15k)
  - 1 HQ pilot (~$30k)
  - Total ≈ **$170k revenue, ~$150k exit ARR**.
- Year 3 plausible: $1–2M ARR. Exit at 4–6x ARR is **$4–12M by year 4** [estimate].
- **This doesn't beat the salary on a 4-year view unless the UK or a franchise network converts.** Upside case: $4M+ ARR by year 5, worth $16–30M.

**Q4. Wedge and moat.**
- **Wedge:** vendor-side Verified Roll report through brokers, plus buyer DD.
- **Moat:** the post-transfer outcome dataset, plus embedded monitoring at serial acquirers.

**Q7. 90-day test.** Run the deal-flow count, ≥5 paid DD reports, one broker pilot and an 8-roll back-test. All four are achievable part-time *only if* employment and LAF restraints are cleared first (not my lane). Founder-led selling needs ~8–10 hours a week of calls during business hours, which is the practical constraint while employed.

**First 10 paying customers (sequenced):**
- 1–3: Melbourne roll buyers on live deals, sourced from the LAF principal network and brokers. Concierge DD at $4–6k, model plus manual review.
- 4–5: two brokers on vendor certification (6+ reports).
- 6: one panel rent-roll valuer licence.
- 7–8: two serial acquirers on annual subscription with monitoring.
- 9: one franchise HQ paid pilot (20 offices).
- 10: one UK consolidator, or one landlord insurer data-partnership pilot (C).

## Questions I'd hand to other specialists
- **Legal:** Does a fee contingent on a roll sale, or vendor-side certification marketed to buyers, constitute estate/business-agent work under the *Estate Agents Act 1980* (Vic)? What's the liability exposure if a certified roll underperforms (misleading conduct under the ACL)? Does an LAF restraint bind?
- **Data/privacy:** Can vendor exports including landlord and tenant personal information be processed for DD without new consent? Can outcome tracking continue after transfer under APP 6?
- **Modelling:** With ~8–30 labelled post-transfer rolls in year 1, is the retention model better than a broker's judgement, or just better-dressed?
- **Competition/strategy:** Would PropertyMe or Cotality acquire this at ~$2M ARR (an exit path) or clone B?
- **UK specialist:** UK lettings-book multiples, annual deal counts, and whether PE buyers' FDD providers would partner or compete.
