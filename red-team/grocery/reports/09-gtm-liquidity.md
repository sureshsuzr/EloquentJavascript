# Marketplace Go-to-Market & Liquidity Lead: red-team report

## Verdict
**Survives only if** it is run as a scheduled-delivery (not instant), single-cluster, specialty-basket marketplace whose launch unit is a *merchant strip or market hall*, not a suburb, and only if customers actually want baskets that span several merchants. That last point is unproven, and it is where the idea lives or dies. **The biggest issue:** this exact model has already been run in Melbourne. YourGrocer (2013–22) was a marketplace of independent grocers, butchers, fishmongers, and the Queen Vic, Prahran and South Melbourne markets. It reached about 15% of online grocery in inner-north postcodes, then ran out of money and was sold for about $3,000. The brief doesn't mention it. The shelf-scan software and the universal catalogue don't fix what killed YourGrocer: order density and contribution margin per order. "Global from day 1" works for the software and the catalogue. It does not work for liquidity.

## Verdict on the business model
From a liquidity point of view, I rank the three versions like this:
1. **Software and catalogue sold to merchants (and through them to Uber Eats/DoorDash), plus a product-availability search layer.** This can be global from day 1, carries no density risk, and rides on order volume Uber and DoorDash already generate. It is the most scalable version and the weakest on wealth unless the catalogue becomes infrastructure.
2. **A marketplace in one cluster with scheduled windows, run as a 90-day test.** It is worth running for its *learning value* (multi-merchant demand, scan accuracy, merchant picking discipline), but it should be priced as an option, not as a company.
3. **A multi-city instant-delivery marketplace.** Fatal. Milkrun, Voly, Send, Deliveroo and YourGrocer all died in AU in 2022–23. Coles is now exclusive with Uber Eats, and Woolworths and Aldi are on DoorDash. A new entrant has no instant-delivery slot left to fill.

The marketplace's real job is to **prove demand and generate catalogue data**. If it reaches the density thresholds below, it becomes the business. If not, roll the software into version 1.

## Attacks on the thesis

**1. A direct Melbourne precedent failed (High).** YourGrocer partnered with independent market retailers from 2013. It had a network of 150 local businesses including QVM, Prahran and South Melbourne markets, 80,000+ orders by 2017, about 15% of online grocery in inner-north postcodes and about $4.5M of groceries through the platform **[verified: SmartCompany/Startup Daily via search summaries]**. It charged free delivery over $60 with a $3 weekly fee **[verified: search summary]**. That implies an average basket of about $56 by 2017 **[estimate: $4.5M ÷ 80k]**. Its last raise, a 2022 crowdfund seeking over $1M, brought in about $225k. It stopped trading around Dec 2022 and was bought by Rewardle (ASX: RXH) for about $3,000 **[verified: Business News Australia via search; date reported as late 2022 / early 2023]**. Lesson: it had brand love and real share in Melbourne's most receptive postcodes, and still never reached self-funding density in nine years. Software doesn't change its order economics. Only bigger baskets, a higher take rate or batching does.

**2. The convenience mission is closed (High).** Since Dec 2025 Coles has been exclusive to Uber Eats, Woolworths is on DoorDash (adding 150+ stores in Jul 2026 and offering 40% off a first order), and Aldi is on DoorDash in Victoria **[verified: Inside FMCG, Medianet, Concrete Playground via search]**. IGA has been on DoorDash since 2021 **[verified: Inside Retail]**. Woolworths kept Milkrun as its roughly 30-minute "missing dinner ingredient" brand **[verified: Woolworths newsroom via search]**, so the brief's framing of Milkrun simply as a failure is stale. Any basket a supermarket can fill will be won by a supermarket on an app the customer already has. What's left is **selection the supermarkets don't carry**.

**3. Multi-merchant baskets multiply failure (High).** If each item has a 92% chance of being in stock (a realistic figure for inventory updated by scans every few days, not continuously), a 20-item basket arrives complete only 19% of the time (0.92^20). At 95% it's 36% **[estimate]**. Each extra merchant adds another pickup that can run late, which hurts on-time delivery (the customer experiences the slowest leg). Customers churn on substitutions and lateness, not on fees. The selling point of the basket is also its biggest operational weakness.

