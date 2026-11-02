# Post-Acquisition Retention & Integration Specialist: red-team report

## Verdict
**Survives-if.** Acquired managements can survive the move to an AI-led service, but only under a slow "soft landing" with the vendor's people, phone number and brand kept for 6–12 months, and no fee change in year 1. A hard switch loses roughly a third of the roll within 12 months and adds ~25–30% to the effective price per management. **The biggest issue is not integration churn but structural churn with no sales arm to refill it.** Gross attrition of 10–14%/yr is normal for any roll. Incumbent sales agencies refill it with investor buyers from their own sales listings; the founder has no such inflow. At roll prices (~$7k), replacing 12%/yr costs ~$840 per property per year, which is more than the $600–700 margin. So the plan only works if the funnel, not acquisition, does the replacing. Gate 3 at 50% is not realistic for rolls bought from sales agencies.

## Attacks on the load-bearing assumptions

**A4 (Retention): acquired managements survive the move to AI-led service. Severity: High.**

1. **What breaks retention after a roll sale is people and phone numbers, not software.** In Australian roll sales, loss at settlement ("slippage") is typically 5–12% when the transfer is run well. One adviser's self-reported sample of 28 sales was mostly 5–12%, with outliers from 4% to 91% [unverified: Pendium Advisory blog, seller-side, self-reported]. Another source says ~5% of landlords commonly leave after a sale [unverified: REIQ article, period not stated]. The causes it lists: the landlord was already planning to sell, move back in or self-manage, or was dissatisfied with service. The 91% outliers come from the vendor PM leaving and taking the book, or from the vendor sales team staying in the suburb and steering landlords. Neither risk is AI-specific, but an AI-led model makes both worse. The landlord loses "my PM Sarah", and the first contact from the new owner is a templated or bot message at exactly the point they decide whether to sign the transfer.

2. **"AI-led" is something landlords notice; "AI-assisted" is not.** Landlords who rate their agency on responsiveness will reward faster replies. Landlords who rate it on relationships, many of them older with one or two properties, read a change in channel (portal or chatbot replacing a phone call) as a downgrade. Retention problems show up in the first arrears, maintenance dispute or lease-break after settlement. That is an exception, and exceptions are what the founder's model routes to a stretched PM carrying 300+ properties. **The plan's productivity lever (300+ per PM) and its retention lever (one human relationship) collide in exactly the first 6 months after acquisition.** Run acquired books at ≤180 per PM for the first 6–9 months and only then step up the ratio.

3. **The retention clause protects only the first ~90–180 days.** Typical structures hold back 10–15% of price, or adjust price for losses within a fixed window (one litigated contract allowed up to 10% adjustment over 180 days) [unverified: REIQ case report; API Magazine guide]. The brief's "10–20% retained ~3 months" is in range. Losses in months 4–24, when service-change churn actually shows up, fall entirely on the buyer. Lender LVR covenants are tested against roll value, so post-window churn is also a covenant risk (see Q4).

4. **The vendor stays in the suburb and stays your competitor for the landlord at the point of sale.** Sub-scale rolls inside sales agencies, the brief's target, are sold by sales principals who keep selling in the same suburbs. Their sales agents have every reason to approach landlords when they come to sell, and selling landlords are exactly the managements that leave. Sale agreements often keep sales leads with the vendor. A third-party agent selling the property counts as a "lost management" under many retention clauses, while a sale through the vendor does not [unverified: rent-roll guides]. **This conflicts directly with Gate 3.** The deal you can buy cheaply is the one where the vendor keeps the sale relationship.

