# Victorian Property & Consumer Law Counsel: red-team report

## Verdict
**Survives-if.** Nothing in Victorian law stops an AI-native, owner-operated PM agency. Three parts of the brief are built the wrong way round, though, and two of them hit revenue. (1) **Referral income from selling landlords is the biggest issue.** Under the Estate Agents Act 1980 (Vic) s 48A, an agent must pass to its client any "rebate" (defined to include a commission or other benefit) received "in relation to the sale, management or leasing" of the client's property. That plausibly takes in a referral fee a sales agent pays the landlord's own managing agent. Fiduciary and secret-commission law then sits on top. The "LAF embedded in a relationship" revenue line is uncertain until senior counsel says otherwise. (2) The founder cannot run or lead the agency unlicensed. The earliest he could hold an individual licence is about 12 months after he starts full-time work as an agent's representative. So a real officer in effective control (OIEC) is a gating hire, not an "open item". (3) An "arrears guarantee" that makes good lost rent is functionally rent-default insurance and must not be offered in that form.

## Attacks on the load-bearing assumptions

**A1. Referral fee on landlord sales (feeds Gate 3; High).** The brief treats this as "a disclosed referral fee". Disclosure alone is not enough:
- CAV's approved rebate statement says s 48A requires the agent to "immediately pay you any rebate they receive in relation to the sale, management or leasing of your property". The Court of Appeal has read "rebate" broadly to include commissions and non-monetary benefits [verified: CAV rebate statement form; Court of Appeal decision as reproduced in secondary commentary]. A fee from Agent X for steering *your managed landlord's* sale is arguably exactly that. If so, the landlord owns the money, not the founder.
- Even where s 48A does not bite, the founder's agency is the landlord's fiduciary under the management authority. Any benefit from a third party for advising that principal on selecting an agent needs fully informed consent. Without it, it is a secret commission: civil disgorgement plus Crimes Act 1958 (Vic) s 176 exposure [estimate: general fiduciary law; s 176 is the secret-commissions offence, but its exact elements are not verified here].
- Getting s 49A wrong is punished harshly. Courts have ordered agents to repay entire commissions (the reported $3M County Court refund) when authority disclosure requirements were not met exactly [verified: Mills Oakley / Point Partners commentary on the 2015–2018 cases].
- ACL s 18/s 29: if the agent shortlist is presented as "best for you" but is limited to agents who pay, that is misleading conduct.
- **What survives:** a separate written *agent-selection engagement*, signed by the landlord when they decide to sell. It states the fee amount, who pays it and the panel criteria, and records the landlord's express consent to the agency keeping the fee. Rebating part of the fee to the landlord turns the conflict into a selling point. Get a written senior-counsel opinion on s 48A before any revenue line depends on it. Until then, model referral income at zero in the base case.

**A2. Comparison funnel (feeds Assumption 3 and Gate 1; High).**
- ACCC comparator guidance (2015, still the operative guide as far as I can find) requires like-for-like comparison, disclosure of commercial relationships *even where they don't affect results*, and no ranking driven by commercial relationships [verified: ACCC comparator website guidance]. An operator ranking itself is the hardest case. A disclosure banner does not cure a methodology that systematically favours the house agency.
- "Rent achieved" by competitor is the riskiest data point. Victorian bond data is not published by agent, and scraped portal "leased" data breaches REA/Domain terms and sits on their database rights and copyright in listing content [estimate]. An unsound number published to steer landlords is a s 18/s 29 contravention and invites injurious-falsehood claims.
- Mystery shopping:
  - **Defamation.** A corporation with 10 or more employees cannot sue for defamation (Defamation Act 2005 (Vic) s 9), but many corridor agencies have fewer than 10 staff, and named individual PMs can always sue [verified: Defamation Act 2005 (Vic) s 9; employee-count reliance is an estimate].
  - **Injurious falsehood and ACL** claims remain open to large competitors.
  - **Recording calls.** Under the Surveillance Devices Act 1999 (Vic), a party may record their own conversation, but *publishing* a record of a private conversation is generally an offence (s 11) [estimate: recalled statute; check s 11 exceptions]. Never publish recordings or quotes. Publish only aggregate, timestamped, documented metrics.
- Severity is High because the funnel is the cheaper of the two acquisition channels. A challenge from a competitor or the ACCC would kill it at exactly the point it starts to work.

