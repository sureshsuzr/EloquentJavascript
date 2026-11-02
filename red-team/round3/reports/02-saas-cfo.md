# SaaS CFO & Market-Size Modeller: red-team report

Model: `red-team/round3/models/software_model.py` (output saved in `models/software_model_output.txt`). All AUD. Written 2 Nov 2026.

## Verdict

**Survives only if the plan is reframed. As a pure Australian SaaS company it is too small to beat $500k plus equity on expected value by enough to justify the variance.** All four products together have an Australian ceiling of about **$5.8M ARR at maturity**, and ~$2M of that is services (D). A realistic Australia-only path reaches **~$1M ARR in year 5, ~$2.6M by year 7 and $3M only in year 8**, with a funding trough of **~$1.2M**. That gives a 7-year expected wealth of ~$3.0M against ~$2.4M from staying employed, with only a **~40% chance of beating the job** and a 30% chance of ending roughly flat.

**The biggest issue is that the founder's edge is worth far more to whoever owns the acquisition than to whoever sells the report.** A 5-point retention error is worth $50–100k on a typical deal, but the market will pay about $3–8k for a DD report. The economics improve only if (a) the UK is in the plan from year 3, or (b) the engine is monetised as principal or carry in roll acquisitions rather than as SaaS.

## Verdict on the software business

- **A (rent-roll DD/valuation) is the wedge, but it isn't a business on its own.** Australia has roughly 650 roll deals a year **[estimate]**, which caps A at ~$1.2–1.7M ARR. Revenue is lumpy and per-deal, and most buyers are occasional. It is the right first product because a single deal proves the model against a broker multiple. But it sells to roughly 100–200 buyers a year in Australia.
- **B (retention monitoring) is a feature, not a company.** Agencies pay PropertyMe only ~$16–23 per property per year for the whole system of record **[unverified: aggregator listings]**. An analytics add-on at $3–4 per property per year with ~8% adoption makes ~$0.7M. PropertyMe's AiMe Connect (live 8 Oct 2026, read-only MCP to Claude/ChatGPT on the Advanced tier) **[verified: Elite Agent/PropTechConnect]** already lets an agency ask its own book "which landlords look at risk". The parts PropertyMe can't easily do are the paid lines: franchise HQ and lender covenant monitoring across systems.
- **C (maintenance intelligence) is the moat, and the buyers are insurers, not agencies.** Agencies pass maintenance cost to landlords, so they have little reason to pay for prediction. The money sits with ~8 landlord insurers and a few maintenance platforms: ~$0.6–0.9M ARR in Australia. The value is that it can't be commoditised: it needs cross-agency invoice histories joined to outcomes. It is the asset a strategic acquirer would pay a premium for.
- **D (agentic DD/integration) is the highest-revenue line, but it's services at ~55% gross margin**, and it is valued at ~1x revenue, not 3–5x. Run it as a paid pilot that collects data, not as the product.
- **Conclusion:** the business is **A as the door, C as the asset, and lenders and roll-up capital as the anchor customers.** B is a module inside A's subscription. D is optional services. As SaaS alone, it only clears the bar with the UK.

## Attacks on the thesis

