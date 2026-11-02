# Competitive Landscape Analyst (Grocery & Quick Commerce): red-team report

FX used throughout: US$1 = A$1.52, €1 = A$1.75, A$1 = ₹57 **[estimate: approximate late-2026 rates; check before using in a model]**. Research date: 2 Nov 2026. Several primary sources (uber.com, pulse.bot) were blocked in this session, so some figures rest on search-result summaries of trade press. Those are labelled.

## Verdict
**As a consumer marketplace with its own delivery: fatal in Australia.** The one feature that sets it apart, a single basket drawn from several local stores, is already shipping inside the incumbents. DoorDash AU has DoubleDash (one extra store, no extra delivery fee). Uber Eats has offered two-store ordering since Oct 2023. DoorDash-owned Deliveroo began trialling three-store "Bundles" in May 2026. Since Menulog left (Nov 2025), the AU on-demand market has consolidated into a Uber Eats/DoorDash duopoly, and each platform is tied to one supermarket major. Every venture-funded AU entrant from 2021–23 (Milkrun, Voly, Send) failed. **It survives only as infrastructure:** shelf-scan inventory, catalogue and listing syndication that makes non-POS independents sellable on Uber Eats, DoorDash, Amazon and Google, sold to them or to Metcash. **The single biggest issue:** demand. The platforms that own the customer can copy the aggregation as a feature, and in part already have. They cannot easily copy accurate inventory from merchants with no POS feed.

