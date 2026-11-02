# Last-Mile & Fulfilment Operations Lead: red-team report

*2 Nov 2026. Lens: the physical flow from shelf to doorstep. All money in AUD (USD at ~0.65). The model is in the scratchpad, and its assumptions are stated inline.*

## Verdict
**The idea survives only if it is not on-demand and not multi-pickup by courier.** The brief's core mechanic is one basket drawn from several merchants and collected by one courier. Each extra merchant stop adds about 10 minutes of paid engaged time (~$6) plus ~$2 of merchant handling, and each stop is another chance of a stock-out or mis-pick. A three-merchant on-demand basket of $90 loses ~$7 per order before CAC and ~$13 after it, which is Milkrun's reported −$10 to −$13 again. The arbitrage holds for **merchant shelves (inventory already held) and off-peak staff time**. It breaks at **Saturday-morning and 4–7pm peaks**, where the platform's demand meets the merchant's walk-in peak. The biggest single issue is that **aggregation is a cost, not a feature, unless consolidation happens before the courier arrives**: specialists drop stock at an anchor grocer on a scheduled milk run, and the courier collects from one place.

## Verdict on the business model
- **Full on-demand marketplace with multi-merchant courier pickup: fatal.** The economics are structurally negative below ~$130 baskets even with one merchant, and multi-stop makes them worse (table below). It is the Milkrun/Voly/Getir pattern with less control over picking.
- **Scheduled, anchor-merchant consolidation in one dense precinct: survives-if.** Baskets must average ≥$100, the precinct must reach ≥60 orders/day within ~6 months, and line fill must be ≥95%. Picking is done off-peak against an 11am cutoff for 4–8pm windows. This is the only physical model I'd launch.
- **Software only (shelf-scan inventory plus catalogue feeding Uber Eats/DoorDash/IGA Online): ops-light and probably the better business.** It sidesteps every problem in this report because DoorDash/Uber already own courier density and absorb the FWC floor. Ops evidence that it is needed: independents on these apps have poor stock accuracy, and that drives refunds and cancellations, which hurts the platforms.

## Attacks on the thesis

**1. Multi-stop pickup kills contribution (High).** Inner-Melbourne courier time per order **[estimate: 5 min positioning + 5 min dwell per merchant (parking on Sydney Rd/Smith St, walk-in, check, cold-bag) + 5 min between merchants + 8 min to customer + 4 min drop, apartments included]**:

| Merchants per basket | Engaged minutes | Courier cost at $32/h engaged + 15% leakage | Contribution at $90 basket, pre-CAC | After CAC ($57 / 10 orders) |
|---|---|---|---|---|
| 1 | 22 | $13.50 | +$6.10 | +$0.40 |
| 2 | 32 | $19.60 | −$0.50 | −$6.20 |
| 3 | 42 | $25.80 | −$7.20 | −$12.90 |

Revenue assumed: 15% merchant take + $9.99 delivery + 5% service fee = $28 on a $90 basket. Other costs: payments 1.7%, refunds/credits 3% of GMV + $1 handling, packaging $1 + $0.50 per merchant, support $1.50 **[estimates]**. At a $130 basket, three merchants still lose $1 pre-CAC. **The marginal merchant must bring ≥$40–50 of extra basket to pay for its own stop.** A butcher's $25 add-on doesn't.

**2. The FWC minimum standards order sets a hard floor for courier pay, and it rises on 1 Jan 2027 (High, time-sensitive).** Since **17 Aug 2026**, employee-like workers delivering food, beverages or **supermarket groceries** via platforms get a floor of **$31.30/h (no vehicle/bike) to ~$32.00/h (car) of engaged time** **[verified: FWC/FWO via SmartCompany, Inside Retail, The Daily Aus, Aug 2026]**. Engaged time runs from acceptance to completion, so **waiting at merchant counters is paid**. Multi-pickup dwell is exactly the time the order makes expensive. Platforms must also fund personal accident insurance. The order is interim, under review, and indexed to the national minimum wage from 1 Jan 2027. The gig "cheap courier minute" that Milkrun-era models assumed has gone.

