# 14 — Skeptic: Outcome-Priced Finance Services (Track A)

Round 2, stage 1. Lens: build the strongest case against Track A (an AI-native, outcome-priced agency that runs the whole finance function), then design the version most likely to end well, and compare it with Track B. 4 Nov 2026. Australian English, AUD. Labels: **[verified: source]**, **[estimate]**, **[unverified]**. Some sites (e.g. bdo.com.au) were blocked from this session.

---

## Part 1. The case against Track A (steelman)

### 1. The category has a body count, including well-funded players
- **Bench** (venture-backed AI bookkeeping for US SMEs, 600+ staff) **shut down without notice on 27 Dec 2024**. Employer.com bought it three days later. Reports say a bank called in its venture debt [verified: TechCrunch 30 Dec 2024; GeekWire; BetaKit]. Customer counts reported vary from ~12,000 to 35,000.
- **Botkeeper** (AI bookkeeping for accounting firms, 11 years old) **announced an orderly wind-down in Feb 2026**. The CEO blamed consolidation among its largest clients, which cut revenue. Xendoo bought the platform [verified: Accounting Today; CPA Practice Advisor 9 Feb 2026; CFO Brew 17 Feb 2026]. A reported ~US$90M of funding is [unverified].
- **Pilot** raised ~US$222M (US$1.2B valuation, 2021). Its 2024 revenue is reported at only ~US$27M [unverified: secondary tracker]. In early 2026 it launched a fully autonomous "AI Accountant" and a US$99/month AI-only tier [unverified: secondary]. **The best-funded "service + software" bookkeeper is now cutting its own price towards software levels.**

Lesson: a services business priced like software fails in one of two ways. Either it can't automate fast enough and margins collapse (Bench), or its clients consolidate or churn and revenue falls faster than costs (Botkeeper).

### 2. Venture capital is flooding both the tools and the firms
- **Basis** (agents for accounting firms): US$100M Series B at US$1.15B valuation, Feb 2026, led by Accel [verified: Built In; Financial IT].
- **Rillet** (AI-native ERP for mid-market companies): US$25M Series A (Sequoia, Jun 2025), US$70M Series B (a16z/ICONIQ, Aug 2025), then a reported US$100M at US$1B (Aug 2026) [verified A/B: CPA Practice Advisor, Built In; C: IT Brief, two sources].
- **AI roll-ups of accounting firms:** Crete (now "Current", backed by Thrive) planned to spend US$500M buying CPA firms and putting AI into them [verified: Reuters via Yahoo, Jun 2025; Accounting Today rebrand]. Multiplier, Modus and others are doing the same. Round 1 already found that Multiplier, Kelly Partners and Count are buying in Australia.
- Europe: Neno raised €6.6M in Aug 2026 for an "AI-native financial services" firm that bundles accounting, tax and admin for SMEs [verified: Vestbee].

So the idea of an "AI-native finance agency" is **already a funded category** with US$1B+ valuations. A Melbourne founder bootstrapping with A$1M isn't early. He'd be the twentieth entrant, without the capital.

### 3. The ledger platforms are building the agent themselves
- **Xero JAX**: auto bank reconciliation in real time (target >80% of lines; 113 of 118 in a Feb 2026 demo), plus a **month-end agent that prepares prepayment and amortisation journals** for review. Xero has partnered with Anthropic [verified: Xero media release, Xerocon London Jul 2026; Accounting Today; CFOtech].
- **MYOB**: AI tools for BAS (Mar 2026), a compliance agent that flags issues before lodgement, and AI Studio with AWS for agents inside Acumatica (May 2026) [verified: Accountants Daily; IT Brief AU]. Claims of an "agentic BAS" are [unverified].
- **Intuit** launched an AI-native Accountant Suite in Australia in Feb 2026 [unverified: single snippet].

For SMEs on Xero or MYOB, the cheap 60–80% of the work (reconciliation, coding, accruals, BAS prep) becomes a **feature of the software they already pay for**. An agency's margin then comes only from the hard 20%: judgement, exceptions and accountability. That 20% is the part that scales linearly with people.

