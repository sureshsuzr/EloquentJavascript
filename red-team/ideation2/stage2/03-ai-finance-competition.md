# AI finance-services market and competition: stage-2 evaluation

Evaluator lens 03: AI finance-services market and competition analyst. Date: 4 Nov 2026. Sources: 17 web searches plus the stage-1 files (11, 12, 13, 14; skims of 01, 02, 03, 08) and `red-team/ideation/SYNTHESIS.md`. Labels: **[verified: source]**, **[estimate]**, **[unverified]**. Amounts are in AUD unless marked US$.

**My job:** settle the S1 dispute between stage-1 reports 11 and 14, and test the service core shared by S1–S4. That means checking how fast AI accounting is being commoditised, what Bench and Botkeeper teach, what outcome pricing looks like in practice, what gross margins, ACVs and churn are achievable by segment, and which segment can be defended. S5–S8 are scored only for their AI-service component and their exposure to competition. Other lenses cover their asset and capital risk.

---

## Assumptions (applied to every candidate)

| Item | Assumption |
|---|---|
| Stay-employed baseline (B0) | A$500k a year package, about A$290k after tax. **10-year after-tax value ≈ A$3.25M** (midpoint of the A$3.0–3.5M used in earlier rounds), with a near-zero chance of total loss. |
| Founder salary when building | A$0 in year 1, then A$150k a year. That is about A$1.0M after tax over 10 years. |
| Tax on exit equity | Effective ~25%: the CGT discount, haircut for the unverified May 2026 indexation proposal. |
| Dilution | Bootstrapped services firm (S1–S4): founder holds 55–65% at exit after a co-founder and ESOP. Capital-heavy models (S5, S7, S8): 25–40% of the operating company plus a promote. |
| Time discount | Exit equity realised in years 7–10 is multiplied by 0.75 (about 4% a year real) before comparison. Salary is not discounted. |
| Base rates | "Great" outcomes are capped at **5–6%** (round-1 calibration) instead of stage-1's 8–13%. |
| Services exit multiples | **0.95–1.35x revenue for practices sold to other practices** [verified: DMY market data, Nov 2025]. About 4–6x (EBITDA) for ~A$5M-revenue firms bought by PE [verified: DMY, May 2026, multiple basis not stated]. AI-native premium of 1.5–3x revenue only with demonstrated 55%+ gross margin and net revenue retention (NRR) above 110% [estimate]. |
| Definitions | **EV** = expected 10-year founder value: after-tax salary plus after-tax, time-discounted equity, less capital lost. **P(positive)** = P(EV outcome > A$3.25M). **P(total loss)** = P(most of the personal capital is lost *and* the founder ends below A$1.5M). |

---

## What the market evidence says (lens findings)

**1. Platforms are commoditising the transaction layer quickly, and 2026 was the turning point.**
- **Xero:** a month-end agent in XeroForce. It checks reconciliation status and posts journals for prepayments and amortisation, and it runs across an accountant's whole client list [verified: Xero media release, Xerocon US, 19 Aug 2026; ChannelLife]. Xero says JAX has more than 500k users [unverified: Xero LinkedIn post; vendor claim].
- **MYOB:** "agentic BAS" went from a sole-trader beta in March 2026 to businesses with 1–19 employees by September 2026. It prepares the BAS but does not lodge it; a registered agent still signs off [verified: Accountants Daily; IT Brief; iTWire].
- **Intuit:** the Accountant Suite launched in Australia on 12 Feb 2026, reported as free to AU firms for now. Intuit Intelligence was switched on in AU on 14 Oct 2026 [verified: QuickBooks AU blog; Accountants Daily; IT Brief].
- **Pilot:** a "fully autonomous" AI Accountant that runs onboarding through monthly close with no human (4 Feb 2026) [verified: CPA Practice Advisor]. A US$99/month tier is reported [unverified].
- **Capital in the category:** Rillet raised US$100M at US$1B (Aug 2026, ICONIQ), its third raise in a year [verified: FinTech Futures]. Basis is valued at US$1.15B [verified in stage 1]. Vistra, a global entity-management incumbent, has an AI compliance agent (Geni) and appointed a Chief AI officer in Apr 2026 [verified: EQT case study; trade press].

