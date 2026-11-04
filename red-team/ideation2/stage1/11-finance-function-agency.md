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

The gross-margin path depends on the ratio of human reviewers to clients moving from 1:6 to 1:12–15 as agents take over reconciliations, accruals, AP coding and first-draft reporting. In 2026 a well-run AI-plus-human pod can probably do that within 3–4 years [estimate]. Below ~45% gross margin with VC-funded growth, you get Bench.

**Land and expand:** land with one module that has a hard, painful outcome (a close guarantee, or collections), then expand to the full function within 6–12 months. Target net revenue retention of 120%+ [estimate], driven by adding modules and by outcome fees growing as clients grow.

---

## Idea 1: "Closewise": a guaranteed finance function for VC-backed scaleups and foreign-group subsidiaries (core idea)

| Field | Assessment |
|---|---|
| **One-liner** | A full finance function (close, compliance, payroll, AR/AP, board reporting, FP&A, audit readiness) for **A$5–100M-revenue VC-backed scaleups and Australian subsidiaries of foreign groups**, run by agents with human review. **Wedge:** "the close by BD5, every lodgement on time, ATO penalties on us." **Who pays:** CEOs and boards of scaleups; regional or group CFOs of foreign parents (who want group reporting by BD3 in IFRS/US GAAP). **Outcome priced:** close by day N with no restatement; compliance with zero penalties; payroll and super accuracy; DSO. Typical ACV A$100–250k. |
| **Why now (2026–28)** | (a) Agents now do real close and reconciliation work (Basis, Rillet, Xero JAX's month-end agent) [verified]. (b) Payday super makes every pay run a compliance event [verified]. (c) VC-backed companies are told to cut burn, and finance is often the second hire to go. (d) Foreign parents rationalising APAC overheads want one accountable provider with a clean SLA. (e) No Australian provider sells on outcomes yet [unverified: absence of evidence]. The window closes when Multiplier, Kelly Partners or a mid-tier firm copies the contract, perhaps by 2028–29. |
| **Why Australia / Melbourne** | **Advantages:** a dense VC network (Blackbird, Square Peg, AirTree, OneVentures); Australian complexity (payday super, STP, BAS, FBT, R&D tax incentive) that is moat-like for foreign firms; Australian subsidiaries of US/EU groups need local substance. Melbourne gives access to the Victorian scaleup scene and the founder's network. **Handicap:** a small market. The scale path is ANZ, then the UK and Singapore (similar compliance regimes), or selling the platform to US scaleups' APAC entities. |
| **Unfair inputs** | **Strong:** he *is* the buyer, a practising SaaS CFO who can define "good" and sell CFO-to-CFO and CFO-to-board; a statistician who can price outcomes (the distribution of close days and error rates per client, set the baseline, price the guarantee); a hands-on agent builder; ex-BCG; marketplace and ops scaling (Fulfilio). **Gaps:** (1) **a registered tax agent / CA partner co-founder** (TPB registration is required to provide BAS and tax services for a fee; he can't be the signing agent), ideally ex-Big 4 or mid-tier, with a scaleup or foreign-subsidiary book; (2) **a delivery lead** with payroll and controllership depth, possibly the same person; (3) an agent engineer by year 1. |
| **Market & model** | **TAM:** ~3–5k VC-backed AU/NZ companies above A$2M revenue [estimate] plus several thousand mid-sized foreign subsidiaries [estimate from ABS ~9,900 foreign-owned businesses, 2014–15] → ~6–9k targets × A$120k ≈ **A$0.7–1.1B ANZ** [estimate]. **Plan:** 25 clients (year 2, A$3.5M revenue), 80 (year 4, A$12M), 180 (year 7, A$28M) [estimate]. Gross margin 45% → 70%; EBITDA 20–30% at scale. **Comparables:** Pilot (US, US$1.2B valuation in 2021 [unverified]); Scale Suite and Standard Ledger (AU, input-priced); Multiplier (roll-up). Exit value: tech-enabled services at ~2–4x revenue, or 10–14x EBITDA [estimate]. |
| **Capital & structure** | Bootstrap A$300–500k of founder capital to 10 clients; then optionally a A$3–5M seed from an AU VC or a services-focused fund to accelerate hiring and agent build. Founder ~55–70% after seed; the tax-agent co-founder 10–20% [estimate]. **No acquisitions needed**, though a later bolt-on of a scaleup-focused boutique (A$1–3M fees, ~1x fees) is an option. PI insurance A$20–50k/year [estimate]. |
| **Floor and failure mode** | Failure: churn after outcome misses, or margin stuck at ~35% because agents don't remove enough human hours. **What's left:** a book of recurring contracts saleable to a mid-tier firm or Multiplier at ~0.8–1.2x revenue [estimate from DMY fee multiples, round 1]. With a A$2–4M book that recovers A$1.5–4M. **P(total loss) ~15–20%.** |
| **Outcome distribution (10 yrs)** | Founder equity at year 10, pre-tax. Assumes a modest salary of A$150–200k from year 2 (≈A$1.0–1.2M after tax over 10 yrs), so equity must be ≥~A$2.2M to beat staying. **Total loss 18%:** A$0.2M. **Modest 45%:** A$4–8M revenue boutique sold at 1–1.5x → A$1.5–5M (midpoint A$3M; about half clear the bar). **Good 28%:** A$20–30M revenue, 2.5x → A$15–22M (A$18M). **Great 9%:** ANZ+UK platform, A$60M+ revenue → A$60M. **EV ≈ A$11.8M** (0.04 + 1.35 + 5.0 + 5.4). **Median ≈ A$3M. P(positive) ≈ 59%.** |
| **Cash generation** | Contribution-positive per client from month 3; company cash-positive at ~15–20 clients (~month 15–24) [estimate]. **Can self-fund growth:** yes. Annual fees are billed monthly in advance, there is no inventory, and the main constraint is hiring reviewers. |
| **AI leverage** | Very high, and it **grows with model improvements**: price is anchored to outcomes (close days, penalties avoided, cash collected), while cost falls. Its own data (close-day distributions, error rates per process, per-client baselines) lets it price guarantees better than rivals, which is the founder's statistics edge. Risk: if agents become good enough for clients to self-serve, the human-trust layer must justify the price. |
| **Job satisfaction** | High in years 1–4: designing the contract and the measurement system, building the agent stack, selling to CFOs and boards, hiring a team. Later it becomes a people-heavy professional-services operation (managing quality and churn), which is less novel. It is close to his current job, multiplied, so the novelty comes from the outcome contract and the AI build. |
| **Key risks** | (1) **Agent capability:** the reviewer-to-client ratio doesn't move past ~1:8, so margins stall at Bench-like levels. (2) **Outcome definition disputes:** "material restatement" and "DSO baseline" fights; clients game baselines. (3) **Distribution and conflict:** his employer's peers are the target customers; he can't sell while employed without consent; VC-portfolio sales cycles are fast but churn rises with portfolio failures (scaleup mortality ~10–20% a year [estimate]). |
| **90-day test** | **Can start while employed only with employer consent**: check the employment contract and use a co-founder as the face. (a) Sign **5 design-partner clients at ≥A$6k/month** with a written outcome SLA (BD5, penalty indemnity). (b) Run the first close for 3 of them: **BD5 met, and human review time ≤25 hours per client per month by month 3**. (c) **PI insurer quote ≤A$50k/year** for the penalty indemnity. **Kill** if <3 of 15 qualified CFO/CEO conversations convert, or review hours exceed 40 per client per month after the second close. |

---

## Idea 2: "Cashline": a working-capital agency priced on cash released, with an embedded receivables-finance option

| Field | Assessment |
|---|---|
| **One-liner** | An AR/collections + AP agency for **A$10–100M B2B mid-market companies with long payment terms** (wholesale and distribution, construction subcontractors, manufacturing, labour hire, freight). **Outcome priced:** cash collected and DSO reduced (share of the working capital released, valued at the client's cost of debt), plus AP savings (discounts, duplicates). It lands with AR, expands to the whole finance function, and **optionally funds receivables against the data it now controls** (outcome-based finance: repayment comes from collections the agency manages). |
| **Why now (2026–28)** | Higher-for-longer rates make working capital expensive. Agents can now chase, reconcile and dispute-manage at scale (Xero JAX AR/AP, HighRadius outcome-priced agents) [verified]. The Payment Times Reporting regime publishes big payers' terms [unverified in this session]. Construction insolvencies keep subcontractors' debtor risk high [unverified]. |
| **Why Australia / Melbourne** | Neutral to positive: AU invoice finance is underpenetrated relative to the UK [unverified]; deep private-credit warehouses (MA Financial and others) are available for receivables [verified in round 1: Fundbox/MA warehouse]. Melbourne has a strong manufacturing and distribution base. |
| **Unfair inputs** | Statistics fits exactly: collection propensity scoring, cash-forecast accuracy, credit risk on the receivables. CFO credibility on working capital; Fulfilio gave him an SME logistics and distribution network. **Gaps:** a credit and collections operator; later a credit-fund partner and an ACL/credit specialist if lending to consumers (avoid: B2B only). |
| **Market & model** | Target: ~25–40k AU B2B companies with A$10–100M revenue and DSO >45 days [estimate]. A A$30M company at DSO 60 → 45 releases ~A$1.2M of cash; worth ~A$100k/year at a 8–9% cost of funds [estimate]. **Fee:** base A$3–5k/month + 5–8% of overdue cash collected, or 25–35% of the financing value of the DSO reduction. Contracted ACV A$60–120k, expanding to A$150k+ with the full function. **Optional book:** fund A$20–50M of receivables at 3–5% net margin from year 3, from a warehouse with ~10–15% first-loss equity [estimate]. **Comparables:** HighRadius (enterprise), Resolve and Fundbox (US/AU), traditional agencies at 15–30% contingency [verified as vendor ranges]. |
| **Capital & structure** | Agency: bootstrap A$300–500k. Receivables book: first-loss equity A$2–5M from a family office plus a senior warehouse; founder ~50–65% of the operating company, and a carry/fee interest in the book. |
| **Floor and failure mode** | Failure: outcome fees are lumpy and clients churn once the backlog of old debt is cleared (a "one-off clean-up" problem). Lending adds credit-loss risk. **Floor:** contracted AR+AP base fees and a saleable client book; the receivables book is secured and recoverable. **P(total loss) ~18%.** |
| **Outcome distribution (10 yrs)** | Same salary assumption as idea 1. **Total loss 18%:** A$0.2M. **Modest 47%:** A$3M. **Good 27%:** A$14M (A$20M revenue agency + book platform fee). **Great 8%:** A$45M (a working-capital platform with a A$300M+ book). **EV ≈ A$8.8M** (0.04 + 1.41 + 3.78 + 3.6). **Median ≈ A$3M. P(positive) ≈ 55%** (about 40% of modest outcomes clear the bar). |
| **Cash generation** | Outcome fees from month 1–2 (old debts collected quickly), so cash arrives faster than in idea 1. Cash-positive at ~20 clients (~month 12–18). The book needs external capital. |
| **AI leverage** | Very high: collections is a repetitive, measurable, multichannel task; propensity models improve with data pooled across clients; the outcome (cash in the bank) can't be disputed. |
| **Job satisfaction** | High for the statistician (credit scoring, forecasting, building a lending book). Lower-status collections work in the early years. |
| **Key risks** | (1) **Recurring-revenue cliff:** once DSO falls, outcome fees shrink unless the contract shares ongoing value. (2) **Client relationships:** aggressive collections harm clients' customer relationships, and the agency is blamed. (3) **Credit risk and regulation** if lending is added. |
| **90-day test** | 3 pilot clients; **≥A$500k of >60-day debt collected at ≤8% fee**; DSO down ≥10 days on a like-for-like cohort; **≥1 client converts to the full finance function**. Can run while employed only with a co-founder or operator delivering. **Kill** if collections stall below 40% of >60-day debt. |

---

## Idea 3 (the intersection): "Assay Finance": an outcome-priced finance function for ASX resources juniors and renewable-project SPVs

| Field | Assessment |
|---|---|
| **One-liner** | A specialist finance function for **ASX mining and exploration juniors** (quarterly activity reports and Appendix 5B cash flows, half-year review, exploration cost capitalisation, JMEI/R&D claims, tenement-commitment tracking, capital-raise readiness) and **renewable-energy and storage SPVs and developers** (multi-SPV close, capex capitalisation, lender covenant and DSCR certificates, PPA/LGC/CIS revenue reconciliation, GST). Later **CMPTI claims** for processors from 2027–28. **Who pays:** juniors' boards and company secretaries; developers; infrastructure funds owning SPVs. **Outcome priced:** every ASX lodgement on time (no ASX queries or suspensions from finance); lender reporting delivered by covenant date; claims captured (contingency on CMPTI/R&D/JMEI dollars). |
| **Why now (2026–28)** | (a) ~745 ASX juniors [verified: Mining Journal, 2025], many with 1–3 staff, under a liquidity crunch and cutting costs [verified: MiningNews headline]. (b) Renewables build-out creates hundreds of SPVs (CIS tenders, REZs); developers hire SPV accountants for "month-end close across multiple SPVs … capex tracking … GST/BAS" [verified: job ads]. Outsourced SPV administration exists, but mostly as part of asset managers (SkySpecs, CWP, New Energy Management) [verified]. (c) **CMPTI** creates a 10% refundable offset on processing costs from 1 Jul 2027 [verified: ATO]. (d) S2 climate disclosures roll down to Group 3 in 2027 [verified]. |
| **Why Australia / Melbourne** | **Strong advantage**: the ASX is the world's largest junior-mining listing venue and Australian regulation is the moat. Handicap: the resources community is Perth-centric; a Perth delivery lead is needed. Melbourne is fine for renewables (Victoria's REZs, offshore wind, SEC). |
| **Unfair inputs** | Pricing and statistics (capex forecasting, covenant headroom models), CFO credibility, agent building. **Gaps:** **a resources-sector CFO/company secretary co-founder from Perth** with a junior-mining network; project-finance experience for SPVs. The founder has no resources network today. |
| **Market & model** | ~745 juniors × A$60–120k = **A$45–90M**; plus SPVs at A$30–80k each and developer groups at A$150–400k [estimate]; plus CMPTI/R&D claims as contingency (10–15% of the offset) [estimate]. SAM ~A$100–200M [estimate], small but deep, and it links to Track B (the data on SPV performance and covenant headroom feeds outcome-based finance). **Comparables:** Perth company-secretarial and accounting boutiques (input-priced) [unverified]; SPV admin by asset managers. |
| **Capital & structure** | Bootstrap A$300–600k; a co-founder with 15–25% equity. Founder 55–70%. No external capital needed. |
| **Floor and failure mode** | Mining cycles: juniors run out of cash in downturns and cut services; receivables risk. Renewables SPVs are more stable (contracted revenue, lender-mandated reporting). **Floor:** a recurring book saleable to a Perth firm; specialised IP. **P(total loss) ~18%.** |
| **Outcome distribution (10 yrs)** | **Total loss 18%:** A$0.2M. **Modest 52%:** A$3M. **Good 24%:** A$12M. **Great 6%:** A$35M (becomes the data and finance layer for transition assets, feeding Track B lending or royalties). **EV ≈ A$6.6M** (0.04 + 1.56 + 2.88 + 2.1). **Median ≈ A$3M. P(positive) ≈ 51%** (about 40% of modest outcomes clear the bar). |
| **Cash generation** | Quarterly ASX deadlines create sticky, predictable revenue; cash-positive ~month 12–18. Self-funding. |
| **AI leverage** | High: Appendix 5B and quarterly reports are templated; lender certificates are formulaic; capex classification and claims are pattern-heavy. Covenant data across SPVs is a unique dataset. |
| **Job satisfaction** | Medium-high: links to Track B interests and the energy transition. But the client base is cyclical and small. |
| **Key risks** | (1) Founder lacks the network: dependent on the co-founder. (2) Cyclicality of juniors (2023–25 lithium bust). (3) SPV work is often captured by asset managers and Big 4 project-finance teams. |
| **90-day test** | Interview 15 junior CFOs/company secretaries and 5 developers; **3 paid pilots** (one quarterly cycle for a junior, one multi-SPV close); **one CMPTI or R&D claim mandate at contingency**. **Kill** if fewer than 2 of 20 accept outcome pricing over hourly. Can largely run while employed through a Perth partner. |

---

## Idea 4 (bold): "Exit-Ready": a finance function paid partly in equity and success fees at the next raise or exit

| Field | Assessment |
|---|---|
| **One-liner** | Idea 1's full finance function for VC-backed and PE-owned scaleups, but **~30–40% of the fee is deferred and converted into a success fee or warrants**, paid when the company raises, refinances or sells. **Outcome priced:** "clean diligence", i.e. a financial-due-diligence and QoE pass with no material adjustments, a fundraising or exit timeline met, and audit-ready accounts. The agency becomes a **diversified portfolio of small equity stakes** in 100–200 scaleups, with services cash flow underneath. |
| **Why now (2026–28)** | Burn discipline makes cash-light finance attractive; secondary markets and continuation funds create liquidity for small stakes; PE "100-day plans" demand fast finance upgrades in portfolio companies; AI cuts delivery cost enough to afford deferral. |
| **Why Australia / Melbourne** | AU VC is concentrated, and a few funds cover hundreds of companies, so a portfolio-wide deal with 2–3 funds gives distribution. Handicap: thinner exit markets than the US. |
| **Unfair inputs** | A CFO who has been through raises, diligence and exits; a statistician who can price a portfolio of options; BCG/VC network. Gaps: a VC/fund-structuring adviser; same tax-agent co-founder as idea 1. |
| **Market & model** | Same TAM as idea 1. Cash price ~A$60–100k + deferred A$40–60k per client per year as success fee (paid at a liquidity event at 1.5–2x) or warrants of ~0.25–0.5% [estimate]. With ~150 clients over 10 years and a 10–15% "meaningful exit" rate, the equity book could be worth A$10–40M [estimate]; this depends heavily on 1–2 outliers. |
| **Capital & structure** | Needs more working capital (deferred fees): A$2–4M from a fund partner or a structured facility; or put the warrants in a separate vehicle with a VC LP. Founder ~45–60%. |
| **Floor and failure mode** | The services cash book is the floor (as in idea 1); warrants may be worth nothing; deferred fees are written off when companies fail. **P(total loss) ~22%.** |
| **Outcome distribution (10 yrs)** | **Total loss 22%:** A$0.2M. **Modest 38%:** A$2.5M. **Good 28%:** A$15M. **Great 12%:** A$50M (one or two portfolio outliers). **EV ≈ A$11.2M** (0.04 + 0.95 + 4.2 + 6.0). **Median ≈ A$2.5M. P(positive) ≈ 52%** (about a third of modest outcomes clear the bar). |
| **Cash generation** | Slower than idea 1: cash-positive ~month 24–30; growth partially funded by external working capital. |
| **AI leverage** | High: it lowers the cash cost of delivery so deferral is affordable; data on hundreds of scaleups' financials improves the pricing of each warrant. |
| **Job satisfaction** | Very high: it combines CFO work, investing and portfolio construction. |
| **Key risks** | (1) Adverse selection: cash-poor, weak companies choose deferral. (2) Conflicts and independence (auditor-like roles in companies in which the agency holds equity; it must avoid audit and assurance work). (3) Long time to liquidity. |
| **90-day test** | A portfolio deal: **one VC or PE fund agrees to refer ≥5 portfolio companies**, and **3 sign** with a deferred component. **Kill** if only the weakest companies accept deferral (selection test: compare with the fund's own quartile ranking). |

---

## Ranking and top pick

| Rank | Idea | EV (A$, founder value, 10 yrs) | Median | P(positive) | P(total loss) | Cash-positive | Start while employed? |
|---|---|---|---|---|---|---|---|
| **1** | **Closewise: guaranteed finance function for scaleups and foreign subsidiaries** | **~11.8M** | ~3M | **~59%** | ~18% | 15–24 months | Only with consent and a co-founder |
| 2 | Exit-Ready (bold): deferred fees and warrants | ~11.2M | ~2.5M | ~52% | ~22% | 24–30 months | Same |
| 3 | Cashline: working-capital agency plus receivables book | ~8.8M | ~3M | ~55% | ~18% | 12–18 months | With an operator |
| 4 | Assay Finance: resources and energy finance function (intersection) | ~6.6M | ~3M | ~51% | ~18% | 12–18 months | Yes, through a Perth partner |

All EVs are subjective; treat the ranking, not the decimals, as the output. Round-1 base rates (a ~5–6% great outcome) would cut every EV by ~30–40%.

**Top pick: Closewise, with Cashline's collections module and Exit-Ready's deferred-fee option as later product lines, not separate companies.**

**The first wedge: "Close by BD5, zero ATO penalties, or we pay"** for **VC-backed scaleups (A$5–50M revenue) and Australian subsidiaries of foreign groups**.
- **The outcome is unambiguous.** A date and a penalty count can't be gamed, unlike DSO baselines.
- **The buyer is senior and the pain is acute.** Boards, VCs and group CFOs pay for reliability; ACVs of A$100–200k are 10–20x Bench's.
- **It's his own domain.** He can sell CFO-to-CFO from day 1, and the measurement system (close-day distributions, error rates) is a statistics problem.
- **It opens the full function.** A close owner sees the ledger, payroll and AR, so expanding into collections (Cashline) and FP&A comes naturally.
- **It avoids Bench's mistakes:** higher price, mid-market rather than micro, client-owned systems, gross margin ≥45% from the first year, growth funded from cash.

**What to watch:** whether the human-review ratio really moves from 1:6 to 1:12+ by year 3. If it doesn't, this is a good boutique (the modest outcome) rather than a platform. The 90-day test is designed to measure exactly that.

**Who to hire first:** a TPB-registered tax agent / CA co-founder with a scaleup or foreign-subsidiary book (15–20% equity), and one agent engineer. Resources/energy (Assay) is the best second vertical once the platform works, because it uses the same engine and links directly to Track B.

Main sources: Techcouver/TechCrunch, NCFA and Wikipedia (Bench); Accounting Today (Digits outcome pricing, Xero JAX); Bloomberg and BusinessWire (Basis, Multiplier); IT Brief and ChannelLife (Multiplier acquisitions); Scale Suite and Standard Ledger (AU pricing); Outsource Accelerator/AFR (ConnectOS, TOA); ABS Counts of Australian Businesses 2021–25; ATO tax transparency; ATO, PwC and Grant Thornton (CMPTI); Mining Journal and MiningNews (juniors); CreditorWatch and Resolve (collection fees); SkySpecs, CWP and job ads (SPV finance). Round-1 verified items (payday super, AASB S2, Campfire/Numeric/Accrual) are reused from `red-team/ideation/stage1/03-finance-function-ai.md`.
