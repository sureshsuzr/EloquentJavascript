# Landlord Wealth & Investment-Services Product Lead: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives-if, but narrower than the brief claims.** Investment support won't feed new managements in any useful volume. On my estimates, a 1,000-property book yields about **2–6 new in-corridor managements a year from landlords' next purchases**, against **100–140 lost to churn**. This is because most Melbourne investors now buy interstate and/or new-build, and since **12 May 2026** established purchases have lost negative gearing. What survives is a **retention-and-refinance service**: an annual hold/sell/refinance review, with broking through a separate credit-representative entity. It is worth roughly **$100–200 per landlord per year** directly, plus whatever churn it prevents, which is unproven. **The single biggest issue is conflict.** A property manager is not neutral on hold vs sell, because a sale ends the management. That undercuts the "independence from sales" edge unless the product is built to handle it.

## Verdict on the platform thesis (which services carry the economics, from your lens)
- **Carries some economics:** refinance and new-purchase **broking**. It is the one investment service with a proven, lender-paid revenue line (upfront ~0.55–0.65%, trail ~0.15–0.20%). The landlord pays nothing visible, and the trail book is an asset that survives management churn. On a 1,000-property book it adds about **$25–60 net per property per year in years 1–2**, rising to about **$80–150** as trail builds.
- **Carries retention, if anything:** an annual **hold/sell/refinance review**, built on the founder's stats edge (a sale-propensity model plus a transparent after-tax model). Its value is churn avoided. Each point of churn avoided is worth about **$50–70 per property per year** at a $5–7k replacement cost.
- **Doesn't carry economics:**
  - Subscription portfolio analytics: about 71–72% of investors own one property, so there is no "portfolio" to analyse.
  - Buyers' agency: it needs licensed staff, purchases are mostly interstate, and it conflicts with developer lease-ups.
  - Sale advice: $0 under s 48A until counsel advises otherwise.
  - "Next purchase feeds new managements": the volume is negligible (see Attack 1).
- **Order:** (1) the review as a pre-licence test, in H1 2027; (2) broking via a credit-rep entity once the review shows uptake; (3) never a buyers' agency in years 1–3. If anything, refer purchases to an independent buyers' agent under a fee-free, consented arrangement.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

**1. "Buying the next property feeds new managements" fails on volume. Severity: High.**
- Investor dwelling commitments were **52,599 nationally in the June quarter 2026**, down 8.6% on the quarter. The fall was concentrated in NSW and Victoria, while new-build investor lending hit a series high of 8,468 [verified: ABS Lending Indicators via trade press summaries, Aug 2026]. That annualises to about 210k loans across about 2.26m investor individuals [verified: ATO 2022–23 via Firstlinks], or very roughly 1.4–1.6m investor households [estimate].
- So about 13–15% of investor households take a new investor loan in a year. Strip out first-time investors, refinances miscoded as purchases, and replacement purchases after a sale, and **about 4–7% of existing landlords add a property each year** [estimate].
- **67–73% of investors say they would buy outside their home state** [verified: Momentum Wealth sentiment surveys 2025/2026, intent not behaviour]. Victorian investors have the extra push of land tax: a $50k threshold since 2024 plus the COVID debt levy to 2033 [verified: SRO].
- **Since 12 May 2026, newly acquired established dwellings can't be negatively geared** (Treasury Laws Amendment (Tax Reform No.1) Act 2026, passed June 2026, operative 1 July 2027) [verified: multiple law-firm and trade summaries]. This pushes the next purchase toward new builds, often growth-corridor house-and-land or off-the-plan.
- **Funnel per 1,000 managed properties (~750 landlords):** 750 × 5% ≈ 37 purchases a year → ×25–35% in Melbourne ≈ 9–13 → ×40–60% inside a six-postcode service radius ≈ 4–8 → ×50–75% capture ≈ **2–6 new managements a year**, against 100–140 lost to churn [estimate]. That covers **2–5% of replacement need**. The round-1 synthesis listed "buyer support" as a growth channel. It isn't one.

**2. A property manager is conflicted on hold vs sell. Severity: High.**
- Round 1's edge was "independence from sales". But a sale ends the management (round-1 report 09: sale or owner move-in is about 7–10 of the 10–14%/yr churn). A PM running hold/sell analytics has a direct financial interest in "hold".
- Australian landlords skew older: about 27% are over 60 and about 48% are 45–64 [unverified: ATO-derived secondary analyses]. For them, hold vs sell is a retirement and estate decision, and advice biased toward holding can do real harm.
- **This conflict is manageable, not disqualifying, if** the model is transparent (inputs and sensitivity shown) and fixed-fee. It should also be co-signed by an independent registered tax agent, and the PM must disclose in writing that it loses revenue on a sale. **It becomes disqualifying if** the review is free, the PM is paid only by retention, and the output is a recommendation rather than a model.

