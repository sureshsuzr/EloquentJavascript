"""
Grocery aggregation marketplace: per-order and per-city unit economics (AUD).
Red-team model, 2 Nov 2026. Run: python3 order_economics.py

Every input is an ESTIMATE unless tagged [verified] in the report.
Key verified anchors:
  - Stripe AU domestic cards 1.65% + $0.30 from 1 Oct 2026 (Stripe support/Wise)
  - FWC Interim On-Demand Delivery MSO from 17 Aug 2026: ~$31.30-32.50/hr ENGAGED time,
    covers platforms delivering food/drinks/liquor/groceries "as soon as possible"
  - Instacart FY25: GTV US$37.22B, 338.8M orders (AOV ~US$110), transaction rev ~7.3% GTV,
    ads ~2.9% GTV, adj. EBITDA 2.9% of GTV
  - DoorDash Q3 25 contribution profit 5.1% of GOV, net revenue margin ~13.5-13.8%
  - Milkrun lost ~$10-13/order (2022-23), shut Apr 2023 after ~$86M raised
"""
from dataclasses import dataclass, replace
import math

@dataclass
class P:
    n_merchants: int = 1
    basket: float = 0.0          # set from basket_by_n if 0
    take_rate: float = 0.15
    delivery_fee: float = 7.99   # customer delivery fee
    service_fee_pct: float = 0.04
    service_fee_cap: float = 6.0
    small_order_fee: float = 0.0
    # picking: 'merchant' (merchant staff pick, merchant bears cost) or 'platform'
    picker: str = "merchant"
    item_value: float = 6.5      # avg $ per item -> items per basket
    pick_items_per_hr: float = 60.0
    picker_cost_hr: float = 42.0 # casual retail award + super + on-costs
    pick_overhead_min: float = 4.0  # per stop: find order, bag, label, handover
    # courier (own platform, paid on engaged time under FWC MSO)
    courier_hr: float = 32.0 * 1.12   # MSO car rate + insurance/admin load
    first_leg_min: float = 9.0   # accept -> first pickup travel (density-dependent; overridden)
    wait_at_merchant_min: float = 4.0
    inter_stop_min: float = 8.0  # merchant -> merchant (2-3 km urban + park)
    last_leg_min: float = 12.0   # last merchant -> customer
    handover_min: float = 3.0
    courier_mode: str = "own"    # 'own' or 'direct' (Uber Direct/DoorDash Drive)
    direct_fee_per_drop: float = 11.0  # per point-to-point job; multi-pickup = N jobs
    # leakage
    oos_item_rate: float = 0.08  # items unavailable (shelf-scan inventory)
    oos_refund_cost_pct: float = 0.012  # credits/goodwill + lost take on refunded items, % basket
    error_rate_per_stop: float = 0.03   # missing/wrong item complaint per merchant stop
    error_cost: float = 12.0
    support_per_order: float = 1.6
    payment_pct: float = 0.0165
    payment_fixed: float = 0.30
    packaging: float = 0.60
    tech_per_order: float = 0.40 # cloud, maps, SMS, scan-vision amortised
    insurance_per_order: float = 0.25
    promo_per_order: float = 2.0 # steady-state discounts/credits averaged over all orders
    batch_share: float = 0.0     # share of orders sharing a courier run with another order
    batch_saving: float = 0.35   # courier minutes saved on a batched order

basket_by_n = {1: 55.0, 2: 85.0, 3: 110.0}

