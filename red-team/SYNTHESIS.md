# Red-team synthesis: AI-native PM agency, Melbourne

13 independent agents, 2 Nov 2026. Reports in `reports/`, model in `models/unit_economics.py`. Figures are the agents' and carry their labels (verified / estimate / unverified) in the source reports. Many Victorian government and legislation sites were blocked from the session, so legal points rest on search summaries: **get a Victorian property lawyer to confirm s 48A, licensing timing and guarantee structure before acting.**

## Overall verdict

**Not fatal, but the plan as written doesn't reach its goal.** The brief's maths converts pre-tax operating margin into founder income and ignores churn replacement, debt amortisation, tax and fixed costs. Corrected, the operator needs roughly **2–3x the scale** the brief assumes (CFO: ~2,000–2,500 properties for a $500k draw at 3x productivity), and debt-funded rolls build equity rather than income for 5–8 years.

What survives is narrower and, arguably, better:
**buy a licensed agency → run it as a sales-independent PM specialist → prove cost-to-serve on real books → grow through point-of-purchase investor referrals and selective rolls.** The comparison site, strata, aggressive guarantees and the referral fee as currently designed should be cut or redesigned.

## The four load-bearing assumptions: scorecard

| # | Assumption | Verdict | Why (agents) |
|---|---|---|---|
| 1 | 3x+ properties per relationship PM | **Weakened** | Most of 3x is role split, not AI; AI alone ≈1.5–2x (04, 05). Per total staff ≈1.2–1.6x (04). At 3x direct cost ≈ incumbent ($1,017 vs $1,014); only 4x gives an edge (~$80) (01). Tenancy-care, leasing and arrears/VCAT roles must be added (04, 10). |
| 2 | Cost gap lasts | **Weak** | Benchmark is an offshore-VA incumbent at ~$430–580/property, not $75k/130 (06). Vendors (PropertyMe agentic AiMe, MRI, Ailo) ship role redesign to everyone: 12–24-month window, not 3–5 years (05, 06). |
| 3 | Funnel CAC ≪ roll cost | **Fails as specified** | Own-agency comparison site: honest ranking picks you ~10–25% → $5–15k/signing; corridor search demand ~300–800/mo; data unsourceable; ACCC/defamation exposure; competes with LAF (08, 03, 06). Real switching pool only ~4–7% of stock/yr (07). |
| 4 | Acquired managements survive | **Survives if slow** | Hard switch ≈66% kept at 12 months; soft landing (brand + vendor PM + fee unchanged 12 months) ≈80%; plus earn-out/stay bonus ≈84% (09). Losses hit in months 3–9, after 3-month holdbacks (09, 10). |

## Where the agents converge (high confidence: 3+ agents independently)

1. **The numbers in the brief are on the wrong base.** The ~3.7x multiple applies to *management commission* (~$1,132–1,429/property), not ~$2.0k gross; fees are quoted incl. GST; current Melbourne multiples are ~2.8–3.5x → **~$4.7–6.1k per management** (01, 02, 06, 11). Revenue ≈ $1.86k/property ex-GST (01, 13).
2. **Churn × replacement cost is the master variable**, ahead of PM productivity (01 ranks productivity ~5th). With no sales team refilling the book, replacing ~10–14%/yr is a permanent cost: ~$840/property/yr if refilled with rolls, ~$240 via a $2k funnel (09); ~$360k/yr per 1,000 properties (01). The "arbitrage" partly runs in reverse: sales agencies pay ~$7k because their listings refill the roll; you'd pay that without the refill (09, 02, 06).
3. **Debt-funded rolls don't pay the founder.** "Half debt-funded, 1,150 properties" → founder salary capacity ≈ −$296k (01), ~$40k (11) or ~$300k (02) depending on loan term and assumptions. Every agent agrees it is well short of $500k. Loan term matters more than rate. LVR covenants can breach in year 1 from churn plus multiple compression alone (01, 02). NAB wants 100+ properties under management already; bank valuation below price → effective LVR ~55–60% (02, 11).
4. **Licensing comes first.** The founder can't sign or advertise management before licensing (s 12, Estate Agents Act). An own licence needs 12 months as a representative → ~Q4 2027 at earliest. A real full-time officer in effective control, or buying a licensed agency, is the first step. From **25 Nov 2026** every representative, including field inspectors, must register individually and do CPD (03, 07, 11).
5. **The referral fee is legally exposed.** s 48A likely requires rebates/commissions to pass to the client; disclosure alone isn't enough; it may also forfeit the Privacy Act small-business exemption. **Model it at $0** until senior counsel advises; restructure as a separate agent-selection engagement with express consent and partial rebate (03, 10). Commercially it is also small: ~$75/property/yr (01), and capture is 10–35%, not 50% (07, 09).
6. **Guarantees mostly attract the wrong properties.** Days-to-lease attracts overpricing (and conflicts with the ban on accepting offers above advertised rent); arrears attracts weak tenants and a lost-rent guarantee may be insurance needing APRA authorisation; a maintenance cap attracts old stock. Keep controllable process guarantees (response time, no markups, no lock-in) backed by fee refunds (03, 07).
7. **Don't sell "AI".** Only 36% of Australians trust AI (Uni Melb/KPMG 2025). Lead with a named PM, reply time and fee transparency; keep the AI invisible, especially on acquired rolls (07, 10, 09).
8. **Strata: avoid as a wedge.** ~$80–130 profit per lot vs $600–700 per rental; Victoria deferred the commission ban; incumbents already have Merlo AI and PE capital; using owners' registers to market rentals is a conflict/privacy problem (12). Get building-level density by targeting investors in 30+ lot buildings directly and winning developer lease-ups (12, 13).

