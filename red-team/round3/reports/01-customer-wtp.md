# Buyer & Willingness-to-Pay Researcher: red-team report

*2 November 2026. Web fetches to acumentis.com.au, nab.com.au and eliteagent.com were blocked from this session, so several figures rest on search-result summaries and are labelled accordingly. Searches used: 19.*

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)

**Survives only if it is sold to repeat capital, not to one-off agencies.** Australian rent-roll transactions are a small, lumpy market: roughly 400–900 deals a year worth about $250–550M [estimate]. Even at full penetration, per-deal DD fees cap out at about $3–8M a year. A realistic Australian ARR ceiling across products A+B is about **$1.5–3M within five years**. That is a good small business, not a clear beat on a $500k salary plus executive equity. **The single biggest issue:** the people with real willingness to pay are 20–40 serial acquirers, franchise HQs and the funded consolidators (Managex in Australia; Dwelly and Lomond in the UK). They want the edge **exclusively**. Selling it to everyone erodes the very mispricing it detects. The business survives if it is (a) priced against value at risk, not as a report; (b) built on a post-acquisition retention-outcome dataset no one else has; and (c) taken to the UK within about 24 months, or used as the engine of a capital-partner vehicle.

## Verdict on the software business (which product, if any, is the business, from your lens)

- **A (rent-roll intelligence) is the wedge.** It is the only product where the pain is acute, dated (a live deal) and quantified ($50–150k at risk per $2M roll). **But it is not, on its own, a business** in Australia, because volume and frequency are too low.
- **B (retention monitoring) is the recurring revenue and the moat-builder.** Sell it only as a **post-acquisition** follow-on (the buyer tracks the roll it just bought) and to franchise HQs and lenders. **Do not sell it cold to agencies.** PropertyMe's "50+ insights", MRI Real Benchmark and Reapit/Console reports already occupy the "book-health dashboard" slot, and agency willingness to pay for analytics is low.
- **C (maintenance) has no paying buyer in Australia yet.** Landlord insurers pay claims for damage and lost rent, not wear-and-tear maintenance, so their willingness to pay for maintenance-cost prediction is weak. C is a data asset that feeds A (fee-quality and landlord-churn drivers), build-to-rent operators and a future insurer-backed plan. It is not a standalone product to sell in 2027.
- **D (agentic DD / integration) is services revenue that funds A.** Integration is where buyers actually feel pain after settlement, and they pay consultant rates for it. It is useful cash flow and a source of outcome data, but it doesn't scale.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

1. **The market is small and infrequent. Severity: High.**
   - About 2.7M rentals, ~80% agent-managed [verified: REIA strategy card 2024; industry estimate], gives ~2.2M managements.
   - If 3–5% change hands a year, that is ~65–110k managements at ~$4.7–6.1k each, or **$300–550M/yr** [estimate].
   - The cross-check by deal count lands in the same range: ~400–900 deals × median ~$470k [verified as 2021–22 eastern-seaboard median: Elite Agent, via search summary; stale].
   - A typical agency buys a roll every 2–5 years, so most "customers" are one-off. There is no recurring relationship and CAC is high relative to a ~$5k ticket.
   - **Ceiling for per-deal DD revenue:** 600 deals × 50% share × $5–10k = **$1.5–3M**. Realistic share in years 1–3 is 10–25%, or **$0.3–1.2M**.

2. **The $100k-per-$2M-roll value claim is overstated before retention clauses. Severity: High.**
   - Australian roll contracts commonly include a **retention/adjustment period**: the price is reduced for managements lost in the first ~3–6 months, sometimes with retentions held back [unverified as a frequency; widely described practice].
   - That clause already transfers the early-churn risk the model prices. The model's real value is in losses in months 6–36, plus fee-quality and arrears flags.
   - **Fix:** interviews must establish typical clause terms. Re-run the value-at-risk sum on months 6–36 only; it may be about half the brief's figure.

