# YURA — Developer Performance Intelligence

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Point YURA at any git repository. It clones the full history, reads every
committer's footprint, and builds a board-ready, McKinsey-styled report that
ranks the team across **volume, consistency, and code quality** — with an
optional LLM pass that judges every commit for quality, authenticity, and
AI-assistance.

## Stack

- **FastAPI** + Jinja2 templates · **SQLite** (SQLAlchemy 2.0)
- Git via the system `git` binary (full history, real committer identities)
- **Server-rendered SVG charts** in the McKinsey exhibit idiom — no JS chart
  dependency, fully self-contained

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python run.py            # → http://127.0.0.1:8000
# or: .venv/bin/uvicorn app.main:app --reload
```

## Flow

1. **Add a repository** — paste an HTTPS or `git@` URL.
2. **Pick a branch** — branches are read remotely (`git ls-remote`) before cloning.
3. **Clone** — full, non-shallow clone of the chosen branch (background task).
4. **Run analysis** — parses `git log --numstat`, aggregates per-developer metrics,
   computes a transparent composite ranking.
5. **Report** — KPI strip + exhibits (ranking, score breakdown, commits, churn,
   cadence timeline) + full scorecard table.

## Scoring (local mode)

Composite score (0–100) = weighted blend, then shrunk by a credibility factor:

| Dimension    | Weight | Inputs                                             |
|--------------|--------|----------------------------------------------------|
| Volume       | 40%    | commit count + code churn                          |
| Consistency  | 25%    | active days + cadence within tenure                |
| Quality      | 35%    | low-effort-commit ratio + commit-message discipline |

`score *= commits / (commits + 8)` — a small-sample dampener so a single-commit
drive-by can't out-rank a sustained contributor.

## Settings

`/settings` stores the LLM provider, API keys (Anthropic / OpenAI), model names,
and a per-run commit cap (cost guard). Keys live in the local SQLite DB.

## LLM mode

`app/services/llm.py` judges each commit diff via the configured provider
(OpenAI or Anthropic), scoring **commit quality, authenticity (real vs. fake
work), and AI-assistance**. Commits are sampled across contributors up to the
scan limit, judged concurrently with a live cost estimate, and folded into the
ranking. The whole run streams real-time progress to the browser over a
WebSocket, and the model writes the report's executive summary.

## Layout

```
app/
  main.py            FastAPI factory
  config.py db.py models.py templating.py
  services/  git_service.py  analysis.py  charts.py  settings_store.py
             models_service.py  llm.py  progress.py
  routers/   repos.py  analysis.py  settings.py
  templates/ base index branches repo running report settings
  static/css/app.css   # McKinsey design tokens
workspace/  cloned repos (gitignored)
data/       sqlite db  (gitignored)
```

## License

YURA is free software licensed under the **GNU Affero General Public License
v3.0 or later** (AGPL-3.0-or-later) — see [LICENSE](LICENSE).

The AGPL's network clause (§13) matters here: if you run a modified version of
YURA as a network service, you must make your modified source available to its
users. Copyright © 2026 Sensium AI and contributors.
