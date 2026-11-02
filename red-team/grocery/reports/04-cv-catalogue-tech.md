# Computer-Vision & Catalogue Engineering Lead: red-team report

## Verdict
**It survives only if POS sales data does the inventory work and scanning is limited to keeping it right.** Phone-video shelf scanning can now identify packaged SKUs at about 95% per facing. It cannot see back-room stock, quantities or sell-through between scans. It struggles with size variants, loose fresh food and unlabelled ethnic imports. A 25-line basket split across 2–3 merchants will reach the customer with at least one wrong line most of the time. **Biggest issue:** the tech is now a commodity. In July 2026 Instacart bought Arpalus, a phone-video shelf-recognition company claiming >95% accuracy. Trax, Focal, Simbe and the general vision-language models (Gemini, Claude) do the rest. The scan technology is not a moat. Any moat comes from the merchant network and the availability data it produces.

## Verdict on the business model
- **Full marketplace with scan-only inventory: no.** Without POS data, the platform sees what was on the shelf at the last scan, not what is there now. Stock-outs reach the customer as missing or substituted lines. With several merchants per basket those misses compound. Picking and delivery have already happened, so they can't be fixed cheaply.
- **Software only (catalogue and availability layer for merchants who sell on DoorDash, Uber Eats and their own sites): the viable version.** The pitch is "scan your store once and get a clean, image-rich, GTIN-matched online catalogue in a day; connect your POS and we keep stock and prices in sync across every channel." The hard, valuable part is onboarding: taking a 6,000-SKU independent from nothing to listed. Scanning is a cheap way to do that onboarding, not a way to run inventory.
- **Best wedge for this founder:** catalogue and availability sync for ethnic and specialty grocers, whose products are missing from GS1 data and badly listed on the delivery apps. Incumbents serve them worst, and the founder's data skills apply directly.

## Attacks on the thesis

**1. Facings are not stock. Severity: High.**
A shelf photo shows whether a product is on the shelf, roughly how many facings are visible, and sometimes how deep the stock goes (only with depth sensors). It cannot show back-room stock, sales after the scan, or deliveries not yet put out. The classic Gruen & Corsten (2002) study put grocery out-of-stocks at about 8% of SKUs at any moment **[verified: Gruen/Corsten via UNH/SN summaries]**. It found roughly a quarter of them were "in the store but not on the shelf" **[unverified: recalled from the same study]**. A scan therefore marks products as out of stock when they are in the back room (lost sales). It also marks products as in stock that sell out two hours later, which reaches the customer as a missing line. Availability decays between scans, and the decay is fastest on fast movers: milk, bread, specials. Those are exactly the lines online baskets are built around.

**2. The basket compounding problem. Severity: High.**
Basket accuracy multiplies across lines. With 25 lines and 95% per-line accuracy, P(every line right) = 0.95^25 ≈ **28%**. At 98% it is ≈ 60%, and at 99% ≈ 78% **[estimate: arithmetic]**. Even 99% per line means one order in five has a problem. With several merchants, a miss at Merchant B can rarely be replaced from Merchant A once the courier has left. The result is a refund, not a substitution. The order then pays its full picking and delivery cost on a smaller basket. For comparison: CHOICE gives Woolworths Online an 85% delivery-accuracy score **[verified: CHOICE comparison page, date unclear]**. A UK Which? survey (late 2025) found 20% of online grocery orders included a substitution **[verified: Which? via search summary]**. Those are retailers with full perpetual inventory and picking systems. Scan-only cannot match them.

**3. Shelf video sees the front of the pack, not the barcode. Severity: High for the catalogue.**
GTINs are printed on the back or bottom of the pack. A video pass along the aisle sees front-of-pack artwork. So every recognition is a visual match to a reference catalogue, and it fails on:
- **Size and pack variants:** 500g vs 1kg, 6-pack vs 10-pack, "Lite" vs "Original", with near-identical artwork.
- **Packaging refreshes:** artwork changes several times a year.
- **New products with no reference images.**

Trax itself names "nearly identical products" and reflective packaging as the hard cases **[verified: Trax accuracy blog]**. The vendor headline figures are all per-facing or per-tag, from vendors, and unaudited:
- Trax: 96% SKU-level **[verified: Trax site, vendor claim]**
- Arpalus: >95% on average **[verified: Instacart press release, 16 Jul 2026]**
- Simbe: 99% shelf-label read **[verified: Simbe/press, vendor claim]**

None is a figure for "correct GTIN, correct size, correct price, in stock."

**4. Prices from shelf labels. Severity: Medium.**
Reading the text on a shelf-edge label is close to solved, at about 99% by Simbe's claim. The hard part is **linking the label to the right product** when stock has drifted along the shelf. Promotions add more problems:
- multibuy offers
- member-only prices
- "while stocks last" offers
- end-of-aisle displays priced on a separate ticket

