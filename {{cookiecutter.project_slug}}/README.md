# {{cookiecutter.project_slug}}

![Run Tests and Lint](https://github.com/{{cookiecutter.project_slug}}/workflows/Run%20Tests%20and%20Lint/badge.svg)

- uv for dependency management
- Pytest for tests
- ruff for formatting and linting
- ty for type checking


## Building

- Install uv https://docs.astral.sh/uv/getting-started/installation/
- Clone from GitHub
- Build - Install, test, lint `make build`. This step pulls the python version defined in pyproject.toml
- Tests can be run with `make test`
