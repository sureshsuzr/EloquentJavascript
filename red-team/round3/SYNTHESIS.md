# Round-3 synthesis: the software / data business

9 independent agents, 3 Nov 2026. Reports in `reports/`; model in `models/software_model.py` (output in `models/software_model_output.txt`). Many sources (NAB, Macquarie, PropertyMe, OAIC, CAV, trade press) were blocked from the session and rest on search summaries. **No Australian rent-roll deal count is published**, so every market size below is an estimate. Counting deals is the first test.

## Bottom line

**As a standalone Australian software company: no.** It is a $1.5–6M-revenue niche that pays you about $150k from year 3 and $500k only around year 8. It beats staying employed only narrowly on expected value, with a ~40% chance of actually doing better (02).

**As an acquisition-pricing engine that you own and use as an investor, with software revenue on the side: yes, it's the best option across all three rounds, and it can start while you're employed for ~$40k.**

Your edge is worth $50–100k per deal to whoever *buys* the roll, but only $3–15k per report to whoever *reads* it (01, 02, 08). So capture it as equity and carry, not as report fees.

## The numbers (agents' estimates)

| | |
|---|---|
| AU rent-roll deals/yr | ~250–900 (estimates vary; ~60–150 in Victoria); ~40 repeat buyers (02, 01, 06, 07) |
| Revenue ceiling, DD reports alone (A) | ~$0.5–1.7M/yr realistic; $3–8M at full share (01, 02, 06, 08) |
| All products, AU maturity | ~$5.8M ARR, of which ~$2M low-margin services (02) |
| Base-case path | $1M ARR in year 5, $3M in year 8; ~$1.2M of funding at the low point; founder pay ~$150k from year 3 (02) |
| Exit | ~$5–18M in AU/NZ; $9–15M founder take only with the UK from year 3 and ~$2.5M seed (02, 04, 07) |
| Value of a correct retention call | Realistically $15–40k per $2M roll over a disciplined checklist (03), not $100k: holdbacks cover early losses (07: 25–40% of price; 06: 5–10%); random variation is ±~5 points on a 400-property roll (03) |

## Seven-year comparison of paths

Two agents modelled this independently with different structures. Use the ranking, not the decimals.

| Path | 02 SaaS CFO (risk-adjusted, after tax and living costs) | 08 Founder-fit |
|---|---|---|
| Stay employed | ~$2.36M (incl. ~$1M expected employer equity) | ~$1.75M |
| Quit to build software | ~$3.03M; 40% chance of beating staying, 30% roughly flat | ~$2.5M; 45% chance of failure, ending near ~$0.67M |
| Operator (rounds 1–2) | ~$2.40M; 30% chance | — |
| Capital partner only | ~$1.60M; 35% chance | ~$1.7M |
| **Hybrid: co-invest in a roll-up + engine in-house + software on the side** | not modelled | **~$3.4M; floor ~$1.5M** |

**Your employer equity is the swing factor:** if it's worth ≥$1.7M over 7 years, staying beats quitting for software (02).

## What the agents agree on (≥4 independently)

