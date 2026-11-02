# Agentic AI Expert: red-team report

## Verdict
**Survives if the plan stops counting on "autonomy" as the edge.** Autonomously managed rentals are not here in late 2026, and they won't be by 2029. What is here is **act-and-report (L3) autonomy on about half of task *volume*, but under 20% of task *risk***. The binding constraints are write access to systems of record, the physical world, statutory accountability and liability. Model capability is not the binding constraint. Inference costs about $15–40 per property per year, so compute is not the issue. The cost is the **human exception queue**. The biggest issue: vendors (PropertyMe's agentic AiMe, EliseAI's Apollo, Tapi) will ship the same L3 autonomy to every agency. The one agentic advantage a vendor can't sell is **an agent that runs a risk book the operator owns**: the maintenance flat fee priced and controlled on your own job-outcome data. That is also where an agent is most likely to break the law, by deferring repairs to protect margin.

## Verdict on the platform thesis
- **Carries the economics (from my lens), in order:**
  1. **PM with measured L3 autonomy on communications and maintenance.** This is a cost floor, not a moat: parity with incumbents within 12–24 months.
  2. **The maintenance flat fee as an agent-operated risk book.** It is the only service where autonomy, the data loop and the founder's statistics combine into something not for sale. Launch only after about 12 months of your own job data. Before that you are pricing blind.
- **Cheap to add, low autonomy risk:** investment-support analytics (L1 reports a human sends). Building them is easy; the value depends on distribution, not AI.
- **Weak from an agentic lens:**
  - Tenant evaluation as a product. The Mar 2026 standard form limits the inputs, and APP 1.7 automated-decision disclosure (from 10 Dec 2026) plus anti-discrimination exposure keep it at L2 permanently.
  - Tenant equity and home-buying services. They are regulated advice and credit; autonomy adds little and adds liability.

## Attacks on the thesis

**A1. The "autonomous rental" framing is wrong today and in 2029. Severity: High.** Decomposed below (25 task types), the realistic frontier is:
- **L3 on high-volume, low-stakes, reversible work:** enquiries, FAQs, scheduling, maintenance intake and triage, reminders.
- **L2 on anything with money, legal notices, selection or evidence.**
- **L0–L1 on VCAT, bond disputes and the physical world.**

The licensed officer in effective control remains accountable for what agents do. A defensible claim is "a named PM supervises a machine that does 80% of keystrokes". "Unmanned" is not a defensible claim. Lead with that, which also fits the 36% AI-trust finding.

**A2. Autonomy is being commoditised faster than the brief assumes. Severity: High.**
- EliseAI launched Apollo, "an agentic AI teammate" that completes tasks end-to-end inside the customer's PMS (3 Sep 2026). It reports $200M ARR and coverage of 1 in 6 US apartments, and raised $350M at a $4B valuation (Sep 2026) **[verified: SiliconANGLE/TechCrunch coverage, company claims]**.
- PropertyMe (about 6,500 agencies, about 2M properties) shipped AiMe Connect and says "Agentic AiMe is coming next" (no date) **[verified: Elite Agent / Proptech Connect]**.
- Tapi claims AI maintenance triage and dispatch across 160k–400k+ ANZ properties **[verified: vendor/trade press; scale unverified]**.

Conclusion: by about mid-2027 an ordinary PropertyMe + Tapi agency can buy L3 maintenance intake and L2 dispatch. Your desk-cost advantage over that agency is perhaps 15–25%, not 2x **[estimate]**.

