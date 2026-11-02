# Brief: grocery aggregation using local merchants as dark stores

Source: founder's description, 3 Nov 2026. Every agent reads this file.

## The founder
Computer scientist, statistician and CFO; ex-BCG; former CEO of LocalAgentFinder (agent-comparison marketplace); founded Fulfilio (warehouse/fulfilment platform, acquired by Australia Post), whose real edge was a *physical arbitrage*: consolidating spare warehouse space into local delivery hubs. Currently a ~$500k/yr tech executive in Melbourne. Wants something that beats that on **wealth creation and job satisfaction**. Heavy hands-on AI user. (Prior red-team rounds on a property-management idea are in `red-team/`; they are not relevant here except as context on the founder's goals and risk limits.)

## The idea (founder's words, lightly edited)
A grocery aggregation business:
- **Merchant software:** merchants scan their stores (e.g. phone video/photos of shelves) to **update inventory and maintain selection** without a POS integration.
- **Universal catalogue:** the platform stitches scans into a **universal SKU list with photos**, matched across merchants.
- **Aggregated delivery:** customers order one basket that can draw from **multiple local merchants used as dark stores**; the platform aggregates pickups into one delivery. Merchants get an **additional sales channel**.
- **Revenue:** the platform **takes a clip of the basket** (a take rate).
- **Scale:** "could be global from day 1."

The founder notes the parallel with Fulfilio: using existing under-utilised physical capacity (merchant shelves and staff) instead of building dark stores.

## Questions this red team must answer
1. Do the unit economics work per order (basket size, take rate, picking, multi-stop pickup, delivery, payments, refunds/substitutions, CAC)? At what order density?
2. Will merchants (independent grocers, IGA/Foodworks, specialty, ethnic, butchers, bakeries, delis, pharmacies, bottle shops) adopt it, keep inventory accurate, pick orders and accept the take rate?
3. Will consumers choose it over Woolworths/Coles/Aldi online, Amazon, Uber Eats/DoorDash grocery and quick commerce? For which baskets?
4. Is shelf-scan inventory technically good enough (SKU recognition, stock levels, prices, freshness of data) and is the universal catalogue buildable?
5. Who already does this (AU and global) and what happened to similar plays (Milkrun, Voly, Getir, Gorillas, Jokr, Instacart, Gopuff, Swiggy Instamart, Zepto, Blinkit, Deliveroo Hop, HungryPanda, etc.)?
6. Is "global from day 1" credible, or is this a city-by-city density business?
7. What are the legal and regulatory constraints (gig-worker rules, food safety, age-restricted goods, pricing accuracy, privacy, payments/marketplace tax)?
8. Which version of the idea, if any, is the business: full marketplace with delivery, software only (scanning and catalogue for merchants or for existing marketplaces), or something else?
9. Founder fit and path versus staying employed and versus the rent-roll pricing-engine path (`red-team/round3/SYNTHESIS.md`).
10. What is the smallest test that proves or kills it within ~90 days?
