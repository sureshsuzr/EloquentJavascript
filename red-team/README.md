# Red team: AI-native property-management agency (Melbourne)

- `BRIEF.md`: the founder's brief, shared by all agents
- `PROTOCOL.md`: rules every agent follows (independence, verification labels, report structure)
- `../.claude/agents/redteam-*.md`: 13 reusable agent role definitions
- `reports/01–13`: independent reports
- `models/unit_economics.py`: scenario model (`python3 red-team/models/unit_economics.py`)
- `SYNTHESIS.md`: consolidated verdict, revised gates, plan and kill criteria. **Start here.**

To re-run one agent after updating the brief: ask Claude Code to run the `redteam-<slug>` agent.