3. **The edge leaks if it is sold. Severity: High.**
   - The round-2 thesis was that the founder, as acquirer, captures mispricing. Selling the same model to every buyer and broker spreads the information, compressing the spread on good books and lowering prices on bad ones.
   - The highest-WTP buyers (serial acquirers, PE) will pay for exclusivity or build in-house. Dwelly raised ~£69m in Feb 2026 plus a ~$170m (US$) Series B in Jul 2026 and is AI-native [verified: Goodwin press release, Multiples, BusinessCloud via search; amounts differ across sources]. Dwelly will not buy third-party DD.
   - **Implication:** the defensible model is either (i) exclusive or territorial licences at high prices, or (ii) a data network whose value grows with outcomes (see Improvements 1–2). Commoditised PDF reports are the wrong model.

4. **Banks don't pay for roll valuations today. Severity: Med–High.**
   - Macquarie reportedly lends to ~70% of roll value "determined by internal Macquarie Multiplier (no cost to client)", amortising to 60% within 3 years [unverified: mortgagechoice.com.au broker summary].
   - NAB lends up to 70% LVR (one page says 80%, 10-year terms), with a minimum of 100 residential properties and 2.5x interest cover [verified via search snippets of nab.com.au and a 2024 NAB flyer; the conflict between 70% and 80% is unresolved].
   - Banks treat rolls as a niche inside business banking: few loans, low losses, and a free internal multiplier. A new vendor faces model-risk review, vendor-risk assessment and a 12–24-month procurement. The per-loan fee pool is ~300–500 new loans × $1–3k = **<$1.5M** [estimate].
   - **Where lenders might pay:** covenant monitoring on the existing book (likely ~2,000–4,000 facilities nationally [estimate]). But this needs the *borrower's* consent and data feed, so it only works if the borrower already uses product B.
   - **Better lender buyers:** specialist or non-bank lenders and private credit wanting to grow in rolls without in-house expertise.

5. **Brokers are paid by vendors on price. Severity: Med.**
   - Generic business-broker fees run ~5–12% of sale price [verified: BusinessForSale]. Rent-roll-specific rates were not found [unverified].
   - A buyer-side tool that discounts the price is hostile to the broker, who controls information-memorandum (IM) and data-room access.
   - **Flip it:** sell brokers a *vendor-side* "verified book quality" report that lets good books command a premium and close faster. Adverse selection, where only good books publish, becomes the product's signalling value.

6. **Agency SaaS (B) fights for a crowded, low-WTP budget line. Severity: Med.** Agencies already pay for the PM system, Cotality/RP Data (from ~$219/month [verified: Cotality packages page via search]), benchmarking (MRI Real Benchmark, price not published) and the inspection, maintenance and tenancy apps. Retention dashboards get bought by the 10–20% of growth-minded principals. The rest churn after the first scare report.

7. **There is no maintenance buyer with budget. Severity: Med.**
   - Terri Scheer covers 250k+ properties [verified: Terri Scheer self-description via search]. EBM RentCover pays ~$43–49M/yr in claims [verified: EBM marketing pages; figures conflict].
   - Their loss drivers are malicious damage, lost rent and legal costs. Wear-and-tear maintenance is excluded.
   - Insurers will buy *loss* signals (tenancy-risk and arrears precursors), not maintenance cost curves. That points back to products A and B.

## Things the brief gets wrong, misses or understates

