# Comparison-Marketplace Growth Lead: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Fatal as specified. Survives only if the funnel stops being a comparison site.** An honest comparison of local PMs in one corridor sends most of its leads to competitors. Unless they pay referral fees, and they have every reason not to fund a rival operator, the founder's own cost per signed management is roughly paid-media cost ÷ self-selection rate. My estimate is ~$4–8k fully loaded, which is no cheaper than buying a roll. The volume is also small: a corridor has a few hundred PM-intent searches a month at most. Biggest issue: **the funnel's economics only worked at LAF because LAF was neutral and was paid by every agent. Owning an agency kills both conditions.** Recommended single channel: **point-of-purchase referrals**, meaning new investor landlords captured at settlement through sales agents, buyers' agents and brokers, paid in reciprocal sale referrals plus a disclosed per-signing fee.

## Attacks on the load-bearing assumptions (only those in your domain; evidence, severity High/Med/Low)

**A3.1 Self-preferencing destroys the funnel's unit economics. Severity: High.**
LAF and OpenAgent make money because every agent in the market pays a success fee on referred business. OpenAgent charges 20–30% of commission on sales [verified: openagent.com.au via search summary]. LAF says PMs pay a pay-on-success fee when they win a listing [verified: localagentfinder.com.au pages via search summary]. Once the founder's agency is one of the options:
- (a) Rival PMs won't join a marketplace run by a competitor that holds their response-time data and their leads. Revenue from referring landlords elsewhere goes close to zero, so every lead that doesn't pick the founder is pure cost.
- (b) If the ranking is honest, the founder's new agency, with no reviews, no track record and no local "rent achieved", will rarely rank first. I estimate it gets chosen 10–25% of the time [estimate: new entrant against 5–8 established options per corridor].
- (c) If the ranking is tilted, the ACCC's precedent is Trivago: $44.7M in penalties for presenting paid-for ranking as cheapest/best [verified: ACCC media release, April 2022]. Disclosure alone doesn't cure a ranking that misleads about why it is ordered the way it is.

Arithmetic: CPC $10–18 [estimate: high-LTV local service, agents bid; no AU PM-specific CPC published, real estate generally $4–15, verified only as agency-marketing figures] × landing→lead 6–10% → CPL $120–250. Lead→appraisal 50%, appraisal→signed 25–35% for switchers → **$1.2–2.0k per signing that goes to anyone**. Divide by the 10–25% share that picks the founder: **$5–15k paid media per own signing**. Then add BDM labour and the comparison data cost. Gate 1 fails on paper before launch.

**A3.2 Not enough volume in a single corridor. Severity: High.**
Victoria has ~745k active bonds [verified: PAEC budget estimates hearing, May 2026]. A 10–15 suburb Melbourne corridor holds roughly 30–50k bonds [estimate: ~5–7% of the state]. About 80–85% are agent-managed [verified only as 2016 REA survey, 84% engage an agent; stale]. Landlords who actively switch PM each year: ~6–10% [estimate: industry anecdote, no AU published figure found]. That gives ~2–4k switch decisions a year in the corridor, plus new investor purchases. Most of those decisions never touch Google: they come from word of mouth, the selling agent, or the incumbent's own sales team. Search demand: "property manager [suburb]" runs at ~10–70 searches/month per suburb [estimate: typical long-tail local-service volume; check in Keyword Planner in week 1]. That is ~300–800/month across the corridor, and LAF, OpenAgent-style pages, REA/Domain agent finders and the incumbents' own ads already contest it. Even at a perfect $2k, paid search caps out at about 3–8 own signings a month. The plan needs ~1,000 properties.

**A3.3 "Rent achieved" and response-time data can't be sourced legally and defensibly at corridor scale. Severity: Med-High.**
- *Rent achieved*: no public source by agency exists. RTBA/DFFH publish by suburb, not by agent [verified: RTBA reporting is aggregate]. Listing data gives **asking** rent, not achieved rent. Labelling asking rent as "achieved" is a misleading-claim risk.
- *Listing data*: scraping REA/Domain is a ToS breach. I couldn't retrieve REA's live clause, so its exact wording is [unverified]. Domain's API gives full listing details only with **agency authorisation** [verified: developer.domain.com.au], so it is no use for building competitor data. A third-party summary says the Domain API terms also bar storage outside Australia [unverified: 13Labs, July 2026]. Licensed Cotality/PropTrack feeds are the clean route but cost tens of thousands a year [unverified; get a quote].
- *Mystery shop*: a corridor has ~40–80 agencies doing PM. A credible panel is 3 contacts per agency per quarter = ~240–480 shops a year at $40–80 each [estimate: casual researcher time] → **$10–35k/yr**. Feasible, but it is a content cost, not a moat.

**A3.4 Funnel-acquired managements are lower quality than the brief assumes. Severity: Med.**
Switchers self-select for complaint-proneness and for switching again. They arrive mid-lease with legacy issues such as arrears, maintenance backlog and missing condition reports. That means higher onboarding exceptions, which hurts assumption 1 directly. A purchased roll arrives as a cohort with known tenure history and a retention clawback (10–20% retained). A funnel signing has no clawback.