1. **The market is tiny in dollar terms (High).** Australia's TAM at 100% penetration of every line is ~$39M. A realistic share is $3–6M. Private vertical SaaS sold in 2026 at a median of ~4.5x ARR, with a range of ~2–7x **[unverified: advisory blogs citing SaaS Capital/Aventis; one cites the SaaS Capital Index at ~3.8x in early 2026]**. A single-country company at $2.5–3M ARR with thin EBITDA sits at **2.5–4x**. That gives an enterprise value of ~$7–11M and a founder net of **~$4.5–6.5M after CGT**. That beats the job, but only if things go well.
2. **Value capture is inverted (High).** The founder's edge is worth ~15% of deal value to a buyer (round 2's test threshold). The incumbent price anchors for DD are a valuer's report (a few thousand dollars **[unverified: no fee schedule found]**) and the broker's free multiple. On ~$1.1M deals, $6k is ~0.5%. Charging more requires either a success fee (buy-side advisory at 1–2% is $11–22k, but that is advisory work, not SaaS) or principal participation.
3. **Few buyers, and occasional ones (High).** Most acquirers buy one roll every 3–5 years. Repeat buyers are franchise groups, a handful of aggregators (Managex, Yolk, Areal-type) **[verified: trade press]**, 20-odd brokers and valuers, and about 6 rent-roll lenders. NAB is the only verified bank programme: up to 70% LVR (another NAB page says 80%), minimum 100 properties, terms to 10 years **[verified: nab.com.au]**. With ~40 recurring buyers, CAC is founder time, and churn is high between deals.
4. **Data access sits with the target, not the customer (High for A, Med for C).** DD needs the *vendor's* export. Vendors resist (confidentiality before signing) unless the broker or lender requires it. Distribution therefore has to come through brokers and lenders, who control the data room. C needs many agencies' invoice histories: privacy consent, contractor names and landlord data. PropertyMe controls the API terms (round 2: partner API, tenancies read-only **[unverified]**).
5. **Platform risk from PropertyMe/EQT and Cotality (High, time-sensitive).** EQT took majority control of PropertyMe in Dec 2025, with ~1.9M properties and 6,000–6,500 agencies across ANZ **[verified: EQT release/Elite Agent]**. A PE owner wants adjacent revenue, and PropertyMe already sees the cross-agency data needed for B and C benchmarks. Cotality's RP Data subscription includes agency benchmarking **[verified: Cotality site]**. If either ships "roll health score" as a free feature, B dies and A's lender line weakens. The window is probably 18–36 months.
6. **Salary-replacement timing (High).** Founder pay is ~$150k from year 3 until cash-positive in year 8. Distributions of $500k a year don't arrive until **year 8** in the base case and never in the bear case. Payment is all back-loaded into the exit.
7. **Capital need is understated if the founder goes full-time (Med).** The trough is ~$1.0–1.2M in Australia and ~$1.6M with NZ and the UK (seed ~$2.5M for buffer). Bootstrapping is possible only if the founder stays employed and keeps it at 1–2 contractors through year 2.

## Things the brief gets wrong, misses or understates

- **"~2.4M managed properties" is plausible but unverified; use 2.2–2.4M.** PropertyMe alone claims ~1.9M across ANZ. Cotality's 2016-Census work put ~60% of investor-owned rentals with an agent **[verified: CoreLogic via press]**. On ~3.0–3.3M rented dwellings, 2.0–2.4M is the range. It barely matters: no line of revenue depends on per-property pricing at scale.
- **The brief lists customers but no buyer counts.** The binding constraint is ~650 deals a year and ~40 recurring institutional buyers, not 2.4M properties.
- **No Australian rent-roll transaction count is published.** Real Estate Dynamics' annual report relies on agency survey data **[verified: survey form]**. A broker or lender count in test 1 is a precondition, not a detail.
- **The multiple base is old and dispersed.** Brokers quote $2.00–3.60 nationally, 3.30–4.10 in Sydney, ~2.75–3.00 in WA, and a 3.05x Sydney sale **[verified: broker articles, mixed dates]**. Fees are compressing as vacancy hit a record-low 0.7% in March 2026 **[unverified: one commentary]**. Low vacancy means fewer new managements, which supports roll prices and deal volume.
- **The brief doesn't separate exit buyers.** Realistic acquirers are PropertyMe/EQT, MRI, Reapit, InfoTrack, Cotality, a bank, a broker group or a UK roll-up. Strategic premiums come only for C's data asset or UK reach.
- **The UK is the bigger prize and the active consolidation market.** Dwelly did 6 acquisitions in 2025, raised £69M of debt and manages 15k+ properties, and Lomond has reportedly made ~40 acquisitions **[verified: Property Reporter/TNW; Lomond unverified]**. PE-backed serial acquirers are exactly the subscription buyers A needs.

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| ~2.4M managed properties AU | 2.0–2.4M; PropertyMe ~1.9M ANZ, 6,000–6,500 agencies | estimate / verified (EQT Dec-25, PropertyMe Oct-26) |
| Number of PM businesses | 11,403 residential leasing & management businesses (2025) | verified: IBISWorld |
| Roll deals per year | ~500–800; base 650 | estimate: ~5–6% of books change hands; no published count |
| Average deal | ~$1.1M (290 props × ~$1,300 × ~2.9x); older eastern-seaboard median $471k | estimate / verified (broker data, dated) |
| Melbourne 2.8–3.5x | National 2.0–3.6x; Sydney 3.3–4.1x; recent 3.05x | verified (broker press, mixed dates) |
| Rent-roll lenders | NAB up to 70% (or 80%) LVR, min 100 PUM, 10-yr term; others not found | verified (NAB) / unverified (others) |
| PMS price per property | ~$1.35–1.95/prop/month (aggregators conflict) | unverified |
| PropertyMe AI | AiMe Connect (MCP, read-only) from 8 Oct 2026; agentic AiMe next | verified: Elite Agent |
| Private vertical SaaS multiple 2026 | ~2–7x ARR, median ~4.5x; vertical 4–8x at $1–50M ARR | unverified: advisory blogs |
| AU ceiling (all products) | $5.8M ARR mature; TAM $39M | model |
| Years to $1M / $3M ARR (AU base) | Y5 / Y8 | model |
| Funding trough | AU $1.2M; AU+NZ+UK $1.6M | model |
| 7-yr wealth: stay vs software | $2.36M vs $3.03M expected; P(beat) 40% | model |