## Verdict on the business model
- **Full marketplace with delivery (founder's version): no.** It competes with two well-funded platforms that already list independents, already pool baskets across stores and already run subscriptions (Uber One, DashPass). Its starting cost position is worse than Milkrun's: Milkrun had one picking location per order; this model has several per order. Milkrun raised ~A$86M and still failed.
- **Marketplace for specialty/ethnic baskets in dense corridors: niche, possibly a lifestyle business.** HungryPanda, the Asian grocery chains' own apps, and Uber Eats/DoorDash listings of the same shops already cover a lot of it. Revenue is capped at a few A$M per city.
- **Software/data layer: the only version with a credible path.** Product: "make any shop's shelf listable and accurate everywhere." Customers are independents (subscription), Metcash/IGA, Foodworks/Drakes-type banner groups, and the platforms themselves (catalogue data, inventory confidence scores). The precedent outcome is an acquisition: Google bought Pointy (local inventory from POS) in 2020, and Uber bought Cornershop, Postmates and Drizly. The realistic outcome is a A$20–150M strategic sale, not a standalone giant **[estimate: comparable-exit range; Pointy price reported ~US$163M, unverified]**.

## Attacks on the thesis

**1. Multi-store aggregation is a commodity feature in the incumbents. Severity: High.**
- DoorDash AU's help centre documents DoubleDash: add one more nearby store (grocery, convenience, alcohol, retail) to an active order, with no additional delivery fee but a service fee **[verified: help.doordash.com/en-au DoubleDash FAQ, via search summary]**. DoorDash says it built DoubleDash first for Australia **[verified: Convenience World/trade report via search summary]**.
- Uber Eats has let customers order from two nearby stores at once since Oct 2023 **[verified: TechCrunch 11 Oct 2023 headline]**.
- Deliveroo (DoorDash-owned since 2 Oct 2025, consideration US$3.72B ≈ A$5.7B **[verified: DoorDash FY2025 10-K]**) began trialling "Bundles" in May 2026: up to three grocery/retail stores in one basket, no extra delivery fee. The reason given was that lack of selection in a single store is a top barrier to grocery orders **[verified: trade press via search summary; page blocked]**. DoorDash can port this to AU at will.
- Grubhub offers two-retailer baskets **[verified: Chain Store Age, undated]**.
- **Implication:** the founder's headline UX already exists at small scale, inside apps that carry tens of millions of users' cards and subscriptions. The platforms have not gone further because multi-pickup costs more, not because they lack the capability. If demand appears, they can raise the store limit in a sprint.

**2. The AU on-demand market has consolidated into two platforms, each tied to a major supermarket. Severity: High.**
- Menulog stopped operating on 26 Nov 2025 after Prosus bought Just Eat Takeaway for €4.1B **[verified: SMH, Smart Company, Retail Gazette, Nov 2025]**. Commentary put Uber Eats at >70% food-delivery share **[unverified: commentator figure, method unclear]**.
- Coles became exclusive to Uber Eats from 26 Dec 2025, covering marketplace, Coles' own e-commerce on-demand fulfilment and retail media **[verified: Medianet/Uber newsroom, Dec 2025, via search summary]**.
- Woolworths joined DoorDash on 11 Dec 2025 and added 150+ more stores in July 2026 with a 40%-off-first-order promotion. It stays on Uber Eats and runs its own Milkrun (claimed 33-minute average, 630+ stores). Woolworths says On Demand is ~40% of its e-commerce orders **[verified: Woolworths/DoorDash releases, Medianet Jul 2026; Woolworths' own claims]**.
- More than 100 IGA stores deliver via DoorDash **[verified: Smart Company, via search summary; date unclear]**. Uber Eats lists IGA and Foodworks stores in Melbourne and publishes an IGA case study **[verified: ubereats.com category page; merchants.ubereats.com]**.
- Amazon AU launched fresh grocery with Harris Farm in Jan 2026 (Sydney, picked from the Leichhardt store, Amazon Flex last mile) and extended it to Canberra by May 2026 **[verified: Amazon AU IR release; Inside Retail]**. The large independent specialist chain that would be a natural anchor merchant is already taken.
- **Implication:** the best independents are already on one or both platforms. The merchants left are mostly those whose inventory is too messy to list, which is exactly the hardest segment to serve. The founder's actual wedge is the inventory problem, not delivery.

**3. Every AU entrant in this category has died, and the causes still apply. Severity: High.**
- **Milkrun:** raised ~A$86M, shut on 14 Apr 2023, ~400 jobs lost; Woolworths bought the brand and customer list for a reported ~A$10M **[verified: Business News Australia, B&T, Broadsheet]**. Causes: owned dark stores, salaried riders, A$5 delivery fee below cost, small baskets, and a 2022 funding market that closed **[verified/estimate: reported loss per order; cost structure from coverage]**. Woolworths rebuilt it on existing stores and gig couriers. That is the founder's "existing capacity" idea, already in the hands of the incumbent with the most stores.
- **Voly:** A$18M seed led by Sequoia (2021), dropped its 15-minute promise and closed warehouses in mid-2022, shut Nov 2022 **[verified: Startup Daily, The New Daily]**.
- **Send:** voluntary administration in 2022, within 12 months of launch **[verified: Startup Daily via search summary]**.
- **Deliveroo AU** went into voluntary administration in Nov 2022 **[verified: same coverage]**.
- **What killed them:** (a) subsidised delivery fees, which taught customers to expect A$0–5 delivery; (b) baskets of A$25–40 that cannot absorb A$8–12 of last-mile cost **[estimate: AU rider cost per drop]**; (c) inventory and capex in dark stores; (d) no repeat-order moat against Woolworths/Coles loyalty. This model removes (c) but makes (b) worse with multiple pickups, and adds a new failure mode: wrong inventory at merchants who are not paid to keep it accurate.

**4. Global evidence: aggregation over independents makes small outcomes or acquisitions. Severity: Med–High.**
- **Mercato (US, the closest analogue):** founded ~2015, ~750 independent stores by 2019, US$26M Series A in Apr 2021 (≈A$40M), CEO claimed profitability in 2023, operating in 48 states in 2024 **[verified: Progressive Grocer, Pulse 2.0; 2023–24 claims unverified, secondary site]**. In 2026 New York's National Supermarket Association said its members were owed >US$1M by Mercato under a US$75M city grocery-delivery contract **[verified: one news repost; treat as unverified until checked against NY press]**. Lesson: ten years of focus on independents produced a modest e-commerce enabler living on government programmes and SaaS-like fees, not a consumer brand. Instacart took the US independents through Storefront and its IGA US partnership **[verified: corporate.iga.com Instacart page]**.
- **Instacart:** FY2025 GTV US$37.2B (≈A$56.6B), 338.8M orders (AOV ≈ US$110 ≈ A$167), revenue US$3.74B (~10% of GTV), GAAP net income US$447M, ad revenue ~US$1.07B (~2.9% of GTV) **[verified: Instacart 8-K FY2025; ad figure from Sacra, unverified]**. Instacart works because of big baskets, retailer-paid fees, and ads. Ads make roughly a third of revenue at near-full margin. An AU independent-grocer marketplace would have none of the CPG ad budgets: those go to Woolworths Cartology and Coles 360.
- **Drizly (US):** liquor marketplace on top of local stores' inventory, where stores delivered. Uber bought it for ~US$1.1B in 2021 and shut it in 2024 **[unverified: from memory, widely reported]**. This is the closest model to "merchants as dark stores". Even a scaled winner got folded into a platform's own grocery and alcohol tab.
- **Cornershop (LatAm multi-store shopper marketplace):** acquired by Uber in 2020–21 **[unverified: from memory]**. The typical exit for this category is a sale to a delivery platform.
- **Getir/Gorillas:** Getir bought Gorillas (Dec 2022), then left the UK, US, Germany and Netherlands (Apr 2024) to focus on Turkey **[verified: TechRadar, The Grocer]**. **Flink** raised US$150M at just under US$1B (Sep 2024) and liquidated its French arm **[verified: TechCrunch, ESM]**. **Jokr** left the US in 2022 **[unverified]**. **Gopuff:** US$250M at US$8.5B in Nov 2025, down from a US$15B peak, after repeated layoffs **[verified: trade press via search summary]**.
- **India (Blinkit/Zepto/Instamart):** by Mar 2026 Blinkit ran 2,243 dark stores, Zepto 1,139 and Instamart 1,143. AOVs are ~₹350–750 (≈A$6–13). Blinkit is around adjusted-EBITDA breakeven (0.6% of NOV, Q4 FY26). Instamart loses ~₹85 per order **[verified: Outlook Business, Business Today, broker estimates via search summaries]**. India works because riders cost ~A$0.50–1 per drop, density is extreme, kirana-dependent households need top-ups, and ad and convenience-fee income is large **[estimate]**. **None of this transfers to Melbourne**, where a gig drop costs roughly 10× as much and Woolworths/Coles already sit within 3–5 km of most metro homes.

**5. How Uber Eats/DoorDash would respond to a merchant-aggregation competitor. Severity: High if it gains traction.**
- **Stage 1: ignore.** A Melbourne pilot of a few thousand orders a month is invisible to them.
- **Stage 2: neutralise.** If the competitor reaches a corridor with real share, expect: zero onboarding cost and a promo-funded commission for the same independents (DoorDash and Uber already fund IGA marketing **[verified: Uber IGA case study]**); geo-targeted first-order discounts (DoorDash ran 40% off Woolworths in Jul 2026); and raising the DoubleDash/multi-store limit. Merchants will multi-home and send their attention to whichever platform brings more volume.
- **Stage 3: acquire, if the catalogue/inventory tech is good.** This is the most likely positive outcome, and it argues for building the software layer from day one.
- **Time-sensitive angle:** DoorDash lost Coles to Uber exclusivity on 26 Dec 2025. It now has a motive to build independent and specialty grocery supply in AU, which makes it a plausible **partner or acquirer** rather than only a threat. Uber Eats, with Coles locked in, has less need.

**6. A universal SKU catalogue already exists for packaged goods. Severity: Med.**
GS1 Australia's barcode and product data (National Product Catalogue) plus the platforms' own catalogues already cover packaged FMCG **[unverified: GS1 AU NPC coverage not checked this session]**. The value that is still uncaptured is in **non-barcoded and variable items** (deli, butcher, bakery, produce, ethnic imports with non-AU barcodes) and in **in-stock confidence**. It is not in matching a jar of Vegemite across 30 shops. Enterprise shelf-scan vendors (Trax, Simbe, Focal Systems) serve chains and are priced for them **[unverified: from memory]**. Nobody obvious serves low-cost phone-video scanning for non-POS AU independents. That is the white space.

## Things the brief gets wrong, misses or understates
- **"Merchants get an additional sales channel"** overstates what is new. Most decent AU independents already have one or two channels via Uber Eats/DoorDash. What the platform adds is accuracy and reach for the long tail, not a channel.
- **"Global from day 1"** contradicts every precedent. Getir, Gorillas, Jokr and Flink all lost money expanding abroad; Getir's non-Turkey markets were only ~7% of revenue when it retreated **[verified: The Grocer/Yahoo, Apr 2024]**. Marketplaces are won city by city. Only the software layer can be global early.
- **Fulfilio parallel is weaker than claimed.** Spare warehouse space was idle capacity that was easy to consolidate. Store shelves are not idle: merchants use them to serve walk-in customers who pay full margin, and staff picking for you competes with the till at peak times.
- **Missing competitors:** Amazon + Harris Farm (2026); Woolworths Milkrun on stores; Coles–Uber Eats exclusivity; DoorDash-owned Deliveroo Bundles; HungryPanda and Asian supermarket apps; Metcash's own IGA online programmes **[unverified: current Metcash online offer not checked]**.
- **Menulog's exit** (Nov 2025) leaves the third platform slot empty in food, but it shows that even a 20-year incumbent with ~24% share **[unverified share]** could not make AU delivery margins work.
- **Missing the ad business.** The model that works (Instacart) earns a large share of profit from CPG advertising. Independents' suppliers don't have national trade budgets for a startup. Without ads, a 10–15% take rate must carry everything.

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| Milkrun shut down 2023 | Closed 14 Apr 2023; ~A$86M raised; brand sold to Woolworths ~A$10M; ~400 jobs | verified: BNA, B&T, Broadsheet |
| Voly closed | Shut Nov 2022; A$18M Sequoia seed | verified: Startup Daily |
| Woolworths on-demand via Uber/DoorDash | Uber since 2021; DoorDash from 11 Dec 2025, +150 stores Jul 2026; Milkrun 630+ stores, 33-min avg | verified: Woolworths/DoorDash releases (Woolworths' claims) |
| Woolworths On Demand share of e-com | ~40% of e-commerce orders | verified as company claim |
| Coles partnerships | Exclusive Uber Eats from 26 Dec 2025; left DoorDash | verified: Medianet, Internet Retailing |
| Menulog (in brief's list as active) | **Stale:** ceased AU operations 26 Nov 2025 | verified: SMH, Smart Company |
| Amazon AU grocery | Fresh launched Jan 2026 with Harris Farm; Canberra by May 2026 | verified: Amazon AU IR, Inside Retail |
| AU grocery shares | Woolworths 38%, Coles 29%, Aldi 9%, Metcash-supplied indies 7% | verified: ACCC final report, Mar 2025 (via coverage) |
| Instacart scale | FY25 GTV US$37.2B, 338.8M orders, rev US$3.74B, NI US$447M | verified: 8-K |
| Instacart ads | ~US$1.07B | unverified (Sacra) |
| DoorDash–Deliveroo | Closed 2 Oct 2025; US$3.72B | verified: DoorDash 10-K |
| Multi-store baskets at incumbents | DoubleDash AU (1 extra store); Uber Eats 2 stores (2023); Deliveroo Bundles 3 stores trial (May 2026) | verified: DoorDash AU help, TechCrunch, trade press |
| Getir outcome | Absorbed Gorillas; left UK/EU/US Apr 2024 | verified: TechRadar, The Grocer |
| Gopuff | US$250M at US$8.5B (Nov 2025), peak US$15B | verified: trade press summary |
| India q-comm | Blinkit 2,243 dark stores; Blinkit ~EBITDA breakeven; Instamart −₹85/order | verified: Outlook Business/broker estimates |
| Mercato | ~750 stores (2019); US$26M Series A (2021); profitable claim 2023 | partly verified; 2023+ unverified |
| Drizly, Cornershop exits to Uber | US$1.1B (2021), Drizly shut 2024 | unverified (memory) |
| Uber Eats >70% AU food share | Commentary figure | unverified |

## Improvements (ranked by impact)
1. **Change the customer from consumers to supply.** Build "Shelf-to-Listing": phone-video scan → priced, photographed, in-stock catalogue → pushed to Uber Eats, DoorDash, Google local inventory and the merchant's own site. Charge merchants A$99–299/month or a share of incremental platform GMV **[estimate: pricing hypothesis]**. You then ride the duopoly's demand instead of fighting it.
2. **Target DoorDash AU as the first strategic partner.** It lost Coles and needs independent and specialty supply. Offer catalogue onboarding and inventory-confidence data. One platform partnership is worth more than 10,000 app downloads.
3. **Sell to banner groups, not to single stores:** Metcash (IGA, ~7% share via indies), Foodworks/Drakes, liquor banners. One deal brings hundreds of stores and their data; one-store sales mean bad CAC.
4. **Make freshness of stock data the product's measurable claim** (e.g., "≥95% of listed items in stock at pick time"). Platforms penalise substitutions and cancellations. If the scans measurably cut them, that is the ROI a platform will pay for.
5. **If a consumer front-end is kept, keep it narrow:** one dense corridor (e.g., Box Hill/Glen Waverley Asian grocers, or Brunswick/Coburg Middle-Eastern and Italian delis), specialty baskets the majors don't stock, scheduled delivery windows, minimum basket ≥A$80. Treat it as a demo for the software, not as the company.
6. **Design for the acquisition from day one:** clean data rights in merchant contracts (you own the catalogue images and SKU graph), APIs the platforms can plug into.

## Tests & kill criteria (≤90 days)
| Test | Metric | Kill threshold | Time |
|---|---|---|---|
| Desk audit of 3 Melbourne corridors: which independents are already on Uber Eats/DoorDash, and how stale are their listings (order 20 test baskets, count substitutions and out-of-stocks) | % of target merchants already listed; stock-out/sub rate | If ≥70% are listed **and** sub/OOS <5%, the inventory problem is solved and the software wedge is gone | 2–3 weeks, ~A$1.5k |
| Scan pilot with 10 non-POS independents | SKU recall/precision, price accuracy, minutes of merchant effort per week | <90% SKU accuracy or >60 min/week of merchant time after week 4 | 6 weeks |
| Platform conversation: DoorDash AU and Uber Eats AU grocery partnerships leads; Metcash digital | Written interest in a data pilot or catalogue API | No pilot interest from any of the three by day 90 | 4–12 weeks |
| Merchant WTP | Number of 30 pitched merchants who pay A$99+/month after a free month | <5 paying | 8–10 weeks |
| Monitor incumbent moves | DoorDash AU raising the DoubleDash store limit or launching Bundles in AU; Uber launching merchant catalogue tooling | If launched and adequate, the consumer version is dead; reposition to pure data | Ongoing |

## Answers to the brief's questions in my domain
**Q5: Who already does this, and what happened?**
- **AU:** Uber Eats and DoorDash both list independents, IGA and Foodworks, and both offer limited multi-store baskets. Woolworths runs Milkrun on its own stores and sells via both platforms. Coles is exclusive to Uber Eats. Amazon partners with Harris Farm. Menulog has gone.
- **Failures (Milkrun, Voly, Send, Deliveroo AU)** died from subsidised fees on small baskets, dark-store capex and the 2022 funding drought.
- **Globally:** quick commerce shrank back to home markets (Getir) or survived at reduced valuations (Gopuff, Flink). India works only because of its labour-cost and density economics. Instacart works on large baskets plus ads. Independent-store aggregators ended either as modest enablers (Mercato) or folded into platforms (Drizly, Cornershop).

**Q6: Global from day 1?** Not for a marketplace: it is won city by city on density, and every global q-commerce expansion destroyed capital. Software (scan → catalogue → syndication) can sell globally early, and that is another reason to make it the business.

**Q8: Which version is the business?** Software and data infrastructure sold to merchants, banner groups and platforms. A consumer front-end is a pilot or demo at most.

**White space:** inventory accuracy and catalogues for non-POS, non-barcoded long-tail merchants (deli, butcher, bakery, ethnic imports), syndicated to the platforms that own demand. It is not the delivery or the basket.

## Questions I'd hand to other specialists
- **Unit economics:** at an AU gig cost of A$8–12 per drop plus A$2–4 per extra pickup, what basket and take rate break even on 2–3-merchant orders? Is it ever below DoubleDash's "no extra delivery fee"?
- **Tech/CV:** can phone-video scans reach ≥95% SKU and price accuracy on unbranded deli/produce and non-English packaging, and how often must merchants rescan?
- **Merchant research:** what share of target independents use a POS that exports inventory (which would make scanning unnecessary)? Do IGA stores on Metcash systems already have a feed?
- **Legal:** do Uber Eats/DoorDash merchant terms or APIs let a third party push catalogue and inventory data on a merchant's behalf? Are there platform parity or exclusivity clauses?
- **Founder fit/capital:** does a likely A$20–150M strategic-sale outcome beat ~$500k salary plus equity and the rent-roll pricing-engine path on risk-adjusted terms?
