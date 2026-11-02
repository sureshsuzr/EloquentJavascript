# Tenancy, Consumer & Privacy Counsel (Victoria): red-team report

*Method note: consumer.vic.gov.au and several law-firm sites were not reachable from the session. The shared web-search budget also ran out before I finished. Victorian points therefore rest on search summaries of CAV, Tenants Victoria, AustLII headings and law-firm commentary. Section numbers marked [estimate] must be checked against the consolidated Residential Tenancies Act 1997 (RTA) before anyone relies on them.*

## Verdict
**Survives-if, and only as a landlord-side platform.** The landlord-side services are lawful inside the licensed agency with disclosure: PM, tenant selection, investment analytics, and a maintenance programme the landlord pays for. The tenant-side "super app" does not survive in the form the brief describes. The single biggest issue is that **renter data is legally purpose-locked and time-limited by statute**:
- Since 31 March 2026, applicants can only be asked for what the standard form allows.
- An unsuccessful applicant's data must be destroyed or permanently de-identified within 30 days (6 months with written consent).
- A renter's data must be destroyed within 3 years after the tenancy ends.
- Any compulsory charge to a renter is banned.

The thesis assumes that tenant data and tenant wallets flow freely into scoring, cross-sell and credit. They don't. A renter can only be served as a *separately consented customer of a separate entity*, never as a by-product of the tenancy.

## Verdict on the platform thesis (which services carry the economics, from my lens)
- **Carries the economics, low legal friction: landlord-paid investment support.** This means portfolio analytics, hold/sell/refinance, and buying the next property. The landlord is already the client, and advice about real property is not a financial product. Refinancing runs through a licensed broker under the NCCP referrer exemption, with the fee disclosed. Buying runs through a separate buyer's-agency engagement.
- **Second: a maintenance programme paid 100% by the landlord.** It is legal if structured as a service contract with no incentive to under-repair (insurance characterisation is for the insurance specialist). **Any split charged to the tenant is unlawful**, so delete it.
- **Tenant evaluation is not a separate product.** As a priced product it collapses into the letting fee. Selling scores outside the agency's own lettings creates a de facto tenancy database, puts the operator in data-broker territory and creates Equal Opportunity Act exposure, all for small revenue.
- **Tenant-side services are a CAC-reduction channel, not a profit centre.** They should be mostly free to the tenant and monetised, if at all, through licensed third parties with consent. Their legal value is mainly as a retention moat for landlords: a better tenant experience means longer tenancies.

## Attacks on the thesis

**A1. The tenant data asset is mostly illegal to build (High).**
- **Information limits:**
  - From 31 March 2026 a prescribed standard application form is mandatory. Asking for information outside it carries maximum penalties of more than $62,700 for a company and $12,500 for an individual [verified: law-firm summary via search; CAV].
  - CAV forced Reapit's 2Apply to strip "optional" questions in 2026, and warned agents that still ask them [verified: CAV media release via search].
- **Destruction and de-identification:**
  - Unsuccessful applicant: within 30 days after the property is leased to someone else, or 6 months with written consent to be considered for other properties.
  - Successful renter: within 3 years after the tenancy ends.
  - These rules sit in the RTA's renter-information provisions (s 505BA onwards) [verified: CAV page and standard form via search; section range estimate].
- **What this does to the model:**
  - Rejected applicants vanish, so you can never observe how they would have performed. Every risk model is trained only on accepted tenants (the reject-inference problem).
  - The panel resets every 3 years.
- **Lawful route:** permanently de-identify records at the deadline into a training store. That is defensible only if re-identification is genuinely impractical. Address-level rent, arrears and maintenance histories linked to a property are re-identifiable, so this needs a documented de-identification standard.
- **Purpose limit:** the RTA requires agents to protect renter information "from misuse". Whether it limits *use* to tenancy purposes, as well as retention, I could not confirm from the text [unverified]. Assume it does.

