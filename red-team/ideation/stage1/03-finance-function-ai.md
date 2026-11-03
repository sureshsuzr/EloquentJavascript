# Stage 1 — Lens 03: Finance-function and CFO-stack AI

Ideation agent: Finance-Function & CFO-Stack AI Product Lead. 3 Nov 2026.
Web searches: 18. Figures are labelled **[verified: source]**, **[estimate]** or **[unverified]**. US$ figures are shown as US$; everything else is AUD.

---

## 0. What the market looks like from this lens (Nov 2026)

**Capital is flooding into AI for the office of the CFO, almost all of it in the US, and almost all of it into software.**

| Company | What | Latest round | Source |
|---|---|---|---|
| Ramp | Spend management, moving into AI finance agents | ~US$1.85B at ~US$60B pre-money (Oct 2026); US$750M at US$44B (Jun 2026) | [verified: Bloomberg via thepaypers / SiliconAngle]; Oct round partly unconfirmed |
| Basis | Accounting agents sold to accounting firms (~30% of US top 25) | US$100M Series B at US$1.15B (Feb 2026) | [verified: Accounting Today / SiliconAngle] |
| Rillet | AI-native ERP / GL for SaaS | US$70M Series B (Aug 2025), ~US$500M valuation; reportedly ~US$1B in 2026 | [verified: Crunchbase/Reuters]; 2026 figure [unverified, single source] |
| Campfire | AI ERP + "Large Accounting Model" | US$65M Series B (Oct 2025), ~US$100M+ total | [verified: Fintech Global / BuiltIn] |
| Numeric | Close automation, now cash management | US$51M Series B (Nov 2025), ~US$89M total | [verified: CPA Practice Advisor] |
| Fieldguide | Agentic audit/advisory platform for firms | US$75M Series C at US$700M (Feb 2026), KPMG invested | [verified: CPA Practice Advisor] |
| Accrual (General Catalyst) | AI-native accounting firm roll-up; bought Puzzle's firm business | US$75M launch (Feb 2026) | [verified: Dealroom / press release] |
| Crete Professionals Alliance (Thrive) | Buy US CPA firms, run with AI | >US$500M acquisition budget over 2 yrs (Jun 2025) | [verified: Reuters via Yahoo Finance] |
| DiligentIQ / DiligenceSquared / QoEAgent | AI due diligence for PE | US$12M A (Feb 2025) / US$5M seed (Mar 2026) / undisclosed | [verified: Pulse2, Fintech Global] |

**Three conclusions follow.**

1. **Horizontal finance software is closed to a solo Melbourne founder.** FP&A copilots, close tools, AI ERPs and spend platforms are being fought over with US$50–2,000M rounds. Against Ramp and Rillet, any Australian "AI FP&A for SaaS" is a feature with a sales team. I discard it.
2. **The money is moving to "services-as-software": buying the work, not selling the tool.** Crete, Accrual and the European players (Neno, Repodo, Benford) [unverified: trade press] buy accounting practices and run them on agents. The arbitrage is buying services revenue at services multiples, raising margins with AI, and exiting as a tech-enabled platform. This is the founder's demonstrated edge, capital allocation plus pricing under uncertainty, applied to finance.
3. **Australia is under-served and supply-constrained.**
   - Accounting services is a **A$35.2B, 37,231-business** industry growing ~0.6% a year [verified: IBISWorld Apr 2026]: fragmented, low growth, with ageing owners.
   - Practices sell at **113–126 cents per dollar of fees**, with metro multiples rising [verified: DMY market data, May 2026], and larger profitable firms at **4–6x maintainable earnings** [verified: DMY Nov 2025].
   - PE has arrived at the top: Grant Thornton Australia sold to New Mountain-backed GT Advisors for **>A$800M** [verified: Consultancy.com.au, citing AFR]. Kelly Partners (ASX: KPG) and Count are listed consolidators.
   - I found **no Australian Crete/Accrual equivalent** [unverified: absence of evidence from 2 searches].
   - In regulated niches, supply is shrinking. **SMSF auditors fell from 7,073 (2014) to 3,382**, with only 37 new approvals in a year [verified: ASIC via SMSF Adviser, Nov 2025]. Median fee is flat at **A$550 for five years** (average A$651) [verified: ATO stats 2023–24].