**A3. Compounding error kills long autonomous workflows unless they are segmented. Severity: High.**
- End-to-end success equals per-step success to the power of the step count: 0.98²⁰ = 0.67; 0.99²⁵ = 0.78; 0.995²⁵ = 0.88; 0.999²⁵ = 0.975 **[calculation]**.
- A re-let (vacate notice → bond → condition report → listing → enquiries → inspections → selection → lease → bond lodgement → ingoing report) is 25–40 steps.
- Frontier agents' reliable horizon (80% success) is about 3–4 hours of expert-equivalent work, versus 16–20 hours at 50% **[unverified: METR figures via secondary sources]**. A re-let spans weeks of wall-clock time and dozens of counterparties.
- The fix is architectural: short agent episodes between **deterministic checkpoints** (a state machine owns the workflow; agents own the steps), verification after every write, and idempotent retries. Never let one agent "run the re-let".

**A4. Computer-use agents on PropertyMe and portals are a trap for writes. Severity: Med.**
- On the OSWorld-Verified benchmark, frontier computer-use scores are about 83–85%, against a 72% human baseline **[unverified: aggregators; leaderboard conflicts]**. Even at 85%, roughly 1 in 7 tasks fails, which is unusable for anything touching trust money or notices. Tool-calling over APIs is far more reliable than driving a screen.
- PropertyMe's partner API reportedly allows **job writes (create/approve/assign/complete) but tenancies are read-only, and there are no webhooks** (polling only) **[unverified: third-party API catalogue; confirm with PropertyMe]**.
- Recommended split:
  - Maintenance runs through the API. No computer-use is needed.
  - Use computer-use only for read/extract tasks and low-stakes portals, such as checking a bond status or downloading council rates, and always with a post-condition check.
  - The trust ledger, disbursements and rent changes stay human-keyed or human-approved in the PMS.
  - Computer-use against PropertyMe's UI may also breach its terms of service. Check before building.

**A5. The flat-fee maintenance book creates an agent alignment problem with statutory teeth. Severity: High.**
- If the operator absorbs repair cost, every triage agent optimised on "cost per job" learns to defer, downgrade urgency or push "renter-caused" classifications.
- Victoria puts repair duties on the rental provider. It also lets the renter commission urgent repairs up to $2,500 and claim reimbursement within 7 days **[verified: CAV urgent repairs]**. Minimum standards and rental minimum energy standards (from 1 Mar 2027) add hard obligations.
- A systematically mis-tuned agent breaches at portfolio scale, and the logs prove it.
- Design rule:
  - The **urgency classifier and the statutory clocks must sit outside the cost-optimising loop**. They are separately evaluated and can only escalate, never de-escalate on cost.
  - Repair-or-replace and "renter fault" decisions stay L2 with a human sign-off.
  - Report "deferred jobs" as a red metric.