- **"Rent-roll brokers e.g. Rent Roll Brokers?":** named firms found are Pendium Advisory ("700+ rolls sold or consulted", cumulative), BDH Solutions (Ross Hedditch, Melbourne/NSW), The Rent Roll Broker (Chris Goodway; source is 2012-era), mc rent roll broking (NSW), Wollermann Group, plus general brokers (LINK, Benchmark, First Choice) [verified as names via search; 2026 activity unverified]. Acumentis (with GWA) is the main **valuer** brand.
- **Multiples:** the brief's 2.8–3.5x matches Acumentis's Melbourne/Sydney range [verified via search summary; undated]. Other evidence: a Pendium Logan sale at 3.00x for $547k; a Sydney 100-property roll at 3.05x; Melbourne inner-city at $3.30–3.75 (BDH, undated). Prices bottom out where a large roll in a weak cycle is "subject to significant discount", which is a factor a model can quantify.
- **Misses the serial-acquirer and consolidator segment:** Managex Funds Management (Poynton/Slatyer) buying and aggregating residential rolls, for example The Agency's WA roll for $3.6M [verified: Business News Australia; date not shown]. In the UK: Dwelly (8+ acquisitions in 2025 and 6–8 in 2026), Lomond (PE-backed, 6 London deals in 2025), and Foxtons (£2.2m for 689 tenancies) [verified: trade press via search]. In Reapit's UK survey, ~half of agents had acquired or considered acquiring, and ~1 in 8 completed a purchase.
- **US analogue the brief omits:** US practice already prices PM firms on door-churn and owner-concentration haircuts (churn >10% and owner concentration >20% compress multiples; platforms trade at 5.5–8x EBITDA, and sub-500-door books under 5x) [verified: ctacquisitions.com 2026 guide, practitioner commentary]. The analytic is not novel. **The data pipe is**.
- **Understated: post-deal integration pain.** Every DD guide splits work across accountant, broker, property professional and lawyer [verified: Avery Law guide via Wollermann]. Nobody owns "will these landlords stay?" That gap is the opening.
- **Time-sensitive:** automated-decision transparency under the Privacy Act starts **10 Dec 2026**. A retention score that informs price is unlikely to be an "automated decision about an individual", but landlord-level churn scores in lender or franchise products need counsel [flag to privacy specialist].

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status / source |
|---|---|---|
| Melbourne roll multiples 2.8–3.5x mgmt income | Acumentis 2.80–3.50 for Melb/Syd; deals at 3.00x and 3.05x; inner-Melb 3.30–3.75 | verified (undated): Acumentis, Pendium, IFA/REB via search |
| Rentals and agent share | ~2.7M rentals, ~80% agent-managed, ~$49B rent/yr | verified (industry estimate): REIA 2024 card |
| Agencies in Australia | 46,793 (REIA); IBISWorld 45–46k "real estate services". PM-active offices far fewer | verified / estimate: ~8–12k PM businesses |
| PM software penetration | PropertyMe passed 5,000 customers (older milestone) | verified (dated): REB |
| Median eastern-seaboard roll value | $470,657 (FY22); median management income per property $1,457 (FY21) | verified, stale: Elite Agent |
| Annual AU roll transactions | ~400–900; ~$250–550M | estimate (no published count; 3–5% of managed stock) |
| Rent-roll valuation fee | Not published | unverified; guess $2.5–8k; confirm in interviews |
| Mid-market M&A DD cost | $50–150k (generic, not rolls) | verified generic: Expert360. Roll DD is far cheaper, ~$5–20k [estimate] |
| Broker commission | Generic business brokers 5–12%; roll-specific not found | partially verified: BusinessForSale |
| NAB roll lending | 70% LVR, min 100 residential PUM, 2.5x ICR; another page says 80%/10 yrs | verified, conflicting: NAB via search |
| Macquarie roll lending | 70% via internal multiplier, free to client; amortise to 60% in 3 yrs | unverified: broker summary |
| Landlord insurer scale | Terri Scheer 250k+ properties; EBM ~$43–49M claims/yr | verified (company claims) |
| UK consolidator funding | Dwelly £69m (Feb 26) + ~US$170m Series B (Jul 26) | verified, amounts vary by source |
| US PM multiples | 5.5–8x EBITDA for platforms with >90% retention; sub-500 doors <5x | verified (practitioner guide) |