**Regulatory tailwinds checked:**
- **Payday super (live 1 Jul 2026):** super is now paid every pay run, within 7 business days; the small business clearing house has closed [verified: ATO checklist via search]. The product opportunity is small, because payroll vendors (Xero, MYOB, Employment Hero) own the fix. The opportunity is in services: practices drowning in client remediation.
- **AASB S2:** Group 2 (two of: ≥A$200M revenue, ≥A$500M assets, ≥250 staff) began 1 Jul 2026; Group 3 follows from 1 Jul 2027; limited assurance applies from year 1 on parts of the report, rising to reasonable assurance from 2030 [verified: AUASB ASSA 2025-10, CA ANZ; sources conflict on year-1 scope]. Emissions SaaS is crowded (Watershed, Sweep, Pathzero, Sumday and many local players). It is better as a module than a company.

### Ideas generated and discarded (brief)
| Idea | Why cut |
|---|---|
| AI FP&A / board-pack copilot for SaaS | Pigment, Runway, Abacum, Rillet and Campfire are bundling it; a feature, not a company |
| Payday-super reconciliation agent | Payroll vendors fixed it by 1 Jul 2026; one-off remediation spike |
| AASB S2 reporting SaaS | Crowded with 10+ vendors; the assurance work goes to Big 4 / mid-tier |
| SaaS revenue-based-lending fund (AU) | Fundbox (MA Financial warehouse, Jan 2026), Stripe Capital, Fundsquire (A$110M lent), Outfund already compete [verified: Medianet, FF News]; cost of capital is the moat and he doesn't have one |
| AI treasury / FX for AU exporters | Airwallex, Wise and the banks; payments economics, not intelligence |
| AI R&D Tax Incentive claims factory | Real but small (~A$1–3M fees pool for a new entrant); ATO/AusIndustry scrutiny; keep as a module of idea 4 |
| AI procurement / AP agent | Ramp, Coupa and every ERP; US-led |

What survives combines four things: a **regulated or trust-gated service**, **fragmented supply sold at low multiples**, **AI that changes the cost per job by 2–5x**, and a **buyer who pays for it as equity rather than as subscription fees**. The four kept ideas follow.

---

## Idea 1 — "Ledgerline": an AI-native accounting and CFO-services roll-up (AU/NZ, then UK)