### 4. Offshore labour sets a hard ceiling on price
A Philippine bookkeeper costs about **A$8–25/hour**, against A$40–80 onshore. A managed full-time bookkeeper costs ~A$1,800–2,200 a month [verified: Scalesuite Oct 2025; Helpware; HireTalent.ph, all vendor sources]. After hidden costs (management, 18–24% attrition) the gap narrows, but every Australian firm already has this option. Offshore staff can't lodge BAS under their own registration, so a **registered agent onshore remains the bottleneck** [verified: vendor source, consistent with the TASA].

### 5. Regulation and liability fall on the agency, not the model
- Anyone who provides BAS or tax services for a fee must be a **registered BAS or tax agent under the Tax Agent Services Act 2009**, carry **PI insurance that meets TPB requirements**, and meet CPE and Code of Conduct duties. The TPB does terminate registrations and ban agents [verified: TPB site; TPB enforcement releases].
- The TPB's **draft AI guidance, TPB(I) D62/2026 (Mar 2026)**, says practitioners remain **ultimately responsible** for AI outputs and must check them and apply professional judgement [verified: TPB exposure draft via dig.watch]. **AI doesn't remove the supervising human from compliance work; it makes that person liable for more volume.**
- Outcome pricing makes it worse. If you promise "error-free BAS", you've written a warranty your PI policy may exclude (contractual liability). Every miss becomes a fee dispute *and* a claim.

### 6. Outcome pricing is hard to define, easy to game and rare in practice
- An Orb 2026 sample puts pure outcome-based pricing at **3.8% of AI products (down from 4.5%)**. Hybrid pricing (base fee plus outcome kicker) is the norm [verified: Orb blog; vendor source].
- In finance, most outcomes **depend on the client**. "Close by day 5" fails if the client approves invoices late. "DSO down 10 days" swings with the client's customer mix and the economy. "Error-free compliance" can only be proven after an ATO review years later. The outcome you can measure cleanly (cash collected) already has a market price: debt collection contingency fees of 10–25% [estimate].
- So "outcome pricing" mostly turns out to be **a fixed fee with SLA credits**. That's fine, but it's not a moat. It's the price of entry.

### 7. Client churn follows funding cycles
Startup and scale-up clients cut outsourced finance when cash is short, then get acquired or hire an in-house CFO when they succeed. Either way they leave. ASX juniors are worse: in the Sept 2024 quarter, average junior cash fell to a two-year low (~A$9.5M), and only about half had more than A$2M [verified: BDO explorer cash update via SmallCaps]. Botkeeper died of exactly this: **client concentration plus consolidation**.

### 8. Services scale linearly, and the market prices them that way
Even at AI-assisted 35–45% EBITDA margins, an accounting or outsourcing business sells for about **6–10x EBITDA** (1–2x revenue) [estimate, consistent with round-1 findings on Kelly Partners/Count multiples]. Getting to A$20M+ of founder equity needs ~A$3–4M EBITDA. That's about A$8–12M revenue: several hundred SME clients, or 60–120 mid-sized clients. With a ~3-person team per A$1M of revenue even after AI [estimate], that's a 30–40 person firm. It can be done. But it's a business you operate, not a platform, and the 2026 AI-roll-up funds are bidding up exactly this asset class.

### Skeptic's verdict on generic Track A
A horizontal, outcome-priced AI finance agency for SMEs or startups has **no unfair input**. The founder's CFO and AI skills are real but common among 2026 entrants. Distribution is the hard part, and he has no channel. And the platform owners (Xero, MYOB, Intuit) are commoditising the automatable layer from below. **I score it at P(positive) ≈ 25%, EV ≈ A$3.3M**, roughly break-even with staying employed (see table at the end).

---

## Part 2. What would have to be true for Track A to work

