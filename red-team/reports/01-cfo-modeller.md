# Unit-Economics Modeller (ex-PE CFO): red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
**Survives-if, and only at roughly 2–3x the scale the brief assumes.** The brief's "750–850 properties replaces $500k" is EBITDA with the founder unpaid. It ignores the cost of replacing churned managements, fixed overhead, GST and debt amortisation. On a bottom-up base case (3x PM productivity, $3k replacement CAC, 12% churn, $575k fixed), the founder can draw $500k only at **~2,500 properties, debt-free**. Rolls bought on 7-year debt send nearly all their cash to the bank for the life of the loan. **Biggest issue: churn × replacement CAC is the hidden recurring cost** (~$360k/yr at 1,000 properties). The plan has no sales desk to feed new managements for free, the way incumbents' sales desks do. PM productivity, the brief's load-bearing assumption #1, ranks only about 5th in sensitivity.

## Attacks on the load-bearing assumptions (only those in your domain; evidence, severity High/Med/Low)

Model: `red-team/models/unit_economics.py` (stdlib Python; all figures AUD ex-GST). Founder salary capacity (FSC) is the most the company can pay the founder as a deductible salary while still doing three things:
- expensing funnel CAC;
- paying interest;
- funding loan principal and roll capex out of after-tax profit, at 25% company tax.

FSC is the number to compare with the $500k target.

**A1. "3x PM productivity" buys cost parity, not advantage. Severity: High.** Splitting the role moves work out of the PM line. It does not delete that work.

| Per property/yr | Incumbent | Founder 2x | Founder 3x | Founder 4x |
|---|---|---|---|---|
| Relationship PM | 704 ($75k×1.22/130; does own inspections) | 508 | 338 | 254 |
| Ops/trust/admin | 250 (leasing/admin support) | 119 | 119 | 119 |
| Field (inspections, condition reports, tours) | in PM line | 350 | 350 | 350 |
| Software/AI | 60 | 150 | 150 | 150 |
| Guarantees, payments | – | 60 | 60 | 60 |
| **Direct cost** | **~1,014** | **1,186** | **1,017** | **933** |

At 3x the founder merely matches the incumbent's direct cost. Only at 4x is he ~$80/property cheaper, and that gap disappears if field cost is $430 instead of $350. Incumbent figures are [estimate: brief's $75k/130 plus my support and software allowances].

**Gate 2 fails on base inputs.** The founder's back office excluding the relationship PM costs **$679/property**, against the Crossub benchmark of ~$560. Passing needs field ≤$250 and software/AI ≤$110, or AI absorbing trust/arrears admin.

**A2. Acquisition: the funnel is not just growth spend. It is permanent maintenance capex. Severity: High.** At 12% gross churn [estimate: ~6% of landlords selling with half not retained, plus agent switches and self-management], a 1,000-property book loses 120 managements a year. Replacing them costs:
- $240k a year at the $2k gate;
- $360k a year at a realistic $3k;
- ~$630k a year if replaced with rolls.

Incumbents get these replacements roughly free from their sales desk. The brief has "no sales team" and counts the referral fee as upside. The model puts referral income at only **$75/property/yr** (6% sell × 50% capture × $2.5k), against about $360/property/yr of replacement cost.

Model output, funnel vs roll (3x, contribution $840/property before fixed costs):

```
funnel @ $2k (gate)        cost/retained 2,000 | payback 2.4 yrs | LTV:CAC 3.5
funnel @ $3k (base)        cost/retained 3,000 | payback 3.6 yrs | LTV:CAC 2.3
roll @ 2.8x                cost/retained 4,479 | payback 5.3 yrs | LTV:CAC 1.6
roll @ 3.3x (base)         cost/retained 5,279 | payback 6.3 yrs | LTV:CAC 1.3
roll @ 3.7x (brief FY22)   cost/retained 5,919 | payback 7.0 yrs | LTV:CAC 1.2
Roll equity/retained prop ~1,978; yr-1 cash: contribution 840 - interest 281 - principal 364 = 195 (5-yr term: 3)
```

A roll at 3.3x with 70% debt over 7 years throws off **$195 per property before fixed costs**. On a 5-year term it throws off $3. The asset is still worth buying, because it can be resold. But it is a **balance-sheet build, not an income source**, until the loan is repaid.

**A3. Retention of acquired books. Severity: Med–High.** Retention holdbacks of 10–20% for ~3 months cover early losses only. I assume 15% of an acquired book is lost in year 1 and 7% of that is recovered through the holdback, which lifts the effective cost from $4,715 to $5,279 per retained property.