5. **Non-competes are getting weaker.** Victoria has no restraints-of-trade statute (that is NSW's Restraints of Trade Act 1976). Victorian courts apply the common law, where an unreasonable restraint generally fails as a whole unless it is drafted as a "cascading" clause. Restraints given by a business vendor are enforced more readily than employee restraints [estimate: settled common-law position; confirm with counsel]. The Commonwealth has announced a ban on non-competes for employees earning below the Fair Work high-income threshold (~$183k–$190k+) from 2027. It applies prospectively, draft legislation has been released, and I could not confirm it has passed [unverified: Mallesons, Clayton Utz, HR Legal commentary; check Parliament status, time-sensitive]. **A vendor PM earning ~$75k hired in 2027 cannot be held by a non-compete.** The only lasting holds are client non-solicit and confidentiality clauses (reportedly outside the ban [unverified]) and money: retention bonuses and equity-like stay payments.

**A3 / Gate 3 (sale capture). Severity: High as a gate; Medium for economics.**
"Half of selling landlords sell through me" assumes three things: no sales team, no vendor sales relationship, and a landlord who trusts a referral from an agency that is paid by the selling agent. I estimate a realistic capture of **20–35%** in years 1–2 for an organically signed book. For acquired books where the vendor keeps sales leads it is **10–20%**, and **0%** where the contract gives the vendor first right [estimate: no published benchmark found; an industry headline says "almost a quarter of sales are generated from the rent roll" for agencies *with* sales teams, unverified body text]. 50% is a stretch target, not a gate. Keep it as a gate and the plan fails on a metric it does not need.

**Churn is structural, not cyclical. Severity: High.**
UNSW/AHURI bond-data research found that 51.4% of Melbourne properties that entered the rental sector in 2015 had left it within five years. It found no exit spike after tenancy reforms [verified: UNSW/AHURI FR391, 2022]. That is ~13%/yr for new entrants. Across the whole stock it is probably 7–10%/yr from sale or owner move-in, plus 2–5%/yr from switching agency or self-managing, for **10–14% gross** [estimate]. The Victorian net decline since 2023 sits on top of this, and the cycle has not ended (see the Numbers table).

## Things the brief gets wrong, misses or understates
- **No allowance for replacement cost.** "750–850 properties unlevered" treats the roll as a perpetuity. At 12% gross churn, replacing properties by acquisition costs ~$840/property/yr ($7k × 12%), which exceeds the $600–700 margin. Replacing them through the funnel at $2k costs ~$240/property/yr, which cuts sustainable margin to ~$400–450. **On that basis, income replacement needs ~1,100–1,250 properties unlevered, not 750–850** [estimate].
- **The roll multiple assumes a sales arm.** At 12% churn and an 8% discount rate, a management earning $650/yr is worth ~$3,250 to a buyer with no inflow (650 / (0.08 + 0.12)). The market pays ~$7k because buyers with sales teams refill the book from investor purchases. The founder buys at the price a sales-agency buyer would pay, without the sales-agency inflow that justifies it. **This is the arbitrage working in reverse.** It only works if the funnel replaces that inflow at under ~$2k.
- **The brief's sell-off figure is stale and has the wrong sign.** "~25k fall to Sep 2024" was the 2023–24 shock. FY25 was roughly flat. 2026 is mixed: early rebound, then a sharp investor lending fall in the June 2026 quarter amid RBA hikes. Plan for churn as a constant of 10–14%, not as a one-off.
- **Captured sales do not hold the roll steady.** A $3k referral fee replaces ~40% of one year's revenue on that property, not the management. Count it as income, not as retention.
- **A buyer of the landlord's property is a separate source of new managements.** If the founder runs the sale process, they can introduce an investor buyer, or offer management to the buyer at settlement. This is the inflow sales agencies get, and it matters more than the referral fee.
- **Conflict of interest.** The founder's agency acts for the landlord (management) while taking money from the selling agent (referral). That needs written, specific, informed consent under the Estate Agents Act 1980 and the conduct rules, and checks against s 49A rebate disclosure. Non-compliance with s 49A has cost agents their full commission (a $3M refund case) [verified in part: Consumer Affairs Victoria guidance; Mills Oakley/Pointon Partners case notes; referral-specific rules unverified].

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| VIC active bonds fell ~25k in year to Sep 2024 | 21,712 fall in year to June 2024 (−3.2%, to 654,717), first annual fall since 1999. ~24k (−3.6%) cited for calendar 2024 | [verified: Homes Victoria Rental Report Jun Q 2024 via search snippet; PropTrack; PIPA] |
| Sell-off continuing | Jun Q 2025: 655,626 active bonds, roughly flat year on year (sources conflict on sign). −3.4% June 2023 peak to Sep 2025. 2026 commentary says refunds exceed lodgements again | [verified: Homes Victoria Jun Q 2025 snippet; Jellis Craig] / [unverified: Property Update 2026] |
| Investors returning 2026 | VIC investor lending +21% y/y into early 2026; then the steepest investor fall in the June Q 2026 ABS data, third RBA hike of 2026 | [unverified: secondary reports of ABS data; check ABS Lending Indicators Sep Q 2026, release due ~Nov 2026] |
| Ex-rental selling vs investor buying | May (2025 or 2026): 1,663 ex-rentals listed vs 1,021 investor purchases in VIC | [unverified: FoundIt via Property Update] |
| Land tax driver | VIC threshold cut to $50k from Jan 2024 plus COVID debt levy | [verified: widely reported; SRO for detail] |
| Melbourne vacancy | 1.5% Apr 2026 | [unverified: SQM via secondary] |
| Gross rental exit | 51.4% of 2015 Melbourne entrants exited within 5 years; no reform-driven spike | [verified: UNSW/AHURI FR391] |
| Retention holdback 10–20% for ~3 months | 10% / 180 days and 15% structures seen | [unverified: REIQ, API Magazine] — brief in range |
| Settlement slippage | 5–12% typical when run well; tail to 91% | [unverified: Pendium, self-reported] |
| Non-compete ban | Employees below high-income threshold, from 2027, prospective | [unverified: law-firm commentary; bill status unconfirmed] |
| PM staff turnover | ~35%/yr nationally | [unverified: industry blog] — vendor-PM retention risk is real |

## Retention curve: three integration approaches
Assumptions [estimate]: price $7,000/management; natural gross churn 12%/yr; holdback refunds losses to month 3. "Excess" means service-change churn in months 3–12.

| Approach | Settlement loss | Early (0–3m) | Excess 3–12m | Retained m3 | Retained m12 | Retained m36 | Effective $/mgmt at m12 | Excl. natural churn |
|---|---|---|---|---|---|---|---|---|
| **A. Hard switch:** rebrand at settlement, vendor PM exits, AI channel day 1, fee aligned within 6 months | 10% | 5% | 15% | 85.5% | 66% | 49% | **$9,050** | $8,235 (+18%) |
| **B. Soft landing:** local brand and phone number kept 12 months, vendor PM kept 6–12 months on a stay bonus, AI behind the human, no fee change for 12 months | 6% | 1% | 5% | 93% | 80% | 61% | **$8,100** | $7,370 (+5%) |
| **C. Partnered:** B plus a vendor earn-out (20–30% of price over 12 months on retained count), a reciprocal sales-referral agreement with the vendor, and the vendor PM converted to a career PM | 5% | 0.5% | 2% | 94.5% | 84% | 65% | **$7,850** | $7,140 (+2%) |

A vs C is ~$1,100–1,200 per management at month 12, which is ~$110k on a 100-door roll, and ~16 points of the book by year 3. Approach C costs a share of sale referrals given back to the vendor, and a stay bonus of ~$10–20k per vendor PM [estimate]. Both are cheaper than the loss under A.

**Communication sequence (C):**
- T−14 days: joint letter from the vendor principal and the PM by name, framed as "same PM, more capacity", with no mention of AI.
- T0: PM phones each top-30% landlord by revenue or risk.
- T+7: transfer and authority paperwork (e-sign), and the phone number unchanged.
- T+30: first "service guarantee" statement (response times met).
- T+60–90: introduce the founder and the career PM. The vendor PM hands over in person.
- T+6–12 months: brand transitions to co-brand "X, part of Y".
- Fee: no change for 12 months. Then move only on renewal or at a value event (new lease), and with a guarantee attached. Never raise fees within the holdback window, which would trigger a dispute over the definition of a "lost management".

## Improvements (ranked)
1. **Add replacement cost to the model.** Size income replacement at ~1,100–1,250 properties unlevered at 12% churn. Make funnel cost per management the variable that decides whether the business works.
2. **Default to integration C.** Write earn-out, stay bonus and sales-referral reciprocity into the term sheet. Pay part of the price on 12-month retention, not 3-month.
3. **Tighten the definition of "lost management"** and extend the holdback to 6 months. Exclude vendor-steered losses from the purchase price, and add a vendor and vendor-staff client non-solicit for 2–3 years. One review reportedly saved a buyer 30% of price by tightening the definition [unverified].
4. **Cap PM load on acquired books at ~180 for 6–9 months.** Treat 300+ as a steady-state target only.
5. **Recast Gate 3.** Track "sale events captured (referral or management retained with the buyer) ≥30% of sale-churn" and "net management retention ≥88%/yr". Drop the fixed 50% sell-through.
6. **Add a buyer-side capture step.** At every captured sale, offer management to an investor buyer and track the rate. It is the missing inflow.
7. **Prefer rolls with weak vendor-sales ties**: retiring principals, PM-only boutiques, or agencies exiting the area. Their roll multiples may be similar and their retention better.

## Tests & kill criteria
| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| First roll (50–150 doors) under approach C | Net retention excluding sales | ≥92% at m6; ≥88% at m12 | 12 months |
| Same roll | Excess churn vs vendor's 3-year history | ≤3 pts above history | 12 months |
| Landlord reaction to AI channel | CSAT/NPS on resolved exceptions; complaints citing "can't reach a person" | NPS ≥ vendor baseline; <2% of landlords complain | 6 months |
| Sale capture | Share of sale-churn events producing referral fee or retained buyer management | ≥25% by m12; kill Gate 3 thesis if <15% | 12–18 months |
| Structural churn | Gross annual loss across all books | If >16%, funnel CAC must be <$1.5k or stop acquiring | Rolling 12 months |
| Vendor PM retention | Vendor PMs still employed at m6 | ≥1 per roll; book-walk losses <3% | 6 months |
| Pre-deal diligence | Vendor's own 36-month churn from PropertyMe export | Price falls if >14%/yr; walk if >18% | Pre-signing |

## Answers to open items in my domain
- **Kill criteria (retention):** net 12-month retention on the first acquired roll below 85% under approach C, or gross churn above 16% with funnel CAC above $2k.
- **Unit-economics model:** add a churn line (10/12/14%) and a replacement-capex line priced at funnel CAC versus roll price. Report "sustainable margin per property" net of replacement. Price effective cost per management at month 12, not at settlement.
- **Capital plan:** LVR covenants should be tested on retained count after the holdback window. Negotiate a covenant buffer that allows for ~15% year-1 attrition.
- **Pre-sell test:** add a sample of acquired-roll landlords. Show them the AI-led service promise and measure the stated intent to stay versus leave.

## Questions I'd hand to other specialists
- **Legal/regulatory:** Does the 2027 non-compete ban (if passed) carve out sale-of-business restraints and client non-solicits? What exact disclosure and consent does the Estate Agents Act require when a managing agent takes a referral fee from a selling agent? Does s 49A apply?
- **Finance/debt:** Will lenders test LVR on month-12 retained count? How do they treat earn-out liabilities?
- **Funnel/acquisition:** Can the comparison funnel deliver ≥10–14% of book size in new managements every year at under $2k each? That is the real Gate 1.
- **Operations/AI:** What exceptions per 100 properties per month occur in the first 6 months after acquisition versus steady state?
- **Market/data:** What is the actual September quarter 2026 Victorian active bond count and the investor lending trend? Is the 2026 refunds-exceed-lodgements claim correct?

Sources consulted (via search; some primary sites were unreachable from this session): Homes Victoria Rental Reports (Jun Q 2024, Jun Q 2025); PropTrack; PIPA; Jellis Craig; UNSW/AHURI Final Report 391; REIQ; API Magazine; Pendium Advisory; Mallesons, Clayton Utz and HR Legal on the non-compete ban; Consumer Affairs Victoria (rebates/authorities); Property Update; Broker News/API Magazine on 2026 ABS lending.