## The strategic reframe (the most valuable idea to come out of the red team)

**Your durable edge is independence from sales, not lower cost** (06, echoed by 09 and 02).
- A PM-only agency can give landlords neutral advice at sale; franchises can't copy that without losing commission.
- It turns sales agencies from retaliators into roll suppliers: *"Sell us your rent roll; we refer your selling landlords back to you (disclosed, consented)."* This also lowers the price (02) and protects retention (09).
- It is the LAF instinct (owning the moment of agent choice) put on a legally defensible footing.

## Recommended plan (consolidated)

**Entry route (11, 02, 03):** buy a Melbourne agency with **250–500 managements** whose principal is retiring and stays 18–24 months as licensee/OIEC.
- **Price:** 25–40% deferred, paid per retained management at 6 and 12 months (a landlord sale counts as a loss), plus vendor finance.
- **What it gives you:** licence, trust account, staff, a lending track record, and real portfolios to measure productivity on.
- **Funding:** no VC for the agency (:Different).

**Pricing rule for rolls (02):** price per property ≤ proven contribution × 0.85 ÷ 0.13. Buy beyond the first deal only once contribution of **≥$850** per property is proven.

**Operating model (04, 05, 10):**
- **Roles:** relationship PM; tenancy-care lead (~500–600 properties); leasing staff (not PM-run tours); arrears/VCAT specialist from 500 properties; field inspectors; backup PM named on every landlord.
- **Software:** own a thin work layer beside PropertyMe (its AI access is read-only), with a case log, agent controller and minute-level measurement. Hard controls in code: no AI writes to the trust ledger, prescribed CAV forms only, a block on outbound promises, statutory clocks, and humans for applicant selection, notices and bond claims.
- **Build:** founder builds the first platform (a contracted engineer costs $1,500+ per property at 100 properties). 90 days ≈ $15–25k cash.

**Growth channel, pick one (08, 07, 12, 13):** **point-of-purchase investor referrals**: sales-only agencies, buyers' agents, brokers, accountants, with disclosed $300–600 per signing; plus developer lease-up mandates. Demote the comparison site to an optional, separate-entity, opt-in, verified-data, aggregate-only product, or drop it.

**Corridor (13):** inner north (Brunswick–Coburg–Northcote–Thornbury–Preston; ~25k private rentals in core postcodes, most fragmented). Keep to a six-postcode core: density is worth ~$300 per property per year in field cost. Alternative: inner south-east. Avoid Box Hill/Glen Waverley, the CBD and growth corridors.

**Pricing (01):** price at or above market. 5.5% vs 5.0% is worth more than going from 3x to 4.5x on PM productivity.

## Revised gates

| Gate | Brief | Revised (source) |
|---|---|---|
| 1 Acquisition cost | Funnel < $2k | ≥25 signings in 90 days at ≤$1.5k fully loaded via the chosen channel; kill <10 (08). Compare against roll equity cost (~$2.2k at 70% LVR), not total price (08). |
| 2 Cost to serve | Beat Crossub $560, PM 300+ | ≥120 properties per total staff; fully loaded wages ≤$900/property; PM desk ≤40 h/100 properties/month (04). Offshore-VA benchmark implies ≥350 per PM (06). Include tenancy-care cost (10). |
| 3 Sale capture | ≥50% sell through you | ≥30% of sales captured (referral **or** management retained with buyer) **and** net retention ≥88%/yr (09). Revenue counted only after s 48A advice (03). |
| New: Retention | — | Acquired-roll loss ≤8% at 12 months (11); vendor's 3-year loss rate known before pricing (13). |

**Exception metric (04, 05):** an exception is any non-field staff touch beyond a one-click approval of an in-policy AI action. Report exceptions, staff minutes and reopen/complaint rate per 100 properties per month, excluding acquisition onboarding. *Minutes* decide gate 2.

## Cheapest tests to run first (before any capital)