## Improvements (ranked by impact)

1. **Price A on value, not on seats.** Charge a fixed fee of $5–8k plus a success fee of 0.5–1% of price when the buyer closes below the vendor ask using the report, or take a retainer from serial acquirers. Aim for ~$15k a deal. On the model, that alone lifts A's ceiling from $1.7M to ~$3M.
2. **Sell to the institutions that touch every deal.** Lenders, brokers and franchise HQs control the data room and the deal flow. Make the report a lender credit input: "retention-adjusted security value", re-run annually for covenants. That turns per-deal revenue into ARR and fixes data access.
3. **Plan for the UK from year 3, and sell to UK PE roll-ups first** (Dwelly, Lomond and similar). In the model, the UK alone adds ~3x Australia's revenue. Only the AU+UK path reaches ~$7M ARR by year 7, and only that one produces a founder net above ~$9M at small-cap multiples.
4. **Build the maintenance dataset as a by-product of DD.** Every DD export includes job and invoice histories. Make data-retention rights (de-identified, aggregated) a contract term from deal one. After ~50 deals you hold ~15,000 property-years of maintenance history: the insurer product and the strategic-exit asset.
5. **Capture the principal upside alongside the SaaS:** carry or co-invest in a family-office roll vehicle that uses the engine (the round-1 Tranche C idea). A 15% mispricing on 3 deals a year at $1.1M is ~$500k a year of value. Owning 20% carry over an 8% pref is worth more than the report fees.
6. **Treat D as paid discovery, priced at cost plus 30%. Never let it exceed 30% of revenue**, or the exit multiple collapses towards 1x.
7. **Accept that B is a feature.** Bundle it into lender and franchise subscriptions; don't build an agency self-serve funnel against PropertyMe.

## Tests & kill criteria (~90 days, ≤$40k, while employed)