*Conclusion.* By 2027–28, bookkeeping, bank reconciliation, coding, accruals and BAS preparation will be a feature of the ledger for any client on Xero, MYOB or QuickBooks. **The price of that layer heads towards software prices (US$100–500 a month).** Stage-1 report 11 assumed "price held while cost falls" and margins of 70–75%. Holding price is only realistic where the deliverable is *not* the ledger's job: specialised regulatory reporting, lender and ASX deliverables, liability-bearing sign-off, and cash outcomes.

**2. What Bench and Botkeeper teach (they died differently).**
- **Bench** burned US$135M [verified: TechCrunch, Feb 2025]. It died when a bank called its venture debt [verified: TechCrunch]. Low price per micro-SMB, human-heavy delivery and a proprietary ledger meant it couldn't automate fast enough to make its price work.
- **Botkeeper** was a B2B2B supplier to accounting firms. Consolidation among its largest clients cut revenue [verified: CPA Practice Advisor, 9 Feb 2026]. Its debt covenants are reported to have depended on those accounts [unverified: secondary summary of Accounting Today].
- **Shared failure modes:** debt on top of fragile unit economics; client concentration; selling to people whose own economics were being restructured; and, for Bench, price set below the cost of the human remainder.
- **Design rules that follow:**
  - no venture debt;
  - no client above 10% of revenue;
  - the ledger stays the client's;
  - the price is set against the *cost of failure* (penalties, lender default, ASX query, suspension), not against the cost of bookkeeping;
  - never be a wholesale supplier to firms that are consolidating.

  This kills stage-1 report 14's "Close Engine" and argues against relying on accounting-firm channels.

**3. Outcome pricing in practice is hybrid. The pure versions are software, not services.**
- HighRadius has $0 subscription and charges a share of realised gains after go-live [verified: Business Wire, 27 Feb 2026]. Critics note that revenue becomes unpredictable when realisation lags [verified: commentary].
- Digits bills accounting firms per client only when ~95% of transactions are "zero-touch" [verified: CPA Practice Advisor, 7 Apr 2026; the 95% figure is third-party].
- Pure outcome pricing is ~3.8% of AI products [verified in stage 1: Orb].
- **For a services firm, the workable form is:**
  - a fixed fee covering 80–90% of expected revenue;
  - SLA credits capped at 10–15% of fees (close by business day N, deadlines met, no finance-caused regulator or lender query);
  - gainshare only where the outcome is a **cash event the firm controls**: aged-debt collection, incentive and refund claims, duplicate-payment recovery.
- Report 14 is right that this is the price of entry, not a moat. **Outcome pricing is a sales tool. Defensibility has to come from the segment.**

**4. Gross margins: no verified AI-native services margin exists.**
- I found no disclosed margins for Current (formerly Crete), Multiplier or Pilot.
- The best hard datapoint: Current's first tax-AI pilot cut preparation time by **~31% across 7,000 returns** [verified: Business Wire, 2 Jun 2026].
- That is meaningful but far from the 1:6 → 1:15 reviewer leverage that report 11 assumes.
- My estimates for an AI-native agency [estimate]: **gross margin ~40–50% in year 1–2, 50–60% at maturity**, EBITDA 20–30%. Higher margins are possible only in templated, deadline-driven segments (5B, SPV packs). Generic SMB margins will be competed away as platform agents take the easy 70%.

**5. Churn and ACV by segment** (no reliable outsourced-finance churn benchmark exists; accounting-firm retention of 85–95% is the closest reference [unverified: vendor blogs]):

