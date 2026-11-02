# Lifetime-Value & Platform Economics Modeller (CFO): red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives-if, but not as a scale-reducer.** At base attach rates, the whole service stack adds **~$160 per managed property per year (+18–19% LTV)**. That cuts the $500k-draw scale from **~3,100 to ~2,500 properties**, not to the ~1,000 the platform story implies. The services only "change the game" if attach rates run at **3–4x my base**, for example in-house broking capturing 45–60% of landlord refinances. Nobody in Australian PM has shown that. **Biggest issue:** the round-1 figure of 2,510 properties already assumed a $75 sale referral that s 48A probably zeroes. Corrected, management alone needs ~3,100 properties. The services mainly win back that loss. They are not a new engine.

## Verdict on the platform thesis (which services carry the economics, from your lens)
- **Carry weight (in order):**
  1. **Landlord mortgage broking** on refinance and the next purchase: +$220 LTV, ~$60/property/yr, pays its fixed cost from ~12.5% refinance capture at 1,000 properties.
  2. **Managements sourced from the landlord's next purchase:** +$88 LTV, worth avoided CAC. It costs nothing and rides on the broking conversation.
  3. **Sale capture, mainly through buyer-management retention rather than the referral:** +$83 LTV, of which about two-thirds is churn reduction.
- **The maintenance subscription** is the second-largest by LTV (+$178) but the worst risk-adjusted. Margin flips negative at ≥20–30% adverse selection. It carries a ~$150k fixed cost that it doesn't cover until ~2,000 properties at ~31% attach. ASIC treats warranty-type cover of wear and tear as likely insurance. **Defer it; if you build it, build it as a no-risk preventive plan or as an insurer's authorised representative.**
- **Tenant evaluation as a priced product** is worth ~$16/property/yr. It is a cost and quality lever, not a revenue line.
- **Tenant-side services are worth ~$25–80 per tenant relationship**, against ~$3,600 for the landlord relationship. Treat them as retention and brand features, never as economics.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

**A1. Services are a rounding error next to the management fee. Severity: High.**
The model takes the round-1 management contribution of **$765** per property (3x productivity, referral removed). Every service at base attach adds **$157/yr in total**, and two-thirds of that comes from broking, maintenance and new-management sourcing. In the LTV tornado, management contribution (±$200) swings LTV by **$1,910**, the discount rate by $917 and churn by $744. The largest attach-rate input, broking capture, swings it by $376. **The super-app is a ~20% overlay on a management business, not a different business.** Each extra 0.5% of headline fee is worth more than every tenant-side service combined.

**A2. Without the s 48A haircut, the round-1 scale target was overstated. Severity: High.**
Round-1 found 2,510 properties for $500k (debt-free, funnel refill, $575k fixed). That run included **$75/property/yr of sale referral at 50% capture**. With referral at $0, which is round-1 counsel's own recommendation, the same model needs **3,100 properties**. The full landlord service stack brings it back to **2,500** (2,080 at $400k fixed). The services are therefore buying back the round-1 assumption, not halving the scale.

**A3. Attach rates are unknown and are the decision variable. Severity: High.**
No Australian PM publishes cross-sell rates. LocalAgentFinder and broker-referral businesses publish lead-to-settlement rates, not rates from an owned book [unverified]. Section 8 of the model shows how scale responds:

| Attach multiple on base | Properties for a $500k draw |
|---|---|
| 1x | 2,500 |
| 2x | 1,930 |
| 3x | 1,620 |
| 4x | 1,400 |

A 4x multiple means 60% of refinances broked in-house, 80% of next-purchase loans, 60% maintenance attach and 80% sale capture. That is implausible, so **~2,000 properties is the realistic floor** with a platform.

