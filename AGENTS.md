# cookiecutter-python-library — Agent Instructions

Instructions for AI coding agents maintaining this cookiecutter template.

## Tech Stack

- Cookiecutter + Jinja2 templating; generated projects target Python 3.14, uv, hatchling, pytest, ruff, ty
- Template repo toolchain: Python 3.14 via mise (`.mise.toml`), cookiecutter via `uvx cookiecutter`

## Commands

| Task | Command |
|------|---------|
| Render (analytics on, agents on) | `uvx cookiecutter --no-input -o /tmp/opencode/out . use_analytics=y use_agent_instructions=y` |
| Render matrix locally | loop `use_analytics` in `y n` × `use_agent_instructions` in `y n` |
| Full template check | render all 4 combos, then in each rendered dir: `make build check_format` and `uv build` |
| Lint hooks | `uvx ruff check hooks/` (keep hooks Jinja-safe: no literal double-open-brace outside real variables) |

## Code Conventions

- Template files live under the slug directory on disk (its name uses cookiecutter template syntax); every `cookiecutter.*` variable inside it must render — the post-gen hook fails the generation on leftovers.
- `cookiecutter.json` holds all prompts; `hooks/post_gen_project.py` only deletes (`notebooks/`, agent files) and asserts; never add generation logic there.
- `AGENTS.md` is canonical in both repos; `CLAUDE.md` is a pointer; Copilot/Cursor files are condensations that must mention `make check` (CI asserts this).
- Mirror structural changes (Makefile targets, lint sets) into the templated `AGENTS.md`.

## Boundaries

- Never commit rendered output (`python-boilerplate/` is gitignored); never commit `.env` or secrets.
- Ask before changing default `python_version`, the ruff select set, or CI strategy.
- Always render all 4 combos and report results before declaring template work done.