1. **A buyer whose finance work is specialised enough** that Xero/MYOB agents and offshore bookkeepers can't do it, and generic AI firms won't learn it, e.g. ASX continuous disclosure, Appendix 5B, covenant and lender reporting, LGC/ACCU and CIS/LTESA reporting, project-finance waterfalls.
2. **A buyer who pays for certainty, not hours:** a missed deadline costs them far more than the fee (an ASX suspension, a lender default notice, a lost tender). Then an SLA-backed fee is worth a premium and outcomes are binary and clearly defined (lodged on time, covenant cert accepted, audit with no adjustments).
3. **Contract length beyond funding cycles:** assets with 15–30 year lives (project SPVs) beat companies with 6-quarter runways (juniors) or seed-stage startups.
4. **A data or asset by-product** that grows in value with scale and can later be monetised outside the fee (asset performance data → underwriting; option or royalty stakes → capital gains). Otherwise it's a linear services business, valued at 6–10x EBITDA.
5. **A capped liability structure:** SLA credits capped at a share of fees, no promise of "error-free tax", a registered agent and PI in place from day one, and AI used under documented human review (to fit D62/2026).
6. **Melbourne must not be a handicap.** Junior resources services are a Perth relationship business (Automic bought Endeavour Corporate in 2023; Eleven, Minerva, Mining Corporate and Nexia/Cicero are all West Perth) [verified: Automic, firm sites]. Renewables developers and infrastructure funds, by contrast, are well represented in Melbourne and Sydney [estimate].

Conditions 1–4 point **away from SMEs and toward the resources and energy intersection** the brief explicitly allows. They favour project SPVs over juniors.

---

## Part 3. The four best versions

### Idea 1 — "SPV Office": an outcome-priced finance and compliance function for renewable and storage project companies (TOP PICK)