**3. Hold/sell and refinance advice is regulated, and three regimes stack. Severity: High (legal path), Med (cost).**
- **Credit (NCCP).** Recommending a loan or lender, or helping apply, is credit assistance. It needs an ACL or authorised credit-representative status, and since 2021 brokers owe a best-interests duty [verified: general knowledge of NCCP s 158LA; confirm with counsel]. A narrow "mere referrer" exemption exists, but it bars anything beyond referral [unverified: reg-level detail not checked].
- **Tax.** After the 2026 CGT and negative-gearing reform, any hold/sell model is mostly a tax computation. It covers deemed disposal at 30 June 2027, indexation plus a 30% minimum tax, grandfathered gearing, and apportionment rules still pending in "Tranche 2" (exposure draft 4 Aug 2026) [verified: Nexia/Corrs/MinterEllison summaries]. Giving that for a fee is a **tax agent service** needing Tax Practitioners Board registration [estimate: Tax Agent Services Act 2009; confirm]. The founder is a CFO, not a registered tax agent. Partner with one.
- **Financial products (AFSL).** Direct residential property is not a financial product, so "hold this house" needs no AFSL. Anything touching super/SMSF purchases, LRBAs or managed property funds does [estimate: Corporations Act s 763A–765A; confirm]. Ban SMSF property advice outright: it is ASIC's spruiker hotspot.
- **Estate agency.** Buyers' agency needs a Victorian estate agent's licence [verified: CAV], and a separate licence in each other state where purchases happen.
- **s 48A.** CAV's rebate statement requires any rebate received "in connection with the sale, management or leasing of the property" to go to the client [verified: CAV form wording via search]. A broker commission on refinancing a managed property, if received by the agency, is plausibly caught. Hence the broking must sit in a **separate legal entity** that contracts directly with the landlord, with the agency receiving nothing. Whether s 48A looks through related entities is **unknown: senior counsel question #1.**

**4. Retention uplift is plausible but can't be proven at starting scale. Severity: Med (strategy), High (if used to justify roll prices).**
- The banking evidence that multi-product customers churn less is mostly selection: engaged customers buy more products. I found no Australian PM data on this.
- Statistical power: detecting a fall from 12% to 8% annual churn needs about **880 properties per arm** for 12 months (α=0.05, power 0.8) [estimate: standard two-proportion calculation]. A 250–500-property acquired book **can't prove the effect within a year.** Don't pay roll multiples on an assumed retention uplift.

**5. Subscription analytics has little demand. Severity: Med.**
- About **71–72% of investor individuals own one property** and about 0.85% own six or more [verified: ATO 2022–23 via Firstlinks/PIPA podcast]. Single-property owners already get free equity estimates from banks, REA/Domain and Cotality apps.
- I estimate **under 5% of a managed book would pay $10+/month** for analytics [estimate]. Analytics is a feature that supports retention, not a product line.

**6. Developer lease-ups combined with investor purchase support is the spruiker trap. Severity: High if combined.**
- The round-1 synthesis recommended developer lease-up mandates as a channel. With negative gearing now limited to new builds, the obvious "next purchase" is off-the-plan stock, and developers pay 3–6%+ marketing commissions [unverified].
- Steering your own landlords into a lease-up client's stock, while presenting as independent, would destroy the independence brand and invite ASIC/CAV attention.
- Hard rule: **no vendor- or developer-paid remuneration on any purchase support**, ever.

## Things the brief gets wrong, misses or understates
- **It misses the 2026 federal tax reform entirely.** This is the single largest change to landlord economics in a generation, and the brief predates it.
  - From 1 July 2027 the CGT discount is replaced by indexation with a 30% minimum tax, and existing assets are deemed sold and reacquired on 30 June 2027.
  - Negative gearing for established dwellings acquired after 12 May 2026 is removed.
  - **Implications:**
    - (a) Existing landlords' grandfathered gearing *raises* the cost of selling and switching to another established property. That lowers sale churn and is good for PM books.
    - (b) New investor purchases of established inner-north stock fall. That shrinks the long-run inflow of new managements, for everyone.
    - (c) Confusion creates a time-boxed demand spike for hold/sell reviews in **Nov 2026 – Jun 2027**, before the founder will own a book. *Time-sensitive.*