| Field | Assessment |
|---|---|
| **One-liner** | Holdco that buys A$1–8M-fee accounting practices (SME compliance, bookkeeping, SMSF, advisory) at ~1.0–1.25x fees, moves them onto one agentic production platform, and lifts EBITDA margin from ~20–25% to 35–45%. **Who pays:** SME clients pay fees; PE and family offices fund the equity; the exit buyer is PE or a strategic acquirer. |
| **Why now (2026)** | (a) Agents now do real end-to-end work: Basis completes a full partnership tax return autonomously [verified: Accounting Today]; Fieldguide runs the audit lifecycle. (b) US proof of the model: Crete has >US$500M to spend and Accrual US$75M [verified]. (c) Australia's succession wave: 37k firms, flat growth, rising multiples, retiring partners. (d) Payday super, S2 and ATO digital changes raise per-client compliance load just as junior-staff supply is tight. (e) The window is 2026–28, before GT/New Mountain, Kelly Partners or a US entrant (Crete/Accrual going international) does it. |
| **Unfair inputs** | **Strong:** practising SaaS CFO, so he is the end customer of the work and can specify "good"; statistician who can price acquisitions under retention uncertainty (directly reuses the rent-roll engine thinking: a fee book behaves like a rent roll); ex-BCG with prior exits, credible to PE and family offices for A$20–50M; heavy hands-on agent builder; Fulfilio integration experience. **Weak spots:** not a CA/CPA, so he can't be the signing partner or tax agent and needs registered tax agents and partner-level professionals; no accounting-firm network; managing professional partners is a different sport from running warehouses. |
| **Market & model** | AU accounting A$35.2B [verified: IBISWorld]. Target segment (SME-facing practices with A$1–10M fees) is ~A$8–12B [estimate]. **Model:** buy at ~1.1x fees / ~4–5x EBITDA; integrate onto the platform; target ~40% margin. Platform at year 7: A$40–60M fees, A$15–20M EBITDA [estimate]. Exit at 10–14x EBITDA for a scaled, tech-enabled platform versus 4–6x for single practices [estimate; US PE accounting platforms reportedly 12–20x, unverified]. **Comparables:** Crete, Accrual, Kelly Partners (ASX: KPG, listed partner-owned roll-up), Count Ltd, GT Australia >A$800M [verified]. |
| **Capital & structure** | PE / family-office-backed holdco. ~A$25–40M equity over 4 years plus acquisition debt (~2–2.5x EBITDA). Sellers roll 20–40% of consideration into holdco equity, earn-outs tied to 24-month client retention. Founder invests A$0.5–0.75M and gets a promote. **Founder ownership after dilution: ~12–20% [estimate]**. Platform/tech built in a separate IP company that licenses it to the holdco, which keeps a software option. |
| **Outcome distribution (10 yrs)** | Founder equity value at year 10, pre-tax, net of capital invested. **Fail 25%:** integration breaks, partners leave, lenders take control → **A$0.3M**. **Modest 35%:** A$4–6M EBITDA at 7x, gets PE CEO salary → **A$3M**. **Good 28%:** A$15M EBITDA, 11x exit → **A$12M**. **Great 12%:** A$25M+ EBITDA, global platform, 14x → **A$40M**. **EV ≈ A$9.3M** (0.08 + 1.05 + 3.36 + 4.8). **Median ≈ A$3M** (inside the "modest" band). |
| **Time to replace $500k** | PE-backed CEO salary of A$400–550k from the first close (~9–15 months after starting full-time). **Can it start while employed?** Only the 90-day test (talking to brokers and sellers, pricing books, lining up capital), and only after checking the outside-interests clause. The first acquisition needs him full-time. |
| **Job satisfaction** | Capital allocation, deal pricing, building the agent platform and recruiting partners: closest to BCG + Fulfilio + CFO combined. **Energy risk:** a large share of time is people management of professionals and client retention, which is less "building from nothing". High stretch. |
| **Key risks** | (1) **Fee deflation:** AI makes compliance cheap for everyone (Xero, MYOB, Basis-equipped rivals), so the extra margin is competed away into prices within 3–5 years; the acquired fee books shrink. *This is the killer: the R1 lesson that "AI cost-out is commoditised by vendors in 12–24 months" applies.* Mitigation: move clients up to advisory/CFO services and S2 work, and price on outcomes. (2) **Post-acquisition client and staff attrition** (the same retention variable as rent rolls; ~10–20% client loss is typical [estimate]). (3) **Capital-markets competition:** GT/New Mountain, Kelly Partners, Count or Crete push AU multiples to 1.4x+, closing the entry arbitrage. |
| **90-day test** | (a) Through DMY / NTAA brokers, get data rooms for 5 practices; build an acquisition-pricing + retention model; **≥2 sellers willing to proceed at ≤1.15x fees with ≥25% rollover**. (b) With one friendly practice, run agents on 50 real jobs (BAS, year-end, SMSF): **≥35% fewer hours with no rise in review error**. (c) **≥2 PE/family offices give indicative terms for ≥A$20M**. **Kill** if hours saved <20%, or sellers want >1.3x, or no capital interest. |

---

## Idea 2 — "QoE Engine": AI financial due diligence for lower-mid-market acquirers and lenders (with co-invest)