Price errors are not cosmetic. Simbe's own fleet data shows about 0.7% of tags wrong in stores that use robots (132M wrong of 18B scanned) **[verified: vendor-reported]**. A platform that shows a scanned price is making a pricing representation under Australian Consumer Law. The price should come from the POS price file. A scanned price should only flag discrepancies.

**5. Loose, fresh and random-weight items. Severity: Medium–High.**
Produce, deli, meat and bakery carry no GTIN. Produce uses PLU codes. Weighed items use in-store random-weight barcodes. These are often 30–50% of an independent's sales by value **[estimate: typical fresh share for independents and specialty stores]** and are the reason customers choose a local butcher or greengrocer. Vision can classify "banana" but not quality, ripeness, origin, cut, or whether the scotch fillet tray is the 400g or the 1.2kg one. The catalogue has to treat these as generic items sold by weight with a price per kg and an estimated weight. That needs adjustment at the till (pre-authorise and capture later). It is a payments and UX problem, not a vision problem, and the brief misses it.

**6. The ethnic long tail. Severity: Medium. This is both the problem and the opportunity.**
Imported Asian, Indian, Middle-Eastern and African SKUs:
- are largely absent from GS1 Australia's National Product Catalogue (NPC)
- carry foreign GS1 prefixes
- have thin coverage in Open Food Facts for Australia (OFF passed ~4M products worldwide in 2025 **[verified: OFF/Wikipedia]**, but its AU board showed only ~1,300 products/month of growth in late 2024 **[verified: OFF AU progressboard]**)

Current vision-language models read CJK and Devanagari scripts reasonably well, so in this segment a scan is the **only** practical way to build the catalogue. That is real value. But the same stores often carry grey imports without compliant English labelling. A platform that lists them inherits that compliance exposure (question for the legal specialist).

**7. Scanning cost is staff labour, not compute. Severity: High for adoption.**
- **Compute is trivial.** A full-store video pass at 1 fps for 45 minutes is about 2,700 frames. At ~258–1,000 tokens per frame (Gemini-style image tokenisation **[unverified: per-frame token count]**) that is roughly 0.7–2.7M input tokens. At Gemini 2.5 Flash list price of US$0.30/M **[verified: pricing aggregators citing Google]**, that is under US$1, or about **A$1–5 per full scan** including output and re-crops **[estimate: AUD≈1.5×USD]**. A cheaper pipeline (on-device detection, embedding retrieval, and a vision-language model only for unresolved crops) brings it to under A$0.50.
- **Staff time is the real cost.** A 45–60 minute pass at A$30–35/hr loaded is ~A$25–35 per scan. Daily scans cost ~**A$750–1,000/month per store** **[estimate]**. That compares with the incremental margin from a new channel. A store doing 20 online orders/week at A$80 and 25% gross margin, after a ~15% clip, earns ~A$1,700/month in net margin, before picking labour. Daily scanning would consume most of it. Merchants will scan once and then stop. Data freshness collapses, and so does the order-accuracy rate.

**8. The tech is a commodity, and well-funded players already own it. Severity: High for the "moat" thesis.**
- **Instacart:** bought Arpalus (July 2026). Its ~600k shoppers already film shelves through "Store View" **[verified: Instacart IR]**.
- **Trax** (part of FORM since Feb 2026): sells on-device phone recognition **[verified: Trax site]**.
- **Focal:** shelf cameras rolled out across Walmart Canada **[verified: Retail Dive]**.
- **Vori:** raised US$22M (May 2026) for an independent-grocer operating system that combines POS and inventory **[verified: multiple reports]**.
- **DoorDash:** already lists IGA stores in AU **[verified: DoorDash/press, 2021–22]**.

A two-to-three engineer team using off-the-shelf models can reach about 90% of Arpalus-level per-facing accuracy within six months **[estimate]**. So can DoorDash, Uber Eats, Metcash or any POS vendor.