**4. Demand for multi-merchant baskets is assumed, not shown (High).** No evidence was found that a meaningful share of Australian shoppers want butcher + Asian grocer + bakery in a single delivery, as opposed to wanting one specialty store delivered. If most real orders are single-merchant, Uber Eats/DoorDash already serve them (many ethnic grocers are listed) **[unverified count]**, and in the Chinese-speaking market HungryPanda/PandaFresh offers same-day grocery and bought Melbourne's Easi **[verified: App Store, Startup Daily]**.

**5. Density math (High).** I modelled a scheduled, batched order: basket $80, 15% take ($12) plus $8 delivery fee = $20 revenue. Costs are a batched courier at about 3 drops per hour at a fully loaded $40/hr ($13.30), payments ($1.40), refunds and substitutions ($1.60) and support ($1). That leaves **about $2.70 contribution per order** before CAC **[estimate]**. A cluster's fixed costs (ops lead, merchant success, support, tooling) run about $250k a year **[estimate]**, so break-even needs **about 250 orders a day** at that margin. At $8 contribution (20% take and 4 drops per hour) it's about 85 orders a day. Either is far above anything YourGrocer appears to have achieved per area.

**6. CAC (Med–High).** Milkrun's leaked cost per new customer was $57 in 2023 **[verified: SMH via SmartCompany/Forbes summaries]**. The giants now subsidise first orders by 40%, so paid CAC for a no-name grocery app in Melbourne in 2026 is plausibly $50–90 **[estimate]**. At $2.70 contribution per order, payback takes 20+ orders. Paid acquisition can't be the main engine. Community, building and search channels have to be.

**7. Supply-side cost is underrated (Med).** Field sales to independent grocers in AU takes 3–6 visits and 2–6 weeks per merchant **[estimate from food-delivery onboarding experience]**. The first scan of a 4,000–8,000-SKU Asian grocer is several hours of work plus a lot of manual matching of imported SKUs with poor barcode data **[estimate]**. Fresh categories (butcher, greengrocer, fish) sell by weight and are barely scannable: they need a short manual menu. So shelf-scanning helps mainly packaged ethnic grocery, which is also where the catalogue is most valuable. Merchant churn is driven by picking during peak trading. Saturday at 11am is when the grocer is busiest and when your orders spike.

**8. Price-parity trap (Med).** Choice (Oct 2025) found supermarket items cost 11–13% more on Uber Eats and DoorDash than in store, and up to about 39% more including fees **[verified: Choice via search summaries]**. Independents will want to mark up to cover a 15% clip. Customers in specialty and ethnic grocery are price-literate and compare in store weekly. If you allow markups, repeat rate suffers. If you ban them, merchant adoption suffers.

## Things the brief gets wrong, misses or understates
- **Misses YourGrocer** (closest precedent, same city, same model) and **QVM's own online multi-trader shop**: one checkout across many traders, delivery to 200+ suburbs, YourGrocer-powered from 2019 **[verified: QVM/Inside Retail via search; current status unverified, so check before launching]**. A market hall is the natural first site because multi-stop pickup collapses to one stop.
- **"Global from day 1"**: true for the scanning app, catalogue and SEO pages. False for anything involving delivery. Liquidity is built one 2–3 km² cluster at a time.
- **Understates the Dec 2025 landscape reset** (Coles+Uber exclusive, Woolworths and Aldi on DoorDash, Bunnings on Uber Eats Feb 2026 **[verified: SmartCompany tag page via search]**). The aggregators are now the default storefront for independents too. The founder's competitor is Uber's merchant tooling, not Instacart.
- **Instant vs scheduled isn't specified.** That choice decides batching, merchant picking load and contribution. Choose scheduled.
- **Brief date** says 3 Nov 2026, but today is 2 Nov 2026. Minor, but date-stamp the decisions.