- **The "next purchase" is increasingly interstate and new-build.** A one-corridor PM can't manage it. At best it can refer it out, which may itself be s 48A-exposed if any fee flows back.
- **It doesn't say what landlords pay for today.**
  - Accountants: about $300–800/yr per rental schedule [estimate].
  - Brokers: paid by lenders; 81.6% of new home loans now go through brokers [verified: MFAA/Cotality, June quarter 2026].
  - Buyers' agents: about $10–18k fixed or 1.5–3% [verified: secondary guide, May 2026].
  - Investor "advisory" firms bundle research with buyers' agency.
  - The PM is the only one of these who sees the actual rent ledger, vacancy and maintenance history. That data, not the advice, is the asset.
- **"Landlord" is the wrong unit.** Model LTV per landlord household (average about 1.3–1.5 properties with you), not per property [estimate].

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| Most landlords own one property | ~2.26m individuals with rental property; >1.6m (~71–72%) own one; ~0.85% own 6+ | [verified: ATO Taxation Statistics 2022–23 via Firstlinks; PIPA podcast] |
| Investors are older | ~27% of landlords aged 60+ (2022–23); ~48% aged 45–64 | [unverified: secondary ATO analyses] |
| Investor purchase volume | 52,599 investor commitments, June quarter 2026, −8.6% on the quarter; drop concentrated in NSW/VIC; investor construction loans 8,468 (series high) | [verified: ABS via trade press, 14 Aug 2026]. Next release 11 Nov 2026 |
| Victorian investor loans | 11,167 in March quarter 2025 | [verified: trade press, 2025 data, stale] |
| Investors buying interstate | 67.1% (2025) → 73% (2026) open to interstate | [verified: Momentum Wealth surveys; intent only] |
| Investors who sold in the past year | 16.7% sold ≥1 property, highest since 2022 | [unverified: PIPA 2025 via podcast summary] |
| Negative gearing / CGT reform | Passed Senate 25 Jun 2026; established dwellings bought after 12 May 2026 lose gearing; CGT indexation + 30% minimum from 1 Jul 2027; deemed disposal 30 Jun 2027; apportionment in Tranche 2 | [verified: Corrs, MinterEllison, Nexia, trade press]. Royal Assent date conflicts (18 vs 26 Jun) |
| Broker commission | Upfront 0.55–0.65%; trail 0.15–0.20%; clawback ~18–24 months; ING clawback change from 1 Aug 2026 | [verified: MFAA, Mozo, The Adviser] |
| Broker share | 81.6% of new home loans (June quarter 2026) | [verified: MFAA/Cotality, 3 Sep 2026] |
| Buyers' agent licensing and fees | Vic licence required; $10–18k fixed or 1.5–3% | [verified: CAV] / [verified: secondary guide] |
| Victorian land tax | $50k threshold ($25k trusts) from 2024; COVID debt levy to 30 Jun 2033 | [verified: SRO]. Brief's implied rate table not confirmed |
| s 48A scope | Rebates "in connection with the sale, management or leasing" must go to client | [verified: CAV rebate statement wording]. Related-entity reach [unverified] |
| New managements from landlord purchases | 2–6 per 1,000 properties per year | [estimate: funnel above] |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Drop "next purchase feeds new managements" from the growth model.** Set it to ~0.3–0.5% of the book per year. Growth still has to come from rolls and point-of-purchase referrals (round 1).
2. **Make the lead investment service a paid "Landlord Hold/Sell & Refinance Review"** ($290–490 fixed, or free for managed landlords once a year).
   - Contents: after-tax hold vs sell under the 2027 rules, land tax, rent and vacancy forecast, an equity/refinance check, and a sale-propensity flag for internal use.
   - Co-signed by a registered tax agent partner, with a written disclosure that "we lose fees if you sell".