## Things the brief gets wrong, misses or understates
- **"Without a POS integration" is a bug, not a feature.** Almost every independent supermarket, bottle shop and pharmacy already runs a scanning POS (SwiftPOS, Idealpos, Square, Lightspeed and similar). The POS knows sales in real time and the current price file. Ignoring it throws away the best signal available. POS stock-on-hand records are inaccurate: one retail study found ~65% of SKU records wrong **[unverified: recalled DeHoratius & Raman 2008]**. But "POS sales + periodic scan correction" beats either one alone by a wide margin.
- **"Universal catalogue" is mostly already built for barcoded mainstream goods.** GS1 Australia's NPC holds brand-owner data and images that Woolworths, Coles and Metcash rely on. GS1's Trusted Content Service gives subscribers access to publicly available NPC data and images **[verified: GS1 AU FAQ]**. Its terms bar on-selling content "in the form it is provided" and allow sharing only when it is built into a different product **[verified: mirrored T&Cs dated 1 Jul 2024; confirm current]**. Pricing is not published. NZ charges NZ$4.15–5.75 per active GTIN per quarter for publishers **[verified: GS1 NZ fee schedule, 2023]**. The unbuilt part is the fresh, ethnic and specialty long tail.
- **Licensing traps:**
  - **Open Food Facts:** the database is ODbL (share-alike, so a publicly used derived database must be released under the same terms). Images are CC-BY-SA. A proprietary catalogue built on OFF risks having to be opened up. Use OFF for gap-fill and matching hints only **[verified: OFF licence terms as I know them; confirm]**.
  - **Brand artwork:** product photos taken by the platform are probably usable for identifying the product, but this needs legal review.
  - **Syndigo, 1WorldSync and Salsify** are US- and EU-centric. In AU, GS1 NPC is the syndication rail.
- **"Global from day 1" is false from a catalogue standpoint.** GTIN data, PLU conventions, label formats, languages and data rights are national. Each country needs its own reference catalogue.
- **Time-sensitive:** the Arpalus acquisition (16 Jul 2026) and Vori's Series B (May 2026) are recent. Instacart does not currently run consumer grocery delivery in AU **[unverified]**, but it could license Store View here.

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| Phone video can identify SKUs | >95% avg item ID (Arpalus); 96% (Trax) | verified: vendor claims, Instacart IR 16 Jul 2026; Trax site |
| Shelf-label price reading | 99% tag ID (Simbe) | verified: vendor claim |
| Price-tag error rate in stores | ~0.7% (132M of 18B tags) | verified: Simbe fleet data, vendor |
| Baseline OOS in grocery | ~8% (7.9% US, 8.6% EU) | verified: Gruen/Corsten 2002 via UNH summary; dated |
| OOS reduction from CV | Focal ">30% fewer OOS-hours"; Simbe "60%" / "20%" conflicting | verified as vendor claims; not independent |
| Online substitution frequency | 20% of UK orders (Which?, late 2025) | verified: search summary |
| Woolworths delivery accuracy | 85% CHOICE score | verified: CHOICE; date unclear |
| Instacart replacement satisfaction | 95% (2024) | verified: Instacart letter |
| OFF size | ~4M products globally (2025) | verified |
| GS1 catalogue cost | AU unpublished; NZ NZ$4.15–5.75 per GTIN per quarter (publisher) | verified NZ; AU unverified |
| VLM compute per full-store scan | ~A$1–5 | estimate: tokens × Gemini Flash list price |
| Staff cost per full-store scan | ~A$25–35 | estimate: 45–60 min × A$30–35/hr |
| Zero-shot VLM product-category accuracy | ~68–71% vs 91% for supervised YOLO | unverified: Oct 2025 preprint, inconsistent |
| Independent IGA on DoorDash | 100+ stores at launch | verified: DoorDash/press, 2021–22 (stale) |

## Improvements (ranked by impact)
1. **Make POS integration the inventory source and scanning the correction.**
   - Build connectors in this order: Square, Lightspeed and Shopify (public inventory and catalogue APIs), then SwiftPOS and Idealpos (partner integrations), then a CSV/SFTP price-file fallback.
   - Model each SKU as: available = f(last confirmed count, sales since, delivery cadence, decay prior).
   - Show "likely available" with a confidence score, and hide SKUs below a threshold.
2. **Scan to onboard, not to operate.**
   - One assisted full-store scan builds the catalogue in a day: shelf-label OCR (description, price and the barcode or PLU often printed on the label), front-of-pack recognition, then a merchant review UI.
   - After that, scan only partially: e.g. "film the 3 aisles with the most misses this week."
3. **Use the shelf-edge label as the primary key.** Many AU shelf labels carry the product barcode or internal code. Decoding it gives an exact GTIN or POS code and avoids most size-variant confusion. Use front-of-pack recognition only to confirm the facing is present.
4. **Get the pickers to collect the data.** Every pick is a free ground-truth check (found or not found, plus a photo). This is the Instacart Store View model, applied to merchant staff. Feed it back into availability.
5. **Run fresh as a separate product.** Use generic items sold by weight, with prices per kg from the POS or the scale system, pre-authorise and capture later, and add a customer note field. Don't try to recognise fresh items by vision.
6. **Catalogue strategy:**
   - License GS1 Trusted Content for mainstream SKUs.
   - Build your own photographed, translated, GTIN-mapped records for the ethnic and specialty long tail. This is the one dataset others lack. Keep it ODbL-clean.
   - Use embedding-based variant matching across merchants, with human review for low-confidence links.
