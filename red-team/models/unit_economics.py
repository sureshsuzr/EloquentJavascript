#!/usr/bin/env python3
"""
Unit-economics model: AI-native residential PM agency, one Melbourne corridor.
Red-team CFO modeller, 2 Nov 2026. Stdlib only. Run: python3 unit_economics.py

All money AUD, ex-GST, nominal (no inflation indexation: rents and wages are
assumed to move together, which is generous to the plan).

Key definitions
- EBITDA: business earnings before interest/tax, with the founder working for $0.
- Founder salary capacity (FSC): the most the company can pay the founder as a
  deductible salary while still funding, from after-tax profit, its loan
  principal and any capitalised roll purchases, and expensing funnel CAC:
      FSC = EBITDA - interest - funnel CAC - (principal + roll capex) / (1 - t)
  This is the number to compare with the ~$500k income target (pre-personal-tax).
  It assumes rent-roll purchase price is NOT tax-deductible or amortisable
  (capital/CGT asset) -- confirm with a tax adviser.
"""
import copy

BASE = dict(
    # ---- revenue drivers ----
    rent_pw=620.0,            # avg weekly rent in managed book (Cotality all-dwellings ~$641 Q2-26; Domain asking ~$600)
    occupancy=0.975,          # fee only on rent collected (Melb vacancy ~1.2-2%, plus re-let gaps)
    fee_incl_gst=0.050,       # headline mgmt fee, quoted incl GST ("at or slightly under market")
    gst=0.10,
    turnover=0.30,            # share of tenancies re-let per year
    letting_weeks=1.5,        # letting fee, weeks of rent incl GST
    ancillary=100.0,          # admin/statement, lease prep, VCAT attendance etc, per property per year
    sale_rate=0.06,           # share of landlords selling per year
    referral_capture=0.50,    # gate 3: half of sellers run selection through founder
    referral_fee=2500.0,      # ex GST, ~20-25% of a ~$12-15k Melbourne commission
    # ---- variable cost drivers ----
    props_per_pm=390,         # 3x incumbent 130
    pm_loaded=132_000.0,      # $110k base + super 12% + payroll tax/workcover/leave
    props_per_ops=800,        # trust accounting / arrears / admin FTE
    ops_loaded=95_000.0,
    field=350.0,              # inspections, condition reports, lease-up tours (brief: $300-450)
    software_ai=150.0,        # PropertyMe-class SoR + AI inference + comms/e-sign/screening
    guarantees=40.0,          # payouts on days-to-lease / maintenance / arrears guarantees
    payments_misc=20.0,       # bank/payment costs absorbed (VIC: no fees on rent payments)
    # ---- fixed costs (per year, at ~1,000 properties) ----
    fixed=575_000.0,          # licensed head of PM/OIEC 180k, AI/eng 160k, insurance PI/PL/cyber 35k,
                              # trust audit+acct+legal 40k, office 50k, comparison site/data 80k, misc 30k
    # ---- acquisition / retention ----
    attrition=0.12,           # gross annual loss of managements (sales not retained, switches, self-manage)
    funnel_cac=3000.0,        # cost per signed management via comparison funnel (gate: <$2k)
    roll_multiple=3.3,        # $ per $1 of management income (ex GST); Melb range ~2.8-3.5 (Acumentis) / brief 3.7 FY22
    transition_loss=0.15,     # acquired managements lost in first year after purchase
    retention_cover=0.07,     # share of those losses compensated via 10-20% retention (~3 months)
    deal_costs=0.03,          # legal, DD, broker, integration as % of price
    # ---- debt ----
    lvr=0.70,
    rate=0.085,               # cash rate 4.60% (Sep-26) + ~3.9% business-loan margin
    term=7,                   # years, P&I
    tax=0.25,                 # base-rate entity company tax
)


def rev_per_prop(p):
    gross_rent = p["rent_pw"] * 52 * p["occupancy"]
    mgmt = gross_rent * p["fee_incl_gst"] / (1 + p["gst"])
    letting = p["rent_pw"] * p["letting_weeks"] * p["turnover"] / (1 + p["gst"])
    referral = p["sale_rate"] * p["referral_capture"] * p["referral_fee"]
    return dict(mgmt=mgmt, letting=letting, ancillary=p["ancillary"], referral=referral,
                total=mgmt + letting + p["ancillary"] + referral)