**3. Fulfilio's idle capacity doesn't carry over cleanly (High).** Spare warehouse space is a static asset priced by the month. Merchant labour is capacity that varies by hour, and grocery demand peaks when stores peak. An independent grocer picks at **~45–60 s per line** without pick-path tooling (Instacart's ~100 s per item "good speed" rule of thumb includes shopper walking in unfamiliar stores) **[unverified: third-party rule of thumb; Instacart reports a ~1 min per-order gain from pick-to-light]**. Plus ~3 min of order handling per merchant. Merchant P&L at a **loaded casual retail wage of ~$38/h** **[estimate: General Retail Award L1 ~$27/h from 1 Jul 2026 + 25% casual loading + super/on-costs]**:

| Merchant (share of $90 basket) | Gross margin | Take 15% | Picking labour | Net to merchant |
|---|---|---|---|---|
| Grocer, $60, 18 lines | 26% → $15.60 | $9.00 | $11.40 | **−$4.80** (or +$6.60 if labour is truly idle) |
| Butcher, $25, 3 lines | 35% → $8.75 | $3.75 | $3.50 | +$1.50 |
| Deli, $20, 4 lines | 40% → $8.00 | $3.00 | $4.00 | +$1.00 |

**For the grocer, the deal is only positive in idle hours.** That makes scheduled, cutoff-based picking a requirement, not an optimisation. Specialists make ~$1–2 per order, which is too small to justify cold-bagging and staging at 5pm on a Friday. Expect them to deprioritise platform orders at peak, which shows up as courier wait time (paid) and late deliveries.

**4. Inventory accuracy is the operational time bomb (High).** Even POS-tracked inventory is wrong often: **65% of ~370,000 store records at one US retailer were inaccurate** **[verified: DeHoratius & Raman, Management Science 2008]**. Shelf scans see facings, not back-stock. They also can't capture weight-priced meat, bakery runs that sell out by 2pm, or price changes since the last scan. My working assumption for shelf-scan data is **5–12% of ordered lines unavailable** at pick time **[estimate]**. In a 25-line, 3-merchant basket at 8%, two lines are short per order on average. In the UK, 20% of shoppers had a substitution in their latest online order **[verified: Which? survey]**, and 30–45% are dissatisfied with the substitute **[verified: J. Retailing study via Mecalux]**. Every short line costs take-rate revenue, a refund transaction, CS contact, and churn. Multi-merchant makes it worse: the probability that a basket is perfect is the product of each merchant's fill rate.

**5. Cold chain across multiple pickups (Med–High).** Under the FSANZ 2-hour/4-hour rule, potentially hazardous food above 5°C is fine under 2 h cumulative, must be used under 4 h, and discarded beyond that **[verified: FSANZ Appendix 2 / NSW Food Authority guidance]**. The time is cumulative from the merchant's fridge. A 42-minute 3-stop run with meat collected first and a failed first attempt can push chilled items toward the limit with no temperature record. That needs insulated bags per merchant, chilled-last pickup sequencing, ice packs, and **no frozen at launch**. If anything goes wrong, the platform is the food business on the hook.

**6. Failed and attended deliveries (Med).** Chilled baskets can't be left in an inner-city lobby in January. Expect 1–3% failed deliveries **[estimate]**, each costing the full basket (perishables can't be restocked) plus the courier leg. Bottle-shop items need ID at the door, so a failure means a return trip to the merchant (paid engaged time).

**7. Incumbents own the fast lane (High).** Woolworths' **On Demand is ~40% of its eCom orders**, and it now delivers via **DoorDash (Dec 2025) and Uber**. Coles sides with Uber Eats **[verified: Inside FMCG Dec 2025]**. Woolworths Group eCom was **$10.6bn in FY26, +15.9%**, with AU Food penetration **>17% in Q4 FY26** **[verified: WOW FY26 results/broker note via Motley Fool]**. Woolworths' Delivery Now costs ~$10–15 **[verified: CHOICE 2025]**. A new entrant paying $25 of courier cost per 3-stop basket can't match that price with a $9.99 fee. IGA has delivered via DoorDash since 2021 (~800 stores online targeted by 2025) **[verified: Inside Retail / Internet Retailing]**.

## Things the brief gets wrong, misses or understates
- **"Aggregates pickups into one delivery" treats consolidation as free.** It is the main cost line, and where it happens (courier van, hub or anchor store) decides the P&L.
- **The Fulfilio analogy:** right on shelves (merchant holds inventory and working capital, which dark stores must fund), wrong on labour (peak-coincident, untrained, unaccountable to your SLA).
- **Brief omits the FWC order (in force since 17 Aug 2026)** and its 1 Jan 2027 increase. Any 2022-era quick-commerce benchmarks understate courier cost.
- **Merchant picking quality is unmanaged.** Instacart controls the picker. Here the merchant's teenager on a Saturday shift picks your order. Mis-picks (wrong size, wrong brand, cracked eggs, wrong meat weight) land on the platform's NPS and refund line.
- **Weight-priced goods** (meat, deli, fruit) need pre-authorisation above the estimate (+10–15%) and a re-price at pick, which the brief's flat "clip of the basket" doesn't handle.
- **Uber Eats already bundles a second nearby store into one cart** (US, Oct 2023) **[verified: TechCrunch]**. AU availability is **[unverified]**. Either way, the incumbent can switch multi-merchant on whenever it shows demand.
- **"Global from day 1" is incompatible with last-mile physics.** Density is per precinct. Route density, merchant clusters and courier pools don't transfer between cities, let alone countries. Only the software layer (scan, catalogue) can be global.