| Field | |
|---|---|
| One-liner | Runs the full finance function for operating and construction-stage solar, wind and BESS SPVs and their holdcos: monthly close, AP/payments, GST/BAS, LGC accounting, lender covenant certificates (DSCR, reserve accounts), CIS/LTESA/offtake reporting, distributions waterfall, audit file. **Who pays:** independent power producers, mid-tier developers, infrastructure and transition funds, community and C&I portfolio owners. **Priced:** per SPV per month (A$4–12k [estimate]) with SLA credits/bonus on hard outcomes: close by business day 5, covenant cert accepted by lender by deadline, audit with no material adjustments, zero late-payment interest. |
| Why now | CIS tenders and state schemes (LTESAs, Victoria's SEC, REZs) are creating hundreds of new SPVs in 2025–28, each needing lender-grade reporting from financial close. Payday Super (1 Jul 2026) and more frequent obligations add load [verified: ATO/Hall & Wilcox on Payday Super]. AI now does document extraction (invoices, O&M reports, AEMO settlement data) and reconciliation reliably enough to run a multi-entity close with few staff. |
| Why Melbourne | Victoria leads on offshore wind, the SEC and storage. Many funds and developers have Melbourne/Sydney finance teams [estimate]. No Perth handicap. Handicap: incumbents with brand (Big 4, Apex Group, which already runs fund administration for Octopus Australia and Federation's renewables trust [verified: Apex releases]; TMF; asset managers' in-house teams). |
| Unfair inputs | CFO who has run complex closes; statistician (settlement data, variance analysis, forecasting curtailment and MLF); ex-BCG; AI builder. **Gaps:** project-finance and energy-market depth (co-founder: ex-IPP or financier asset-management finance lead); a registered tax agent/CA as head of compliance. |
| Market & model | ~300–600 operating or construction-stage utility-scale and large C&I SPVs in the NEM/WEM by 2028 [estimate]; plus fund holdcos. At A$80–150k per SPV per year, the addressable market is ~A$40–80M a year [estimate]. Target 60–80 SPVs by year 6 → A$7–10M revenue, 35–40% EBITDA. Comparables: Apex/TMF/Vistra (fund and SPV admin); Big 4 managed services. No AI-native specialist found. |
| Capital & structure | Bootstrap plus ~A$1–1.5M angel/family-office round; ~70% founder ownership after co-founder and ESOP. No balance sheet needed. Later option: a data/underwriting arm (Track B). |
| Floor & failure mode | Contracts are multi-year and SPVs don't churn with funding cycles (they churn on asset sale, and a buyer often keeps the provider). The floor is a profitable 10–15 person firm worth A$3–8M. Failure mode: can't win the first five SPVs against the incumbents → stop within 12 months, having spent ~A$0.3–0.5M. P(total loss) ~20%. |
| Outcomes (10 yrs, founder value incl. salary) | Loss 20% (A$0.8M); modest 40% (A$2.5M: small profitable firm); good 30% (A$6M: 40 SPVs, sale to Apex/a Big 4/an asset manager at ~8x); great 10% (A$15M+: 100+ SPVs plus a data product feeding performance-guarantee underwriting). **EV ≈ A$4.5M; median ≈ A$2.5–3M; P(positive) ≈ 40%.** |
| Cash generation | Cash-positive from client 4–6 (~month 9–15). Can fund growth from its own cash. |
| AI leverage | Every SPV has the same template: a standard chart of accounts, recurring documents (O&M invoices, AEMO settlements, LGC registry), the same covenant formulas. That's ideal for agents, and each new SPV costs less to serve. Better models increase the margin. **The data by-product** (generation vs. P50, availability, curtailment, opex per MW across many assets) is what gives it value beyond a services firm. |
| Job satisfaction | High for this founder: CFO craft, statistics on real asset data, building the agent stack. Some grind on compliance. |
| Key risks | (1) Buyers stick with Big 4/Apex because of brand when lenders are involved. (2) Liability for a wrong covenant certificate. (3) Fewer SPVs if the build-out slows (grid delays). |
| 90-day test (while employed) | 20 interviews with CFOs/finance leads at IPPs, developers and funds. **Pass:** ≥3 LOIs or paid pilots at ≥A$5k per SPV per month, and ≥2 say they'd switch from their current provider at contract renewal. Build one shadow close (public data plus a friendly SPV) to day 5. **Kill:** <2 pilots, or price below A$3k per SPV per month. Can be done while employed if no conflict with the employer. |

### Idea 2 — "Junior Office": an AI-native finance, cosec and compliance office for ASX explorers

| Field | |
|---|---|
| One-liner | A fixed monthly fee covers bookkeeping, payroll, BAS, Appendix 5B and quarterly reports, half-year and full-year audit files, JMEI/R&D claims and company secretarial work. Outcomes guaranteed: 5B lodged on time, audit with no adjustments, ASX queries answered within the deadline. |
| Why now | Explorers raised more in late 2025 (fewer firms with tiny raises; 103 raised ≥A$10M in the Dec-25 quarter) [verified: BDO via search snippet]. Critical-minerals policy. AI drafting of 5B/quarterlies and announcements. |
| Why Australia / Melbourne | Australia has the world's largest pool of listed explorers. **Melbourne is a handicap:** the business is Perth-centric and relationship-led. Automic (750+ listed registry clients, bought Endeavour Corporate) and West Perth firms dominate [verified: Automic site]. |
| Unfair inputs | CFO, AI. Gaps: Perth-based company secretary/CA partner with a director network. |
| Market & model | ~700–900 explorers [estimate]. Finance plus cosec ~A$60–150k a year each → ~A$60–100M market [estimate]. Gross margin is high once templated. |
| Capital & structure | Bootstrap; possibly buy a small Perth cosec book (a channel, not a roll-up). |
| Floor & failure | Churn when juniors run out of cash; bad debts; price competition from incumbents who are themselves adding AI. P(total loss) ~25%. |
| Outcomes | Loss 25% (A$0.8M); modest 45% (A$2.5M); good 25% (A$5M); great 5% (A$10M). **EV ≈ A$3.1M; P(positive) ≈ 30%.** |
| Cash | Fast (client 3), but lumpy with the cycle. |
| AI leverage | Strong (templated disclosures), but easy for incumbents to copy. |
| Job satisfaction | Medium: high-volume compliance, small-cap politics. |
| Key risks | Funding-cycle churn; Perth incumbents; officer liability as company secretary. |
| 90-day test | 15 junior CFO/chair interviews. Pass: ≥5 at ≥A$6k a month who'd switch at year end. |

### Idea 3 — "Close Engine": a wholesale close and BAS service for Australian accounting practices

| Field | |
|---|---|
| One-liner | B2B2B: delivers the monthly close and BAS working papers to accounting firms, priced per close delivered by day N and reviewed, under the firm's registration. Avoids the SME acquisition problem. |
| Why now | 2026 firm consolidation and staff shortages; Payday Super; agentic BAS. |
| Why Australia | AU-specific BAS/GST/STP/Payday Super rules give some protection from US tools. |
| Unfair inputs | AI build skill. Gaps: practice channel; a CA partner. |
| Market & model | Thousands of practices; pricing pressure from offshore (A$8–25/hr) and from Xero/MYOB built-in agents. |
| Capital | Needs VC to win the race against Basis-type tools. Founder ~40–50%. |
| Floor & failure | **This is Botkeeper's model**, and Botkeeper failed when its clients consolidated. P(total loss) ~35%. |
| Outcomes | Loss 35% (A$0.6M); modest 35% (A$2.5M); good 22% (A$6M); great 8% (A$20M). **EV ≈ A$4.0M; P(positive) ≈ 30%.** |
| Cash | Slow if VC-funded; quick if run as a service. |
| AI leverage | Highest of the four, but so is the risk of commoditisation by Xero/MYOB. Models improving helps everyone equally. |
| Job satisfaction | Product-building fun; market grind. |
| Key risks | Platform bundling; Basis and well-funded entrants; channel concentration. |
| 90-day test | 10 practices sign up for paid pilots at ≥A$150 per close with ≥90% accepted without rework. Kill otherwise. |

### Idea 4 (bold) — "Fees for Royalties": a resources finance office paid partly in royalties and options

| Field | |
|---|---|
| One-liner | Run Idea 2's finance office, but price ~50% in cash (covering cost) and ~50% in **small net smelter royalties (0.25–1% NSR) over tenements, plus options**. Over 5–8 years you build a portfolio of 40–80 royalties and option stakes in Australian critical-minerals and gold projects. The outcome priced is the *company's* outcome: a discovery or financing. |
| Why now | Juniors are short of cash and prefer paying in paper. The royalty and stream market for Australian critical minerals is growing (Track B). This is the "prospect generator" model applied to services. |
| Why Australia | Deep explorer base; royalties are legally established in Australian mining law (registrable as caveats/agreements). Melbourne handicap as in Idea 2. |
| Unfair inputs | Pricing under uncertainty (portfolio statistics on discovery base rates); CFO structuring. Gaps: a geologist co-founder to screen tenements; the Perth channel. |
| Market & model | Cash side covers costs; equity side has a long-tailed payoff. Comparable: royalty companies buying junior royalties at A$0.5–3M each [estimate]. |
| Capital & structure | Own cash; later spin the royalty book into a royalty vehicle and raise from family offices or super funds (Track B). Founder ~70–80%. |
| Floor & failure | Cash fees cover the firm's costs; the royalty book is free optionality. Most royalties expire worthless; conflict-of-interest and disclosure risks (related-party, independence). P(total loss) ~20%. |
| Outcomes | Loss 20% (A$1.0M); modest 40% (A$2.5M); good 28% (A$5M); great 12% (A$20M: one royalty on a project that gets built). **EV ≈ A$4.6M; median ≈ A$2.5M; P(positive) ≈ 37%.** |
| Cash | Lower than Idea 2 (half the fees are non-cash). Break-even later (year 2). |
| AI leverage | AI runs the office; statistics prices the royalty book. |
| Job satisfaction | High: deals, geology, pricing. |
| Key risks | Explorers' boards won't grant royalties for services; a sector bust; the hard-to-scale Perth channel. |
| 90-day test | 15 junior chairs: will ≥4 accept fees as 0.5% NSR plus options instead of cash? If no, kill. |

---

## Part 4. Comparison with Track B

| Dimension | Generic Track A (SME finance agency) | Best Track A (SPV Office) | Typical Track B (performance contracts, royalties, warranty MGA, behind-the-meter assets) |
|---|---|---|---|
| Floor | Thin (client book, 1x revenue) | Moderate (multi-year contracts, data) | Strong (hard assets, recoverable capital) but capital at risk |
| Time to cash | 3–6 months | 9–15 months | 18–36 months; often needs fund or project finance |
| Capital needed | Low | Low | High (A$5–50M+ external) |
| Scaling | Linear with headcount | Linear, with a data by-product | Capital-led; scales with balance sheet |
| Uses founder's pricing/underwriting edge | Weakly | Moderately (now), strongly (data → underwriting) | Strongly |
| Crowding | Severe (Basis, Rillet, Pilot, Current, offshore, Xero/MYOB) | Low–moderate (Apex, Big 4, in-house) | Varies; super funds and specialists in big tickets, gaps at A$1–30M |
| P(positive), EV | ~25%, ~A$3.3M | ~40%, ~A$4.5M | Probably 30–45%, with a fatter tail [estimate; not modelled here] |

**Conclusion:** generic Track A is dominated. It has lower upside than Track B and no better floor than a well-designed Track A. The Track A version that survives the skeptic's case is **the one that makes Track B easier**. SPV Office earns cash early with little capital, puts the founder inside the finance of dozens of energy assets, and builds the performance data needed to price performance guarantees, revenue floors or asset acquisitions later (a Track B move). Fees for Royalties does the same in minerals. **Track A works as a way into Track B, not as a standalone business.**

Design rules for any Track A version:
1. Serve entities, not founders: SPVs or listed companies with statutory deadlines, not startups.
2. Price as a fixed fee plus SLA credit and bonus. Cap liability at 1–3 months' fees. Never warrant "error-free tax".
3. Register as a tax or BAS agent with PI from day one. Document human review under D62/2026.
4. Own the data rights (anonymised and aggregated) in the contract. That's where value beyond 8x EBITDA comes from.
5. Start while employed with a shadow close and paid pilots, and quit only at ≥5 contracted SPVs (~A$0.5M ARR).

---

## Top pick and ranking

**Top pick: SPV Office.** An outcome-priced (SLA-backed), AI-native finance and compliance function for Australian renewable and storage project companies. It's designed to become a performance-data and underwriting business in Track B.

1. **SPV Office** — EV ≈ A$4.5M; P(positive) ≈ 40%.
2. **Fees for Royalties** (bold) — EV ≈ A$4.6M; P(positive) ≈ 37%. It has a higher tail but a Perth-channel problem.
3. **Close Engine** (wholesale for accounting practices) — EV ≈ A$4.0M; P(positive) ≈ 30%. This is Botkeeper's model, and the platforms are bundling.
4. **Junior Office** — EV ≈ A$3.1M; P(positive) ≈ 30%.
(Reference: generic SME/startup Track A — EV ≈ A$3.3M; P(positive) ≈ 25%. Not recommended.)

All outcome figures are **[estimate]**: founder value over 10 years including salary taken, before tax, compared with staying employed (~A$3.0–3.5M).

### Sources (searched 4 Nov 2026)
- Bench: techcrunch.com/2024/12/30/bench-to-be-acquired-after-abruptly-shutting-down; geekwire.com; betakit.com
- Botkeeper: accountingtoday.com/news/botkeeper-shuts-down; cpapracticeadvisor.com/2026/02/09/botkeeper-is-closing-its-doors; cfobrew.com/stories/2026/02/17/botkeeper-what-went-wrong
- Basis: builtin.com/articles/basis-raises-100m-series-b-20260226. Rillet: cpapracticeadvisor.com (Jun 2025), builtin.com (Aug 2025), itbrief.news (Aug 2026)
- Crete/Current: finance.yahoo.com (Reuters, Jun 2025); accountingtoday.com (rebrand)
- Xero JAX: xero.com/media-releases/xero-announces-new-ai-innovations-xerocon-london; accountingtoday.com/news/xeros-jax-ai-gains-agentic-capacities
- MYOB: accountantsdaily.com.au/technology/22204-myob-unveils-new-ai-capabilities; itbrief.com.au/story/myob-launches-ai-tools-for-bas-insights-invoicing
- TPB: tpb.gov.au (PI and registration); dig.watch (draft D62/2026); tpb.gov.au/questions-coalface-march-2025
- Offshore costs: scalesuite.com.au; helpware.com; hiretalent.ph
- Payday Super: hallandwilcox.com.au; ato.gov.au small-business newsroom
- Explorers: smallcaps.com.au (BDO cash data); automicgroup.com.au; Perth firm sites
- Apex renewables mandates: apexgroup.com/insights
- Pricing: withorb.com/blog/2026-state-of-ai-agent-pricing-models-trends-and-whats-working