def var_cost_per_prop(p):
    pm = p["pm_loaded"] / p["props_per_pm"]
    ops = p["ops_loaded"] / p["props_per_ops"]
    rest = p["field"] + p["software_ai"] + p["guarantees"] + p["payments_misc"]
    return dict(pm=pm, ops=ops, field=p["field"], software_ai=p["software_ai"],
                other=p["guarantees"] + p["payments_misc"], total=pm + ops + rest)


def fixed_at(n, p):
    # 55% of fixed is unavoidable from day one (licensee, insurance, eng, audit); rest scales to 1,000;
    # above 1,000 fixed grows 15% per extra 1,000 properties (second office/team lead/finance)
    return p["fixed"] * (0.55 + 0.45 * min(n, 1000) / 1000) + p["fixed"] * 0.15 * max(0, n - 1000) / 1000


def price_per_prop(p):
    return p["roll_multiple"] * rev_per_prop(p)["mgmt"]


def eff_cost_per_retained_roll_prop(p):
    unrecovered = max(0.0, p["transition_loss"] - p["retention_cover"])
    return price_per_prop(p) * (1 + p["deal_costs"]) / (1 - unrecovered)


def annuity(principal, rate, term):
    return principal * rate / (1 - (1 + rate) ** -term) if principal > 0 else 0.0


def steady_state(n, p, roll_share=0.0, debt_phase="peak", replace_via="funnel"):
    """Steady state at n properties. roll_share of the book was bought with debt.
    debt_phase: 'peak' = year after purchase (full balance), 'mid' = average over term, 'none' = repaid."""
    r = rev_per_prop(p)["total"]
    v = var_cost_per_prop(p)["total"]
    ebitda = n * (r - v) - fixed_at(n, p)
    debt0 = n * roll_share * price_per_prop(p) * p["lvr"]
    pay = annuity(debt0, p["rate"], p["term"])
    if debt_phase == "peak":
        interest = debt0 * p["rate"]
    elif debt_phase == "mid":
        interest = debt0 * p["rate"] * 0.55  # avg balance of an annuity loan ~55% of original
    else:
        interest, pay = 0.0, 0.0
    principal = max(0.0, pay - interest) if debt_phase != "none" else 0.0
    if debt_phase == "mid":
        principal = debt0 / p["term"]
    repl = n * p["attrition"]
    funnel = repl * p["funnel_cac"] if replace_via == "funnel" else 0.0
    rollcapex = repl * eff_cost_per_retained_roll_prop(p) if replace_via == "roll" else 0.0
    t = p["tax"]
    fsc = ebitda - interest - funnel - (principal + rollcapex) / (1 - t)
    return dict(n=n, rev=n * r, ebitda=ebitda, margin=ebitda / (n * r), interest=interest,
                principal=principal, maint_acq=funnel + rollcapex, fsc=fsc, debt0=debt0)


def breakeven(p, target, **kw):
    for n in range(100, 20001, 10):
        if steady_state(n, p, **kw)["fsc"] >= target:
            return n
    return None


def ramp(p, plan, years=10):
    """Annual ramp. plan: list of (funnel_signs, roll_buy) per year. Founder paid $0;
    shortfalls funded by founder equity. Returns rows and summary."""
    n = 0.0
    debt = 0.0
    loans = []  # (balance, payment)
    cum_equity = 0.0
    rows = []
    for y in range(years):
        signs, buy = plan[y] if y < len(plan) else plan[-1]
        lost_attr = n * p["attrition"]
        if signs == "R":
            signs = lost_attr
        unrec = max(0.0, p["transition_loss"] - p["retention_cover"])
        retained_buy = buy * (1 - unrec)
        price = buy * price_per_prop(p) * (1 + p["deal_costs"])
        new_debt = buy * price_per_prop(p) * p["lvr"]
        equity_for_roll = price - new_debt
        n_start = n
        n = max(0.0, n - lost_attr + signs + retained_buy)
        n_avg = (n_start + n) / 2
        r = rev_per_prop(p)["total"]
        v = var_cost_per_prop(p)["total"]
        # min staffing: at least 1 PM + fixed floor even tiny
        ebitda = n_avg * (r - v) - fixed_at(max(n_avg, 1), p)
        interest = 0.0
        principal = 0.0
        new_loans = []
        for bal, pay in loans:
            i = bal * p["rate"]
            pr = min(bal, pay - i)
            interest += i
            principal += pr
            if bal - pr > 1:
                new_loans.append((bal - pr, pay))
        loans = new_loans
        if new_debt > 0:
            loans.append((new_debt, annuity(new_debt, p["rate"], p["term"])))
            interest += new_debt * p["rate"] * 0.5  # half-year interest on new loan
        funnel = signs * p["funnel_cac"]
        pretax = ebitda - interest - funnel
        tax = max(0.0, pretax) * p["tax"]
        cash = pretax - tax - principal - equity_for_roll
        cum_equity += -min(0.0, cash) if cash < 0 else 0.0
        debt = sum(b for b, _ in loans)
        rows.append(dict(yr=y + 1, props=n, rev=n_avg * r, ebitda=ebitda, interest=interest,
                         principal=principal, funnel=funnel, roll_equity=equity_for_roll,
                         cash=cash, debt=debt))
    return rows


