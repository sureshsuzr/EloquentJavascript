# Merchant Researcher (Independent & Specialty Retail): red-team report

_2 Nov 2026. Several primary sources were blocked from this session (accc.gov.au, merchants.ubereats.com, merchants.doordash.com, smartcompany.com.au), so some figures rest on search-engine summaries of those pages. These are labelled as such._

## Verdict
**Survives only if the platform takes on the merchant's work and the merchant mix is chosen for margin. As briefed, the merchant side fails.** A 10–20% take on packaged grocery, plus merchant-side picking and merchant-side shelf scanning, leaves a typical independent supermarket with about zero contribution per order. The merchant responds the way independents already do on Uber Eats and DoorDash: higher online prices, missing range and slow picking. **Biggest issue:** independents will not do the operational work that keeps the system accurate (scanning, picking, substituting) during trading hours. If the platform must do it, this is an Instacart-style shopper business, not a "dark stores for free" arbitrage.

## Verdict on the business model
- **Full multi-merchant marketplace with merchant picking and scanning:** not viable from the merchant side. Merchant economics only work for high-margin specialty stores (bakeries, delis, some ethnic grocers). Those stores have small sub-baskets, so per-order platform costs hit hardest there.
- **Marketplace where the platform does the picking and the scanning** (Instacart model: one shopper walks a strip of stores and captures shelf video while picking): this is the version merchants will adopt. They do nothing and get incremental orders at 8–15%. It is labour-heavy for the platform, so it only works at order density on one dense shopping strip.
- **Software only (catalogue and shelf-scan as a service), sold to Metcash, Foodworks/AUR, or to Uber Eats and DoorDash for their independent-grocer supply):** this is the strongest merchant-side business. Merchants already sell on those apps. Their pain is getting a correct catalogue with photos and stock onto those apps without a POS integration. Metcash is losing share partly because of low online penetration (Morningstar view [verified: Morningstar via search summary]). A tool that gets ~1,600 IGA stores to "online-ready" is worth more to Metcash than to any single store.
- **My view:** the business is a **specialty-strip shopper marketplace in one suburb cluster, used to prove the catalogue and scan tech, then sold as software to platforms and banner groups**. Do not build it as a merchant-funded aggregator of independent supermarkets.

## Attacks on the thesis

**1. The take rate consumes all of the merchant's per-order margin on packaged grocery (High).**
Contribution per $35 merchant sub-basket at a 15% take, with ~6 minutes of merchant picking at ~$35/hr loaded casual retail wages ($3.50) [estimate: General Retail Industry Award Level 1 casual ~$31–33/hr plus on-costs, after the July 2026 increase (not checked)]:

| Merchant type | Gross margin | GM $ | – take | – pick | Contribution |
|---|---|---|---|---|---|
| IGA/Foodworks-style supermarket | 22–28% [estimate: Metcash banner product margins "flat", ACCC 2025 per search summary; broker listings show 25–31%] | $8.75 | $5.25 | $3.50 | **~$0** |
| Bottle shop | 22–30% [verified: Baron Accounting guide, secondary] | $9.10 | $5.25 | $2.00 | ~$1.85 |
| Butcher | ~29–35% [unverified: single broker listing at 29.2%] | $11.20 | $5.25 | $4.50 (cutting/weighing) | ~$1.45 |
| Greengrocer | 30–40% gross, but 5–10% shrink [estimate] | $12.25 | $5.25 | $5.00 (selecting produce) | ~$2 before shrink |
| Asian/Indian/ME grocer | 25–35% [estimate] | $10.50 | $5.25 | $4.00 | ~$1.25 |
| Bakery / deli / patisserie | 55–70% [estimate: food-cost ratios ~30–40%] | $21.70 | $5.25 | $2.50 | **~$14** |

Independent supermarkets' net margins are around 2–4% [estimate; the 6.6% and 10.2% in broker listings are cherry-picked sale pitches], so a 10–20% clip cannot come from margin. It is paid either by price markups or by the store's own operators working unpaid hours. CHOICE found grocery items on delivery apps averaged ~11% dearer and up to ~40% dearer [verified: CHOICE via search summary], and Uber says each merchant sets its own app prices. **Independents will mark up**, which removes the consumer case against Coles on Uber Eats and Woolworths on DoorDash.

**2. Merchants will not pick reliably during trading hours (High).**
A typical independent supermarket has 2–5 people on the floor; a butcher, bakery or deli has 1–3. Peak delivery demand (Fri–Sun, 4–7pm weekdays) overlaps with peak in-store trade. The first thing owners sacrifice is the tablet order. The usual failure modes: late acceptance, quiet substitution of the item at hand, "out of stock" for anything in the back room. Multi-merchant baskets compound this. Fill rate across stores multiplies (0.95⁴ ≈ 0.81 for a four-store basket being fully correct) [estimate]. A late pick at any one store holds up the whole consolidated delivery.

