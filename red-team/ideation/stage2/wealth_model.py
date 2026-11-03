#!/usr/bin/env python3
"""
Stage-2 probability-weighted wealth model (wealth-modeller lens), 3 Nov 2026.

Models candidates C0-C9 from red-team/ideation/SHORTLIST.md plus the
stay-employed baseline on ONE consistent set of assumptions.

Output metric: founder's year-10 wealth CREATED by the path, in nominal A$,
after tax, with every after-tax cash flow compounded at 4%/yr to year 10.
  wealth = after-tax salary/fees (employment or venture)
         + after-tax employer equity vested while employed
         + after-tax founder equity proceeds (incl. return of own capital)
         - personal capital invested
No living costs are deducted in the headline figure (same convention as most
stage-1 agents). Living costs and existing wealth enter only the certainty-
equivalent (CE) calculation, where levels matter.

All scenario values are the modeller's re-estimates [estimate] unless noted.
Run:  python3 wealth_model.py   (prints all tables; deterministic seed)
"""
import numpy as np

RNG_SEED = 20261103
N = 40_000
YEARS = 10

# ---------------------------------------------------------------- assumptions
BASE = dict(
    salary0=500_000,        # current package, year 1 [brief]
    salary_growth=(0.01, 0.05),  # uniform range of annual growth, staying
    reentry_factor=0.85,    # salary on returning to a job after a failed venture
    reentry_gap=0.5,        # years of zero income before re-entry
    reentry_equity=0.5,     # re-entry job grants half the equity rate
    # employer equity, pre-tax value accruing over 10 yrs if he stays [estimate]
    emp_equity_vals=(200_000, 1_000_000, 3_000_000),
    emp_equity_probs=(0.50, 0.35, 0.15),   # mean ~A$0.9M
    emp_equity_tax=0.40,
    reinvest=0.04,          # after-tax return on saved cash
    illiquid_haircut=0.20,  # equity still held at year 10 is marked down 20%
    w0=3_000_000,           # existing liquid net worth [assumption]
    living=180_000,         # after-tax living costs, growing 3%/yr (CE only)
    gamma=2.0,              # CRRA coefficient of relative risk aversion
)

# Equity tax: the May-2026 Budget proposes replacing the 50% CGT discount with
# indexation + 30% minimum tax from 1 Jul 2027 [verified as a proposal: EY,
# Baker McKenzie, Ashurst budget notes]. Founder gains here accrue almost all
# after Jul 2027 on a low cost base, so indexation barely helps and the gain is
# taxed near the 47% marginal rate. A startup carve-out (50% discount for
# early-stage founders) is under consultation [verified as proposal: Grant
# Thornton, BDO, Forbes AU, Jun 2026]; it probably won't cover buyouts, funds
# or land development. Effective rates used [estimate]:
TAX_BUYOUT = 0.40   # holdcos, roll-ups, land development profit
TAX_CARRY = 0.42    # fund carry / promote / GP stake
TAX_STARTUP = 0.33  # VC startups: ~50% chance the carve-out applies
TAX_OLD = 0.235     # sensitivity: pre-reform 50% discount at 47%


def income_tax(x):
    """2026-27 resident rates incl. 2% Medicare [verified: superguide, etax]."""
    x = np.asarray(x, float)
    t = np.zeros_like(x)
    for lo, hi, r in ((18_200, 45_000, 0.15), (45_000, 135_000, 0.30),
                      (135_000, 190_000, 0.37), (190_000, 1e12, 0.45)):
        t += np.clip(np.minimum(x, hi) - lo, 0, None) * r
    return t + 0.02 * x


# --------------------------------------------------------------- candidates
# Each scenario: p, quit (yr he stops employment; None = never),
#   sal: list of (from_year_absolute, pre-tax A$/yr) venture cash comp steps,
#   end: year venture income stops (fail) -> re-entry after gap; None = runs to 10
#   cap: list of (year, A$) personal capital in;  rec: (year, A$) capital salvage
#   X: founder equity proceeds pre-tax (A$, includes own capital) at exit yr
#   bucket: fail/modest/good/great
def S(bucket, p, quit, sal=(), end=None, cap=(), rec=None, X=0.0, exit=10.0,
      sigma=0.5):
    return dict(bucket=bucket, p=p, quit=quit, sal=list(sal), end=end,
                cap=list(cap), rec=rec, X=X, exit=exit, sigma=sigma)


