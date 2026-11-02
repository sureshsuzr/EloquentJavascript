# Marketplace Skeptic: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Fatal as written (full on-demand marketplace, "global from day 1").** **Survives-if** narrowed to a scheduled, high-basket specialty marketplace in one Melbourne catchment, or sold as an onboarding layer to the platforms that already have the demand. The biggest problem is the courier. Since 17 Aug 2026 a courier costs at least A$31.30 per engaged hour, and a multi-stop pickup uses 35–45 engaged minutes. That is A$18–24 per order before refunds, payments, support or CAC. A 10–20% take on a A$60–80 independent-grocer basket brings in only A$6–16. Each extra merchant in a basket adds cost and adds a point where the order can fail. Batching is supposed to fix this, but batching only works once order density exists, and density is exactly what a new entrant lacks.

## Verdict on the business model (which version, if any, is the business, from your lens)
| Version | Verdict | Why |
|---|---|---|
| 1. Full multi-merchant on-demand marketplace with own delivery | **Kill** | Three-sided cold start against Uber Eats and DoorDash. Both already list IGA, Aldi and Woolworths, and Uber Eats now has Coles. Contribution per order is negative below ~3 drops per courier-hour. The AU graveyard: Milkrun, Voly, Deliveroo. |
| 2. Software-only (shelf scan + catalogue sold to merchants) | **Kill as a venture** | Instacart bought exactly this capability (Arpalus, smartphone shelf-video to item-level stock, >95% item ID) on 16 Jul 2026. Independent merchants have low willingness to pay and churn heavily. At best this is a feature, not a company. |
| 3. White-label onboarding/catalogue layer for existing marketplaces (Uber Eats, DoorDash/Deliveroo, HungryPanda, Metcash/IGA) | **Keep as a 90-day test only** | It solves a real pain: long-tail grocers with no POS integration can't keep catalogue and inventory feeds current. But there are only 2–4 buyers in AU, Instacart has shown platforms build or buy this themselves, and the likely outcome is an acqui-hire or a services contract. On expected value it probably doesn't beat the A$500k salary. |
| 4. Specialty-niche marketplace (one community or category, scheduled windows, high basket) | **Survives-if** | Only version where the economics can close. Needs AOV ≥A$110, customer-paid delivery, consolidated routes (≥4 drops/hr), ≥97% item fill and ≥35% 4-week repeat. Ceiling is a profitable local business, not a venture outcome. |

From my lens, **no version is a venture-scale business that beats the round-3 hybrid path**. Version 4 is a lifestyle business and version 3 is an option. Neither should require the founder to quit.

## Attacks on the thesis (only in your domain; evidence, severity High/Med/Low)

**A1. Courier cost exceeds the clip, and the law now makes this structural. Severity: High.**
The FWC minimum standards order for on-demand food, beverage and grocery delivery took effect 17 Aug 2026. It sets A$31.30/hr for bicycles, A$31.80 for motorcycles and A$32 for cars, paid on engaged time from acceptance to completion, with a top-up over earnings periods of up to 21 days [verified: Inside Retail Aug 2026; TWU release 8 Jul 2026; SmartCompany]. A reported further 50c rise from 1 Jan 2027 is [unverified, single source; time-sensitive]. A two-merchant basket means: travel to merchant A plus wait, travel to B plus wait, then travel to the customer. That is 35–45 engaged minutes, or A$18–24 [estimate: 10 min per inter-store leg, 5 min wait per pickup, 15 min to deliver]. Uber Eats and DoorDash dilute this cost over restaurant density and stacked orders. A new entrant can't.

**A2. Grocery margins can't fund a 10–20% clip unless prices are marked up. Severity: High.**
Metcash, the IGA wholesaler, runs about 1.6% net margin [verified: alphaspread / FY results reporting]. Independent store net margins aren't published. My estimate is 2–4% net on 22–30% gross [estimate: industry norms; store P&Ls are private]. A 15% clip plus 3–5% of sales in staff picking time means each online sale loses money at shelf price. Merchants only participate by marking up online prices 10–20%, as they already do on Uber/DoorDash. That kills the price story against Woolworths/Coles online. Instacart, the most scaled operator, takes only about 7.1–7.3% of GTV as transaction revenue (about 10.1% including ads) [verified: Q1/Q2 2025 reporting; FY25 GTV US$37.2B, revenue US$3.74B; my division]. If 15% were sustainable at scale, Instacart would charge it.

