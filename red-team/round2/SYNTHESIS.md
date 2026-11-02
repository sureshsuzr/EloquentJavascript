# Round-2 synthesis: the platform thesis

10 independent agents, 2–3 Nov 2026. Reports in `reports/`, model in `models/ltv_model.py` (imports round-1 `red-team/models/unit_economics.py`). Legal points rest largely on search summaries, because Victorian legislation, CAV and Treasury sites were blocked from the session. **Verify before acting**, especially the claimed 2026 federal tax changes (see "Must verify").

## Bottom line

**The bundle doesn't change the order of magnitude, and a few parts of it are illegal or uninsurable as written. But one part is a real edge for a statistician-CFO, and it isn't the one the brief led with.**

- **Lifetime value with all services is only ~10–30% above management alone** (01, 07). At base take-up rates the stack adds ~$160 per property per year. The property count for a $500k draw falls from **~3,100** to **~2,500**, not to ~1,000.
  - Correction to round 1: once s 48A zeroes the $75 sale referral, management alone needs ~3,100 properties, not ~2,500. Services mostly win that back.
- **Halving the scale would need take-up at 3–4x base** (01), for example capturing 45–60% of landlord refinances in-house. Nobody in Australian PM has shown that.
- **Direction matters more than breadth** (07). The services worth money **win and keep managements**. They are channels *into* PM, not products sold *through* it. Cross-sell in comparable businesses stayed in single digits to low teens unless the operator controlled the transaction.

## Your question: is autonomous rental management here?

**No, and not by 2029. But the binding constraints aren't model capability** (09).
- **Today:** ~45–55% of task volume can run as act-and-report (L3), but **under 20% of the money at risk** can.
- **What stays human through 2029:** anything touching trust money, legal notices, applicant selection or bond evidence.
- **The binding constraints:** write access to the system of record, physical work, licensee accountability and liability, and privacy law (automated-decision disclosure from 10 Dec 2026).
- **Autonomy is commoditising fast.** EliseAI claims 1 in 6 US apartments and a $4B valuation; PropertyMe has announced agentic AiMe; Tapi sells AI maintenance triage. An AI-native operator probably beats a PropertyMe + Tapi agency on desk cost by **15–25% by mid-2027, not 2x**.
- **Compute is cheap and people are the cost.** Compute plus voice costs ~$15–40 per property per year. The cost is human exception handling.
- **Architecture:** long workflows compound errors (0.99 per step over 25 steps ≈ 0.78), so a deterministic workflow engine with statutory clocks owns the sequence and agents do the steps.

## Service-by-service verdict

| Service | Verdict | Why | Sources |
|---|---|---|---|
| **Landlord investment support at buy/sell/refinance moments** | **Build first: it carries the economics** | Hold/sell & refinance review, then broking via a separate credit-representative company: ~$60–180 per property per year, plus retained managements on sale and new ones from next purchases. Worth ~$60–150k/yr per 1,000 properties. Strengthens independence from sales. | 01, 03, 06, 07, 10 |
| **Maintenance** | **Build as cost-plus coordination + preventive plan + reserve; no risk transfer yet** | A flat fee absorbing variance is likely **insurance in kind** (APRA + AFSL). Adverse selection plus a 20% pricing miss costs ~$170k/yr at 500 properties. Its value is as a retention and data product. Risk transfer only later, via an insurer (authorised rep), then a binder/MGA beyond ~3,000 properties. | 02, 03, 07, 08, 09 |
| Tenant share of maintenance fee | **Kill: unlawful** | RTA bans the charge, and since Mar 2026 the ban reaches third-party rent-tech; repairs are the landlord's duty. | 02, 04, 05 |
| Tenant evaluation as a priced product | **Fold into the letting fee** | ~$16/property/yr; commoditised (Snug, 2Apply, Ignite); a 1,000-property book has ~15–30 defaults/yr, so 10–20 years of data to beat rules; standard form limits the data; rejected applicants' data destroyed in 30 days. Use a transparent rule set and a human decision. | 01, 04, 08, 10 |
| Rent guarantee / arrears cover | **Replace with a service guarantee** | Agency-issued rent guarantee = insurance. Offer a letting-fee refund + free re-let if a placed tenant is evicted for arrears within 12 months (~$15–30 per property per year). Distribute insurers' landlord cover. | 02, 03 |
| Tenant "grow equity" / rent as credit | **Kill as revenue** | Rent can't go on credit files under Part IIIA; renter fees are banned; savings products need an AFSL/ADI. Only a free, renter-controlled verified rent ledger ("genuine savings" evidence) is buildable. | 03, 05, 10 |
| Tenant home-buying | **Keep as a free "First Home Pathway" in a separate opt-in entity** | ~10% of renters buy per year; the 5% Deposit Scheme is uncapped; brokers write 81.6% of loans; Equifax/Occubuy launched a renter-to-owner score (Sep 2026). Worth <$25–80 per tenant relationship vs ~$3,600 per landlord relationship. | 01, 03, 05, 10 |
| Moving within the portfolio | **Keep as a retention feature** | Lawful with consent. Small but it cuts vacancy. | 04, 05 |
| Landlord analytics subscription | **Kill** | ~71–72% of investors own one property. | 06 |

