# Red-team protocol (shared by every agent)

1. Read `red-team/BRIEF.md` in full. You understand the objective: replace a ~$500k income with an AI-native PM agency in one Melbourne corridor, with international scale as optional upside.
2. Work **independently**. Do not read other agents' reports. Stay in your own lane; your value is a view the others won't have.
3. Be adversarial but constructive: try to kill the idea in your domain, then say what would have to be true for it to survive and how to make it survive.
4. Verify numbers. Use web search where it helps (Australian/Victorian sources first: CAV, legislation.vic.gov.au, REIV, ABS, CoreLogic/Cotality, Domain/REA, ACCC, OAIC, RBA, company sites, trade press). Label every figure **[verified: source]**, **[estimate: reasoning]** or **[unverified]**. Don't invent citations. If a fact in the brief looks wrong or stale, say so and give the correction.
5. Today is 2 November 2026. Flag anything time-sensitive.
6. Write your report to `red-team/reports/<NN>-<slug>.md` (path given in your role) using exactly this structure:

```
# <Role title>: red-team report
## Verdict (3–5 lines: survives / survives-if / fatal, and the single biggest issue)
## Attacks on the load-bearing assumptions (only those in your domain; evidence, severity High/Med/Low)
## Things the brief gets wrong, misses or understates
## Numbers checked (table: claim | finding | status/source)
## Improvements (concrete changes to the plan, ranked by impact)
## Tests & kill criteria (cheap experiments, metric, threshold, timeframe)
## Answers to open items in my domain
## Questions I'd hand to other specialists
```

7. Length 1,500–3,000 words. Dense, specific, no filler or generic startup advice. Australian English, AUD.
8. When done, reply with only the 5 most important findings (one line each) plus the report path.