**3. Merchants will not keep scanning (High).**
The thesis assumes merchants record a shelf video often enough to keep stock and prices current. Evidence from every merchant-maintained catalogue (Uber Eats menus, Google Business, IGA Shop Online ranges) is that owners do it once at onboarding and then drift. Instacart decided that *shoppers*, not stores, would capture shelf video (Store View), and it cites an ECR Retail Loss Group figure that up to 60% of inventory records are inaccurate [verified: Grocery Dive / Supermarket News via search summary]. If Instacart, with US$30bn+ GTV, won't rely on stores to scan, a startup shouldn't either. Specific blind spots: random-weight and counter items (meat, deli, bakery, loose produce) have no shelf SKU; back-room stock is invisible; shelf-edge prices at independents are frequently stale; and imported ethnic SKUs often carry no GS1 barcode or only foreign-language labels.

**4. "Additional sales channel" is mostly cannibalisation (Med–High).**
An independent's online orders come mostly from existing local customers. When those customers order online, the store loses impulse add-ons and pays 15% on sales it would have made anyway [estimate; Uber Eats' IGA Portside Wharf case, 3,000+ orders since Oct 2021 [verified: Uber Eats merchant page via search summary], is vendor marketing and reports no incrementality]. Owners know this. To make the channel genuinely additional, the platform has to bring customers from outside the store's catchment. That is the multi-merchant basket's real value, and the pilot should measure it.

