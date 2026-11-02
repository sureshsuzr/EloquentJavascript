# Marketplace Unit-Economics Modeller (CFO): red-team report

Model: `red-team/grocery/models/order_economics.py` (output: `order_economics_output.txt`). All figures in AUD. FX assumption 1 USD = 1.52 AUD [estimate]. Several primary sources (fairwork.gov.au, IBISWorld paywall, Uber Direct AU rate card) could not be opened from this session; those figures rest on search summaries and are labelled.

## Verdict

**As described (on-demand, multi-merchant baskets, revenue = a basket clip), it is fatal.** Contribution is negative at every take rate from 5% to 20% and at every order density, before any fixed cost: about -$6 per single-merchant order and -$9 to -$13 per two- or three-merchant order at a 15% take. More density only narrows the loss (to about -$1.60 at 32 orders/km²/day). **The biggest problem is that each extra pickup stop adds about $7.50 of courier cost**, and the Fair Work minimum standards that started on 17 Aug 2026 lock that cost in, while the merchant has no margin left to fund it. It **survives only if** it becomes scheduled, routed delivery of large baskets (≥$120) from one or two merchants, or a consolidation-hub model. In that form it is a regional grocery-delivery operator that needs about 1,200–1,700 orders a day in one 120 km² zone to cover HQ plus a $500k founder draw. It is not a global software marketplace.

## Verdict on the business model

