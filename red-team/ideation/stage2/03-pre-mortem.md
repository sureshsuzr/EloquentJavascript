# Pre-Mortem Skeptic: stage-2 evaluation

Evaluator 03, 3 Nov 2026. Method: for each candidate, assume it has failed by 2030 and write the most likely cause. Then test the three stage-1 claims that recur across the shortlist: **the Australian field is empty**, **entry prices are cheap**, and **the regulatory tailwind is real**. 17 web searches, mostly search summaries rather than primary documents. Labels: **[verified: source]**, **[estimate]**, **[unverified]**.

## Assumptions

One set, applied to every candidate.

- **Baseline (stay employed, 10 years): A$3.2M** of after-tax wealth. This is roughly A$1.5–1.7M of saved after-tax salary (A$500k gross at a ~45% average tax rate, less living costs), plus ~A$1.0–1.4M of expected employer equity, plus returns on savings. It extends the earlier rounds' A$2.0–2.4M over 7 years [estimate]. I treat outcomes below **A$4.0M** as not materially beating the baseline, given the extra risk taken.
- **Tax:** salary at marginal rates (47% top); equity exits at ~23.5% effective (50% CGT discount); fund carry taxed as capital where structured that way, otherwise as income; company profits at 25–30% before distribution.
- **Founder salary in the venture:** A$250–350k until the business can pay more. PE/holdco-funded roles pay A$300–400k from first close. VC-backed roles pay A$250k until Series B.
- **Dilution:** VC paths reach 20–35% founder ownership at exit after 2–3 rounds. Holdco and independent-sponsor paths reach 15–30% (co-invest plus promote). Bootstrapped paths reach 55–80%.
- **Discounting:** wealth is in 2026 dollars. Equity proceeds received in years 7–10 are discounted at 6% a year real, which cuts back-ended "great" outcomes by ~25–35%. Salary is not discounted. This is one reason my EVs sit below stage 1's.
- **Fail case:** he spends 2–4 years on the venture and loses most of the capital he put in (A$0.3–1.0M). He forfeits unvested employer equity (~A$0.5–1.0M) and re-enters at ~A$400k. That puts **fail-case wealth at about A$1.3–1.9M**, unless the path started while he was still employed, in which case it is about A$2.3–2.6M.
- **Probabilities:** where my reading of the evidence differs from stage 1, I re-weight. In particular, no first-time manager, sponsor or MGA founder gets better than about 10% in the "great" bucket.

**Headline finding.** On these assumptions, **every candidate's EV falls to A$3.6–5.0M**, compared with stage-1 figures of A$4.0–9.3M. Two things inflated stage 1:
- "Great" tails of 10–12% at A$20–40M, undiscounted;
- fail probabilities of 20–30% for first-time buy-outs and funds. Base rates support 35–45%: only ~58% of searches ever acquire, and ~25% of acquisitions lose money [verified: Stanford 2026 via secondary summaries].

So nothing clearly dominates staying employed on expected value. The choice turns on **survival, how severe the downside is for him personally, and whether he can learn cheaply before quitting**.

## Scores

Columns:
- **Survive 2030:** probability the venture is still a going concern on plan in 2030.
- **P(>A$4M):** probability of materially beating the baseline.
- **Fail-case wealth:** 10-year wealth if it fails.
- **Downside severity:** for the founder personally, 10 = worst. It covers capital, personal-guarantee or covenant exposure, regulatory and reputational liability, and lost employer equity.
- **Claim fragility:** how badly the stage-1 claims about an empty field, cheap entry and a regulatory tailwind held up, 10 = collapsed.

