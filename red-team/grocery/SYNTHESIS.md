# Grocery aggregation: red-team synthesis

11 independent agents, 3 Nov 2026. Reports in `reports/`. Models: `models/order_economics.py` (output in `order_economics_output.txt`) and `models/last_mile_scenarios.py`. Several sources (Fair Work, ACCC, SmartCompany, Uber/DoorDash merchant pages) were blocked from the session and rest on search summaries.

## Bottom line

**The marketplace as described (merchants as dark stores, multi-merchant on-demand baskets, take rate, global from day 1) doesn't work. All 11 agents independently reached the same conclusion.** It loses money on every order at every take rate; the same model already failed in Melbourne; and the incumbents already have the feature, the couriers and the independents.

**One thing survives: the supply-side data layer.** A matched catalogue plus live availability for the long tail (no-barcode, ethnic/imported, deli/butcher/fresh), sold to companies that already own demand and couriers. It's a smaller, data-led business with a possible strategic exit. It ranks **below the rent-roll pricing-engine hybrid** and is the fallback if that path's tests fail.

## Why the marketplace fails

1. **Per-order economics are negative at any density** (01, 05, 07).
   - On-demand at a 15% take: −$6 (1 merchant, $55 basket), −$9 (2 merchants), −$13 (3 merchants).
   - Negative at every take rate from 5% to 20%; still −$1.60 per order at 32 orders/km²/day, before fixed costs (01).
   - Each extra pickup adds ~$6–7.50 of courier time (05, 01) plus ~$2 of merchant handling (05). A three-merchant basket runs ~$26–32 in courier pay alone (08).
   - For comparison, Instacart's whole profit is ~2.9% of sales (~$4.80 per order), so one extra stop exceeds it (01).
2. **Courier labour now has a legal floor.** Since 17 Aug 2026 the FWC interim order sets ~$31.30/hr per *engaged* hour (accept → deliver) for app-based supermarket grocery delivery. Waiting at merchant counters is paid time, which is exactly what multi-pickup creates (01, 05, 07, 08). Uber Direct and DoorDash Drive price per pickup-to-door job, so a 3-merchant basket is 3 deliveries (01).
3. **Merchants can't afford the take rate** (01, 02).
   - **Independent grocer (~25–28% margin), doing its own picking:** +$1.62 per order at a 5% take, −$0.34 at 10%, −$2.29 at 15% (01). ~$0 per order at 15% (02).
   - **Bakeries and delis (higher margin):** tolerate 10–15%.
   - **Merchant expectations:** ~8–12%, from Instacart and DoorDash precedent (02).
   - **Merchant response:** they raise online prices. CHOICE found delivery-app baskets cost 31–39% more than in-store (03).
4. **The Fulfilio analogy breaks** (01, 02, 05, 11). Fulfilio's warehouse space was genuinely idle and interchangeable. Merchants' shelves are under-used, but their staff are busiest (Saturday mornings, 4–7pm) exactly when delivery demand peaks. Picking with paid casual labour loses ~$4.80 per order at a 15% take (05).
5. **Inventory accuracy compounds against you** (02, 04, 05, 07, 09).
   - A shelf scan is a snapshot: no back-room stock, stale within hours on fast lines, and an industry estimate of up to 60–65% of store inventory records being wrong.
   - At 95% per-line accuracy, a 25-line order is fully right ~28% of the time (04). A four-store basket at 95% per store arrives complete ~81% of the time (02).
   - Across merchants a miss becomes a refund, not a substitution.
6. **The same model already failed in Melbourne.** **YourGrocer** (2013–22) delivered multi-shop baskets from ~150 independents and markets. It reached $9.2M sales in FY22 with a $158 average order, lost ~$680k, failed to crowdfund and sold its assets for ~$3k (03, 09). The ceiling was ~1,100 orders a week across the city; beating $500k needs ~$150–300M a year of sales, 20–40x YourGrocer's peak (03).
7. **The incumbents already have it** (03, 06, 07, 10).
   - **Multi-store baskets:** DoorDash **DoubleDash** adds a second store with no extra fee; Uber Eats has done two-store orders since Oct 2023; Deliveroo (DoorDash-owned since Oct 2025) has trialled 3-store "Bundles" since May 2026 (06).
   - **Two platforms, each tied to a major:** Coles is exclusive to Uber Eats (26 Dec 2025); Woolworths is on DoorDash (150+ more stores Jul 2026) and runs Milkrun (48% of its delivery orders within 2 hours); Aldi delivers via DoorDash; Menulog shut (26 Nov 2025); Amazon fresh grocery is live in Sydney via Harris Farm; 100+ IGAs have been on DoorDash since 2021.
   - The brief's competitor premises are out of date.
