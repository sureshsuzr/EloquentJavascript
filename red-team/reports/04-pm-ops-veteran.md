# Veteran Head of Property Management (Melbourne): red-team report

## Verdict
**The plan survives only if it changes how it measures. Judged on the measure the brief uses now, the 3x claim is close to fatal.** "300+ properties per relationship PM" mostly reflects how the work is split between roles. It does not show that AI makes anyone more productive. Incumbents already split leasing, inspections and accounts away from the PM, so the founder's 3x shrinks to roughly **1.2–1.6x in properties per *total* FTE**, and that is the number the P&L depends on. The biggest problem is the denominator: Gate 2 should measure **properties per total FTE and department wage cost per property**, not PM headcount. The plan also has to plan for an "exceptions-only" PM job, which concentrates conflict and will churn people faster than a $110k salary can hold them.

## Attacks on the load-bearing assumptions

**A1. Cost to serve: 3x properties per relationship PM. Severity: High.**

*Workload per 100 properties per month in a Melbourne mixed portfolio.* These are my estimates from running departments, checked against public data where I could find it.

| Activity | Events /100/mo | Automatable? | Human (judgment/relationship) | On site |
|---|---|---|---|---|
| Maintenance requests | 25–40 (urgent 3–5) | Triage, quotes, dispatch and tenant updates: ~70% | Over-limit approvals, tenant-caused damage, mould/damp, recurring faults, landlord pushback: 6–10 | Trades access, occasional PM attendance |
| Arrears | 6–12 events; 1–2 reach notice stage | Reminders, payment plans to template, notice drafting | Hardship, family violence, plan breaches, the decision to go to VCAT | — |
| VCAT (all types) | 0.4–0.8 | Bundle assembly, evidence indexing | Strategy, hearing (4–10 h each incl. prep) | Hearing (mostly remote) |
| Fixed-term ends and renewals | 6–8 | Notices, e-sign | Landlord's intentions; post-Nov-2025 there is no end-of-term ground, so the "should we keep them" conversation is harder | — |
| Rent reviews (max 1 per 12 months) | 7–8 | Comparables, notice | Setting the %, landlord consult, renter challenge to CAV | — |
| Vacates and re-lets | 2.5–3.5 (30–40% annual turnover) | Ads, scheduling, application screening (standard form helps) | Selection, landlord sign-off, bond claim decision | Exit CR, viewings (3–6 sessions), entry CR, keys |
| Routine inspections (max 1 per 6 months, none in first 3 months) | ~14–16 | Report write-up from photos, issue extraction | Follow-up on breaches | Yes, all |
| Compliance (smoke annual; gas and electrical every 2 years; minimum standards) | ~8 smoke + ~8 gas/elec | Scheduling and outsourcing to compliance contractors: ~95% | Non-compliance remediation with stubborn landlords | Contractor |
| Landlord contact (inbound) | 30–60 | ~half (statements, "when is the inspection") | Sell/hold, capex advice, complaints, lost-management saves | — |
| Insurance claims | 0.5–1 | Form filling | Evidence, landlord hand-holding (10–20 h for a malicious-damage claim) | Sometimes |
| Onboarding / lost managements | 1–3 | Data migration, authorities | Retention call | Key/compliance audit visit |
| Tail events (death, hoarding, squatting, flood, police) | 0.1–0.3 | — | 10–40 h each | Yes |

The raw volume is roughly **250–400 events/100/month**. In a traditional portfolio model a PM "touches" about 80–120 cases/100/month and spends about **110–125 hours** on them, including leasing and inspections (a PM on 130 properties spends about 145–160 working hours a month). Take out the field and leasing hours and the desk work is about **60–75 h/100/month**.

For a PM to carry 300 properties, with 25% of their time protected for proactive landlord work (about 120 productive hours a month), desk load has to fall to **≤40 h/100/month**. That is about a 1.7x cut in desk time. It is achievable but not easy, and it is **not 3x**. The rest of the "3x" is the role split, and anyone running a pod model already has that. Harcourts' MD describes a traditional 130–180 properties per PM depending on support. Ausnet runs 11,500 properties with 127 PM staff (~90 per FTE). Those two figures together show the split is already priced in.

*The arithmetic that kills the "beat $580" claim.* The brief compares PM wages only and leaves out on-costs. Super is 12% (from 1 July 2025), and with payroll tax and WorkCover the loaded multiplier is about 1.2. On that basis:
- Incumbent: $75k × 1.2 / 130 = **~$690/property**, not $580.
- Founder: $110k × 1.2 / 300 = **$440**; at a realistic 220 it is **$600**.
- The comparator that matters is **whole-department wages per property**. I estimate $900–1,200 at incumbents with ~80–100 properties per total FTE. My 1,000-property org chart below costs about **$1,170/property** with the founder unpaid as Head of PM. That is only a little better than a well-run incumbent, and only on the assumption that AI absorbs maintenance coordination and accounts.

