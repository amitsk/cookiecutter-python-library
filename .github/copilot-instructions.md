# Copilot Instructions (template repo)

Condensed from `AGENTS.md` (canonical). Cookiecutter + Jinja2 template; generated projects use Python 3.14, uv, pytest, ruff, ty.

Workflow: `uvx cookiecutter --no-input -o /tmp/opencode/out .` with `use_analytics`/`use_agent_instructions` in `y n`; in each rendered dir run `make build check_format` + `uv build`.

Conventions: template files under the slug dir must fully render (post-gen hook fails on leftovers); hooks only delete + assert; `AGENTS.md` canonical, this file + Cursor rules are condensations mentioning `make check`.

Boundaries: never commit rendered output or secrets; ask before changing `python_version`, ruff selects, or CI strategy.
