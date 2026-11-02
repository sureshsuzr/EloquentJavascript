#!/usr/bin/env python3
"""
Round-2 LTV & platform-economics model: managed property as distribution channel.
Red-team CFO (LTV modeller), 2 Nov 2026. Stdlib only. Run: python3 ltv_model.py

AUD, ex-GST, nominal. Builds on round-1 red-team/models/unit_economics.py (imported for
the management P&L, fixed-cost curve and founder-salary-capacity (FSC) definition).

Unit of analysis = one managed property (one landlord relationship + its sitting tenant).
Every service is: event/attach rate x conversion x net cash per conversion, with an
explicit start lag (trust takes time), and runs only while the management survives
(annual churn c). Broker trail, once written, survives management churn (it rides the
loan, not the management). Everything discounted at d.

Labels: [V] verified (see report), [E] estimate, [U] unknown -> ranges + break-even attach.
"""
import copy, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "models"))
import unit_economics as r1   # round-1 model

R1 = copy.deepcopy(r1.BASE)
R1["referral_capture"] = 0.0          # sale capture modelled separately here, net of s 48A
MGMT_REV = r1.rev_per_prop(R1)["total"]           # ~1,782 (mgmt+letting+ancillary)
MGMT_VAR = r1.var_cost_per_prop(R1)["total"]      # ~1,017 at 3x
MGMT_CONTRIB = MGMT_REV - MGMT_VAR                # ~765

A = dict(
    disc=0.12,            # [E] small-business cost of equity
    churn=0.12,           # [E] round-1: 10-14% gross management loss/yr
    horizon=30,
    # --- tenant evaluation (priced to landlord at each letting) ---
    te_turnover=0.30,     # [E] round-1 re-let rate
    te_attach=0.50,       # [U] share of lettings where landlord buys the add-on
    te_price=120.0,       # [E] ex GST per letting, on top of the letting fee
    te_cost=60.0,         # [E] database/ID/income checks + review time per letting
    te_rent_uplift=0.005, # [E] better rent-setting at re-let (fixed-price advertising caps this)
    # --- maintenance subscription (flat fee absorbs repair variance) ---
    mx_expected=1800.0,   # [E] expected annual reactive repair spend per rental (BIS 2017 $1.7-2.7k; ATO aggregate implies ~$1-1.5k)
    mx_attach=0.15,       # [U]
    mx_loading=0.20,      # [E] fee = expected x (1+loading)
    mx_adverse=0.10,      # [E] subscribers cost more than the priced average (old stock self-selects)
    mx_saving=0.08,       # [E] preventive + dense network delivery saving on cost
    mx_admin=100.0,       # [E] per subscriber per year (coordination, claims, reserve capital cost)
    mx_churn_cut=0.02,    # [E] subscribers churn 2 pts less (12-month contract, sticky)
    mx_fixed=150_000.0,   # [E] trades/maintenance manager + actuarial/legal (+ insurer partner costs)
    mx_lag=1,
    # --- landlord broking (refinance + next purchase), via credit rep under an aggregator ---
    br_has_loan=0.65,     # [E] share of landlords with an investment loan
    br_balance=420_000.0, # [E] average outstanding investor balance (new investor loans ~$686k nat. Sep-25 [V])
    br_refi_rate=0.10,    # [E] ~619k refinances/yr on ~6m loans [V flow, E rate]
    br_refi_capture=0.15, # [U] share of landlord refis written in-house
    br_buy_rate=0.04,     # [E] share of landlords buying another property per year
    br_buy_loan=600_000.0,
    br_buy_capture=0.20,  # [U]
    br_upfront=0.0060,    # [V] 0.55-0.65% upfront
    br_trail=0.0015,      # [V] 0.15-0.20% trail
    br_split=0.90,        # [E] broker share after aggregator
    br_clawback=0.05,     # [E] expected upfront lost to clawback
    br_loan_exit=0.20,    # [E] hazard trail stops (refi elsewhere, sale, amortisation)
    br_cost=1300.0,       # [E] broker time + compliance (BID file) per settled loan
    br_fixed=50_000.0,    # [E] aggregator, PI, CRM, compliance, part of a credit-rep's base
    br_lag=1,
    # --- next-purchase -> new management sourced from own landlords ---
    nm_buy_rate=0.04,     # same event as br_buy_rate
    nm_in_area=0.40,      # [E] share of next purchases in Melbourne/serviceable (land tax pushes interstate)
    nm_capture=0.50,      # [U] share of those whose management we win
    nm_value=3000.0,      # [E] avoided funnel CAC per management (round-1 base $3k; roll $5.3k)
    nm_lag=1,
    # --- sale capture, net of s 48A (Estate Agents Act) ---
    sc_sale_rate=0.06,    # [E] round-1
    sc_capture=0.20,      # [E] round-1 range 10-35%
    sc_fee=2500.0,        # [E] referral from selling agent
    sc_p48a=0.60,         # [E] probability the referral must be rebated to landlord (=> $0)
    sc_inv_buyer=0.30,    # [E] share of buyers who are investors
    sc_keep_cap=0.40,     # [E] buyer keeps us when we ran the sale process
    sc_keep_uncap=0.08,   # [E] ... when we did not
    # --- tenant: move within portfolio ---
    tm_move=0.30,         # tenancies ending/yr
    tm_local=0.50,        # [E] movers staying in the area
    tm_match=0.08,        # [U] matched to a managed vacancy (portfolio ~4% of corridor stock)
    tm_value=150.0,       # [E] agency saving per in-portfolio placement (no renter fees allowed)
    # --- tenant: first-home finance ---
    tf_rate=0.04,         # [E] renter households buying a first home per year (HILDA 18-24s 7.6% [V, dated])
    tf_capture=0.04,      # [U]
    tf_loan=550_000.0,
    # --- tenant subscription (equity / rent-history / deposit pathway) ---
    ts_attach=0.02,       # [U]
    ts_net=60.0,          # [E] $8/month less costs
    ts_fixed=30_000.0,
    te_fixed=20_000.0,    # model/data upkeep for priced screening
)

