# Stage 1, round 2, lens 11: an AI-native finance function priced on outcomes (Track A)

Ideation agent: AI-Native Outcome-Priced Finance Function (core product and market). 4 Nov 2026.
16 web searches. Figures are labelled **[verified: source]**, **[estimate]** or **[unverified]**. US$ is shown as US$; everything else is AUD.

---

## 0. What the market looks like (Nov 2026)

**Software is crowded and well funded; the work itself is not yet sold on outcomes in Australia.**

| Player | What it tells us |
|---|---|
| **Bench** (>US$100M raised) | Shut down without notice on 27 Dec 2024; bought by Employer.com on 30 Dec [verified: TechCrunch via Techcouver, NCFA]. No official reason. Reported causes: a cash crunch, negative unit economics on ~US$250/month human-heavy bookkeeping, service decline after layoffs, and a proprietary platform that trapped customers' books [unverified: secondary analysis]. |
| **Pilot** (US) | ~US$27M revenue (2024); "AI Accountant" launched Feb 2026; US$99/month AI-only tier [unverified: aggregators]. |
| **Digits** | Outcome-based pricing for accounting *firms* from Apr 2026; business owners still pay a subscription [verified: Accounting Today]. |
| **Basis / Rillet / Campfire / Numeric** | Basis US$100M at US$1.15B (Feb 2026) [verified: Bloomberg]; Rillet ~US$1B Series C (Aug 2026) [unverified]; Campfire and Numeric US$50–65M rounds [verified in round 1]. |
| **Multiplier** | US$35M Series B (Aug 2026); 10 acquisitions incl. Oxygen Advisors and Greenhawk (NZ, serving AU startups); no AU acquisition found [verified: BusinessWire, IT Brief]. |
| **Xero JAX, Intuit** | JAX is becoming an agentic "superagent" (bank recs, AR/AP, month-end agent); accountants report early failures [verified: Accounting Today, Public Accountant]. Intuit launched an AI-native Accountant Suite in AU [verified: headline only]. |
| **AU outsourced finance** | Full department from ~A$1,500/month, most clients A$2,500–6,000; mid-tier A$5–15k+; fractional CFO A$2.5–15k. All priced by scope or hours [verified as vendor-published: Scale Suite, Standard Ledger]. |
| **Offshore BPO** | ConnectOS (Melbourne) ~A$100M revenue, >2,500 staff [verified: AFR via Outsource Accelerator]; TOA >4,180 staff [self-reported]. An offshore finance seat costs ~A$2,500–4,500/month. |

**Conclusions.**
1. **No one in Australia sells the finance function to companies on outcomes** [unverified: absence of evidence from 4 searches].
2. **Bench is the anti-pattern:** cheap, micro-SMB, human-heavy, proprietary ledger, growth at negative gross margin. Each design choice below inverts one of those.
3. **AI is a commodity input; the moat is the outcome contract:** the measurement, the guarantee and the insurance behind it, and the CFO/board trust. This gets *stronger* as models improve, because cost falls while price is anchored to outcome value.
4. **The buyer already spends ~A$350–500k a year.** A A$20M-revenue company carries a controller, an accountant, an AP/AR officer, part of payroll, a BAS/tax agent and fractional CFO time [estimate].
5. **Market:** 2.73M trading businesses; ~8.5% (~230k) turn over ≥A$2M, growing ~4% a year [verified: ABS Counts of Australian Businesses 2021–25]. Perhaps 60–90k in A$2–100M have a finance function worth outsourcing [estimate]. ~9,900 majority foreign-owned operating businesses [verified: ABS for DFAT, 2014–15; old]; ~745 ASX mining juniors [verified: Mining Journal, 2025].

**Tailwinds that make outcomes measurable and errors expensive:** payday super from 1 Jul 2026 (super within 7 business days of each pay run) [verified in round 1: ATO]; criminal wage underpayment offence from 1 Jan 2025 [unverified]; AASB S2 Group 3 from 1 Jul 2027 [verified in round 1]; Critical Minerals Production Tax Incentive, a refundable 10% offset on eligible processing costs for 2027–28 to 2039–40 [verified: ATO, PwC].