**A2. Any compulsory charge to renters is banned, including the maintenance fee split (High).**
- RTA s 51 prohibits certain charges. s 51A prohibits application fees and rent-payment fees, including fees charged by third-party rent-tech platforms [verified: Tenants Victoria section list; CAV; Premier].
- s 42 requires a fee-free rent payment method [verified: AustLII s 42 snippet].
- Background checks are at the agent's cost [verified: CAV via news].
- Repair duties sit with the rental provider. Shifting them by agreement would be a prohibited term (s 27B) and/or a prohibited charge [estimate: s 27B listed as an offence by CAV; its fit to maintenance is my reading].
- **Consequence:**
  - A "maintenance fee split with tenants" is unlawful as a term of the tenancy.
  - Any tenant product offered during the application, or bundled with the lease or rent payment, will be treated as a disguised fee.
  - The Renting Taskforce has issued 250 warnings, 130 infringements and about $900k in fines, and started 11 court actions (as at 27 Aug 2026) [verified: Premier/CAV].
  - New rent-tech business models are exactly its target.

**A3. Conflicts: serving the renter while acting for the landlord (High for some combinations, manageable for others).**
- CAV's own guidance names acting for both landlord and tenant, or seller and buyer, as conflict-of-interest examples under the Estate Agents (Professional Conduct) Regulations 2018 [verified: CAV "Acting for a client" via search]. The managing agent is the landlord's fiduciary. The renter is a "consumer" owed fair dealing, not loyalty.
- The danger runs in both directions:
  - **Landlord harmed:** the agency earns from the renter (savings, broking, moving), so it goes soft on arrears, bond claims or rent reviews.
  - **Renter harmed:** the agency uses what it learned through a tenant product (savings balance, income growth, pre-approval amount) to set rent increases or to time a sale. That is misuse of confidential information. It is arguably unconscionable under the ACL and a privacy breach.
- **This is the disqualifying combination: renter financial data reaching the rent-setting or landlord-advice function.** It must be architecturally impossible, not merely forbidden by policy.

**A4. Selling the landlord's property to the sitting tenant (High if one entity acts for both).**
- The PM agency is the landlord's agent. If the same group also acts as the tenant's buyer's agent or finance helper on that property, it is dual agency on price, which is the core term.
- s 55 Estate Agents Act (agent or associate acquiring an interest) is also engaged if any related entity takes a position [verified: REIV description of s 55].
- s 48A applies: any benefit received in relation to the sale of the client's property must be passed to the landlord [round 1, verified].
- **Survivable version:**
  - The agency acts for the landlord only and introduces the tenant as a prospective buyer, with written disclosure.
  - The tenant is told in writing that the agency acts for the vendor and is advised to get independent representation.
  - No group entity represents the tenant on that transaction.
  - The tenant's platform data is never used for the vendor's negotiation.
- This is commercially attractive anyway: no vacancy, no campaign and no vendor advertising spend. It is also the best use of the "independence from sales" edge.

**A5. Steering a renter to another managed property (Med).**
- For applicants: lawful with the standard form's written consent to be considered for other properties, which also extends retention to 6 months.
- For sitting renters: the agency owes Landlord A loyalty. Soliciting A's good tenant to move to Landlord B's property, or using A's tenancy data to target them, breaches that duty.
- **Rule:** only respond to a renter-initiated move, after notice has been given, and tell both landlords.
- Since 25 November 2025, end-of-fixed-term no-reason notices are gone [verified: round 1], so periodic tenancies are long. That makes the "move within the portfolio" funnel structurally smaller than the brief implies.

**A6. Using tenant data for credit and "equity" products (High for credit and deposits, Med for rent-history evidence).**
- Moving a renter's details into a broker's pipeline requires either:
  - the NCCP reg 25 referrer exemption, which is narrow: incidental referral, commission disclosed, and no "suggesting" a particular product [verified: Bright Law, MFAA via search]; or
  - credit-representative status.
- Savings and deposit features are financial products. They need an ADI partner and an AFSL, or authorised-representative cover.
- **"Rent history as credit evidence":**
  - Rent is not consumer credit. A credit reporting body cannot hold rent payments as repayment-history information under Part IIIA [estimate: Part IIIA definitions]. Opt-in services such as PaymentReport exist, but their bureau acceptance is unverified [unverified]. A pilot of rent data in mortgage scoring has been reported (Regulation Asia, paywalled) [unverified].
  - Lawful version: a renter-controlled, downloadable verified rent ledger that the renter chooses to share. It is cheap and has no licence issue.
  - Unlawful version: the agency pushing tenant payment data to lenders or bureaus without express consent.