**A4. Maintenance subscription: adverse selection plus insurance law. Severity: High (structure) / Med (economics).**
Margin per subscriber at a 20% loading is $404 with no adverse selection, $238 at 10%, $73 at 20% and −$93 at 30%. Landlords with old, poorly kept stock will opt in first. The Victorian Residential Tenancies Act (RTA) already puts the repair duty on the rental provider, so the landlord's alternative is self-insuring. The US benchmark (Frontdoor, ~55% gross margin FY25 [verified: Frontdoor FY25 results]) depends on exclusions and claim denial. In Victoria, an agent who denies a claim still has to arrange the repair, so that model doesn't transfer. ASIC says an extended warranty may be a contract of insurance, more likely if it covers wear and tear, which would require APRA authorisation and probably an AFSL [verified: ASIC extended-warranties guidance]. The variance-absorbing design is the insurance-like part. Charging the tenant a split of the fee runs into the RTA renter-fee restrictions [estimate: CAV lists bans on application and rent-payment fees, and third-party platform fees from 31 Mar 2026; verified: CAV]. Treat the tenant split as dead.

**A5. Broking is the best service, but its value is in trail and timing, and it pays off slowly. Severity: Med.**
- **Per settled loan:**
  - A $420k landlord refinance nets ~$2,630 NPV: upfront 0.60% × 90% aggregator split, less 5% clawback, plus the PV of a 0.15% trail at 20%/yr loan exit, less $1,300 cost per loan.
  - A $600k purchase loan nets ~$4,310.
- **Rates used:** 0.55–0.65% upfront and 0.15–0.20% trail [verified: Mozo 2026 / MFAA]. Clawbacks are rising (median gross clawback per broker +16.5% in 2025 [verified: MFAA via TheAdviser]).
- **Timing:** refinance events run at ~10%/yr of borrowers (619k refinances in the year to Sep-25 [verified: ABA]) on an estimated ~6M loans, and only ~65% of landlords have a loan [estimate]. One broker therefore sees ~65 refinance and ~40 purchase opportunities a year per 1,000 properties. At 15–20% capture that is **~18 loans a year per 1,000 properties**, which doesn't occupy a broker. The service needs a credit representative under an aggregator (NCCP Act; Best Interests Duty).

**A6. "New managements from property #2" is smaller than it looks because the next purchase often isn't in Victoria. Severity: Med.**
About 71–72% of investors own one property and ~19% own two [verified: ATO tax stats via PropertyUpdate]. Victorian land tax pushes investors interstate (73% open to buying interstate [verified: Momentum Wealth 2026 survey, intent only]). I assume 40% of next purchases are serviceable. On that assumption, 4% buy rate × 40% serviceable × 50% capture = **0.8 new managements per 100 properties a year**. That replaces ~7% of the 12% annual churn at no CAC. It is useful, but it doesn't refill the book the way a sales team does.

**A7. Tenant-side LTV is tiny. Severity: High for the narrative, Low for the money.**
- **Fees:** the agency can't charge renters fees.
- **In-portfolio moves:** these earn nothing directly. The placement saving is ~$150, and with ~4% corridor share a match happens ~8% of the time.
- **First-home finance:** 4% of renter households buy a year (HILDA: 7.6% of 18–24s, 2013–16 [verified, dated]) × 4% capture × $3,840 per loan ≈ $6/yr.
- **Total:** **$24 per tenant relationship at base, $78 at upside.**

The tenant side earns its place only by lowering arrears, vacancy and turnover cost on the landlord side. Even that is unproven.

**A8. Payback on a bought management doesn't change sign. Severity: High.**
- **Roll purchase:** at round-1's $5,279 per retained roll management, contribution before fixed costs pays back in 6.9 years simple for management only and 5.8 years with all landlord services. **Discounted at 12% with 12% churn, it never pays back** (LTV/cost 0.68, rising to 0.80 with services).
- **Funnel acquisition at $3k:** discounted payback is 8 years for management only and 6 years with services (LTV/cost 1.19, rising to 1.40).

**Services don't rescue roll economics at current multiples.** They make funnel acquisition worth ~$1,000 more of allowable CAC per management.