**Discarded:** cheap AI bookkeeping for micro-SMBs (this is Bench; Xero/Intuit give it away); generic accounting roll-up (banned; Multiplier, Kelly Partners, Count); CFO-office software (US$50–100M rivals); a standalone collections agency (low-status, regulated; better as a module); offshore BPO with an AI wrapper (scale game AI erodes); outcome-priced R&D tax claims (small, ATO scrutiny; keep as a module).

---

## 1. Design principles shared by all four ideas

**The outcome-pricing menu** (a contract template the four ideas reuse):

| Module | Outcome priced | Fee structure | Risk the agency takes |
|---|---|---|---|
| **Close and reporting** | Board pack and management accounts by business day N (BD5 → BD3), with no material post-close adjustments | Fixed monthly fee; 10–20% service credit for each missed close or restatement; bonus for BD3 | Late close or restatement |
| **Compliance** (BAS/GST, PAYG, payday super, STP, FBT, income tax prep) | Every lodgement on time and accurate | Fixed fee plus a **penalty indemnity**: the agency pays ATO penalties and GIC caused by its own errors (capped, backed by PI insurance) | ATO penalties and interest |
| **Payroll** | Every pay accurate and on time; super within 7 days | Per-employee fee; agency bears remediation cost of its own errors | Underpayment remediation |
| **AR / collections** | Cash collected; DSO reduced against a 12-month baseline | Base fee + **5–8% of overdue cash collected** (agencies charge 15–30% [verified as vendor ranges: CreditorWatch, Resolve]) or a share of the working-capital value of DSO reduction | Unpaid effort |
| **AP / payments** | Paid accurately and on time; duplicates caught; early-payment discounts captured | Per-payment fee + 20–30% of discounts and duplicate recoveries captured | Late fees, duplicate payments |
| **FP&A** | 13-week cash forecast within ±5%; budget variance explained by BD7 | Fixed fee + accuracy bonus | Forecast misses (reputation only) |

**How risk is shared.**
- Base fees cover ~70–75% of expected revenue, so the agency stays solvent in a bad month.
- ~10–15% of revenue is at risk through service credits; ~15–25% is upside through outcome fees.
- Liability is capped at 12 months of fees and backed by PI insurance.
- **The client owns its systems and data** (its own Xero, NetSuite or MYOB file, its bank feeds), with escrowed runbooks. This is the anti-Bench clause and a sales advantage: "if we disappear, your books don't".

**Unit economics: one A$20M-revenue client** [all estimates]

| Line | Traditional outsourced firm | AI-native agency, year 1 | AI-native agency, year 4 |
|---|---|---|---|
| Price per year (base + outcome fees) | A$90–150k | A$150–180k | A$140–170k (price held; outcome fees rise) |
| Human delivery | ~1.2–1.5 FTE (A$100–140k) | Client lead at 1:6 (A$28k) + analyst at 1:3 (A$25k) + CFO/partner at 1:20 (A$15k) | Lead at 1:12 (A$14k) + analyst at 1:6 (A$12k) + partner at 1:30 (A$10k) |
| AI compute and platform | small | A$10–15k | A$5–8k |
| PI insurance, tax-agent sign-off, penalty reserve | A$3k | A$6k | A$5k |
| **Gross margin** | **~25–35%** | **~45–55%** | **~70–75%** |

Gross margin rises as the ratio of human reviewers to clients moves from 1:6 to 1:12–15, with agents doing reconciliations, accruals, AP coding and first-draft reporting [estimate]. Below ~45% gross margin with VC-funded growth, you get Bench. **Land and expand:** land with one module that has a hard outcome (the close guarantee or collections), then add modules within 6–12 months; target net revenue retention of 120%+ [estimate].

---

## Idea 1: "Closewise": a guaranteed finance function for VC-backed scaleups and foreign-group subsidiaries (core)