SERVICES = ["te", "mx", "br", "nm", "sc", "tm", "tf", "ts"]
NAMES = dict(te="Tenant evaluation (priced)", mx="Maintenance subscription", br="Landlord broking",
             nm="New mgmts from landlord #2", sc="Sale capture net s48A", tm="Tenant move in portfolio",
             tf="Tenant first-home finance", ts="Tenant subscription")
ATTACH_KEY = dict(te="te_attach", mx="mx_attach", br="br_refi_capture", nm="nm_capture", sc="sc_capture",
                  tm="tm_match", tf="tf_capture", ts="ts_attach")


def loan_npv(p, loan):
    up = loan * p["br_upfront"] * p["br_split"] * (1 - p["br_clawback"])
    trail = loan * p["br_trail"] * p["br_split"]
    pv_trail = trail / (p["disc"] + p["br_loan_exit"])
    return up + pv_trail - p["br_cost"]


def service_annual(p, on):
    """Expected net cash per surviving managed property per year (after lag), and churn delta."""
    v = {}
    dc = 0.0
    if "te" in on:
        v["te"] = p["te_turnover"] * p["te_attach"] * (p["te_price"] - p["te_cost"]) \
                  + p["te_rent_uplift"] * r1.rev_per_prop(R1)["mgmt"]
    if "mx" in on:
        fee = p["mx_expected"] * (1 + p["mx_loading"])
        cost = p["mx_expected"] * (1 + p["mx_adverse"]) * (1 - p["mx_saving"])
        v["mx"] = p["mx_attach"] * (fee - cost - p["mx_admin"])
        dc -= p["mx_attach"] * p["mx_churn_cut"]
    if "br" in on:
        n = loan_npv(p, p["br_balance"])
        m = loan_npv(p, p["br_buy_loan"])
        v["br"] = p["br_has_loan"] * p["br_refi_rate"] * p["br_refi_capture"] * n \
                  + p["br_buy_rate"] * p["br_buy_capture"] * m
    if "nm" in on:
        v["nm"] = p["nm_buy_rate"] * p["nm_in_area"] * p["nm_capture"] * p["nm_value"]
    if "sc" in on:
        v["sc"] = p["sc_sale_rate"] * p["sc_capture"] * p["sc_fee"] * (1 - p["sc_p48a"])
        keep = p["sc_capture"] * p["sc_keep_cap"] + (1 - p["sc_capture"]) * p["sc_keep_uncap"]
        dc -= p["sc_sale_rate"] * p["sc_inv_buyer"] * keep
    if "tm" in on:
        v["tm"] = p["tm_move"] * p["tm_local"] * p["tm_match"] * p["tm_value"]
    if "tf" in on:
        v["tf"] = p["tf_rate"] * p["tf_capture"] * loan_npv(p, p["tf_loan"])
    if "ts" in on:
        v["ts"] = p["ts_attach"] * p["ts_net"]
    return v, dc