| Field | Assessment |
|---|---|
| **One-liner** | An engine that ingests a target's ledger, bank feeds, payroll, billing and CRM, then produces a quality-of-earnings pack in days instead of weeks. The pack covers proof of cash, revenue quality, cohort retention, working-capital peg and SaaS metrics, with every number traceable to source rows. **Who pays:** acquirers and lenders on A$2–75M deals: PE, search funds, strategic buyers, private-credit funds, M&A brokers (sell-side "vendor QoE"). The founder also co-invests in deals the engine prices well. |
| **Why now (2026)** | LLMs can now reconcile messy SMB ledgers. Lower-mid-market deal volume is rising with baby-boomer succession. Traditional QoE costs US$30–150k and takes 4–8 weeks, which prices out sub-A$20M deals [estimate]. Private credit (AU A$200B+ [unverified]) needs cheap, repeatable underwriting. Investors fund the category (DiligentIQ, DiligenceSquared), but nobody owns AU/UK LMM financial DD [unverified]. |
| **Unfair inputs** | **Strongest pure-skill fit of the four:** statistician + CFO + ex-BCG diligence; already reads SaaS ledgers daily. It generalises the round-3 rent-roll engine (same architecture: ingest a book → calibrated P10–P90 value and retention), so work carries over. Investor network = customers. **Weak:** QoE reports carry professional-liability weight, and buyers and lenders want a recognised firm's name on the report, so he needs a partner firm or PI insurance. |
| **Market & model** | AU/NZ sub-A$75M private M&A ~1,500–3,000 deals/yr [estimate]; UK ~5–8k; US LMM ~10k+ [estimate]. **Pricing:** A$8–25k per deal pack, or A$60–150k/yr subscription for active PE / private-credit funds; vendor QoE via brokers at A$5–10k. Realistic AU/NZ ceiling ~A$3–6M ARR; venture scale needs the UK/US by year 3 [estimate]. **Comparables:** DiligentIQ US$12M A; DiligenceSquared US$5M seed; Capsa AI £1.7M seed [verified]. Incumbents: mid-tier TS teams (Pitcher, BDO, RSM) using Fieldguide-type tools. |
| **Capital & structure** | Bootstrap A$50–150k to a concierge v1, then optionally a A$2–3M seed for UK/US. **Founder ownership ~65–80%** (bootstrap) or ~55% (seeded). Co-invest of A$100–300k per deal from personal capital, or a small SPV / search-fund style vehicle. |
| **Outcome distribution (10 yrs)** | **Fail 40%:** report fees too thin and the Big 4/mid-tier tools catch up → **A$0.2M**. **Modest 35%:** A$2–4M ARR niche plus a few co-invests → **A$2.5M**. **Good 18%:** A$10M ARR in AU/UK, sold to a TS firm or data vendor, plus co-invest carry → **A$10M**. **Great 7%:** US scale, platform exit → **A$30M**. **EV ≈ A$4.9M** (0.08 + 0.88 + 1.8 + 2.1). **Median ≈ A$1.5–2M**. |
| **Time to replace $500k** | 3–5 years from the software alone; sooner if co-invest returns land (lumpy). **Can start while employed: yes**, as a nights-and-weekends concierge, subject to the employment contract. This is the lowest-cost option to start. |
| **Job satisfaction** | Very high intellectual fit (modelling, data, underwriting). Lower "empire-building" energy unless paired with co-investing. Risk: it feels like a consulting practice if it never productises. |
| **Key risks** | (1) **The value sits with the buyer, not the reader** (round-3 lesson): fees stay at A$5–15k while the buyer gains A$100k+. Mitigation: co-invest and carry. (2) **Liability and acceptance:** lenders insist on a named firm. (3) **Fast followers:** Fieldguide, Basis and Big 4 internal tools cover 70% of a generic QoE within 2 years. **Kills it:** lenders refuse to rely on it, and no PE pays a subscription. |
| **90-day test** | Run 5 "shadow QoEs" on deals that have closed, where the network has the human QoE: **engine matches adjusted EBITDA within ±5% on ≥4/5, in ≤3 days**. Then **3 paid pilots at ≥A$8k** and **1 subscription LOI ≥A$60k/yr** from a PE or private-credit fund. **Kill** if <2 pilots convert. |

---

## Idea 3 (bold / non-obvious) — "Signoff": an AI-native SMSF and regulated-trust audit factory that buys up retiring auditors' capacity