| ID | Candidate | Survive 2030 | P(>A$4M) | Fail-case wealth | Downside severity | Claim fragility | Pre-mortem EV (stage 1) | Median | **Overall (1–10)** |
|---|---|---|---|---|---|---|---|---|---|
| C0 | Rent-roll hybrid (benchmark) | 75% | 25% | A$2.4M | 2 | 5 | **A$3.7M** (3.0–3.4 at 7 yrs) | 3.4 | **5.5** |
| C1 | ANZ vertical-software holdco | 55% | 35% | A$1.7M | 5 | **7** | **A$5.0M** (8.0–8.5) | 3.3 | **6.0** |
| C2 | AI accounting roll-up | 55% | 30% | A$1.3M | 6 | **8** | **A$4.1M** (4.3–9.3) | 3.0 | **4.0** |
| C3 | SMSF compliance factory | 60% | 30% | A$1.5M | 6 | 6 | **A$3.9M** (5.4–5.5) | 3.0 | **5.0** |
| C4 | Pricing-led distribution holdco | 70% | 40% | A$1.4M | 6 | 4 | **A$4.9M** (7.2) | 3.6 | **6.5** |
| C5 | Succession-capital platform | 65% (as activity) | 30% | A$2.4M | 3 | 6 | **A$4.8M** (4.9–7.8) | 3.5 | **5.5** (as a wrapper) |
| C6 | Succession Credit fund | 45% | 25% | A$1.3M | **8** | 6 | **A$3.7M** (4.7–5.3) | 3.0 | **3.5** |
| C7 | Private-markets valuation layer | 45% | 30% | A$1.5M | 4 | 6 | **A$4.3M** (4.0–6.6) | 3.2 | **4.5** |
| C8 | AI-priced niche MGA | 35% | 25% | A$1.6M | 5 | 6 | **A$4.6M** (5.7–7.6) | 1.6–3.0 | **3.0** |
| C9 | Grid-capacity arbitrage | 45% | 28% | A$1.5M | 5 | 6 | **A$4.2M** (4.9–6.2) | 3.2 | **4.5** |

EV workings use buckets of [P fail / modest / good / great] × [10-year wealth A$M] [estimate]:

| ID | Fail | Modest | Good | Great |
|---|---|---|---|---|
| C0 | .30 × 2.4 | .45 × 3.4 | .20 × 5.0 | .05 × 8 |
| C1 | .35 × 1.7 | .35 × 3.3 | .22 × 7.5 | .08 × 20 |
| C2 | .35 × 1.3 | .35 × 3.0 | .22 × 6.5 | .08 × 15 |
| C3 | .30 × 1.5 | .40 × 3.0 | .23 × 6.0 | .07 × 12 |
| C4 | .25 × 1.4 | .40 × 3.6 | .27 × 7.0 | .08 × 15 |
| C5 | .35 × 2.4 | .40 × 3.5 | .18 × 7.0 | .07 × 18 |
| C6 | .40 × 1.3 | .35 × 3.0 | .18 × 6.0 | .07 × 15 |
| C7 | .45 × 1.5 | .30 × 3.2 | .18 × 7.0 | .07 × 20 |
| C8 | .55 × 1.6 | .22 × 3.0 | .16 × 8.0 | .07 × 25 |
| C9 | .45 × 1.5 | .30 × 3.2 | .18 × 7.0 | .07 × 18 |

The overall score weights survival and downside severity about as heavily as EV, because a founder who replaces a A$500k income and has ~A$1M at risk cannot diversify across ten attempts.

## Candidate notes

**C0: Rent-roll pricing-engine hybrid.**
- **Most likely cause of failure by 2030:** the licensed operator's integration loses ~20–34% of landlords on the rolls bought, more than the engine's pricing edge (round 3: ~66% vs ~80% kept). The co-invest returns about cost. Meanwhile PropertyMe's agentic AiMe (EQT-owned) makes the "engine" look like a feature.
- **What stage 1 missed:** this is the safest candidate because it is small. He keeps his job, and only A$0.3–0.5M is at risk. But its ceiling is low, and 250–900 deals a year cannot carry a A$500k income.
- **Its real value:** as the **first vertical of a broader acquisition-pricing engine** (C5/C1/C4), not as a destination.
- **Verdict:** keep as the low-cost first project. Don't call it the plan.