def fixed_extra(p, on):
    return sum(p[k + "_fixed"] for k in on if k + "_fixed" in p)


def ltv(p, on=(), contrib=MGMT_CONTRIB):
    """Discounted LTV per managed property (before fixed costs and acquisition cost).
    Year 0 = first year under management; services start after their lag."""
    v, dc = service_annual(p, on)
    c = max(0.01, p["churn"] + dc)
    tot = 0.0
    parts = {k: 0.0 for k in v}
    parts["mgmt"] = 0.0
    for t in range(p["horizon"]):
        s = (1 - c) ** t / (1 + p["disc"]) ** t
        parts["mgmt"] += contrib * s
        for k, x in v.items():
            if t >= p.get(k + "_lag", 1):
                parts[k] += x * s
    tot = sum(parts.values())
    return tot, parts, c


def fsc(n, p, on=(), base=R1):
    """Founder salary capacity, debt-free, churn refilled via funnel (round-1 definition).
    Services: steady-state annual value per property; internally sourced managements
    are already valued as avoided CAC in 'nm'."""
    v, dc = service_annual(p, on)
    attr = max(0.0, p["churn"] + dc)
    ebitda = n * (MGMT_CONTRIB + sum(v.values())) - r1.fixed_at(n, base) - fixed_extra(p, on)
    return ebitda - n * attr * base["funnel_cac"]


def scale_for(p, on=(), target=500_000, base=R1):
    for n in range(100, 20001, 10):
        if fsc(n, p, on, base) >= target:
            return n
    return None