8. **The graveyard** (06, 07, 11): Milkrun (~A$86M raised, ≥$10 lost per delivery, brand sold to Woolworths for ~A$10M), Voly, Send, Deliveroo AU, Getir's 2024 retreat to Turkey. Mercato in the US ended up supplying its catalogue to DoorDash and Grubhub (02), with reports of members owed money (06, unverified). Capital is scarce: only 31 AU rounds under A$5M in Q2 2026; Zepto has fallen from US$7B to ~US$4.5B (11).
9. **"Global from day 1" is incompatible with a density business** (all agents). Delivery is won one 2–3 km² cluster at a time. EU platform-work employment presumption (from 2 Dec 2026), NYC grocery pay (~US$21.44/hr), and per-country food, liquor, tax and privacy rules (08). **Only software, catalogue and data can go global.**
10. **Shelf scanning is a commodity** (04, 07). Instacart bought Arpalus (16 Jul 2026; phone-video shelf recognition, >95% claimed); Trax/FORM, Focal, Simbe and Vori sell similar tools; frontier vision models get a small team most of the way.

## What survives, and in what form

| Version | Verdict | Sources |
|---|---|---|
| Full on-demand multi-merchant marketplace | **Kill** | all |
| Scanner software sold to merchants | **Kill as a company** (feature; ~A$1–4M ARR ceiling in AU) | 04, 07, 10 |
| Café/restaurant supply (B2B) | **Kill**: Ordermentum, Choco; retail prices sit above wholesale | 10 |
| Scheduled specialty niche via one anchor store per precinct | **Lifestyle-scale at best** | 01, 05, 07, 09 |
| **Long-tail catalogue + live availability data, sold to platforms and brands** | **The only venture-credible version** | 04, 06, 10, 11 |

**The scheduled niche, if anyone wants to run it.** One anchor grocer or IGA per precinct as hub; specialists pick by a cutoff; twice-daily consolidation; employed van drivers plus 3PL overflow; evening or next-morning windows.
- **Per order:** about +$6.60 on a $90 basket (05); +$12.70 with routed vans, $120+ baskets and ≤2 merchants (01).
- **Survival thresholds:** order ≥$110, item fill ≥96–97%, 4-week repeat ≥30–35%, ≤$12 per drop (07).
- **Scale for a $500k draw:** ~1,650 orders/day in one 120 km² zone and $10–20M of funding (01).
- **Verdict:** it doesn't beat staying employed.

**The data layer** (10 is the clearest; 04, 06 and 11 agree):
- **What it is:** a matched catalogue plus live availability for products the mainstream catalogues don't cover. GS1's National Product Catalogue covers mainstream packaged goods but restricts redistribution; Open Food Facts' ODbL licence risks forcing a derived catalogue open (04). Ethnic/imported, no-barcode, deli/butcher and fresh items are the gap.
- **Architecture:** POS-first. Square, Lightspeed and Shopify sales and price files are the record; scanning is used once, to onboard a store's catalogue, plus periodic partial correction; pickers' found/not-found feeds back. Prices must come from the POS (ACL). Weighed items are sold per kg (04).
- **Buyers:**
  1. DoorDash AU, the natural first partner and likely acquirer because it lost Coles and needs grocery supply; Uber Eats; HungryPanda; Metcash/IGA; Foodworks; Australia Post/Rendr (06, 10, 11). They pay for onboarding coverage and fewer cancellations.
  2. Importers and challenger FMCG brands, for distribution intelligence on the independent and ethnic channel (~A$20–80k/yr each). Independents are ~7% of supermarket sales, and big FMCG budgets follow Woolworths/Coles data and retail media (10).