C = {}

C['C0'] = dict(name='Rent-roll engine hybrid (stay employed)', tax=TAX_BUYOUT,
    note='never quits; $40k test + $400k co-invest for 10-20% of a licensed '
         'operator roll-up', scen=[
    S('fail', .40, None, cap=[(0.3, 40e3), (1.5, 400e3)], rec=(4.0, 80e3)),
    S('modest', .35, None, cap=[(0.3, 40e3), (1.5, 400e3)], X=1.0e6, exit=8),
    S('good', .19, None, cap=[(0.3, 40e3), (1.5, 400e3)], X=3.0e6, exit=8),
    S('great', .06, None, cap=[(0.3, 40e3), (1.5, 400e3)], X=7.0e6, exit=9),
])

C['C1'] = dict(name='ANZ vertical-software holdco', tax=TAX_BUYOUT,
    note='search while employed, quit m9, close deal 1 ~m18', scen=[
    S('fail', .20, 0.75, sal=[(0.75, 0)], end=2.0, cap=[(0.75, 120e3)]),
    S('fail', .15, 0.75, sal=[(0.75, 0), (1.5, 300e3)], end=4.0,
      cap=[(0.75, 120e3), (1.5, 900e3)], rec=(4.0, 180e3)),
    S('modest', .38, 0.75, sal=[(0.75, 0), (1.5, 300e3), (3.5, 375e3)],
      cap=[(0.75, 120e3), (1.5, 900e3)], X=2.2e6, exit=9, sigma=.4),
    S('good', .21, 0.75, sal=[(0.75, 0), (1.5, 300e3), (3, 450e3), (5, 550e3)],
      cap=[(0.75, 120e3), (1.5, 900e3)], X=8.0e6, exit=9),
    S('great', .06, 0.75, sal=[(0.75, 0), (1.5, 300e3), (3, 450e3), (5, 650e3)],
      cap=[(0.75, 120e3), (1.5, 900e3)], X=28e6, exit=10.5, sigma=.6),
])

C['C2'] = dict(name='AI-native accounting roll-up (Ledgerline)', tax=TAX_BUYOUT,
    note='PE-backed: high salary, 12-20% ownership; crowded field', scen=[
    S('fail', .15, 0.75, sal=[(0.75, 0)], end=1.75, cap=[(0.75, 60e3)]),
    S('fail', .22, 0.75, sal=[(0.75, 0), (1.25, 400e3)], end=4.0,
      cap=[(0.75, 60e3), (1.25, 600e3)], rec=(4.0, 60e3)),
    S('modest', .40, 0.75, sal=[(0.75, 0), (1.25, 400e3), (3, 450e3)],
      cap=[(0.75, 60e3), (1.25, 600e3)], X=1.8e6, exit=8, sigma=.4),
    S('good', .18, 0.75, sal=[(0.75, 0), (1.25, 450e3), (3, 550e3)],
      cap=[(0.75, 60e3), (1.25, 600e3)], X=7.0e6, exit=8),
    S('great', .05, 0.75, sal=[(0.75, 0), (1.25, 450e3), (3, 600e3)],
      cap=[(0.75, 60e3), (1.25, 600e3)], X=22e6, exit=9, sigma=.6),
])