**C1: ANZ vertical-software holdco.**
- **Most likely cause of failure by 2030:** after a 12–18-month search he closes deal 1 at ~6x on a second-tier asset, because every good ANZ vertical tool already had five global calls. Gross retention runs at 85–88% as AI-native entrants reprice the niche. With A$1.5–2M of EBITDA the holdco can't raise round 2, and he ends up as a A$300k CEO of one small software company.
- **The "empty field" claim is the weakest on the shortlist.** In 2025–26 alone:
  - Valsoft/Fluent bought Eziway (Apr 2026) [verified: Valsoft release];
  - Arcadea bought JAIX (Apr 2026) and Agdata (Apr 2025) [verified: Business Wire];
  - Constellation/Vela's Libra bought Expedient (Jun 2026) [verified: trade press];
  - Exa Capital, a permanent-hold investor, bought StaffReady and Flow Software [verified: Medianet, PrivSource];
  - ASG bought PlayHQ; Invincible bought ProSpend; Access Group bought ATO SmartDocs, Onboarded and ChangeGPS;
  - Potentia works the larger end (HotDoc, Feb 2026).

  These buyers have lower capital costs, ready-made playbooks and patience.
- **Cheap entry is true only for the adverse-selected tail.** Small-SaaS listing data puts founder-dependent, no-growth tools at ~2x profit, but quality systems of record are bid up [unverified: bigideasdb, Moore 15.7x mid-market]. The SaaSpocalypse cuts both ways: the CSU-family buyers' share prices fell, but their deal pace did not.
- **A hazard stage 1 understated:** he is a sitting SaaS CFO. Sourcing SaaS targets is the **sharpest employment conflict on the list**, and the search phase can't credibly run "while employed" without written consent.
- **Why it still ranks high:** founder fit is the best on the list. The failure mode most likely in the first two years (no deal at an acceptable price) is cheap, and the upside is real.

**C2: AI-native accounting roll-up ("Ledgerline").**
- **Most likely cause of failure by 2030:** he buys four practices at ~1.25x fees against 47 rival bidders per listing [verified: DMY]. He loses 15% of clients and two partners. Agentic tools from Xero, BGL and Basis spread the hours saved across the whole market, so fee rates fall and the margin uplift never reaches the P&L. Lenders tighten covenants.
- **The field is crowded:**
  - Kelly Partners: A$159M revenue, roughly one deal a month;
  - Count: H1 2026 revenue +54% on acquisitions [verified: Count results summary];
  - Findex: still buying (Brisbane, Mar 2026) [verified];
  - GT Australia: now owned by GT US/New Mountain [verified];
  - Multiplier: ten acquisitions including two in NZ with Australian clients, and a reported US$35M raise in Aug 2026 [verified: IT Brief, Dealroom].
- **Ownership:** the founder isn't a CA and would own 12–20%.
- **Verdict:** stage 1's A$9.3M EV relied on a 10–14x exit that no AU platform has proven. **Demote.**

**C3: SMSF compliance factory.**
- **Most likely cause of failure by 2030:** referring accountants keep the client relationship and use BGL/Class AI in-house. Wholesale price falls toward A$800–900 per fund, and the bought books lose 15–20% of funds. Separately, an ASIC review finds evidence gaps at the high-volume signing auditor.
- **The "auditor shortage" is real but isn't pricing power.** Numbers fell to 3,882 (Jun 2025) [verified: ASIC REP 825 via SMSF Adviser], but ASIC calls it expected attrition, and the median fee has been flat at ~A$550 for five years. Work is concentrating in high-volume firms that already exist.
- **ASIC is moving against high-volume auditors, not toward them:** 64 actions against SMSF auditors in FY26 [verified: ASIC 26-170MR].
- **The field isn't empty:** Pemba-owned SuperConcepts (PE consolidation of SMSF administration), Multiport, Heffron, SuperGuardian, esuperfund, and ASF Audits with its AI assistant.
- **Div 296 is narrower than it sounds:** it adds work mainly for the minority of funds with balances above A$3M [estimate].
- **Downside:** licensing and liability concentrated in hired auditors he depends on.

