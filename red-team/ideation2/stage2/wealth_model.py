#!/usr/bin/env python3
"""
Round-2 stage-2 probability-weighted wealth model (wealth-modeller lens), 4 Nov 2026.

Models B0 (stay), B1 (staged distribution holdco) and S1-S8 from
red-team/ideation2/SHORTLIST.md, plus the three S2 variants, on ONE set of
assumptions. Engine and baseline are deliberately the same as round 1
(red-team/ideation/stage2/wealth_model.py) so the rounds are comparable.

Metric: wealth CREATED by year 10, nominal A$, after tax:
    after-tax pay (job or venture) + after-tax employer equity vested
  + after-tax founder proceeds (incl. own capital back) - personal capital in,
  every flow compounded at 4%/yr after tax to year 10.
Living costs are not deducted (differences between paths are what count).

Definitions used in the tables
  EV, Med, P10 (the "floor"), P90 : of wealth created, A$M
  dEV         : EV minus stay-employed EV (same random draws)
  P>stay      : P(path wealth > stay wealth on the same draw)  = "P(positive)"
  P(TL)       : P(total loss) = he quits AND the venture fails, losing >=80%
                of his capital (killed-while-employed tests do not count)
  P(kill)     : P(the venture is killed by its test while still employed)
  gap1-5      : expected pre-tax cash income given up in years 1-5 vs staying
  CashYr      : stage-1/modeller estimate of venture cash-positive year
  EqMed|ok    : median pre-tax founder equity at exit given no failure

All scenario values are the modeller's [estimate]s; derivations are in comments.
Run: python3 wealth_model.py   (deterministic seed)
"""
import numpy as np

RNG_SEED = 20261104
N = 40_000
YEARS = 10

BASE = dict(
    salary0=500_000, salary_growth=(0.01, 0.05),
    reentry_factor=0.85, reentry_gap=0.5, reentry_equity=0.5,
    emp_equity_vals=(200_000, 1_000_000, 3_000_000),
    emp_equity_probs=(0.50, 0.35, 0.15),          # mean ~A$0.9M [assumption]
    emp_equity_tax=0.40,
    reinvest=0.04, illiquid_haircut=0.20,
)

# ---------------------------------------------------------------- tax
# ENACTED regime [verified via secondary: Treasury Laws Amendment (Tax Reform
# No. 1) Bill 2026 passed 25 Jun 2026, assent 26 Jun 2026 - Accountants Daily,
# KPMG TNF, Perpetual]: for CGT events from 1 Jul 2027 individuals/trusts lose
# the 50% discount; cost base CPI-indexed; 30% minimum tax on gains. Founder
# cost bases here are ~0, so indexation is worth ~nothing and gains are taxed
# at ~47% marginal. Division 152 small-business concessions survive; the 50%
# active-asset reduction turnover threshold is to rise from A$2M to A$10M from
# 1 Jul 2027 [announced 18 Jun 2026; legislative status unclear -> 50% weight].
# With that reduction the effective rate is ~23.5%. So for a services Pty Ltd:
#   modest exits (turnover < A$10M):  0.5*47% + 0.5*23.5% ~= 35%
#   good/great exits (turnover > A$10M): ~45% (small indexation benefit)
# Capital-type vehicles (royalty co, fund carry, closure SPVs): passive or
# large -> ~45%.  The 50% "Innovative Business" startup concession is still
# in consultation and unlikely to cover services/royalty businesses -> ignored.
# CURRENT (pre-1 Jul 2027) regime shown as a counterfactual: 50% discount ->
# 23.5%; modest exits may stack the active-asset reduction (MNAV <= A$6M) -> 20%.
TAX = {
    'SVC': dict(new=dict(modest=.35, good=.45, great=.46),
                old=dict(modest=.20, good=.235, great=.235)),
    'CAP': dict(new=dict(modest=.45, good=.45, great=.46),
                old=dict(modest=.26, good=.28, great=.28)),   # part carry as income
    'HOLD': dict(new=dict(modest=.43, good=.45, great=.46),
                 old=dict(modest=.235, good=.235, great=.235)),
}


def income_tax(x):
    """2026-27 resident rates incl. 2% Medicare [verified in round 1]."""
    x = np.asarray(x, float)
    t = np.zeros_like(x)
    for lo, hi, r in ((18_200, 45_000, 0.15), (45_000, 135_000, 0.30),
                      (135_000, 190_000, 0.37), (190_000, 1e12, 0.45)):
        t += np.clip(np.minimum(x, hi) - lo, 0, None) * r
    return t + 0.02 * x


def S(bucket, p, quit, sal=(), end=None, cap=(), rec=None, X=0.0, exit=10.0,
      sigma=0.5, kill=False):
    return dict(bucket=bucket, p=p, quit=quit, sal=list(sal), end=end,
                cap=list(cap), rec=rec, X=X, exit=exit, sigma=sigma, kill=kill)