## Numbers checked
| Claim / input | Finding | Status / source |
|---|---|---|
| Milkrun failed | Shut Apr 2023 after $86M raised; Woolworths kept the brand as its ~30-min service | verified: SmartCompany, Inside Retail, Woolworths newsroom via search |
| Milkrun unit economics | ~$10–13 loss/order; $57 per new customer | verified (leaked docs, disputed): SMH via SmartCompany/Forbes |
| Voly | Closed Nov 2022, ran out of runway | verified: Startup Daily/SmartCompany |
| YourGrocer | 150 merchants incl. 3 markets; 80k orders, 15% inner-north share, $4.5M GMV (2017); collapsed ~Dec 2022; sold ~$3k | verified: search summaries of SmartCompany/BNA; FY22 $9.2M sales unverified (Dealroom) |
| Supermarket online penetration | Coles 11.2% FY25, 13.3% Q1 FY26; Woolworths 16.2% Q1 FY26 | verified: Market Index/Power Retail via search |
| Delivery-app markup | 11–13% item markup; up to ~39% with fees | verified: Choice Oct 2025 via search |
| Aggregator commission | DoorDash AU 15/25/30%; Uber Eats ~20/25/30% after Mar 2026 | unverified (secondary blogs conflict) |
| Box Hill density | 14,353 residents (2021), ~4,100/km² over 3.5 km² | verified: Wikipedia/ABS 2021 |
| CBD students | ~39% of CBD residents in tertiary education; ~80% under 35 | verified: City of Melbourne profile via search (date unclear) |
| Paid CAC 2026 | $50–90 per first-order customer | estimate (Milkrun $57 in 2023 + 40%-off incumbent promos) |
| Contribution/order (scheduled) | ~$2.70 at 15% take; ~$8 at 20% take + 4 drops/hr | estimate (model above) |

## Improvements (ranked by impact)
1. **Make the launch unit a pickup hub, not a suburb.** Start where 8–12 complementary merchants sit within about 300 m (a market hall or a dense strip). The courier does one pickup run; merchants (or one paid "runner") stage bags at a single point. That turns multi-stop into single-stop and is the closest analogue to Fulfilio's hub consolidation.
2. **Scheduled windows only** (e.g. 5–7pm and 7–9pm same day, order by 2pm; plus weekend morning). This allows batching at 3–5 drops per hour, lets merchants pick off-peak, and avoids competing on speed.
3. **Make the product proposition "the specialty shop the supermarket doesn't sell".** Specialty and ethnic first, with fresh protein and bakery as basket-builders. Skip general groceries, alcohol and pharmacy at launch (age and scheduling rules).
4. **Use the catalogue as a demand engine** (the transferable LocalAgentFinder lesson). Publish product-by-suburb availability pages ("where to buy [brand/product] in Box Hill") and a "find it near me" search. Long-tail SEO for specialty SKUs has intent and zero CAC. Caveat: in 2026, Google AI Overviews reduce organic click-through, so measure clicks, not rankings. Comparison and SEO don't help with *repeat* grocery frequency, which is a habit and an app retention problem.
5. **Get distribution through buildings, not ads.** Use build-to-rent and student-accommodation operators in CBD/Southbank/Box Hill (one landlord means 300–1,000 doors and a concierge or parcel room for unattended drops), plus community channels: WeChat/RedNote groups for Box Hill, Indian community groups for the Tarneit/Point Cook corridor, and university student associations. Pay for referrals ($15/$15) only after a second order, not the first.
6. **Merchant terms:** 15% commission with **price parity** (in-store price = app price), with the delivery fee paid by the customer. Offer a free listing feed to Uber Eats/DoorDash from your catalogue as the merchant hook. That way merchants get value even when your marketplace is thin, which protects supply retention.
7. **Use third-party last-mile (Uber Direct/DoorDash Drive) until about 80 orders a day**, then trial employed or contracted batch drivers. This keeps fixed costs variable during the test (pricing unverified; verify AU rates).

## Tests & kill criteria (90-day plan)
**Cluster choice (weeks 0–2, $3k):** run a smoke test in three candidate areas with landing pages and community posts. Collect waitlist sign-ups and the "what would you order" basket composition. The candidates:
- (a) **CBD/Carlton/North Melbourne anchored on QVM** plus CBD Asian grocers: highest residential density, no-car students, one-hub pickup. The risk is small baskets.
- (b) **Box Hill core** (Station St/Whitehorse Rd/Box Hill Central): Asian grocers, butchers and bakeries clustered by the station, an apartment pipeline, and bigger family baskets in surrounding Whitehorse. The risk is that PandaFresh/HungryPanda and WeChat group-buying are entrenched.
- (c) **Footscray** (Vietnamese/African/Indian, Footscray Market). Lower basket value.

My prior is **(b) Box Hill with delivery to about 4 km for scheduled windows**: the merchant cluster plus family baskets beat the CBD's student baskets. Let the waitlist data overrule me.

