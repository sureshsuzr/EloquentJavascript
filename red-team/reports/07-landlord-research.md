# Landlord Customer Researcher & Pre-sell Test Designer: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives-if.** Landlords do switch over service, and a quality-led offer with a named PM can win them. But four things in the brief work against it. The plan leads with "AI-native", which most Australians distrust. Most of the proposed guarantees attract the wrong properties. The corridor's pool of landlords who actually switch each year is small. And **the founder cannot legally sign, or even openly solicit, management authorities before a licensed entity exists.** That last point is the biggest issue. Gate 1 ("< $2k per signed management") cannot be tested honestly until a licence exists, either through a hired licensed officer in effective control (OIEC) or through a licensed partner. So securing the licence comes before any pre-sell.

## Attacks on the load-bearing assumptions (only those in your domain; evidence, severity High/Med/Low)

**A3 Acquisition: comparison-funnel cost well under roll purchase cost. Severity: High.**
- *The pool is smaller than it looks.* Industry rent-roll attrition is about 15–17% a year [verified: RED 2020 figure of 17.3% via Console blog; Elite Agent "typical 15%"]. Much of that is properties being sold, landlords self-managing, or owners moving back in, not switches to another agency. I estimate genuine agency-to-agency switches at **about 4–7% of managed stock per year** [estimate: attrition minus sale-driven exits, which are elevated in Victoria]. In a two-LGA corridor such as Merri-bek plus Darebin, with roughly 40k rental dwellings and about 30k of them agency-managed [estimate: 2021 Census, ~32–34% renting households], that gives **about 1,200–2,100 switch events a year**. To reach 50–100 signings in year one from switchers alone, the funnel would need 3–8% of them. That is plausible, but it is a ceiling. The funnel cannot get the founder to 750+ properties, which confirms the brief's view that acquisition is the main growth channel.
- *Switching is cheap for landlords, but they put it off.* Landlords "take less than two weeks to research a PM" [verified: REA survey via Elite Agent; REIQ says 63% spend about two weeks]. Victorian authorities usually carry 28–30 days' notice [verified: agency guides; contractual, not statutory]. Trade press now runs headlines like "Switching PMs takes one email" [verified: REB 2026]. The barrier is inertia, not cost. So the funnel has to catch landlords at a **trigger event**: a vacancy, a bad maintenance bill, their PM leaving, a rent review, or a new purchase. Interception at those moments beats persuasion.
- *The highest-intent segment is not switchers at all.* New investor purchasers are. Victoria led investor lending growth at +12.9% in the year to Sep 2025 [verified: SPI/ABS], and investors took 40.6% of national new mortgage lending value in Sep 2025 [verified: Cotality via SPI]. Every settlement needs a PM. Buyer's agents, mortgage brokers, conveyancers and accountants all sit upstream of that decision, and none of them is a comparison site.

**A4 Retention: acquired managements survive an AI-led service. Severity: Med–High.**
- Only 36% of Australians are willing to trust AI, and only 30% think its benefits outweigh the risks, the lowest of 47 countries [verified: University of Melbourne/KPMG 2025, n=48,340]. Landlords are mostly aged 40–65, a group that skews further against AI [estimate]. Telling a bought roll "we're now AI-led" hands the landlord a reason to leave in exactly the window when leaving is easiest, just after the notice of transfer.
- :Different's landlord reviews centre on unreachable staff and a sense that "cheap means no one owns it" [partly verified: ProductReview listing; review content only partly visible]. Its failure taught landlords what "tech PM" means, and that memory has not gone away.
- The fix: AI stays invisible to landlords. Market the service on a named PM, response time and transparency. If tenants and landlords sense they are talking to software, retention falls [estimate].

**A1 Cost to serve. Severity: Med (my lane: demand side).**
Landlord demand for contact limits PM leverage. REIQ found 53% of landlords expect contact at least monthly [verified: REIQ]. At 300 properties per PM, that is about 160 relationship touches a month per PM before any exceptions. It is doable if most touches are proactive AI-drafted updates sent under the PM's name. If landlords expect live calls, it is not.