def low_salary(q, good=False, great=False, ramp=0.5, step2=2.0, s1=150e3, s2=250e3):
    """Default LOW founder salary path: 0 for `ramp` yrs after quitting,
    A$150k until the business is self-funding, A$250k after; A$350-400k from
    yr 5 only in good/great outcomes (profits otherwise reinvested)."""
    st = [(q, 0), (q + ramp, s1), (q + step2, s2)]
    if good:
        st.append((max(5.0, q + step2 + 0.5), 350e3))
    if great:
        st.append((max(5.0, q + step2 + 0.5), 400e3))
    return st


def svc(p, q, X, test_cost=50e3, cap=400e3, early=.5, late_end=2.25, ramp=0.5,
        step2=2.0, rec=0.1, exits=(9.0, 9.5, 10.5), sig=(0.45, 0.55, 0.65)):
    """Generic founder-built venture: tests while employed, quits at q.
    p = (fail, modest, good, great); `early` = share of fails killed by the
    employed test (never quits, loses test cost only)."""
    pf, pm, pg, pG = p
    return [
        S('fail', pf * early, None, cap=[(0.4, test_cost)], kill=True),
        S('fail', pf * (1 - early), q, sal=low_salary(q, ramp=ramp, step2=step2),
          end=q + late_end, cap=[(0.4, test_cost), (q, cap)],
          rec=(q + late_end, rec * cap)),
        S('modest', pm, q, sal=low_salary(q, ramp=ramp, step2=step2),
          cap=[(0.4, test_cost), (q, cap)], X=X[0], exit=exits[0], sigma=sig[0]),
        S('good', pg, q, sal=low_salary(q, good=True, ramp=ramp, step2=step2),
          cap=[(0.4, test_cost), (q, cap)], X=X[1], exit=exits[1], sigma=sig[1]),
        S('great', pG, q, sal=low_salary(q, great=True, ramp=ramp, step2=step2),
          cap=[(0.4, test_cost), (q, cap)], X=X[2], exit=exits[2], sigma=sig[2]),
    ]


C = {}
# ------------------------------------------------------------------ B1
# Round-1 pick (C4s): quit only on a signed SPA + ABL term sheet. Scenario
# values copied from round 1 unchanged; tax now the enacted regime (HOLD).
C['B1'] = dict(name='Staged distribution holdco (round-1 C4s)', tax='HOLD',
    cash='yr 2-3 (levered)', scen=[
    S('fail', .25, None, cap=[(0.5, 80e3)], kill=True),
    S('fail', .17, 2.0, sal=[(2.0, 325e3)], end=5.0, cap=[(0.5, 80e3), (2.0, 900e3)],
      rec=(5.0, 135e3)),
    S('modest', .33, 2.0, sal=[(2.0, 325e3), (3.5, 400e3)], cap=[(0.5, 80e3), (2.0, 900e3)],
      X=3.0e6, exit=9, sigma=.4),
    S('good', .19, 2.0, sal=[(2.0, 325e3), (3.5, 500e3), (5.5, 600e3)],
      cap=[(0.5, 80e3), (2.0, 900e3)], X=9.0e6, exit=10),
    S('great', .06, 2.0, sal=[(2.0, 325e3), (3.5, 500e3), (5.5, 650e3)],
      cap=[(0.5, 80e3), (2.0, 900e3)], X=18e6, exit=10.5, sigma=.6),
])

# ------------------------------------------------------------------ S1
# Closewise. Firm value -> founder share (60% after TPB-agent co-founder 15-20%
# and ESOP; 45% in great after a A$3-5M raise):
#  modest: A$4-6M revenue, 10-15% EBITDA, sold at ~1.0x rev  -> A$5M x 0.58 = 2.8M
#  good:   A$12-15M rev, 22-25% EBITDA (~A$3M) x 7-8 = A$22M x 0.55     = 12M
#  great:  A$35-45M rev ANZ+UK platform at 2.2x rev ~A$90M x 0.45        = 40M
# Probabilities: crowded (Basis, Rillet, Pilot, JAX, Multiplier) but he is the
# buyer and ACVs are 10-20x Bench's -> .32/.43/.20/.05.
C['S1'] = dict(name='Closewise (scaleups + foreign subs)', tax='SVC',
    cash='m15-24', scen=svc((.32, .43, .20, .05), 0.75, (2.8e6, 12e6, 40e6),
                            cap=400e3, early=.45))