**Phase 1, concierge (weeks 2–6, about $20k):** sign 8–10 merchants on paper. Hand-build the top 600 SKUs. Take orders through a simple storefront or WhatsApp. Founder plus a contract ops lead (about $9k/month) pick up and deliver or dispatch through Uber Direct. Sign two building partners. Target 150 orders.

**Phase 2, product in loop (weeks 6–13, about $55k):** the scanning app goes live with 3–4 packaged-goods merchants, with weekly audits against physical counts. Spend $8k on a paid CAC test (Meta, Google, RedNote) and run referrals. Total cash for 90 days is about **$80k plus roughly 20 founder hours a week** **[estimate]**.

| Metric | Go (day 90) | Kill |
|---|---|---|
| Multi-merchant orders (≥2 merchants) | ≥40% | <20% (aggregation thesis dead; pivot to software) |
| Item found rate (scan-based merchants) | ≥95% | <90% after 6 weeks |
| Perfect-order rate (complete, on time) | ≥85% | <70% |
| Orders/day run-rate in cluster | ≥30, with a trajectory to 100 by month 9 | <12 |
| AOV | ≥$75 | <$50 |
| Month-1 repeat (ordered again within 30 days) | ≥40% | <20% |
| Orders per active customer per month | ≥2.5 | <1.5 |
| Blended CAC / paid CAC | ≤$30 / ≤$55 | >$50 / >$90 |
| Contribution/order after courier, excl. CAC | ≥$4 | <$0 |
| Merchant retention / weekly scan compliance | ≥80% / ≥80% | <60% |
| Merchant pick time | ≤10 min/order | >20 min |

**When to expand:** only after a cluster holds ≥100 orders a day with positive contribution after courier costs for 8 consecutive weeks, and month-3 retention is ≥25%. Then clone with a playbook budget of ≤$150k per cluster and a target of ≤6 months to cluster break-even. Each new cluster should reuse at least 50% of catalogue SKUs (this is where the "global" catalogue pays off).

## Answers to the brief's questions in my domain
- **Q1 (density):** A scheduled, batched cluster needs roughly **85–250 orders a day** to cover about $250k of cluster overhead, depending on take rate (15–20%) and drops per hour (3–4) **[estimate]**. Instant delivery needs more and still fails.
- **Q2 (merchant adoption):** Merchants will sign up easily, since a free extra channel is attractive. They will *stay accurate and pick reliably* only if they see ≥$1.5–3k a month of incremental sales within 6–8 weeks **[estimate]**. Below that, scans go stale and found rates fall. Supply retention follows demand density.
- **Q3 (consumer choice):** Specialty, diaspora and premium-fresh baskets over $70, ordered on a weekly schedule. Not top-ups and not general groceries.
- **Q6 (global):** Global: scanning app, catalogue, SKU matching, availability search and SEO, and merchant feeds to Uber/DoorDash. Local: merchants, couriers, windows and community demand. It is a city-by-city density business. Don't open a second city until cluster economics clear the expansion gate.
- **Q10 (smallest test):** The 90-day concierge-then-product test above for about $80k. The single most diagnostic number is the multi-merchant order share.

## Questions I'd hand to other specialists
- **CFO/unit economics:** contribution per order at 3 vs 4 drops per hour and 15% vs 20% take, including substitution refunds. What break-even orders a day does your model give?
- **Legal:** how the Fair Work "employee-like"/delivery minimum standards affect batch-driver costs. The Victorian liquor delivery and age-verification rules for a later bottle-shop category. Price-parity clauses under competition law.
- **Tech/CV:** found-rate accuracy from shelf scans for imported Asian packaged goods with non-GS1 or missing barcodes, and how long a scan stays fresh.
- **Competitive:** does Uber Eats or DoorDash AU support a single basket across several stores today? Is QVM's online shop still running, and on what platform, after YourGrocer's collapse?
- **Merchant research:** what effective commission and markup independent Asian grocers in Box Hill pay on Uber, DoorDash and HungryPanda today, and their minimum acceptable fee for a channel that also lists them on those apps.
- **Founder-fit:** can this be tested at about 20 hours a week while employed, or does the concierge phase require leaving the job (which changes the comparison with the round-3 pricing-engine path)?
