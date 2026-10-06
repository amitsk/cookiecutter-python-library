# {{cookiecutter.project_slug}} — Copilot Instructions

Condensed from `AGENTS.md` (canonical). Python `{{cookiecutter.python_version}}`, uv, pytest, ruff (88 cols, `E501` off), ty.

Workflow: `make install`, then `make verify` (= `make check`: `check_format` + `lint` + `type_check` + `test`). `make build` = install + checks. Package with `uv build`.

Conventions: code in `src/{{cookiecutter.pkg_name}}/` with type hints (`py.typed` shipped); tests in `tests/{{cookiecutter.pkg_name}}/` with plain `assert`; annotate public functions (`ANN`), keep `ty check src/{{cookiecutter.pkg_name}}` clean.

Boundaries: never commit secrets/`.env`; ask before license, `requires-python`, or public API changes.
