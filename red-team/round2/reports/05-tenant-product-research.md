# Tenant-Side Product Researcher: red-team report

## Verdict
**Survives only as a thin retention and referral layer. It fails as a pillar of the economics.** Most renters want to buy, but only about 10% become owners in any year. Victoria has banned fees to renters for applications and rent payments since 31 Mar 2026. Rent cannot go onto an Australian credit file. The only way to make money on the tenant side is commission from lenders, utilities or insurers, which is worth roughly $40–110 per property per year. **The biggest issue:** the founder's equity / credit / savings framing rests on a mechanism (rent reporting to credit bureaus) that doesn't exist here. In Australia, rent history helps a borrower as *genuine savings evidence*, using an agent's ledger, which the PM already provides for free. Build one priced tenant service, a **first-home pathway monetised through broker commission**, and treat the rest as free goodwill.

## Verdict on the platform thesis
- **Tenant services carry none of the economics**, and nothing on the tenant side changes the 2,000–2,500-property scale needed for a $500k draw. Revenue that could realistically be captured is about $40–60 per property per year from home loans plus about $40–80 from utility connections, which incumbents already capture.
- **What the tenant side is good for:**
  1. Lower landlord-side costs: fewer disputes, earlier notice of moves, re-letting within the portfolio.
  2. A small, high-margin commission line.
  3. A feed into the landlord funnel. A renter who "rentvests" (buys an investment property while still renting) is a future management, though that property is usually outside the corridor.
- **Order to add services:**
  1. Free verified rental ledger and reference, plus a "move within the portfolio" option. These are cost and retention tools.
  2. First-home pathway through a broker, as an ACL credit representative or a disclosed referrer, but only after the 6-week test passes.
  3. **Never build:** tenant subscriptions, rent-payment rails, deposit or savings products, rent-to-own, or a tenant share of the maintenance fee.

## Attacks on the thesis

**A1. Intent is plentiful; action is about 10% a year. (High)**
- Stated intent:
  - 78% of renters want to buy and 59% don't think they can (AHURI 2024).
  - 57% "plan to buy within 2 years" (Resolve Finance, a lender-commissioned survey).
  - Only 13–19% expect to buy within 12 months (Westpac 13%, Agile Consumer Pulse 14% of non-owners, Finder 19%).
- Behaviour: in HILDA panel data about 10% of renters became owners each year in 2013–16, down from 13.6% in 2001–04, and only 7.6% of 18–24-year-olds.
- Lead with the behavioural number. A product sized on "57% plan to buy" will overbuild by about 5x.

**A2. "Rent history as credit evidence" is not available in Australia. (High)**
- Part IIIA of the Privacy Act confines credit reporting to consumer credit information, and a landlord collecting rent is not a credit provider (Bright Law commentary on the amending regulations; check against the Privacy (Credit Reporting) Code 2025). Experian and Equifax are effectively the only bureaus since Experian absorbed illion's consumer data. I found no AU rent-reporting product at either.
- The US/UK analogues are weak even where rent reporting is legal:
  - **US:** the Urban Institute / Esusu randomised trial raised the share of renters *with* a score by about 12 points but found no significant effect on reaching prime (661+).
  - **UK:** reviews of CreditLadder note "not many lenders take rent into account" in lending decisions.
- What actually matters here is **rent as genuine savings**. Some lenders accept 3–12 months of on-time rent on a *licensed agent's ledger* in lieu of savings, up to 95% LVR. Private and family leases are usually rejected.
- So the PM already holds the valuable artefact (the ledger). It costs nothing to produce and can't be sold to the renter, because of the Victorian fee ban.

**A3. Victorian law blocks charging renters directly. (High)**
- From 31 Mar 2026, rental providers, agents *and third-party platforms* may not charge renters fees for applications or rent payments (CAV; Tenants Victoria "Rental apps").
- That kills the RentPay / Rental Rewards model in Victoria. RentPay was about $0.6M revenue in FY24 with roughly 11.4k active users nationally, and Rent.com.au still loses about $3.7M a year.
- It also kills any tenant share of a maintenance fee. Repairs are the rental provider's duty under the RTA, and a renter-paid "maintenance subscription" invites a CAV infringement plus a reputational story.
- Anything the tenant pays for must be **genuinely optional, sold by a separate entity and not a condition of the tenancy**. In practice, every dollar of tenant-side revenue comes from third parties.