Covenant risk compounds this. Take 70% LVR at 3.3x:
- If multiples fall to 2.8x, LVR becomes **82.5%**.
- First-year principal is only ~11% of the loan, while churn plus transition loss erodes ~20% of the collateral.

So LVR drifts *up* in year 1 unless the lost managements are replaced at once. A breach is plausible without anything going badly wrong operationally.

**A4. Durability (window). Severity: Med.** The window matters less than the brief thinks. The base case does not deliver a cost gap to defend at 3x (A1). At 4x the gap is ~$80/property, or ~$80k a year at 1,000 properties: material, but not a moat.

## Things the brief gets wrong, misses or understates

1. **GST.** Victorian fees are usually quoted GST-inclusive. 5.0% incl GST is 4.55% of revenue. At $620/week and 97.5% occupancy that is **$1,429 management income per property**. Total revenue including letting, ancillary and referral is ~$1,857, not $2.0k.
2. **The multiple applies to management income only, not $2.0k.** The Victorian FY21–22 average annual management income (AAMI) was ~$1,132–1,140/property [verified (search excerpt): Elite Agent coverage of Real Estate Dynamics]. Rents have risen since, so today's figure is ~$1.4–1.6k [estimate]. Roll price is therefore **~$4.7–5.3k/property**, not $5–7k. Paying $7k implies 3.7x on ~$1.9k, which is unlikely.
3. **The 3.70x multiple looks stale or high.** Current Melbourne ranges are $2.80–3.50 [verified (search excerpt): Acumentis, undated] and $2.75–3.00 [IFA/realestatebusiness, undated]. Inner suburbs reach "$3.00+" and outer suburbs fall below $3.00. I use 3.3x as the base. Get a 2026 Real Estate Dynamics or BDH figure before negotiating.
4. **The 30–35% margin is an incumbent-at-scale figure.** On the founder's stack, margin at 1,000 properties is **14%** at 3x and **19%** at 4x. That is because fixed costs (licensed head of PM/OIEC, AI engineering, insurance, trust audit, office, the comparison site) are ~$575/property at 1,000 properties. The 30% margin arrives only at ~2,500 properties.
5. **The founder's own salary is the output, but he is also unpaid labour in the ramp.** Every ramp scenario below runs 5–10 years with the founder drawing nothing. At $500k a year, the forgone income is $2.5–5M on top of the cash invested.
6. **Debt principal comes from after-tax money.** A rent roll is (I believe) a capital/CGT asset, not deductible or depreciable [estimate: get tax advice]. So every $1 of principal needs $1.33 of pre-tax profit.
7. **Interest rate barely matters; loan term matters a lot.** The cash rate is 4.60% after a 29 Sep 2026 hike, and a further hike is widely expected **tomorrow, 3 Nov 2026** [unverified: secondary sources; time-sensitive]. Moving the rate 7%→10% swings FSC by $27k. Moving the term 5→10 years swings it by $223k.
8. **Ramp losses and working capital are absent.** Even a 60-property year 1 loses ~$300k at EBITDA, because ~55% of fixed costs come before any revenue.

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| VIC avg mgmt fee ~5.1% (FY22) | 5.14% FY21–22 (4.85% low in Jun Q). A 2026 guide claims ~5.9%. Check whether these are incl GST | [verified (search excerpt): Real Estate Dynamics via Elite Agent]; 5.9% [unverified: LocalAgentFinder blog] |
| Revenue ~$2.0k/property/yr | ~$1.86k ex GST incl letting, ancillary and referral; management-only ~$1.43k | [estimate: model at $620/wk] |
| Melbourne rent | ~$641/wk all dwellings (Cotality Q2-26); Domain asking ~$600; vacancy 1.2% (May-26) | [unverified: secondary summaries of Cotality/Domain; Jellis Craig FY27 report] |
| Multiple ~$3.70 | Current $2.80–3.50 Melbourne; <$3.00 outer suburbs | [verified (search excerpt): Acumentis; IFA] — brief likely high |
| 1,000 properties ≈ $5M+ roll | $4.7M at 3.3x × $1,429 | [estimate: model] |
| 750–850 properties × $600–700 = $500k | EBITDA $450–595k; after 12% churn replaced at $2k: **$270–391k**; at $3k: $180–289k; before fixed-cost realism, tax or debt | **Wrong** [model §1] |
| 1,100–1,200 properties if half debt-funded | 1,150 properties: roll $5.4M, debt $2.7M, P&I $530k/yr, **equity $2.7M**, FSC **−$296k** in debt years | **Wrong** [model §1] |
| Incumbent wage $580/property | $75k base is $580; loaded (super 12%, leave, workcover) ~$700 | [estimate] |
| Founder $110k PM needs 300+ properties | $132k loaded. At 300 properties = $440/property PM cost, but field + software add $500 | [model] |
| Field $300–450 | Plausible; base $350. Note it is *additive* to the PM line | [estimate] |
| Debt at ~70% LVR | Rate ~8–9.5% (business/low-doc secured lending 2026 ~7.2–10%); term is the key unknown | [unverified: lender/broker pages, Everstone/ING] |
| Retention 10–20% for ~3 months | Covers early losses only; covenant drift (A3) | [estimate] |