# ------------------------------------------------------------------ S2
# Resources Finance Office. ~750 5B filers x A$70-150k (13) = A$80-150M pool.
#  modest: 25-40 clients, A$3M rev, ~1.0x rev = A$3.5M x 0.62          = 2.2M
#  good:   ~100-120 clients, A$10-12M rev, 25% EBITDA x 7 = A$16M x .58 = 9M
#  great:  A$20M+ rev + energy SPVs, sold to registry/PE platform at
#          ~2x rev = A$40M x 0.55                                          = 22M
# Perth handicap + cyclical clients, but standard public deliverable and a
# proven strategic exit (Automic/Advent A$725M [verified by 13]).
S2a_p = (.27, .47, .21, .05)
C['S2a'] = dict(name='S2a Resources Finance Office: service only', tax='SVC',
    cash='m15-20', scen=svc(S2a_p, 0.75, (2.2e6, 9e6, 22e6), cap=450e3, early=.45))
# S2b: ~30% of fees taken as 0.25-0.5% NSRs/options from consenting clients.
# Lower cash fees slow growth -> service equity x0.85. Royalty book handled as
# an add-on in run(): ~30 royalties written over 10 yrs, P(project producing
# by yr 10) 1.5% each [estimate: explorer projects rarely reach production in
# <10 yrs, and boards grant royalties on non-core ground]; producing royalty
# value lognormal median A$2.0M (sigma 1.0); non-producing option value
# ~A$20k each; 20% illiquidity marks; taxed CAP.
# (Revised down from p=2%/median A$2.5M on reflection: expected pre-tax book
#  ~A$1.2M, i.e. ~0.6 producing royalties x ~A$3.3M mean, plus options.)
C['S2b'] = dict(name='S2b ... + royalties for fees', tax='SVC', cash='m18-26',
    scen=svc(S2a_p, 0.75, (2.2e6 * .85, 9e6 * .85, 22e6 * .85), cap=450e3, early=.45),
    roy=dict(n=30, p=0.015, med=2.0e6, sig=1.0, opt=20e3))
# S2c: + Runway Capital (refund advances, bridge notes, royalty buying) from
# yr ~4 if the office survives. P(fund/SPV programme raised | survive) 45%;
# GP stake+carry at yr 10 lognormal median A$3M (sigma .9); founder co-invest
# A$0.3M at yr 4. P(blow-up) 7% of surviving paths: co-invest lost and the
# office's equity x0.7 (adverse selection / conflict scandal).
C['S2c'] = dict(name='S2c ... + Runway Capital', tax='SVC', cash='m15-20 (fund: yr 4+)',
    scen=svc(S2a_p, 0.75, (2.2e6, 9e6, 22e6), cap=450e3, early=.45),
    fund=dict(p=.45, med=3.0e6, sig=.9, coinv=300e3, t=4.0, blow=.07, hit=.7))

# ------------------------------------------------------------------ S3
# Contractor Cash Desk: agency + approved-invoice finance (first-loss from
# family offices; founder co-invests A$0.3M in first loss at yr ~2.25).
#  modest: agency A$4M rev, ~1.0x, 55%                                  = 2.0M
#  good:   A$9M agency + A$40M book (net 4%) -> EBITDA ~A$3.5M x 7 x 45% = 11M
#  great:  vertical champion sold to bank/strategic                       = 32M
# WA/Qld distance, credit/fraud risk -> .33/.42/.20/.05
s3 = svc((.33, .42, .20, .05), 0.75, (2.0e6, 11e6, 32e6), cap=300e3, early=.40)
for sc in s3:
    if not sc['kill']:
        sc['cap'].append((2.25, 300e3))       # first-loss co-invest (lost on fail)
C['S3'] = dict(name='Contractor Cash Desk / Cashline', tax='SVC', cash='m12-18', scen=s3)

# ------------------------------------------------------------------ S4
# SPV Office: slow sales (12-24 months), cold-start problem, then 10-15-yr
# contracts. Quits at yr 1 after a paid pilot; salary ramp slower.
#  modest: A$3M contracted rev at ~1.4x = A$4.3M x 0.62                 = 2.6M
#  good:   A$8-9M rev, 35% EBITDA ~A$3M x 9 (annuity-like) x 0.55 x .6  = 10M
#          (x.6 = probability-weighted haircut for sale to an asset manager
#           at a services, not infrastructure, multiple)
#  great:  100+ SPVs + data/underwriting arm                              = 28M
C['S4'] = dict(name='SPV Office', tax='SVC', cash='yr 2-3',
    scen=svc((.33, .42, .20, .05), 1.0, (2.6e6, 10e6, 28e6), cap=500e3, early=.35,
             late_end=2.5, ramp=1.0, step2=2.5))

