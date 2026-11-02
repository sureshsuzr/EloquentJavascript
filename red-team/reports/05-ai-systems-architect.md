# AI & Systems Architect: red-team report

## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)

**Survives-if.** The technology is not the binding constraint. What AI can safely automate today is drafting, triage, scheduling and evidence assembly. It cannot safely commit the agency to anything: money, dates, legal notices or trust movements. The biggest issue is that the brief treats "PropertyMe exposes live data to external AI assistants" as an automation substrate. **AiMe Connect (Oct 2026) is read-only MCP into a user's own Claude or ChatGPT account.** It is a reporting tool, not a write path. Every productivity gain therefore has to come from a work layer the founder owns: a work ledger and agent orchestrator sitting beside PropertyMe. That layer must be instrumented from day one to measure exceptions per 100 properties per month. Without it, Gate 2 cannot be measured and the 3x claim stays a belief. Second issue: at 100 properties, any paid engineering costs more per property than the whole Crossub benchmark. The founder has to build it himself or the gate is meaningless.

## Attacks on the load-bearing assumptions (only those in your domain; evidence, severity High/Med/Low)

**A1. Cost to serve, 3x+ properties per PM (High).**
- AI removes typing, not events. Workload is driven by repairs, arrears, vacancies, disputes, entries and landlord calls, and AI does not reduce their number. It cuts handling time on the routine ones and does nothing for the judgment-heavy tail: VCAT, insurance claims, difficult landlords, bond disputes. [estimate: my experience of ops agents] Drafting and triage typically cut handling time on routine items by 40–70%, and on escalations by about 0–20%. If escalations take about 40% of a PM's hours (common in mixed-quality rolls), the blended gain is about 1.5–2x, not 3x. Getting to 3x needs the **role split** (field staff, a lease-up function, a back-office/trust officer) plus **portfolio hygiene**: shedding the worst 5–10% of landlords and properties, which drive a disproportionate share of exceptions. The brief credits AI for what is mostly an org-design and portfolio-selection effect. That is still fine, but it changes what to measure.
- **"Exceptions per 100 properties" is undefined and gameable.** If an AI draft approved by a human without edits counts as "no exception", the metric flatters automation while a PM still reads every message. Use three numbers instead: (a) **human touches** (any human open, edit, approve or call), (b) **judgment exceptions** (a decision only a licensed person should make), and (c) **handling minutes**. The 300+ ratio rests on (c), not (a).

**A2. Durability, the 3–5 year window (High).**
- PropertyMe has said agentic AiMe follows AiMe Connect [verified: trade-press coverage of the AiMe Connect launch, eliteagent.com / proptechconnect.com, Oct 2026]. Rex has shipped an AI suite [verified: pulse.bot trade press]. Ailo markets "no one left in trust accounting" at a customer agency [verified: ailo.io blog, Jul 2026; vendor claim]. The drafting and triage layer will be in incumbents' core software within 12–24 months [estimate]. A harness built on PropertyMe is a **lead of about 18 months, not 3–5 years**. The durable edge is operational: role design, density, routing, exception discipline and the data from measuring them. The software gap is not durable.

**A4. Retention through an AI-led service (Med).**
- Acquired rolls come on whatever system the vendor agency used: PropertyMe, PropertyTree, Console Cloud, Rex PM and others. Each migration is a ledger cut-over (opening balances, bonds, arrears, standing disbursements) plus a comms switch. A botched cut-over is the most likely retention killer in the first 90 days after acquisition, and it happens before any AI benefit shows. So migration tooling is part of the platform, not a one-off.

**Platform dependency (Med).** Building on PropertyMe means its API terms, tier pricing and its own agentic roadmap shape the founder's cost-out. Access is partner-gated (client_id and secret issued manually) with no published rate limits [verified: third-party API catalogues apis.io / apitracker; no official developer portal found]. Write scopes are "not typically available" [verified: community wrapper docs, pypme]. Plan as if writes are limited to a few endpoints (documents, comments, bills) and may be refused.

## Things the brief gets wrong, misses or understates