**A3. AI doing "transactional work" (feeds Assumption 1; Med–High).**
- AI has no legal status under the Estate Agents Act. Every act of estate agency is attributed to the licensee and supervised by the OIEC, who must take reasonable steps to make sure staff comply with the law [verified: CAV OIEC guidance].
- From 25 November 2026, agents' representatives must hold their own Business Licensing Authority (BLA) registration, and licensees and representatives must complete 5 CPD activities a year [verified: CAV "New rules: Estate agents and agents' representatives"]. The regulator is tightening individual accountability just as the model thins out the humans.
- Some acts are high-risk for automation. Notices to vacate, breach notices, rent-increase notices and bond claims have strict form, timing and evidence rules. A defective notice is invalid at VCAT. Since 25 November 2025, end-of-fixed-term no-reason notices are gone (RTA ss 91ZZD/91ZZDA repealed) [verified: Justice Connect HLIP; Domain]. Since the same reforms, bond claims must be supported by evidence [verified: CAV "No more unsupported bond claims"].
- **Rule:** the AI drafts and a human registered representative issues anything with legal effect. Count this as a "judgment exception" in the productivity metric, not as transactional work. My estimate is that it adds 5–15 exceptions per 100 properties per month, which goes straight into Assumption 1.

**A4. Service guarantees (Med; the arrears guarantee is High).**
- Fee-waiver guarantees ("if not leased in X days, no letting fee") are fine as long as they are honoured exactly and are not undermined by fine print. Unfair contract terms now carry civil penalties (since 9 November 2023) [verified: ACL amendments; well established].
- An **arrears guarantee** that pays the landlord rent the tenant fails to pay indemnifies against a third party's default. That is the core of landlord rent-default insurance. Carrying on insurance business without APRA authorisation is prohibited under the Insurance Act 1973 (Cth) [estimate: legal characterisation; needs advice]. Reframe it as a *process guarantee*: arrears notice within 24 hours, VCAT application by day X, fee refunded if the process is missed. Refer landlords to licensed landlord insurers instead, and note that taking commission on that referral needs AFSL authorised-representative coverage or an exemption.
- A **days-to-lease guarantee** creates a conflict. The cheapest way to hit it is to underprice the rent, which breaches duty to the landlord. Since 25 November 2025 it is also illegal to accept offers above the advertised rent [verified: CAV; Tenants Victoria]. The asking price therefore becomes the ceiling, which sharpens the conflict. Pair it with a "rent achieved within X% of agreed appraisal" metric.
- A **maintenance-cost guarantee** must not lead to deferring urgent repairs. Rental minimum standards apply before a property can be advertised [verified: multiple; commencement dates conflict between 25 Nov 2025 and 31 Mar 2026], and urgent-repair duties are strict.

**A5. Retention of acquired rolls (Assumption 4; Med).** Assigning management authorities on a rent-roll sale needs landlord notice. Most Victorian authorities let the landlord end the authority on short notice [estimate: standard REIV authority terms]. Two compliance points also affect retention:
- Every acquired authority must be re-papered with a compliant s 49A rebate statement. Inherited defective authorities put the commission entitlement at risk under s 50 [verified: CAV; case commentary].
- Due diligence must cover the vendor's trust-account audit history. CAV is suspending licences for audit failures [verified: CAV enforcement releases].

