"""Round-3 SaaS CFO model: rent-roll / PM data business (products A-D).

Run:  python3 red-team/round3/models/software_model.py
All AUD. Every input is tagged [V]=verified (see report), [E]=estimate, [U]=unverified.
Time base: Y1 = FY Nov-2026..Oct-2027. 7-year horizon to Nov-2033.
"""
from dataclasses import dataclass, field

# ---------------------------------------------------------------- 1. Volumes
AU = dict(
    managed_props=2_300_000,   # [E] PropertyMe ~1.9M ANZ (Dec-25/Oct-26 [V]) + PropertyTree/Console/Rex/Ailo; 2.4M in brief plausible upper
    pm_businesses=11_400,      # [V] IBISWorld residential leasing & mgmt businesses 2025 = 11,403
    pm_agencies_real=7_000,    # [E] PropertyMe 6,500 agencies [V] incl NZ; dedupe offices vs businesses
    roll_deals=650,            # [E] full+partial roll sales/yr: ~5-6% of ~11k books; no published count exists
    avg_deal_value=1_100_000,  # [E] ~290 props x ~$1,300 commission x ~2.9x; eastern-seaboard median $471k (older broker data [V])
    lenders=6,                 # [E] NAB [V] + CBA/Westpac/Bankwest/Macquarie/private credit [U]
    franchise_hqs=12,          # [E] Ray White, LJ Hooker, Harcourts, Belle, McGrath, First National, PRD, Raine&Horne, Century21, Laing+Simmons, Elders, Stone
    roll_brokers_valuers=20,   # [E] Pendium, Acumentis, Real Estate Dynamics, Wollermann etc.
    landlord_insurers=8,       # [E] Terri Scheer, EBM RentCover, CHU, Allianz, Suncorp brands, IAG brands, QBE, Youi
    maint_platforms=4,         # [E] Tapi, Rent Manager-style, PropertyMe Maintenance, Ailo
)

# Market multipliers for other geographies, relative to AU on deal count and props  [E]
GEO = {
    "NZ": dict(deal_x=0.15, prop_x=0.15, local_cost=150_000),   # ~600k rentals; small, PropertyMe/Tapi present
    "UK": dict(deal_x=2.5,  prop_x=1.6,  local_cost=900_000),   # active PE roll-ups (Dwelly 6 deals 2025 [V], Lomond); fees % of rent
    "US": dict(deal_x=4.0,  prop_x=4.0,  local_cost=2_500_000), # SFR PM M&A (Evernest/Poplar, PURE HomeRiver [V]); AppFolio/Buildium data; fragmented
}

# ---------------------------------------------------------------- 2. Product revenue at maturity (AU)
@dataclass
class Product:
    name: str
    lines: list = field(default_factory=list)  # (label, units, penetration, price)
    gm: float = 0.8
    def arr(self, scale=1.0):
        return sum(u * p * px for _, u, p, px in self.lines) * scale

A = Product("A rent-roll DD/valuation", [
    ("buy-side DD reports",      AU["roll_deals"], 0.30, 6_000),    # [E] ~0.5% of deal value; 5-pt retention error ~$50k on $1.1M deal
    ("vendor-prep reports",      AU["roll_deals"], 0.15, 2_000),
    ("lender subscriptions",     AU["lenders"],    0.50, 40_000),
    ("broker/valuer seats",      AU["roll_brokers_valuers"], 0.35, 12_000),
    ("roll-up/PE subs",          8,                0.50, 30_000),   # [E] Managex, Yolk, Areal-type buyers
], gm=0.80)

B = Product("B retention/book-health monitoring", [
    ("agency per-property",      AU["managed_props"], 0.08, 3.60),  # $0.30/prop/mo; core PMS costs ~$16-23/prop/yr [U aggregators]
    ("franchise HQ licences",    AU["franchise_hqs"], 0.40, 50_000),
    ("lender covenant monitoring", AU["lenders"],     0.50, 25_000),
], gm=0.85)

C = Product("C maintenance cost intelligence", [
    ("insurer data licences",    AU["landlord_insurers"], 0.40, 150_000),
    ("maintenance platform API", AU["maint_platforms"],   0.50, 80_000),
    ("agency benchmarking",      AU["managed_props"],     0.04, 2.40),
], gm=0.75)

D = Product("D agentic DD/integration", [
    ("integration projects",     AU["roll_deals"], 0.12, 25_000),  # services-heavy
    ("integration software subs", 30,              0.6, 20_000),   # serial acquirers
], gm=0.55)

PRODUCTS = [A, B, C, D]