**5. Incumbents already own the supply relationship (Med–High).**
- IGA stores have run on DoorDash since 2021 (100+ stores, ~1,600 products at launch) [verified: Inside Retail/Inside FMCG via search summary]. Metcash's own store-fulfilled IGA Shop Online targeted 800 stores by FY25; 190 were live in the last confirmed figure [verified: itnews, ~2022; current count unverified].
- From 26 Dec 2025, Coles is exclusive with Uber Eats and Woolworths moved to DoorDash [verified: Inside FMCG / Uber newsroom via search summary]. Both apps already host the major chains, so they want independents for range differentiation and will compete hard (fee cuts, marketing funds) for exactly the specialty and ethnic merchants this plan needs.
- Metcash is buying IGA stores (target: own 25–30% of network revenue; first Victorian Daly's IGA acquisitions Q4 FY26) [verified: Inside FMCG, May 2026, via search summary]. Corporate-owned IGAs will follow Metcash's channel decisions, not a startup's.
- Metcash has its own B2B "Sorted" marketplace (SAP Commerce, ~3,500 suppliers) [verified: B2BEA/itnews via search summary], which gives it product-catalogue data for IGA ranges a startup would have to rebuild.

**6. Precedents point toward aggregators becoming supply feeds (Med).**
- **Mercato (US)** aggregated 800–1,000+ independent grocers but relied on DoorDash for most deliveries and in 2024 pushed its inventory onto Grubhub [verified: Business Wire / Progressive Grocer via search summary]. The independent-grocer aggregator ended up as catalogue and supply middleware for the big apps. That is the realistic end state here.
- **HungryPanda's PandaFresh** sells Asian groceries from its **own warehouse** rather than from partner grocers, unlike rivals that use existing stores [verified: FCSI operator profile via search summary]. The best-placed player for the ethnic-grocer niche chose not to rely on those merchants' inventory.
- **Milkrun and Voly** were dark-store operators, not merchant networks, so they say little about merchant behaviour. They do show that Australian density does not fund fast delivery. Voly creditors were owed $17.7m and expected 15–27c in the dollar; Milkrun lost ≥$10 per delivery [verified: Startup Daily/Forbes AU via search summary].
- **Instacart retailer fees:** retailers complained publicly about ~10%+ commissions [verified: The Counter/WSJ-derived, 2020]. One grocer chose DoorDash at ~9%. Grocery merchants anchor near **8–12%**, not 20%.

**7. Merchant heterogeneity raises onboarding cost (Med).**
Each segment has its own constraints. Pharmacies can't list S2/S3 medicines without a pharmacist's involvement. Bottle shops need a licence that allows delivery, plus age checks at the door. Butchers sell by weight, so final prices are only known after cutting. Bakeries sell out by 2pm. Onboarding sales and support cost per merchant will be high: 3–6 visits [estimate]. Lifetime value per specialty merchant at ~$300–1,500/month GMV is small.

## Things the brief gets wrong, misses or understates
- **"Merchant shelves and staff are under-utilised capacity."** Shelves are, staff are not. Independent retail runs on the thinnest award-wage roster the owner can manage. Fulfilio's spare warehouse space was idle; a deli counter at 11am Saturday is not.
- **No POS integration is a weakness as well as a selling point.** Without POS data you can't detect sell-through between scans. Even a cheap read-only POS feed (Square, Lightspeed and Shopify have APIs) beats video for stock levels in packaged grocery. Use scanning for catalogue creation and POS or shopper capture for stock.
- **Price parity is not addressed.** Merchants will set higher online prices. The plan needs a policy (parity required, capped markup, or transparent markup) and a matching take rate.
- **Who is the merchant of record?** This determines GST, refunds, liquor and pharmacy compliance. Merchants will expect the platform to absorb chargebacks and refunds for substitution disputes.
- **Drakes is SA/QLD.** It is irrelevant to a Melbourne pilot. In Victoria the relevant independents are IGA (including Supa IGA and Ritchies stores), Foodworks/AUR, Leo's/Supa-style family chains, and the large ethnic independents.
- **Merchant churn on delivery apps** is a documented pattern. Independents list, get a small number of orders, stop updating the menu and go dormant. Plan for active-merchant rate, not signed-merchant count.
- **Time-sensitive:** platform exclusivities (Coles–Uber from Dec 2025, Woolworths–DoorDash) and Metcash's store-ownership push are shifting now. Re-check before the pilot. The brief is dated 3 Nov 2026, one day after today. Probably a typo; flagged.

## Numbers checked

| Claim / assumption | Finding | Status / source |
|---|---|---|
| Merchants tolerate a 10–20% take | Grocers anchor near ~9–12% (Instacart/DoorDash precedent); restaurants pay ~30% on AU apps but have higher GM | verified (secondary): The Counter 2020; search summary of AU restaurant commission coverage |
| Independent supermarket GM / net | GM ~22–28%, net ~2–4%; single-store listings show 25–31% GM, 6.6–10% net (sale pitches) | estimate; broker listings [unverified] |
| Coles/Woolworths EBIT margins 5–6% vs Metcash lower | Confirmed by ACCC final report (21 Mar 2025) | verified: ACCC via SBS/search summary |
| Delivery-app grocery markup | ~11% average, up to ~40% | verified: CHOICE via search summary |
| IGA on DoorDash | 100+ stores, ~1,600 SKUs, 2021 | verified: Inside Retail (dated) |
| IGA Shop Online | Target 800 stores by FY25; ~190 live at last confirmed count | verified (dated ~2022); current count unverified |
| Coles–Uber Eats exclusive; Woolworths–DoorDash | From 26 Dec 2025 | verified: Inside FMCG / Uber newsroom via search summary |
| Metcash FY26 | Revenue $19.63bn; Food EBIT $261.8m (+5.4%); IGA price gap 2.1%; network ownership target 25–30% | verified: ASX / BNA via search summary |
| Shelf-scan already exists at scale | Instacart Store View: shopper-captured video; ECR estimate up to 60% inventory records inaccurate | verified: Grocery Dive / Supermarket News via search summary |
| HungryPanda grocery | PandaFresh runs own warehouse; grocery sales "22.9m" in 2024 (currency unclear, likely GBP) | verified (company profile); currency unverified |
| Mercato merchant count | 800–1,000+ independents; DoorDash fulfils most orders; on Grubhub from 2024 | verified: Business Wire via search summary |
| Merchant pick cost per sub-basket | ~$2–5 | estimate: 4–8 min at ~$35/hr loaded |

## Improvements (ranked by impact)
1. **Platform picks and scans; merchants only sell.** Send one shopper per strip on a loop. They pick multi-store baskets and record shelf video as a by-product (the Instacart Store View pattern). Merchants then do nothing and can accept 8–12%. This turns the scan-compliance problem into a labour-cost problem, which can be measured.
2. **Choose merchants by margin and destination value, not by count.** Lead with bakeries, delis, specialty butchers, ethnic grocers with hard-to-find SKUs, fishmongers and quality greengrocers. Use one independent supermarket only for staples. Packaged grocery is the most price-transparent category and the one where Coles and Woolworths win.
3. **Tier the take rate by category.** For example: 6–8% on packaged grocery, 12–15% on fresh and specialty, 15–20% on prepared food and bakery. Pair it with a published price-parity rule (within 5% of shelf price) to protect the consumer case.
4. **Read-only POS sync wherever it exists** (Square, Lightspeed and Shopify have APIs). Scanning fills the gaps rather than carrying the whole load.
5. **Build the catalogue as a separately saleable asset from day 1:** GTIN plus photos plus multilingual names for imported SKUs. Its likely buyers are Metcash and AUR (for IGA and Foodworks online readiness), and Uber Eats and DoorDash (independent-supply onboarding).
6. **Make "new customers" the merchant pitch, not "another channel".** Show each merchant how many orders came from customers outside their usual catchment. That is the only figure that justifies the fee.
7. **Keep pharmacy and liquor out until the core works.** Both add licensing work for little basket value.

## Tests & kill criteria (90 days, one Melbourne cluster)

**Cluster:** Brunswick–Coburg–Brunswick East (Sydney Rd and Lygon St strips; about a 3 km radius). It has a dense mix of Middle-Eastern, Italian and Greek grocers and delis, Turkish and Lebanese bakeries, butchers, greengrocers, several IGA/Foodworks-format independents and bottle shops. Households have high rental density and lower car ownership [estimate; check ABS Census 2021 for Merri-bek SA2s]. Backup cluster: Box Hill (Asian grocers), which tests the ethnic-SKU catalogue problem directly.

**20-merchant mix:** 3 independent supermarkets, 5 ethnic grocers, 3 butchers, 3 bakeries, 2 delis, 2 greengrocers, 1 fishmonger, 1 bottle shop (sign up only once delivery-licence status is confirmed).

**Phase 1, weeks 1–4: discovery (approach ~45 merchants to sign 20).** In a 30-minute structured interview, capture GM by category, POS, current apps and their order volumes and fees, online pricing practice, floor staff by hour, last time the menu or catalogue was updated, and the take rate they would accept. Ask for their Uber Eats/DoorDash payout statements; owners who share them are serious. Close with a signed letter of intent.
- **Kill or redesign:** fewer than 12 of 45 sign an LOI at ≥10% take *with* price parity; or fewer than 5 independent supermarkets or ethnic grocers sign at any rate.

**Phase 2, weeks 4–12: concierge pilot.** Use 2 platform shoppers on bikes or a small van, with catalogue capture done by hand by the team. Run a simple web order page for a seeded audience: 300–500 local households from street flyers and community groups.
- **Platform-side scanning test:** compare platform-scanned stock with what was actually found at pick. Target **item fill rate ≥95%** by week 8. Kill if below 90% at week 8.
- **Merchant-side scanning test:** ask 5 merchants to scan weekly themselves. Kill merchant-scanning if fewer than 3 of 5 still scan in week 6.
- **Merchant-pick variant (4 merchants pick their own orders):** kill merchant picking if median accept-to-ready time is over 15 minutes or more than 10% of orders are late.
- **Retention:** at least 15 of 20 merchants still active and willing to continue at full take in week 12. Kill below 10.
- **Incrementality:** at least 40% of each merchant's pilot orders come from customers who say they don't normally shop there. Below 20% means the channel is cannibalisation.
- **Price parity held** (audited basket within 5% of shelf price) at ≥80% of merchants.

**Cost:** about $60–90k all in (two casual shoppers for 8 weeks, vehicle, flyers, a no-code storefront, the founder's time) [estimate].

## Answers to the brief's questions in my domain
**Q2. Will merchants adopt, keep inventory accurate, pick orders and accept the take rate?**
- **Adopt:** yes, if signing up is free and costs no effort. Most specialty merchants will try a new channel.
- **Keep inventory accurate:** no, not by themselves. Accuracy has to come from platform shoppers or a POS feed.
- **Pick:** unreliably at peak. Butchers and delis are the worst, because they serve over the counter. Independent supermarkets are workable off-peak only.
- **Accept the take rate:** 8–12% on packaged goods and 12–18% on specialty and prepared food. Above that they will mark up prices.
- **What makes them stay:** incremental customers they can see, weekly payouts, zero admin, and no tablet that interrupts trade.

**Q8. Which version is the business?** From the merchant side: a platform-picked specialty-strip marketplace as the proving ground, with catalogue and scan software for banner groups and delivery apps as the scalable business.

**Q10. Smallest test in 90 days?** The 20-merchant Brunswick–Coburg concierge pilot above. Its sharpest single metric is **fill rate at pick against platform-scanned stock**, with **week-12 merchant retention at full take rate** second.

**Q6. Global from day 1?** Not on the merchant side. Merchant acquisition is door-to-door, segment-specific and depends on local award wages, licensing and banner contracts.

## Questions I'd hand to other specialists
- **Unit economics:** what does a platform shopper cost per multi-stop basket at 1, 3 and 6 stores, and what order density per strip-hour makes the platform-pick model positive?
- **Technology:** what recognition accuracy can a shopper's walking video reach on unbarcoded imported SKUs, random-weight items and shelf-edge prices, and how often must shelves be re-scanned for 95% fill?
- **Legal:** for Victorian liquor delivery from third-party bottle shops, who holds the licence obligation? Who is merchant of record for GST and refunds? What is the casual or contractor status of multi-store shoppers after the 2024 "employee-like" gig-worker reforms?
- **Partnerships / M&A:** would Metcash, AUR, Uber Eats or DoorDash pay for an independent-supply catalogue? What did Mercato's Grubhub deal pay?
- **Consumer research:** in Brunswick–Coburg, what share of households would pay a $6–10 delivery fee for a specialty multi-store basket that Coles on Uber Eats can't supply?
