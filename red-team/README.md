# Red team: AI-native property-management agency (Melbourne)

- `BRIEF.md`: the founder's brief, shared by all agents
- `PROTOCOL.md`: rules every agent follows (independence, verification labels, report structure)
- `../.claude/agents/redteam-*.md`: 13 reusable agent role definitions
- `reports/01–13`: independent reports
- `models/unit_economics.py`: scenario model (`python3 red-team/models/unit_economics.py`)
- `SYNTHESIS.md`: round-1 (agency) verdict, revised gates, plan and kill criteria
- `round2/`: platform-thesis round (10 agents incl. agentic AI expert): `round2/SYNTHESIS.md`, `round2/models/ltv_model.py`

To re-run one agent after updating the brief: ask Claude Code to run the `redteam-<slug>` agent.
- `round3/`: software/data business round (9 agents): `round3/SYNTHESIS.md` **latest: start here**, `round3/models/software_model.py`