| Field | Assessment |
|---|---|
| **One-liner** | Every one of Australia's ~650k SMSFs needs an annual independent audit by an ASIC-approved SMSF auditor [annual-audit requirement verified; fund count ~650k estimate, ATO]. Approved auditors are disappearing (3,382, down from 7,073; 37 new a year) [verified]. Build a firm where agents do 80–90% of the evidence-gathering and testing, and approved auditors review and sign at 3–5x today's throughput. Acquire retiring auditors' client lists. Extend to **real-estate trust-account audits**, NFP/ACNC reviews, AFSL/ACL compliance audits, and S2 limited-assurance support. **Who pays:** SMSF trustees, through referring accounting firms (B2B2C); agencies for trust audits. |
| **Why now (2026)** | Licensed capacity is shrinking while demand is flat to rising. This is the same structure as Fulfilio: a scarce, fragmented, under-used asset (here, **signing capacity** rather than warehouse space) that can be aggregated and made productive. The largest firms already average **2,164 funds per auditor** [verified: Accountants Daily FY2026 platform data], which proves a factory model is possible. The May 2026 budget raised the importance of audit automation [verified: SMS Magazine]. Prices have been flat for five years (median A$550), so a cost leader takes share without needing to raise prices. |
| **Unfair inputs** | Statistics (sampling, anomaly detection: this *is* audit), agent building, operations scaling (Fulfilio), CFO credibility with accountants. **The real-estate trust-account adjacency is a genuine network edge** (LocalAgentFinder, rounds 1–3 relationships with agency principals). **Weak spots:** he is not an approved auditor, so he must employ or partner with them and meet ASIC independence rules; incumbents (ASF Audits with its "Audy" AI assistant, Super Audits) are already tech-enabled and BGL-integrated [verified: BGL event page, promotional]. |
| **Market & model** | SMSF audit pool ≈ 650k × A$550–650 ≈ **A$360–420M/yr** [estimate from verified fee data]. Trust-account audits: ~40k+ licensed agency trust accounts across Australia at A$1.5–5k [estimate]. **Target:** 60–100k SMSF audits a year at A$450–550 (undercutting slightly) with 45–55% EBITDA margins → A$30–55M revenue, A$15–25M EBITDA by year 6–7 [estimate]. Valued like a tech-enabled compliance services business: 8–12x EBITDA [estimate]. |
| **Capital & structure** | Bootstrap-friendly: A$0.75–1.5M founder capital for platform plus the first 2–3 auditor-book acquisitions (books trade at ~0.8–1.2x fees [estimate]); vendor finance from retirees. Optional PE growth round later. **Founder ownership 60–85%** (approved auditors as partners hold equity). |
| **Outcome distribution (10 yrs)** | **Fail 30%:** ASIC independence or quality findings, or the referral channel stays loyal to incumbents → **A$0.3M**. **Modest 40%:** 15–25k audits, steady A$3–5M EBITDA cash cow → **A$3M**. **Good 22%:** 60k+ audits plus trust/NFP lines, sold to PE at 9x → **A$10M**. **Great 8%:** national leader in regulated audit plus S2 assurance pull-through → **A$25M**. **EV ≈ A$5.5M** (0.09 + 1.2 + 2.2 + 2.0). **Median ≈ A$3M**. |
| **Time to replace $500k** | ~2.5–4 years. Cash-generative early, with a seasonal peak around EOFY to October. **Can start while employed?** The test can; operations need him full-time by year 1. |
| **Job satisfaction** | High for the builder/statistician in years 1–3 (designing the factory, the anomaly models, acquisitions). It **risks becoming a compliance mill**: less stretch and less status than ideas 1–2. Medium energy long term. |
| **Key risks** | (1) **Regulatory:** ASIC tightening on high-volume auditors (48 enforcement actions in 2025 [verified]); a single systemic error can cost the licence of the signing auditor. (2) **Distribution:** referring accountants are sticky and some own their auditor relationships; BGL/Class may favour incumbents. (3) **Price collapse:** if "fully automated audits" arrive industry-wide, fees fall toward A$250–300 and the market halves. **Kills it:** ASIC signals that AI-led audit evidence is inadequate. |
| **90-day test** | Partner with one retiring approved auditor; obtain 300 de-identified prior audit files. **Pipeline completes ≥80% of the standard checklist tests with a miss rate ≤ the human's on a blind re-review**, and reviewer time per fund is **≤25 min** versus ~90–120 today [estimate]. **Referral LOIs from accounting firms covering ≥3,000 funds**, and **≥2 auditor books for sale at ≤1.0x fees**. **Kill** if ASIC/auditor-body advice says the evidence model fails ASA/ASAE standards, or LOIs cover <1,000 funds. |