## Where your CS / stats / CFO edge is decisive (and where it isn't)

**Decisive:**
1. **Pricing rent-roll acquisitions on modelled retention** (08). Avoiding a 5-point retention error is worth ~$100k on a $2M roll. Incumbents price on a rule-of-thumb multiple. This is the round-1 roll-up, made defensible by your edge: **a data-led acquirer**.
2. **Maintenance cost modelling** from acquired books' invoice history (2,000–4,000 property-years per acquisition) (02, 08, 09). It is the one AI/data asset vendors can't sell to every agency, because it depends on your own outcome data and risk book (09).
3. **In-tenancy arrears early warning** (08): ~12,000 tenancy-months/yr per 1,000 properties is enough to rank late-payment risk within 6 months, and it is a lawful operational use.
4. **Workflow-engine architecture plus evals** (09): the engineering discipline separates 15–25% from parity.

**Irrelevant or worse:**
- **Tenant scoring:** the data is too thin and too legally constrained.
- **Rent setting and landlord churn models:** they add little over bought Cotality/Domain data plus simple alerts.
- **Any model of renter finances:** it is a disqualifying conflict if it touches rent-setting or landlord advice.

**Hard design rule from 09:** keep urgency and statutory-deadline classifiers outside any cost-optimising loop. A triage agent that learns to defer repairs breaches Victorian repair duties across the portfolio.

## Legal architecture (04, 03)

- **LicensedCo** (estate agent licence) acts only for landlords: management, letting, the landlord-paid maintenance programme, investment analytics and reviews.
- **FinanceCo**: a corporate credit representative under an aggregator's credit licence. ~6–10 weeks, $10–20k to set up, with an experienced broker. Own credit licence only above ~150 loans/yr. **No personal-advice AFSL; nothing involving super/SMSF property** (an ASIC 2026 priority).
- **RenterCo**: a separate company, opt-in after the lease is signed, with its own privacy policy and a code-enforced information barrier so renter data never reaches rent-setting or landlord advice.

**Two disqualifying conflicts:**
1. Renter financial data reaching rent-setting or advice given to landlords.
2. One group entity acting for both the landlord-vendor and the tenant-buyer on the same property.

**s 48A is broader than referral fees.** It likely reaches insurance commissions, trade discounts and possibly broker commission on loans secured on the managed property. Model all at $0 until counsel advises; disclose in the rebate statement.

**Neutrality caveat (06):** a PM isn't neutral on hold-versus-sell, because a sale ends the management. The review must show the model rather than make a recommendation, charge a fixed fee, have a registered tax agent co-sign, and disclose in writing that the agency loses fees on a sale.

**Privacy (04, 08):**
- Disparate-impact testing before 10 Dec 2026.
- Opt in to the Privacy Act now (s 6EA).
- Use only standard-form fields.
- A human decides every application.