## Numbers checked
| Claim / input | Finding | Status / source |
|---|---|---|
| Courier minimum pay | $31.30/h (bike/no vehicle) to ~$32.00/h car, engaged time, from 17 Aug 2026; rises 1 Jan 2027 | [verified: FWC/FWO via SmartCompany, Inside Retail, The Daily Aus] |
| Uber Direct pricing | Fixed + distance per delivery; $0.50/min wait fee after 10 min; activation fees per location | [verified: Uber AU merchant pages, via search summary] |
| Uber Direct per metro drop | ~$8–12 | [unverified: Oddle blog; reseller "from $6.99"] |
| Zoom2u Melbourne same-day | From $25; 3-hour from $39 incl. GST | [verified: Zoom2u site; vendor "from" price] |
| Milkrun per-order loss | ~−$13 mid-2022, ~−$10 later; CAC ~$57 | [verified: press reports of leaked deck, via search summaries] |
| Voly | FY22 net loss $13.6m; creditors paid 15–27c/$ | [verified: administrator reports via press] |
| Woolworths On Demand share | ~40% of eCom orders | [verified: Inside FMCG Dec 2025] |
| Woolworths eCom FY26 | $10.6bn, +15.9%; AU Food >17% penetration Q4 | [verified: WOW FY26 via Motley Fool/broker] |
| Getir / Gorillas | Exited UK, DE, NL, US in Apr 2024 (7% of revenue) | [verified: TechRadar, The Grocer] |
| Gopuff | Valuation US$15bn (2021) → US$8.5bn Nov 2025 (~A$13bn); still not profitable | [verified: Bloomberg via search; profitability timing unverified] |
| Deliveroo | Exited AU 2022 ($33m loss cited); DoorDash owns Deliveroo since Oct 2025 | [verified: press / Wikipedia] |
| Inventory record inaccuracy | 65% of records wrong at one US retailer | [verified: DeHoratius & Raman 2008] |
| Pick speed | ~100 s/item "good" for Instacart shoppers | [unverified: Ridester] |
| Average AU online basket (all retail) | $96 in 2025 | [verified: Australia Post via search; not grocery-specific] |
| Restaurant commission on Uber Eats/DoorDash AU | ~30% | [unverified for grocery; grocery likely lower] |

## Improvements (ranked by impact)
1. **Anchor-store consolidation, not courier multi-pickup.** One independent grocer or IGA per precinct acts as the hub. Specialists (butcher, baker, deli) pre-pick orders by an 11am/3pm cutoff, and a shared milk-run collects them twice daily (~$60/run). At 40 orders/day that is ~$3 per order. At 100 orders/day it is ~$1.20. The courier then makes one pickup. Contribution at a $90 basket becomes about **+$6.60 pre-CAC**: $28 revenue − $10 delivery (batched 2–3 drops per trip) − $3 inbound − $1.70 payments − $3.70 refunds − $1.50 packaging − $1.50 support **[estimate]**. The anchor's back room and cool room are the real Fulfilio arbitrage. Pay the anchor a hub fee (~$1.50/order) on top of its sales.
2. **Scheduled windows only at launch** (same-day 4–8pm, next-morning). This moves picking into merchant idle hours (10am–3pm weekdays) and lets one courier run 2–3 drops per trip. Add on-demand later only for single-merchant baskets ≥$60.
3. **Curate the catalogue to "reliable SKUs".** At launch, list only items with ≥98% observed fill over 2 weeks. Show weight-priced items with a pre-auth range. Show specialty fresh items only if the merchant confirmed them that morning. This reverses the "scan everything" framing: accuracy beats breadth.
4. **Courier sourcing: two employed drivers in small refrigerated or insulated vans for scheduled routes**, with Uber Direct/Zoom2u as overflow. At ~$72/h loaded van and driver **[estimate]**, 5 drops/h = ~$14.40 per drop and 7 drops/h = ~$10.30. Employment avoids the employee-like-worker classification fight and gives control over cold chain, ID checks and service. Avoid building a contractor pool: it now carries the FWC floor without the control.
5. **Picker app with barcode confirmation and photo of the bagged order** per merchant, a per-merchant scorecard (fill rate, pick time, mis-picks), and delisting below 95% fill.
6. **Minimum basket of $60 and a $9.99 fee**, with fees waived above $150. Basket size is the strongest lever in every scenario I ran.
7. **Cold chain SOP:** chilled packed last at each merchant, insulated tote and ice pack, temperature logger in each van, no frozen in phase 1, attended delivery or customer-supplied esky for chilled.