---

## Idea 4 — "Finance Desk": an agentic finance team-as-a-service for AU/NZ scaleups, sold global-from-Australia

| Field | Assessment |
|---|---|
| **One-liner** | A fixed-fee "finance department in a box" for venture-backed and mid-market (A$5–150M revenue) companies. It covers monthly close in 3 days, AASB 15/ASC 606 revenue recognition, board packs and SaaS metrics, payday-super and payroll compliance, R&D tax incentive claims, audit readiness, and early AASB S2 work, plus a part-time CFO. Built on Rillet/Campfire/Numeric-type tools and his own agents. **Who pays:** CEOs and boards, at A$5–25k/month. Later it is sold to US startups at an Australian cost base. |
| **Why now (2026)** | AI ERPs (Rillet, Campfire) make a 3-person team able to run 30–50 clients' books [estimate]. Payday super and S2 add work that scaleups can't staff. Senior finance talent is scarce and expensive. US precedents (Pilot, Zeni) have shown demand [unverified current status]. |
| **Unfair inputs** | **Highest credibility to sell:** he *is* a SaaS CFO, and VC portfolios, ex-BCG alumni and AU tech founders are a direct network. **Weak:** a pure service business, so selling hours dressed as software; likely conflict with his current employer's interests while employed. |
| **Market & model** | AU/NZ scaleups and mid-market needing outsourced finance: ~5–10k companies [estimate]. Average A$8k/month → a 300-client book = **A$29M revenue** at 30–40% margin [estimate]. Comparables: outsourced CFO firms (local boutique players) [unverified]; Pilot (US) raised US$100M+ at a US$1.2B valuation in 2021 [unverified, pre-AI comparable]. |
| **Capital & structure** | Bootstrap A$0.3–0.6M; profitable at ~25 clients. **Founder ownership 80–100%**. Could become the organic "platform core" that Idea 1 bolts acquisitions onto. |
| **Outcome distribution (10 yrs)** | **Fail 30%** → **A$0.3M**. **Modest 45%:** A$5–10M revenue boutique → **A$2.5M**. **Good 20%:** A$25M revenue, sold to a mid-tier firm or PE → **A$8M**. **Great 5%:** cross-border platform → **A$20M**. **EV ≈ A$3.8M** (0.09 + 1.13 + 1.6 + 1.0). **Median ≈ A$2.5M**. |
| **Time to replace $500k** | ~2–3 years (≈40–60 clients at 35% margin). Hard to start while employed: same customer set as his employer's peers, and his time is the product. |
| **Job satisfaction** | Familiar and competent, but it is his current job multiplied across clients. **Low stretch** relative to his ambition. |
| **Key risks** | (1) Basis-equipped accounting firms and Rillet's own service partners commoditise it. (2) Bounded scale: a services business with key-person dependence. (3) Pricing pressure as "AI does the close" becomes the norm. **Kills it:** clients buy the software plus one bookkeeper instead. |
| **90-day test** | Sign 5 paying clients at ≥A$5k/month via VC portfolio intros (each needs an employment-contract check). **Kill** if CAC per client >A$10k or delivery hours per client exceed 25/month after month 2. |

---

## Comparison and ranking

| Rank | Idea | EV (A$, 10-yr founder equity) | Median | Start while employed? | Time to $500k | Satisfaction |
|---|---|---|---|---|---|---|
| **1** | **Ledgerline: AI-native accounting roll-up** | **~9.3M** | ~3M | Test only | ~1 yr (PE-funded salary) | High (deal + build), people-heavy |
| 2 | Signoff: SMSF / regulated audit factory (bold) | ~5.5M | ~3M | Test only | 2.5–4 yrs | High early, falls later |
| 3 | QoE Engine: AI financial DD + co-invest | ~4.9M | ~1.5–2M | **Yes** | 3–5 yrs | Very high fit |
| 4 | Finance Desk: finance team-as-a-service | ~3.8M | ~2.5M | Weakly | 2–3 yrs | Medium |

Bar for comparison: staying employed ≈ A$2.0–2.4M after tax over 7 years (brief), roughly A$3–3.5M over 10 years by extrapolation [estimate]. Every EV clears that bar. **Only idea 1 clears it at a median-plus outcome by a wide margin, and ideas 2 and 4 have medians at or below it.** All EVs are subjective estimates; treat the ranking, not the decimals, as the output.