**A2. "PMs run small pre-qualified viewing tours at lease-up." Severity: High.**
At 1,000 properties and 30–40% turnover that means 300–400 re-lets a year, each needing 3–6 viewing sessions: **1,000–2,000 tours a year, or 4–8 every working day**. Melbourne leasing peaks in December–February. A 300-property PM would have 8–12 vacancies at once in January. Either they stop doing relationship work or days-to-lease slips, and days-to-lease is a guaranteed metric in this plan. Leasing has to be a separate role (leasing consultants paid $70–85k or per lease). The PM should only run tours for prestige stock or problem landlords.

**A4. Acquired managements survive the move to an AI-led service. Severity: High in my domain.**
Each acquired roll arrives with a hidden backlog: overdue smoke/gas/electrical checks, missing or expired management authorities, unreconciled trust items, incomplete key registers, no ingoing condition reports, and tenants already in arrears. I budget **2–4 PM hours per property in the first 90 days**, or 200–400 hours per 100 acquired. Landlords leave sub-scale rolls when their known PM disappears; the PM leaving is the trigger, not the AI. At 300 landlords per PM, one resignation puts **$600k of revenue (~$2.2M of roll value)** at key-person risk.

## Things the brief gets wrong, misses or understates

1. **Wrong denominator.** "Properties per relationship PM" flatters the model. Use **properties per total FTE** (target ≥120 against an incumbent 80–100) and **wage cost per property, fully loaded** (target ≤$900).
2. **The exceptions-only job is a burnout machine.** If AI handles everything pleasant and routine, the PM's day is made up entirely of angry landlords, abusive tenants, VCAT and hardship. Kolmeo's 2026 survey (n=411, Kantar) found **63% of PMs feel overwhelmed** and **nearly 2 in 5 are considering leaving or unsure**. Legislative change was named by 43% as a major pressure. Industry turnover is commonly quoted at ~35%/yr (attributed to Macquarie benchmarking, undated, unverified). A $110k salary fixes the pay complaint. It does not fix the conflict load, and the conflict load is the main reason PMs leave. Concentrating it makes it worse.
3. **Recent law raises the human workload.** The Nov 2025 reforms removed the end-of-fixed-term no-grounds notice, so bad tenancies run longer and landlords need more reassurance. From **13 October 2026** (three weeks ago, so time-sensitive), bond claims must be supported by evidence given to the renter beforehand and must not contradict the condition report, with penalties for breaches. Vacates now need better evidence. This also cuts in the founder's favour: strong photo-backed condition reports produced by field staff plus AI are a real quality edge.
4. **After-hours is missing from the plan.** Victoria's urgent-repair categories (burst pipes, gas leaks, no hot water, unsafe premises) arrive at night and on weekends at about 1–2 per 100 per month. Someone licensed-adjacent has to answer. Budget a roster allowance of $8–15k/yr per on-call person, or an outsourced after-hours service, and an AI triage layer that **must not** be the final decision-maker on safety.
5. **Guarantees turn exception bursts into cash liabilities.** A response-time guarantee fails at exactly the moment the model is weakest: January, storms, a PM resignation. A maintenance-cost guarantee is underwriting risk (old stock, landlords who defer capex). Guarantee days-to-lease and response SLAs only, and only once 6 months of data exist.
6. **The trust account and officer-in-effective-control role is a real job.** Daily reconciliation, monthly owner disbursements and the annual audit need a named accountable person (0.5–1 FTE at 1,000 properties), even with software.
7. **Gate 2 can't be proven on 50–100 properties.** Tail events (VCAT, insurance claims, deaths, floods) occur at ≤1/100/month, so a 100-property sample sees too few to estimate them, and one summer of leasing seasonality is missing. Measure *rates* at 100, but don't declare 300 per PM proven until ≥250 properties × 12 months.
8. **The market is shrinking.** Victorian active bonds fell from 674,462 (Dec 2023) to 649,978 (Dec 2024), and from Sep 2023 to Sep 2025 they fell by more than 22,000. Expect **lost-management churn of 8–12%/yr from sales alone**, each loss needing a retention call and a handover. Organic growth has to cover that before it adds anything.

## Numbers checked