**C4: Pricing-led B2B distribution holdco.**
- **Most likely cause of failure by 2030:** the 2026 rate rises (four in 2026 [unverified]) push construction and mining customers into a 2027–28 slowdown just as he raises prices. Two key accounts and a senior rep leave, and the top supplier invokes change of control. Working capital tightens under ABL covenants, and the lender asks for a personal guarantee to waive a breach.
- **Of the four major claims, this one held up best.** I found **no AU AI/pricing-led distributor roll-up at A$1.5–4M EBITDA**. PE activity sits higher up: PEP/ATOM, Five V/Questas at A$375M, IPD/CMI at A$101M [verified: MergerLinks, Financial Standard]. That gives an exit market without competition at the entry size.
- **Still unverified:** entry multiples (4–5x) and the 100–300 bps uplift (vendor claims).
- **Its failure modes show up early:** the 90-day invoice-line leakage test kills it before he quits.
- **Downside is the most physical on the list:** leverage, inventory, people and possible PG pressure. So the rule is **ABL without a PG or no deal**.
- **Satisfaction risk:** sales-rep culture change is the grind he disliked. Still, it is a profitable business on day 1, not a density build.

**C5: Succession-capital platform (engine + sponsor).**
- **Most likely cause of failure by 2030:** the engine flags thousands of owners, but conversion is no better than broker listings. The real deals come from accountants and brokers. Family offices back him for one deal, not a fund. By 2029 he is a part-time independent sponsor with two small co-invests, still employed or re-employed.
- **"Empty field" is mostly true:** the AU search ecosystem is still anecdotal [verified: searchfunder posts 2024–26]. But that emptiness also means no LP base.
- **Downside is the lowest of the equity ideas,** because it can run while he is employed. But it **doesn't replace A$500k on its own**.
- **Verdict:** score it as the **capital and origination wrapper** for C1 or C4 (and C0's engine), not as a standalone company.

**C6: Succession Credit fund (and BookCo).**
- **Most likely cause of failure by 2030:** he raises A$25–30M from family offices during ASIC's private-credit crackdown, as frozen funds (Bathla, MA, Metrics, ~A$9B gated [verified: stage-1 sources]) make HNW investors wary of credit managers. Vintage 1 lends to buyers the banks declined. A rate-driven slowdown brings 4–6% annual losses on goodwill with 20–40% recovery. Investors redeem, and he spends 2029 on workouts with failing family businesses.
- **The tailwind is a headwind for a first-time manager:** ASIC's 2026 enforcement priority is "poor private credit practices" [verified: ASIC/FNArena].
- **Severity is the highest on the list:**
  - personal reputational exposure as a responsible manager;
  - unfair-contract-terms liability;
  - workouts against small-business owners;
  - a public failure record that follows him.
- **The BookCo entry is capped** by Macquarie and NAB lending to 70–80% LVR.
- **Verdict: demote.** Fold the rent-roll stretch-debt idea into C0 as a co-invest feature.

**C7: Independent valuation and risk layer.**
- **Most likely cause of failure by 2030:** funds and trustees answer ASIC/APRA by buying a *signature*: Kroll, Big 4, Herron Todd White for property, or IQ-EQ/Perpetual trustee services. They don't buy a model. CPS 230 onboarding takes 6–18 months. By the time one super fund signs, the seed money has gone, and a custodian or MSCI bundles a "good enough" daily estimate.
- **The tailwind is real** (ASIC 18 June 2026 notice; REP 820; APRA 12 of 23 trustees short) [verified: ASIC, Investor Daily]. But the regulation names *qualified external valuers*, which favours incumbents.
- **The "empty field" claim is partly true:** there is no loan-level AU utility, but MSCI, S&P, Houlihan Lokey, Lincoln, Chronograph and 73 Strings are all a sales hire away.
- **Downside is moderate:** VC-funded, but it costs ~3 years of A$250k pay instead of A$500k.
- **Upside:** the global DC-pension angle keeps a right tail. This is the best "software" option, but enterprise sales cycles cut against the income constraint.

**C8: AI-priced niche MGA.**
- **Most likely cause of failure by 2030:** no carrier gives a binder to a founder with no underwriting record. The one that does withdraws after a correlated loss (one model or installer failure across many policies).
- **AI-agent liability:**
  - Armilla (Lloyd's-backed, US$25M limits, US$25M raise Jan 2026), AIUC and Testudo already hold Lloyd's capacity and can write APAC from London [verified: Fintech Global, FF News].
  - Australian insurers are adding AI exclusions or quietly covering AI under cyber and E&O [verified: Insurance Business AU].
  - I found **no local MGA**, but the Australian premium pool is small and can be served from outside.
- **VoltCover:** no mandate exists, and I found no sign of one coming [unverified absence]. Installers won't pay voluntarily.
- **Verdict:** lowest survival on the list (35%). Its EV is held up only by the tail.

**C9: Grid-capacity arbitrage.**
- **Most likely cause of failure by 2030:** the information gap he means to price gets published. The AEMC's draft rules include a **public large-load register** and a 30 MW "large load" threshold (submissions close 5 Nov 2026) [verified: AEMC/W.Media].
- **Evidence that queue speculation unwinds:** AEMO's 2026 ESOO reports 36% of developing data-centre projects cancelled and ~27% average connection use [verified: AEMO ESOO 2026 overview]. Option fees on 2–3 sites are written off when buyers (Keppel, Stockland, PGIM, NEXTDC) go direct.
- **Battery-side revenue fell** from ~A$142k to ~A$85k per MW a year [verified: Modo via stage 1].
- **Downside:** moderate and option-based.
- **Fit:** the best Fulfilio-style fit and high satisfaction, but lumpy income and a closing window.

## Promotions/demotions

- **Merge C5 into C1/C4 as the capital wrapper.** Use deal-by-deal independent-sponsor equity, with the scoring/QoE engine as proprietary origination, and no fund until two deals have performed. As a standalone it fails the income constraint.
- **Fold the BookCo half of C6 into C0** as stretch-debt co-investment alongside the operator. **Drop the Succession Credit fund** for this founder now; revisit after five years of acquisition experience.
- **Demote C2.** Multiplier, Kelly Partners, Count, Findex and GT/New Mountain hold the field, and the founder's edge isn't distinctive there.
- **Demote C8's AI-liability variant.** Keep VoltCover only as a free watch item: a mandate for insurance-backed installer guarantees would change the answer.
- **Promote 03's "QoE Engine" from the not-shortlisted pool**, as the single shared engine behind C0, C1, C4 and C5. It is the one asset that can be built for under A$50k while employed, and it is useful whichever buy-out path survives.
- **Consider the Victorian compliance-services platform (08 A) as an alternative first platform inside C4's "boring cash-flow buy-out" category, not as its own candidate.** It has mandated, contracted demand and fast income. The failure mode is the technician shortage, and it is the most ops-heavy of the options.
- **Don't promote aged-care underwrite-and-own or home-care consolidation.** Funding-cliff, regulatory and reputational downsides are the most severe of any idea generated.

## Ranking and recommendation

| Rank | ID | Score | Why |
|---|---|---|---|
| 1 | C4 Pricing-led distribution holdco | 6.5 | Field claim survived scrutiny; highest median (A$3.6M) and survival (70%); failure visible in a cheap 90-day data test; cash flow from day 1. Main risks: cycle, PG and grind. |
| 2 | C1 ANZ vertical-software holdco | 6.0 | Best founder fit and good upside, but the "empty field" claim collapsed (Valsoft, Arcadea, Vela, Exa, Access, ASG); sharpest employer conflict. |
| 3 | C5 Succession-capital platform (as wrapper) | 5.5 | Low downside, starts while employed; not a business on its own. |
| 4 | C0 Rent-roll hybrid | 5.5 | Safest; low ceiling. |
| 5 | C3 SMSF compliance factory | 5.0 | Real but already consolidating; ASIC enforcement and fee-flat evidence undercut the "shortage" thesis. |
| 6 | C7 Valuation layer | 4.5 | Real tailwind that favours signature incumbents; slow sales. |
| 7 | C9 Grid-capacity arbitrage | 4.5 | Information edge is being regulated away (public large-load register). |
| 8 | C2 AI accounting roll-up | 4.0 | Crowded; fee deflation. |
| 9 | C6 Succession Credit fund | 3.5 | Most severe personal downside; worst timing for a first-time credit manager. |
| 10 | C8 Niche MGA | 3.0 | Capacity binary; global players already capitalised. |

**My one choice: C4, the pricing-led distribution holdco, financed through C5's deal-by-deal sponsor structure, with C1 run as a parallel 90-day test.**

The case rests on the most likely failure, not the best case:
- **C4's most likely failure is a modest outcome, not a wipe-out:** a profitable distributor where the pricing lift is 75 bps instead of 150. That outcome still pays a A$300–350k salary and keeps capital mostly intact.
- **C1's most likely failure is losing the auction** to permanent-capital buyers, or overpaying for a second-tier asset.
- **Every other candidate's most likely failure** is a binary he can't test before quitting: a carrier binder, a fund raise, CPS 230 procurement or a DNSP connection offer.

**Conditions without which I would not recommend C4:**
1. an ABL or cash-flow facility **with no personal guarantee**;
2. no single supplier above ~25% of COGS without an assignable agreement;
3. entry at 5x or below;
4. leakage of at least 150 bps shown on real invoice lines before signing.

If C1's 90-day test unexpectedly finds three or more founder-owned systems of record with GRR of at least 90% at 6x or below, swap the order: C1 has the better fit and the fatter tail.

## Sequencing

1. **Months 0–1, while employed: get written outside-interests consent.** This gates everything.
   - C4 and C9 don't conflict with a SaaS employer.
   - C1 does, and if consent for software sourcing is refused, C1 waits until after he resigns.
   - No customer contact on any path before consent.
2. **Months 0–4: build the shared engine** (QoE plus retention/pricing; under A$50k), using C0's rent rolls as the first calibration set. Co-invest no more than A$300k in C0 only if the operator gives outcome-data rights.
3. **Months 2–5: C4's 90-day test.**
   - Three distributors share 24 months of invoice lines.
   - At least 15 targets at 5x or below.
   - At least A$3M soft-circled.
   - One ABL indication without a PG.

   Run C1's test in parallel only if consent allows: 40 founder calls; kill if fewer than 3 targets are at 6x or below with GRR of at least 90%.
4. **Jump trigger** (expected around month 9–12): a signed LOI, committed equity and a lender term sheet without a PG. He resigns only then, which also protects unvested employer equity for as long as possible.
5. **Years 1–3:** run the platform, prove the lift, add 1–2 bolt-ons, and use the engine for origination. Consider a committed vehicle (C5 proper) only after two deals have performed.
6. **Don't start now:** C6, C8 and C2. **Keep as watch items:** C9 (if the AEMC large-load register is diluted), VoltCover (if a guarantee mandate appears) and C7 (if a super fund offers a paid pilot through his network).

**How they combine:** one engine (QoE/pricing) and one capital structure (deal-by-deal sponsor) serve C0 as a training set, C4 as the platform and C1 as an option. The founder's edge is the same in all three: pricing a recurring book under uncertainty, then owning it.