1. **Shadow test (04, 05):** pay an agency $5–15k for 4 weeks of PropertyMe activity; replay cases through your agents; measure desk-minutes per 100 properties. Kill if it can't get under ~40 h at simulation.
2. **Legal opinion (03):** s 48A referral structure, guarantee structure, licensing route, LAF restraint. ~1–2 weeks.
3. **Deal-flow count (02):** 6 weeks with two rent-roll brokers; count sub-scale rolls in the corridor, their 3-year loss rates and current multiples; get lender term sheets.
4. **Channel test (08, 07):** under a licensed partner's co-brand, 12 weeks, ~$50–75k, ≥30 signed authorities target.
5. **PI/cyber insurance quotes with no AI exclusion (10).**

## Dated decision calendar and kill criteria (11, with inputs from 01/04/08/13)

Personal limits: ≤$1.2M cash at risk, ≤$1.5M personal guarantee, never secured on the family home; keep the job to **30 Jun 2027**.

| Date | Gate | Kill / pivot if |
|---|---|---|
| 31 Jan 2027 | **G0** | LAF restraint not cleared; no lender term sheet; legal opinion negative on s 48A *and* no workable alternative. |
| 30 Jun 2027 | **G1** | <30 signed authorities at ≤$2k; no LOI on an acquisition or licensed partner; shadow test >70 h/100 properties. |
| 31 Dec 2027 | **G2** | First acquisition not settled with ≥25% vendor-financed. |
| 30 Sep 2028 | **G3** | Acquired-roll loss >8%; <200 properties per relationship PM → run it as a normal agency or sell the roll. |
| 30 Jun 2029 | **G4** | <700 properties or founder draw <$200k. |
| 31 Dec 2030 | **Final** | Sustainable draw <$400k and net roll equity <$3M → exit. |

Corridor kill (13): bonds falling >4%/yr through 2026, top-3 agencies >55% of listings, or blended roll losses >15%/yr.

## Where the agents disagree (needs your judgement or better data)

- **Bond trend / sell-off attrition:** 08 says active bonds recovered to 745k+ (May 2026); 13 says losses are ~7–9% of a book per year from 2023–24 data; 02 says refunds exceeded lodgements by mid-2026. Get the DFFH June-quarter 2026 data (blocked in session).
- **Founder income at 1,000 properties:** 04's org chart gives ~$650/property margin (founder unpaid as Head of PM); 01's model gives 14% EBITDA at 3x with $575k fixed costs. The difference is mostly fixed overhead; the model lets you test a leaner fixed base ($400k → 3x needs ~2,000 properties for $500k).
- **Debt-funded outcome:** ranges from −$296k (01, 7-year loan) to ~+$300k (02), driven by loan term and multiple. Lender term sheets resolve this.
- **Current fee level:** quoted 5.5–6% (07, 13) vs realised ~5.4% and lower on sitting tenants (13).

## Corrections to the brief

- Multiple base is management commission, not gross revenue; FY22 $3.70 is stale and was a peak; current ~2.8–3.5x.
- Bidding: fixed-price advertising since 2021; Nov 2025 added a ban on accepting offers above the advertised rent. End-of-term no-grounds notices abolished (Nov 2025); bond claims need evidence (Oct 2026).
- RDRV live since June 2025; Renting Taskforce permanent; minimum energy standards from **1 Mar 2027**; portable bonds live from 1 Jul 2026.
- Privacy Act automated-decision transparency from **10 Dec 2026**; representative registration from **25 Nov 2026**; Victorian election **28 Nov 2026**.
- Strata: the NSW phase-out is a voluntary industry policy; Victoria deferred its ban; "Strata Community" is the association, not a roll-up; OC managers are registered, not yet licensed.
- Leasey.AI (Canada) and Picket (US) aren't Australian precedents; Cubbi/Kolmeo failure unconfirmed; real AU failures are :Different and Yabonza.

## Answers to the open items

| Open item | Answer | Source |
|---|---|---|
| Licensed operator | Buy a retiring principal's licensed agency (preferred), or hire a full-time OIEC with equity and vesting. No rent-a-licence. | 11, 03 |
| Unit-economics model | `models/unit_economics.py`: 1x–4x scenarios, roll vs funnel, debt, tornado. | 01 |
| Strata model | `reports/12`: avoid; partnership adjacency at most, year 3+. | 12 |
| Pre-sell test | `reports/07` and `reports/08`: under a licensed co-brand, 12 weeks, $50–75k. | 07, 08 |
| Minimum platform | `reports/05`: 90-day plan, rules file plus one PropertyMe adapter, shadow mode first. | 05 |
| Capital plan | Self-fund plus vendor finance plus bank debt after 100+ properties; family office or wholesale only after two integrated acquisitions; no VC. | 11, 02 |
| Kill criteria | Calendar above. | 11 |