**A3.5 Comparison against roll cost is set up wrongly. Severity: Med.**
The brief's own numbers give $2.0k × 3.70 = **$7.4k** per management, not $5–7k. More importantly, roll purchases are ~70% debt-funded, so the *equity* cost per roll management is ~$2.2k plus debt service. A $2k all-equity, fully expensed funnel signing is therefore not "well under" roll cost on a cash-equity basis. It only wins if it is ≲$1k or if debt capacity is the binding constraint. Gate 1's threshold should be set against equity per acquired management, not headline multiple.

## Things the brief gets wrong, misses or understates
1. **Licensing blocks the gate test.** You can't hold management authorities in Victoria without a licensed estate agent in effective control. The founder "does not yet have a licensed operator partner". So Gate 1 can't measure *signed* managements until that is solved. Options: sign under a licensed partner agency as a co-brand, or test with signed letters of intent. LOIs overstate conversion by ~2x [estimate].
2. **Ex-CEO of LAF building a competing PM comparison** raises restraint, confidentiality and reputational questions. LAF already has suburb-level PM comparison pages in Melbourne, e.g. Kew [verified: localagentfinder.com.au]. The founder would be outbidding his old company for its own keywords. Check the separation deed.
3. **Attrition data is stale and points the wrong way now.** "Active bonds fell ~25k to Sep 2024" was true then. Bonds were 732k at June 2024 [verified: REIV/RTBA] and are 745k+ by May 2026 [verified: PAEC transcript]. The investor sell-off has stabilised in count, which reduces "orphaned landlord" flow from sales.
4. **Sales-agency reciprocity is missing.** The brief's later-life earner, referring landlords' sales to agents, is also the best *acquisition* currency. Sales agents meet every investor buyer and many sales-only boutiques lose that landlord to a rival PM department. Trading "I send you my landlords' sales" for "you send me your investor buyers" is a channel nobody else in the corridor can offer, because incumbents with PM departments keep both sides.
5. **Google AI Overviews and LLM answer engines** (time-sensitive, 2026) are eroding organic CTR on "best property manager [suburb]" queries. Comparison SEO built now is building on a shrinking surface.
6. **Referral-fee disclosure** under the Estate Agents Act (Vic) and Professional Conduct Regulations applies both ways. Paying sales agents per referral and taking sale-referral fees both need written disclosure to the landlord [unverified: confirm section with a Vic property lawyer].

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| Roll cost ~$5–7k/management | $2.0k × 3.70 = $7.4k; equity at 70% LVR ≈ $2.2k | [estimate: brief's own inputs] |
| Victorian active bonds fell ~25k (yr to Sep 2024) | Plausible then; now 745k+ (May 2026), up from 732,125 (Jun 2024) | [verified: RTBA via REIV; PAEC 2026-27 hearing] |
| Comparison sites earn from agent success fees | OpenAgent 20–30% of commission (sales); LAF pay-on-success from PMs | [verified: company sites via search] |
| Self-preferencing/paid ranking legal risk | Trivago $44.7M penalty, 2022 | [verified: ACCC media release] |
| Listing data obtainable via API | Domain full listing detail needs agency authorisation | [verified: developer.domain.com.au] |
| REA ToS prohibits scraping | Likely; live clause not retrieved | [unverified] |
| Landlords using an agent | 84% (2016 REA survey) | [verified but stale] |
| AU PM-specific CPC | None published; RE generally $4–15 CPC, $80–250 CPA | [unverified: agency marketing pages]; my working figure $10–18 [estimate] |
| Title search cost for owner letters | Folio search ~$8.30 (2026-27), plus address-lookup fee | [verified: LANDATA 2026-27 charges via secondary source]; direct-marketing restrictions [unverified] |
| Corridor search volume | ~300–800 PM-intent searches/month | [estimate: Keyword Planner check in week 1] |

## Improvements (concrete changes to the plan, ranked by impact)
1. **Replace the comparison funnel with one channel: point-of-purchase referrals.** Target investors buying in the corridor, captured before they've chosen a PM, so there's no incumbent to break. Partners are sales-only agencies and agencies with weak PM desks (primary), buyers' agents and investor-focused brokers (secondary). Currency:
   - (a) A disclosed per-signing fee of $300–600 [estimate: below BDM cost per signing].
   - (b) Reciprocity: the founder's sale-referral flow goes to partner agents. This is LAF embedded in relationships, used as a *buying* currency.

   Target cost per signed: $800–1,500 all-in.
2. **Off-the-plan settlement bundles as the density accelerant.** One completion of 40–150 units in the corridor, won through the developer or selling agent, gives a dense cluster in one building with new stock and low early maintenance. Pitch it as a tender with guarantees on days to lease. One win can equal six months of funnel output.
3. **Demote the comparison content to a trust asset, not a channel.** Publish a quarterly, methodologically transparent mystery-shop of response times across corridor agencies, with the founder's agency *excluded or scored by a third party*. Use it in PR and partner pitches, never as a ranked chooser. Budget ≤$10k/yr. This removes the ACCC ranking risk and keeps the founder's distinctive LAF credibility.
4. **Triggered direct mail, not blanket mail.** Write only to owners of corridor rentals showing a pain signal observed manually, not scraped: re-listed 2+ times, or 28+ days on market. Offer a guarantee-led switch ("leased in 21 days or first 3 months' fees waived"). Blanket owner mail at 0.5–1% response × 25% close × ~$12/letter (title + print + post) ≈ **$5–10k per signing** [estimate]. It is not worth it untriggered.
5. **Reframe Gate 1** as "fully loaded cost per signed management ≤ 50% of equity cost per roll management (~$1.1k), at ≥10 signings/month run-rate". A $2k gate at 3/month proves nothing about scale.
6. **Include BDM labour and onboarding in cost per signed.** A corridor BDM costs ~$110–140k plus ~$300–500 commission per signing [estimate]. At 8–12 signings/month that is $900–1,400 per signing before media.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

**Prerequisite (weeks 0–3):** a co-branded management agreement with a licensed partner agency so real authorities can be signed (or Crossub-backed partner). Without it every number below is LOI-inflated.

**90-day plan, total ~$75k cash plus founder time:**

| # | Experiment | Budget | Metric | Pass / kill (day 90) |
|---|---|---|---|---|
| 1 (primary) | Recruit 12–15 referral partners (sales-only agents, 4 buyers' agents, 3 investor brokers); disclosed $500 per signing plus reciprocal sale referrals | $15k fees + $25k part-time BDM | Signed managements; cost per signing; signings per active partner per month | Pass: ≥25 signed, ≤$1.5k fully loaded, ≥5 partners producing. Kill: <10 signed or <3 producing partners |
| 2 | Off-the-plan pitch to 3 developers/project marketers with completions in the next 12 months | $5k (collateral, guarantee modelling) | Shortlisted or awarded buildings | Pass: 1 award or shortlisting ≥40 lots. Kill: zero shortlists after 3 pitches → drop |
| 3 | Paid search control: own-brand landing page (not comparison), corridor PM keywords | $10k | True CPC, CPL, cost per appraisal, cost per signing | Kill the paid channel if CPL >$200 or cost per signing >$2.5k. Expected: kill |
| 4 | Triggered letters to 500 owners of stale or re-listed corridor rentals, guarantee offer | $7k | Response rate, signings | Pass: ≥2% response, ≥4 signings. Kill: <1% |
| 5 | Mystery-shop panel, 30 agencies × 2 contacts, published as a report and used in partner pitches | $5k | Partner meeting acceptance rate with vs without report | Keep if acceptance lifts ≥30%; otherwise drop |
| 6 | Measure the self-preferencing effect directly: show 100 leads a disclosed 3-option shortlist including the founder | $3k | Share choosing founder | If <30%, the comparison funnel is permanently dead for own-agency acquisition |

**Overall kill criterion for assumption 3:** at day 90, if no channel delivers ≥10 signings/month at ≤$1.5k fully loaded on a trend line, treat organic acquisition as immaterial. Plan the business as roll acquisition plus retention, and size the debt plan accordingly.

## Answers to open items in my domain
- **Pre-sell test design for one corridor:** run experiments 1, 4 and 6 above, under a licensed partner's authority. Pre-sell should mean *signed* authorities with a 60-day cooling clause, not LOIs. Track the source of every signing in PropertyMe from day one.
- **Funnel vs roll acquisition (unit-economics input):** use funnel ≈ $1.0–1.5k per management (referral channel, if it passes), versus roll ≈ $7.4k headline / ~$2.2k equity. Funnel managements also carry higher 12-month churn (assume 15–20% vs 8–12% for a well-run roll [estimate]) and zero clawback. Model payback on equity, not headline.
- **Kill criteria (acquisition):** as above. Also kill the comparison site outright if experiment 6 shows <30% self-selection.
- **Channel (the :Different lesson):** one channel: point-of-purchase referrals via sales agents, with off-the-plan bundles as an occasional lumpy upside of the same relationships. Paid search, comparison and mail are not run as channels after day 90.

## Questions I'd hand to other specialists
1. **Legal/regulatory:** does the founder's LAF separation deed restrict a PM comparison product? What exactly do the Estate Agents Act and Regs require for disclosing per-referral payments both ways? Are there restrictions on using LANDATA title results for direct marketing?
2. **Licensing/operator:** can signings be made under a co-brand with a licensed partner, with authorities assignable to the founder's entity later without landlord re-consent?
3. **M&A/rent roll:** what is the realistic equity per management after LVR, clawback and transaction costs? This sets the true bar for Gate 1.
4. **Operations:** how many exceptions per 100 does a mid-lease switcher add in month 1–3, compared with a roll cohort or a new-purchase landlord?
5. **Retention:** does a landlord acquired at purchase via a sales agent retain better than a switcher? This decides whether reciprocity is a moat or just a cheap source.
6. **Data/finance:** what are quotes for licensed corridor listing feeds (Cotality, PropTrack) if a data product is ever built?
