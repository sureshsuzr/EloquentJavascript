# Probability-weighted wealth model: stage-2 evaluation (round 2)

Lens: the round-2 objective taken literally. That means equity value plus modest salary over 10 years, P(positive) (ending ahead of staying), P(total loss), the floor (P10), and cash generation, all on one set of assumptions. The model is `red-team/ideation2/stage2/wealth_model.py` (40,000 Monte Carlo draws, fixed seed). Its full output is in `wealth_model_output.txt` in the same folder. 9 web searches. Labels: **[verified: source]**, **[estimate]**, **[unverified]**.

**Bottom line.**
- On consistent assumptions, **no candidate gets P(positive) above ~33%**. Stage-1 reported 40–65%.
- Only **S1 (Closewise)** and **B1** have clearly positive expected value against staying (+A$0.48M and +A$0.30M). S2 turns slightly positive only with royalties and only when entered as a hybrid.
- Every quit path has a floor (P10) about A$1.3–2.2M below staying.
- The structural reason is simple. A modest outcome (a profitable A$3–5M-revenue services firm) almost never beats a A$500k job after tax and lost employer equity. So **P(positive) ≈ P(good or great) ≈ 25–30%** for every candidate, whatever its label.
- The one design lever that clearly helps is **quitting later, on traction**: keep the job ~18 months with a co-founder delivering, and quit at ~A$1M ARR. That lifts S1 to dEV +A$0.59M and halves P(total loss) to 9%.

## Assumptions

All candidates and the baseline use these assumptions. The engine is the same as round 1, so the rounds can be compared.