## Improvements (concrete changes to the plan, ranked by impact)

1. **Sell price certainty, not reports.** Price A against value at risk:
   - $4,950 for ≤300 managements; $9,500 for 300–1,000; $15–25k above that (ex GST).
   - Or a success fee: 10% of the documented price reduction or retention-clause improvement, capped at 1% of price.
   - At ~0.3–0.5% of a $1–3M deal, this is below the accountant's fee and well below the value at risk.
2. **Make outcome data the moat.** Every A engagement includes free 12–24-month retention tracking (product B) on the acquired roll, in exchange for consented, de-identified outcome data. After ~50 tracked acquisitions the firm owns the only **"predicted vs realised retention" dataset** in Australia. Brokers, valuers, Cotality and PropertyMe don't have it, because none of them sees post-settlement outcomes across PM systems.
3. **Lead with serial buyers and franchise HQs, not the long tail.**
   - Target ~20–40 serial acquirers.
   - Target ~10–15 network HQs (Ray White, LJ Hooker, Harcourts, First National, Belle, Raine & Horne, PRD, Century 21, Barry Plant, Jellis Craig, Biggin & Scott, Nelson Alexander). Network licence for intra-network roll trades and retention monitoring: $60–200k/yr.
   - HQs earn franchise fees on PM income, so network landlord churn is their P&L line.
4. **Partner with one valuer (Acumentis-type) and one broker.**
   - Valuer: the founder supplies the model, the valuer signs. This makes the output bankable without a valuer's licence or PI exposure.
   - Broker: vendor-side "verified book quality" report, $2–4k paid by the vendor, marketed as lifting the multiple.
5. **Price B as a post-deal add-on:** $0.30–0.50 per managed property per month, minimum $250/month. Lender covenant monitoring: $600–1,200 per facility per year, sold to non-bank and private-credit lenders first.
6. **Plan the UK as market two by month 18–24.** It has larger, funded consolidators and more transactions [estimate]. Pre-sell to buyers of the 2nd tier (not Dwelly), such as Lomond-style PE platforms and regional consolidators.
7. **Alternative with higher expected value:** use A and B as the engine of a **capital-partner vehicle**. A family office or PE fund deploys $20–50M into rolls; the founder earns a fee of 1–2% of deployed capital plus carry. On WTP grounds this beats SaaS because the edge is monetised exclusively, and it ties back to round 2.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| Test | Metric | Continue if | Kill if | Time / cost |
|---|---|---|---|---|
| 20 discovery interviews (below) | Live-deal data shared; stated WTP | ≥6 of 10 acquirers/brokers would share a live export within 30 days; median stated WTP ≥$4k per deal | <3 would share data; WTP <$1.5k | 6 weeks, ~$2k |
| Retention-clause check | Typical adjustment period and terms | Months 6–36 losses still ≥3% of price on average | Clauses cover ≥80% of realised loss | Inside interviews |
| Paid pilot (offer below) | Paid DDs signed | ≥3 paid at ≥$3k by day 75 | 0–1 paid | 90 days, <$10k |
| Back-test on 3–5 historical acquisitions | Model vs multiple on realised 24-month loss | Model error ≤half of the multiple-implied error | No improvement | 8–10 weeks |
| Franchise HQ | LOI or paid pilot | 1 HQ pilot ≥$20k | No HQ will share network data | 90–120 days |
| Lender | Pilot on ≥10 facilities | 1 non-bank or bank pilot | All say "internal multiplier is enough" | 120 days |

**20 discovery interviews (who):**
- 6 serial acquirers (principals who bought ≥2 rolls since 2022)
- 3 franchise-HQ PM or growth heads
- 3 rent-roll brokers (Pendium, BDH, one Vic broker)
- 2 roll lenders (NAB/Macquarie roll specialists) and 1 non-bank or private credit lender
- 2 aggregators or family offices (Managex-type)
- 2 vendors planning a sale within 24 months
- 1 landlord insurer (Terri Scheer or EBM product or pricing head)