def fmt(x, w=10):
    return f"{x:>{w},.0f}"


def print_unit(p, label):
    r = rev_per_prop(p)
    v = var_cost_per_prop(p)
    print(f"\n=== Per-property P&L, {label} ===")
    print(f"Revenue  mgmt {r['mgmt']:.0f} | letting {r['letting']:.0f} | ancillary {r['ancillary']:.0f} "
          f"| referral {r['referral']:.0f} | TOTAL {r['total']:.0f}")
    print(f"VarCost  PM {v['pm']:.0f} | ops/trust {v['ops']:.0f} | field {v['field']:.0f} | "
          f"sw/AI {v['software_ai']:.0f} | other {v['other']:.0f} | TOTAL {v['total']:.0f}")
    print(f"Contribution/prop {r['total'] - v['total']:.0f}; fixed/prop @1,000 = {fixed_at(1000, p) / 1000:.0f}")


def main():
    p = copy.deepcopy(BASE)
    print("AUD, ex-GST. Base-case inputs in BASE dict.")
    print(f"Roll price/property = {price_per_prop(p):,.0f}; effective cost per RETAINED acquired property "
          f"(deal costs + unrecovered transition loss) = {eff_cost_per_retained_roll_prop(p):,.0f}")
    print_unit(p, "base 3x (390 props/PM)")

    print("\n=== 0. Incumbent benchmark vs founder direct cost (per property per year) ===")
    inc = dict(pm=75_000 * 1.22 / 130, support=250, software=60)
    inc_total = sum(inc.values())
    print(f"  Incumbent (PM $75k loaded 1.22x /130 does own inspections; leasing/admin support; software): "
          f"PM {inc['pm']:.0f} + support {inc['support']} + sw {inc['software']} = {inc_total:.0f} direct, "
          f"+ ~300 shared overhead")
    for k, ppm in [("1x", 130), ("2x", 260), ("3x", 390), ("4x", 520)]:
        v = var_cost_per_prop(dict(p, props_per_pm=ppm))
        print(f"  Founder {k} ({ppm}/PM): direct {v['total']:.0f}  (vs incumbent {inc_total:.0f}: "
              f"{v['total'] - inc_total:+.0f})")
    bo = var_cost_per_prop(p)["total"] - var_cost_per_prop(p)["pm"]
    print(f"  Gate 2 check: founder back office ex-relationship-PM = {bo:.0f}/property vs Crossub benchmark ~560")

    # ---------- 1. Brief arithmetic check ----------
    print("\n=== 1. Brief arithmetic: 750-850 props x $600-700 margin ===")
    for n, m in [(750, 600), (850, 700), (800, 650)]:
        ebitda = n * m
        repl = n * p["attrition"] * 2000
        print(f"  {n} x {m} = EBITDA {ebitda:,.0f}; less replacing {p['attrition']:.0%} churn at $2k CAC "
              f"= {ebitda - repl:,.0f}; at $3k CAC = {ebitda - n * p['attrition'] * 3000:,.0f}")
    n = 1150
    roll = n * price_per_prop(p)
    d = roll * 0.5
    print(f"  'Half debt-funded' 1,150 props: roll value {roll:,.0f}; debt (50%) {d:,.0f}; interest @8.5% "
          f"{d * 0.085:,.0f}; P&I 7yr {annuity(d, 0.085, 7):,.0f}/yr; founder equity {roll - d:,.0f}")
    print(f"  ...EBITDA at $650 margin {n * 650:,.0f}; FSC = {n * 650 - d * 0.085 - (annuity(d, 0.085, 7) - d * 0.085) / 0.75 - n * 0.12 * 3000:,.0f}")

    # ---------- 2. Productivity scenarios at 1,000 properties ----------
    print("\n=== 2. Productivity scenarios @1,000 properties (steady state) ===")
    print(f"{'scen':>5}{'p/PM':>6}{'rev/p':>7}{'cost/p':>8}{'EBITDA':>10}{'margin':>8}"
          f"{'FSC unlev':>11}{'FSC 50%roll pk':>16}{'FSC 50% mid':>13}{'FSC debt-free':>14}")
    for k, ppm in [("1x", 130), ("2x", 260), ("3x", 390), ("4x", 520)]:
        q = dict(p, props_per_pm=ppm)
        s0 = steady_state(1000, q)
        s1 = steady_state(1000, q, roll_share=0.5, debt_phase="peak")
        s2 = steady_state(1000, q, roll_share=0.5, debt_phase="mid")
        cost = rev_per_prop(q)["total"] - s0["ebitda"] / 1000
        print(f"{k:>5}{ppm:>6}{rev_per_prop(q)['total']:>7.0f}{cost:>8.0f}{fmt(s0['ebitda'])}{s0['margin']:>8.0%}"
              f"{fmt(s0['fsc'], 11)}{fmt(s1['fsc'], 16)}{fmt(s2['fsc'], 13)}{fmt(s0['fsc'], 14)}")

    # ---------- 3. Break-even scale ----------
    print("\n=== 3. Scale needed (properties) for FSC = $0 and FSC = $500k ===")
    print(f"{'scen':>5}{'lean fixed':>11}{'FSC=0 unlev':>13}{'500k unlev':>12}{'500k 50%roll pk':>17}{'500k 100%roll pk':>18}{'500k debt-free':>16}")
    for k, ppm in [("1x", 130), ("2x", 260), ("3x", 390), ("4x", 520)]:
        for fx in (575_000, 400_000):
            q = dict(p, props_per_pm=ppm, fixed=fx)
            be0 = breakeven(q, 0)
            b1 = breakeven(q, 500_000)
            b2 = breakeven(q, 500_000, roll_share=0.5, debt_phase="peak")
            b3 = breakeven(q, 500_000, roll_share=1.0, debt_phase="peak")
            b4 = breakeven(q, 500_000, replace_via="funnel", debt_phase="none")
            f = lambda x: f"{x:,}" if x else ">20k"
            print(f"{k:>5}{fx:>11,}{f(be0):>13}{f(b1):>12}{f(b2):>17}{f(b3):>18}{f(b4):>16}")

    # ---------- 4. Acquisition: funnel vs roll ----------
    print("\n=== 4. Funnel vs roll: cost per retained management and payback ===")
    contrib = rev_per_prop(p)["total"] - var_cost_per_prop(p)["total"]
    print(f"  Contribution per property per year (3x, before fixed) = {contrib:,.0f}")
    for label, cost in [("funnel @ $2k (gate)", 2000), ("funnel @ $3k (base)", 3000),
                        ("funnel @ $5k (bad)", 5000),
                        ("roll @ 2.8x", eff_cost_per_retained_roll_prop(dict(p, roll_multiple=2.8))),
                        ("roll @ 3.3x (base)", eff_cost_per_retained_roll_prop(p)),
                        ("roll @ 3.7x (brief FY22)", eff_cost_per_retained_roll_prop(dict(p, roll_multiple=3.7)))]:
        life = 1 / p["attrition"]
        print(f"  {label:<26} cost/retained {cost:>7,.0f} | payback on contribution {cost / contrib:>4.1f} yrs "
              f"| LTV:CAC (contrib x {life:.1f}yr life) {contrib * life / cost:>4.1f}")
    print("  NB roll cost is partly recoverable (resaleable asset; debt-financeable at 70% LVR); funnel CAC is sunk.")
    eq = eff_cost_per_retained_roll_prop(p) - price_per_prop(p) * p["lvr"]
    print(f"  Roll equity per retained property ~{eq:,.0f}; first-year cash on that equity: contribution {contrib:,.0f} "
          f"- interest {price_per_prop(p) * p['lvr'] * p['rate']:,.0f} - principal "
          f"{annuity(price_per_prop(p) * p['lvr'], p['rate'], p['term']) - price_per_prop(p) * p['lvr'] * p['rate']:,.0f}"
          f" = {contrib - annuity(price_per_prop(p) * p['lvr'], p['rate'], p['term']):,.0f} pre-tax, pre-fixed")
    p5 = dict(p, term=5)
    print(f"  ...same with 5-yr term: {contrib - annuity(price_per_prop(p) * p['lvr'], p['rate'], 5):,.0f}")

    # ---------- 5. Ramp ----------
    R = "R"  # funnel signs = replace attrition only
    plans = {
        "A funnel only, grow to ~2,500 then hold": [(60, 0), (200, 0), (300, 0), (400, 0), (450, 0), (500, 0),
                                                     (550, 0), (R, 0), (R, 0), (R, 0)],
        "B roll-led (debt) to ~1,100 then hold": [(30, 250), (60, 250), (80, 300), (80, 300), (R, 0)],
        "C brief mix to ~1,300 then hold": [(60, 150), (150, 200), (200, 250), (220, 200), (R, 0)],
        "D brief mix to ~2,500 (what $500k needs)": [(60, 200), (200, 300), (300, 400), (350, 400), (400, 300),
                                                      (R, 0)],
    }
    for name, plan in plans.items():
        rows = ramp(p, plan)
        print(f"\n=== 5. Ramp {name} (3x; founder paid $0; cash = after tax, principal, roll equity) ===")
        print(f"{'yr':>3}{'props':>7}{'rev':>11}{'EBITDA':>11}{'interest':>10}{'princ':>10}{'funnelCAC':>11}{'rollEq':>10}{'cash':>11}{'debt':>11}")
        cum = 0.0
        trough = 0.0
        for r_ in rows:
            cum += r_["cash"]
            trough = min(trough, cum)
            r_["cum"] = cum
            print(f"{r_['yr']:>3}{r_['props']:>7,.0f}{fmt(r_['rev'], 11)}{fmt(r_['ebitda'], 11)}{fmt(r_['interest'])}"
                  f"{fmt(r_['principal'])}{fmt(r_['funnel'], 11)}{fmt(r_['roll_equity'])}{fmt(r_['cash'], 11)}{fmt(r_['debt'], 11)}")
        first_pos = next((r_["yr"] for r_ in rows if r_["cash"] > 0), None)
        print(f"  Peak founder cash in (trough of cumulative cash): {-trough:,.0f}; cumulative cash yr10: {cum:,.0f};"
              f" first cash-positive year (founder still unpaid): {first_pos}")
        print(f"  Plus forgone salary ~$500k/yr x years until FSC>=500k (see table 3) = the real cost of the ramp.")

    # ---------- 6. Tornado ----------
    print("\n=== 6. Tornado: FSC at 1,000 props, 50% of book roll-bought, peak debt year (base 3x) ===")
    base_fsc = steady_state(1000, p, roll_share=0.5, debt_phase="peak")["fsc"]
    print(f"  Base FSC = {base_fsc:,.0f}")
    ranges = {
        "props_per_pm (260 / 520)": ("props_per_pm", 260, 520),
        "fee_incl_gst (4.4% / 5.5%)": ("fee_incl_gst", 0.044, 0.055),
        "rent_pw (560 / 680)": ("rent_pw", 560, 680),
        "attrition (18% / 8%)": ("attrition", 0.18, 0.08),
        "funnel_cac (5000 / 1500)": ("funnel_cac", 5000, 1500),
        "fixed (750k / 400k)": ("fixed", 750_000, 400_000),
        "field (450 / 250)": ("field", 450, 250),
        "software_ai (300 / 80)": ("software_ai", 300, 80),
        "rate (10% / 7%)": ("rate", 0.10, 0.07),
        "term (5 / 10 yrs)": ("term", 5, 10),
        "roll_multiple (3.8 / 2.8)": ("roll_multiple", 3.8, 2.8),
        "turnover/letting (20% / 40%)": ("turnover", 0.20, 0.40),
        "referral_capture (20% / 60%)": ("referral_capture", 0.20, 0.60),
        "pm_loaded (150k / 120k)": ("pm_loaded", 150_000, 120_000),
    }
    res = []
    for label, (k, lo, hi) in ranges.items():
        a = steady_state(1000, dict(p, **{k: lo}), roll_share=0.5, debt_phase="peak")["fsc"]
        b = steady_state(1000, dict(p, **{k: hi}), roll_share=0.5, debt_phase="peak")["fsc"]
        res.append((abs(b - a), label, a, b))
    for sw, label, a, b in sorted(res, reverse=True):
        print(f"  {label:<32} bad {a:>10,.0f}  good {b:>10,.0f}  swing {sw:>9,.0f}")

    print("\n=== 6b. Tornado: FSC at 2,500 props, debt repaid, funnel replacement (base 3x ~ the $500k point) ===")
    base2 = steady_state(2500, p, debt_phase="none")["fsc"]
    print(f"  Base FSC = {base2:,.0f}")
    res = []
    for label, (k, lo, hi) in ranges.items():
        if k in ("rate", "term", "roll_multiple"):
            continue
        a = steady_state(2500, dict(p, **{k: lo}), debt_phase="none")["fsc"]
        b = steady_state(2500, dict(p, **{k: hi}), debt_phase="none")["fsc"]
        res.append((abs(b - a), label, a, b))
    for sw, label, a, b in sorted(res, reverse=True):
        print(f"  {label:<32} bad {a:>10,.0f}  good {b:>10,.0f}  swing {sw:>9,.0f}")

    # ---------- 7. Worst plausible and best plausible ----------
    worst = dict(p, props_per_pm=260, fee_incl_gst=0.046, attrition=0.18, funnel_cac=4500, rate=0.10,
                 transition_loss=0.25, roll_multiple=3.5, fixed=650_000, field=420, software_ai=220, term=5,
                 referral_capture=0.2, rent_pw=590)
    best = dict(p, props_per_pm=520, fee_incl_gst=0.052, attrition=0.09, funnel_cac=1800, rate=0.075,
                transition_loss=0.08, roll_multiple=3.0, fixed=450_000, field=300, software_ai=120, term=10,
                referral_capture=0.5, rent_pw=650)
    print("\n=== 7. Worst / base / best plausible ===")
    for label, q in [("worst", worst), ("base", p), ("best", best)]:
        print_unit(q, label)
        for n in (1000, 1500, 2500):
            s = steady_state(n, q, roll_share=0.5, debt_phase="peak")
            s2 = steady_state(n, q, debt_phase="none")
            print(f"   n={n:>5}: EBITDA {s['ebitda']:>10,.0f} ({s['margin']:.0%}) | FSC 50%-roll peak-debt {s['fsc']:>10,.0f} "
                  f"| FSC debt-free {s2['fsc']:>10,.0f}")
        print(f"   props for FSC=500k (debt-free, funnel replacement): {breakeven(q, 500_000, debt_phase='none')}")

    # ---------- 8. Cash-on-cash ----------
    print("\n=== 8. Cash-on-cash: buy 1,000-property book outright at base terms, run at 3x ===")
    price = 1000 * price_per_prop(p) * (1 + p["deal_costs"])
    debt = 1000 * price_per_prop(p) * p["lvr"]
    equity = price - debt + 150_000  # + working capital
    for ppm in (130, 260, 390, 520):
        q = dict(p, props_per_pm=ppm)
        unrec = max(0.0, q["transition_loss"] - q["retention_cover"])
        n_kept = 1000 * (1 - unrec)
        s = steady_state(n_kept, q, debt_phase="peak")
        ebitda = s["ebitda"]
        pay = annuity(debt, q["rate"], q["term"])
        intr = debt * q["rate"]
        pretax = ebitda - intr - n_kept * q["attrition"] * q["funnel_cac"]
        cash = pretax - max(0, pretax) * q["tax"] - (pay - intr)
        print(f"  {ppm:>3} props/PM: equity {equity:,.0f}; yr-1 after-tax free cash to equity {cash:>10,.0f} "
              f"-> cash-on-cash {cash / equity:>6.1%} (founder salary $0)")


if __name__ == "__main__":
    main()