# ------------------------------------------------------------------ S5
# MeterProof first (asset-light, while employed), then ColdCore assets with
# CEFC-backed debt and family-office equity; founder 35-50% of opco, 20-30% at
# exit + promote. Founder adds A$0.3M to the first asset SPV at yr 2.
#  modest: MeterProof A$1-2M EBITDA services firm, 0.7 share            = 2.0M
#  good:   A$60M asset platform, opco+promote                            = 9M
#  great:  national cold-chain EaaS sold to infra/super                  = 28M
# VEEC surplus/price (~A$80 in Jan 2026 [verified: CORE Markets]) and ESC
# acceptance of ML baselines are binary-ish policy risks.
s5 = svc((.32, .42, .21, .05), 1.0, (2.0e6, 9e6, 28e6), cap=500e3, early=.45)
for sc in s5:
    if not sc['kill']:
        sc['cap'].append((2.0, 300e3))
C['S5'] = dict(name='ColdCore + MeterProof', tax='SVC', cash='m12-18 (MeterProof)', scen=s5)

# ------------------------------------------------------------------ S6
# PassMark -> VoltCover 2.0. PassMark run alongside the job 12-18 months
# (quit 1.25). MGA needs carrier capacity (binary).
#  modest: PassMark A$3-5M rev sold ~A$6M x 0.45 (seeded)               = 2.5M
#  good:   PassMark + MGA A$25M GWP, ~A$30M value x 0.32                 = 9M
#  great:  product mandated + NZ/UK                                       = 25M
C['S6'] = dict(name='PassMark -> VoltCover 2.0', tax='SVC', cash='yr 1-2 (PassMark)',
    scen=svc((.36, .40, .19, .05), 1.25, (2.5e6, 9e6, 25e6), cap=350e3, early=.45))

# ------------------------------------------------------------------ S7
# Long Tail Royalties: royalty co raising A$15-25M first close; founder 15-25%
# + 10% promote. Failure = cannot raise (mostly detected before quitting) or
# sub-scale book (book recoverable at ~0.6x -> rec 60% of capital).
#  modest: A$30M book at 1.0x -> founder ~1.5M; good A$100M NAV -> 6M;
#  great: listed at A$250M+ -> 18M (stage-1 03 figures, kept).
s7 = [
    S('fail', .38 * .55, None, cap=[(0.4, 60e3)], kill=True),
    S('fail', .38 * .45, 1.0, sal=[(1.0, 0), (1.5, 200e3)], end=3.5,
      cap=[(0.4, 60e3), (1.0, 500e3)], rec=(3.5, 300e3)),
    S('modest', .34, 1.0, sal=[(1.0, 0), (1.5, 200e3)],
      cap=[(0.4, 60e3), (1.0, 500e3)], X=1.5e6, exit=10, sigma=.4),
    S('good', .23, 1.0, sal=[(1.0, 0), (1.5, 200e3), (4.0, 300e3)],
      cap=[(0.4, 60e3), (1.0, 500e3)], X=6e6, exit=10, sigma=.5),
    S('great', .05, 1.0, sal=[(1.0, 0), (1.5, 200e3), (4.0, 350e3)],
      cap=[(0.4, 60e3), (1.0, 500e3)], X=18e6, exit=10.5, sigma=.6),
]
C['S7'] = dict(name='Long Tail Royalties', tax='CAP', cash='asset-level day 1; G&A yr 2-3',
               scen=s7)

# ------------------------------------------------------------------ S8
# Closure Co: regulator transfer + contamination tail; ring-fenced SPVs (no
# personal liability assumed). Quit 1.25 on a first signed transfer.
C['S8'] = dict(name='Closure Co', tax='CAP', cash='first deal (liability-backed)',
    scen=svc((.42, .30, .22, .06), 1.25, (1.5e6, 8e6, 28e6), cap=400e3, early=.40,
             rec=0.0))

# ---------------------------------------------------------------- hybrids
# Sequencing variants (not shortlist candidates): keep the job ~18 months
# while a co-founder runs delivery (needs written employer consent); quit only
# at >= A$1M ARR / 8-10 paying clients. More failures are caught before he
# quits (70% vs 45%), but the business grows more slowly (equity x0.9) and he
# puts in more test capital (A$150k incl. co-founder pay top-up).
def hybrid(base_p, X, cap, q=1.5):
    return svc(base_p, q, tuple(x * 0.9 for x in X), test_cost=150e3, cap=cap,
               early=.70, ramp=0.0, step2=1.0)

C['S1h'] = dict(name='S1 hybrid: quit at A$1M ARR (yr 1.5)', tax='SVC', cash='m15-24',
    scen=hybrid((.32, .43, .20, .05), (2.8e6, 12e6, 40e6), 300e3))
C['S2bh'] = dict(name='S2b hybrid: quit at A$1M ARR (yr 1.5)', tax='SVC', cash='m18-26',
    scen=hybrid(S2a_p, (2.2e6 * .85, 9e6 * .85, 22e6 * .85), 350e3),
    roy=dict(n=30, p=0.015, med=2.0e6, sig=1.0, opt=20e3))