## Model outputs (pasted)

Productivity at 1,000 properties (steady state; replacement via $3k funnel):
```
scen p/PM rev/p cost/p   EBITDA margin  FSC unlev  FSC 50%roll peak-debt  FSC debt-free
 1x  130  1857  2269  -411,680  -22%   -771,680        -1,154,809          -771,680
 2x  260  1857  1761    96,012    5%   -263,988          -647,116          -263,988
 3x  390  1857  1592   265,243   14%    -94,757          -477,885           -94,757
 4x  520  1857  1508   349,858   19%    -10,142          -393,270           -10,142
```
Break-even scale (properties):
```
scen fixed    FSC=0  FSC=$500k unlev  $500k 50%-roll (peak debt)
 2x  575k     2,180      4,400             >20k
 2x  400k     1,360      3,350             >20k
 3x  575k     1,250      2,510             >20k
 3x  400k       740      2,000             >20k
 4x  575k     1,030      2,070           10,360
 4x  400k       580      1,670            6,910
Gate case (CAC $2k, churn 10%), 3x:          FSC=0 at 830;  $500k at 1,790
Gate case + 4x + lean fixed $400k:           FSC=0 at 410;  $500k at 1,270
```
Ramps (3x; founder unpaid; cash after tax, principal and roll equity):
```
A funnel-only to ~1,900:  peak founder cash in $6.2M; first cash-positive yr 8 (+$202k/yr, still < $500k)
B roll-led to ~1,070:     peak $7.8M; not cash-positive by yr 10 (debt + replacement CAC)
C brief mix to ~1,180:    peak $6.9M; not cash-positive by yr 10; EBITDA steady state $398k
D brief mix to ~2,300:    peak $9.7M; EBITDA $1.24M, yet cash -$630k/yr while debt amortises
```
Tornado. At 1,000 properties, 50% roll-bought, peak debt year, the order is:
1. funnel CAC ($420k swing)
2. fixed costs ($350k)
3. churn ($300k)
4. properties per PM ($254k)
5. rent ($251k)
6. fee ($230k)
7. loan term ($223k)
8. software/AI ($220k)
9. field ($200k)

Rate is last ($27k).

At 2,500 properties debt-free, the order is:
1. funnel CAC ($1.05M)
2. rent ($814k)
3. fee ($786k)
4. churn ($750k)
5. properties per PM ($635k)
6. software/AI ($550k)
7. field ($500k)

**Most sensitive input: replacement CAC × churn, followed by price (fee and rent).**

Worst plausible (2x, fee 4.6% incl GST, churn 18%, CAC $4.5k, field $420, software/AI $220, fixed $650k, 10% rate, 5-year term):
- contribution is $296/property;
- EBITDA is negative even at 2,500 properties;
- there is no scale at which $500k is reachable.

Best plausible (4x, fee 5.2%, churn 9%, CAC $1.8k, fixed $450k):
- 35% margin at 1,000 properties;
- $500k at **960 properties** debt-free.

The brief's 750–850 is therefore a best-case-only number.

Cash-on-cash, buying a 1,000-property book outright (equity $1.7M including working capital, founder unpaid): year-1 cash-on-cash is **−44%** at 3x and **−40%** at 4x.

## Improvements (concrete changes to the plan, ranked by impact)

1. **Make retention and capture the core product, not upside.** Replacing churn is the largest recurring cost, so:
   - Run tenant-to-owner and buyer-investor capture as a measured funnel.
   - Every referred sale should carry a reciprocal agreement: the selling agent passes investor buyers' managements back to you.
   - Each point of churn is worth ~$30k a year per 1,000 properties at $3k CAC.
   - Target ≤9% gross churn.