| Item | Assumption |
|---|---|
| Metric | Wealth created by year 10, nominal A$, after tax: after-tax pay + after-tax employer equity + after-tax founder proceeds − personal capital. Every flow compounds at **4%/yr after tax** to year 10. Living costs are not deducted (only the differences between paths count). |
| B0, stay employed | A$500k in year 1, growing 1–5%/yr. Employer equity A$0.2M / 1.0M / 3.0M (p 0.50/0.35/0.15, mean ~A$0.9M), forfeited on quitting [assumption, as round 1]. **EV A$4.77M, median 4.56, P10 4.07, P90 6.21.** This is higher than the "A$3.0–3.5M" quoted in stage-1 because it includes compounding and deducts no living costs. Use the deltas. |
| P(positive) | P(path wealth > stay wealth on the same draw). It is **not** "half the modest band", which stage-1 files 11 and 13 used. |
| P(total loss) | He quits, the venture fails, and he recovers <20% of his capital. Tests killed while he is still employed don't count; they are reported as P(kill). |
| Floor | P10 of wealth created, and dP10 against staying. |
| Base rates | Great outcome **5%** (6% for B1 and S8). Round 1 used 5–6%, and stage-1 used 7–14%. Fail is 27–42%. Context: about 48% of new Australian businesses survive four years, and 63% of all businesses do [verified: ABS 8165.0 via NT Treasury 2024–25 snapshot]. An experienced, bootstrapped founder should do better than that, which is why total failure sits at about 30%, not 50%. Between 35% and 70% of failures are caught by the 90-day/pilot test before he quits. |
| Exit values | Services firms: ~1.0x revenue when modest; 7–9x EBITDA when good. Listed Australian business services trade at ~8.3x EV/EBITDA [verified: InterFinancial Business Services dashboard, Jun 2026], and small private firms trade lower. Great outcomes are diluted by a raise. Per-candidate derivations (revenue × multiple × ownership) are in the script comments. |
| Founder ownership | 55–62% for bootstrapped services (after a co-founder at 15–20% and an ESOP); 45% in great outcomes after a raise; 45–50% for the operator-lenders; 20–30% plus a promote for capital platforms (S5, S7). |
| Salary path | **Low by default**: A$0 for 6 months after quitting, A$150k until the business is self-funding, A$250k after that, and A$350–400k from year 5 only in good or great outcomes. A failed venture means re-entry at 85% of salary after a 6-month gap, with half the equity rate. |
| Reinvestment | Variant: cap salary at A$150k and reinvest the difference after 25% company tax, compounding at the business's ROIC (0/15/30%) into exit value. |
| Capital at risk | A$0.35–0.8M per candidate, including test costs and co-investments, within the brief's A$0.75–1.2M. No personal guarantees. Equity still held at year 10 is marked down 20% for illiquidity. |
| **Tax (headline: enacted regime)** | For CGT events from **1 Jul 2027**, individuals and trusts lose the 50% discount; the cost base is CPI-indexed, with a **30% minimum tax** on gains. **Passed both houses 25 Jun 2026; royal assent 26 Jun 2026** [verified via secondary sources: Accountants Daily, KPMG TaxNewsFlash, Perpetual; I couldn't open the Act]. Gains accrued before 1 Jul 2027 keep the discount. All four Div 152 small-business concessions survive. The turnover threshold for the **50% active-asset reduction rises from A$2M to A$10M** from 1 Jul 2027; this was announced 18 Jun 2026, but its legislative status is unclear [verified as announced: Treasury explainer p2026-781365, CA ANZ]. The A$6M net-asset test is unchanged. The startup ("Innovative Business") 50% concession is still in consultation and is ignored. **Effective rates:** services exits **35%** when modest (turnover <A$10M; 50% weight on the reduction applying) and **45–46%** when good or great; capital vehicles (royalty, carry, closure) **45%**; B1 holdco 43–46%. |
| Tax (counterfactual: current regime) | 50% discount at 47%, so **23.5%** (20% for modest services exits that stack the active-asset reduction). Shown as dEVold. Almost every exit here falls after 1 Jul 2027, so this regime **does not apply**. It shows how much of the stage-1 optimism came from tax. |

**What the tax change means in practice.** For a founder with a near-zero cost base, indexation is worth nothing, so the tax rate on a sale roughly doubles from 23.5% to ~45%. The one big exception is the **50% active-asset reduction for businesses under A$10M turnover**. It favours selling a modest services firm *before* revenue passes A$10M, and it makes structuring advice worth having early. His **current employer equity** keeps the discount on gains accrued to 30 Jun 2027, so it should be valued at that date.

## Scores

Model output (A$M; dEV and dP10 are against staying):

```
ID      EV   Med   P10   P90    dEV P>stay P(TL) Pkill  dP10 gap1-5 EqMed|ok dEVold P>s old EV@p1
B0    4.77  4.56  4.07  6.21     --     --    --    --    --     --       --     --      --    --
B1    5.07  4.34  2.30  8.42  +0.30    31%   17%   25% -1.77   0.40     3.99  +0.94     37%  6.14
S1    5.25  3.82  2.44  9.59  +0.48    27%   18%   14% -1.63   1.24     3.56  +1.48     32%  6.31
S2a   4.34  3.29  2.30  7.47  -0.43    22%   15%   12% -1.77   1.28     2.74  +0.27     27%  5.16
S2b   4.67  3.82  2.41  8.01  -0.10    29%   15%   12% -1.66   1.28     3.85  +0.69     35%  6.11
S2c   4.64  3.75  2.31  8.09  -0.13    28%   15%   12% -1.76   1.28     3.70  +0.67     34%  5.51
S3    4.54  2.98  2.07  8.63  -0.23    22%   20%   13% -1.99   1.26     2.59  +0.58     25%  6.03
S4    4.49  3.32  2.14  8.00  -0.28    23%   21%   11% -1.93   1.36     3.30  +0.51     28%  5.57
S5    4.16  2.89  1.88  7.40  -0.61    20%   18%   14% -2.19   1.20     2.61  +0.07     24%  4.93
S6    4.65  3.76  2.53  7.61  -0.12    24%   20%   16% -1.54   1.13     3.16  +0.58     29%  4.92
S7    3.83  3.18  2.00  6.18  -0.94    16%    0%   21% -2.07   1.09     2.21  -0.55     20%  4.35
S8    4.48  3.14  2.26  7.74  -0.29    22%   25%   17% -1.80   1.11     2.66  +0.29     25%  5.33
S1h   5.36  4.08  2.75  9.18  +0.59    28%    9%   22% -1.32   0.87     3.20  +1.48     33%  6.26
S2bh  4.88  4.10  2.74  7.89  +0.11    30%    8%   19% -1.33   0.91     3.59  +0.84     36%  6.14
```

How to read the less obvious columns:
- **gap1-5:** pre-tax cash income given up in years 1–5.
- **EqMed|ok:** median pre-tax founder equity at exit, if the venture doesn't fail.
- **EV@p1:** this model run with the stage-1 agents' own probabilities.
- **S1h and S2bh:** hybrid entries that keep the job ~18 months and quit at ~A$1M ARR (see Sequencing).

**Break-even P(fail)** (the failure rate at which dEV = 0), with the rate used in brackets:
- B1 0.55 (0.42) · S1 0.51 (0.32) · **S1h 0.61** · S2bh 0.36 (0.27) · S6 0.29 (0.36) · S8 0.27 (0.42)
- S2b 0.21 (0.27) · S3 0.21 (0.33) · S4 0.20 (0.33) · S2c 0.19 (0.27)
- **S2a, S5 and S7: none.** They lose to staying even at zero failure, because their modest and good outcomes are too small.

| ID | Fail/mod/good/great | dEV | P(positive) | P(total loss) | Floor P10 (dP10) | Cash-positive | **Wealth-lens score /10** |
|---|---|---|---|---|---|---|---|
| B0 | — | 0 | — | 0% | 4.07 (best) | now | **6.5** |
| B1 | .42/.33/.19/.06 | +0.30 | 31% | 17% | 2.30 (−1.77) | yr 2–3, levered | **6** |
| S1 | .32/.43/.20/.05 | **+0.48** (S1h +0.59) | 27% (28%) | 18% (S1h 9%) | 2.44 (S1h 2.75) | m15–24 | **7** |
| S2a | .27/.47/.21/.05 | −0.43 | 22% | 15% | 2.30 | m15–20 | 4.5 |
| S2b | same + royalty book | −0.10 (S2bh +0.11) | 29% (30%) | 15% (8%) | 2.41 (2.74) | m18–26 | **6** |
| S2c | same + Runway Capital | −0.13 | 28% | 15% | 2.31 | m15–20; fund yr 4+ | 5.5 |
| S3 | .33/.42/.20/.05 | −0.23 | 22% | 20% | 2.07 | m12–18 | 4.5 |
| S4 | .33/.42/.20/.05 | −0.28 | 23% | 21% | 2.14 | yr 2–3 | 4.5 |
| S5 | .32/.42/.21/.05 | −0.61 | 20% | 18% | 1.88 (worst) | m12–18 (MeterProof) | 3.5 |
| S6 | .36/.40/.19/.05 | −0.12 | 24% | 20% | **2.53** | yr 1–2 (PassMark) | 5 |
| S7 | .38/.34/.23/.05 | −0.94 | 16% | **~0%** | 2.00 | asset-level, day 1 | 3 |
| S8 | .42/.30/.22/.06 | −0.29 | 22% | **25%** | 2.26 | first deal | 4 |

**Tornado for the top 3** (change in dEV, A$M, low/high input):

```
S1  base +0.48: exit values x0.75/x1.25 -0.75/+0.75; equity tax 47%/23.5% -0.19/+0.97; 1-yr slip -0.57;
                employer equity x2/x0.5 -0.48/+0.24; great x0.5/x1.5 -0.41/+0.41; good x0.7/x1.3 -0.40/+0.40;
                P(fail) +/-10pts -0.25/+0.27; venture salary x0.8/x1.2 -0.20/+0.20; low-salary reinvest -0.09/+0.10
S2b base -0.10: tax -0.14/+0.82; employer equity -0.50/+0.25; exit values -0.47/+0.47; 1-yr slip -0.46;
                good -0.27/+0.27; salary -0.22/+0.21; great -0.19/+0.19; P(fail) -0.16/+0.17
B1  base +0.30: tax -0.07/+0.64; exit values -0.50/+0.50; employer equity -0.36/+0.18; 1-yr slip -0.30;
                good -0.28/+0.28; salary -0.28/+0.28; P(fail) -0.24/+0.23; great -0.23/+0.23
P(positive): S1 27% (tax 23.5%: 31%; exits x0.75: 22%; P(fail)+10: 23%)
             S2b 29% (35/23/25)   B1 31% (37/25/26)
```

**What the tornado says.**
- The top inputs are the **exit multiple, the tax rate, the value of his employer equity and a one-year slip**. P(fail) comes well behind, because most failures are caught while he is still employed or are cheap once he is back in a job.
- **Low salary plus reinvestment is not free.** Capping pay at A$150k and reinvesting the difference:
  - S1: −A$0.12M at 0% ROIC, +A$0.03M at 15%, +A$0.26M at 30%.
  - It pays only if the business really compounds retained cash at well above ~15%, and the gain is then taxed at ~45% on exit.

## S1 dispute: report 11 (EV A$11.8M, P+ 59%) against report 14 (A$3.3M, 25%)

The two reports measure **different things on different products**, and both are partly right. The script reconciles them step by step:

| Step | Founder equity EV, pre-tax unless noted | Change |
|---|---|---|
| Report 11 as published: equity only, salary excluded; .18/.45/.28/.09 → A$0.2/3/18/60M | **11.83** | |
| (1) Base rates moved to .32/.43/.20/.05 (great 5%, as in round 1) | 7.95 | −3.88 |
| (2) Values: modest A$2.8M (1.0x revenue), good A$12M (A$12–15M revenue, ~A$3M EBITDA × 7–8, 55% owned), great A$40M (diluted to 45%). Report 11's A$18M good case assumes 2.5x revenue for a services firm; its A$60M great case assumes no dilution. | 5.60 | −2.35 |
| (3) Enacted CGT (35/45/46%) | **3.18 after tax** | −2.42 |
| (4) Full model: add low salary, subtract capital, forgone A$500k salary and employer equity | **dEV +0.48; P(positive) 27%** | |
| Report 11's own inputs run through this model | dEV +3.30; P(positive) 42% | |
| Report 14's generic-SME version (values ×0.5–0.7 for SME ACVs and Xero/MYOB bundling) | dEV −0.43; P(positive) 22% | |

**Verdict.**
- **Report 14 is right about generic Track A** (dEV slightly negative, P(positive) ~22–25%).
- **Report 11 is right that the scaleup and foreign-subsidiary segment is better** (A$100–250k ACVs, a CFO-to-CFO sale). But its EV is overstated about 3.7x before tax, for three reasons:
  - about 45% of the gap is the great-outcome probability (9% against 5%) and good-case frequency;
  - about 25% is service-firm multiples;
  - about 30% is tax.
- Report 11's **59% P(positive)** is mostly definitional. It counts half the modest band as positive, but here a modest A$3M-equity outcome loses about A$1.5M against staying.
- **Reconciled S1: dEV ≈ +A$0.5M, P(positive) ≈ 27%** (28% hybrid). It is the best shortlist candidate on EV, but it is not a high-probability path. Report 14's P(positive) was closer to right; report 11's ranking was closer to right.

## Candidate notes

**B0, stay (6.5).**
- It beats 9 of the 13 modelled entries on EV and has by far the best floor (P10 A$4.07M).
- Its value rises if his employer equity is worth more than about A$0.9M. That remains the first number to pin down, as in round 1.
- Gains on his current equity accrued before 1 Jul 2027 keep the 50% discount.

**B1, staged holdco (6).**
- It drops from round 1's +0.46 to **+0.30**, because the enacted regime is now ~45% where round 1 assumed 40%.
- Its quit-on-signed-deal design gives the highest P(positive) (31%) and the highest break-even P(fail) (0.55).
- The founder rejected roll-ups for strategic reasons, and this lens doesn't overturn that. But in wealth terms it is still the bar the Track A and B ideas must clear, and only S1 clears it.

**S1, Closewise (7).**
- Best dEV (+0.48) and best P90 (A$9.6M). The founder sells as the buyer, and the outcome definitions (close day, penalties) are hard to game.
- What stage-1 missed: his *modest* case doesn't beat staying, so P(positive) is just P(reaching ~A$12M revenue).
- It is also the most exposed to a one-year slip (−0.57) and to exit multiples (±0.75).
- Entered as a hybrid (S1h), P(total loss) falls from 18% to 9% and the floor rises A$0.3M.
- The binding constraint is employer consent: his employer's SaaS peers are the customers.

**S2a, Resources Finance Office, service only (4.5).**
- The spend pool is A$80–150M (13). So even the "good" case (100+ clients, A$10–12M revenue) yields only about A$9M of pre-tax equity, and its break-even is "none".
- Stage-1's 52–60% P(positive) depended on 37–43% good-case probabilities, which a Perth-centric, cyclical, relationship-locked niche doesn't support.
- Service-only S2 is a good *floor*, not a wealth path.

**S2b, plus royalties for fees (6).**
- The royalty book adds ~+0.33 dEV against S2a. I model 30 small NSRs, each with a 1.5% chance of producing within 10 years (median value A$2M), worth ~A$1.2M pre-tax in expectation, after a 15% drag on service growth from the lower cash fees.
- The book is a right-skewed option with almost no cash cost, and it is the cheapest upside in the shortlist.
- What stage-1 missed: 03's 14% great-case probability and A$8M median imply royalties paying out at near-producer rates. At realistic explorer-to-production odds, the book is worth about one extra modest exit, not a platform.
- Gates: board acceptance and independence (03's test of ≥3 LOIs is the right one).

**S2c, plus Runway Capital (5.5).**
- It adds about +0.30 against S2a: a 45% chance of a fund or SPV programme, GP value of ~A$3M median at year 10, carry taxed at ~45%.
- It also adds a 7% blow-up branch (adverse selection, conflict) that impairs the office's value by 30%.
- On wealth it is roughly equal to S2b, but with more licensing work and governance risk. It is an option to exercise in year 4, not a reason to start.

**S3, Contractor Cash Desk (4.5).**
- The first-loss co-investment pushes P(total loss) to 20% and gives the second-worst floor among the Track A ideas (A$2.07M).
- Stage-1 used a 13% great-case probability. At 5%, it falls below staying.
- The tier-1 approved-invoice idea is sound credit design. But it is a module for S1 or S2 (a receivables product for clients already served), not a standalone company run from Melbourne for WA/Qld clients.

**S4, SPV Office (4.5).**
- Its slow 12–24-month sales cycle is the killer in wealth terms: salary starts a year later and the cold start fails often (33%).
- Annuity contracts help the good-case multiple, but the good case is capped (~A$10M of equity).
- Better run as a second vertical of S1 or S2 once there are reference clients.

**S5, ColdCore + MeterProof (3.5).**
- It has the worst floor (A$1.88M) and break-even "none", because the asset platform dilutes him to 20–30% and adds A$0.3M of co-investment.
- VEEC price and surplus risk (spot ~A$81 in Jan 2026 [verified: CORE Markets]) plus ESC acceptance of ML baselines are policy cliffs.
- Stage-1 counted ~A$1.5M of salary as part of "positive" while ignoring the forgone A$500k.

**S6, PassMark → VoltCover (5).**
- It has the **best floor of any quit path (P10 A$2.53M)**, because PassMark runs alongside the job for ~15 months and many failures are caught there.
- Its EV is roughly break-even (−0.12), capped by MGA ownership dilution (~32% at exit) and a binary capacity gate.
- A sound "cheap option". On equity value it is not a primary bet.

**S7, Long Tail Royalties (3).**
- It has the **lowest P(total loss), effectively 0%**, because the book is recoverable at ~0.6x. But it also has the lowest EV (−0.94) and P(positive) (16%).
- The founder owns 15–25% after raising A$15–25M, so even a A$100M-NAV book gives ~A$6M pre-tax. His statistics edge accrues mostly to the LPs.
- It is better used as the **exit buyer for S2b's royalties**, or as a personal LP allocation, than as a company he runs.

**S8, Closure Co (4).**
- It has the highest P(total loss) (25%), and contamination tails can't be fully ring-fenced if regulators resist.
- The upside is real, but at a 5–6% great-case probability it is below staying.
- Worth only its stage-1 regulator meeting as a free test.

## Promotions/demotions

- **Merge S1 and S2 into one company with two verticals.** The two share the agent stack, the outcome contract, the TPB-registered agent and PI cover. Scaleups and foreign subsidiaries (acyclical, Melbourne/Sydney) offset the cyclicality of juniors (Perth). S2b's royalty option rides on the resources vertical. Diversifying the client base should cut P(fail) and lift P(good). On the tornado, −5 points of failure and +10% on good values add ~+0.25 dEV.
- **Fold S3 and S4 in as modules or verticals of that company.** Receivables finance on tier-1-approved invoices and SPV covenant reporting fit there. Neither works standalone in wealth terms.
- **Demote S5 and S7 to options.** Run MeterProof as a while-employed test only. Use S7 as the exit market and LP route for S2b's royalties.
- **Promote "hybrid entry" (S1h/S2bh) to the default.** It is the only change that moves P(total loss) a lot (18% → 9%) and the floor (+A$0.3M). It needs written employer consent and a co-founder able to deliver from month 3.
- **From the not-shortlisted ideas,** 13's **Runway Capital 5B data model** is worth building in the first 90 days anyway. It is S2's sales tool and S2c's engine, and it costs only analysis.

## Ranking and recommendation

1. **S1 Closewise, entered as a hybrid (7):** dEV +0.48 (+0.59 hybrid), P(positive) 27–28%, P(total loss) 9–18%. It has the best EV and P90 in the shortlist.
2. **S2b Resources Finance Office with royalties (6):** dEV −0.10 (+0.11 hybrid), P(positive) 29–30%. It has the best "cheap upside" and is Track B in disguise. Best as S1's second vertical.
3. **B1 staged holdco (6):** dEV +0.30, P(positive) 31%. It is the wealth bar, but the founder has rejected it.

Then S2c (5.5), S6 (5), S2a, S3 and S4 (4.5), S8 (4), S5 (3.5) and S7 (3). B0 (6.5) ranks above every option except S1.

**My one choice: S1 Closewise, built as a hybrid, with S2's resources vertical (paid partly in royalties) added once Closewise has 8–10 clients.**

**Honest caveat.** Even this choice beats staying in only ~28–30% of worlds. Its value is in the right tail (P90 ~A$9.2–9.6M against A$6.2M for staying) and in his satisfaction objective, not in a high probability of winning. Under the enacted CGT regime, his strongest levers are ones he controls:
- exit multiples, which come from margins and recurring revenue;
- not slipping a year;
- timing a modest exit under the A$10M-turnover active-asset threshold.

## Sequencing

1. **Now to Mar 2027 (while employed):**
   - Get written employer consent; S1's customers are his employer's peers.
   - Value his employer equity as at 30 Jun 2027.
   - Get tax advice on the founder holding structure and the Div 152 path.
   - Run S1's 90-day test: 5 design partners at ≥A$6k/month on an outcome SLA, review time ≤25 hours per client per month, and a PI quote.
   - In parallel, build the 5B data set and survival model. That is S2's sales tool, its royalty-pricing engine and S2c's underwriting, all in one piece of work.
2. **Apr 2027 to mid-2028 (hybrid):**
   - The co-founder (a TPB-registered tax agent/CA) delivers; he sells and builds agents in evenings and with consent.
   - **Quit trigger:** ≥A$1M ARR, gross margin ≥45%, review ratio trending to 1:10.
   - **If not met by mid-2028:** stay, and keep the stake as an option. The model counts this branch as costing ~A$150k.
3. **After quitting:**
   - Add the resources vertical (S2) with a Perth co-founder, offering a cash or royalty fee choice.
   - Add receivables finance (S3) for clients already served, and SPV reporting (S4) on referrals.
   - Consider a Runway Capital SPV (S2c) only after 8 quarters of client data, with S7-type royalty buyers as the exit route for the royalty book.
4. **Exit planning:** if growth stalls at a modest scale, sell before turnover passes A$10M to keep the 50% active-asset reduction (35% expected rate against 45%). Otherwise compound to the good case, where the multiple matters more than the tax.

Sources: Accountants Daily ("Controversial CGT changes clear both houses of parliament"); KPMG TaxNewsFlash Jun 2026; Perpetual "Capital gains tax changes explained"; Treasury explainer p2026-781365; CA ANZ media release 18 Jun 2026; InterFinancial Business Services dashboard Jun 2026; NT Treasury business count snapshot (ABS 8165.0, 2024–25); CORE Markets environmental market update Jan 2026; BDO Explorer Quarterly Cash Update Jun 2026. Everything else is stage-1 material or **[estimate]**.