1. **Rent-roll due diligence (A) is the way in, not the business**: the deal volume is too thin (01, 02, 04, 06, 07, 08).
2. **Sell to capital, not to agencies.** Customers are acquirers, roll-ups, franchise HQs and brokers. Anything sold to individual agencies gets copied by PropertyMe: EQT-owned since Dec 2025, ~1.9M properties, AiMe Connect live since 8 Oct 2026, agentic AiMe announced (04, 05, 06, 07).
3. **Banks aren't an early customer.** Macquarie reportedly values rolls in-house at no charge; APRA vendor onboarding (CPS 230/234) takes 6–18 months; reach lenders via a panel valuer (01, 05, 06, 07, 08).
4. **The moat is outcome data:** roll histories matched to what happened 12–36 months after sale. Every engagement needs a licence to keep de-identified features plus 12- and 24-month post-settlement exports. Privacy guidance means DD data must otherwise be destroyed (03, 05, 06, 07).
5. **Ground truth is the bottleneck, not code.** Post-sale loss is driven mostly by how the buyer integrates (~66% vs ~80% kept), which is larger than the error being priced. Backtest on rolls acquirers bought 2–4 years ago; ~30 deals with outcomes are needed to prove a pricing lift (03, 05).
6. **The UK may be the bigger market** (Dwelly, Lomond, LSL, Foxtons buying; the Renters' Rights Act, in force 1 May 2026, pushes small agents to sell). But the large UK roll-ups build their own pricing, and Nurtur already sells brokers a lettings-valuation tool (02, 04, 06).

## Product verdicts

| Product | Verdict | Notes |
|---|---|---|
| **A: rent-roll DD / pricing** | **Wedge; best used in-house by an acquirer you invest in** | Concierge v0 in ~5–6 founder-weeks; productised v1 in 6–8 months part-time; $15–35k cash (05). 60–70% of a generic report is reproducible via AiMe Connect plus an LLM; the differentiator is a calibrated P10–P90 retention/price band under integration scenarios, figures traceable to source rows, and a lender-acceptable format (05). |
| A as a vendor-paid "Verified Roll" via brokers | Worth testing | $2–4k, vendor-paid, so brokers aren't threatened and you see every listed roll (06). |
| **B: retention / book-health monitoring** | **Split verdict** | Feature vs PropertyMe for single agencies (02, 04, 07). Viable only as post-acquisition monitoring for serial acquirers ($15–40k/yr) and franchise HQs ($50–200k/yr) (01, 06). |
| **C: maintenance intelligence** | **Module inside A, not a business** | Tapi (~$49M raised, 160–400k+ properties, free quarterly maintenance index) and hipages/Bricks + Agent own the data; insurers exclude wear and tear and already buy Cotality/Geoscape/Nearmap (04, 09). 02 sees it as the insurer-facing moat. That is the minority view, conditional on insurers paying. Use it to score each property's capex and 2027 energy-standard liability as a retention-risk input. |
| D: agentic DD / integration | Services cash flow | ~1x revenue multiple (02, 07). |

## Recommended path

**The hybrid** (08, supported by 01, 02, 07):
1. **Build the pricing engine** (A, plus C as a module) in your own IP company, part-time, while employed.
2. **Co-invest $300–500k** as capital and data partner in a roll-up run by a licensed operator, for 10–20% equity or carried interest. The engine is its exclusive acquisition tool. Alternatively, run a $20–50M roll-buying vehicle for a family office or PE backer on a fee plus carry (01).
3. **Sell only non-conflicting products to outsiders:** post-acquisition monitoring (B), vendor-paid Verified Roll reports and a free quarterly roll-transaction and retention index (to become the reference; the latest public Victorian figures are 2021–22) (07).
4. **Don't sell buyer-side DD to all comers while investing in a buyer.** That is a conflict that poisons data sharing (08).
5. **Add the UK** only once AU outcomes prove the model.

**Personal limits:** ≤$750k cash at risk, no personal guarantees (08).

## Before anything else (non-negotiable)

1. **Employment:** review your contract (outside interests, IP assignment, confidentiality; Corporations Act ss 182–183 duties if you're an officer). Get **written employer consent before writing code or contacting customers**. Build on your own devices and accounts. Risk is near zero if your employer has no exposure to property, data, lending or insurance; severe if it does (08).
2. **LocalAgentFinder confidentiality never expires**, and monitoring (B) overlaps with LAF's agent-performance data (08).
3. **Tax (unverified, but reported independently in rounds 2 and 3):** the May 2026 Budget proposal to replace the 50% CGT discount with indexation plus a 30% minimum tax from 1 Jul 2027, with startup/small-business carve-outs in flux. How and when you issue founder shares could move after-tax exit value by $1–3M on $10M. **Get tax advice before incorporating, and before 30 Jun 2027** (08, round-2 06).
4. **Data residency:** Anthropic's own API has no AU region; use Amazon Bedrock's AU profile (newest-model availability there unverified). Vendor-side de-identification before upload; raw data deleted within 30 days (05).
5. **Licensing:** price per report or by subscription. A sale-linked success fee may constitute estate-agent work in Victoria (06), which conflicts with 01, 02 and 07 suggesting success fees. **Get advice before using one.**

## 90-day test (~$40k, while employed; finish by ~30 Apr 2027)

| # | Test | Continue if | Kill if | Source |
|---|---|---|---|---|
| 0 | Contract review + employer consent | Written consent by 15 Dec 2026 | Consent refused or conflicted employer → hold until you leave | 08 |
| 1 | **Count deals** with 3 brokers + NAB | ≥250 deals/yr nationally | Fewer → A is a consultancy | 02, 06 |
| 2 | **Data access:** 10 agencies asked for report packs; brokers/acquirers asked for past deals with outcomes | ≥3 agencies deliver in 3 weeks; ≥10 deals with outcomes licensed by day 90 | <2 brokers and 3 agencies share by 31 Jan 2027 | 03, 08 |
| 3 | **Backtest** on rolls bought 2–4 years ago | Within 3 points of actual retention; ≥10% better than trailing loss rate; beats a 5-variable heuristic by ≥3 points | >5 points off | 02, 03, 07 |
| 4 | **Paid pilots** | ≥3 paid DD reports at ≥$5k (07: ≥2 of 5 at ≥$7.5k) + 1 LOI from a lender or franchise HQ | <3 paid | 01, 02, 07 |
| 5 | **Maintenance module** | Top-decile ranking captures ≥20% of next-year spend; a $3k+ shock lifts landlord loss ≥1.2x; ledger captures ≥60% of true spend | Below thresholds → drop C | 03, 09 |
| 6 | **Operator / capital partner:** talk to 3 licensed operators and 2 family offices or PE funds | LOI with a licensed operator by 30 Jun 2027 | No partner → software-only route, with UK interest from 5 acquirers as the tiebreak | 01, 08 |

## Decision calendar (08, 02)

- **15 Dec 2026:** contract review, employer consent, tax adviser engaged.
- **31 Jan 2027:** deal count and data agreements (tests 1–2).
- **30 Apr 2027:** backtest and paid pilots (tests 3–5).
- **30 Jun 2027:** operator/capital-partner LOI; founder-share and tax structure done.
- **31 Dec 2027: resign only if all hold:**
  - ≥$250k contracted recurring revenue (or ≥$400k trailing incl. DD);
  - ≥8 paying customers across ≥2 segments, incl. a lender or franchise HQ;
  - data rights to ≥50k property-years;
  - a backtest beating broker multiples;
  - or the roll-up equity/carry deal signed.
- **End 2028:** ≥$0.7M recurring revenue (go back to a job if <$0.4M).
- **End 2029:** ≥$1.5M, or sell at 2–4x revenue.

## Corrections to the brief

- Real Estate Dynamics is a broker/consultancy, not a benchmarking dataset. Macquarie benchmarking is a periodic survey, latest ~2024 (04).
- hipages bought 51% of VIZ ($1.4M, Apr 2026); VIZ sells insurance to tradies, not landlord warranties. CHU is a strata insurer (09).
- Non-compete ban: an exposure draft (7 Sep 2026), not law; threshold $190,100 for FY27; doesn't apply at ~$500k (08).
- Victorian active bonds reportedly ~745k (May 2026), up from 732k (Jun 2024), so earlier attrition assumptions may be stale (03).
- Managed properties nationally: 2.0–2.4M is the defensible range (02).