| Segment | Realistic ACV | Annual logo churn | Main churn cause | Who commoditises or competes | Defensibility |
|---|---|---|---|---|---|
| VC scaleups (S1) | A$60–150k | **20–30%** [estimate] | Outgrow and hire an in-house CFO; die; get acquired | Pilot, Standard Ledger, Scalesuite, offshore, Xero/QBO agents, Multiplier | **Low** |
| Foreign subsidiaries (S1) | A$40–120k | 8–12% | Parent switches to a global provider | **Vistra (AI agent, bought Melbourne's Leydin Freyer)**, TMF, Azets, Big 4 | Medium. Sales are RFP-led from offshore HQs, a poor fit for a Melbourne start-up |
| ASX juniors (S2) | A$40–120k (stage-1 A$80–150k is high) | 15–25% | Delisting, mergers, cash drought, board change | **Automic** (Advent completed the purchase Dec 2025 [verified]), Vistra/Leydin Freyer, West Perth boutiques | Medium; high where data and capital are attached |
| Renewable SPVs (S4) | A$60–150k per SPV | **<8%** | Asset sale (the buyer often keeps the provider) | RES/Blueshore (>3GW, "full management of the project SPV company") and OX2 (invoices, accounting, annual reports, bank and auditor coordination) [verified: pv magazine, OX2 site] | **High once in**; the cold start is the problem |
| Mining/renewable-build contractors (S3) | A$100–250k | 15–20% plus insolvency | Cash pressure eases; failure | ERP vendors, factors, debtor supply-chain finance programmes | Medium-high **only with the approved-invoice finance arm** |

**Lifetime value per logo** (ACV × gross margin ÷ churn) [estimate]:
- SPVs: ~A$0.5–1.0M
- foreign subsidiaries: ~A$0.3–0.5M
- contractors: ~A$0.3–0.6M
- juniors: ~A$0.15–0.3M
- scaleups: ~A$0.15–0.25M

**Exit-buyer evidence.** Vistra buying Leydin Freyer (a Melbourne corporate-services firm with an ASX small-cap book) [verified headline: PAM Insight; date unverified] and Advent buying Automic [verified] show that strategic buyers exist for "back office to listed small caps". They also show that a Melbourne base is not disqualifying in that segment.

---

## Scores

Lens criteria are scored 1–10, where higher is better (for commoditisation, higher means *more protected*). EV, P(positive) and P(total loss) use the common assumptions above. All are [estimate].

| ID | Protection from commoditisation | Outcome-pricing fit | GM path | ACV × retention | Moat / defensibility | Cash speed | EV (A$M) | P(positive) | P(total loss) | **Overall (lens)** |
|---|---|---|---|---|---|---|---|---|---|---|
| B0 Stay | n/a | n/a | n/a | n/a | n/a | 10 | 3.25 | n/a (baseline) | ~0% | **6.0** |
| B1 Distribution holdco | 6 | 3 | 5 | 6 | 5 | 6 | ~3.7 | ~32% | ~15% | **4.0** (out of scope per brief) |
| S1 Closewise | **3** | 6 | 4 | 4 | 3 | 7 | **~3.8** | **~32%** | ~25% | **4.5** |
| S2 Resources Finance Office | 6 | 8 | 6 | 5 | 6 (7 with Runway Capital) | 7 | ~4.5 | ~42% | ~20% | **6.5** |
| S3 Contractor Cash Desk | 6 | **9** | 5 | 7 | 6 | 7 | ~4.7 | ~42% | ~22% | **6.5** |
| S4 SPV Office | **8** | 7 | 7 | **9** | **8** | 5 | ~4.5 | ~45% | ~18% | **7.0** |
| S2+S4 merged ("Transition Finance Office", see below) | 7.5 | 8 | 7 | 8 | 8 | 6 | **~5.0** | **~47%** | ~18% | **7.5** |
| S5 ColdCore + MeterProof | 7 | 9 | 6 | 7 | 6 | 6 | ~4.8 | ~45% | ~15% | **6.5** |
| S6 PassMark → VoltCover 2.0 | 4 | 7 | 6 | 5 | 4 | 6 | ~4.0 | ~38% | ~25% | **5.0** |
| S7 Long Tail Royalties | 8 | n/a | n/a | n/a | 5 | 4 | ~3.8 | ~38% | ~10% | **5.0** |
| S8 Closure Co | 9 | 6 | n/a | n/a | 6 | 3 | ~3.3 | ~28% | ~35% | **3.5** |

How to read the EVs: every candidate's stage-1 EV falls by 35–65% under common base rates and lens-specific haircuts (price deflation, churn). **None beats staying by much on expectation; the merged SPV and resources office does so most reliably.** That matches the round-1 conclusion that quitting early is roughly break-even, and staged quitting is what creates the edge.

---

## Candidate notes

**B0 — Stay employed.** The lens adds one point. Every month he stays, the platforms commoditise more of generic Track A, so delay *hurts* S1 but barely affects S2/S4. Their moat is regulatory specialisation that Xero and MYOB are not building. Staying while running the 90-day tests is the dominant first move.

**B1 — Staged distribution holdco.** It is outside this round's brief and outside my lens. One note: AI-roll-up funds (Current, Multiplier, Modus) are bidding up exactly the "AI-improvable services business" asset class [verified: Accounting Today; jupid buyer guide]. That supports the founder's rejection of acquisition-led plans. It also means any future *sale* of S1–S4 has an active buyer pool.

**S1 — Closewise (settling the dispute).**
- **The verdict sides with report 14, not report 11:** EV ≈ A$3.8M and P(positive) ≈ 32%, against 11's A$11.8M and 59%.
- **Report 11's model fails in three places:**
  1. Gross margin of 70–75% with price held. The verified 2026 evidence (Pilot autonomous close, Xero month-end agent, MYOB agentic BAS, free Intuit suite) says the price of the ledger layer collapses for exactly the Xero/QBO-based scaleups S1 targets.
  2. Scaleup churn of 20–30% a year, which caps NRR.
  3. A 28% "good" plus 9% "great" probability, against round-1 base rates of 5–6% great.
- **Report 14 is slightly too harsh on the foreign-subsidiary half.** That buyer is sticky and pays for accountability. But the competitor there is Vistra, which has an AI agent, a Melbourne footprint and global parent relationships, and the sale is decided offshore.
- **The Exit-Ready warrants variant** adds adverse selection (cash-poor companies choose deferral) and pushes cash generation out.
- **Distribution conflict:** his employer's CFO peers are the market.
- **What to keep from S1:** its contract template (fixed fee + capped credits + penalty indemnity backed by PI). Reuse it in S2/S4.

**S2 — Resources Finance Office.**
- **Why it rates well:** strongest measurable deliverable (5B by day 20, quarterly, no finance-caused ASX query). It has a public data exhaust of ~750 filers × 4 quarters a year, and no AI 5B product exists (I found none [searched]). The incumbents are relationship firms, not AI firms.
- **What stage 1 missed:**
  1. *Junior ACVs are lower than claimed.* Many juniors spend A$40–80k on finance and company secretarial work, not A$80–150k [estimate], so per-logo LTV is the weakest of the vertical segments.
  2. *Automic now has Advent's money* (completed Dec 2025 [verified]), and Vistra owns Melbourne's Leydin Freyer. The first scaled AI-CoSec competitor is likely to be an incumbent, not a start-up.
  3. *That same consolidation is the exit route* and proves Melbourne is workable.
- **The real upside is Runway Capital** (refund advances, royalties from 5B data). Without it, S2 is a A$5–10M-revenue boutique.

**S3 — Contractor Cash Desk.**
- **Best outcome-pricing fit in the set:** cash timestamps come from the debtor's own portal, and gainshare is natural. Highest ACV.
- **The service alone commoditises:** AR agents (HighRadius, Tesorio, Sidetrade/ezyCollect) are becoming outcome-priced software. **The approved-invoice finance arm is what is defensible.** That brings in capital, credit and licensing risk, which other lenses assess.
- **WA/Qld concentration and commodity cyclicality** raise churn.
- **Best treated as a module or a later product line** of S4/S2 for renewable-build contractors, whose debtors are CIS-backed SPVs the firm already serves. That is a real network effect stage 1 didn't spot.

**S4 — SPV Office.**
- **Best economics per logo:** contracts of 10–15 years (OX2's model [verified]), very low churn, templated deliverables (covenant certificates, CISA settlement, LGC reconciliation), and lender-grade outcomes that platforms are not building.
- **The competitive blind spot in stage 1:** the competitor isn't the Big 4. It's **commercial asset managers who bundle finance into technical and commercial management (TCM).** RES/Blueshore (>3GW; "full management of the project SPV company") and OX2 [verified].
- **So the wedge must be:**
  - sell *to* the asset managers and to funds with in-house asset management, as the AI back office behind them (a supplier, with no single client above 10%, per the Botkeeper rule); or
  - target the long tail of mid-sized IPPs, community and C&I portfolios, and offshore sponsors with no local team.
- **Cold start:** 12–24-month sales cycles. That is why it should start while he is employed.

**S5 — ColdCore + MeterProof.** Under my lens, MeterProof is the cleanest "AI service priced on an outcome": certificates created and savings verified. It is protected from ledger commoditisation. Its competition is accredited persons and ESCOs copying the method, plus certificate-price risk (VEEC surplus [verified in stage 1]). It doesn't overlap S1–S4, so it is a credible Track B alternative, not a complement.

**S6 — PassMark → VoltCover 2.0.** The AI-audit layer is the most commoditisable item outside S1. Document and photo checks are what OEMs, the CER and insurers can build in-house. Value sits in the capped guarantee and insurer capacity, which my lens can't validate. P(positive) ~38%.

**S7 — Long Tail Royalties.** It has no AI-services component; "AI-priced" is a thin edge against Vox and Elemental, who already buy small Australian royalties. Under my lens it is mainly the **exit for S2's royalty-for-fees option**: S2 originates, and S7 or a consolidator buys. Low P(loss) but heavy dilution.

**S8 — Closure Co.** It has no finance-services overlap. "AI-measured rehab outcomes" doesn't solve the binding constraints (regulator acceptance of liability transfer, contamination tail). Lowest lens score.

---

## Promotions, demotions and mergers

1. **Merge S4 + S2 into a "Transition Finance Office"** (my top candidate):
   - **Anchor on renewable/storage SPVs.** They have the best LTV and churn and are Melbourne-centric.
   - **Juniors are the second vertical**, entered through a Melbourne CoSec channel (a partnership, or a small book bought as distribution, not a roll-up).
   - **One agent stack:** templated public and lender deliverables, a capped-SLA contract, a registered tax agent and PI from day 1. Both verticals are deadline-driven, regulator-facing and specialised beyond what Xero/MYOB agents will build.
   - **The optional asset layer is unchanged:** SPV performance data feeds Track B underwriting (revenue floors, availability guarantees), and 5B data feeds Runway Capital.
2. **Fold S3's service into the merged office** as a module for *renewable-build* contractors paid by served SPVs. Defer the finance arm until year 3+ and use a partner balance sheet first.
3. **Demote S1** to "contract template plus foreign-subsidiary module". Don't build a scaleup-focused firm.
4. **Demote report 14's Close Engine** (wholesale to accounting firms) for good. It is Botkeeper's failure mode, and Basis and Digits are already there with venture money.
5. **Promotion candidate from stage 1:** report 12's *AP payment integrity* is not a company, but it is a valuable module for SPVs and juniors. Duplicate-payment and redirection-fraud controls are a hard, priced outcome lenders care about.

---

## Ranking and recommendation

| Rank | Candidate | Lens score |
|---|---|---|
| 1 | **S2+S4 merged: Transition Finance Office** (SPV-anchored) | 7.5 |
| 2 | S4 SPV Office (standalone) | 7.0 |
| 3 (tie) | S2 Resources Finance Office; S3 Contractor Cash Desk; S5 ColdCore + MeterProof | 6.5 |

**Choice: the SPV-anchored Transition Finance Office (S4 first, S2 second, S3 as a module).** It is the only AI-finance design where all of these hold:
- the deliverable is beyond the reach of ledger-platform agents;
- churn is under 10%;
- the outcome can be measured against a lender or regulator deadline;
- Melbourne is an advantage;
- a data by-product leads into Track B.

It still only modestly beats staying on expectation (EV ~A$5.0M vs A$3.25M; P(positive) ~47%). That is why sequencing matters.

---

## Sequencing (while employed, then the quit trigger)

**Months 0–3, while employed** (disclose to the employer; no overlap with SaaS customers):
1. **SPV shadow close.** Using public AEMO settlement data and a friendly sponsor's documents, build an agent pipeline that produces one SPV's monthly management pack, DSCR covenant certificate and LGC reconciliation. **Pass:** reviewer time ≤15 hours per SPV per month.
2. **20 interviews** with CIS-awarded sponsors, mid-sized IPPs, funds and commercial asset managers (RES/Blueshore, OX2, CWP, New Energy Management) as *potential customers for a white-label back office*. **Pass:** ≥3 paid pilots or LOIs at ≥A$5k per SPV per month.
3. **5B parser** across ~750 filers and a free overhead/runway benchmark sent to Melbourne juniors. This tests S2's demand and starts the Runway data asset.
4. **Get a PI quote** for a capped SLA plus a penalty indemnity, and sign up a registered tax-agent/CA co-founder.

**Months 4–12:** keep the job while the co-founder delivers 3–5 pilots. **Kill** if fewer than 2 SPV pilots convert, price lands below A$3k per SPV per month, or review time stays above 30 hours per SPV per month.

**Quit trigger:** ≥A$0.5M contracted ARR on ≥3-year terms, with no client above 25% (falling to 10% by year 3), and gross margin ≥45% after month 6.

**Years 2–4:** add juniors through a Melbourne CoSec channel. Add the renewable-build contractor module and the AP-integrity module. Price on a fixed fee + capped credits + gainshare on claims and recoveries.

**Years 4–7:** turn on the asset options when the data supports them. SPV performance data goes into Track B underwriting with a capital partner. 5B data goes into refund advances and small royalties (S7 as the buyer or exit).

**Exit buyers:** Vistra, Automic/Advent, Apex, RES/OX2-type asset managers, or AI-roll-up platforms.

**Never:** take venture debt, sell wholesale to accounting firms, or price the ledger layer per transaction.

---

### Sources (searched 4 Nov 2026)
- Xero month-end agent: xero.com/media-releases/new-ai-innovations-xerocon-denver; channellife.co.nz/story/xero-expands-ai-tools-for-accountants-small-firms
- Intuit AU: quickbooks.intuit.com/au/blog/product-update/intuit-accountant-suite-launch; accountantsdaily.com.au/business/22139; itwire.com (Intuit Intelligence AU)
- MYOB agentic BAS: accountantsdaily.com.au/technology/22894; itbrief.com.au/story/myob-widens-ai-bas-beta-to-australian-small-employers
- Pilot: cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant
- Botkeeper: cpapracticeadvisor.com/2026/02/09/botkeeper-is-closing-its-doors; cfotech.com.au
- Bench: techcrunch.com/2025/02/05/bench-burned-through-135-million-before-shutting-down; techcrunch.com/2025/01/03/inside-the-wild-fall...
- Rillet: fintechfutures.com (Rillet unicorn, Aug 2026)
- HighRadius: businesswire.com/news/home/20260227310299/en
- Digits: cpapracticeadvisor.com/2026/04/07/digits-announces-outcome-based-pricing-for-accounting-firms
- Current/Crete: businesswire.com/news/home/20260602293257/en; accountingtoday.com (Crete US$500M)
- Automic/Advent: automicgroup.com.au/news/advent-completes-acquisition...; Vistra/Leydin Freyer: paminsight.com/epc/article/vistra-acquires-australian-accountancy-firm; Vistra Geni: eqtgroup.com/thinq/case-study/vistras-journey...
- RES/Blueshore and OX2: pv-magazine-australia.com (RES/Blueshore); ox2.com/australia/technologies/technical-and-commercial-management
- Practice multiples: DMY market data (Nov 2025, May 2026)
- Churn references: vendor blogs (accounting-firm retention 85–95%) [unverified]