## Top pick and why

**Ledgerline: an AI-native accounting and CFO-services roll-up in Australia/NZ, priced by the founder's own acquisition engine.**

1. **It applies the strongest lesson from rounds 1–3.** The edge is worth most to the *acquirer*, not the report-reader. Here he is the acquirer.
   - **A deep market:** 37k firms and A$35B of fees, not 250–900 rent-roll deals a year.
   - **A clear multiple arbitrage:** buy at ~1.1x fees / 4–6x EBITDA; sell a scaled tech-enabled platform at 10–14x.
2. **It reuses the rent-roll work almost directly.** A fee book is a rent roll: recurring clients, retention uncertainty, earn-outs. The pricing engine from round 3 becomes the internal acquisition model, which is the hybrid the brief already favours, moved to a bigger pond.
3. **The US has validated it with capital, and Australia hasn't been taken.** Crete and Accrual have US$575M+ of buying power. I found no AU equivalent.
   - **His profile is the one capital backs for this:** CFO + statistician + agent builder + exit.
4. **It solves the income constraint fastest.** A PE-funded platform CEO salary replaces A$500k within ~12 months, unlike any bootstrap path.

**Honest caveats:**
- This is a people-heavy services business, a category that did poorly in earlier rounds.
- The arbitrage window may last only 3–5 years before AI deflates compliance fees industry-wide.
- Run it with the **QoE Engine (idea 2) as the cheap, start-while-employed precursor**: the same ingest-and-price technology diligences practice acquisitions.
- Treat **Signoff (idea 3) as either a bolt-on vertical or the bootstrap fallback** if PE capital doesn't come at acceptable terms.

**Ranked list:**
1. Ledgerline: AI-native accounting/CFO-services roll-up, EV ~A$9.3M
2. Signoff: AI-native SMSF and trust-account audit factory, EV ~A$5.5M
3. QoE Engine: AI financial due diligence plus co-invest, EV ~A$4.9M
4. Finance Desk: agentic finance team-as-a-service, EV ~A$3.8M

### Key sources (from searches, 3 Nov 2026)
- Basis US$100M at US$1.15B: accountingtoday.com/articles/ai-for-accounting-startup-basis-hits-1-15b-valuation
- Rillet US$70M B: news.crunchbase.com/fintech/startup-rillet-ai-seriesb-a16z-iconiq/
- Campfire US$65M B: fintech.global/2025/10/16/campfire-secures-65m-series-b-to-transform-finance-ai/
- Numeric US$51M B: cpapracticeadvisor.com/2025/11/20/ai-accounting-platform-numeric-raises-51m-series-b/173638/
- Ramp US$44B / ~US$60B: siliconangle.com/2026/06/04/financial-technology-provider-ramp-raises-750m-funding-44b-valuation/; thepaypers.com (Oct 2026)
- Fieldguide US$75M C at US$700M: cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-…
- Crete US$500M roll-up: finance.yahoo.com/news/thrive-backed-accounting-firm-crete-130200467.html
- Accrual / Puzzle: dealroom.co/news/148460-accrual-buys-puzzles-firm-business-…
- GT Australia sale: consultancy.com.au/news/12400/grant-thornton-partners-approve-move-to-private-equity-backed-global-platform
- Practice multiples: dmy.sites.arosoftware.com/latest-market-data---may-2026
- IBISWorld AU accounting: ibisworld.com/australia/market-size/accounting-services/561
- SMSF auditors: smsfadviser.com/news/24975-smsf-auditor-numbers-continue-to-decline; ATO fee data via smsmagazine.com.au; capacity: accountantsdaily.com.au/business/23014-the-60-fold-capacity-gap-reshaping-smsf-audit
- AASB S2 Group 2 / assurance: auasb.gov.au ASSA 2025-10; charteredaccountantsanz.com
- AU RBF market: newshub.medianet.com.au (Fundbox, Jan 2026); ffnews.com (Fundsquire)
- AI DD comparables: pulse2.com/diligentiq-12-million-series-a; fintech.global (DiligenceSquared)