def market_table():
    print("\n=== 1. AU mature revenue ceiling by product (penetration as stated) ===")
    tot = 0
    for p in PRODUCTS:
        print(f"{p.name:40s} ARR ${p.arr():>12,.0f}  GM {p.gm:.0%}")
        for lab, u, pen, px in p.lines:
            print(f"   {lab:30s} {u:>10,.0f} x {pen:>4.0%} x ${px:>8,.2f} = ${u*pen*px:>11,.0f}")
        tot += p.arr()
    print(f"{'AU TOTAL (all four, mature ~Y7-10)':40s} ARR ${tot:>12,.0f}")
    # theoretical TAM at 100% penetration
    tam = sum(u * px for p in PRODUCTS for _, u, _, px in p.lines)
    print(f"{'AU TAM @100% penetration':40s}     ${tam:>12,.0f}")
    print("\n=== 2. With expansion (A+D scale on deals, B+C on props; minus local cost) ===")
    ad = A.arr() + D.arr(); bc = B.arr() + C.arr()
    run = tot
    for g, m in GEO.items():
        add = ad * m["deal_x"] + bc * m["prop_x"]
        run += add
        print(f"+{g}: +${add:>11,.0f}  (one-off entry cost ~${m['local_cost']:,.0f}); cumulative ${run:,.0f}")
    return tot, run

# ---------------------------------------------------------------- 3. Ramp
def ramp(ceiling, years=10, k=0.65, t_mid=5.5, start_frac=0.0):
    """Logistic adoption to a ceiling; returns ARR list year 1..years"""
    import math
    return [ceiling / (1 + math.exp(-k * (t - t_mid))) for t in range(1, years + 1)]

def first_year(series, target):
    for i, v in enumerate(series, 1):
        if v >= target:
            return i
    return None

def pnl(series, gm, cac_ratio=0.9, base_opex=300_000, per_arr_opex=0.22, founder_sal=(0, 0, 150_000), draw_cap=500_000):
    """P&L per year. S&M = cac_ratio x new ARR (blended CAC payback ~11 months on GM).
    Opex = fixed base (hosting, data, legal, insurance, 1-2 engineers) + variable per ARR (support, CS, eng).
    Founder salary: 0 while employed (Y1-Y2), then founder_sal[2]; extra distribution only from positive
    EBITDA once cumulative cash > 0, capped so total draw <= draw_cap.
    Funding need = deepest cumulative cash trough (must be funded by founder cash or angels)."""
    out, cash, prev, trough = [], 0, 0, 0
    for yr, arr in enumerate(series, 1):
        new = max(0, arr - prev); prev = arr
        sal = founder_sal[min(yr, 3) - 1]
        base = base_opex * (0.5 if yr <= 2 else 1.0)   # part-time phase: contractors only
        ebitda = arr * gm - new * cac_ratio - base - arr * per_arr_opex - sal
        cash += ebitda; trough = min(trough, cash)
        extra = min(draw_cap - sal, max(0, ebitda)) if cash > 0 else 0
        heads = (1 if yr <= 2 else 2) + arr / 220_000   # [E] ~$200-250k ARR per FTE small vertical SaaS
        out.append((arr, ebitda, cash, sal + extra, heads))
    return out, -trough

def ramps():
    print("\n=== 3. Ramp scenarios (ARR by year; Y1 = Nov-26..Oct-27; Y1-2 part-time) ===")
    scen = {
        "AU-only base (A wedge, B+C added Y3-5)": dict(ceiling=3_500_000, k=0.75, t_mid=5.5, gm=0.78, own=0.80),
        "AU+NZ+UK (seed ~$2.5M at Y3)":           dict(ceiling=12_000_000, k=0.7, t_mid=6.5, gm=0.78, own=0.55),
        "AU-only bear (A only, low adoption)":    dict(ceiling=1_200_000, k=0.8, t_mid=4.5, gm=0.80, own=0.90),
    }
    res = {}
    for name, s in scen.items():
        r = ramp(s["ceiling"], k=s["k"], t_mid=s["t_mid"])
        p, need = pnl(r, s["gm"], base_opex=220_000 if "bear" in name else (500_000 if "UK" in name else 300_000))
        y1, y3 = first_year(r, 1e6), first_year(r, 3e6)
        print(f"\n{name}: yrs to $1M ARR = {y1}, to $3M = {y3}; peak funding need ${need:,.0f}")
        print("  Yr        ARR      EBITDA   cum cash  founder pay  FTE")
        for i, (arr, e, c, d, h) in enumerate(p, 1):
            print(f"  {i:2d} {arr:>11,.0f} {e:>11,.0f} {c:>10,.0f} {d:>12,.0f} {h:5.1f}")
        res[name] = (r, p, s["own"])
    return res

# ---------------------------------------------------------------- 4. Exit values
def exits(res):
    print("\n=== 4. Exit value at Y7 (ARR x multiple x founder ownership, after CGT est.) ===")
    # [E] private vertical SaaS 2026: ~2-7x ARR, median ~4.5x; <$5M ARR AU single-country data business 2.5-4x;
    # strategic (PropertyMe/EQT, Cotality, MRI, InfoTrack, Reapit) up to 5-6x if data asset is unique.
    mults = {"distressed/acqui-hire": 1.5, "small-cap AU": 3.0, "strategic": 5.0}
    for name, (r, p, own) in res.items():
        arr7 = r[6]
        for m_name, m in mults.items():
            ev = arr7 * m
            net = ev * own * (1 - 0.235)   # [E] 47% top rate x 50% CGT discount; small-business concessions likely fail $6M test
            print(f"  {name[:38]:38s} ARR7 ${arr7:>10,.0f} {m_name:22s} EV ${ev:>11,.0f} founder net ${net:>10,.0f}")