C['C3'] = dict(name='SMSF compliance factory', tax=TAX_BUYOUT,
    note='family-office holdco, 25-30% founder; fee deflation priced in', scen=[
    S('fail', .12, 0.75, sal=[(0.75, 0)], end=1.75, cap=[(0.75, 50e3)]),
    S('fail', .18, 0.75, sal=[(0.75, 0), (1.25, 300e3)], end=4.0,
      cap=[(0.75, 50e3), (1.25, 700e3)], rec=(4.0, 175e3)),
    S('modest', .45, 0.75, sal=[(0.75, 0), (1.25, 300e3), (3, 350e3)],
      cap=[(0.75, 50e3), (1.25, 700e3)], X=2.2e6, exit=8, sigma=.4),
    S('good', .20, 0.75, sal=[(0.75, 0), (1.25, 300e3), (3, 450e3)],
      cap=[(0.75, 50e3), (1.25, 700e3)], X=8.0e6, exit=8),
    S('great', .05, 0.75, sal=[(0.75, 0), (1.25, 300e3), (3, 500e3)],
      cap=[(0.75, 50e3), (1.25, 700e3)], X=20e6, exit=9, sigma=.6),
])

C['C4'] = dict(name='Pricing-led B2B distribution holdco', tax=TAX_BUYOUT,
    note='levered platform, ~30% founder FD; ABL without PG is the gate', scen=[
    S('fail', .15, 0.75, sal=[(0.75, 0)], end=2.0, cap=[(0.75, 80e3)]),
    S('fail', .20, 0.75, sal=[(0.75, 0), (1.5, 325e3)], end=4.5,
      cap=[(0.75, 80e3), (1.5, 900e3)], rec=(4.5, 135e3)),
    S('modest', .38, 0.75, sal=[(0.75, 0), (1.5, 325e3), (3, 400e3)],
      cap=[(0.75, 80e3), (1.5, 900e3)], X=3.0e6, exit=8, sigma=.4),
    S('good', .21, 0.75, sal=[(0.75, 0), (1.5, 325e3), (3, 500e3), (5, 600e3)],
      cap=[(0.75, 80e3), (1.5, 900e3)], X=9.0e6, exit=9),
    S('great', .06, 0.75, sal=[(0.75, 0), (1.5, 325e3), (3, 500e3), (5, 650e3)],
      cap=[(0.75, 80e3), (1.5, 900e3)], X=18e6, exit=10.5, sigma=.6),
])

C['C5'] = dict(name='Succession-capital platform (engine + sponsor)', tax=TAX_CARRY,
    note='engine + 1 co-invest while employed; quits ~yr 2.25 only on traction',
    scen=[
    S('fail', .45, None, cap=[(0.3, 100e3), (1.5, 300e3)], rec=(6.0, 180e3)),
    S('modest', .33, 2.25, sal=[(2.25, 300e3), (4, 400e3)],
      cap=[(0.3, 100e3), (1.5, 300e3), (3, 400e3)], X=2.5e6, exit=9, sigma=.4),
    S('good', .17, 2.0, sal=[(2.0, 300e3), (4.5, 550e3)],
      cap=[(0.3, 100e3), (1.5, 300e3), (3, 500e3)], X=7.0e6, exit=10.5),
    S('great', .05, 2.0, sal=[(2.0, 300e3), (4.5, 650e3)],
      cap=[(0.3, 100e3), (1.5, 300e3), (3, 500e3)], X=20e6, exit=10.5, sigma=.6),
])

C['C6'] = dict(name='Succession Credit fund (via BookCo)', tax=TAX_CARRY,
    note='first-time credit manager; quits yr 1 with anchor soft-circled; GP '
         'profits (fees less platform cost) paid out as income', scen=[
    S('fail', .35, 1.0, sal=[(1.0, 0)], end=2.75, cap=[(1.0, 450e3)]),
    S('fail', .10, 1.0, sal=[(1.0, 0), (2.0, 300e3)], end=5.0,
      cap=[(1.0, 500e3), (2.0, 500e3)], rec=(5.0, 250e3)),
    S('modest', .34, 1.0, sal=[(1.0, 0), (2.0, 350e3), (4, 450e3)],
      cap=[(1.0, 500e3), (2.0, 500e3)], X=1.5e6, exit=10.5, sigma=.4),
    S('good', .16, 1.0, sal=[(1.0, 0), (2.0, 350e3), (3, 600e3), (5, 1.1e6)],
      cap=[(1.0, 500e3), (2.0, 500e3)], X=6.0e6, exit=10.5),
    S('great', .05, 1.0, sal=[(1.0, 0), (2.0, 350e3), (3, 700e3), (5, 1.6e6)],
      cap=[(1.0, 500e3), (2.0, 500e3)], X=18e6, exit=9, sigma=.6),
])