3. **Put broking in a separate entity** (credit representative under an aggregator ACL). Hire a broker on salary plus bonus, not a commission-split contractor, to keep advice quality. The agency takes nothing until s 48A advice confirms a structure. Model group revenue, not agency revenue.
4. **Use the sale-propensity model defensively, not to block sales.** When the model flags a likely sale, the response has three parts:
   - (a) offer the review early;
   - (b) offer a tenant-in-place sale to an investor buyer through an independent selling agent, with management offered to the buyer at settlement (round-1 report 09's buyer-side capture);
   - (c) never discourage a sale.
   Track "sale events converted to retained management".
5. **Refer interstate and new-build purchases out, fee-free:** to an independent buyers' agent and a PM partner in the destination state. Accept it as goodwill rather than revenue until counsel clears any fee.
6. **Hard prohibitions in the policy file:** no SMSF property advice; no developer- or vendor-paid purchase fees; no buyers' agency in years 1–3; no "recommendation" output, only modelled scenarios.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| Test | Design | Metric | Kill / continue threshold | When |
|---|---|---|---|---|
| **T1 Review willingness to pay (pre-licence, runs now)** | Analytics and general information need no estate agent licence [estimate; confirm]. Partner with 2–3 accountancy firms with Melbourne landlord clients; offer a 2027 tax-reform hold/sell review at $0 / $290 / $490 (randomised price); tax agent co-signs | Paid conversion from qualified invitations; NPS; share who ask about refinance; share who ask "who manages your property, and are you happy?" | Continue if ≥8% pay at $290 *and* ≥20% of reviewees want a refinance check; kill the paid product if <3% pay at any price | Dec 2026 – Jun 2027 (window closes 30 Jun 2027) |
| **T2 Refinance conversion** | Same cohort, referred to a partner broker (no fee to the founder until legal advice) | Share of indebted reviewees who settle a refinance within 6 months | Viable if ≥10%; drop broking if <4% | Jan – Dec 2027 |
| **T3 Retention effect** | On the first acquired book, randomise half of landlords to a proactive annual review; ask a partner agency to replicate to reach ~900 per arm, or accept a 24-month horizon | 12-month lost-management rate; sale-intent signals; sale events converted to retained management | Claim retention value only if ≥3 points lower churn (p<0.1) or ≥30% of flagged sales retained | 2028–2029 |
| **T4 Funnel check** | Log every managed landlord purchase (postcode, new vs established, state) | New in-radius managements per 1,000 per year | If <5, the "feeds managements" claim is formally dead | Rolling from first book |

Legal gate before T2 revenue: senior counsel on s 48A related-entity reach, NCCP referrer rules, and TPB scope (~2–3 weeks, ~$10–20k [estimate]).

## Answers to the round-2 questions in my domain
1. **Which services carry the economics, and in what order:**
   - First, the hold/sell and refinance review, as a retention instrument and lead source.
   - Second, broking via a separate entity.
   - Buyers' agency and analytics subscriptions don't carry economics.
2. **LTV:**
   - The PM relationship gives about $600–850 contribution per property per year over about 7–9 years.
   - Investment services add about **$100–200 per landlord household per year** at steady state: broking about $55–150 including trail, review fees about $20–50 [estimate].
   - A 2-point churn reduction, if proven, adds about $100–140 per property per year.
   - Combined, they move the property count needed for a $500k draw from about 2,000–2,500 to about **1,700–2,200**. That helps, but it is not transformative.
3. **Regulation:**
   - Credit needs ACL or credit-rep status plus the best-interests duty. Manageable via an aggregator.
   - Tax advice needs TPB registration. Manageable via a partner.
   - An AFSL is only needed for SMSF or funds. Avoid.
   - Buyers' agency needs a licence in each state.
   - s 48A on any fee received by the agency.
   - **Disqualifying conflicts:** developer-paid purchase support combined with a claim of independence; a free review paid for only by retention with no disclosure; SMSF property advice.
4. **Founder edge:**
   - Decisive: sale-propensity modelling from ledger, tenure and owner-age data; a transparent after-tax hold/sell engine under the new CGT rules (CFO plus stats); and the trial design that measures retention honestly.
   - Irrelevant: selling the advice itself, where trust, licences and tax registration do the work.
5. **Smallest test:** T1. It can run before the licence and before any acquisition, it is time-boxed by the 30 June 2027 tax change, and it costs about $15–30k.

## Questions I'd hand to other specialists
- **Vic regulatory counsel:**
  - Does s 48A reach commissions earned by a *related* broking entity on a managed landlord's refinance?
  - Is a free hold/sell review given by a managing agent "estate agency" conduct, and does it engage s 49A disclosure?
- **Tax/TPB specialist:** Where is the line between "general information" and a tax agent service for an automated after-tax hold/sell model? How do Tranche 2 apportionment rules change the output?
- **CFO modeller:** Re-run the scale-for-$500k model with broking group revenue (with a trail-book valuation) and churn sensitivity of −1/−2/−3 points.
- **Corridor analyst:** What share of inner-north rental stock is post-12-May-2026 new build vs grandfathered established? How fast will new-investor inflow decline?
- **Privacy specialist:** Is using rent-ledger and owner data to market credit services a permitted secondary use (APP 6/7)? Does it trigger loss of the small-business exemption?
- **Retention specialist:** Can a multi-agency data partnership supply the ~900-per-arm sample for T3?
