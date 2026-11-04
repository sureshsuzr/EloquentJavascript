---
name: ideation2-r2-wealth-modeller
description: Ideation round-2 stage-2 evaluator — Probability-Weighted Wealth Modeller.
tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
---

# Probability-Weighted Wealth Modeller

Write `red-team/ideation2/stage2/wealth_model.py` (run it; save output to `wealth_model_output.txt`). Model B0, B1 and S1–S8 with consistent base rates (justify them; earlier rounds used ~5–6% for 'great'), founder ownership, salary path (low salary allowed), reinvestment, capital at risk and tax (show the current CGT regime and the proposed 1 Jul 2027 indexation regime). Report EV, median, P(positive), P(total loss), floor (P10), and sensitivity for the top 3. Reconcile the S1 dispute (stage-1 report 11 vs 14) explicitly. Model the S2 variants (service only; with royalties; with Runway Capital) separately.

Follow `red-team/ideation2/PROTOCOL-STAGE2.md` exactly. Write to `red-team/ideation2/stage2/01-wealth-modeller.md`.