Add one bonus conversation with a PM-software partner team (PropertyMe/Console) on export and API terms.

**Script (30 min):**
1. Walk me through your last roll deal: size, price, multiple, and how the price was set.
2. What DD did you do, who did it, what did it cost and how long did it take?
3. What was in the retention clause?
4. 12 and 24 months later, how many managements had you lost compared with what you expected? What did that cost?
5. What do you wish you'd known before signing?
6. What would you pay to know it, and from which budget?
7. Would you share a raw export from a live deal under NDA?
8. Who else signs off?

**Go signal:** a quantified post-deal loss surprise (≥5% of managements beyond the clause period) in ≥half of the acquirer interviews, plus data shared on a live deal.

**Paid-pilot offer:** "Retention-adjusted DD in 10 business days from your target's PropertyMe/Console export: modelled 36-month retention, fee-quality and arrears flags, and a retention-adjusted price range with suggested clause terms. **$4,950 ex GST (≤500 managements). Full refund if we don't surface at least one issue worth ≥2% of the price that the IM missed.** Includes free 12-month retention tracking after settlement in exchange for de-identified outcome data."

## Answers to the round-3 questions in my domain

**Q1. Who pays, how much, how often; big enough?** Buyers with willingness to pay, ranked:

| Rank | Buyer | Typical spend | Frequency |
|---|---|---|---|
| 1 | Serial acquirers / aggregators | $5–25k per deal | 1–5 deals/yr |
| 2 | Franchise HQs | $60–200k/yr | Annual licence |
| 3 | Brokers / vendors | $2–4k per vendor report | Per sale |
| 4 | Non-bank lenders | $1–3k per loan plus monitoring | Per loan, then annual |
| 5 | Big-4 banks | Low | Slow procurement |
| 6 | Insurers | Low, for maintenance products | n/a |

- **Australian revenue ceiling in years 3–5:** ~$1.5–3M ARR [estimate]. At 25–35% EBITDA, the business can pay the founder ~$300–600k. The exit at 3–6x ARR is **$5–18M**.
- That matches a $500k salary but doesn't clearly beat it on wealth unless the UK works or the capital-partner variant is added.
- NZ adds little: about a tenth of Australia's scale [estimate].

**Q4. Wedge and moat:** A is the wedge. The moat is the outcome dataset (predicted vs realised retention) built through B. Maintenance is a secondary data moat inside B.

**Q6. Versus rounds 1–2, on WTP grounds:** the software is the lowest-capital route, but also the one most likely to stall at around $1M revenue. Its strongest role is as the exclusive edge of a capital-partner vehicle.

**Q7. 90-day test:** run the 20 interviews, the paid-pilot offer and one back-test. Kill A as a standalone SaaS if fewer than 3 paid pilots are signed and fewer than 3 parties share live data.

## Questions I'd hand to other specialists

- **Legal/privacy:**
  - Can a vendor lawfully hand landlord and tenant personal data to a third-party analytics provider pre-settlement?
  - Does the APP small-business exemption cover typical agencies but not us?
  - Does the 10 Dec 2026 automated-decision regime touch landlord-level churn scores?
- **Data/engineering:** do PropertyMe, Console/Reapit and Rex exports carry enough history (landlord tenure, fee changes, lost-management reasons) to model months 6–36 churn? Is API access permitted for a non-agency third party?
- **Competitor analyst:** what stops Cotality or PropertyMe from bundling a "roll health score"? Are Acumentis or Pendium already building one?
- **Finance/modelling:** after typical retention clauses, what is the net value at risk per $2M roll? Is the 5-point error realistic?
- **Employment/IP:** can interviews and pilots run while employed, and could the current employer claim the IP?
- **Capital-partner specialist:** is there a family office or private-credit appetite for a $20–50M roll-aggregation fund with a data-led manager?
