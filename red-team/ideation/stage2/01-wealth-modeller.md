# Probability-weighted wealth model: stage-2 evaluation

Lens: the brief's objective function taken literally. That means 10-year probability-adjusted wealth, the time to get back to ~A$500k of income, and the downside, all on one set of assumptions. The model is `red-team/ideation/stage2/wealth_model.py` (40,000 Monte Carlo runs, fixed seed), and its full output is in `wealth_model_output.txt` in the same folder. 11 web searches. Labels: **[verified: source]**, **[estimate]**, **[unverified]**.

**Bottom line.** On consistent assumptions, after cutting the stage-1 agents' optimism and applying the proposed 2027 CGT regime, **no "quit now" candidate clearly beats staying employed on expected value, and every one of them loses on a risk-adjusted (certainty-equivalent) basis.** Only two kinds of path add value after risk: those that **keep the salary while building an option** (C0 and C5), and a buyout entered **only once the deal is signed and the debt is termed** (C4 or C1, staged). The stage-1 EVs of A$5–9M against a ~A$3.2M bar came mostly from three things: generous great-case probabilities, the old 50% CGT discount, and great-case values that ignore preferences, hurdles and illiquidity.

## Assumptions

All candidates and the baseline use the same assumptions.

| Item | Assumption |
|---|---|
| Metric | Wealth created by year 10, nominal A$, after tax. It is the sum of after-tax pay, after-tax employer equity and after-tax founder proceeds, minus personal capital. Every flow compounds at **4%/yr after tax** to year 10. Living costs are *not* deducted from the headline (as in most stage-1 files), so differences between paths are what count. |
| Stay-employed baseline | A$500k in year 1, growing 1–5%/yr (uniform). Employer equity worth A$0.2M / 1.0M / 3.0M (p 0.50/0.35/0.15; mean ~A$0.9M), accruing evenly and forfeited on quitting. Result: **EV A$4.77M, median A$4.56M, P10–P90 A$4.06–6.20M**. This is higher than stage-1's "A$3.0–3.5M" because of compounding and no living costs. Use the deltas. |
| Income tax | 2026-27 resident rates (0/15/30/37/45%) plus 2% Medicare **[verified: superguide, etax]**. A$500k pays ~A$201k. |
| Equity tax | The May 2026 Budget proposes replacing the 50% CGT discount with indexation and a 30% minimum tax from **1 Jul 2027** **[verified as a proposal: EY, Baker McKenzie, Ashurst]**. Almost all founder gains here accrue after that date on a low cost base, so indexation barely helps and the effective rate approaches 47%. A 50% discount for early-stage founders is under consultation **[verified as a proposal: Grant Thornton, BDO, Forbes AU, Jun 2026]** and probably won't cover buyouts, funds or land. Rates used: **40%** for buyouts, holdcos and land; **42%** for carry and GP stakes; **33%** for VC startups (~50% chance the carve-out applies); **36%** for the MGA. Sensitivity: the old regime at 23.5%. |
| Dilution / ownership | Bottom up, per candidate. Buyout platforms: 20–30% (co-invest plus promote over a 1x + 8% hurdle, so the promote is ~0 in modest cases). PE-backed roll-ups: 12–20%. VC startups: 25–35% at exit, with liquidation preferences cutting modest exits. Funds: 55–65% of the GP. |
| Founder salary | Self-funded search: A$0 until close. Buyout CEO: A$300–325k. PE-backed CEO: A$400–450k. VC seed: A$250k. A$500k+ only in good or great cases (salary plus distributions). |
| Failure | A failure either costs a no-deal year (search costs lost) or impairs the business (most capital lost, back to a job by year 4–5). Re-entry is at **85%** of the stay salary after a 6-month gap, with half the equity rate. |
| Capital at risk | A$0.3–1.0M per candidate, inside the brief's A$0.75–1.2M. No personal guarantees assumed. |
| Illiquidity | Equity still held at year 10 is marked down 20%. |
| Risk aversion | CRRA with γ = 2 (also γ = 1 and 3), on existing liquid wealth of **A$3.0M** [assumption] plus path wealth, minus A$180k/yr of after-tax living costs. |