## Tests & kill criteria (90 days, one precinct, e.g. Brunswick/Sydney Rd or Fitzroy/Smith St)
| Test | Metric | Pass | Kill | When |
|---|---|---|---|---|
| Concierge pilot: 1 anchor + 4 specialists, founder plus 1 ops hire, 1 van | Orders/day | ≥40 by week 10 | <20 by week 8 | Wk 1–10 |
| Basket | AOV | ≥$100 | <$75 | Wk 4 on |
| Inventory from shelf scans | Line fill without customer contact | ≥95% | <90% after curation | Wk 2 on |
| Merchant picking | Seconds per line; % picks in merchant-declared quiet hours | ≤50 s; ≥70% | >80 s or anchor refuses peak picks | Wk 3 |
| Delivery cost | $ per order delivered (all-in, incl. inbound) | ≤$14 | >$20 at 40 orders/day | Wk 8 |
| Multi-merchant value | % baskets with ≥2 merchants; incremental AOV vs single | ≥35%; +$35 | <15% or <+$20 | Wk 8 |
| Retention | 30-day repeat | ≥40% | <25% | Wk 12 |
| Merchant economics | Merchants still active and accepting ≥12% take | 5/5 | Anchor quits | Wk 12 |
| Cold chain/quality | Complaints per 100 orders; failed deliveries | ≤3; ≤2% | >6; >4% | ongoing |

Run a parallel **software-only test** that costs nothing physical: offer shelf-scan stock sync to 10 independents already on Uber Eats/DoorDash and measure the cancellation/refund-rate drop over 6 weeks.

## Answers to the brief's questions in my domain
- **Q1 Unit economics/density.** On-demand multi-pickup is negative at any realistic basket. Anchor-consolidated, scheduled delivery is positive pre-CAC at a $90+ basket from ~40 orders/day per precinct. It covers CAC and a share of overhead at ~$110+ baskets, 6–7 drops/h and ≥100 orders/day. A precinct is roughly a 2–3 km radius with one anchor. Melbourne would need ~10–15 precincts to reach ~$50m GMV/yr **[estimate: 100 orders/day × $110 × 360 ≈ $4m GMV per precinct]**.
- **Q2 Merchant picking/accuracy.** Specialists will pick small add-ons off-peak but earn only ~$1–2 per order. Grocers lose money picking at peak with paid labour. Accuracy has to be enforced by curation and barcode confirmation, not assumed from scans.
- **Q3 Which baskets.** Planned weekly top-up plus specialty (good meat, bread, deli) for affluent inner-city households, scheduled for the evening. Not urgent baskets, where Woolworths/DoorDash win.
- **Q5 Precedents.** Milkrun (−$10 to −13/order; brand bought by Woolworths 2023), Voly (15–27c/$), Getir/Gorillas exits (2024), Gopuff valuation reset, Deliveroo AU exit (2022). Instacart is the counter-example: it works on dense US baskets (~US$100+), batching, and ad revenue **[unverified figures]**, with picking it controls.
- **Q6 Global.** Ops is city-by-city and precinct-by-precinct. Only the software is global.
- **Q7 Regulatory (ops angle).** FWC on-demand delivery order (interim, rising 1 Jan 2027), FSANZ temperature control, liquor delivery ID checks, food-business registration of any hub.

## Questions I'd hand to other specialists
- **Unit economics/CFO:** Rerun with my anchor-model inputs. What CAC and repeat rate make a precinct pay back in <12 months?
- **Legal:** Does the FWC order cover scheduled grocery delivery by contractors, and does employing drivers trigger the Road Transport/Storage awards? What are Victorian liquor-delivery requirements?
- **Merchant/supply:** Will an IGA/independent accept being a hub for competitors' specialty products, and at what fee?
- **Tech/CV:** Can shelf scans estimate stock depth and weight-priced items, or only presence? What re-scan frequency gets ≥95% fill?
- **Consumer:** How big is the inner-Melbourne segment that pays $10 for a scheduled multi-shop basket instead of Woolworths plus a walk to the butcher?
- **Competition:** Is Uber Eats multi-store cart live in AU, and what would make DoorDash switch on grocery multi-merchant?