## Revised thesis (what the evidence supports)

> **A data-led acquirer and operator of rent rolls, sales-independent, whose two proprietary assets are (1) retention-modelled acquisition pricing and (2) a maintenance cost and quality book; with a landlord investment desk at buy/sell/refinance moments as the channel that wins and keeps managements.** Tenant services are free retention features in a separate entity. AI is the operating system, not the pitch.

This isn't "just run an agency". The agency is the balance sheet that produces the data. The edge is in pricing acquisitions, pricing maintenance and keeping landlords, which are the three things your skills improve and incumbents do by rule of thumb.

## Smallest tests that prove or kill the thesis (≈$50k total, ~10–12 weeks, mostly before owning anything)

| # | Test | Cost / time | Continue if | Kill if | Source |
|---|---|---|---|---|---|
| 1 | **Maintenance backtest:** 3-yr PropertyMe invoice export from 1–3 agencies (or acquisition targets in diligence); predict next-year cost per property | <$10k, 4–6 wks | Simple tariff predicts book-level cost within ±10–25% | Error >35% of mean → no flat fee ever; cost-plus only | 08, 09, 02 |
| 2 | **Retention-pricing model:** score 2–3 rolls for sale on modelled 3-yr loss vs broker multiple | ~$5k + broker time, 6 wks | Model finds ≥15% mispricing on at least one roll | No spread vs broker pricing | 08 + round 1 (02) |
| 3 | **Landlord hold/sell & refinance review**, via accountants, at $0 / $290 / $490 | ~$10–15k, Dec 2026–Jun 2027 | ≥8% pay $290 and ≥20% want a refinance check | <3% pay at any price | 06 |
| 4 | **Vendor-parity test:** same tasks on PropertyMe AiMe, Tapi and EliseAI-class tools vs your agents | ~$10–15k, 6–8 wks | Your desk minutes ≥15% better | Within 15% → stop building commodity agents; build only the risk/maintenance layer | 09 |
| 5 | **Legal opinions:** three-entity structure, s 48A reach (broking, insurance, maintenance), maintenance-plan insurance boundary (s 763E incidental) | ~$10–20k, 3–4 wks | Workable structure for the investment desk and the maintenance plan | Both blocked | 02, 03, 04 |
| 6 | (After first acquisition) **RenterCo opt-in** on one roll | ~$3–8k, 90 days | ≥15% opt-in; ≥3 settled loans per 300 households in 6 months | <15% opt-in, or any complaint linking the offer to rent/renewal | 04, 05 |

## Must verify (high-impact claims resting on search summaries)

1. **Federal tax changes (06):** claimed removal of negative gearing for newly bought established dwellings from 12 May 2026, and CGT moving to indexation with a 30% minimum tax from 1 Jul 2027, with existing assets deemed sold on 30 Jun 2027. If true, this is a major demand window for hold/sell advice from now to June 2027, and a drag on new investor inflow. **Check against Treasury/ATO before using it.**
2. Victorian third-party rent-tech fee ban start date (31 Mar 2026 vs 25 Nov 2025 per different agents).
3. PropertyMe partner API: job writes allowed, tenancies read-only, no webhooks (09).
4. Add-on insurance deferred-sales exemptions: expired 5 Oct 2026 unless the 2031 extension was finalised (03).
5. s 48A text and scope; the standard application form's full field list; RTA rules on tenancy databases (03, 04).

## Disagreements between agents

- **Which landlord service leads:** broking (01: highest risk-adjusted LTV) vs investment-review-as-channel (07: value is in retained and new managements). These are compatible: the review is the front door; broking and management retention are the monetisation.
- **Maintenance:** 08/09 see it as the founder's best data edge; 02/07 see it as the most likely way to lose money if priced early. Resolution: cost-plus now, model the risk on acquired data, transfer risk only via an insurer later.
- **Size of the investment-desk prize:** $60–180 per property per year across agents; scale for $500k between ~1,700 and ~2,500 properties.