## Things the brief gets wrong, misses or understates
1. **"Bidding banned (Nov 2025)" is only half right.** Fixed-price advertising has applied since the 2021 reforms. The 25 November 2025 change banned *accepting* above-advertised offers and closed the remaining routes [verified: Premier's release; CAV]. Together with the abolition of end-of-fixed-term notices (also 25 November 2025), this materially lowers landlord control and raises investor exit pressure, which bears on attrition.
2. **"Standard application form, no fees (Mar 2026)."** Correct: commencement was 31 March 2026. The ban also covers RentTech platforms passing fees on. Penalties exceed $12,000 for businesses [verified: CAV; Premier]. Also missing from the brief: applicants may only be asked for what is in the form. That directly limits AI tenant screening, because no scraping social media and no extra data points are allowed.
3. **Agent's representative registration from 25 November 2026**, three weeks from today, is missing from the brief. Every PM and field inspector who performs agency functions needs BLA registration, a fee and CPD. Using cheaper field staff for condition reports and inspections almost certainly makes them agents' representatives [estimate]. Budget for registration and CPD per head.
4. **Consumer Legislation Amendment Bill 2026** was before Parliament (Legislative Council amendments in August 2026). It gives the BLA power to suspend licences for trust-audit non-compliance and includes other Estate Agents Act changes [verified: REIV summary; legislation.vic.gov.au amendment schedule]. Its passage status is time-sensitive; check before acquiring.
5. **Privacy is understated.** The brief only mentions automated decision-making (ADM) transparency, but there are four separate points:
   - The small-business exemption (turnover of $3M or less) is lost by anyone who discloses personal information for a benefit unless the individual consents [verified: Privacy Act s 6D; OAIC]. Selling-landlord referrals for a fee do exactly that.
   - New APP 1.7–1.9 (ADM transparency) apply to decisions made from **10 December 2026**, whenever the system was built. OAIC guidance was released on 30 September 2026 [verified: OAIC; Maddocks; White & Case]. Rental application assessment clearly "significantly affects" an individual.
   - The statutory privacy tort is now in force [estimate: commenced June 2025].
   - The Equal Opportunity Act 2010 (Vic) applies to discriminatory screening outcomes, including those produced by models.
6. **Strata claims need correction.** The 3-year cap on owners corporation manager terms is right (OC Act s 119(1D); 5 years for retirement villages) [verified: CAV factsheet; Law Handbook]. Removal is via s 119(6), revocation "at any time"; "simple majority" means an ordinary resolution per commentary and is unverified against the statute. The current regime is **registration** with the BLA plus PI insurance. A full licensing scheme is government-supported and was introduced into Parliament in mid-2026, with commencement uncertain [verified: LC Lawyers; LookUpStrata]. An OC manager business needs its own registration separate from the estate agency, its own trust arrangements, and a Chinese wall where the same firm both manages the building and markets rental management to owners. I found no verified Victorian ban on insurance commissions yet; it is "consulting" only.
7. **AI-altered listing images.** Victoria has no AI label rule, but existing misleading-advertising rules cover enhanced photos and CAV is actively investigating. NSW requires disclosure (fines up to $22k) [verified: news reporting]. If the platform is meant to cross state lines, build disclosure in by default.

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| Rental bidding banned Nov 2025 | Ban on accepting above-advertised offers commenced 25 Nov 2025; fixed-price advertising since 2021 | verified: CAV, Premier VIC, Tenants Vic |
| Standard application + no rent-payment fees Mar 2026 | 31 Mar 2026; business fines >$12k | verified: CAV, Premier |
| End-of-fixed-term NTV | Abolished 25 Nov 2025 (ss 91ZZD/91ZZDA repealed) | verified: Justice Connect, Domain |
| Agent's rep registration | Mandatory BLA registration from 25 Nov 2026; 5 CPD/yr | verified: CAV |
| Individual licence experience | ≥1 yr full-time as agent's rep in Vic within last 3 yrs | verified: CAV licence page |
| Licence education | Diploma (CPP51122) vs Cert IV units: sources conflict | unverified, check CAV |
| Trust audit | Annual audit by approved auditor; within 3 months of FY end; lodge within 10 business days; up to 120 penalty units | verified: CAV |
| ADM transparency | APP 1.7–1.9 from 10 Dec 2026 | verified: OAIC, law firms |
| OC manager contract cap | 3 years (s 119(1D)); revocable any time (s 119(6)) | verified: CAV factsheet; "simple majority" unverified |
| OC manager licensing | Registration now; licensing introduced mid-2026, timing uncertain | verified (secondary) |
| ACCC comparator rules | Disclose commercial relationships; no commercially driven ranking | verified: ACCC 2015 guide |
| Defamation: corporations | 10+ employees can't sue | verified: Defamation Act 2005 (Vic) s 9 |

## Improvements (ranked by impact)
1. **Hire or partner the OIEC before anything else.** It must be a real, full-time licensed agent at the principal office with property-management depth. Avoid "rent-a-licence", which is a known CAV enforcement target. Offer equity with vesting. The founder should register as an agent's representative now (Cert IV units, myCAV, after 25 Nov 2026) and pursue his own licence after 12 months of full-time representative work. That makes Q4 2027 to Q1 2028 the earliest he could be OIEC [estimate].
2. **Rebuild the referral line.** Run it through a separate agent-selection engagement with express informed consent and a s 48A opinion. Disclose the fee, rebate part of it to the landlord, and keep panel criteria public. Model it at zero until counsel clears it. Gate 3 ("half of sellers sell through the founder") should be measured on *consented engagements*.
3. **Separate the comparison site from the agency.** Use a different entity and publish the methodology. Rank by landlord-chosen criteria, label the house agency as "our agency", and exclude it from default ranking or show it in a fixed, labelled slot. Use only data you have a right to use: mystery-shop outputs as aggregate metrics with methodology and right of reply, no recordings, and no "rent achieved" unless sourced from consented landlord data. Get ACL and defamation legal review before launch, and buy media-liability insurance.
4. **Rewrite the guarantees as process and fee-refund guarantees.** Drop any indemnity for tenant default. Add a rent-achieved metric to balance days-to-lease.
5. **Human sign-off register.** Every notice, bond claim, VCAT application, rent increase and application decision is issued by a named registered representative, with AI drafts logged. This becomes the evidence base for "reasonable steps" by the OIEC.
6. **Privacy-by-design now.**
   - Opt in to the Privacy Act (s 6EA), or assume the exemption is lost because of referrals.
   - Publish an APP 1.7-compliant ADM statement by 10 December 2026.
   - Screen only on standard-form fields and keep a human decision on every application.
   - Adopt a retention and destruction policy for unsuccessful applications.
7. **Acquisition due-diligence checklist.** Cover trust audit history, s 49A compliance of every authority, CAV complaints, bond reconciliation and the reconciliation of the trust ledger to the bank at cut-over. Build re-papering of authorities into the deal, and tie part of the retention holdback to how many landlords sign.

## Tests & kill criteria
| Test | Metric | Threshold | Timeframe |
|---|---|---|---|
| s 48A/fiduciary opinion on referral fee | Written opinion | If the fee must be paid to the landlord, or is unworkable with consent, remove it from the model and recut Gate 3 | 4–6 weeks, ~$8–15k [estimate] |
| OIEC search | Signed, qualified OIEC | No credible OIEC in 4 months: kill or switch to buying a licensed agency with its licensee | 4 months |
| Comparison-site pre-launch review | ACL and defamation sign-off on methodology; rival complaint rate | Any credible legal letter on methodology in first 90 days → pause and fix; two → drop the self-listing | 90 days post-launch |
| Notice-accuracy audit | % of AI-drafted notices needing human correction | >5% after 3 months → the role split must keep humans, not AI, on legal documents | First 100 properties |
| Consent rate for selection engagement | % of selling landlords signing the disclosed engagement | <30% → referral line not viable | First 20 sellers |

## Answers to open items in my domain
- **Licensed operator / co-founder: who.** A licensed estate agent with at least 5 years of property management, trust-account experience, a clean CAV record, and willingness to be OIEC full-time at the principal office. A licensee from a sub-scale roll being sold is ideal, because the acquisition then brings the OIEC with it. The founder can be director and shareholder; the BLA assesses directors' fitness. Without registration, the founder must not negotiate leases, appraise rents for reward, collect rent or sign authorities.
- **What the founder can do unlicensed:** capital, technology, ops design, comparison-site publishing (with care), hiring, and lender relationships. He cannot do client-facing agency work.
- **Minimum platform:** a compliant trust ledger is non-negotiable from day one (PropertyMe or similar), with audit-ready reconciliation. Crossub as back office does not shift licensee liability. The licensee remains responsible for the trust account and every act done in its name [estimate].
- **Strata model (legal side):** separate OC manager registration and PI cover, terms of 3 years or less, no automatic rollover via AGM restarts (commentary flags this as an unlawful extension), and disclosure of any insurance commissions now in anticipation of a ban.
- **Kill criteria:** see the table above.

## Questions I'd hand to other specialists
- **Finance/unit economics:** remodel with referral income at $0 and at 50% rebated. Add per-head BLA registration and CPD, trust-audit fees (~$3–8k/yr [estimate]), media-liability and PI premiums, and an OIEC salary of $150k+.
- **Rent-roll M&A:** how often do Victorian rolls carry defective s 49A authorities? Price re-papering attrition into the multiple.
- **Insurance broker:** structure for an arrears product through a licensed insurer, and whether AFSL authorised-representative status is worth having.
- **Ops/AI:** realistic count of exceptions with legal effect per 100 properties per month once notices and screening stay human.
- **Growth:** can the funnel work with the house agency *excluded* from default ranking?
- **Data:** a lawful source for competitor "rent achieved" data (consented landlord uploads? licensed Cotality/PropTrack feeds?).