**A3. Multi-merchant baskets multiply failure points. Severity: High.**
If each merchant hits 95% item availability, a basket of 10 items from 2 merchants has 0.95^10 ≈ 60% chance of arriving complete [estimate]. Every missing item becomes a refund, a substitution dispute or a support ticket. DoorDash's own developer docs say a Drive order is rejected outright if one item fails inventory unless partial-cart handling is enabled [verified: developer.doordash.com]. Two-merchant baskets also create timing risk: one shop's staff are busy, the courier waits, and the hot or cold chain breaks. The "aggregation" feature is the main feature and also the main liability.

**A4. Shelf scans go stale faster than they refresh. Severity: High.**
Instacart's Arpalus claims >95% item *identification* [verified: Supermarket News / PR Newswire 16 Jul 2026]. Identification isn't the same as quantity-on-hand, back-room stock, price-label accuracy or 4pm availability after a morning scan. Instacart solves freshness with 600k shoppers scanning as they pick. An independent grocer won't scan daily. At weekly scans, fast movers like milk, bread, meat and produce, which make up most of the basket, are wrong by mid-week [estimate]. Inaccurate inventory produces refunds, and refunds destroy repeat purchase.

**A5. The incumbents already have demand, couriers and the independents. Severity: High.**
DoorDash has run IGA delivery since 2021 (100+ stores at launch) [verified: Inside Retail Feb 2021]. Woolworths joined DoorDash in Dec 2025 while Coles moved to Uber Eats [verified: Inside FMCG 11 Dec 2025]. DoorDash closed its Deliveroo acquisition on 2 Oct 2025 (~US$3.9B) [verified: BusinessWire]. Bunnings joined Uber Eats in Feb 2026 [verified: SmartCompany tag page]. Woolworths' own ecommerce penetration is 16.2% (Q1 FY26) and 18.2% (Q1 FY27) [verified: Woolworths ASX releases via search summaries], and it runs Milkrun out of Metro stores with gig couriers. On demand, couriers and the independents themselves, the space is taken. The only gap left is the merchants these platforms can't onboard cheaply. That is an input to sell to them (version 3), not a market to fight them for.

**A6. "Global from day 1" is a category error. Severity: High.**
The software can ship globally. The marketplace can't, because liquidity is per suburb: each city needs its own merchants, couriers, regulation (gig rules, liquor, scheduled medicines) and CAC. The best-funded attempt failed. Getir was valued up to US$11.8B (~A$18B) in 2022, bought Gorillas, then quit the UK, Germany, the Netherlands and the US in Apr 2024 [verified: Bloomberg/Yahoo, Apr 2024]. Mubadala took the rest in 2024 [unverified: Wikiwand]. Jokr left the US in 2022 [unverified, from memory].

**A7. Cold start is three-sided, and each side needs the other two first. Severity: High.**
Consumers want breadth, so they need many merchants. Merchants want orders before they'll scan weekly and train pickers. Couriers want continuous jobs before they'll stay on an app paying the floor. Marketplace founders usually subsidise one side. Here the subsidy is per order (A1), so growth makes losses worse. Milkrun raised ~A$86M, lost at least A$10 per delivery [verified: Wikipedia/Startup Daily], collapsed in Apr 2023 after 19 months, and its brand sold for a reported ~A$10M [verified: B&T; price is press-reported]. Voly raised A$18M seed and shut down in Nov 2022 [verified: SmartCompany]. Deliveroo entered voluntary administration in AU in Nov 2022 [verified: SmartCompany].

**A8. Instacart's early history is the founder's case, and it was brutal. Severity: Med.**
Instacart used stores as warehouses, which is the same insight. It reportedly lost ~US$10 (~A$15) per order in 2014–15 [verified: Quartz citing The Economist; "rumoured"]. Simo said it lost money on every order until 100 million orders [unverified, secondary source]. It reached contribution-positive in only 10 US markets by 2016 [verified: Fortune Mar 2016], with US$-scale venture funding and single-store baskets. Postmates (sold to Uber 2020, ~US$2.65B) never made money on its own [unverified, from memory].

**A9. The founder's Fulfilio analogy breaks. Severity: Med.**
Fulfilio consolidated idle warehouse space for B2B shippers with contracted, predictable volume. Here the idle capacity is retail shelves and shop staff, who are busiest at exactly the times consumers order (after work, weekends). That isn't idle capacity, and every order competes with the walk-in customer at the register.