**A4. Trust: the agent works for the landlord. (High)**
- 65% of renters rent through an agent (CHOICE / Shelter / NATO, *Unsettled*). Renters' experience of agents is poor: only 20% of people trust agents (2013 poll, stale) and 76% of buyers and sellers don't fully trust them (Real Insurance 2025).
- Snug's "Match Score" drew a Guardian investigation over renters' data being used against them.
- The trust risk is specific: you know the renter's income, savings and buying plans from the standard application form. A renter will fear, rationally, that this shapes their next rent increase or renewal.
- **This is disqualifying unless engineered out:**
  - a separate entity and brand;
  - express opt-in (APP 7 direct marketing);
  - a hard information barrier so landlords and PMs never see engagement or finance data;
  - application data never used for marketing (APP 6 secondary use).

**A5. "Equity building" and "deposit pathways" are regulated financial services. (Med–High)**
- Holding savings is ADI territory. Pooled savings or investment products need an AFSL. Deposit loans and shared equity are credit (ACL) and capital-heavy: OwnHome raised $31M (2022, led by Square Peg with CBA's x15) and still takes a 1.1–2.2% premium.
- Meanwhile the state crowds out the market:
  - The 5% Deposit Scheme (First Home Guarantee) has had unlimited places, no income caps and a $950k Melbourne cap since 1 Oct 2025.
  - Victoria's first-home stamp duty exemption covers purchases up to $600k.
- A startup savings or deposit product cannot beat a free government guarantee. The value is in **navigating** these schemes, and that is mortgage broking.

**A6. Tenant LTV is short and leaks out of the corridor. (Med)**
- The average Victorian bond lasted about 2.2 years (AHURI, 2015–16 data).
- Inner-north houses cost $1.2–1.7M, well above the $950k cap. Renters who buy either buy a local unit ($520–620k, which fits both the stamp duty exemption and the guarantee) or move to the outer north or west.
- The relationship ends at settlement, unless they become a landlord.

**A7. Moving help is high-frequency but already monetised and commoditised. (Med)**
- Utility connection services pay agencies about $30–70 per connection (Movinghub via Property Tree: $70 electricity / $50 gas, 2019). Direct Connect and Snug integrate it.
- CHOICE warns renters about these services.
- An acquired agency almost certainly already books this income, so it isn't new revenue. Confirm in due diligence.

## Things the brief gets wrong, misses or understates
1. **"Rent history as credit evidence"**: wrong mechanism for Australia (see A2). Replace it with a "verified rental ledger for genuine savings plus a guarantee-scheme pathway".
2. **"Fee could be split between landlord and tenant"** (maintenance): conflicts with the RTA's allocation of repairs and with the 31 Mar 2026 fee ban. Treat it as **not viable**, not merely "restricted".
3. **The product list in my role brief:**
   - "Kasada" is a Sydney bot-defence cybersecurity company, not proptech. Drop it.
   - "Experian/Equifax rent reporting in AU": I found no evidence it exists.
   - Equifax's tenancy database (NTD) is negative-only *[unverified: from general knowledge]*.
   - Renter Resume and RentPay are Rent.com.au products.
4. **Missed: the 5% Deposit Scheme changes (1 Oct 2025).** This is the biggest tenant-side tailwind. For inner-north unit buyers, the guarantee plus the stamp duty exemption makes a 5% deposit (about $30k on a $600k unit) realistic. That is where the pull is.
5. **Missed: the tenant as a source of landlords.** Rentvesting is a recognised trend (Resolve's "57%" includes investment purchases), but investment purchases leave the corridor, which dilutes density.
6. **Understated: the privacy cliff.** The OAIC automated-decision transparency rules start **10 Dec 2026**. Taking broker commissions in exchange for tenant data is the "benefit for personal information" trigger that loses the small-business exemption, as round 1 found. Budget for full APP compliance from day one of any tenant-side product.
7. **Understated: s 48A.** It concerns rebates owed to the agent's *client* (the landlord). A broker referral commission on a *tenant* isn't obviously caught, but an agent getting paid by third parties on people its client brought in needs counsel. The NCCP referrer exemption requires disclosure of the benefit, no fee to the consumer, consent, and hand-off within 5 business days (MFAA guidance).

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| Renters who want to buy | 78% want to, 59% think it impossible | [verified: AHURI 2024 via search summaries] |
| Renters planning to buy within 2 years | 57% (up from 42%) | [verified: Resolve Finance Generation Rent; lender-commissioned] |
| Renters expecting to buy within 12 months | 13–19% | [verified: Westpac Jan 2025 13%; Agile 14%; Finder 19%] |
| Actual renter→owner transition | ~10%/yr (2013–16); 13.6% (2001–04); 18–24s 7.6% | [verified: HILDA 2018 report via Domain/Pursuit] |
| Melbourne-specific intention to buy | Not found | [unverified]: no Victorian breakdown located |
| Rent on AU credit files | Not reportable; landlord isn't a credit provider | [verified: Bright Law on Privacy Regs; OAIC Part IIIA]: confirm with counsel |
| Rent as genuine savings | Some lenders, 3–12 months, agent ledger, ≤95% LVR | [verified: RateCity, Home Loan Experts; lender policies vary] |
| 5% Deposit Scheme | Unlimited places, no income cap, Melbourne cap $950k from 1 Oct 2025 | [verified: Housing Australia; Nelson Alexander] |
| VIC first-home stamp duty | Nil ≤$600k, concession to $750k | [verified: Aussie, Austax; check SRO] |
| Victorian renter fee ban | Application and rent-payment fees banned, incl. third-party apps, from 31 Mar 2026 | [verified: CAV, Tenants Victoria] |
| RentPay scale | ~11.4k active users (early 2025); ~$0.6M revenue FY24; group loss ~$3.7M FY25 | [verified: ASX filings via OnlineMarketplaces, StockAnalysis] |
| US rent-reporting effect | +12pp have a score; no significant prime effect | [verified: Urban Institute/Esusu RCT via GlobeSt] |
| UK rent reporting | CreditLadder claims 200k+ tenants; Canopy £7.99/mo; few lenders use it | [verified: company claims; Finder UK] |
| OwnHome | $31M Series A 2022; 1.1–2.2% premium; no recent customer data | [verified: press; customer count unverified] |
| Victorian bond duration | ~2 years 2.5 months | [verified: AHURI brief, 2015–16 data; stale] |
| Renting via an agent | 65% | [verified: CHOICE Unsettled] |
| Utility referral to agency | ~$30–70 per connection | [verified: Elite Agent, MRI 2019; stale] |
| Broker commission | Upfront ~0.65–0.70% of drawn loan; trail ~0.15%; clawback 18–24 months | [verified: Mint Equity, MFAA] |
| Inner-north medians 2026 | Units ~$520–620k; houses ~$1.2–1.74M | [verified: Collings, Jellis Craig; sources conflict] |
| Tenant buyers per 1,000 managed homes | ~70–120/yr | [estimate: 10%/yr HILDA, higher-income inner-north renters, some multi-adult households] |

## Improvements (ranked by impact)
1. **Pick one priced tenant service: the "First Home Pathway".**
   - Offer: a free verified rental ledger and reference letter (the genuine-savings proof), a check against the guarantee scheme and stamp duty exemption, and a broker appointment.
   - Monetise through lender commission: run it as an ACL credit representative under an aggregator (about 80–90% of commission retained) or as a disclosed referrer (about 15–30% of commission) *[estimate]*.
   - Economics per 1,000 properties *[estimate]*: ~90 buyers/yr × 10–15% capture ≈ 9–14 loans × ~$540k × 0.65% ≈ $32–49k upfront, plus about $8k a year of trail per cohort, building up. That is **~$40–60 per property per year** at steady state. It's small, but it is pure margin on an existing touchpoint.
2. **Make the ledger and reference free and instant for every tenant.** It is the trust token: "we work for your landlord, but we'll give you the proof you need to leave and buy". It costs about nothing in PropertyMe. Never charge for it and never condition it on taking the broker.
3. **In-portfolio move-on.** When a tenant gives notice, offer priority on portfolio vacancies (portable bonds since 1 Jul 2026 per round 1). The pay-off is on the landlord side: shorter vacancy, a known-good tenant, and an earlier, coordinated notice. Measure it as landlord-side days vacant saved, not as tenant revenue.
4. **A sitting-tenant offer on landlord sales.** About 7–9% of a book sells each year (round 1). Offering the sitting tenant a disclosed, independently valued first look ties directly to the sales-independence edge. Volume is small (estimate 3–8 per 1,000 properties per year), but the vendor saves marketing and vacancy, and you keep the management if the buyer is an investor.
   - **Conflict:** you act for the vendor. The tenant must have their own advice, and the Sale of Land Act and underquoting rules apply. Get legal sign-off first.
5. **Information barrier by design.** Use a separate entity and brand, opt-in only, and never show the landlord or PM tenant finance data or engagement. Publish this barrier in the tenant pack, because it is the trust product.
6. **Drop the rest:** rent-reporting subscriptions, rewards cards, rent-to-own, savings or deposit wallets, tenant maintenance contributions and any "super app" tenant UI. Use SMS and email from the named PM.

## Tests & kill criteria

**6-week First Home Pathway test** (on a licensed partner's or the acquired agency's portfolio)
- **Sample:** all tenancies longer than 6 months with a clean ledger, about 300–400 households from a 400–500-property book. Randomise:
  - **A:** First Home Pathway offer;
  - **B:** move-on offer (priority on portfolio vacancies plus help with connections);
  - **C:** control (ledger available on request only).
- **Channel:** one SMS and one email from the *named PM*, plus one reminder in week 3. The offer carries the disclosure ("we may receive a commission from the broker; your landlord never sees this").
- **Pre-registered metrics:**
  1. Request rate for the ledger or pack (A vs C).
  2. Broker calls booked.
  3. Stated purchase horizon (≤12 months).
  4. Trust item: "I'm comfortable my rental agency offering this" (1–5).
  5. Opt-outs and complaints.
- **Pass (week 6):**
  - arm A request rate ≥8% and ≥3% booked broker calls (about 4–5 of 150);
  - opt-outs ≤2% and zero data-use complaints;
  - trust score ≥3.5.
- **Kill:** requests below 3%, or booked calls below 1%, or any complaint that the offer was linked to renewal or rent. Shelve the tenant side and keep only the free ledger.
- **Lagging gate (6 months):** at least 3 settled loans per 300 households contacted, and at least 25% of booked calls reaching pre-approval. Otherwise run it as a referral only, at zero build cost.
- **Arm B (secondary):** of the tenants who give notice in the window, at least 15% apply in-portfolio. Expect only about 15–25 notices, so treat the result as directional.
- **Cost:** a few days of founder time, plus partner and broker agreements. About $3–8k cash *[estimate]*.

**Pre-test legal check (1 week):** confirm s 48A, the NCCP referrer exemption, APP 6/7 and the small-business-exemption consequence. Kill if counsel says the commission must be rebated to the landlord.

## Answers to the round-2 questions in my domain
1. **Which services carry the economics:** none on the tenant side. Add the First Home Pathway third or fourth, after PM plus landlord services, and only if the test passes. The free ledger and in-portfolio move-on come first because they cut landlord-side cost.
2. **LTV per tenant relationship:** ~2.2-year tenancy × P(buy during tenancy) ~20% × capture 10–15% × ~$4.5–5k net present commission ≈ **$90–150 per tenancy**, or about $40–60 per property per year. Add about $40–80 per property per year in utility referrals, which is probably already in the acquired agency's numbers. It doesn't move the 2,000–2,500-property requirement.
3. **Regulation:**
   - **Tenant fees:** banned (RTA and the 31 Mar 2026 third-party ban).
   - **Credit assistance:** needs an ACL or credit-representative status, or a strict referrer exemption.
   - **Savings, deposit and "equity":** need an ADI, AFSL or ACL plus capital. Not viable.
   - **Rent reporting:** not legally available.
   - **Disqualifying conflict:** using application or finance data for marketing, or letting it touch rent and renewal decisions.
   - **Manageable conflict:** disclosed, opt-in broker referral behind a published information barrier.
4. **Autonomy frontier (tenant side):** the ledger and reference letter, scheme-eligibility checks and in-portfolio matching can be fully automated now. Anything that amounts to credit assistance or advice needs a human broker. Selecting applicants for in-portfolio moves stays human, given the Privacy ADM rules from 10 Dec 2026.
5. **Founder edge:**
   - **Decisive:** the statistical edge in *predicting who moves and who buys*. Ledger regularity, tenure, rent-to-income and household change predict notice timing, which improves landlord-side vacancy planning, and time the broker offer. Experiment design matters too.
   - **Irrelevant:** building consumer apps for renters. Renters won't install an agency app, and distribution is SMS from the PM.
6. **Smallest test:** the 6-week, 3-arm test above, about $5k, with pre-registered thresholds.

## Questions I'd hand to other specialists
- **Lawyer:**
  - Does s 48A reach third-party commissions earned on *tenants*?
  - Can an agency or affiliate be an ACL credit representative without a conflict under the Estate Agents Act and its Professional Conduct Regulations?
  - Is a sitting-tenant first look compatible with vendor duties and underquoting rules?
- **Privacy:** confirm the APP 6/7 position on using standard-form application data for any marketing, and the small-business-exemption trigger.
- **CFO / model:** what is the utility-referral income already in target agencies' P&L, and is it in the $1.86k per property?
- **Data / underwriting:** can ledger and tenure data predict notice-giving at 60–90 days with useful accuracy (AUC above about 0.7) on a real book?
- **Corridor analyst:** what share of inner-north renters who buy stay in the corridor (units) versus leave? Do rentvesting tenants buy within reach of the managed area?
- **Network access:** CBRE (Australian Renter Survey 2026) and The Adviser pages were blocked in this session. Read the CBRE survey for renter willingness to pay and the full Resolve data.