**Base rates used to re-estimate the stage-1 probabilities:**
- Search funds: ~58–60% acquire, and roughly a quarter of acquisitions lose money [verified: Stanford GSB 2026 study summary; loss share from secondary summaries]. So a first buyout has P(no deal or impaired) of about 0.35–0.45, not 0.20–0.25.
- Seed to Series A: ~13–20% now [verified: Carta, 12.9% within one year for Q3 2024 seeds]. VC-path failure rates of 55% are therefore generous to the founder.
- Small owner-run software trades at ~3.5–5x EBITDA, and the private SaaS median was 4.0x revenue in Q2 2026 [verified: Acquire.com/DealStats and SEG via search summaries]. Entry at 4.5–6x is plausible, but buyers are competing for it (Valsoft, Access, Jonas).
- AEMO's 2026 ESOO counts 225 data-centre projects (67 GW) in connection processes, and >40% of 2025 projects have dropped out or regressed [verified: AEMO ESOO overview]. The queue is real but speculative, which cuts both ways for C9.
- Private credit: freezes, write-downs and ASIC stop orders in 2026 [verified: Clayton Utz Oct 2026; Alternative Credit Investor Sep 2026]. That is a hard backdrop for a first-time credit manager (C6).
- Accounting consolidation: GT Australia was sold to the PE-backed GT Advisors (~A$0.8–1B), and BGH-backed Horizon Nexus reached 350 staff within months [verified: Consultancy.com.au, Accountants Daily]. C2's field is getting more crowded, not less.

## Scores

Model output (A$M; dEV and dCE are versus staying; CE uses γ = 2):

```
Stay employed: EV 4.77  median 4.56  P10 4.06  P90 6.20  CE g=1/2/3 4.72/4.68/4.65
ID     EV   Med   P10   P90   dEV P>stay  CE2  dCE2  CE1  CE3  Rep<=3y <=5y medYr gap1-5 EV@p1 stage1EV
C0   5.16  4.69  3.73  6.95  0.39   50%  4.85  0.17 4.99 4.74   100%  100%  0.0  0.00  5.16 3.0-3.4(7y)
C1   4.53  3.08  1.97  8.60 -0.24   25%  3.30 -1.38 3.73 3.04     0%    4%  8.2  1.09  5.57 8.0-8.5
C2   4.72  3.52  2.46  8.17 -0.05   24%  3.72 -0.96 4.07 3.51     0%   26%  8.2  0.72  6.15 4.3-9.3
C3   4.55  3.29  2.33  8.29 -0.22   24%  3.55 -1.14 3.90 3.33     0%    7% 99.0  1.02  5.36 5.4-5.5
C4   4.69  3.59  1.86  8.90 -0.08   31%  3.52 -1.16 4.00 3.18     0%   30%  8.2  1.02  5.92 7.2
C5   4.94  4.26  3.60  6.44  0.17   23%  4.50 -0.18 4.67 4.38    45%   67%  4.0  0.32  5.43 4.9-7.8
C6   3.84  2.55  2.02  7.21 -0.93   20%  2.84 -1.84 3.17 2.66    21%   36%  7.0  1.08  4.98 4.7-5.3
C7   5.41  3.02  2.57 10.67  0.64   19%  3.49 -1.20 3.97 3.27     0%   12% 99.0  1.16  7.91 4.0-6.6
C8   4.67  2.74  2.36  9.27 -0.10   20%  3.21 -1.48 3.62 3.01     0%   16% 99.0  1.29  5.81 5.7-7.6
C9   4.55  2.82  2.10  8.87 -0.22   25%  3.16 -1.52 3.61 2.92     0%   25%  6.0  1.42  5.49 4.9-6.2
C4s  5.23  4.37  2.41  8.88  0.46   32%  4.28 -0.40 4.68 3.97    50%   59%  5.0  0.39  5.23 (staged C4)
C1s  5.21  4.07  2.53  8.77  0.44   26%  4.09 -0.60 4.50 3.81    25%   60%  5.0  0.48  5.21 (staged C1)
```

How to read the less obvious columns:
- **Rep≤3y / ≤5y:** the share of runs that are back to ≥A$500k of pre-tax cash income in a full year within 3 or 5 years of quitting. Never quitting counts as replaced.
- **medYr:** the median years from quitting to that point. 99 means not reached by year 10.
- **gap1-5:** the expected pre-tax income given up in years 1–5.
- **EV@p1:** this model's values run with the stage-1 agents' own probabilities.