## Things the brief gets wrong, misses or understates
- **The take rate can't be quoted in isolation.** Merchants on aggregators already pay ~30% (Uber Eats restaurant marketplace rate) or 16% for self-delivery [unverified: third-party 2026 guide; Uber merchant page not checked]. Grocery rates are negotiated privately. A merchant compares the clip with their own net margin, not with Uber.
- **The FWC order changes the economics (17 Aug 2026) and the brief doesn't mention it.** Any courier-cost model from before Aug 2026, including Milkrun-era comparisons, understates costs.
- **"Deliveroo Hop" isn't an AU comparable.** Deliveroo left AU in Nov 2022, and Deliveroo is now owned by DoorDash.
- **Instacart's Arpalus deal (Jul 2026) makes the scanning wedge time-sensitive.** Expect DoorDash and Uber to follow within 12–24 months.
- **Brief date.** It says 3 Nov 2026, but today is 2 Nov 2026. Minor, but it shows the brief was drafted in a hurry.
- **Basket mismatch.** The independents the brief lists (butchers, bakeries, delis, ethnic grocers) sell perishables and variable-weight items. Those are the hardest to scan, price and substitute, and the most likely to be wrong.

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| Gig courier minimum pay | A$31.30/hr bike, A$31.80 motorbike, A$32 car, engaged time, from 17 Aug 2026; covers grocery | [verified: Inside Retail, TWU, SmartCompany] |
| Further rise 1 Jan 2027 | +50c | [unverified: single source] |
| Milkrun | ~A$86M raised; ≥A$10 loss per delivery; closed Apr 2023; brand to Woolworths ~A$10M | [verified: Wikipedia, Startup Daily, B&T] |
| Voly | A$18M seed; shut Nov 2022 | [verified: SmartCompany, Startup Daily] |
| Getir | Exited UK/DE/NL/US Apr 2024; peak valuation up to US$11.8B (~A$18B) | [verified: Bloomberg/Yahoo] |
| Instacart take | Transaction revenue ~7.1–7.3% GTV (Q1–Q2 2025); FY25 total revenue/GTV ≈10.1% | [verified: earnings summaries; derived] |
| Instacart early losses | ~US$10 (~A$15) per order, 2014–15 | [verified: Quartz citing Economist, "rumoured"] |
| Instacart shelf-scan | Acquired Arpalus 16 Jul 2026; phone video, >95% item ID | [verified: Supermarket News, Retail TouchPoints] |
| DoorDash + IGA | Since Feb 2021, 100+ stores at launch | [verified: Inside Retail] |
| Woolworths + DoorDash; Coles to Uber Eats | Dec 2025 | [verified: Inside FMCG] |
| DoorDash–Deliveroo | Completed 2 Oct 2025, ~US$3.9B | [verified: BusinessWire] |
| Woolworths ecom penetration | 16.2% Q1 FY26 → 18.2% Q1 FY27 | [verified: ASX release summaries] |
| Metcash net margin | ~1.6% | [verified: alphaspread / FY results] |
| Independent grocer net margin | 2–4% | [estimate: private data] |
| Mercato (US indie-grocer marketplace) | Raised US$26M Series A 2021; claimed profitability (undated); current status unclear | [unverified: no 2024–26 coverage found] |
| FX | US$1 ≈ A$1.54 | [estimate: ~0.65 AUD/USD] |

**Per-order contribution, two-merchant on-demand basket, launch density** [estimate]:
| Line | A$ |
|---|---|
| Basket | 75 |
| Take at 15% | +11.25 |
| Customer delivery + service fee | +9.00 |
| Courier, 40 engaged min at the floor | −21.00 |
| Payments ~1.8% of basket+fees | −1.50 |
| Refunds/missing items (4% of basket) | −3.00 |
| Support, promos, failed orders | −3.00 |
| **Contribution before CAC** | **≈ −8** |

Breakeven needs either ≥3 batched drops per courier-hour (courier cost ≈A$10) **and** AOV ≥A$110, or a customer delivery fee ≥A$15. In practice that means scheduled, not on-demand. At ~A$40 CAC and 35% 4-week repeat, payback is beyond 6 months even when contribution is positive [estimate].