| Field | Assessment |
|---|---|
| **One-liner** | Full finance function (close, compliance, payroll, AR/AP, board reporting, FP&A, audit readiness) for **A$5–100M VC-backed scaleups and Australian subsidiaries of foreign groups**, run by agents with human review. **Wedge:** "close by BD5, every lodgement on time, ATO penalties on us." **Who pays:** CEOs and boards; regional or group CFOs (who want group reporting by BD3 under IFRS/US GAAP). **Priced on** close day and restatements, zero penalties, payroll/super accuracy, DSO. ACV A$100–250k. |
| **Why now (2026–28)** | Agents now do real close and reconciliation work (Basis, Rillet, JAX month-end agent) [verified]; payday super makes every pay run a pass/fail event [verified]; VC-backed companies are cutting burn; foreign parents want one accountable APAC provider; no AU provider sells on outcomes [unverified: absence of evidence]. The window closes when Multiplier, Kelly Partners or a mid-tier firm copies the contract (~2028–29). |
| **Why Australia / Melbourne** | Dense VC network (Blackbird, Square Peg, AirTree); Australian complexity (payday super, STP, BAS, FBT, R&D incentive) deters foreign providers; foreign subsidiaries need local substance. **Handicap:** a small market, so scale means ANZ, then the UK and Singapore (similar regimes). |
| **Unfair inputs** | He *is* the buyer: a practising SaaS CFO who defines "good" and sells CFO to CFO. As a statistician he can price the guarantees (close-day and error distributions, client baselines). Agent builder, ex-BCG, scaled Fulfilio. **Gaps:** (1) **a TPB-registered tax agent / CA co-founder** (registration is needed to provide BAS and tax services for a fee), ideally with a scaleup or foreign-subsidiary book; (2) a payroll and controllership delivery lead; (3) an agent engineer by year 1. |
| **Market & model** | ~3–5k VC-backed AU/NZ companies above A$2M plus several thousand mid-sized foreign subsidiaries → ~6–9k targets × A$120k ≈ **A$0.7–1.1B ANZ** [estimate]. **Plan:** 25 clients/A$3.5M revenue (year 2); 80/A$12M (year 4); 180/A$28M (year 7). Gross margin 45% → 70%; EBITDA 20–30% at scale [estimate]. **Comparables:** Pilot (US$1.2B in 2021 [unverified]); Scale Suite and Standard Ledger (input-priced); Multiplier. Exit at ~2–4x revenue / 10–14x EBITDA for tech-enabled services [estimate]. |
| **Capital & structure** | Bootstrap A$300–500k to 10 clients; optional A$3–5M seed. Founder ~55–70%; co-founder 10–20%. No acquisitions needed (a ~1x-fees boutique bolt-on is optional). PI insurance ~A$20–50k/yr [estimate]. |
| **Floor and failure mode** | Failure means churn after missed outcomes, or margin stuck at ~35%. **Floor:** a recurring book saleable to a mid-tier firm or Multiplier at ~0.8–1.2x revenue [estimate, DMY multiples via round 1]. **P(total loss) ~18%.** |
| **Outcome distribution (10 yrs)** | Founder equity at year 10. Assumes a A$150–200k salary from year 2 (~A$1.0–1.2M after tax), so equity of ≥~A$2.2M beats staying. Loss 18% → A$0.2M; modest 45% → A$3M (A$4–8M revenue boutique at 1–1.5x; about half clear the bar); good 28% → A$18M (A$20–30M revenue at 2.5x); great 9% → A$60M (ANZ+UK platform). **EV ≈ A$11.8M; median ≈ A$3M; P(positive) ≈ 59%.** |
| **Cash generation** | Contribution-positive per client from month 3; company cash-positive at 15–20 clients (~month 15–24). **Self-funding:** monthly billing in advance, no inventory; hiring reviewers is the constraint. |
| **AI leverage** | Very high, and **rising with model quality**: price is anchored to outcomes while cost falls. Its own data on close days and error rates by process lets it price guarantees better than rivals. Risk: if clients can self-serve with agents, the trust layer must justify the price. |
| **Job satisfaction** | High in years 1–4: contract and measurement design, the agent build, selling to boards, team building. Later it becomes a people-heavy services operation, close to his current job multiplied. |
| **Key risks** | (1) **Agent capability:** the reviewer-to-client ratio stalls at ~1:8 and margins look like Bench's. (2) **Disputes over outcome definitions** ("material restatement", baselines). (3) **Distribution and conflict:** his employer's peers are the customers; scaleup mortality (~10–20%/yr [estimate]) drives churn. |
| **90-day test** | **While employed only with employer consent**, with the co-founder as the face. (a) **5 design partners at ≥A$6k/month** on a written outcome SLA. (b) First closes for 3: **BD5 met, review time ≤25 hours per client per month by month 3**. (c) **PI quote ≤A$50k/yr** covering the penalty indemnity. **Kill** if <3 of 15 qualified conversations convert, or review time exceeds 40 hours per client per month after the second close. |