# ---------------------------------------------------------------- 5. 7-year wealth comparison
def after_tax(x):
    # 2026-27 resident rates [E: Stage-3 rates, 15% second bracket from 1 Jul 2026 per legislated cut] + 2% Medicare
    b = [(18_200, 0), (45_000, 0.15), (135_000, 0.30), (190_000, 0.37), (1e12, 0.45)]
    t, lo = 0, 0
    for hi, r in b:
        if x > lo:
            t += (min(x, hi) - lo) * r
        lo = hi
    return x - t - 0.02 * x

def wealth():
    print("\n=== 5. Risk-adjusted 7-year wealth (net of $160k/yr living cost, savings compounding 6%) ===")
    LIVING, R, YRS = 160_000, 0.06, 7

    def path(incomes, terminal=0.0):
        w = 0.0
        for inc in incomes:
            w = w * (1 + R) + (after_tax(inc) - LIVING)
        return w + terminal

    # (a) stay: $500k cash, 3% growth, plus employer equity (expected $1.0M, [E])
    stay = path([500_000 * 1.03 ** i for i in range(YRS)], terminal=1_000_000)

    # Software: Y1-Y2 part-time (keep job; but founder spends ~$150k/yr own cash on 1-2 contractors), quit start Y3
    def sw(draws, exit_net, cash_in):
        inc = [500_000, 500_000] + draws
        return path(inc, terminal=exit_net) - cash_in * (1 + R) ** 5
    # Draws/exit nets taken from sections 3-4 (founder pay $150k Y3+ until cash-positive; founder funds
    # ~$500k of the trough, angels the rest at the ownership shown in section 3).
    sw_scen = {
        "SW strong (AU+UK, ~$7M ARR Y7)": (0.10, [150e3, 150e3, 150e3, 150e3, 500e3], 11.0e6, 500e3),
        "SW base (AU ~$2.6M ARR Y7)":     (0.30, [150e3, 150e3, 150e3, 150e3, 150e3], 5.5e6, 500e3),
        "SW lifestyle/bear (~$1M ARR)":   (0.30, [150e3, 150e3, 150e3, 150e3, 150e3], 2.2e6, 500e3),
        "SW fail (shut Y4, job Y5)":      (0.30, [150e3, 150e3, 450e3, 480e3, 500e3], 0.0, 500e3),
    }
    # (b) operator (round 1/2): ~$1.2M cash risk; draws ramp; roll equity at Y7
    op_scen = {
        "Op success (2,500 props)": (0.30, [500e3, 500e3, 150e3, 250e3, 350e3, 450e3, 500e3], 5.0e6, 1.2e6),
        "Op middling (1,000)":      (0.40, [500e3, 500e3, 100e3, 150e3, 200e3, 250e3, 250e3], 2.0e6, 1.0e6),
        "Op fail":                  (0.30, [500e3, 500e3, 80e3, 80e3, 450e3, 480e3, 500e3], 0.2e6, 1.0e6),
    }
    # (c) capital partner: family-office equity funds rolls; founder salary $300k + 20% carry over 8% pref
    cp_scen = {
        "CP success": (0.35, [500e3, 500e3, 300e3, 300e3, 300e3, 350e3, 350e3], 2.5e6, 0.3e6),
        "CP middling": (0.40, [500e3, 500e3, 300e3, 300e3, 300e3, 300e3, 300e3], 0.6e6, 0.3e6),
        "CP fail": (0.25, [500e3, 500e3, 250e3, 0, 450e3, 480e3, 500e3], 0.0, 0.3e6),
    }
    print(f"(a) Stay employed: ${stay:,.0f}  (deterministic-ish)")

    def ev(scen, is_sw=False):
        tot, rows = 0, []
        for n, (pr, draws, ex, cash) in scen.items():
            v = sw(draws, ex, cash) if is_sw else path(draws, ex) - cash * 0.3 * (1 + R) ** 4
            # operator/CP: assume ~30% of cash invested is a permanent loss net of equity already in terminal
            rows.append((n, pr, v)); tot += pr * v
        return tot, rows
    for label, scen, flag in [("Software", sw_scen, True), ("(b) Operator", op_scen, False), ("(c) Capital partner", cp_scen, False)]:
        e, rows = ev(scen, flag)
        for n, pr, v in rows:
            print(f"   {n:32s} p={pr:.2f}  wealth ${v:>12,.0f}")
        p_beat = sum(pr for _, pr, v in rows if v > stay)
        print(f"{label}: expected ${e:,.0f}; P(beat staying) = {p_beat:.0%}")

if __name__ == "__main__":
    au, glob = market_table()
    res = ramps()
    exits(res)
    wealth()