2. **Price at or above market, not under.** Fee and rent outrank productivity at scale. A move from 5.0% to 5.5% incl GST is worth ~$140/property/yr, which equals going from 3x to ~4.5x on the PM line. Sell the guarantees *for* a premium. Treat the "slightly under market" positioning as a kill-test hypothesis, not a default.
3. **Restructure roll deals to remove debt drag:**
   - Pay on *retained management income after 12 months*, through an earn-out or vendor finance, rather than up-front at 3.3x.
   - Target neglected sub-scale rolls at ≤2.8x.
   - Negotiate a 10-year amortisation with a covenant tested on management income or interest cover, not on roll valuation.
   - Expect rolls to deliver income only after year 7–10. Build the plan to $500k on organic book plus debt-free rolls.
4. **Cut fixed cost below $400k.** The founder should get licensed and act as officer in effective control or licensee, and personally build the harness for the first 300 properties. Run the comparison site as a marketing line with its own CAC, not as overhead.
5. **Attack field and software, not just the PM ratio.** Gate 2 needs back office (excluding the relationship PM) ≤$560: field ≤$250 through routing density, plus software/AI ≤$110. Use Crossub as the back office until in-house cost beats ~$560.
6. **Reset the target to "$500k at ~1,800–2,000 properties"** (gate inputs) with a 6–8 year horizon, and plan equity of **$2–4M** (best/gate case) to **$6M+** (base).

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| Test | Metric | Pass / kill | When |
|---|---|---|---|
| Funnel CAC, fully loaded (site running cost, mystery shopping, ads) | $ per signed management | Pass ≤$2k; **kill funnel-led growth if >$3.5k after 50 signs** | Month 6–9 |
| Price elasticity pre-sell | Sign rate at 5.5% vs 4.9% incl GST, same guarantees | If premium sign rate ≥70% of discount sign rate, price at premium | Month 3–6 |
| Gross churn, organic + first acquired parcel | Annualised lost managements | Pass ≤10%; **kill/re-plan if >14% at month 12** | Month 12 |
| Acquired-book retention | % of managements kept 12 months post-close | Pass ≥88%; kill roll-led strategy if <80% | 12 months post-close |
| PM load | PM hours per property per month (390 properties ≈ 0.36h) | ≤0.40h at 250+ properties; **kill AI-led thesis if >0.6h at month 18** | Month 18 |
| Direct cost (PM + ops + field + software) | $/property/yr | ≤$850 (beats incumbent by ~$160) | 300 properties |
| Lender term sheets (2 banks plus 1 non-bank) | Term, covenant basis, rate | Need ≥7–10 years and no valuation-only LVR test; else fund rolls by earn-out only | Before first purchase |
| Referral capture | % of sellers using founder's selection | ≥40% (gate 3 is 50%), but treat as retention tool | First 10 sales |

## Answers to open items in my domain
- **Unit-economics model with 2x/3x/4x, funnel vs roll, payback:** see above and the script.
  - At 1,000 properties, FSC is negative in every productivity case.
  - The $500k point is ~4,400 properties at 2x, ~2,500 at 3x and ~2,070 at 4x (base fixed costs, debt-free), falling to ~1,270–1,790 under gate inputs.
  - Funnel payback is 2.4–3.6 years. Roll payback is 5.3–7.0 years on contribution.
- **Capital plan:** self-funding works only in the gate or best case, with peak need ~$2–4M plus forgone salary. The base case needs $6–10M of cumulative founder or investor cash, so it cannot be self-funded.
  - Debt fits only a book that is already retained, on a long tenor.
  - **The milestone that makes a raise credible:** 300 properties with churn ≤10%, CAC ≤$2k, direct cost ≤$850 and PM hours ≤0.4 per property per month, sustained for two quarters.
- **Kill criteria:** see the table. In short, kill if churn exceeds 14% *and* CAC exceeds $3k at month 12, because then no achievable productivity level reaches $500k below ~3,000 properties.

## Questions I'd hand to other specialists
- **Tax:** is a purchased rent roll deductible or amortisable, or purely a CGT asset? Should the founder take salary or dividends? Does Victorian payroll tax apply at this headcount (threshold and 4.85% rate [unverified])?
- **Legal/CAV:** what is the minimum cost of a compliant licensee/OIEC structure? Do referral fees need disclosure, and are there any caps under the *Estate Agents Act 1980*? Is reciprocal referral of investor buyers' managements permitted?
- **Lending/broker:** what are actual 2026 rent-roll facility terms (tenor, covenants, revaluation frequency) after the Sep-26 hike and a possible Nov-26 hike?
- **Ops:** what is a realistic dense-route cost per routine inspection and per condition report in one corridor? Can trust accounting and arrears be largely automated on PropertyMe?
- **Market/brokers:** what are current 2026 Melbourne multiples for sub-scale rolls inside sales agencies, and what is the real churn on acquired books after a brand change?