7. **Narrow the merchant set.** Start with bottle shops, specialty and ethnic grocers (fewer SKUs, slower turnover, poorly served catalogues). Avoid fast-turning convenience stores with high OOS rates in the first phase.

## Tests & kill criteria

| Test (≤90 days) | Metric | Kill / proceed threshold |
|---|---|---|
| Assisted onboarding scan at 5 stores (2 ethnic, 1 IGA, 1 bottle shop, 1 butcher) | % SKUs correctly matched (GTIN or POS code, size, price) after merchant review; minutes per 1,000 SKUs | Kill if <90% matched or >60 staff-min per 1,000 SKUs |
| Scan-only vs scan + POS availability | Shadow-order 100 baskets of 20 lines/store; predicted-available lines actually on shelf | Kill scan-only if per-line accuracy <97% at a 24h scan interval; proceed if scan + POS ≥98.5% |
| Freshness decay | Re-check sampled SKUs at 2h, 8h, 24h, 72h after scan | Measures the needed scan interval; if <24h is needed, scan-only is dead |
| Merchant re-scan compliance | Share of stores re-scanning unprompted weekly | Kill scan-as-maintenance if <40% at week 6 |
| Long-tail value | Share of ethnic-store SKUs missing from GS1/OFF; merchant willingness to pay for a ready-made Uber/DoorDash listing | Proceed if >50% missing and ≥3 of 5 merchants pay ≥A$300 setup |
| POS reach | Share of target merchants on POS systems with usable APIs | If <50%, budget for the price-file fallback |

## Answers to the brief's questions in my domain
**Q4: Is shelf scanning good enough, and is the catalogue buildable?**
- **Product identity: yes, for packaged goods.** At about 95% per facing, it is good enough to build a catalogue with human review.
- **Live inventory: no.** Facings ≠ stock, scans go stale within hours on fast movers, and errors compound across the basket.
- **Prices:** read them from the POS price file. Use scans only to flag discrepancies.
- **Fresh and loose items:** handle them as generic items sold by weight, not by vision.
- **Achievable rates** **[estimate]**:

  | Setup | Lines wrong per order | Orders with a wrong line (25 lines) |
  |---|---|---|
  | Scan-only, weekly | 8–15% | ~90% |
  | Scan-only, daily | 4–8% | ~65–85% |
  | POS + daily partial scans + picker feedback | 1.5–3% | ~30–50% |

  The full major-chain online benchmark is roughly 85% delivery accuracy (CHOICE) and ~20% of orders with a substitution (UK Which?).
- **Catalogue:** buildable. Mainstream data comes from GS1 (licensed). The long tail has to be built by the platform, and that part is defensible.
- **Build effort** **[estimate]**:
  - MVP (capture app, vision-language model pipeline, matching, merchant review UI, one POS connector): 3–4 engineers × 5–6 months ≈ A$0.6–0.9M.
  - Production (multi-POS, availability model, fresh, a catalogue operations team): 8–12 people × 18 months ≈ A$4–6M.
- **Per-store compute:** A$5–50/month. It is not a constraint. Staff time for scanning is the constraint, at ~A$25–35 per full pass.
- **Moat:** none in the vision technology. Any moat lies in the merchant connections and POS integrations, the long-tail catalogue, and accumulated per-SKU availability priors.

**Q5 (my lane only):** Arpalus/Instacart, Trax/FORM, Focal, Simbe and Vori show that the capability exists and is being consolidated by large players.

**Q8:** From my lens: software (catalogue onboarding plus multi-channel availability sync), POS-first, starting with the ethnic and specialty long tail. Not a scan-only marketplace.

## Questions I'd hand to other specialists
- **Unit economics:** at a 2–3% per-line miss rate and multi-merchant pickup, what refund and redelivery cost per order breaks the model? Is a single-merchant basket the only economic unit?
- **Merchant adoption:** will an independent let a third party read its POS data? What do SwiftPOS and Idealpos charge for API access or partnerships?
- **Legal:**
  - ACL liability for displayed prices sourced from scans
  - FSANZ labelling of listed grey-import SKUs
  - copyright in brand artwork captured by merchant scans
  - OFF ODbL share-alike exposure
- **Competition:** would DoorDash or Uber Eats in AU pay for (or copy) a catalogue-onboarding tool for their independents? Is Metcash a buyer or a blocker?
- **Founder fit:** is a data-and-catalogue software company with modest scale (a niche of A$5–20M ARR) better than the round-3 pricing-engine path?