Under the old CGT regime (23.5%), dEV is: C0 +0.58, C1 +0.29, C2 +0.41, C3 +0.31, C4 +0.47, C5 +0.56, C6 −0.64, C7 +1.03, C8 +0.32, C9 +0.40, C4s +0.95, C1s +0.95.

**Break-even P(fail)**, the failure probability at which dEV = 0, against the value used in brackets: C0 0.66 (0.40) · C1 0.27 (0.35) · C2 0.36 (0.37) · C3 0.22 (0.30) · C4 0.33 (0.35) · C5 0.63 (0.45) · C6 0.12 (0.45) · C7 0.67 (0.55) · C8 0.53 (0.55) · C9 0.40 (0.45) · C4s 0.60 (0.42) · C1s 0.58 (0.39).

| ID | Fail/mod/good/great (re-est.) | dEV | P(beat stay) | dCE (γ=2) | Yrs to A$500k after quitting (median) | Break-even P(fail) vs used | **Wealth-lens score /10** |
|---|---|---|---|---|---|---|---|
| C0 | .40/.35/.19/.06 | +0.39 | 50% | **+0.17** | never leaves it | 0.66 vs 0.40 | **7** |
| C1 | .35/.38/.21/.06 | −0.24 | 25% | −1.38 | ~8 (staged: 5) | 0.27 vs 0.35 | 5 |
| C2 | .37/.40/.18/.05 | −0.05 | 24% | −0.96 | ~8 | 0.36 vs 0.37 | 5 |
| C3 | .30/.45/.20/.05 | −0.22 | 24% | −1.14 | not by yr 10 | 0.22 vs 0.30 | 4 |
| C4 | .35/.38/.21/.06 | −0.08 (staged +0.46) | 31% | −1.16 (staged −0.40) | ~8 (staged: 5) | 0.33 vs 0.35 (staged 0.60) | **6** |
| C5 | .45/.33/.17/.05 | +0.17 | 23% | **−0.18** | 4 (0 if it fails) | 0.63 vs 0.45 | **7** |
| C6 | .45/.34/.16/.05 | −0.93 | 20% | −1.84 | ~7 | 0.12 vs 0.45 | 3 |
| C7 | .55/.28/.13/.04 | **+0.64** | 19% | −1.20 | not by yr 10 | 0.67 vs 0.55 | 5 |
| C8 | .55/.23/.17/.05 | −0.10 | 20% | −1.48 | not by yr 10 | 0.53 vs 0.55 | 4 |
| C9 | .45/.30/.19/.06 | −0.22 | 25% | −1.52 | ~6 | 0.40 vs 0.45 | 4 |

The **tornado** for the top 3 (C4 entered as C4s), plus C2 as third on CE, shows the change in dEV in A$M for each low/high input:

```
C0  base +0.39: exit values x0.75/x1.25 -0.21/+0.21; P(fail) -10/+10pts +0.15/-0.15; equity tax 47%/23.5% -0.08/+0.19;
                great x0.5/x1.5 -0.13/+0.13; good x0.7/x1.3 -0.11/+0.11; 1-yr slip -0.04
C5  base +0.17: exit values -0.37/+0.37; tax -0.11/+0.39; employer equity x2/x0.5 -0.27/+0.14; great -0.22/+0.22;
                venture pay x0.8/x1.2 -0.22/+0.22; good -0.16/+0.16; P(fail) +0.10/-0.10; slip -0.08
C4s base +0.46: exit values -0.54/+0.54; tax -0.21/+0.49; employer equity -0.36/+0.18; slip -0.32; good -0.30/+0.30;
                venture pay -0.28/+0.28; P(fail) +0.26/-0.25; great -0.26/+0.26
C2  base -0.05: employer equity -0.53/+0.26; exit values -0.49/+0.49; tax -0.20/+0.46; slip -0.46; venture pay -0.36/+0.36;
                great -0.33/+0.33; P(fail) +0.31/-0.30
```

**What the tornado says:**
- For every quit path, the largest inputs are the **exit multiple and the tax regime**, then **what his employer equity is really worth**. All three can be checked cheaply.
- P(fail) matters less than stage-1 implied, because most failure modes are cheap if he can go back to a job.
- **A one-year slip costs C2 A$0.46M and C4s A$0.32M**, because the lost salary is real and immediate.

## Candidate notes