C['C7'] = dict(name='Private-markets valuation layer (Mark)', tax=TAX_STARTUP,
    note='VC path; seed salary; liquidation prefs cut modest exits', scen=[
    S('fail', .55, 0.75, sal=[(0.75, 0), (1.25, 250e3)], end=3.0,
      cap=[(0.75, 300e3)]),
    S('modest', .28, 0.75, sal=[(0.75, 0), (1.25, 250e3), (3, 300e3)],
      cap=[(0.75, 300e3)], X=2.0e6, exit=7, sigma=.5),
    S('good', .13, 0.75, sal=[(0.75, 0), (1.25, 250e3), (3, 350e3), (5, 450e3)],
      cap=[(0.75, 300e3)], X=14e6, exit=9, sigma=.6),
    S('great', .04, 0.75, sal=[(0.75, 0), (1.25, 250e3), (3, 400e3), (5, 500e3)],
      cap=[(0.75, 300e3)], X=45e6, exit=10, sigma=.7),
])

C['C8'] = dict(name='AI-priced niche MGA', tax=0.36,
    note='capacity-gated; needs underwriter co-founder', scen=[
    S('fail', .55, 0.5, sal=[(0.5, 0), (1.25, 250e3)], end=3.0,
      cap=[(0.5, 400e3)], rec=(3.0, 50e3)),
    S('modest', .23, 0.5, sal=[(0.5, 0), (1.25, 250e3), (3, 300e3)],
      cap=[(0.5, 400e3)], X=1.5e6, exit=7, sigma=.5),
    S('good', .17, 0.5, sal=[(0.5, 0), (1.25, 250e3), (4, 400e3)],
      cap=[(0.5, 400e3)], X=10e6, exit=9, sigma=.6),
    S('great', .05, 0.5, sal=[(0.5, 0), (1.25, 250e3), (4, 500e3)],
      cap=[(0.5, 400e3)], X=30e6, exit=10, sigma=.7),
])

C['C9'] = dict(name='Grid-capacity arbitrage (powered land)', tax=TAX_BUYOUT,
    note='options not land; lumpy; first site sale yr 3-4', scen=[
    S('fail', .45, 1.0, sal=[(1.0, 0)], end=3.0, cap=[(1.0, 250e3), (2.0, 250e3)],
      rec=(3.0, 50e3)),
    S('modest', .30, 1.0, sal=[(1.0, 0), (2.5, 250e3)],
      cap=[(1.0, 250e3), (2.0, 250e3)], X=2.5e6, exit=6, sigma=.5),
    S('good', .19, 1.0, sal=[(1.0, 0), (2.5, 300e3), (4, 450e3), (6, 550e3)],
      cap=[(1.0, 250e3), (2.0, 250e3), (3, 300e3)], X=9.0e6, exit=9),
    S('great', .06, 1.0, sal=[(1.0, 0), (2.5, 300e3), (4, 500e3), (6, 650e3)],
      cap=[(1.0, 250e3), (2.0, 250e3), (3, 300e3)], X=25e6, exit=10, sigma=.7),
])