def order_pnl(p: P):
    b = p.basket or basket_by_n[p.n_merchants]
    items = b / p.item_value
    fulfilled = b * (1 - p.oos_item_rate)  # take & service fee only on what ships
    take = p.take_rate * fulfilled
    service = min(p.service_fee_pct * fulfilled, p.service_fee_cap)
    rev = take + service + p.delivery_fee + p.small_order_fee
    # picking
    pick_min = items / p.pick_items_per_hr * 60 + p.pick_overhead_min * p.n_merchants
    pick_cost = pick_min / 60 * p.picker_cost_hr if p.picker == "platform" else 0.0
    merchant_pick_cost = pick_min / 60 * p.picker_cost_hr if p.picker == "merchant" else 0.0
    # courier
    if p.courier_mode == "own":
        mins = (p.first_leg_min + p.n_merchants * p.wait_at_merchant_min
                + (p.n_merchants - 1) * p.inter_stop_min + p.last_leg_min + p.handover_min)
        mins = mins * (1 - p.batch_share * p.batch_saving)
        courier = mins / 60 * p.courier_hr
    else:
        mins = float("nan")
        courier = p.direct_fee_per_drop * p.n_merchants  # point-to-point jobs, no multi-pickup
    pay = p.payment_pct * (fulfilled + service + p.delivery_fee) + p.payment_fixed
    oos = p.oos_refund_cost_pct * b
    errors = p.error_rate_per_stop * p.n_merchants * p.error_cost
    var = (pick_cost + courier + pay + oos + errors + p.support_per_order + p.packaging
           + p.tech_per_order + p.insurance_per_order + p.promo_per_order)
    return dict(basket=b, items=items, revenue=rev, take=take, pick=pick_cost,
                merchant_pick=merchant_pick_cost, courier=courier, courier_min=mins,
                payments=pay, oos=oos, errors=errors, contribution=rev - var,
                contrib_pct_gmv=(rev - var) / b)

def merchant_view(p: P, gm=0.28):
    """Merchant's incremental margin on a platform order (before any halo)."""
    r = order_pnl(p)
    per_merchant_sales = r["basket"] * (1 - p.oos_item_rate) / p.n_merchants
    gross = per_merchant_sales * gm
    fee = per_merchant_sales * p.take_rate
    pick = r["merchant_pick"] / p.n_merchants
    card = 0.0
    return per_merchant_sales, gross - fee - pick

def fmt(d):
    return " ".join(f"{k}={v:7.2f}" for k, v in d.items() if isinstance(v, float) and not math.isnan(v))

def line(): print("-" * 100)