def main():
    p = copy.deepcopy(A)
    print("AUD ex-GST. Management contribution/property (round-1 3x, referral removed): "
          f"rev {MGMT_REV:,.0f} - var {MGMT_VAR:,.0f} = {MGMT_CONTRIB:,.0f}")
    print(f"Per-loan broker NPV: refi ${p['br_balance']:,.0f} -> {loan_npv(p, p['br_balance']):,.0f}; "
          f"purchase ${p['br_buy_loan']:,.0f} -> {loan_npv(p, p['br_buy_loan']):,.0f}; "
          f"FHB ${p['tf_loan']:,.0f} -> {loan_npv(p, p['tf_loan']):,.0f}")

    print("\n=== 1. Steady-state net value per managed property per year, by service (base) ===")
    v, dc = service_annual(p, SERVICES)
    for k in SERVICES:
        _, d1 = service_annual(p, [k])
        print(f"  {NAMES[k]:<30} {v[k]:>7,.0f}/yr   churn delta {d1 * 100:+.2f} pts   fixed {p.get(k + '_fixed', 0):>8,.0f}")
    print(f"  {'TOTAL services':<30} {sum(v.values()):>7,.0f}/yr   vs management contribution {MGMT_CONTRIB:,.0f}")

    print("\n=== 2. LTV per managed property (discounted, before fixed + acquisition) ===")
    rank = sorted(SERVICES, key=lambda k: -(ltv(p, [k])[0] - ltv(p)[0]))
    combos = [("0 services (mgmt only)", []), (f"1: +{NAMES[rank[0]]}", rank[:1]),
              (f"2: +{NAMES[rank[1]]}", rank[:2]), ("landlord-side all", ["te", "mx", "br", "nm", "sc"]),
              ("all services", SERVICES)]
    base_ltv = ltv(p)[0]
    for label, on in combos:
        t, parts, c = ltv(p, on)
        print(f"  {label:<40} LTV {t:>7,.0f}  (+{t - base_ltv:>5,.0f}, {t / base_ltv - 1:+.0%})  churn {c:.1%}")
    print("  Marginal LTV by service (alone):")
    for k in rank:
        print(f"    {NAMES[k]:<30} +{ltv(p, [k])[0] - base_ltv:>6,.0f}")

    print("\n=== 3. Scale needed for $500k FSC (debt-free, funnel refill at $3k) ===")
    for fx in (575_000, 400_000):
        b = dict(R1, fixed=fx)
        print(f"  round-1 fixed {fx:,}:")
        for label, on in combos + [("broking + new-mgmt only", ["br", "nm"]),
                                   ("broking + new-mgmt + sale", ["br", "nm", "sc"])]:
            n = scale_for(p, on, base=b)
            print(f"    {label:<40} {n if n else '>20k':>6}")

    print("\n=== 4. Low / base / high attach (all other inputs base) ===")
    rng = dict(te=(0.2, 0.5, 0.8), mx=(0.05, 0.15, 0.30), br=(0.05, 0.15, 0.30), nm=(0.25, 0.50, 0.70),
               sc=(0.10, 0.20, 0.35), tm=(0.03, 0.08, 0.15), tf=(0.01, 0.04, 0.10), ts=(0.005, 0.02, 0.05))
    for k in SERVICES:
        out = []
        for a in rng[k]:
            q = dict(p, **{ATTACH_KEY[k]: a})
            if k == "br":
                q["br_buy_capture"] = a * 4 / 3
            out.append(service_annual(q, [k])[0][k])
        print(f"  {NAMES[k]:<30} attach {rng[k]} -> $/prop/yr {out[0]:>6,.0f} {out[1]:>6,.0f} {out[2]:>6,.0f}")

    print("\n=== 5. Break-even attach: service covers its own fixed cost (at N properties) ===")
    for N in (400, 1000, 2000):
        line = []
        for k in ["te", "mx", "br", "ts"]:
            fx = p[k + "_fixed"]
            be = None
            for i in range(1, 1001):
                a = i / 1000
                q = dict(p, **{ATTACH_KEY[k]: a})
                if k == "br":
                    q["br_buy_capture"] = a * 4 / 3
                if N * service_annual(q, [k])[0][k] >= fx:
                    be = a
                    break
            line.append(f"{k} {be:.1%}" if be else f"{k} n/a")
        print(f"  N={N:>5}: " + " | ".join(line))
    q = dict(p, mx_adverse=0.25, mx_saving=0.0)
    print(f"  Maintenance margin per subscriber: base {service_annual(dict(p, mx_attach=1), ['mx'])[0]['mx']:,.0f}; "
          f"if adverse selection 25% & no saving {service_annual(dict(q, mx_attach=1), ['mx'])[0]['mx']:,.0f}")
    for load in (0.10, 0.20, 0.30):
        for adv in (0.0, 0.10, 0.20, 0.30):
            m = service_annual(dict(p, mx_attach=1, mx_loading=load, mx_adverse=adv), ["mx"])[0]["mx"]
            print(f"    loading {load:.0%} adverse {adv:.0%}: margin/subscriber {m:>6,.0f}")

    print("\n=== 6. Tornado: LTV (all landlord-side services) to each input, low/high ===")
    on = ["te", "mx", "br", "nm", "sc"]
    b0 = ltv(p, on)[0]
    print(f"  Base LTV {b0:,.0f}")
    tor = {
        "churn (14% / 10%)": [("churn", 0.14, 0.10)],
        "disc (15% / 9%)": [("disc", 0.15, 0.09)],
        "br capture refi/buy (5/7% / 30/40%)": [("br_refi_capture", 0.05, 0.30), ("br_buy_capture", 0.07, 0.40)],
        "br refi rate (6% / 14%)": [("br_refi_rate", 0.06, 0.14)],
        "br balance (300k / 550k)": [("br_balance", 300_000, 550_000)],
        "br trail exit (30% / 12%)": [("br_loan_exit", 0.30, 0.12)],
        "mx attach (5% / 30%)": [("mx_attach", 0.05, 0.30)],
        "mx adverse sel (30% / 0%)": [("mx_adverse", 0.30, 0.0)],
        "nm capture (25% / 70%)": [("nm_capture", 0.25, 0.70)],
        "nm in-area (20% / 60%)": [("nm_in_area", 0.20, 0.60)],
        "landlord buy rate (2% / 6%)": [("br_buy_rate", 0.02, 0.06), ("nm_buy_rate", 0.02, 0.06)],
        "sc capture (10% / 35%)": [("sc_capture", 0.10, 0.35)],
        "s48A prob (100% / 0%)": [("sc_p48a", 1.0, 0.0)],
        "te attach (20% / 80%)": [("te_attach", 0.2, 0.8)],
        "mgmt contribution (565 / 965)": None,
    }
    res = []
    for label, chg in tor.items():
        if chg is None:
            lo = ltv(p, on, contrib=MGMT_CONTRIB - 200)[0]
            hi = ltv(p, on, contrib=MGMT_CONTRIB + 200)[0]
        else:
            lo = ltv(dict(p, **{k: a for k, a, _ in chg}), on)[0]
            hi = ltv(dict(p, **{k: b for k, _, b in chg}), on)[0]
        res.append((abs(hi - lo), label, lo, hi))
    for sw, label, lo, hi in sorted(res, reverse=True):
        print(f"  {label:<38} {lo:>7,.0f} {hi:>7,.0f}  swing {sw:>6,.0f}")

    print("\n=== 7. Payback on a bought management (round-1 cost per retained $5,279; funnel $3k) ===")
    cost_roll = r1.eff_cost_per_retained_roll_prop(r1.BASE)
    for label, on_ in [("mgmt only", []), ("+ broking", ["br"]), ("+ broking + new mgmt", ["br", "nm"]),
                       ("landlord-side all", ["te", "mx", "br", "nm", "sc"])]:
        v, dc = service_annual(p, on_)
        c = p["churn"] + dc
        for cl, cost in [("roll", cost_roll), ("funnel", 3000)]:
            cum, yr, cumd = 0.0, None, 0.0
            for t in range(40):
                s = (1 - c) ** t
                cf = MGMT_CONTRIB + sum(x for k, x in v.items() if t >= p.get(k + "_lag", 1))
                cumd += cf * s / (1 + p["disc"]) ** t
                if cumd >= cost and yr is None:
                    yr = t + 1
            simple = cost / (MGMT_CONTRIB + sum(v.values()))
            tot = ltv(p, on_)[0]
            print(f"  {label:<24}{cl:<7} simple {simple:>4.1f} yrs | discounted, churn-adj {str(yr) if yr else 'never':>5} yrs"
                  f" | LTV/cost {tot / cost:>4.2f}")
    print("  NB contribution here is BEFORE fixed costs (~$575/prop at 1,000). After fixed, mgmt-only roll never pays back.")

    print("\n=== 8. What attach would make services halve the $500k scale? (fixed 575k) ===")
    n0 = scale_for(p, [])
    for mult in (1, 2, 3, 4):
        q = dict(p, br_refi_capture=min(1, 0.15 * mult), br_buy_capture=min(1, 0.20 * mult),
                 mx_attach=min(1, 0.15 * mult), nm_capture=min(1, 0.5 * mult), sc_capture=min(1, 0.2 * mult))
        n = scale_for(q, ["te", "mx", "br", "nm", "sc"])
        print(f"  attach x{mult}: properties for $500k {n} (mgmt-only {n0})")

    print("\n=== 9. Per-TENANT relationship LTV (one tenancy, avg length 1/turnover yrs) ===")
    for label, q in [("base", p), ("upside", dict(p, tf_rate=0.06, tf_capture=0.10, tm_match=0.15, ts_attach=0.05))]:
        yrs = 1 / q["tm_move"]
        per_yr = q["tf_rate"] * q["tf_capture"] * loan_npv(q, q["tf_loan"]) + q["ts_attach"] * q["ts_net"]
        pv = sum(per_yr / (1 + q["disc"]) ** t for t in range(int(round(yrs))))
        move = q["tm_local"] * q["tm_match"] * q["tm_value"] / (1 + q["disc"]) ** yrs
        print(f"  {label:<7} tenancy {yrs:.1f} yrs: finance+subscription PV {pv:,.0f} + in-portfolio move {move:,.0f}"
              f" = {pv + move:,.0f} per tenant relationship")
    print("  vs landlord relationship (mgmt only) LTV", f"{ltv(p)[0]:,.0f}")
    print("\n=== 10. Round-1 reconciliation ===")
    print(f"  Round-1 $500k scale 2,510 included referral $75/prop/yr (50% capture, no s48A haircut).")
    print(f"  Same model, referral at $0: {scale_for(p, [])} properties; with landlord services at base attach: "
          f"{scale_for(p, ['te','mx','br','nm','sc'])}")
    mxar = dict(p, mx_attach=1)
    print(f"  Maintenance via APRA insurer as authorised rep (15% commission, $60 admin, no risk): "
          f"{0.15 * p['mx_expected'] * (1 + p['mx_loading']) - 60:,.0f}/subscriber vs risk-bearing base "
          f"{service_annual(mxar, ['mx'])[0]['mx']:,.0f} (before s48A on commissions)")


if __name__ == "__main__":
    main()