## Things the brief gets wrong, misses or understates
1. **The licensing order is missing.** Under the Estate Agents Act 1980 (Vic), a person must not act as an estate agent unless licensed: up to 12 months' jail or 500 penalty units for an individual [verified: CAV penalties table, s 12]. The definition covers people who carry on, or *advertise or hold out* that they will carry on, agency work, which includes leasing and collecting rent [partly verified: secondary summaries of s 4; primary text not retrievable here]. An unlicensed entity's authority is unenforceable and it cannot hold trust money [estimate based on standard regime; confirm with counsel]. To be licensed, the founder personally needs at least one year full-time as an agent's representative in the last three years, plus the prescribed course [verified: CAV via search]. So the founder cannot be the licensee in 2026–27. A company licence needs an **OIEC who holds an individual licence**, one OIEC per company, and a licensed agent in charge of each office [verified: ABLIS/CAV via search; whether the OIEC must be a director is unverified]. *Hiring or partnering with an OIEC is the first step, not an "open item".*
2. **Time-sensitive: agents' representatives need direct individual registration from 25 Nov 2026** [verified: CAV "New rules" page]. Every PM hire, and possibly field inspectors depending on what they do, must be registered or employed under the new regime. Ask counsel whether condition-report-only field staff count as doing agency work.
3. **Most guarantees create adverse selection** (see Improvements #2). Landlords who value a days-to-lease guarantee have hard-to-lease properties or unrealistic rents. Those who value an arrears guarantee have marginal tenants. A maintenance-cost cap attracts old housing stock. Existing AU guarantees, such as "no management fee for 3 months if not leased in 3 weeks" (PM WA) or rent paid from day 15 (Coral Sea, Qld), come from small operators who can screen each listing by hand [verified: agency pages; currency unverified].
4. **The comparison channel collides with LAF.** LocalAgentFinder already runs a national PM comparison with fees, rental history and reviews, paid by agents on a success fee [verified: LAF site]. The founder's comparison would compete with his former company for the same landlord searches and on the same SEO terms. Check for any restraint or confidentiality obligations, and expect agents who appear on LAF to view a disclosed own-brand comparison as hostile. ACCC disclosure obligations under the ACL (misleading conduct) apply whenever the operator ranks itself [estimate; brief already flags].
5. **The landlord base is shrinking while investor buying recovers.** Active Victorian bonds were 655,626 at June 2025, down 1.5% year on year, after falling 3.6% in the year to Sep 2024 [verified: Homes Victoria Rental Report]. Land tax now starts at a $50k threshold (since Jan 2024) [verified: secondary]. Net new investor lending is rising in Victoria, so the churn is turnover between owners, not only exit. That is good for the referral-on-sale thesis and the new-purchase funnel, and bad for roll attrition.
6. **Gate 3 (half of selling landlords sell through the founder) is untested and probably optimistic.** Selling landlords often go to the agency already managing the property, or to a family or friend contact. Nothing in the public evidence supports 50%. Track intent to sell in the pre-sell (below) and set the gate from that data.

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| VIC avg mgmt fee ~5.1% (FY22) | Current guides show Melbourne at ~5.5–6% plus 1–2 weeks letting fee; LAF's national avg is ~7.5% (incl. GST, different basis) | [unverified primary; secondary guides: YourPropertyGuide, LAF]; 5.1% looks low or stale for 2026 |
| Revenue ~$2.0k/property/yr | $580/wk median (Dec 2025) × 52 × 5.5% ≈ $1,660 mgmt + ~0.7 wks letting/yr (~$400) + admin fees ≈ $2.0–2.2k | [estimate; median rent from WhichRealEstateAgent, unverified] |
| Rent-roll attrition | 15–17% p.a. | [verified: RED 2020 via Console; Elite Agent] |
| Active bond decline ~25k (year to Sep 2024) | 677,492 → 652,766 (−24,726, −3.6%); June 2025: 655,626 (−1.5% y/y) | [verified: Homes Victoria] |
| Landlords who self-manage | 14–33% depending on survey and year | [verified: REA 2016 (86% use PM); REA 2020 (33% self-manage); IBISWorld 2017 (~25%)]; no current figure |
| Investors with one property | ~72% (1.623M of ~2.26M) | [verified: ATO Tax Stats 2022–23 Table 8, plus Firstlinks] |
| AI trust | 36% willing to trust; 30% say benefits > risks (lowest of 47 countries) | [verified: Univ. Melbourne/KPMG 2025] |
| Landlord research time | < 2 weeks; 63% around two weeks | [verified: REA via Elite Agent; REIQ] |
| Contact expectation | 53% expect monthly contact | [verified: REIQ] |
| Authority notice period | Typically 28–30 days (contractual) | [verified: agency guides; not statutory] |
| Unlicensed agency penalty | 12 months or 500 penalty units (individual) | [verified: CAV, s 12] |
| PM flat-fee scale precedent | Queensland PM reached 400 PUM on a flat fee (June 2026) | [verified: REB headline; paywalled detail] |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Secure the licence first, and structure the pre-sell around it.** Two legal routes exist:
   - **(a) Own company licence with a hired OIEC.** Recruit a senior licensed PM, ideally the first career PM, as OIEC and an equity partner. This takes about 2–4 months including BLA processing [estimate]. Authorities are signed in the founder's company name from day one. This is the preferred route.
   - **(b) Licensed partner agency for the pilot.** A small corridor agency signs the authorities, holds trust money and carries the licence. The founder's company supplies the back office under a services agreement. A pre-agreed right to buy the roll at a fixed multiple runs from the founder's licensing date. Landlords must be told who their agent is. On a roll sale, each landlord is notified and may leave, so expect some loss [estimate].
   - **(c) Not allowed:** advertising "we manage your property" or collecting authorities in an unlicensed entity's name. An unpaid research waitlist ("register interest; we are not yet licensed and cannot act for you") is lower risk, but it measures intent, not conversion. Discount its results by 50–70%.

   Get written advice from a Victorian property lawyer on s 4 "holding out" before any public ad.
2. **Change the guarantees so they reward good behaviour, not bad properties.**
   - *Keep* guarantees the agency controls: landlord reply within 4 business hours (fee credit if missed); maintenance approved with quotes, no markups and no admin-fee padding; statements and EOFY pack on time; **no lock-in (leave on 30 days' notice, no exit fee)**.
   - *Make conditional* any days-to-lease guarantee: it applies only if the landlord accepts the agency's rent recommendation and the presentation checklist. Otherwise it invites overpriced listings.
   - *Do not offer* arrears or maintenance-cost guarantees. Offer landlord-insurance referral instead. If an arrears guarantee is offered, price it as insurance.
   - Screen intake with a property-quality score, rejecting very old stock and properties with active tribunal (VCAT) disputes. Report the score mix as a go/no-go metric.
3. **Drop "AI-native" from landlord-facing copy.** Lead with "your named PM, 4-hour reply, every number visible". Keep AI for investors, lenders and recruiting. Test this explicitly (Tests, T3).
4. **Ideal customer profile (ICP).** Owners of 1–3 properties (72% of investors own one), aged 35–65, in professional jobs, either living 30+ km away/interstate/overseas or recently purchased. Houses and townhouses where rent is ≥ $550/wk (higher fee per touch). Avoid: the cheapest studio and older apartment stock (low fee, high exceptions), properties with live VCAT disputes, and portfolios of 10+ properties (they negotiate fees down and leave as a block). Secondary: owners in investor-heavy owners corporations, which ties in with the strata thesis.
5. **Make introducers the main channel, with comparison second.** These are buyer's agents, mortgage brokers, accountants (who see rental schedules) and conveyancers. Pay disclosed referral fees ($200–400 per signed management [estimate]) or offer reciprocal referrals. A comparison site is slower SEO capital and conflicts with LAF.
6. **Run a "free PM audit" lead magnet.** Compare the landlord's rent against the market, total fees, and maintenance markups from their own statements, plus a mystery-shop result on their current PM. This uses the founder's LAF skills, catches trigger events, and gathers comparison data.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

**Pre-sell test: one corridor (suggest Brunswick–Coburg–Preston–Reservoir, Merri-bek plus Darebin; investor-heavy, house and townhouse mix, inside 15 km for dense routing).**

- **Preconditions (weeks −8 to 0):** licence route (a) or (b) in place; written legal sign-off on all copy; PropertyMe (or a Crossub back office) live; one career PM hired (OIEC or registered agent's representative).
- **Target lists:**
  - (1) Google Search intent terms: "property manager [suburb]", "change property manager", "property management fees Melbourne".
  - (2) Meta audiences aged 35–65 interested in investing/property, geo-fenced to Melbourne and interstate capitals.
  - (3) 20 introducers: 8 buyer's agents active in the corridor, 6 brokers, 6 accountants.
  - (4) Owners-corporation investor-owner mail-outs only where lawful. Note: privacy restrictions on using OC registers [unverified; confirm with counsel].
  - (5) Current corridor rental listings that are stale (> 21 days on market), with the free audit offered via the listing agent channel. Contact only by lawful means; owner contact details are usually unavailable.
- **Offer:**
  - 5.5% + GST management fee, 1 week's letting fee, no lock-in.
  - A named PM with a 4-hour reply guarantee and $50 fee credit per miss.
  - No maintenance markup; a full switch handled for the landlord.
  - Month 1 fee waived for switchers.
- **Script (discovery call, 20 min):** current PM and fee → last problem and how it was handled → vacancy days and rent vs our estimate → "what would make you move this month?" → audit result → offer → book signing. Record the trigger and objection codes for every call.
- **Sample size:** at least 30 signed authorities, enough to estimate a ~10% close rate within roughly ±4 points and cost per signed authority within about ±30% [estimate]. That needs about 300 qualified leads.
- **Duration:** 12 weeks of active acquisition, then 90 days to track transfer completion and early churn.
- **Budget [estimate]:**
  - Media $15–25k (search CPC about $8–20; cost per qualified lead about $50–80).
  - Introducer fees about $5k.
  - Pro-rata PM and founder sales time about $25k.
  - Legal $5–10k.
  - **Total about $50–65k.**
- **Metrics:**
  - Conversion at each stage: click→lead, lead→qualified, qualified→call, call→proposal, proposal→signed, signed→transferred, transferred→retained at 90 days.
  - **Fully loaded cost per signed authority** (media + fees + labour).
  - Cost per *transferred* management.
  - Results split by source (switcher, new purchase, self-manager).
  - Share of signed properties passing the quality score.
  - Share of signed landlords intending to sell within 24 months (feeds Gate 3).
  - Landlord contacts per property per month in the first 90 days (feeds A1).

**Go/no-go:**
| Result | Meaning |
|---|---|
| ≥ 30 signed, fully loaded cost ≤ $2k per transferred management, ≥ 85% transfer, ≥ 75% pass quality score | **Go**: funnel is a real channel; fund scale-up |
| $2–4k, or < 30 signed but quality is high | **Iterate**: shift spend to introducers; re-test for 8 weeks |
| > $4k, or < 70% quality pass (guarantees drawing junk), or 90-day churn > 10% | **No-go on funnel**: treat acquisition as the only growth engine; drop guarantees except the service-level guarantees (SLAs) |

**Side tests (in parallel, same budget):**
- **T2, guarantees:** A/B a conditional days-to-lease guarantee against SLAs only. Kill the lease guarantee if it lifts sign-ups by < 20% or lowers the quality-pass rate by > 10 points.
- **T3, AI framing:** A/B "AI-native agency" against "named PM, 4-hour reply". Drop AI copy if it converts ≥ 15% worse (relative).
- **T4, retention proxy (2 weeks, about $2k):** survey 150 landlords via a panel with this question: "Your agency is bought and now uses AI for routine tasks, with your PM unchanged. Would you stay, review, or leave?" Kill the "AI-led" retention story if more than 25% say "leave or review".

## Answers to open items in my domain
- **Pre-sell design:** above. It cannot legally begin before a licensed entity (own OIEC or partner) is in place. A legal "register interest" waitlist can run now as a research signal only.
- **Signing real authorities pre-licence:** You cannot do this in your own name. Either hire an OIEC and license the company (preferred), or pilot under a licensed partner with a roll-purchase option. Do not collect authorities in an unlicensed entity's name or advertise management services before licensing.
- **Kill criteria (customer side):** fully loaded funnel cost > $4k per transferred management after 20 weeks; 90-day churn > 10% on acquired or switched managements; more than 25% intent to leave when told about the AI-led service; guarantee-driven intake failing the quality screen at > 30%.

## Questions I'd hand to other specialists
1. **Legal/regulatory:** Exact s 4 "holding out" boundary for waitlists and comparison sites. Does an OIEC need to be a director? Do condition-report-only inspectors need registration after 25 Nov 2026? What notification and consent does a landlord need on a partner-to-founder roll transfer? How must a self-ranked comparison be disclosed?
2. **Unit economics:** Rerun the model with fee 5.5–6% (not 5.1%), 4–7% annual switch pool, introducer fees, and 15–17% attrition. What attrition rate breaks the debt-service ratio (DSCR) on a 70% LVR roll loan?
3. **Acquisitions:** What retention clawbacks are typical when the buyer's service model differs from the vendor's? Can the 10–20% retention be lifted to cover a 6-month window?
4. **Founder/legal:** Any LAF restraint, non-solicit or confidentiality obligations that affect a competing PM comparison?
5. **Ops:** Can 300 properties per PM sustain 53% of landlords expecting monthly contact? What share of touches can be proactive and AI-drafted without hurting retention?
6. **Strata:** Can owners-corporation investor-owner lists be used lawfully for marketing (Privacy Act/OC Act)?
