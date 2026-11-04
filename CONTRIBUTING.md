---

### `CONTRIBUTING.md`
```markdown
# Student Workflow & Role Assignments

## Team Roles
Assign one primary role to each team member (teams of 3–4):
- **Project Lead / Scrum Master:** Assigns GitHub Issues, reviews Pull Requests, manages merges.
- **Game Logic Developer:** Fixes bugs in `player.py` and `main.py`.
- **Data & Score Specialist:** Fixes bugs in `scoreboard.py` and score tracking.
- **Documentation & QA:** Writes issue descriptions, tests fixes, and documents code comments.

## Branching Protocol
1. **Never commit directly to `main`.**
2. Create a branch for every fix:
   - Example: `git checkout -b fix/player-health-bug`
   - Example: `git checkout -b fix/scoreboard-formatting`
3. Push your branch to GitHub:
   ```bash
   git push origin fix/your-branch-name