1. **"PropertyMe exposes live data to external AI assistants, so building on the system of record incrementally is possible": half right.** AiMe Connect is MCP, **read-only**, follows existing user permissions, and is limited to Manage PM **Advanced tier or above**, from about 8 Oct 2026 [verified: eliteagent.com and proptechconnect.com coverage; the tier detail comes from one source]. It connects a *person's* Claude or ChatGPT session to the data. It does not give a server-side agent a write path. It is excellent for landlord reporting, portfolio analysis and exception dashboards. It is useless for closing a loop: sending a notice, booking an inspection, raising a work order or receipting. Production agents need the partner API (gated) or the founder's own work ledger, with the PM performing the write in PropertyMe.
2. **Data governance of AiMe Connect itself.** Linking a PM's own ChatGPT or Claude account sends renter personal information into that account's retention and training settings, and PropertyMe tells customers to review these [verified: same coverage]. Use Team or Enterprise plans with training off, or route through an API with zero data retention or a Sydney region (AWS Bedrock ap-southeast-2). Never let PMs use personal consumer accounts.
3. **Privacy ADM transparency obligations start 10 Dec 2026**, about five weeks from today [verified: OAIC media release; Allens, Corrs, Maddocks; OAIC guidance issued 30 Sep 2026]. New APP 1.7–1.9 require privacy policies to disclose the kinds of personal information used and the kinds of decisions made or substantially informed by computer programs. Applicant shortlisting, arrears escalation and maintenance prioritisation are all candidates. A small business turnover exemption may technically apply to a young agency [unverified for this entity; check with privacy counsel]. Opt in anyway: landlords, banks and roll vendors will diligence it, and the comparison funnel will hold personal data.
4. **Trust accounting is not an AI surface.** Victorian agents must reconcile monthly (Reg 26, Estate Agents (General, Accounts and Audit) Regulations 2018) and audit annually within three months of 30 June [verified: CAV auditing page; CAV 2026–27 CPD outline]. CAV is publicly prosecuting audit failures, including a licence suspension [verified: CAV news items; I could not fetch them to confirm dates]. Rule: **AI never writes to the trust ledger.** It may prepare disbursement packs and flag reconciliation variances, and nothing more.
5. **Hard-coded Victorian statutory clocks the agents must obey:** urgent repairs (renter may self-arrange up to $2,500; reimbursement within 7 days of written notice) [verified: CAV]; general inspections need 7 days' written notice, not in the first 3 months, at most once every 6 months [verified: CAV renter guidance via MP guidebook; secondary sources conflict, so confirm on CAV]; certain notices to vacate and rent-increase notices lengthened from 60 to 90 days; latest reforms in force 31 Mar 2026 [verified: CAV news]. RDRV has operated since 23 June 2025 and handles repair and bond disputes [verified: CAV/VCAT]. A triage agent that under-classifies an urgent repair produces a cost the agency cannot control.
6. **Comparison-funnel data pipeline.** Domain's API terms reportedly bar storing or using API data outside Australia [verified only via secondary commentary, 13labs.au; check the clause]. Scraping REA or Domain for "rent achieved" breaches their ToS. The funnel's data layer needs a licensed source (Domain API, Cotality) and AU-resident processing. That rules out naive US-hosted LLM pipelines over that data.

## Numbers checked (table: claim | finding | status/source)