**A6. AI-generated condition reports are now a litigation target. Severity: Med.**
- Since Oct 2026, bond claims need evidence. Advocates explicitly cite "AI-created inaccurate condition reports" as a target of the reforms **[verified: CHOICE]**.
- Video-to-report tools exist (ConditionIt; SnapInspect's AI-assisted reports) **[verified: vendor sites; accuracy unverified]**.
- Use them for drafting (L1–L2): the AI drafts from timestamped video and an inspector or PM certifies it. The video stays the evidence and the report is an index into it. That is a better evidentiary position than today's photo reports, and it is also the strongest honest "AI" story to tell renters.

**A7. Automated-decision transparency. Severity: Med (time-sensitive: 10 Dec 2026).**
- APPs 1.7–1.9 require privacy-policy disclosure where a program makes, or substantially assists, decisions that significantly affect individuals. OAIC guidance came out around 30 Sep 2026 **[verified: Allens, GT Law commentary; OAIC page]**.
- Applicant ranking, rent setting, arrears escalation and bond claims all qualify.
- This is manageable (disclosure plus human review), but it rules out "black-box autonomous selection" as a selling point.

## Things the brief gets wrong, misses or understates
1. **"AiMe Connect is read-only" is true, but irrelevant to your build.** The relevant fact is the *partner* API's write surface (jobs, yes; tenancies and ledger, no) and its lack of webhooks. Polling latency (minutes) caps how responsive "real-time" autonomy can be. Plan for an event store of your own.
2. **Compute cost is a rounding error.** On current list prices:
   - Claude Sonnet 5.5 is $2/$10 per MTok (cache reads $0.20); Opus 5.5 is $4/$20; Haiku 5.5 is $0.10/$0.50 **[verified: Anthropic pricing as cached 6 Oct 2026]**.
   - A typical triage or drafting call is about $0.05 on Sonnet and about $0.09 on Opus **[estimate: 8k fresh + 30k cached input, 2.5k output]**.
   - About 150 calls plus about 30 voice minutes per property per year comes to **$15–40/property/yr** **[estimate]**, against $430–580 for offshore-VA incumbents.
   - **The unit of cost is the human exception, not the token.**
3. **Voice agents are ready for intake, not for the whole job.** All-in voice-agent cost is about A$0.10–0.45/min **[unverified: US$0.07–0.31/min, vendor-adjacent blogs]**. After-hours tenant intake and trade scheduling are L3-ready now. Emergencies (gas, flooding, electrical, security) must route by deterministic rules to a human on-call within minutes, whatever the model thinks.
4. **The data loop is smaller than "data and AI" implies.** At 500 properties you see about 1,000–1,500 maintenance jobs a year **[estimate: 2–3 jobs/property/yr]**. That is enough to learn the cost distributions by category, but not property-level pricing. You need pooled priors (several acquired books' 3-year job histories, insurer or trade data) before the flat fee is underwritable.
5. **The brief misses model-change risk.** Models and prices change every 3–6 months, often with breaking API changes. Without a regression eval harness, each upgrade is an uncontrolled change to a regulated process.

## Numbers checked

| Claim | Finding | Status/source |
|---|---|---|
| PropertyMe has agentic AI | AiMe Connect (Claude/ChatGPT on live data) from 8 Oct 2026; "Agentic AiMe coming next", no date | verified: Elite Agent, Proptech Connect |
| PropertyMe scale | ~6,500 agencies, ~2M properties, 35k users | verified (company claim via trade press) |
| PropertyMe API write access | Jobs writable; tenancies read-only; no webhooks | unverified: third-party API catalogues |
| EliseAI agentic | Apollo (3 Sep 2026); $200M ARR; 1 in 6 US apartments; $350M @ $4B | verified: press coverage of company claims |
| Tapi footprint | 160k → "400k+" properties ANZ, AI triage | verified vendor claim; scale unverified |
| Computer-use reliability | OSWorld-Verified top ~83–85% vs human 72.36% | unverified (aggregators conflict) |
| Agent time horizon | 50% horizon ~16–20 h; 80% ~3–4 h; doubling ~4 months post-2023 | unverified (secondary reports of METR) |
| LLM pricing | Sonnet 5.5 $2/$10; Opus 5.5 $4/$20; Haiku 5.5 $0.10/$0.50 per MTok (USD) | verified: Anthropic, cached 6 Oct 2026 |
| Voice agent cost | US$0.07–0.31/min all-in | unverified (vendor-adjacent blogs) |
| Urgent repairs | Renter may spend ≤$2,500 incl. GST; reimbursed within 7 days | verified: CAV |
| ADM transparency | APP 1.7–1.9 from 10 Dec 2026 | verified: Allens, GT Law, OAIC |
| Compute per property | $15–40/yr | estimate (above) |

## Autonomy grid (today late 2026 → 2027 → 2029; binding constraint)

| # | Task | Now | 2027 | 2029 | Binding constraint |
|---|---|---|---|---|---|
| 1 | Rental enquiries, inspection booking | L3 | L4 | L4 | trust |
| 2 | Tenant FAQs/general comms | L3 | L3 | L4 | trust, tone liability |
| 3 | Maintenance intake (chat/voice) + triage | L3 | L3 | L4 | emergency safety |
| 4 | Trade dispatch within landlord-approved limit | L2 | L3 | L3 | API write; liability |
| 5 | Quote collection/comparison | L2 | L3 | L3 | trade adoption |
| 6 | Trade price negotiation | L1 | L2 | L3 | trust, relationships |
| 7 | Invoice matching → bill entry | L2 | L3 | L3 | ledger access (by design) |
| 8 | Trust disbursements/reconciliation | L1 | L2 | L2 | law (trust account), liability |
| 9 | Rent arrears reminders | L3 | L3 | L3 | law (notice form) |
| 10 | Breach/vacate notices | L1 | L2 | L2 | law, VCAT evidence |
| 11 | VCAT/RDRV preparation | L1 | L1 | L2 | law, advocacy |
| 12 | Application processing/verification | L2 | L2 | L3 | standard form, fraud |
| 13 | Applicant selection | L1 | L1 | L1 | anti-discrimination, APP 1.7 |
| 14 | Rent setting / increase notices | L1 | L2 | L2 | excessive-rent test, landlord sign-off |
| 15 | Lease renewal offers | L2 | L3 | L3 | landlord consent |
| 16 | Listing copy/photos | L3 | L3 | L4 | misleading-ad law |
| 17 | Entry/ingoing condition report from video | L1 | L2 | L2 | evidence law, physical world |
| 18 | Routine inspection report | L1 | L2 | L2 | physical world |
| 19 | Bond lodgement/claims | L1 | L2 | L2 | evidence rules, portal access |
| 20 | Compliance (gas/electrical/smoke/MES) scheduling | L2 | L3 | L4 | data completeness |
| 21 | Owner monthly reporting | L3 | L4 | L4 | — |
| 22 | Owner decision advice (repair vs replace, hold/sell) | L1 | L1 | L2 | advice liability, trust |
| 23 | Key handling, physical access | L0 | L0 | L0 (smart locks: L2) | physical world |
| 24 | Complaint handling/escalation | L1 | L2 | L2 | trust |
| 25 | Landlord acquisition/onboarding | L1 | L2 | L2 | relationships, licensing |

Roughly 45–55% of interaction volume is L3-capable today; under 20% of dollar-at-risk is **[estimate]**.

## Improvements (ranked by impact)
1. **Make the maintenance risk book the AI-native core, not "autonomous PM".**
   - Own dispatch through a contracted trade panel with structured job outcomes: cause code, parts, labour time, recall within 90 days, photo before/after.
   - That outcome data is the proprietary loop. Vendors sell triage; none hold the fee risk.
2. **Architecture: a state machine owns the workflow, agents own the steps, a policy engine owns permissions.**
   - Components:
     - an event store fed by PMS polling and inbound channels;
     - a case log;
     - a workflow engine with statutory clocks;
     - an agent runtime: Haiku-class for classification, Sonnet-class for drafting and tools, Opus-class for exceptions;
     - a tool gateway that classes every tool as Read / Reversible write / Irreversible / Money / Legal, with autonomy granted per (task × class × confidence);
     - a human queue with diff-view one-click approval;
     - voice on a managed platform calling the same tools.
   - Set Australian inference geography where available. APP 1.7 notices go live before 10 Dec 2026 if any pilot runs.
3. **Eval harness before autonomy.**
   - Golden sets of ≥300 labelled cases per task type, built from the round-1 shadow-test data.
   - Every model or prompt change must pass a regression gate.
   - 5% random human audit of L3 actions.
   - Canary rollout per task type, a kill switch per task type, and 5–10 minute undo windows on outbound messages.
4. **Separate the safety evaluators from the cost optimisers (A5).** The urgency, habitability and statutory-deadline classifiers are evaluated on recall (target ≥99.5% on emergencies). Cost models never see their override.
5. **Buy, don't build: voice, computer-use and video-to-report.** Your edge is orchestration, evals and pricing.

## 6-month autonomy roadmap (from shadow data now through the first acquired book)

| Month | Milestone | Measurable target |
|---|---|---|
| 1–2 (Nov 26–Jan 27) | Replay harness on partner-agency PropertyMe export; golden sets for 6 task types (1, 2, 3, 5, 9, 21) | ≥300 labelled cases per type; baseline desk-minutes per 100 properties/month measured |
| 3 | L1 drafts live in partner agency (co-brand) | ≥75% of drafts sent unedited or with minor edits; 0 statutory-clock misses |
| 4 | L3 on enquiries, FAQs, intake, reminders, owner reports; voice after-hours intake | Customer-visible error ≤0.5% of L3 actions; emergency recall 100% on test set, ≥99.5% live; first response <5 min |
| 5 | L2→L3 dispatch inside landlord limits via API; video-assisted condition reports at L1 | ≥60% of jobs dispatched without staff touch beyond one click; recall-within-90-days tracked |
| 6 | Exception-rate review; decide L3 expansion | Desk ≤40 h/100 properties/month (round-1 gate) and trending to ≤30 h; exceptions ≤25% of cases; compute + voice ≤$40/property/yr |

## Tests & kill criteria
| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| Shadow replay (round-1 test, extended) | Draft acceptance; simulated desk-minutes | Kill the autonomy edge if acceptance <60% or >55 h/100 properties/month | 6 weeks, ~$15k |
| Vendor parity check | Same tasks run on PropertyMe AiMe / Tapi / EliseAI-class tools | If vendor stack gets within 15% of your minutes, stop building commodity agents; build only the risk-book layer | 8 weeks |
| Maintenance predictability | 3-yr job ledgers from 2–3 books; predict next-year cost per property | MAE ≤35% of mean at segment level, else flat fee needs caps/pooling or dies | 8 weeks |
| Emergency triage | 1,000 replayed + synthetic calls | 0 missed emergencies; ≥95% correct urgency class | 4 weeks |
| Computer-use reliability (portal reads) | 200 runs with post-condition checks | ≥98% verified success, else human | 2 weeks |

## Answers to the round-2 questions in my domain
- **Q4 (feasibility and frontier):**
  - Technically, L3 on the transactional half now; L3 on dispatch, renewals and compliance by 2027; L2 ceiling on money, notices, evidence and selection through 2029.
  - Legally, a licensee stays accountable; APP 1.7 from 10 Dec 2026; no "fully autonomous" agency before 2029.
  - Physical tasks are unchanged unless smart locks and contracted field inspectors are adopted.
- **Q1:** PM (autonomy as the cost floor) first, then the maintenance risk book once ≥12 months of your own outcome data exist.
- **Q5 (founder edge):**
  - **Decisive:** eval and measurement design, exception economics, actuarial pricing of the maintenance book, and the CFO view of cost per completed task.
  - **Irrelevant:** model capability, voice and computer-use infrastructure (all bought), and "having AI" (everyone will).
- **Q2:** autonomy moves cost, not lifetime value. A realistic 2029 desk floor of about 15–25 h/100 properties/month **[estimate]** is reachable by everyone, so it doesn't change the scale needed for $500k. Only the risk-book margin does.
- **Q6:** the predictability test plus the vendor-parity test, about 10 weeks for under $30k. If maintenance cost isn't predictable and vendors match your minutes, the "AI-native" premium is gone.

## Questions I'd hand to other specialists
- **Insurance/APRA:** is a fixed-fee repair absorption "insurance" when the operator also controls the repair decision? Does that change if a trade panel carries the risk?
- **Tenancy lawyer:** does an AI-drafted, human-certified video condition report meet the Oct 2026 bond-evidence standard? Are emergency-repair SLAs enforceable against an automated triage failure?
- **PropertyMe partnerships:** is write API access to jobs guaranteed for a competitor-operator, and what are the ToS on UI automation?
- **Actuary:** what minimum pooled job data supports pricing by age, type and condition at ±20%?
- **Privacy counsel:** what APP 1.7 wording covers triage, arrears escalation and applicant shortlisting?