- **Merchants are data suppliers** to be given free tools, not customers (10).
- **Moat:** a statistically designed store panel plus cross-merchant matching of no-barcode items. This suits the founder's statistics background (10).
- **Precedent:** **Pointy** got independents' inventory online and reportedly sold to Google for ~US$160M (unconfirmed): a data sale to a company that owns demand (10).
- **Exit range:** ~A$20–150M, a strategic sale to a platform (06).
- **Global:** licence the engine offshore where traditional trade dominates FMCG sales; the only version where "global from day 1" is credible (10).

## Paths compared (11; one model, rely on the ranking)

| Path | 7-yr expected value | Notes |
|---|---|---|
| Rent-roll hybrid (round 3) | ~A$3.0M | Floor ~A$1.5M |
| Grocery marketplace | ~A$3.2M | All from the long tail: median ~A$0.5M, ~13% chance of beating staying, certainty-equivalent ~A$1.5M |
| Grocery data/software layer | ~A$2.5M | |
| Stay employed | ~A$2.0M | |

**You can't run both while employed, so choose.** The rent-roll hybrid stays first; the grocery data layer is the fallback (11).

## Legal structure, if any marketplace element is ever tested (08)

- **Disclosed agent:** merchants are the sellers and licensees and pick; delivery is bought from 3PLs (Uber Direct, DoorDash Drive, Sherpa, Zoom2u) or done by an employed fleet; payments through Stripe Connect or Adyen. ~3 months and ~$60–120k to set up.
- **Never copy Instacart's contractor in-store shoppers:** the highest legal risk under the "whole relationship" test and unfair-deactivation claims.
  - This conflicts with **02**, which wants platform shoppers for accuracy. They must then be **employees**, which worsens 01's picking economics.
- **Pricing:** every displayed price is the platform's ACL representation, so it needs scan timestamps and a "charge the lower price" rule. The drip-pricing ban (in force 1 Jul 2027) means all-in prices; the Unit Pricing Code likely applies.
- **Restricted goods:** liquor only with the bottle shop as seller and ID at the door; exclude tobacco (Vic licence required) and vapes (pharmacy only).
- **Cold chain:** chilled pickups go last, with a time cap.
- **Privacy:** blur faces on-device in shelf video; automated-decision transparency from 10 Dec 2026; never scrape retailer images (copyright; EU database right).

## Check first (non-negotiable, 11)

**Fulfilio sale documents.** Australia Post bought **Rendr** (same-day merchant delivery) in April 2026. Any restraint or confidentiality term still binding you from the Fulfilio sale could block local-delivery aggregation. The federal non-compete reform doesn't cover sale-of-business restraints or your income level. Review those documents and your employment contract **by 15 Dec 2026**, alongside the rent-roll path's employer-consent step.

## Cheapest tests (only if the rent-roll tests fail by 31 Jan 2027)

| # | Test | Cost / time | Kill if | Source |
|---|---|---|---|---|
| 1 | **Coverage check:** which independents in 3 Melbourne areas are already on Uber Eats/DoorDash; order 20 test baskets | ~A$1.5k, 2 weeks | ≥70% already listed **and** stock errors <5% → the software gap is gone too | 06 |
| 2 | **Concierge long-tail catalogue** for ~50 Melbourne ethnic/specialty stores, pitched to one platform and 10 brands/importers | ≤A$40k, 90 days | No paid platform pilot (≥A$20k or LOI covering 100+ stores) **and** <3 of 10 brands pre-pay ≥A$10k for a report; or no paying pilot by 30 Apr 2027 | 10, 11 |
| 3 | (Optional, only if pursuing a niche) **Concierge pre-order service**, Brunswick/Northcote + CBD/Southbank, at real prices plus markup and fee | ~A$25–40k, 90 days | <75 paying customers by day 60; <25% 4-week repeat; <30% multi-shop orders; average order <$60; <88% items supplied after week 6 | 03 |

Personal limit for grocery: ≤A$250k cash, no personal guarantees (11).

**Time-sensitive:** Woolworths Investor Day on **18 Nov 2026** (online and Milkrun plans) is worth reading before committing to anything here (03).