# ---- Sequencing variants (not shortlist candidates): buyout entered only once
# a deal is signed and debt is termed while still employed (needs employer
# consent). No-deal outcomes cost almost nothing; everything shifts ~1.25 yrs.
C['C4s'] = dict(name='C4 staged: quit only at signed SPA + ABL', tax=TAX_BUYOUT,
    note='sourcing while employed via C5 engine; quit yr 2', scen=[
    S('fail', .25, None, cap=[(0.5, 80e3)]),
    S('fail', .17, 2.0, sal=[(2.0, 325e3)], end=5.0, cap=[(2.0, 900e3)],
      rec=(5.0, 135e3)),
    S('modest', .33, 2.0, sal=[(2.0, 325e3), (3.5, 400e3)], cap=[(0.5, 80e3), (2.0, 900e3)],
      X=3.0e6, exit=9, sigma=.4),
    S('good', .19, 2.0, sal=[(2.0, 325e3), (3.5, 500e3), (5.5, 600e3)],
      cap=[(0.5, 80e3), (2.0, 900e3)], X=9.0e6, exit=10),
    S('great', .06, 2.0, sal=[(2.0, 325e3), (3.5, 500e3), (5.5, 650e3)],
      cap=[(0.5, 80e3), (2.0, 900e3)], X=18e6, exit=10.5, sigma=.6),
])
C['C1s'] = dict(name='C1 staged: quit only at signed deal 1', tax=TAX_BUYOUT,
    note='as C4s; employer conflict risk higher (SaaS employer)', scen=[
    S('fail', .25, None, cap=[(0.5, 120e3)]),
    S('fail', .14, 2.0, sal=[(2.0, 300e3)], end=4.75, cap=[(2.0, 900e3)],
      rec=(4.75, 180e3)),
    S('modest', .34, 2.0, sal=[(2.0, 300e3), (4, 375e3)], cap=[(0.5, 120e3), (2.0, 900e3)],
      X=2.2e6, exit=9.5, sigma=.4),
    S('good', .21, 2.0, sal=[(2.0, 300e3), (3.5, 450e3), (5.5, 550e3)],
      cap=[(0.5, 120e3), (2.0, 900e3)], X=8.0e6, exit=10),
    S('great', .06, 2.0, sal=[(2.0, 300e3), (3.5, 450e3), (5.5, 650e3)],
      cap=[(0.5, 120e3), (2.0, 900e3)], X=28e6, exit=10.5, sigma=.6),
])

# Stage-1 agents' bucket probabilities (averaged where several agents scored it)
STAGE1_P = dict(
    C1=dict(fail=.25, modest=.35, good=.29, great=.11),
    C2=dict(fail=.25, modest=.35, good=.28, great=.12),
    C3=dict(fail=.275, modest=.375, good=.25, great=.10),
    C4=dict(fail=.20, modest=.35, good=.32, great=.13),
    C5=dict(fail=.325, modest=.35, good=.225, great=.10),
    C6=dict(fail=.30, modest=.35, good=.25, great=.10),
    C7=dict(fail=.375, modest=.30, good=.235, great=.09),
    C8=dict(fail=.47, modest=.23, good=.20, great=.10),
    C9=dict(fail=.35, modest=.30, good=.25, great=.10),
)

# Stage-1 headline EVs (as quoted in SHORTLIST.md) for the comparison column
STAGE1_EV = dict(C0='3.0-3.4 (7y)', C1='8.0-8.5', C2='4.3-9.3', C3='5.4-5.5',
                 C4='7.2', C5='4.9-7.8', C6='4.7-5.3', C7='4.0-6.6',
                 C8='5.7-7.6', C9='4.9-6.2', C4s='n/a', C1s='n/a')


# ---------------------------------------------------------------- simulation
def sal_at(steps, t):
    v = 0.0
    for start, amt in steps:
        if t >= start:
            v = amt
    return v


def overlap(a0, a1, b0, b1):
    return max(0.0, min(a1, b1) - max(a0, b0))