ORDER = ['B1', 'S1', 'S2a', 'S2b', 'S2c', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S1h', 'S2bh']

STAGE1_P = dict(   # (fail, modest, good, great) from the stage-1 files
    S1=(.18, .45, .28, .09), S2a=(.12, .43, .37, .08), S2b=(.10, .33, .43, .14),
    S2c=(.12, .43, .37, .08), S3=(.22, .35, .30, .13), S4=(.175, .40, .325, .10),
    S5=(.135, .45, .33, .085), S6=(.28, .42, .24, .06), S7=(.07, .41, .40, .12),
    S8=(.25, .30, .35, .10), B1=(.20, .35, .32, .13),
    S1h=(.18, .45, .28, .09), S2bh=(.10, .33, .43, .14))
STAGE1_EV = dict(B1='+0.46 dEV (r1)', S1='11.8 (11) / 3.3 (14)', S2a='5.2-8.7',
                 S2b='8.3 (03)', S2c='8.8 (13C)', S3='6.2-8.8', S4='4.5-7.8',
                 S5='5.6-8.1', S6='6.2-7.0', S7='5.2', S8='6.3',
                 S1h='(variant)', S2bh='(variant)')


# ---------------------------------------------------------------- engine
def sal_at(steps, t):
    v = 0.0
    for start, amt in steps:
        if t >= start:
            v = amt
    return v


def overlap(a0, a1, b0, b1):
    return max(0.0, min(a1, b1) - max(a0, b0))


def simulate_path(scen, taxr, draws, A, scale_X=1.0, sal_scale=1.0, delay=0.0,
                  lowsal_cut=0.0, roic=0.0):
    g, E, z = draws['g'], draws['E'], draws['z']
    n = len(g)
    quit, end = scen['quit'], scen['end']
    q = 99.0 if quit is None else quit
    ret = None if end is None else end + delay + A['reentry_gap']
    wealth = np.zeros(n)
    income = np.zeros((n, YEARS))
    reinvested = 0.0   # foregone salary retained in the company (reinvest variant)
    for y in range(1, YEARS + 1):
        y0, y1 = y - 1.0, float(y)
        growth = (1 + g) ** (y - 1)
        emp_share = overlap(y0, y1, 0, q)
        re_share = overlap(y0, y1, ret, 99) if ret is not None else 0.0
        vend = (end + delay) if end is not None else 99.0
        ven = 0.0
        for m in range(12):
            t = y0 + (m + 0.5) / 12
            if q <= t < vend:
                st = [(s + (delay if s > q else 0), a) for s, a in scen['sal']]
                s_now = sal_at(st, t) * sal_scale
                if lowsal_cut and s_now > 150e3 and scen['X'] > 0:
                    cut = min(lowsal_cut, s_now - 150e3)
                    s_now -= cut
                    tx = min(scen['exit'] + delay, YEARS)
                    # retained after 25% company tax, compounding at ROIC to exit
                    reinvested += cut / 12 * 0.75 * (1 + roic) ** max(0, tx - t)
                ven += s_now / 12
        emp = A['salary0'] * growth * (emp_share + re_share * A['reentry_factor'])
        pre = emp + ven
        income[:, y - 1] = pre
        after = pre - income_tax(pre)
        eq = E / YEARS * (emp_share + re_share * A['reentry_equity'])
        after = after + eq * (1 - A['emp_equity_tax'])
        wealth += after * (1 + A['reinvest']) ** (YEARS - (y - 0.5))
    capital_total = 0.0
    for t, amt in scen['cap']:
        t2 = t + (delay if (quit is not None and t > q) else 0)
        if end is not None and t2 > end + delay:
            continue
        capital_total += amt
        wealth -= amt * (1 + A['reinvest']) ** (YEARS - t2)
    if scen['rec'] is not None:
        t, amt = scen['rec']
        wealth += amt * (1 + A['reinvest']) ** (YEARS - min(t + delay, YEARS))
    Xv = np.zeros(n)
    if scen['X'] > 0:
        s = scen['sigma']
        X = (scen['X'] * scale_X + reinvested) * np.exp(s * z - s * s / 2)
        tx = scen['exit'] + delay
        if tx > YEARS:
            X = X * (1 - A['illiquid_haircut'])
            tx = YEARS
        Xv = X
        net = X - taxr * np.maximum(0, X - capital_total)
        wealth += net * (1 + A['reinvest']) ** (YEARS - tx)
    return wealth, income, Xv, capital_total


def make_draws(n, seed):
    rng = np.random.default_rng(seed)
    A = BASE
    return dict(g=rng.uniform(*A['salary_growth'], n),
                E=rng.choice(A['emp_equity_vals'], size=n, p=A['emp_equity_probs']),
                z=rng.standard_normal(n), u=rng.uniform(size=n),
                u2=rng.uniform(size=n), u3=rng.uniform(size=n),
                z2=rng.standard_normal(n), rk=rng.uniform(size=(n, 40)),
                zr=rng.standard_normal((n, 40)))


def stay(draws, A=BASE):
    w, inc, _, _ = simulate_path(S('stay', 1, None), 0.0, draws, A)
    return w, inc


def run(key, draws, A=BASE, pfail_shift=0.0, scale=None, sal_scale=1.0, delay=0.0,
        regime='new', tax_override=None, probs=None, lowsal_cut=0.0, roic=0.0,
        addons=True):
    cand = C[key]
    scale = scale or {}
    ps = np.array([s['p'] for s in cand['scen']], float)
    bk = [s['bucket'] for s in cand['scen']]
    if probs:
        tot = {b: sum(p for p, bb in zip(ps, bk) if bb == b) for b in set(bk)}
        ps = np.array([p / tot[b] * probs[b] for p, b in zip(ps, bk)])
    fails = np.array([b == 'fail' for b in bk])
    if pfail_shift:
        pf = ps[fails].sum()
        npf = min(max(pf + pfail_shift, 0.01), 0.95)
        ps[fails] *= npf / pf
        ps[~fails] *= (1 - npf) / (1 - pf)
    ps = ps / ps.sum()
    idx = np.minimum(np.searchsorted(np.cumsum(ps), draws['u']), len(ps) - 1)
    n = len(draws['u'])
    W, INC = np.zeros(n), np.zeros((n, YEARS))
    TL, KILL, OK = (np.zeros(n, bool) for _ in range(3))
    EQ = np.zeros(n)
    tp = TAX[cand['tax']][regime]
    for k, sc in enumerate(cand['scen']):
        m = idx == k
        if not m.any():
            continue
        sub = {kk: v[m] for kk, v in draws.items()}
        b = sc['bucket']
        taxr = tax_override if tax_override is not None else tp.get(b, .45)
        w, inc, xv, capt = simulate_path(sc, taxr, sub, A, scale.get(b, 1.0),
                                         sal_scale, delay, lowsal_cut, roic)
        # ---- add-ons (S2b royalty book, S2c fund)
        if addons and b != 'fail' and 'roy' in cand:
            r = cand['roy']
            ctax = tax_override if tax_override is not None else TAX['CAP'][regime]['good']
            prod = sub['rk'][:, :r['n']] < r['p']
            vals = r['med'] * np.exp(r['sig'] * sub['zr'][:, :r['n']])
            book = (prod * vals).sum(1) + (~prod).sum(1) * r['opt']
            book *= (1 - A['illiquid_haircut'])
            w = w + book * (1 - ctax)
            xv = xv + book
        if addons and b != 'fail' and 'fund' in cand:
            f = cand['fund']
            ctax = tax_override if tax_override is not None else TAX['CAP'][regime]['good']
            raised = sub['u2'] < f['p']
            blow = raised & (sub['u3'] < f['blow'] / f['p'])
            gp = np.where(raised & ~blow, f['med'] * np.exp(f['sig'] * sub['z2']
                                                            - f['sig'] ** 2 / 2), 0.0)
            gp *= (1 - A['illiquid_haircut'])
            co = f['coinv'] * (1 + A['reinvest']) ** (YEARS - f['t'])
            # co-invest: paid in if raised; returned inside gp unless blow-up
            w = w - np.where(raised, co, 0) + gp * (1 - ctax) + np.where(raised & ~blow, co, 0)
            # blow-up impairs the office equity
            w = w - np.where(blow, xv * (1 - f['hit']) * (1 - taxr), 0)
            xv = xv + gp - np.where(blow, xv * (1 - f['hit']), 0)
        W[m], INC[m] = w, inc
        capin = sum(a for _, a in sc['cap'])
        recov = sc['rec'][1] if sc['rec'] else 0.0
        TL[m] = (b == 'fail') and not sc['kill'] and recov < 0.2 * capin
        KILL[m] = sc['kill']
        OK[m] = b != 'fail'
        EQ[m] = xv
    return dict(W=W, INC=INC, TL=TL, KILL=KILL, OK=OK, EQ=EQ, ps=ps)


def summarise(r, Ws, INCs):
    W = r['W']
    gap = (INCs[:, :5] - r['INC'][:, :5]).sum(1).mean()
    eqok = np.median(r['EQ'][r['OK']]) if r['OK'].any() else 0
    return dict(EV=W.mean(), Med=np.median(W), P10=np.percentile(W, 10),
                P90=np.percentile(W, 90), dEV=W.mean() - Ws.mean(),
                Ppos=(W > Ws).mean(), TL=r['TL'].mean(), KILL=r['KILL'].mean(),
                gap=gap, eqok=eqok, dP10=np.percentile(W, 10) - np.percentile(Ws, 10))


def m(x):
    return x / 1e6


def main():
    D = make_draws(N, RNG_SEED)
    Ws, INCs = stay(D)
    print('=' * 100)
    print('ROUND-2 WEALTH MODEL  (A$M, 10-yr wealth created, after tax, 4%/yr compounding)')
    print(f'B0 Stay employed: EV {m(Ws.mean()):.2f}  median {m(np.median(Ws)):.2f}  '
          f'P10 {m(np.percentile(Ws,10)):.2f}  P90 {m(np.percentile(Ws,90)):.2f}')
    print()
    hdr = (f"{'ID':5}{'EV':>6}{'Med':>6}{'P10':>6}{'P90':>7}{'dEV':>7}{'P>stay':>7}"
           f"{'P(TL)':>7}{'Pkill':>7}{'dP10':>7}{'gap1-5':>7}{'EqMed|ok':>9}"
           f"{'dEVold':>8}{'P>s old':>8}{'EV@p1':>7}  stage-1 EV / cash-positive")
    print('Enacted CGT regime (indexation + 30% min tax from 1 Jul 2027) is the headline;')
    print('dEVold / P>s old = same model under the CURRENT 50%-discount regime.')
    print(hdr)
    res = {}
    for k in ORDER:
        r = run(k, D)
        s = summarise(r, Ws, INCs)
        ro = summarise(run(k, D, regime='old'), Ws, INCs)
        p1 = dict(zip(('fail', 'modest', 'good', 'great'), STAGE1_P[k]))
        s1 = summarise(run(k, D, probs=p1), Ws, INCs)
        res[k] = s
        print(f"{k:5}{m(s['EV']):6.2f}{m(s['Med']):6.2f}{m(s['P10']):6.2f}{m(s['P90']):7.2f}"
              f"{m(s['dEV']):+7.2f}{s['Ppos']:7.0%}{s['TL']:7.0%}{s['KILL']:7.0%}"
              f"{m(s['dP10']):+7.2f}{m(s['gap']):7.2f}{m(s['eqok']):9.2f}"
              f"{m(ro['dEV']):+8.2f}{ro['Ppos']:8.0%}{m(s1['EV']):7.2f}  "
              f"{STAGE1_EV[k]} / {C[k]['cash']}")
    print()
    # ---------------------------------------------------------- break-even
    print('Break-even P(fail) (dEV = 0) vs the value used:')
    out = []
    for k in ORDER:
        pf_used = sum(s['p'] for s in C[k]['scen'] if s['bucket'] == 'fail')
        lo, hi = -0.6, 0.6
        for _ in range(25):
            mid = (lo + hi) / 2
            d = run(k, D, pfail_shift=mid)['W'].mean() - Ws.mean()
            lo, hi = (mid, hi) if d > 0 else (lo, mid)
        be = pf_used + lo
        out.append(f"{k} {'none' if be <= 0.02 else f'{min(be, .95):.2f}'} ({pf_used:.2f})")
    print('  ' + ' | '.join(out))
    print()
    # ---------------------------------------------------------- tornado
    top = ['S1', 'S2b', 'B1', 'S2c']
    print('Tornado (change in dEV, A$M) for the modeller\'s top 3 shortlist candidates + S2c:', top)
    for k in top:
        base = res[k]['dEV']
        rows = []
        def d(**kw):
            return (run(k, D, **kw)['W'].mean() - Ws.mean() - base) / 1e6
        rows.append(('exit values x0.75/x1.25',
                     d(scale=dict(modest=.75, good=.75, great=.75)),
                     d(scale=dict(modest=1.25, good=1.25, great=1.25))))
        rows.append(('P(fail) +10/-10 pts', d(pfail_shift=.10), d(pfail_shift=-.10)))
        rows.append(('great value x0.5/x1.5', d(scale=dict(great=.5)), d(scale=dict(great=1.5))))
        rows.append(('good value x0.7/x1.3', d(scale=dict(good=.7)), d(scale=dict(good=1.3))))
        rows.append(('equity tax 47%/23.5%', d(tax_override=.47), d(tax_override=.235)))
        rows.append(('venture salary x0.8/x1.2', d(sal_scale=.8), d(sal_scale=1.2)))
        A2 = dict(BASE); A2['emp_equity_vals'] = tuple(2 * v for v in BASE['emp_equity_vals'])
        A3 = dict(BASE); A3['emp_equity_vals'] = tuple(.5 * v for v in BASE['emp_equity_vals'])
        D2 = make_draws(N, RNG_SEED); D2['E'] = D['E'] * 2
        D3 = make_draws(N, RNG_SEED); D3['E'] = D['E'] * .5
        e2 = (run(k, D2)['W'].mean() - stay(D2)[0].mean() - base) / 1e6
        e3 = (run(k, D3)['W'].mean() - stay(D3)[0].mean() - base) / 1e6
        rows.append(('employer equity x2/x0.5', e2, e3))
        rows.append(('1-yr slip / none', d(delay=1.0), 0.0))
        rows.append(('low salary: A$100k/yr reinvested @0%/@20% ROIC',
                     d(lowsal_cut=100e3, roic=0.0), d(lowsal_cut=100e3, roic=0.20)))
        rows.sort(key=lambda x: -max(abs(x[1]), abs(x[2])))
        print(f"  {k} base dEV {base/1e6:+.2f}, P>stay {res[k]['Ppos']:.0%}")
        for name, a, b in rows:
            print(f"     {name:48}{a:+6.2f} /{b:+6.2f}")
    print()
    # ---------------------------------------------------------- P>stay sensitivity
    print('P(positive) under tax/exit sensitivities (top candidates):')
    for k in top:
        a = (run(k, D, tax_override=.235)['W'] > Ws).mean()
        b = (run(k, D, scale=dict(modest=.75, good=.75, great=.75))['W'] > Ws).mean()
        c = (run(k, D, pfail_shift=.10)['W'] > Ws).mean()
        print(f"  {k}: base {res[k]['Ppos']:.0%} | tax 23.5% {a:.0%} | exits x0.75 {b:.0%} "
              f"| P(fail)+10pts {c:.0%}")
    print()
    # ---------------------------------------------------------- S1 reconciliation
    print('S1 dispute: report 11 (EV ~A$11.8M, P+ 59%) vs report 14 (EV ~A$3.3M, P+ 25%)')
    def ev(p, v):
        return sum(a * b for a, b in zip(p, v))
    p11, v11 = (.18, .45, .28, .09), (0.2, 3.0, 18.0, 60.0)
    steps = [('11 as published: pre-tax founder EQUITY, salary excluded', p11, v11, 1.0)]
    p_me = (.32, .43, .20, .05)
    steps.append(('(1) base rates -> .32/.43/.20/.05 (great 5%)', p_me, v11, 1.0))
    v_me = (0.0, 2.8, 12.0, 40.0)
    steps.append(('(2) values: 1.0x-rev modest, 7-8x EBITDA good, raise dilution great',
                  p_me, v_me, 1.0))
    steps.append(('(3) enacted CGT (35/45/46%)', p_me,
                  (0, 2.8 * .65, 12 * .55, 40 * .54), 1.0))
    for name, p, v, f in steps:
        print(f"   {name:72} equity EV {ev(p, v)*f:5.2f}")
    print(f"   (4) full model, incl. low salary, capital, forgone A$500k + employer equity:"
          f" dEV {m(res['S1']['dEV']):+.2f}, P>stay {res['S1']['Ppos']:.0%}, "
          f"wealth EV {m(res['S1']['EV']):.2f} vs stay {m(Ws.mean()):.2f}")
    p14 = (.30, .40, .22, .08)   # implied generic SME version (14 gives EV 3.3M/25%)
    s14 = summarise(run('S1', D, probs=dict(zip(('fail', 'modest', 'good', 'great'), p14)),
                        scale=dict(modest=.7, good=.6, great=.5)), Ws, INCs)
    print(f"   (5) 14's generic-SME version (values x0.5-0.7: SME ACVs, Xero/MYOB bundling): "
          f"dEV {m(s14['dEV']):+.2f}, P>stay {s14['Ppos']:.0%}")
    s11 = summarise(run('S1', D, probs=dict(zip(('fail', 'modest', 'good', 'great'), p11)),
                        scale=dict(modest=3.0/2.8, good=18/12, great=60/40)), Ws, INCs)
    print(f"   (6) 11's own inputs through this model (salary, tax, forgone pay): "
          f"dEV {m(s11['dEV']):+.2f}, P>stay {s11['Ppos']:.0%}")
    print()
    # ---------------------------------------------------------- salary/reinvest
    print('Salary path: dEV and P>stay with founder salary capped at A$150k (cut reinvested)')
    for k in top:
        for roic in (0.0, 0.15, 0.30):
            s = summarise(run(k, D, lowsal_cut=250e3, roic=roic), Ws, INCs)
            print(f"   {k} ROIC {roic:.0%}: dEV {m(s['dEV']):+.2f}  P>stay {s['Ppos']:.0%}  "
                  f"P10 {m(s['P10']):.2f}")
    print()
    print('Bucket probabilities used (fail incl. killed-while-employed / modest / good / great):')
    for k in ORDER:
        agg = {}
        for s in C[k]['scen']:
            agg[s['bucket']] = agg.get(s['bucket'], 0) + s['p']
        print(f"   {k:4} " + ' / '.join(f"{agg[b]:.2f}" for b in ('fail', 'modest', 'good', 'great'))
              + f"   ({C[k]['name']})")


if __name__ == '__main__':
    main()