| Test | Metric | Continue if | Kill if | By |
|---|---|---|---|---|
| Deal-flow census with 3 brokers + NAB | Australian roll deals/yr, number of repeat buyers, % with system export in the data room | ≥500 deals; ≥30 repeat buyers | <300 deals or <15 repeat buyers (Australia can't carry A) | 15 Dec 2026 |
| Backtest 3 historical deals (buyer's post-deal data) | Modelled 3-yr retention vs actual; spread vs price paid | Error ≤3 pts; ≥1 deal mispriced ≥10% | Error >5 pts | 31 Jan 2027 |
| Paid pilots | Signed paid reports at ≥$5k, or a lender pilot | ≥3 paid reports + 1 lender/franchise LOI | 0 paid after 10 pitched | 31 Jan 2027 |
| Willingness to pay for success fee | % of buyers accepting fee + 0.5% success | ≥30% | <10% (it's a $3k report business) | 31 Jan 2027 |
| UK pull | Calls with 5 UK roll-up/PE acquirers | ≥2 ask for a pilot on a UK book | 0 interest | 31 Jan 2027 |
| Insurer interest in C | Meetings with 4 landlord insurers | 1 data-partnership LOI | All decline, or data rights refused | 28 Feb 2027 |
| Employer IP and conflict clearance | Written consent | Granted | Refused → stop, or wait until resignation | Before writing code |

**Resignation gate (30 Jun 2027):** ≥$250k of contracted ARR or bookings, ≥1 lender or franchise customer, and the backtest passed. Otherwise keep it part-time or stop.

## Answers to the round-3 questions in my domain

**1. Who pays, how much, and is it big enough?**

- **Who pays:** acquirers (~$6k per report, ~$15k with success pricing), lenders ($25–40k/yr), franchise HQs (~$50k/yr), brokers (~$12k/yr), insurers ($150k/yr data licences), and agencies only marginally.
- **Australia alone is too small for a large exit:** ~$3.5M realistic ARR, against a ~$5.8M ceiling. It is big enough to beat the salary **in expected value, with ~40% probability**.
- **Founder income:** ~$150k from year 3, reaching $500k only in year 8.
- **Exit:** at year 7, Australia-only, ~$8–13M EV, with the founder netting ~$4.9–8.1M. The AU+UK path gives ~$21–35M EV and a founder net of ~$9–15M.

**5. Capital and timeline.**

- **Years 1–2, part-time:** ~$300k founder cash (contractor engineer, legal, data).
- **Years 3–5, full-time:** a further ~$0.9M. Fund it with ~$0.5M founder money plus ~$0.5–0.7M from angels or strategics at ~20% dilution.
- **UK:** needs a ~$2.5M seed in year 3 (founder ~55% at exit).
- **Avoid VC before year 3.** The TAM won't support a venture story until the UK is proven.

**6. Comparison (7-year, risk-adjusted, after tax, net of $160k/yr living cost):**

| Route | Expected wealth (7 yr) | P(beat staying) |
|---|---|---|
| Stay employed (includes ~$1M expected employer equity) | **$2.36M** | n/a |
| Software | **$3.03M** | 40% |
| Operator | **$2.40M** | 30% |
| Capital partner | **$1.60M** | 35% |

Software has the best expected value and the most job satisfaction for this founder (analytics, product, deal-making, no trust accounts). It also has the widest spread: a 30% chance of roughly zero wealth gain over 7 years. If employer equity is worth ≥$1.7M in expectation, staying wins.

**7. Smallest test:** the deal-flow census plus a 3-deal backtest plus 3 paid reports, finished by 31 January 2027.

## Questions I'd hand to other specialists

- **Data/privacy counsel:** can de-identified ledger and maintenance data from a DD export be retained and pooled under the Privacy Act and the vendor NDA? What do PropertyMe's API and data terms permit for third-party benchmarking?
- **Statistician:** with ~650 deals a year and short post-deal histories, how many labelled outcomes are needed before modelled retention beats the broker multiple by ≥3 points?
- **Incumbent strategist:** what is PropertyMe/EQT's 2027 roadmap for cross-agency benchmarks, and would they acquire, partner or clone?
- **UK specialist:** UK letting-agency deal count, DD norms, data systems (Reapit, Alto, Goodlord), and Renters' Rights Act effects on roll values.
- **Employment lawyer:** the founder's IP-assignment and moonlighting clauses, and whether a lender or franchise pilot conflicts with the employer's business.