- **Full on-demand marketplace with multi-stop aggregation: not a business.** The aggregation feature is the part that loses the most money. In my model a 3-merchant $110 basket loses about twice as much per order as a 1-merchant $55 basket.
- **Scheduled multi-merchant delivery (2-hour windows, routed vans, merchants stage orders ahead): it could be a business.** Scenario D makes about +$12.70 an order (10.6% of GMV). That is roughly Instacart-level EBITDA per order (about $4.80) plus margin to cover city overhead. But it is a logistics business with a city-by-city J-curve.
- **Hub consolidation (merchants drop picked bags at a micro-hub; one courier leg to the customer): the best contribution (+$18 before the cost of merchants' drops)**, and it is the Fulfilio-style physical arbitrage the founder actually knows. It still needs density, a lease and merchants willing to drop off.
- **Software only (shelf-scan inventory and a universal catalogue, sold to merchants or to Uber Eats, DoorDash or Instacart AU feeds): the only version without courier economics.** From my lens it is the lowest-risk way to monetise the hardest asset (catalogue and inventory truth) and to test demand. Its revenue ceiling is another specialist's question.

## Attacks on the thesis

1. **The take rate cannot fund delivery (High).** A 15% clip on an $85 basket is $11.70. Courier cost for that 2-stop order is about $24 (40 engaged minutes × ~$36/hr loaded). Even with a $7.99 delivery fee and a 4% service fee, revenue is $22.85 against about $32 of variable cost. Instacart closes this gap with retailer markups, consumer fees, membership and **ads at about 2.9% of GTV, which is 28% of its revenue** [verified: Instacart FY25 results via search summaries]. Its adj. EBITDA is still only 2.9% of GTV [verified]. DoorDash's contribution is 5.1% of GOV [verified: Q3 2025 release summary]. **The incumbents' entire margin is smaller than the extra-stop cost in this design.**

2. **Multi-stop aggregation is the cost engine, not the moat (High).** Each extra merchant adds about 4 min waiting, 8 min travelling between stops, a picking handover and a 3% error risk. That is **about $7.50 an order at MSO rates**, and it shrinks with density only through batching. Customers do not pay 9% more for a basket split three ways. Uber Direct and DoorDash Drive are priced per point-to-point job [verified: Uber AU merchant page, fixed plus distance fee, $0.50/min wait after 10 min]. So outsourcing a 3-merchant basket means three drops, about $33 [estimate at about $11 a job; AU rate card not public].

3. **Merchant economics break at the take rates the platform needs (High).** An independent grocer with 25–30% gross margin [verified only anecdotally: an IGA broker listing showing GP rising 25.1% to 30.6%; the IBISWorld margin is paywalled] that picks a $39 share of a basket keeps **+$1.62 at a 5% take, -$0.34 at 10%, and -$2.29 at 15%** after about 7 minutes of picking labour at $42/hr loaded. Specialty merchants (40% GM) tolerate 10–15%. Merchants will accept the fee only if staff time is truly idle, but platform demand peaks (Saturday morning, 5–7pm) coincide with in-store peaks. **The Fulfilio analogy fails here: spare warehouse space was idle, but merchants' labour at peak is not.**

4. **Platform-paid picking (the Instacart model) is fatal (High).** Paying pickers adds $9–20 an order and takes contribution to -$15 to -$34. "Who picks, and at whose cost" is the most sensitive single choice in the model, swinging contribution by $12.56 an order.

5. **Courier cost is now regulated upward (High, time-sensitive).** The FWC Interim On-Demand Delivery Employee-like Worker Minimum Standards Order has been in force since **17 Aug 2026**. It sets about $31.30/hr (bike) to $32–32.50/hr (car) of engaged time and **expressly covers groceries delivered "as soon as possible"** [verified: Fair Work releases, SmartCompany, Workpro, HCA via search; order text not opened]. It is interim and may be varied, and further last-mile orders are being considered. Scheduled-window delivery may fall outside the "as soon as possible" limb. Lawyers should confirm, but this is a structural reason to prefer scheduled delivery.

6. **Density helps far less than founders assume (Med-High).** Going from 1 to 32 orders/km²/day lifts blended contribution from -$7.70 to -$1.60, through shorter first legs and batching. That is not enough to cross zero. Density is necessary but not sufficient; basket size and stops per order matter more.

7. **CAC cannot be recovered (High in the base case).** With negative contribution, LTV is negative whatever the retention. Even in scenario C (+$8.54 an order), a customer placing 14 orders in year 1 with 45% retention is worth about $170 of 3-year contribution after a $25 welcome credit. That supports a CAC of about $55 at 3× LTV/CAC [estimate], which is tight against AU delivery-app acquisition costs [unverified].

8. **Shelf-scan inventory adds an out-of-stock tax (Med).** Each 1-point change in the item OOS rate moves contribution by about $0.25 an order, and errors compound across merchants. With 3 merchants at 3% error per stop, about 9% of orders carry a complaint. The OOS sensitivity, a $2.80 swing between 4% and 15% OOS, is smaller than the courier and fee levers, but it drives retention, which this per-order model does not capture.

## Things the brief gets wrong, misses or understates

- **"Takes a clip of the basket" as the revenue model** misses that every surviving player earns most of its margin from consumer fees, item markups and ads, not merchant commission. Retail media (sponsored products in the universal catalogue) is the missing revenue line. At Instacart scale it is about 3% of GTV, but it needs large brand advertisers, not independent grocers.
- **"Under-utilised physical capacity"**: shelves and stock are under-utilised; staff at peak are not. The arbitrage is real for *inventory*, not for *picking labour*.
- **"Global from day 1"**: per-order economics are set by local courier wages, local regulation (the AU MSO), and density in each 100–150 km² zone. Each city needs about $2.2M a year of fixed cost [estimate] and its own density. Only the software layer can be global.
- **History is understated.** Milkrun lost about $10–13 an order and shut in April 2023 after about $86M; Woolworths bought the brand for a reported ~$10M [verified: Startup Daily, Forbes AU, Wikipedia]. Voly closed in Nov 2022 after an $18M seed round [verified: SmartCompany]. Getir's UK business lost £168M in 2022, and Getir exited UK/DE/NL in April 2024 [verified: UKTN, Retail Tech Innovation Hub]. Gopuff claimed about US$4 an order of contribution while still cutting jobs and raising fees [verified: City AM, Retail Dive summaries]. Those businesses had *one* pick location per order, so this design starts from a worse cost structure.
- **Incumbent online penetration is high and growing.** Woolworths' e-commerce penetration reached 15.1% in FY25 [verified: Woolworths FY25 coverage], and Woolworths owns the Milkrun brand. The commodity basket is taken; the gap is specialty or ethnic baskets the majors do not stock.

## Numbers checked

| Claim / input | Finding | Status / source |
|---|---|---|
| Instacart economics | FY25 GTV US$37.22B, 338.8M orders, AOV about US$110 (A$167); transaction revenue about 7.3% of GTV, ads about 2.9%; adj. EBITDA US$1.09B = 2.9% GTV (about A$4.84 an order) | [verified: Instacart FY25/Q3 25 releases via search summaries] |
| DoorDash | Contribution 5.1% of GOV; net revenue margin 13.3–13.8% (Q3 25) | [verified: DoorDash Q3 25 release summary] |
| Milkrun | -$10 to -$13 an order; closed 14 Apr 2023; brand sold for a reported ~$10M | [verified: Startup Daily/Forbes AU] |
| Courier cost | MSO $31.30–32.50/hr engaged time from 17 Aug 2026; covers grocery "as soon as possible"; model uses $35.84 loaded | [verified: FWO/FWC via summaries]; load [estimate] |
| Payments | Stripe AU domestic cards 1.65% + $0.30 from 1 Oct 2026 (was 1.7% + $0.30) | [verified: Stripe support/Wise via summary] |
| Independent grocer GM | 25–31% (broker listings); used 28% | [unverified as an industry average; anecdotal] |
| Uber Direct AU | Fixed plus distance fee; $0.50/min wait after 10 min; $350 per extra location; no published per-drop rate | [verified: merchants.ubereats.com/au]; $11/job [estimate] |
| Delivery-app markup | CHOICE found app grocery prices about 11% above in-store (Oct 2025) | [verified: Medianet release] |
| Woolworths online | 15.1% penetration FY25 | [verified: FY25 coverage] |
| Basket sizes | $55 / $85 / $110 for 1/2/3 merchants | [estimate: specialty top-up baskets, well below the about A$167 Instacart AOV] |
| Engaged minutes | 28 / 40 / 52 for 1/2/3 stops (unbatched) | [estimate: urban 20–22 km/h, 4 min wait, 8 min between stops] |
| Picking | 60 items/hr plus 4 min a stop at $42/hr | [estimate: casual retail award plus on-costs] |

## Model outputs (15% take, merchant picks, own MSO couriers)

| | 1 merchant ($55) | 2 merchants ($85) | 3 merchants ($110) |
|---|---|---|---|
| Contribution at 5 / 10 / 15 / 20% take | -11.35 / -8.82 / -6.29 / -3.76 | -17.23 / -13.32 / -9.41 / -5.50 | -23.38 / -18.32 / -13.26 / -8.20 |
| Platform picks (15%) | -15.01 | -24.16 | -33.51 |
| Uber Direct-style point-to-point (15%) | -0.57 | -7.52 | -15.20 |
| Orders per engaged courier-hour (unbatched / 2-batched) | 2.1 / 3.4 | 1.5 / 2.4 | 1.15 / 1.85 |

**Density** (blended 50/35/15 mix, batching rising with density): -$9.63 at 0.5 orders/km²/day, -$3.63 at 8, -$1.63 at 32. **The break-even density does not exist.**

**Survival scenarios** (per order): (B) on-demand with 40% batching and orders staged ready: -$1.95. (C) single-merchant $130 full shop, 12% take, $9.99 fee: **+$8.54**. (D) scheduled 2-hour windows, routed, 2 merchants, $120, 12%: **+$12.71**. (E) hub consolidation: **+$18.18**, before merchants' drop cost of about $3–6.

**Break-even** over a 120 km² inner-Melbourne zone, with city fixed costs about $2.15M/yr and central tech/HQ about $3.5M/yr [estimates]:

| | City fixed only | City + central | + $500k draw, ×1.25 buffer |
|---|---|---|---|
| Scenario C | 690/day (5.7/km²) | 1,813/day (15.1/km²) | 2,467/day (20.6/km²) |
| Scenario D | 463/day (3.9/km²) | 1,218/day (10.1/km²) | 1,657/day (13.8/km²) |

**Sensitivity** (tornado at 8 orders/km²/day; base -$3.63): who picks ($12.56 swing) > basket size -25%/+40% ($7.05) > take rate 10/20% ($6.78) > delivery fee $4.99/$10.99 ($5.90) > merchant wait 8/2 min ($5.13) > courier rate ($4.63) > promo ($3.50) > OOS ($2.80) > time between stops ($2.36).

**Most sensitive input:** among continuous inputs, **courier minutes per order** (stops × (wait + time between stops)) taken together with **basket size**, because they set cost per dollar of GMV. Structurally, **who bears picking labour**.

## What has to be true

- **$500k founder draw:** scenario D or E economics, **about 1,650 orders a day (about 600k a year, about A$72M GMV) in one zone**, plus about $10–20M of funding to get through 2–3 years of ramp at -$5M to -$7M a year [estimate]. A venture-backed board will not approve a $500k draw before profitability; expect $200–250k.
- **Venture outcome:** at 2× net revenue (low-margin delivery multiple), an A$300M exit needs about A$150M of net revenue, **about A$0.6B GMV and about 22,500 orders a day**, which is 13 times the per-zone break-even, so 10 or more dense zones. That is Milkrun-scale ambition, with a worse cost structure and no ad network.

## Improvements (ranked by impact)

1. **Drop on-demand delivery and sell scheduled windows** (same-day evening, next-morning). Routed vans make about $12.70 instead of -$9.40 an order and may sit outside the MSO's "as soon as possible" coverage (legal to confirm).
2. **Cap stops at 2 and price extra stops explicitly** ($3–4 per additional merchant), or **consolidate at a micro-hub** that merchants drop to on a schedule: the Fulfilio play.
3. **Set a minimum basket (about $80) or a small-order fee.** Basket size is the second-largest lever.
4. **Take rate of about 8–10% from merchants plus a 5% consumer service fee, and price-parity markups of up to 10%** (in line with the CHOICE-reported 11% app markup). Don't ask grocers for 15–20%.
5. **Make merchants pick from their own staged order queue, paid by a lower fee**, never platform pickers.
6. **Build retail media from day one** on the universal catalogue (sponsored placement for brands and distributors that sell to independents).
7. **Software-first wedge:** license shelf-scan inventory and catalogue feeds to independents for listing on Uber Eats, DoorDash and their own sites. This gives revenue without couriers and real data on inventory accuracy and merchant demand.

## Tests & kill criteria

| Test (≤90 days) | Metric | Kill threshold |
|---|---|---|
| Concierge scheduled delivery in one suburb cluster (5–8 merchants, founder or contract van, Shopify-style storefront) | Average basket; stops per order | Basket <$80 or more than 1.6 stops per order after 6 weeks |
| Time-and-motion on 100 real orders | Engaged courier minutes per order; merchant wait | >30 min per order scheduled, or >5 min wait per stop |
| Merchant fee test (offer 8/12/15%) | Sign-up and 60-day retention; picking time logged | Fewer than 40% of approached grocers sign at ≥10%, or more than 30% churn by day 60 |
| Inventory accuracy audit of shelf-scan versus physical count | Item OOS or mismatch at pick | >8% item OOS after 4 weeks of weekly scans |
| Paid acquisition, $10k | CAC to first order; 60-day repeat | CAC >$60 or fewer than 35% placing a second order within 30 days |
| Uber Direct and DoorDash Drive quotes for a 3-stop route in Melbourne | Cost per job, batching terms | If >$9 a drop and no multi-pickup, the outsourced courier option is dead |

## Answers to the brief's questions in my domain

**Q1 (per-order economics and density):** No, not as designed. Contribution is negative at every take rate and density, at -$6 to -$13 an order. It turns positive only with scheduled, routed delivery, baskets of $120 or more, at most 2 stops, and a 12% take plus about $10 of consumer fees (+$8.50 to +$12.70 an order). Break-even then needs about 4–6 orders/km²/day for city fixed costs and about 10–15 for city plus HQ.

**Q6:** It is a city-by-city density business. Courier wages, regulation and fixed costs are local.

**Q8 (from a P&L lens):** Software and catalogue first. Scheduled hub-consolidated delivery is the only version of the marketplace that pencils out.

**Q10:** The 90-day concierge scheduled-delivery test above. The kill metrics are basket size, stops per order and engaged minutes per order.

## Questions I'd hand to other specialists

- Legal: does scheduled-window grocery delivery fall outside the MSO's "as soon as possible" coverage? What exposure would we have under pending last-mile orders?
- Merchant research: what is the true idle picking capacity by hour at independent grocers? Will they stage orders by a cutoff?
- Tech: what item-level OOS accuracy does shelf-scan achieve with weekly scans versus daily scans?
- Consumer: what share of AU households would pay about $10 for a scheduled specialty or ethnic basket of $120 or more?
- Competitors: Uber Direct and DoorDash Drive AU multi-pickup terms; Woolworths MILKRUN's current coverage.