- **Tenancy-database risk:** a cross-landlord "tenant score" shared outside the agency's own lettings is functionally a residential tenancy database. The RTA's database rules then apply: listing only for specified breaches, notice to the renter, limits on how long a listing stays [estimate: RTA database part; not re-verified this round].

**A7. Equal Opportunity Act risk in scoring (High).**
- Discrimination in accommodation covers applying, occupying and leaving. Indirect discrimination (s 9) arises from an unreasonable requirement or practice that disadvantages an attribute group, and motive is irrelevant (s 10) [verified: EO Act table of contents; CAV].
- Victorian attributes include age, disability, employment activity, parental and carer status, race and others [verified: CAV list].
- Proxies such as income source (Centrelink correlates with disability, age and carer status), household composition, postcode, employment type, gaps in rental history and "stability" features will produce disparate impact.
- The s 15 positive duty to take reasonable and proportionate measures to eliminate discrimination applies to the agency [estimate: s 15 scope].
- The landlord, the agency and a scoring vendor can each be liable (authorising or assisting provisions) [estimate].
- Commonwealth Disability, Racial and Age Discrimination Acts apply in parallel.

**A8. Federal privacy (High from 10 December 2026).**
- **ADM transparency:** APP 1.7–1.9 require the privacy policy to disclose substantially automated decisions that significantly affect individuals and the kinds of personal information used. This applies from 10 December 2026; OAIC guidance was issued 30 September 2026 [verified: Maddocks, Allens, White & Case via search]. A rental-application ranking is squarely caught.
- **Small-business exemption:** lost for any entity that discloses personal information for a benefit without consent (s 6D). Cross-sell referrals do exactly that [verified: round 1]. Opt in under s 6EA.
- **Direct marketing:** APP 7 bars direct marketing with information the person would not reasonably expect to be used that way. A rental applicant does not expect home-loan marketing. Combined with the Spam Act, this means express, unbundled consent, not inferred consent.
- **Tranche 2:** the exposure draft (Privacy Amendment (Personal Data Protection) Bill 2026) was released 31 August 2026 and consultation closed 18 September 2026; commencement dates are blank [verified: Clayton Utz, Mills Oakley, AG consultation via search].
  - It would replace APPs 3, 4 and 6 with a single "fair and reasonable" test.
  - It would ban trading in personal information without consent [verified: summaries].
  - The small-business exemption reportedly *stays* in the draft [verified: one firm summary; others ambiguous].
  - Build to the draft now: secondary use of tenancy data for cross-sell is unlikely to be "fair and reasonable".