## Things the brief gets wrong, misses or understates
- **Round-1 scale is optimistic by ~600 properties** because the $75 referral is still in it (A2).
- **The trail outlives the management.** Broking LTV stays with the broker after the landlord churns, until the loan is refinanced or discharged. This is the only service whose value doesn't die with the management, and it should be valued separately (it can be sold).
- **The real point-of-sale prize is the buyer's management, not the referral fee.** In the model, ~two-thirds of sale-capture value comes from investor buyers keeping the manager (churn −0.26 points). The referral fee is worth $12/yr after a 60% s 48A haircut.
- **"Investment support" is broking.** Portfolio analytics as a paid subscription has no evidence of willingness to pay. Model it as the free top of the broking funnel.
- **Mix:** the next property is increasingly interstate, so investment support grows the broking book faster than the management book.
- **Tenant evaluation:** priced screening sits on top of a letting fee the landlord already sees as covering it. Vic fixed-price advertising and the ban on accepting offers above advertised rent cap any rent-setting uplift (modelled at 0.5% of management fee, ~$7/yr).

## Numbers checked (table: claim | finding | status/source)
| Claim | Finding | Status/source |
|---|---|---|
| Broker upfront ~0.65%, trail ~0.15% | 0.55–0.65% upfront; 0.15–0.20% trail; ASIC average upfront ~0.54% | [verified: Mozo 2026; MFAA]; ASIC figure [unverified] |
| Broker clawbacks material | Median gross clawback per broker +16.5% in 2025 | [verified: MFAA 2026 report via TheAdviser] |
| Refinance frequency | 618,966 external refinances in the year to Sep-25; ~10%/yr of loans | [verified: ABA flow]; rate [estimate] |
| Investor loan size | National new investor loan ~$686k (Sep-25 qtr); Vic owner-occupier $664k (Jun-26) | [verified: ABS via YourMortgage/Canstar]; book balance $420k [estimate] |
| Landlords own one property | ~71–72% one, ~19% two | [verified: ATO via PropertyUpdate] |
| Repair spend per rental | $1.7k unit / $2.7k house (2017); ATO repairs $3.19bn FY22 in aggregate | [verified: BIS Oxford 2017 via DHA; Kanebridge]; $1,800 base [estimate] |
| Home-warranty margins | Frontdoor FY25 gross margin ~55%, revenue $2.09bn USD | [verified: Frontdoor FY25 release] |
| Flat-fee repair cover is insurance? | ASIC: an extended warranty may be insurance, more likely if it covers wear and tear | [verified: ASIC]; application to this product [unverified, needs counsel] |
| Renter fees | Application and rent-payment fees banned; third-party platform ban from 31 Mar 2026 | [verified: CAV] |
| Melbourne sale commission | ~1.6–2.5%, average ~2.1% | [verified: WhichRealEstateAgent/Mozo 2026] |
| Renter → owner transition | 7.6%/yr for 18–24s (2013–16) | [verified, dated: HILDA via Domain]; 4% all renters [estimate] |
| Round-1 $500k scale 2,510 | 3,100 with referral at $0 | [model: ltv_model.py §10] |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Rebase the target.** Plan on **~3,100 properties for management only and ~2,500 with landlord services**, or ~2,100 with $400k fixed. Stop presenting the platform as a way to reach $500k on ~1,000 properties.
2. **Make broking service #1**, run as a credit representative under an aggregator. Start with an annual "portfolio and loan review" for every landlord, which is the analytics product, given away free. Measure capture per refinance event. Value the trail book as a separate asset.
3. **Service #2: own the moment of sale for the buyer.** Under an independent selling-agent-selection engagement, get a contractual right to offer management to an investor buyer and to keep the sitting tenant. Drop the referral fee from the base case.
4. **Defer the maintenance subscription to after 1,500 properties.** If you test it, use the authorised-representative or no-risk preventive form (~$264 per subscriber; model §10, before any s 48A treatment of commissions). Never split the fee with the tenant.
5. **Price tenant evaluation into the letting fee** and use it to cut arrears and turnover cost. Don't market it as a separate SKU.
6. **Drop tenant revenue lines from the plan.** Keep tenant features that measurably reduce vacancy and turnover, and track them as landlord-retention metrics.
7. **Put pricing ahead of the platform.** +0.5% on the headline fee ≈ +$130/property/yr, about the whole service stack.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)
| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| Loan-review offer to the acquired agency's landlords (or to a partner agency's book under its brand), via a partnered credit rep | Share of contacted landlords booking a review; settled loans per 100 landlords | Continue if ≥10% book and ≥1.5 settlements/100/yr; kill broking-led thesis if <0.5 | 6 months |
| Refinance capture | In-house share of landlord refinance events detected (discharge or new mortgage notices) | ≥15% to keep; ≥30% to invest in a broker FTE | 12 months |
| Buyer-management retention at sale | Share of investor-buyer sales where the management is kept | ≥30% where we ran selection; kill if <10% | 12–18 months |
| Maintenance price test (quote only, no risk taken) | Opt-in rate and property-age skew of opt-ins vs book | Kill risk-bearing design if opt-ins are ≥25% older or costlier than book | 8 weeks |
| Next-purchase locality | Share of landlords' next purchases in serviceable Melbourne | Model assumes 40%; if <25%, cut new-management sourcing to zero | Survey + 12 months |
| Attach index | Landlord services value per property per year | ≥$300/yr by year 3 (≈2x base) or stop calling it a platform | 36 months |