**C0: Rent-roll engine hybrid (7).**
- It is the only candidate with positive dCE, because he never gives up the A$500k or the employer equity. Its P10 (A$3.73M) is the cost of losing ~A$0.44M.
- It is small: dEV +A$0.39M, with a ceiling of ~A$7M in the great case.
- Stage-1 never put it on a 10-year basis. On these assumptions it is worth ~A$5.2M against A$4.8M for staying. That is a real but modest improvement, not the "A$4.5–5M vs A$3.2M" some agents implied.
- Its value is as an **option and a data asset**: it produces the outcome data and deal flow that C5 and C4s need.
- The one binding risk is employer consent.

**C1: Vertical-software holdco (5).**
- Stage-1's EV of A$8–8.5M comes mostly from a 10–12% chance of a A$35–40M-EBITDA platform. For a first-time buyer starting at A$1–4M EBITDA, I put that at 6%.
- Modest outcomes earn almost no promote: at A$6M EBITDA and 7x, LP equity doesn't clear a 1x + 8% hurdle. So the median falls to A$3.1M.
- Break-even P(fail) is 0.27, below a realistic first-buyout rate.
- **Staged entry (C1s) turns it positive (+A$0.44M).**
- The extra risk is his SaaS employer: an outside-interest conflict is likeliest here, so staging may not be allowed.

**C2: Accounting roll-up (5).**
- Its PE-paid salary (A$400–450k) gives it the best quit-path CE. That is also its weakness: the salary assumes PE will back a non-CA first-time CEO in a field now holding KPG, Findex, Count, GT Advisors (New Mountain), Horizon Nexus (BGH) and Multiplier.
- Stage-1's A$9.3M was **pre-tax equity only, excluding salary**, so it isn't comparable with the other EVs.
- At 12–20% ownership, even a good outcome yields only ~A$7M pre-tax.
- It is the most exposed to slippage and to his employer-equity value. If his current equity is worth ≥A$2M, C2 loses ~A$0.5M.

**C3: SMSF compliance factory (4).**
- It has the lowest failure rate here (0.30), but the lowest break-even (0.22). The spend pool is small (audit ~A$0.4B), and wholesale fees face AI deflation, so modest outcomes cap at ~A$3M EBITDA and never pay A$500k cash.
- It works better as a **bolt-on vertical** inside C5 or C2 than as a standalone platform.

**C4: Pricing-led distribution holdco (6; staged).**
- Leverage on a cheap, asset-backed entry gives the best modest case of the buyouts (~A$3M pre-tax proceeds plus A$400k pay).
- Run straight, it is roughly break-even (−0.08), with the worst P10 (A$1.86M), because an impaired levered platform is the costliest failure.
- **Staged, so that he quits only on a signed SPA and an asset-based lending (ABL) term sheet without a PG, it moves to +A$0.46M with the second-best quit-path CE.** The distribution business also has no conflict with a SaaS employer.
- The ABL-without-PG assumption is **[unverified]** and is the gating test.

**C5: Succession-capital platform (7).**
- Stage-1 modelled it as a quit path. Its real advantage in wealth terms is that he **quits only on traction**, so the 45% failure branch costs ~A$0.3M rather than years of income. That gives it the best floor of the founder paths (P10 A$3.6M).
- Its EV gain is modest (+0.17), because sponsor economics are back-ended carry taxed at ~42%.
- It is worth more as the **origination engine for C4s** than as a fund business on its own.