---

## Idea 2: "Cashline": a working-capital agency priced on cash released, with a receivables-finance option

| Field | Assessment |
|---|---|
| **One-liner** | AR/collections + AP for **A$10–100M B2B companies with long terms** (distribution, construction subcontractors, manufacturing, labour hire, freight). **Priced on** overdue cash collected (5–8%, against agencies' 15–30% [verified as vendor ranges: CreditorWatch, Resolve]) or 25–35% of the financing value of DSO reduction, plus a share of AP discounts and duplicates recovered. Expands into the full function and, later, **funds receivables it already manages** (outcome-based finance: repayment comes from collections it runs). |
| **Why now** | Expensive working capital; agents now chase, reconcile and manage disputes at scale (JAX AR/AP; HighRadius sells outcome-priced agents) [verified]. |
| **Why Australia / Melbourne** | Neutral-positive: private-credit warehouses for receivables exist (MA Financial/Fundbox) [verified in round 1]; Melbourne's manufacturing and distribution base; Fulfilio network. |
| **Unfair inputs** | Collection-propensity and credit scoring, cash forecasting, CFO credibility. **Gaps:** a credit/collections operator; later a credit-fund partner. B2B only (avoid consumer credit licensing). |
| **Market & model** | ~25–40k target companies [estimate]. A A$30M company cutting DSO 60→45 releases ~A$1.2M, worth ~A$100k/yr at 8–9% [estimate]. ACV A$60–120k, A$150k+ with the full function. Optional A$20–50M receivables book at 3–5% net margin from year 3, 10–15% first-loss equity [estimate]. |
| **Capital & structure** | Agency bootstrapped (A$300–500k); book needs A$2–5M first-loss from a family office plus a warehouse. Founder ~50–65% of the operating company plus a carry on the book. |
| **Floor and failure mode** | Outcome fees fall once the old-debt backlog is cleared; aggressive chasing harms client relationships; credit losses if lending. Floor: base fees, a saleable book, secured receivables. **P(total loss) ~18%.** |
| **Outcome distribution (10 yrs)** | Loss 18% → A$0.2M; modest 47% → A$3M; good 27% → A$14M; great 8% → A$45M (platform with a A$300M+ book). **EV ≈ A$8.8M; median ≈ A$3M; P(positive) ≈ 55%.** |
| **Cash generation** | Fastest of the four: old debts produce fees in months 1–2; cash-positive ~month 12–18. The book needs outside capital. |
| **AI leverage** | Very high; the outcome (cash in the bank) is indisputable, and pooled payment-behaviour data improves with every client. |
| **Job satisfaction** | High on modelling and building a credit book; lower-status collections work early. |
| **Key risks** | (1) Recurring-revenue cliff after the clean-up. (2) Client-relationship damage. (3) Credit and regulatory risk if lending. |
| **90-day test** | 3 pilots: **≥A$500k of >60-day debt collected at ≤8%**, DSO down ≥10 days, **≥1 converts to the full function**. Needs an operator to deliver while employed. **Kill** if <40% of >60-day debt is collected. |

---

## Idea 3 (the intersection): "Assay Finance": a finance function for ASX resources juniors and renewable-project SPVs

| Field | Assessment |
|---|---|
| **One-liner** | Specialist finance function for **ASX mining juniors** (quarterly activity reports and Appendix 5B, exploration capitalisation, JMEI/R&D claims, raise readiness) and **renewable and storage SPVs** (multi-SPV close, capex capitalisation, lender covenant/DSCR certificates, PPA/LGC/CIS revenue reconciliation), later **CMPTI claims** for processors. **Priced on** ASX and lender deadlines met with no finance-caused queries, plus contingency (10–15%) on incentive dollars captured. |
| **Why now** | ~745 ASX juniors [verified: Mining Journal], many with 1–3 staff and facing a liquidity crunch [verified: MiningNews headline]. CIS/REZ build-out creates hundreds of SPVs; developers hire for "month-end close across multiple SPVs … capex tracking … GST/BAS" [verified: job ads]. CMPTI starts 1 Jul 2027 [verified: ATO]. |
| **Why Australia / Melbourne** | **Strong**: the ASX is the world's main junior-mining venue, and local rules are the moat. Handicap: resources are Perth-centric, so a Perth lead is needed. Melbourne suits renewables (Victorian REZs, offshore wind, SEC). |
| **Unfair inputs** | Capex forecasting, covenant-headroom modelling, CFO credibility, agents. **Gap:** a Perth resources CFO/company-secretary co-founder; project-finance depth. No resources network today. |
| **Market & model** | Juniors ~745 × A$60–120k = A$45–90M; SPVs A$30–80k each; developer groups A$150–400k; plus contingency on claims. SAM ~A$100–200M [estimate]: small but deep. Covenant and performance data on SPVs feeds Track B (outcome-based finance). |
| **Capital & structure** | Bootstrap A$300–600k; co-founder 15–25%; founder 55–70%. |
| **Floor and failure mode** | Junior cycles (the 2023–25 lithium bust) cut budgets; SPV work is often captured by asset managers (SkySpecs, CWP) [verified] or Big 4 project-finance teams. Floor: a recurring book saleable to a Perth firm. **P(total loss) ~18%.** |
| **Outcome distribution (10 yrs)** | Loss 18% → A$0.2M; modest 52% → A$3M; good 24% → A$12M; great 6% → A$35M (the finance and data layer for transition assets). **EV ≈ A$6.6M; median ≈ A$3M; P(positive) ≈ 51%.** |
| **Cash generation** | Quarterly ASX and lender deadlines give sticky revenue; cash-positive ~month 12–18; self-funding. |
| **AI leverage** | High: Appendix 5B, quarterlies and lender certificates are templated; capex classification and claims are pattern-heavy. |
| **Job satisfaction** | Medium-high; links to Track B and the energy transition, but the client base is small and cyclical. |
| **Key risks** | (1) Network depends on the co-founder. (2) Cyclicality. (3) Incumbent asset managers bundle SPV finance. |
| **90-day test** | 20 interviews (15 junior CFOs/company secretaries, 5 developers); **3 paid pilots** (one quarterly cycle, one multi-SPV close); **1 claim mandate at contingency**. **Kill** if <2 of 20 accept outcome pricing. Can run while employed through a Perth partner. |

---

## Idea 4 (bold): "Exit-Ready": a finance function paid partly in success fees and warrants

| Field | Assessment |
|---|---|
| **One-liner** | Idea 1's service for VC- and PE-backed companies, with **30–40% of the fee deferred** into a success fee (1.5–2x, paid at the next raise, refinancing or sale) or warrants (~0.25–0.5%). **Priced on** "clean diligence" (QoE with no material adjustments), raise or exit timelines met, and audit-ready accounts. The agency builds a **portfolio of small stakes in 100–200 companies** on top of services cash flow. |
| **Why now** | Burn discipline makes cash-light finance attractive; secondaries and continuation funds create liquidity for small stakes; AI cuts delivery cost enough to afford deferral. |
| **Why Australia / Melbourne** | Concentrated AU VC: a deal with 2–3 funds reaches hundreds of companies. Handicap: thinner exit markets. |
| **Unfair inputs** | A CFO who has done raises, diligence and exits; option pricing; VC and BCG network. Gap: fund-structuring adviser; the same tax-agent co-founder as idea 1. |
| **Market & model** | Same TAM as idea 1. Cash A$60–100k + deferred A$40–60k per client per year. ~150 clients over 10 years at a 10–15% meaningful-exit rate → equity book A$10–40M [estimate], driven by 1–2 outliers. |
| **Capital & structure** | A$2–4M of working capital to fund deferral (fund partner or structured facility), or warrants held in a vehicle with a VC LP. Founder ~45–60%. |
| **Floor and failure mode** | Services book is the floor; deferred fees written off on failures; warrants may be worthless. **P(total loss) ~22%.** |
| **Outcome distribution (10 yrs)** | Loss 22% → A$0.2M; modest 38% → A$2.5M; good 28% → A$15M; great 12% → A$50M. **EV ≈ A$11.2M; median ≈ A$2.5M; P(positive) ≈ 52%.** |
| **Cash generation** | Slower: cash-positive ~month 24–30, partly funded externally. |
| **AI leverage** | Lower delivery cost funds the deferral; financial data across hundreds of scaleups prices each warrant. |
| **Job satisfaction** | Very high: CFO work plus investing. |
| **Key risks** | (1) Adverse selection: weak, cash-poor companies choose deferral. (2) Independence conflicts (no audit or assurance work). (3) Long time to liquidity. |
| **90-day test** | One VC/PE fund refers ≥5 portfolio companies and **3 sign with deferral**. **Kill** if only the fund's bottom-quartile companies accept. |

---

## Ranking and top pick

| Rank | Idea | EV (A$) | Median | P(positive) | P(total loss) | Cash-positive |
|---|---|---|---|---|---|---|
| **1** | **Closewise: guaranteed finance function (scaleups, foreign subsidiaries)** | **~11.8M** | ~3M | **~59%** | ~18% | 15–24 months |
| 2 | Exit-Ready (bold): deferred fees and warrants | ~11.2M | ~2.5M | ~52% | ~22% | 24–30 months |
| 3 | Cashline: working-capital agency + receivables book | ~8.8M | ~3M | ~55% | ~18% | 12–18 months |
| 4 | Assay Finance: resources and energy (intersection) | ~6.6M | ~3M | ~51% | ~18% | 12–18 months |

EVs are subjective; round-1 base rates (~5–6% great) would cut each by ~30–40%. Rank, not decimals, is the output.

**Top pick: Closewise. Fold Cashline (collections) and Exit-Ready (deferral) in as later product lines, and make Assay the second vertical.**

**The first wedge: "Close by BD5, zero ATO penalties, or we pay"** for VC-backed scaleups (A$5–50M revenue) and Australian subsidiaries of foreign groups. Why this wedge:
- **The outcome is ungameable.** A date and a penalty count can't be argued, unlike a DSO baseline.
- **The buyer is senior and the pain is acute.** ACVs of A$100–200k are 10–20x Bench's.
- **He can sell it on day 1,** CFO to CFO, and pricing the guarantee is a statistics problem.
- **The close owner sees the ledger, payroll and AR,** so collections and FP&A follow.
- **It inverts Bench:** a higher price, mid-market clients, client-owned systems, ≥45% gross margin from year 1, and growth funded from cash.

**The variable to watch:** whether the ratio of human reviewers to clients moves from 1:6 to 1:12+ by year 3. If it doesn't, this is a good boutique, not a platform. The 90-day test measures exactly that.

**First hires:** a TPB-registered tax agent / CA co-founder with a scaleup or foreign-subsidiary book (15–20% equity), and an agent engineer.

Sources: Techcouver/TechCrunch and NCFA (Bench); Accounting Today (Digits, Xero JAX); Bloomberg and BusinessWire (Basis, Multiplier); IT Brief and ChannelLife (Multiplier); Scale Suite and Standard Ledger (AU pricing); Outsource Accelerator/AFR (ConnectOS); ABS Counts of Australian Businesses; ABS/DFAT foreign ownership; ATO and PwC (CMPTI); Mining Journal and MiningNews; CreditorWatch and Resolve; SkySpecs, CWP and job ads (SPVs). Round-1 verified items are reused from `red-team/ideation/stage1/03-finance-function-ai.md`.