| Claim | Finding | Status / source |
|---|---|---|
| Incumbent PM wage cost ≈ $580/property ($75k/130) | Arithmetic is right but on-costs are excluded. Loaded ≈ $690. The relevant comparator is department cost, ~$900–1,200/property | [estimate: SG 12% from Jul 2025 + payroll tax/WorkCover ≈ 1.2x; ~80–100 props/FTE] |
| Traditional PM load ~130 | 130–180 depending on support (Harcourts MD); ~90 per PM staff at Ausnet (11,500/127) | [verified: eliteagent.com (Kasey McDonald); realestatebusiness.com.au R&W/Ausnet ranking] |
| 300+ per relationship PM credible | Credible only with leasing, field, accounts and hard-cases split out, desk load ≤40 h/100/mo, and conflict work offloaded | [estimate: workload table above] |
| Field cost $300–450/property/yr | 2 routines × ~$150 + 0.35 × (entry + exit CR ~$200 each) ≈ $440. Leasing labour is **not** included and adds ~$150–250 | [estimate; Crossub $150/inspection from brief, unverified] |
| PM turnover | ~35%/yr commonly cited | [unverified: attributed to Macquarie benchmarking, via stafflink/ipropertyexpress] |
| PM stress | 63% overwhelmed; ~2 in 5 considering leaving or unsure; 43% cite legislative change | [verified: Kolmeo State of PM 2026 via realestatebusiness.com.au] |
| Routine inspection limits | ≤1 per 6 months, none in first 3 months, 7 days' notice | [verified (secondary summaries of RTA/CAV); confirm on CAV] |
| Smoke / gas / electrical | Smoke alarms annually; gas and electrical every 2 years; extended to all agreements (start date for older agreements differs by source) | [verified: VBA/BPC Residential Tenancies Regulations 2021 page; extension timing unverified] |
| No-grounds end-of-term notice | Removed from 25 Nov 2025 | [verified: Justice Connect HLIP] |
| Bond claim evidence rule | In force 13 Oct 2026 | [verified: consumer.vic.gov.au news "No more unsupported bond claims"] |
| VCAT volume | Residential Tenancies List ~45k applications/yr (45,863 in 2021–22) against ~650k bonds ≈ 7 per 100 tenancies/yr, or ~0.6/100/month all parties | [verified: VCAT 2021–22 via Wikipedia; Anika Legal Nov 2025 for ~45k avg] |
| Active bond decline (~25k to Sep 2024) | 674,462 → 649,978 (Dec 23 → Dec 24); >22k fall Sep 23 → Sep 25 | [verified: PIPA / ABC reporting of Homes Victoria data; Property Update] |
| :Different ~200 staff | Not checked here | [unverified] |

## Improvements (ranked by impact)

1. **Redefine Gate 2.** Require (a) ≥120 properties per total FTE, (b) fully loaded wage cost ≤$900/property, (c) relationship-PM load ≤40 desk-hours/100/month. Drop "300 per PM" as the headline. It is an output of those three, not a goal.
2. **Build a "hard-cases desk" from 500 properties.** One specialist ($90–110k) owns arrears beyond day 14, VCAT, bond disputes, insurance claims and hardship. This takes the burnout fuel off relationship PMs and builds VCAT expertise, which will be the founder's most valuable compliance asset under the 2025–26 laws.
3. **Separate leasing from PMs.** Use leasing consultants with a per-lease bonus. PMs keep the landlord sign-off call on tenant selection.
4. **Make an AI-built evidence pack the product.** Use dense-route field staff, standardised photo protocols, AI comparison of entry and exit reports, and evidence bundles that meet the 13 Oct 2026 bond rule and VCAT standards. This is the one place where AI plus field staff clearly beats incumbents now. It also cuts PM time on the most adversarial workflow.
5. **Fund a 90-day acquisition-onboarding team.** Budget $250–400 per acquired property: a compliance sweep, authority re-signing, a key audit and a "meet your new PM" call within 14 days. Put it in the roll purchase price model.
6. **Cap and price PM retention.** Contract a maximum load (e.g. 300 properties or 40 exception-hours/100/month, whichever comes first). Pay a bonus tied to landlord retention and PM-hours per 100. Run a buddy-PM system so every landlord knows two names, which reduces key-person risk.
7. **Narrow the guarantees** to days-to-lease and first-response time. Remove maintenance-cost and arrears guarantees until 12 months of data exist.

## Tests & kill criteria

| Test | Metric | Threshold | Timeframe / cost |
|---|---|---|---|
| **Shadow baseline before owning anything.** Pay a willing Melbourne agency (or the target roll vendor) to tag 2 PMs' PropertyMe activity and timesheets for 4 weeks | Desk-hours and exceptions/100/month, split by category | Gives the denominator. If desk work is <50 h/100 the AI prize is small | 4–6 weeks, $5–15k |
| **Replay test.** Run the AI harness in shadow on that agency's inbound messages and tickets | % of cases closed with no human edit; error rate on legal notices | ≥55% closed untouched with 0 legally defective notices, or rethink | 4 weeks after baseline |
| First 100 properties (live) | Exceptions/100/mo and PM minutes/100/mo | ≤50 exceptions and ≤45 h by month 6, trending down | 6 months |
| Scale proof | Properties per total FTE; loaded wage cost/property | ≥120 and ≤$900 at ≥250 properties for 12 months, including a January | 12–18 months |
| **Kill:** productivity | PM desk-hours/100/mo | >70 h at month 9 with no downward trend, which means you have built an incumbent with a better salary | — |
| **Kill:** people | Relationship-PM voluntary attrition | ≥1 of the first 3 PMs quits within 12 months citing workload or conflict | — |
| **Kill:** retention | Landlord lost-management rate excluding sales | >8%/yr on acquired rolls in year 1 | — |
| Quality guard | Days-to-lease, bond-claim success, VCAT win rate | At or better than corridor median from the comparison tool data | Ongoing |