if __name__ == "__main__":
    print("1. CONTRIBUTION PER ORDER by merchants/basket x take rate (merchant picks, own MSO couriers)")
    line()
    print(f"{'n':>2} {'basket':>7} " + " ".join(f"{'take '+str(int(t*100))+'%':>10}" for t in (0.05, .10, .15, .20)) + "   courier$  courier-min")
    for n in (1, 2, 3):
        row = []
        for t in (0.05, .10, .15, .20):
            r = order_pnl(P(n_merchants=n, take_rate=t))
            row.append(r["contribution"])
        r15 = order_pnl(P(n_merchants=n))
        print(f"{n:>2} {r15['basket']:7.0f} " + " ".join(f"{c:10.2f}" for c in row) + f"   {r15['courier']:8.2f}  {r15['courier_min']:6.0f}")
    line()
    print("Detail at 15% take, merchant picks:")
    for n in (1, 2, 3):
        print(f" n={n}: " + fmt(order_pnl(P(n_merchants=n))))
    line()
    print("2. SAME, PLATFORM PICKS (Instacart model) at 15% take")
    for n in (1, 2, 3):
        r = order_pnl(P(n_merchants=n, picker="platform"))
        print(f" n={n}: contribution={r['contribution']:7.2f}  pick={r['pick']:6.2f}  courier={r['courier']:6.2f}")
    line()
    print("3. SAME, UBER DIRECT / DOORDASH DRIVE (point-to-point, ~$11/job est.), merchant picks, 15% take")
    for n in (1, 2, 3):
        r = order_pnl(P(n_merchants=n, courier_mode="direct"))
        print(f" n={n}: contribution={r['contribution']:7.2f}  courier={r['courier']:6.2f}  (customer gets {n} drops)")
    line()
    print("4. MARGINAL COST OF EACH EXTRA PICKUP STOP (own courier, merchant picks)")
    base = order_pnl(P(n_merchants=1, basket=85))
    for n in (2, 3, 4):
        r = order_pnl(P(n_merchants=n, basket=85))
        print(f" same $85 basket split over {n} merchants: extra cost vs 1 stop = {base['contribution']-r['contribution']:6.2f}")
    line()
    print("5. MERCHANT VIEW: incremental margin per platform order (gross margin 28% indep. grocer; 40% specialty)")
    for gm in (0.28, 0.40):
        for t in (0.05, .10, .15, .20):
            s, m = merchant_view(P(n_merchants=2, take_rate=t), gm)
            print(f" GM {gm:.0%} take {t:.0%}: merchant sales/order {s:6.2f}  margin after fee+pick {m:6.2f}")
    line()
    print("6. COURIER PRODUCTIVITY (orders per engaged courier-hour)")
    for n in (1, 2, 3):
        r = order_pnl(P(n_merchants=n))
        oph = 60 / r["courier_min"]
        print(f" n={n}: {r['courier_min']:.0f} engaged min/order -> {oph:.2f} orders/engaged hr; with 2-order batching ~{oph*1.6:.2f}")
    line()

    # ---- density -> first-leg time, and city P&L ----
    print("7. DENSITY: city P&L. Service area 120 km2 (inner Melbourne ring). Mix 50/35/15 of 1/2/3-merchant orders.")
    AREA = 120.0
    def blended(p_kwargs, density):
        # first-leg (accept->pickup) and idle reposition shrink with density of orders (orders/km2/day)
        # nearest-available-courier distance ~ 0.5/sqrt(active couriers per km2); active couriers ~ density*AREA/12h/1.8 oph
        active = max(density * AREA / 12 / 1.8, 0.5)
        km = 0.5 / math.sqrt(active / AREA)
        first_leg = 3 + km / 22 * 60  # 3 min accept/park + travel at 22 km/h
        batch = min(0.6, 0.12 * math.log2(1 + density))  # batching opportunities grow with density
        mix = {1: .5, 2: .35, 3: .15}
        kw = dict(first_leg_min=first_leg, batch_share=batch); kw.update(p_kwargs)
        c = sum(w * order_pnl(P(n_merchants=n, **kw))["contribution"] for n, w in mix.items())
        g = sum(w * basket_by_n[n] for n, w in mix.items())
        return c, g, first_leg
    # city fixed costs (A$/yr) at steady state for one metro zone
    city_fixed = {
        "city GM + ops lead": 320_000, "merchant success (3 FTE)": 330_000, "courier ops/dispatch (3 FTE)": 300_000,
        "support base (2 FTE)": 160_000, "brand marketing base": 600_000, "catalogue QA / scan ops (2 FTE)": 200_000,
        "insurance, legal, compliance": 150_000, "office/vehicles/misc": 90_000,
    }
    FIXED_CITY = sum(city_fixed.values())
    central = 3_500_000   # product/eng (12 FTE), founder team, finance -- shared across cities
    print(f" city fixed = ${FIXED_CITY:,.0f}/yr; central (tech+HQ) = ${central:,.0f}/yr")
    print(f" {'orders/km2/day':>15} {'orders/day':>10} {'first-leg min':>13} {'contrib/order':>13} {'city contrib/yr':>16} {'after city fixed':>16} {'after central':>14}")
    for d in (0.5, 1, 2, 4, 8, 16, 32):
        c, g, fl = blended({}, d)
        od = d * AREA
        yr = c * od * 365
        print(f" {d:15.1f} {od:10.0f} {fl:13.1f} {c:13.2f} {yr:16,.0f} {yr-FIXED_CITY:16,.0f} {yr-FIXED_CITY-central:14,.0f}")
    # solve break-even
    def solve(target):
        lo, hi = 0.05, 500
        if blended({}, hi)[0] <= 0: return None
        for _ in range(80):
            mid = (lo + hi) / 2
            c, g, fl = blended({}, mid)
            if c * mid * AREA * 365 < target: lo = mid
            else: hi = mid
        return hi
    for label, tgt in (("city fixed", FIXED_CITY), ("city + central", FIXED_CITY + central),
                       ("+ $500k founder draw + 25% buffer", (FIXED_CITY + central + 500_000) * 1.25)):
        d = solve(tgt)
        if d is None:
            print(f" break-even vs {label:<34}: NEVER (contribution/order stays negative at any density)"); continue
        c, g, fl = blended({}, d)
        print(f" break-even vs {label:<34}: {d:5.1f} orders/km2/day = {d*AREA:6,.0f} orders/day, GMV ${d*AREA*365*g/1e6:5.1f}M/yr, contrib/order ${c:.2f}")
    line()

    print("8. CUSTOMER LTV vs CAC (15% take, mix as above, dense case 8 orders/km2/day)")
    c, g, fl = blended({}, 8)
    for orders_y1, ret in ((8, .35), (14, .45), (24, .55)):
        # 3-yr LTV: y1 orders, then annual retention on orders
        ltv = c * orders_y1 * (1 + ret + ret**2)
        first_promo = 25.0  # first two-order welcome credits
        print(f" orders yr1={orders_y1:2d}, yoy retention={ret:.0%}: 3-yr contribution LTV ${ltv-first_promo:7.0f}  -> max CAC for 3x LTV/CAC ${(ltv-first_promo)/3:6.0f}")
    line()

    print("9. SENSITIVITY (tornado) on blended contribution/order at 8 orders/km2/day, base 15% take, merchant picks")
    base_c, _, _ = blended({}, 8)
    tests = [
        ("take rate 10% / 20%", {"take_rate": .10}, {"take_rate": .20}),
        ("delivery fee $4.99 / $10.99", {"delivery_fee": 4.99}, {"delivery_fee": 10.99}),
        ("wait at merchant 8 / 2 min", {"wait_at_merchant_min": 8}, {"wait_at_merchant_min": 2}),
        ("inter-stop 12 / 5 min", {"inter_stop_min": 12}, {"inter_stop_min": 5}),
        ("courier $/hr 40 / 30", {"courier_hr": 40.0}, {"courier_hr": 30.0}),
        ("OOS 15% / 4%", {"oos_item_rate": .15, "oos_refund_cost_pct": .025}, {"oos_item_rate": .04, "oos_refund_cost_pct": .006}),
        ("promo $4 / $0.5", {"promo_per_order": 4.0}, {"promo_per_order": 0.5}),
        ("platform picks / merchant picks", {"picker": "platform"}, {}),
    ]
    rows = []
    for name, lo, hi in tests:
        cl, _, _ = blended(lo, 8); ch, _, _ = blended(hi, 8)
        rows.append((abs(ch - cl), name, cl, ch))
    # basket size sensitivity separately (global dict)
    saved = dict(basket_by_n)
    for k in basket_by_n: basket_by_n[k] = saved[k] * 0.75
    cl, _, _ = blended({}, 8)
    for k in basket_by_n: basket_by_n[k] = saved[k] * 1.4
    ch, _, _ = blended({}, 8)
    basket_by_n.update(saved)
    rows.append((abs(ch - cl), "basket -25% / +40%", cl, ch))
    print(f" base = ${base_c:.2f}")
    for sw, name, cl, ch in sorted(rows, reverse=True):
        print(f" {name:<34} low ${cl:6.2f}  high ${ch:6.2f}  swing ${sw:5.2f}")
    line()

    print("10. BENCHMARKS (per order, A$; FX 1 USD = 1.52 AUD est.)")
    fx = 1.52
    aov = 37.22e9 / 338.8e6
    print(f" Instacart FY25: AOV US${aov:.0f} = A${aov*fx:.0f}; revenue ~10.2% GTV = A${aov*fx*.102:.2f}/order; adj EBITDA 2.9% GTV = A${aov*fx*.029:.2f}/order (ads are ~28% of revenue)")
    print(f" DoorDash Q3 25: contribution 5.1% of GOV; on a A$55 grocery basket = A${55*.051:.2f}/order")
    print(" Milkrun 2022-23: about -A$10 to -A$13 per order (founder vs leaked deck); closed Apr 2023")
    m, _, _ = blended({}, 8)
    print(f" This model, dense case: A${m:.2f}/order before city fixed costs")
    line()

    print("10b. SURVIVAL SCENARIOS (per order, own couriers)")
    scen = {
     "A. on-demand multi-merchant, base (2 stops, $85, 15%, $7.99)": P(n_merchants=2),
     "B. A + batching 40% + 2-min waits (orders staged ready)": P(n_merchants=2, batch_share=.4, wait_at_merchant_min=2, first_leg_min=5),
     "C. single IGA-type full shop $130, 12% take, $9.99 fee, cap $8, batch 40%": P(n_merchants=1, basket=130, take_rate=.12, delivery_fee=9.99, service_fee_cap=8, batch_share=.4, first_leg_min=5, wait_at_merchant_min=2),
     "D. scheduled 2-hr windows, routed van 3 drops/hr, 2 merchants $120, 12%": P(n_merchants=2, basket=120, take_rate=.12, delivery_fee=9.99, service_fee_cap=8, first_leg_min=0, wait_at_merchant_min=1.5, inter_stop_min=2, last_leg_min=12, handover_min=3, batch_share=1.0, batch_saving=.45, promo_per_order=1.0),
     "E. D + platform consolidation: merchants drop to hub, 1 courier leg": P(n_merchants=1, basket=120, take_rate=.15, delivery_fee=9.99, service_fee_cap=8, first_leg_min=0, wait_at_merchant_min=1, last_leg_min=12, batch_share=1.0, batch_saving=.5, promo_per_order=1.0, pick_overhead_min=8),
    }
    for k, p in scen.items():
        r = order_pnl(p)
        print(f" {k:<80} contrib ${r['contribution']:6.2f} ({r['contrib_pct_gmv']:.1%} GMV), courier ${r['courier']:.2f}")
    print(" (E ignores merchant->hub drop cost, ~$3-6/order if merchants do it, and a hub lease)")
    line()
    # city break-even on scenario D economics
    cD = order_pnl(scen["D. scheduled 2-hr windows, routed van 3 drops/hr, 2 merchants $120, 12%"])["contribution"]
    cC = order_pnl(scen["C. single IGA-type full shop $130, 12% take, $9.99 fee, cap $8, batch 40%"])["contribution"]
    for nm, cc in (("C", cC), ("D", cD)):
        if cc > 0:
            for label, tgt in (("city fixed", FIXED_CITY), ("city+central", FIXED_CITY + central), ("+$500k draw x1.25", (FIXED_CITY + central + 500_000) * 1.25)):
                od = tgt / cc / 365
                print(f" scenario {nm} (${cc:.2f}/order) break-even vs {label:<18}: {od:6,.0f} orders/day = {od/AREA:5.1f} orders/km2/day over {AREA:.0f} km2")
    line()

    print("11. WHAT HAS TO BE TRUE: venture outcome")
    for exit_ev in (150e6, 300e6, 1e9):
        net_rev = exit_ev / 2.0   # 2x net revenue (low-margin delivery marketplace multiple)
        gmv = net_rev / 0.24      # net revenue (take+fees) ~24% of GMV in this model
        orders = gmv / 76         # blended basket
        print(f" exit A${exit_ev/1e6:,.0f}M @2x net rev -> net rev A${net_rev/1e6:,.0f}M, GMV A${gmv/1e9:.2f}B, {orders/365:,.0f} orders/day")