| Claim | Finding | Status/source |
|---|---|---|
| PropertyMe exposes live data to external AI | Yes, AiMe Connect via MCP, read-only, Claude and ChatGPT, Advanced tier+, about 8 Oct 2026 | [verified: eliteagent.com, proptechconnect.com coverage] |
| PropertyMe API write access | Partner-gated, manually issued credentials; writes limited ("not typically available"); no documented rate limits | [verified: third-party catalogues and community wrapper; no official portal found] |
| PropertyMe Advanced price | about $195/month per 100 properties (+GST); sources conflict | [unverified: ITQlick/Spendbase; check propertyme.com.au/pricing] |
| Console Cloud / Rex PM / Ailo / Kolmeo APIs | Console: API exists, enterprise-tier gated. Rex PM: API for account holders. Kolmeo: partner API (invoice sync). Ailo: no public API found | [verified at listing level only: Capterra, fitgap, bricksandagent, npm] |
| ADM transparency start | 10 Dec 2026, APP 1.7–1.9; OAIC guidance 30 Sep 2026 | [verified: OAIC, Allens, Maddocks] |
| Trust reconciliation and audit (Vic) | Monthly reconciliation (Reg 26); annual audit lodged within 3 months of 30 June | [verified: CAV] |
| Urgent repair cap | $2,500 renter-arranged; 7-day reimbursement | [verified: CAV] |
| Inspection rules | 7 days' notice; not in first 3 months; ≤1 per 6 months | [verified: CAV renter material, secondary] |
| AI condition-report tooling in AU | Inspection Express 360AI (exit inspections, 2025); Property Inspect InspectAI room summaries; video-to-report mainly UK (KapturAI) | [verified: vendor sites; performance claims unverified] |
| LLM cost/property/yr | about $25–60 (comms + vision) | [estimate: ~100 comms events/property/yr × ~3 model calls × ~20k in / 1k out tokens at mid-tier pricing ≈ A$25–35; plus 2 inspections × ~300 photos ≈ A$5–15; ×1.5 for retries and evals] |
| Make-or-buy benchmark $560/property | My software + AI run-rate cost at scale is about $120–220/property/yr excluding engineering; at 100 properties engineering dominates | [estimate: see costs below] |

## Improvements (concrete changes to the plan, ranked by impact)

1. **Build a work ledger, not "AI on PropertyMe".** Use one Postgres event store in which every inbound item (email, SMS, call transcript, portal message, PropertyMe event via API poll or webhook) becomes a *case* with type, property, SLA clock, AI action, human touches, minutes and outcome. PropertyMe stays the system of record for tenancy, ledger and documents, and the ledger is the system of *work*. This is the only asset that is genuinely yours. It is what proves Gate 2, and it is what you show a lender or acquirer.
2. **Tiered autonomy policy, enforced in code and not in prompts.**
   - *T0, auto-send:* acknowledgements, FAQ answers drawn from lease or property facts, appointment confirmations for slots already chosen by the scheduler, payment reminders built from fixed templates.
   - *T1, draft and one-click approve:* maintenance triage outcome and trade dispatch under the landlord's pre-authorised limit (for example ≤$300 or ≤$500), inspection notices (the scheduler computes legal dates and the AI only fills the template), routine landlord updates.
   - *T2, human decides:* anything creating an obligation (date promises, money, waivers, rent changes), applicant selection, arrears escalation past the first reminder, any notice to vacate (prescribed CAV forms only, never LLM-composed), bond claims, anything mentioning lawyers, VCAT, RDRV, discrimination, family violence, health or safety.
   - *Outbound commitment gate:* every outbound message passes a second-model or rules check for dates, dollar amounts, promises, admissions and legal terms not present in the case facts. If it fails, the message is held for a human.