## Answers to the round-2 questions in my domain
**Q1: Which one or two services, in what order?**
1. Landlord broking, with the investment review as its free front end.
2. Point-of-sale buyer retention, through an independent selection engagement.

The maintenance subscription comes third, after 1,500 properties, in a no-risk form. Tenant services are features, not products.

**Q2: LTV per relationship, and does it change scale?**
- **Landlord relationship (per managed property, 12% discount, 12% churn):**
  - Management only: **$3,569**.
  - Plus broking: $3,789.
  - Plus broking and maintenance: $3,970.
  - All landlord services: **$4,212**.
  - All services: $4,246.
- **Tenant relationship:** **$24 at base, $78 at upside.**
- **Scale for a $500k draw ($575k fixed):**
  - 3,100 → 2,750 with broking alone.
  - **2,500** with all landlord services.
  - **~1,930** if attach rates double.

This is a ~20% reduction, not a step change.

**Q3 (economic side):** s 48A turns the sale referral from $75 to ~$12/yr in expectation. The maintenance plan's risk-bearing form is the insurance-exposed one, and its no-risk form is about as profitable. Renter fee bans make the tenant subscription marginal.

**Q5: Where the founder's edge is decisive.** Pricing the maintenance risk, in principle, and building the event-detection engine for refinance and sale propensity. Both raise capture. The model says capture rates, not cost, are what services depend on. The edge is irrelevant to tenant-side monetisation, which is capped by law.

**Q6: Smallest test.** A 6-month loan-review campaign on an existing book under a partner's credit representative, measured as settled loans per 100 landlords. Fewer than 0.5 per 100 per year kills the platform economics. ≥1.5 justifies the build.

## Questions I'd hand to other specialists
- **Regulatory counsel:**
  - Does s 48A reach lender commissions paid to a related broking entity when the managing agent introduces the landlord?
  - Is a fixed-fee, defined-scope preventive maintenance plan (no variance cover) outside the Insurance Act?
  - Are authorised-representative insurance commissions caught by s 48A where premiums are paid from trust?
- **Growth/funnel:** what refinance and sale-event detection data can be used lawfully after 10 Dec 2026 (privacy, automated decisions, Spam Act)?
- **PM operations:** do in-portfolio tenant moves measurably cut vacancy days and arrears enough to count as a landlord-retention lever?
- **M&A:** will vendors or lenders pay for a broking trail book bundled with a rent roll, and at what multiple of trail?

Model: `red-team/round2/models/ltv_model.py`, which imports round-1 `red-team/models/unit_economics.py`. Run with `python3 ltv_model.py`.