## Improvements (concrete changes to the plan, ranked by impact)
1. **Drop on-demand and run scheduled windows.** Two windows a day and next-day routes turn A$21 per order into ~A$8–10 per drop at 4–5 drops/hr [estimate]. Pre-picked orders also mean merchants pick in quiet hours, which fixes A9.
2. **Choose one niche where incumbents are weak.** Examples are a Melbourne Asian or Middle-Eastern grocer cluster (Box Hill, Springvale, Footscray, Coburg) or a premium butcher+deli+bakery "weekend box". Consumers already make special trips for these baskets, so they are high-AOV and loyalty-driven. HungryPanda already competes in Asian groceries, so check its depth first.
3. **Make the customer pay for delivery and keep the merchant clip at 8–12%.** Price parity is the merchant's selling point, so don't take it away.
4. **Run version 3 in parallel as the low-cost option.** Pitch "we onboard and maintain the catalogue for your long-tail independents" to Uber Eats AU, DoorDash AU and Metcash (IGA). Charge per SKU-store per month. A signed pilot is worth more than any consumer traction.
5. **Treat scanning as internal ops, not as the product.** Have your couriers or pickers scan, as Instacart does, rather than relying on merchants.
6. **Strike "global from day 1"**. Go one catchment, then one city, then decide.

## Tests & kill criteria
| Test | Metric | Kill threshold | Time |
|---|---|---|---|
| Concierge niche marketplace: 8–12 merchants, one catchment, Shopify storefront, 2 delivery windows/day, contractor drivers on the FWC rate | AOV; item fill rate; 4-week repeat; cost per drop | AOV <A$90; fill <96%; repeat <30%; cost/drop >A$12 after week 6 | 60 days, ~A$25–40k |
| Merchant behaviour | % merchants scanning/updating weekly without nagging; acceptance of a 10% clip | <40% active at week 4; <50% accept a 10% clip | 30 days |
| Scan accuracy | Scan-predicted availability vs physical audit at order time, 5 stores | <95% availability accuracy with weekly refresh | 30 days |
| Multi-merchant basket demand | % orders drawing from ≥2 merchants | <25%. If below this, aggregation isn't the value and the thesis collapses to single-store delivery, which Uber and DoorDash already do | 60 days |
| White-label (v3) | Paid pilot or LOI from Uber Eats AU, DoorDash AU or Metcash | No paid pilot by day 90 | 90 days |

The founder can run all of this from employment with one paid operator. Quitting is justified only if test 1 passes **and** contribution is positive at 300+ orders/week.

## Answers to the brief's questions in my domain
- **Q1 Unit economics:** Negative at launch, about −A$8 per two-merchant on-demand order. Positive only with scheduled batching (≥3–4 drops/hr), AOV ≥A$110 and customer-paid delivery. Density threshold is roughly 40–60 orders per window per ~3 km catchment [estimate].
- **Q3 Consumers:** Price-sensitive buyers won't switch from Woolworths/Coles/Aldi online, and top-up buyers won't switch from Uber/DoorDash/Milkrun. The only defensible baskets are specialty or community baskets that the chains don't stock.
- **Q5 Comparables:** Milkrun, Voly and Deliveroo AU are dead. Getir, Gorillas and Jokr retreated. Instacart took about 100M orders to make money. DoorDash and Uber already serve the independents. Instacart now owns phone-based shelf scanning.
- **Q6 Global:** Not credible. This is a city-by-city density business.
- **Q8 Which version:** Version 4 (scheduled specialty niche) as a test, with version 3 (white-label to platforms) as the option. Kill versions 1 and 2.
- **Q9 Founder path:** The round-3 hybrid (~A$3.4M 7-yr modelled, floor ~A$1.5M) beats any version here on risk-adjusted value. Grocery is worth a side test, not a resignation.
- **Q10 Smallest test:** the concierge niche marketplace plus a v3 pitch, run together within 90 days for under ~A$40k.

## Questions I'd hand to other specialists
- **Regulatory:** Does the FWC order bind a startup platform from its first courier, or only above a size or "employee-like" threshold? How do liquor and pharmacy items in mixed baskets change licensing?
- **CV/tech:** What is realistic quantity-on-hand accuracy (not identification) from weekly phone scans, for fresh and variable-weight items?
- **Merchant research:** What are actual independent grocer net margins and online mark-ups on Uber/DoorDash in AU? Will 10–12% be accepted with price parity?
- **GTM:** What do Uber Eats AU, DoorDash AU and Metcash actually pay to onboard a non-POS merchant today? Is there a budget line for v3?
- **Finance:** Compare the expected value of v3 (acqui-hire, A$5–30M) with staying employed and with the round-3 hybrid.
