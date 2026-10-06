# {{cookiecutter.project_slug}} — Agent Instructions

Instructions for AI coding agents working in this repo. Follow them without asking.

## Tech Stack

- Python `{{cookiecutter.python_version}}` (floor in `pyproject.toml`), uv, hatchling build backend
- pytest (`testpaths = ["tests"]`) with `pytest-cov`, `pytest-mock`, `faker`
- ruff (lint + format, line-length 88, `E501` ignored), ty (`ty check src/{{cookiecutter.pkg_name}}`), pre-commit
{% if cookiecutter.use_analytics == "y" -%}
- Optional analytics extra: jupyter, pandas, matplotlib, seaborn, plotly, ipykernel
{% endif %}

## Commands

Single entrypoint: `make verify` (= `make check`: format-check + lint + type-check + test).

| Task | Command |
|------|---------|
| Install | `make install` (`uv sync --dev`) |
| Full build | `make build` (install, lint, type-check, test) |
| Verify (no install) | `make verify` |
| Tests | `make test` (coverage floor applies) |
| Lint | `make lint` (`ruff check src/ tests/`) |
| Types | `make type_check` |
| Format check / fix | `make check_format` / `make fix_format` |
| Coverage HTML | `make coverage` |
| Package build | `uv build` |
{% if cookiecutter.use_analytics == "y" -%}
| Analytics env | `make install-analytics` (`uv sync --extra analytics`) |
| Jupyter Lab | `make jupyter` |
{% endif %}

## Code Conventions

- Layout: `src/{{cookiecutter.pkg_name}}/` (`__init__.py`, `py.typed`, `app.py`, `main.py`); tests in `tests/{{cookiecutter.pkg_name}}/test_*.py`.
- ruff selects include `ANN` (annotate public functions), `S` (bandit), `TRY`, `PL`; tests relax `S101`, `ANN`, `PLR2004` (see `pyproject.toml` per-file-ignores).
- Type hints required in `src/`; `py.typed` ships them (PEP 561). Keep `ty check` clean.
- Tests use plain `assert`, Arrange-Act-Assert; name tests after behavior.
- Entry point pattern (`src/{{cookiecutter.pkg_name}}/main.py`): thin `main()` calling into `app`, logging via `loguru`.

```python
from {{cookiecutter.pkg_name}}.app import scrabble_score


def main() -> None:
    print(scrabble_score("hello"))
```

## Boundaries

- Never commit `.env`, secrets, or notebooks output artifacts; never hand-edit lockfiles.
- Ask before changing `license`, `requires-python`, or the public package API.
- Always run `make verify` before declaring work done; quote its result.