## Answers to open items in my domain

**Definition of the exception metric, measurable from day 1.**
- *Case*: every inbound or system-generated item (message, ticket, notice, scheduled task) logged against a property in the system of record.
- *Exception*: a case in which **any salaried non-field human** (PM, leasing, hard-cases, accounts) does anything beyond a single one-click approval of an AI-proposed action **within pre-authorised policy**. Editing an AI draft counts. A phone call counts. Overriding a policy limit counts.
- **Report three numbers per 100 managed properties per calendar month:** (1) exceptions, (2) human minutes logged against them (auto-timed from the case tool, plus manual call logging), (3) the "escape rate", meaning cases the AI closed that later reopened or produced a complaint or legal defect.
- Segment by category (maintenance, arrears, leasing, landlord, legal/VCAT, compliance, onboarding). Report **onboarding exceptions separately** so acquisitions don't hide steady-state performance.
- **Field visits are not exceptions.** They are measured as cost per visit.
- The headline target for 300 per PM is **≤40 PM-hours/100/month**. Exception count is diagnostic; minutes are what decides it.

**Org charts (with AI handling maintenance coordination, comms and statements)**

| Role | 100 | 500 | 1,000 |
|---|---|---|---|
| Founder: licensee / officer in effective control, Head of PM, after-hours escalation | 1 | 1 | 1 (or hire a Head at ~$150k+ and step back) |
| Relationship PM ($110k) | 1 (also leasing and some inspections; not a 300 test) | 2 | 3–4 |
| Hard-cases (arrears, VCAT, bond, insurance) | founder | 0.5 (shared) | 1 |
| Leasing consultant | PM + casual | 1 | 2 |
| Field inspector (dense route, ~6 visits/day) | contractor ~$150/visit | 1–1.5 | 2.5 |
| Trust accounts / compliance admin | bookkeeper 0.2 | 0.5 | 1 |
| Onboarding (acquisitions) | — | contract team as needed | 0.5–1 |
| **Total FTE excluding founder** | ~1.5 | ~5.5–6.5 | ~10–11.5 |
| **Properties per FTE** | n/a | ~80–90 | ~90–100 |
| Loaded wages per property (my estimate) | ~$1,600 | ~$1,250 | ~$1,100–1,200 |

At 1,000 properties this gives roughly $2.0k revenue less ~$1.15k wages less ~$200 software, insurance and overheads, which is **~$650/property**, consistent with the brief's margin. The catch is that the founder works in the business, unpaid, as Head of PM. Reaching ≥120 per FTE (~8 FTE) requires AI to remove the maintenance coordinator and half the accounts role. That is the real bet, and the shadow test can measure it before any money is spent.

**What :Different and task-based models teach.** Pod and task models raise properties per PM but often *lower* landlord satisfaction ("nobody owns my property") and increase handoff errors. :Different had ~200 staff for its book [unverified], and cheap pricing could not cover service labour. The lesson for this plan: keep one named owner per landlord, split the *tasks* behind that owner, and never let the price fall before PM-hours per 100 do.

**What breaks first at scale, in order:** January leasing peak → one or two VCAT/arrears marathons per PM per quarter → after-hours urgent repairs → a PM resignation carrying 300 landlords → backlog from roll onboarding → maintenance-cost guarantees during storm season.

## Questions I'd hand to other specialists
- **Licensing/legal:** Can agent's representatives under one officer in effective control lawfully carry the hard-cases desk, including VCAT representation, for a corporate licensee? Which tasks must a licensed estate agent perform personally?
- **Finance:** Does the roll lender's covenant treat onboarding attrition (lost managements in the first 90 days) as a retention clawback? Can the onboarding budget be capitalised into the acquisition cost?
- **AI/tech:** Can PropertyMe's activity log and API support automatic minute-tracking per case, and does its data export include the full message history needed for the shadow and replay test?
- **Consumer law/ACCC:** Do "guaranteed" response times and days-to-lease create misleading-conduct exposure if they are missed in peak season?
- **Rent-roll broker:** What is the typical lost-management rate in the 6 months after a sub-scale roll changes owner, and how are retention clauses priced in Melbourne today?
- **Insurance:** Will PI and landlord insurers accept AI-issued notices (breach, rent increase, notice to vacate) without human sign-off?