3. **Instrument exceptions from day one.** Define the three metrics (touches, judgment exceptions, minutes) per 100 properties per month, broken down by case type. Also log draft acceptance without edit, edit distance, SLA breaches, and complaints and disputes per 100. Before any AI goes in, baseline it on the first acquired or partner roll.
4. **Buy everything except the ledger and orchestrator.** Use PropertyMe for trust, tenancy and owner statements. Buy the inspection app (Inspection Express or similar) and add your own vision pass. Buy telephony and SMS (Aircall or similar, Twilio, or PropertyMe's native SMS). Use existing maintenance and trade tooling (PropertyMe maintenance or Kolmeo-style trade portals). Do not build a tenant app, ledger, owner portal or payments.
5. **Choose the system of record for acquisition compatibility, not features.** PropertyMe has the deepest AU footprint (about 35k users per launch coverage [unverified]), an AI read layer and an API. Write a migration runbook for PropertyTree and Console Cloud to PropertyMe (opening trust balances, bonds via RTBA, arrears, recurring disbursements) and rehearse it on a dummy roll before the first purchase.
6. **Jurisdiction as configuration: premature as architecture, right as discipline.** Do not build a multi-jurisdiction rules engine or adapters for several PM systems. You will run one state on one system for at least 24 months. Do keep every statutory clock, form and threshold in a single versioned policy file, separate from code, with a CAV source link and a review date. That costs nothing, is needed anyway because Victorian rules changed in Nov 2025 and Mar 2026, and leaves a credible path to NZ or NSW later. "Adapters over the system of record" is correct in its one useful form: one thin PropertyMe adapter behind an interface, so a forced migration (pricing, ToS or an AiMe conflict) costs weeks, not months.
7. **Condition reports: AI drafts, a human attests.** Field staff capture timestamped photos and video against a room checklist. The vision model drafts item-level condition text. Field staff correct it on site and sign. The renter gets the report through the standard process. The original media is kept immutably for 7+ years to support bond disputes at RDRV or VCAT. Track bond-dispute rate and win rate per 100 vacates as the quality metric.
8. **Founder writes the first platform.** As a hands-on AI user with Claude Code, he can build the ledger, orchestrator and integrations in about 6–8 weeks. A contractor at $150–200k/yr spread across 100 properties costs $1,500–2,000 per property, roughly 3x Crossub's benchmark. External engineering is a post-Gate-2 hire.

## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)

| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| **Shadow mode on a partner roll** (licensed partner grants read access via AiMe Connect or API plus inbox export; agents draft, nothing is sent) | % of inbound cases where the PM would send the AI draft unedited or with minor edits | ≥60% overall, ≥80% on T0/T1 types; otherwise the cost-out thesis is weak | Days 30–60, ≥1,000 cases |
| **Exception baseline** on the same roll | Human touches and handling minutes per 100 properties per month, by case type | Establish a baseline. Kill or redesign if modelled AI plus role split cannot reach ≤⅓ of baseline minutes | Day 45 |
| **Commitment-gate red team** (500 synthetic adversarial tenant messages: demands, injection attempts, discrimination bait, urgent-repair edge cases) | Escaped unauthorised commitments; urgent repairs under-classified | 0 escapes; ≤1% under-classification with all misses flagged for human review; otherwise no T0 autonomy | Day 60 |
| **Condition-report pilot** (10 entry/exit reports, AI-drafted vs PM-written) | Field minutes per report; item-level error rate on blind review | ≥40% time saved; error rate ≤ human baseline | Day 75 |
| **Live 50–100 properties** | Handling minutes per property per month; SLA breach rate; complaints | ≤ about 25 min/property/month total human time (300 properties per PM at about 125 PM hrs/month, excluding field) [estimate]; kill Gate 2 if >45 min after 6 months | Months 4–12 |

## Answers to open items in my domain

**Minimum platform for the first 100 properties** (buy, build or manual):
- *Buy:* PropertyMe Advanced (trust, tenancy, owner portal, AiMe Connect), an inspection app, telephony and SMS, Google Workspace or M365, a Team or Enterprise LLM seat for PMs, and an LLM API with zero retention or AU region.
- *Build:* the work ledger (Postgres), inbound normaliser (email, SMS, call transcripts), orchestrator with tiered policy and commitment gate, inspection scheduler with statutory date logic plus route batching, landlord monthly report generator (AiMe Connect or API read plus template), and exceptions dashboard.
- *Manual:* trust reconciliation and disbursement approval, applicant selection, arrears past first reminder, every legal notice, bond claims, landlord relationship calls, and acquisition migrations.

**Integration order:** (1) inbound comms into the ledger with measurement only; (2) PropertyMe read adapter so cases carry tenancy context; (3) maintenance triage plus trade dispatch at T1; (4) inspection scheduling and notices; (5) arrears reminders at T0 and escalation packs at T2; (6) condition-report drafting; (7) landlord reporting; (8) lease-up enquiries and viewing-tour booking. Measurement comes first because Gate 2 depends on it. Maintenance comes next because it is the highest-volume, most measurable category.

**Agent designs (one line each):**
- *Maintenance:* classify urgent or non-urgent against the CAV urgent-repair list (if in doubt, urgent), request photos, check the landlord's authority limit, dispatch from a preferred trade panel, and chase completion.
- *Tenant comms:* answers grounded only in lease and property facts retrieved from PropertyMe. Unknown answers go to a human; the model never infers one.
- *Arrears:* day 1/3/7 templated reminders. Day 14 produces a T2 pack with ledger, history and options. The PM decides on any notice.
- *Inspections:* the scheduler computes legal windows and clusters by suburb, and the agent only fills notices.
- *Condition reports:* described above.
- *Landlord reporting:* monthly narrative over ledger and maintenance data, with every number pulled by query and none generated by the model.

**Human-in-the-loop thresholds:** T0/T1/T2 as above. Re-tier a case type only after ≥200 cases with ≥95% unedited approval and zero gate escapes.

**Audit trail:** for each case keep the input, retrieved facts, prompt version, model version, draft, gate verdict, human action, sent text and timestamps, append-only. This serves APP 1.7 disclosure, RDRV/VCAT evidence and CAV inquiries.

**Failure modes and controls:**
- Hallucinated commitments: commitment gate plus T2.
- Discrimination: no AI ranking of applicants; AI only checks completeness of the standard application form; quarterly audit of lease-up outcomes; the Equal Opportunity Act 2010 (Vic) still applies.
- Privacy: AU-region or zero-retention APIs; no consumer accounts; least-privilege MCP; quarterly ADM disclosure review.
- Prompt injection from tenant email and attachments: agents with send rights never read raw attachments; tools are whitelisted per tier.
- Trust errors: no AI writes; dual approval of disbursements; monthly Reg 26 reconciliation by a human.

**Cost per property** [estimates, AUD/yr at 100 → 1,000 properties]:

| Item | At 100 | At 1,000 |
|---|---|---|
| PropertyMe | ~$25–30 | ~$25–30 |
| Inspection app | ~$20–40 | ~$20–40 |
| Telephony/SMS | ~$30–60 | ~$20–30 |
| LLM API | ~$25–60 | ~$25–60 |
| Hosting, logging, evals | ~$60 | ~$10 |
| Seats and Workspace | ~$80 | ~$15 |
| **Total excluding engineering** | **about $250–330** | **about $120–190** |
| Engineering | founder time, or $1,500+ if contracted | about $150–200 (one engineer) |

At 1,000 properties the software and AI cost is comfortably under the $560 benchmark. AI is not the cost problem; staffing is.

**90-day plan:**
- *Weeks 1–3:* policy file (CAV clocks and forms), case taxonomy, ledger schema, inbound capture.
- *Weeks 4–6:* PropertyMe adapter, maintenance and comms agents in shadow mode on a partner roll, commitment gate.
- *Weeks 7–9:* adversarial red-team suite, exception baseline, scheduler, arrears templates, privacy policy with ADM disclosures (live before 10 Dec 2026).
- *Weeks 10–13:* condition-report pilot, landlord report, migration runbook rehearsal, go or no-go on T1 autonomy for the first owned properties.
- *Cash spend:* about $15–25k (software, LLM, legal review of the autonomy policy and privacy policy).

## Questions I'd hand to other specialists

- **Regulatory/licensing:** can an unlicensed agent's representative approve T1 actions, or must the officer in effective control? Does AI-sent correspondence change supervision obligations under the Estate Agents Act 1980?
- **Legal/privacy:** does the small-business exemption apply in year one? Does voluntary APP compliance create liability? Is MCP access by PMs a "disclosure" to an overseas recipient under APP 8?
- **Operations:** what is the real time split of an incumbent Victorian PM (escalation vs routine)? I need it to size A1.
- **M&A/finance:** which PM systems do sub-scale sales-agency rolls in the target corridor run on? That drives migration cost and retention risk.
- **Distribution:** can the comparison funnel's rent-achieved data be licensed (Domain, Cotality) under AU-only processing terms, and at what cost?