def simulate_path(scen, tax_eq, draws, A, scale_X=1.0, sal_scale=1.0, delay=0.0):
    """Return (wealth[N], income[N, YEARS]) for one scenario across draws."""
    g, E, z = draws['g'], draws['E'], draws['z']
    n = len(g)
    quit = scen['quit']
    end = scen['end']
    q = 99.0 if quit is None else quit
    ret = None if end is None else end + delay + A['reentry_gap']
    wealth = np.zeros(n)
    income = np.zeros((n, YEARS))
    for y in range(1, YEARS + 1):
        y0, y1 = y - 1.0, float(y)
        growth = (1 + g) ** (y - 1)
        emp_share = overlap(y0, y1, 0, q)
        re_share = overlap(y0, y1, ret, 99) if ret is not None else 0.0
        venture_share_end = (end + delay) if end is not None else 99.0
        # venture income: integrate steps over the year (monthly resolution)
        ven = 0.0
        for m in range(12):
            t = y0 + (m + 0.5) / 12
            if q <= t < venture_share_end:
                st = [(s + (delay if s > q else 0), a) for s, a in scen['sal']]
                ven += sal_at(st, t) / 12 * sal_scale
        emp = A['salary0'] * growth * (emp_share + re_share * A['reentry_factor'])
        pre = emp + ven
        income[:, y - 1] = pre
        after = pre - income_tax(pre)
        # employer equity accrues while employed
        eq = E / YEARS * (emp_share + re_share * A['reentry_equity'])
        after = after + eq * (1 - A['emp_equity_tax'])
        wealth += after * (1 + A['reinvest']) ** (YEARS - (y - 0.5))
    # capital in / salvage
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
    if scen['X'] > 0:
        s = scen['sigma']
        X = scen['X'] * scale_X * np.exp(s * z - s * s / 2)
        tx = scen['exit'] + delay
        if tx > YEARS:
            X = X * (1 - A['illiquid_haircut'])
            tx = YEARS
        net = X - tax_eq * np.maximum(0, X - capital_total)
        wealth += net * (1 + A['reinvest']) ** (YEARS - tx)
    return wealth, income


def make_draws(n, seed):
    rng = np.random.default_rng(seed)
    A = BASE
    return dict(
        g=rng.uniform(*A['salary_growth'], n),
        E=rng.choice(A['emp_equity_vals'], size=n, p=A['emp_equity_probs']),
        z=rng.standard_normal(n),
        u=rng.uniform(size=n),
    )


def stay(draws, A):
    s = S('stay', 1.0, None)
    return simulate_path(s, 0.0, draws, A)


def run(cand, draws, A=BASE, pfail_shift=0.0, scale=None, sal_scale=1.0,
        delay=0.0, tax=None, probs=None, return_q=False):
    """Mix scenarios by draws['u']. scale: dict bucket->multiplier on X.
    probs: optional bucket->probability override (spread pro rata within bucket)."""
    scale = scale or {}
    ps = np.array([s['p'] for s in cand['scen']], float)
    if probs:
        bk = [s['bucket'] for s in cand['scen']]
        tot = {b: sum(p for p, bb in zip(ps, bk) if bb == b) for b in set(bk)}
        ps = np.array([p / tot[b] * probs[b] for p, b in zip(ps, bk)])
    fails = np.array([s['bucket'] == 'fail' for s in cand['scen']])
    if pfail_shift:
        pf = ps[fails].sum()
        new_pf = min(max(pf + pfail_shift, 0.01), 0.95)
        ps[fails] *= new_pf / pf
        ps[~fails] *= (1 - new_pf) / (1 - pf)
    ps = ps / ps.sum()
    cum = np.cumsum(ps)
    idx = np.searchsorted(cum, draws['u'])
    idx = np.minimum(idx, len(ps) - 1)
    n = len(draws['u'])
    W = np.zeros(n)
    INC = np.zeros((n, YEARS))
    Q = np.full(n, np.nan)
    for k, sc in enumerate(cand['scen']):
        mask = idx == k
        if not mask.any():
            continue
        sub = {kk: v[mask] for kk, v in draws.items()}
        w, inc = simulate_path(sc, tax if tax is not None else cand['tax'], sub, A,
                               scale_X=scale.get(sc['bucket'], 1.0),
                               sal_scale=sal_scale, delay=delay)
        W[mask] = w
        INC[mask] = inc
        if sc['quit'] is not None:
            Q[mask] = sc['quit']
    if return_q:
        return W, INC, ps, Q
    return W, INC, ps


def ce(W, A=BASE):
    living = sum(A['living'] * 1.03 ** (y - 1) * (1 + A['reinvest']) ** (YEARS - (y - 0.5))
                 for y in range(1, YEARS + 1))
    tot = np.maximum(A['w0'] + W - living, 50_000)
    gm = A['gamma']
    if abs(gm - 1) < 1e-9:
        c = np.exp(np.mean(np.log(tot)))
    else:
        c = np.mean(tot ** (1 - gm)) ** (1 / (1 - gm))
    return c - A['w0'] + living