**A9. Investment support creates an inverted conflict (Med).**
- The PM agency loses the management when the landlord sells. "Hold" advice therefore serves the agency's fee. That is the mirror image of the sales-agent conflict the brief claims to be free of.
- Rebates on the onward purchase (developer or selling-agent commissions to a buyer's agent, finance commissions) engage s 48A where they relate to the client's sale, management or leasing. They are also secret commissions unless the client gives fully informed consent.
- Fix: disclose the management-fee interest on every hold/sell recommendation, publish the methodology, and rebate or disclose all third-party benefits.

## Things the brief gets wrong, misses or understates
1. **"Fee could be split between landlord and tenant."** It cannot be a tenancy term or a condition of renting. Delete it.
2. **"Victorian standard application form limits screening data" understates the point.** The bigger constraints are the destruction regime and the 3-year post-tenancy limit: there is no permanent tenant graph. The founder's "data moat" must be built on *property* data (maintenance, condition, rent achieved) and consented landlord data, not renter data.
3. **There is no specific "30-day deletion" in the Privacy Act.** The 30 days comes from the Victorian RTA regime, with a 6-month consented extension. Correction to the role brief's framing: the trigger is "within 30 days after the rental agreement is entered into with someone else" [verified: CAV via search].
4. **The tranche 2 "second wave" is not law.** It is an exposure draft with no commencement date as at 2 November 2026. The small-business exemption likely survives tranche 2. The exemption risk comes from trading in personal information, not from turnover.
5. **Renter fee rules apply to "persons", not only landlords.** The March 2026 fee ban expressly reaches third-party platforms [verified: CAV/Premier summaries]. A separate tenant-services entity does not escape the ban if its product is attached to applying or paying rent.
6. **Time-sensitive:**
   - Agents' representative registration from 25 November 2026.
   - Victorian election on 28 November 2026. Rental policy may tighten further; the Greens are pushing lease-break fee abolition and rent caps.
   - ADM transparency from 10 December 2026.

## Numbers checked
| Claim | Finding | Status/source |
|---|---|---|
| Standard application form from Mar 2026 | 31 Mar 2026; company max penalty >$62,700 (individual >$12,500) for out-of-form requests | verified: CAV / law-firm summary via search |
| Deletion within 30 days, unsuccessful applicants | 30 days after agreement with another renter; 6 months with written consent; successful renter 3 years post-tenancy | verified: CAV, standard form via search |
| Application and rent-payment fees banned incl. third-party platforms | Yes, 31 Mar 2026; RTA s 51A; fee-free method under s 42 | verified: CAV, Premier, Tenants Vic |
| Renting Taskforce enforcement | 250 warnings, 130 infringements, ~$900k fines, 11 court actions (to 27 Aug 2026) | verified: Premier/CAV |
| ADM transparency | APP 1.7–1.9 from 10 Dec 2026; OAIC guidance 30 Sep 2026 | verified: Maddocks, Allens |
| Tranche 2 | Exposure draft 31 Aug 2026; submissions closed 18 Sep; commencement blank; "fair and reasonable" replaces APPs 3/4/6 | verified: Clayton Utz, AG consultation, Mills Oakley |
| Small-business exemption removed in tranche 2 | Reportedly *retained* in draft | verified (one firm), conflicting commentary |
| Rent history in Australian credit files | Not standard; opt-in services exist | unverified |
| NCCP referral | reg 25 exemption narrow; commission disclosure; no product suggestion | verified: Bright Law / MFAA |
| Landlord–tenant conflict recognised | CAV names landlord and tenant, and buyer and seller, as conflict examples | verified: CAV via search |

## Improvements (ranked by impact)
1. **Use a three-entity architecture.**
   - **(a) LicensedCo (agency):** acts only for landlords. Covers PM, letting, tenant selection, the maintenance programme and landlord investment analytics. Holds the trust account and tenancy data.
   - **(b) RenterCo (separate company, own privacy policy, own consent):** a renter-chosen app offering a verified rent ledger, moving help, savings via an ADI partner, and buyer education. Renters sign up after lease signing, never at application. Renter-entered data never flows to LicensedCo. The only flow from LicensedCo to RenterCo is the renter's *own* payment ledger, pushed at the renter's explicit, revocable request.
   - **(c) Licensed partners for regulated acts:** a credit-licensed broker (could later be a group ACL holder), an AFSL authorised-representative arrangement or ADI partner for savings, and a licensed insurer if any risk product is offered. All benefits are disclosed, and landlord-related benefits are rebated per s 48A advice.
2. **Information barrier as code.** Rent-setting, renewal and landlord-advice models must be technically unable to read RenterCo data. Log every access, audit annually, and publish the barrier in both privacy policies. This is the difference between "manageable" and "disqualifying".
3. **Delete tenant fee splits and all application-stage offers.** Price maintenance 100% to the landlord.
4. **Build the data moat on property, not people.** Rely on asset condition, maintenance cost curves, rent achieved, vacancy and landlord behaviour. Renter data goes to a de-identified training store at the statutory deadline under a written de-identification standard (k-anonymity or aggregation by suburb and band; no address keys). Model reject inference explicitly.
5. **Screening model governance before 10 December 2026.**
   - Standard-form fields only.
   - Human decision on every application, with a named registered representative.
   - APP 1.7 ADM statement.
   - Annual disparate-impact testing across EO attributes using proxy methods.
   - Ban features: income *source*, household composition, postcode, age of references, "gaps".
   - Give applicants a reasons-on-request process.
6. **Sale-to-tenant protocol:** vendor-only agency, written disclosure to the tenant, independent representation advised, no group buyer-side role, and no RenterCo data used.
7. **Steering protocol:** applicants only with standard-form consent; sitting renters only after they give notice; disclose to both landlords.
8. **Opt in under Privacy Act s 6EA now.** Drafting to the tranche 2 "fair and reasonable" test costs little now and saves a rebuild later.

## Tests & kill criteria
| Test | Metric | Threshold | Timeframe / cost |
|---|---|---|---|
| Written opinion: RTA renter-info provisions (s 505BA ff), s 51/51A, s 48A applied to the 3-entity design | Opinion confirms RenterCo with post-lease opt-in is not a prohibited charge or misuse | Negative → drop RenterCo monetisation; keep it as a free retention tool only | 4–6 weeks, ~$10–20k [estimate] |
| RenterCo consent funnel on an acquired roll | % of renters who opt in post-lease to the rent ledger | <15% in 90 days → tenant side is not a channel | 90 days, ~$15k build [estimate] |
| Disparate-impact audit of the screening model on de-identified history | Approval-rate ratio by proxy attribute groups | Any group <0.8 of the reference group that can't be cured by feature removal → no automated ranking; human-only shortlisting | Before 10 Dec 2026 deployment |
| Sale-to-tenant pilot | % of selling landlords who agree to a tenant introduction; complaints | <10% uptake or any CAV complaint → drop | First 20 sellers |
| Barrier audit | Unauthorised cross-entity data accesses | Any → stop cross-sell until fixed; two → wind up RenterCo data sharing | Quarterly |

## Answers to the round-2 questions in my domain
**Q1 (which services carry the economics):** landlord-paid investment support first, then the landlord-paid maintenance programme. Tenant evaluation is part of letting, not a product. Tenant services are a moat and a channel, not revenue, until the opinion clears.

**Q2 (lifetime value):** renter lifetime value is legally capped. There is no fee during the tenancy, the data is purpose-locked, and data is destroyed within 3 years after the tenancy. Any tenant revenue must come from RenterCo customers who consented separately. For the $500k draw, plan on landlord-side lifetime value only. Renter-side value is upside that does not lower the ~2,000-property scale requirement unless the consent funnel test shows uptake above 30%.

**Q3 (regulated services; which conflicts are disqualifying):**

*Disqualifying:*
- Charging renters any compulsory or tenancy-linked fee, including a maintenance split.
- Renter financial data flowing into rent-setting or landlord advice.
- One group entity acting for both vendor-landlord and tenant-buyer on the same property.
- Undisclosed or unrebated benefits on landlord sales, purchases, maintenance or finance.
- Selling cross-landlord tenant scores, which becomes a tenancy database and creates EO exposure.
- Credit or deposit products without an ACL, an AFSL or a partner.

*Manageable with separation, consent and disclosure:*
- In-portfolio steering of consenting applicants.
- Introducing a sitting tenant as a buyer (vendor-only).
- Renter rent ledger and savings via RenterCo.
- Landlord refinancing via a licensed broker.
- Landlord investment advice with the PM-fee conflict disclosed.

**Q4/Q5:** autonomy must stay assistive on selection and rent-setting (EO and ADM exposure; human-issued notices). The founder's stats edge is decisive in de-identification, reject inference and disparate-impact testing.

**Q6 (smallest test):** the written opinion on the three-entity design plus a 90-day RenterCo opt-in test on one acquired roll.

## Questions I'd hand to other specialists
- **Insurance/APRA specialist:** is a flat-fee maintenance programme that absorbs repair-cost variance "insurance business" or a financial product for managing financial risk? Does performing repairs in kind take it outside?
- **Credit/financial services:** a group ACL versus a reg 25 referral arrangement for landlord refinancing and tenant first-home loans. What is the AFSL path for a renter savings feature via an ADI?
- **CFO modeller:** remodel with zero tenant fees, renter revenue as an option on consent (0–30%), and landlord-side lifetime value only.
- **Data/AI architect:** a de-identification standard robust to address re-identification; reject-inference approach; enforceable cross-entity barrier.
- **Regulatory counsel (round 1, 03):** does s 48A extend to finance or buyer's-agency benefits on a landlord's *next* purchase? Check the Estate Agents (Professional Conduct) Regulations 2018 wording on dual agency and related-party trades.