**C6: Succession Credit fund (3).**
- First-time manager fundraising is happening in a 2026 market of freezes, write-downs and ASIC stop orders. Non-property credit is what allocators want, but they want a track record.
- Failure costs ~A$0.5M of opex and 1.75 years of income. Even good outcomes are GP income taxed as income. Break-even P(fail) is 0.12.
- Keep **BookCo** (C0's lending sleeve) as a later product line, not a platform.

**C7: Valuation layer "Mark" (5).**
- It has the **highest EV gain (+0.64)** and the lowest median: 55% failure, plus liquidation preferences that cut modest exits to ~A$2M.
- For a risk-averse founder it is the worst trade-off after C6/C8/C9 (dCE −1.20), and it never replaces A$500k cash within 10 years in the median run.
- It is the only candidate whose value would rise materially if the startup CGT carve-out passes (it already gets 33% here).
- It should be validated cheaply (paid pilots) while employed, not jumped into.

**C8: Niche MGA (4).** Capacity is a binary gate. In Australia AI-specific cover is still at the exploratory stage (Tego) while Armilla, backed by Lloyd's, writes it offshore **[verified: IT Brief; Beinsure]**. The model has it below staying on both EV and CE. Run a carrier-appetite test only as a free option.

**C9: Grid-capacity arbitrage (4).** Its development profit is income-like and lumpy. It loses most from a one-year slip (zero pay in years 1–2.5) and has the largest expected income gap in years 1–5 (A$1.42M). AEMO's attrition data (>40% of projects dropping out or regressing) argues for a higher failure rate, not lower.

## Promotions/demotions

- **Merge C0 into C5.** The rent-roll engine is vertical #1 of the succession-capital engine. Both are "stay employed and build the option" paths and share the data asset.
- **Promote a sequencing variant, "C4s/C1s staged buyout,"** as a candidate in its own right. It is the only quit path with positive dEV and a break-even P(fail) above any realistic estimate (0.58–0.60).
- **Demote C6 to a product line** (BookCo) and C3 to a vertical.
- **Not shortlisted:** of these, the **home-care consolidation exec + co-invest (09)** deserves a look through this lens. A sponsor-paid exec salary from month 0–6 plus co-invest is the same shape as C2, and stage-1 gave it the highest median (A$4.0M). I didn't model it. If a sponsor offers ≥A$450k plus 3–5% equity, it would score about like C2.

## Ranking and recommendation

1. **C0 + C5 (merged): the engine plus co-invest/sponsor while employed.** It is the only family with positive certainty equivalents. It is cheap, keeps the salary, and generates the deal flow and data for step 2.
2. **C4, entered staged (C4s).** It has the best quit-path EV (+A$0.46M) and good modest-case economics, with no employer conflict. It replaces A$500k in ~5 years from quitting in the median run (~50% within 3 years).
3. **C2.** It has the best straight-quit CE thanks to the PE salary. Take it only if a sponsor commits ≥A$400k pay and ≥15% ownership up front.
4. C1 (staged): equal to C4s on EV, but carries employer-conflict and AI-churn risk.
5. C7: the right tail is attractive, but the median is poor. Validate it while employed.
6. C3, 7. C8, 8. C9, 9. C6.

**My one choice: the C0/C5 succession-capital engine, built while employed, used as the origination engine for a staged C4 distribution buyout.** He quits only on a signed SPA, an ABL term sheet without a PG, and ≥A$3M of equity committed.

**Honest caveat.** Even this choice has a negative certainty equivalent at γ = 2 (−0.40) and only a 32% chance of beating staying, so the gain is in expected value, not probability. It is break-even at γ ≈ 1. On wealth alone the decision is close. Two things tip it:
- the brief's satisfaction objective;
- the fact that staying gets **worse** if his employer equity is worth less than assumed (the tornado shows +A$0.18M for C4s if employer equity is halved).

**The first number to pin down is a realistic value for his current employer equity.**

## Sequencing

1. **Now to Dec 2026:**
   - Get written employer consent for outside interests in rent rolls, SME succession, distribution and private-credit valuation (not software).
   - Engage a tax adviser **before 30 Jun 2027**. Under the proposed regime, structure and timing are worth ~A$0.2–0.5M per candidate (the tax tornado row), and gains accrued before 1 Jul 2027 keep the 50% discount.
   - Value his employer equity properly, since it is the swing input for every quit path.
2. **2027, while employed (≤A$150k):**
   - Run the round-3 rent-roll tests and the C0 co-invest LOI.
   - Build the C5 scoring engine on rent rolls first, then distributors.
   - Run C4's free "pricing-leakage" analyses on 3 distributors' invoice data.
   - Run C7's paid-pilot test only as a free option.
3. **Jump trigger (late 2027–2028):**
   - **For C4s:** quit only with a signed SPA at ≤5x, an ABL term sheet with no PG, ≥A$3M of equity committed, and leakage of ≥150 bps proven.
   - **Fallback:** if no deal reaches signing within ~18 months, stay employed and keep C0 as the floor. The model treats this branch as costing ~A$80k, and that branch is what makes the staged path positive.
4. **How the candidates combine:**
   - C0 and C3 are verticals of the C5 engine.
   - BookCo (from C6) is a later financing product line for the same deal flow.
   - C4 (or C1) is the first platform the engine buys.
   - C7 and C8 stay as cheap tests, and are pursued only if they produce paid pilots or a carrier term sheet while he is still employed.