def years_to_replace(INC, Q):
    """Years from quitting until the first full calendar year with pre-tax cash
    income (venture pay/fees/distributions, or a re-entry job) >= A$500k
    nominal. Never quits -> 0. Not reached by year 10 -> 99."""
    n = INC.shape[0]
    out = np.zeros(n)
    for i in range(n):
        q = Q[i]
        if np.isnan(q):
            continue
        out[i] = 99
        for y in range(int(np.floor(q)) + 2, YEARS + 1):   # first full year after quit
            if INC[i, y - 1] >= 500_000:
                out[i] = y - q
                break
    return out


def m(x):
    return f"{x/1e6:5.2f}"


def main():
    A = BASE
    draws = make_draws(N, RNG_SEED)
    Wst, INCst = stay(draws, A)
    out = []
    P = out.append
    P(f"Stay employed: EV {m(Wst.mean())}M  median {m(np.median(Wst))}M  "
      f"P10 {m(np.percentile(Wst,10))}M  P90 {m(np.percentile(Wst,90))}M  "
      f"CE g=1/2/3 {m(ce(Wst, dict(A, gamma=1.0)))}/{m(ce(Wst))}/"
      f"{m(ce(Wst, dict(A, gamma=3.0)))}M")
    P("")
    hdr = (f"{'ID':3} {'EV':>6} {'Med':>6} {'P10':>6} {'P90':>6} {'dEV':>6} "
           f"{'P>stay':>6} {'CE2':>6} {'dCE2':>6} {'CE1':>6} {'CE3':>6} "
           f"{'Rep<=3y':>10} {'<=5y':>5} {'medYr':>5} {'gap1-5':>6} {'EV@p1':>6}  stage1EV")
    P(hdr)
    results = {}
    for cid, cand in C.items():
        W, INC, ps, Q = run(cand, draws, return_q=True)
        yrs = years_to_replace(INC, Q)
        W1, _, _ = run(cand, draws, probs=STAGE1_P[cid]) if cid in STAGE1_P else (W, 0, 0)
        gap = np.maximum(0, INCst[:, :5] - INC[:, :5]).sum(axis=1).mean()
        Ag1 = dict(A, gamma=1.0)
        Ag3 = dict(A, gamma=3.0)
        r = dict(EV=W.mean(), med=np.median(W), p10=np.percentile(W, 10),
                 p90=np.percentile(W, 90), dEV=W.mean() - Wst.mean(),
                 pbeat=(W > Wst).mean(), ce2=ce(W), ce1=ce(W, Ag1), ce3=ce(W, Ag3),
                 p3=(yrs <= 3).mean(), p5=(yrs <= 5).mean(),
                 medyr=np.median(yrs), gap=gap, ev1=W1.mean())
        r['dce'] = r['ce2'] - ce(Wst)
        results[cid] = r
        P(f"{cid:3} {m(r['EV'])} {m(r['med'])} {m(r['p10'])} {m(r['p90'])} "
          f"{m(r['dEV'])} {r['pbeat']:6.0%} {m(r['ce2'])} {m(r['dce'])} "
          f"{m(r['ce1'])} {m(r['ce3'])} {r['p3']:10.0%} {r['p5']:5.0%} "
          f"{r['medyr']:5.1f} {m(gap)} {m(r['ev1'])}  {STAGE1_EV[cid]}")
    P("")
    P("Notes: A$M, nominal year-10 after-tax wealth created over 10 yrs. "
      "Rep<=3y/<=5y: share of runs whose pre-tax cash income is back to >= A$500k "
      "in a full year within 3/5 years of quitting (never quitting counts as "
      "replaced). medYr = median years from quit to that point (99 = not by "
      "yr 10). EV@p1 = EV with the stage-1 agents' bucket probabilities on this "
      "model's values. gap1-5 = expected pre-tax income forgone vs "
      "staying in yrs 1-5. CE1/CE2/CE3 = certainty equivalents (gamma 1/2/3, "
      "W0 A$3M, living A$180k/yr).")
    P("")
    # bucket probabilities and old-tax-regime sensitivity
    P("Bucket probabilities used (fail/modest/good/great) and EV under the "
      "pre-2027 CGT regime (23.5%):")
    for cid, cand in C.items():
        b = {}
        for s in cand['scen']:
            b[s['bucket']] = b.get(s['bucket'], 0) + s['p']
        W_old, _, _ = run(cand, draws, tax=TAX_OLD)
        P(f"  {cid} {cand['name'][:46]:46} "
          f"{b.get('fail',0):.2f}/{b.get('modest',0):.2f}/{b.get('good',0):.2f}/"
          f"{b.get('great',0):.2f}  EV_oldtax {m(W_old.mean())}  "
          f"dEV_oldtax {m(W_old.mean()-Wst.mean())}")
    P("")
    # tornado on top 3 by dCE
    top = ['C0', 'C5', 'C4s', 'C2']  # modeller's top 3 (C4 via staged entry) + C2, 3rd by CE
    P("Tornado (change in dEV vs staying, A$M; low / high input):")
    for cid in top:
        cand = C[cid]
        base = results[cid]['dEV']
        rows = []

        def d(**kw):
            W, _, _ = run(cand, draws, **kw)
            return W.mean() - Wst.mean() - base
        rows.append(('P(fail) -10 / +10 pts', d(pfail_shift=-0.10), d(pfail_shift=+0.10)))
        rows.append(('Great-case value x0.5 / x1.5', d(scale={'great': .5}), d(scale={'great': 1.5})))
        rows.append(('Good-case value x0.7 / x1.3', d(scale={'good': .7}), d(scale={'good': 1.3})))
        rows.append(('All exit values x0.75 / x1.25',
                     d(scale={'modest': .75, 'good': .75, 'great': .75}),
                     d(scale={'modest': 1.25, 'good': 1.25, 'great': 1.25})))
        rows.append(('Venture salary x0.8 / x1.2', d(sal_scale=.8), d(sal_scale=1.2)))
        rows.append(('Timeline +1 yr slip / none', d(delay=1.0), 0.0))
        rows.append(('Equity tax 47% / 23.5%', d(tax=0.47), d(tax=TAX_OLD)))
        def d_emp(f):
            dr = dict(draws, E=draws['E'] * f)
            Wc, _, _ = run(cand, dr)
            Ws, _ = stay(dr, A)
            return Wc.mean() - Ws.mean() - base
        rows.append(('Employer equity x2 / x0.5', d_emp(2.0), d_emp(0.5)))
        rows.sort(key=lambda r: -abs(r[1] - r[2]))
        P(f"  {cid} {cand['name']}  base dEV {m(base)}M")
        for lab, lo, hi in rows:
            P(f"    {lab:40} {lo/1e6:+6.2f} {hi/1e6:+6.2f}")
    P("")
    # breakeven: P(fail) at which dEV = 0 for each candidate
    P("Break-even P(fail) (dEV vs staying = 0), other buckets rescaled:")
    for cid, cand in C.items():
        pf0 = sum(s['p'] for s in cand['scen'] if s['bucket'] == 'fail')
        lo, hi = -pf0 + 0.01, 0.94 - pf0
        f = lambda sh: run(cand, draws, pfail_shift=sh)[0].mean() - Wst.mean()
        if f(hi) > 0:
            be = '>0.94'
        elif f(lo) < 0:
            be = '<0.01'
        else:
            for _ in range(25):
                mid = (lo + hi) / 2
                if f(mid) > 0:
                    lo = mid
                else:
                    hi = mid
            be = f"{pf0 + lo:.2f}"
        P(f"  {cid}: used {pf0:.2f}, break-even {be}")
    txt = "\n".join(out)
    print(txt)
    with open(__file__.replace('.py', '_output.txt'), 'w') as fh:
        fh.write(txt + "\n")


if __name__ == '__main__':
    main()
