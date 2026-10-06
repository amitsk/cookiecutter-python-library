# LLM Bootstrap Design

**Date:** 2026-10-06
**Status:** Approved — user selected "Full matrix (Recommended)", authorized implementation.

## Outcome

Generated projects bootstrap LLMs with one command and one canonical instruction file. Template root documents maintainer workflow for LLMs editing the template itself.

## Scope

In scope:
- Template-root `AGENTS.md`, `CLAUDE.md` pointer, `.github/copilot-instructions.md`, `.cursor/rules/*.mdc`.
- Generated-project `AGENTS.md` (templated), `CLAUDE.md`, `.github/copilot-instructions.md`, `.cursor/rules/*.mdc`, gated by new `use_agent_instructions` flag (`y`/`n`).
- `verify` Makefile alias, `.gitignore` unification, CI assertions.
- Out of scope: `description` prompt, `.python-version`/`.mise.toml` in generated project, `CONSTRAINTS.md`/skills scaffolding.

## Decisions

1. Single canonical source: `AGENTS.md` is full; `CLAUDE.md` is a 3-line pointer; Copilot/Cursor files are condensed (≤30 lines) and must reference `make check` so CI can assert sync.
2. Cookiecutter renders all agent files with Jinja; `hooks/post_gen_project.py` deletes them when `use_agent_instructions=n` and always fails on leftover `{{` outside `.git/`.
3. LLM entrypoint is `make verify` (= `make check`: format-check + lint + type_check + test). `make build` remains install+lint+type+test.
4. Matrix in `.github/workflows/template-ci.yml`: `use_analytics {y,n}` × `use_agent_instructions {y,n}` (4 combos), each asserts notebooks presence/absence, agent-files presence/absence, no `{{` leftovers, then `make build check_format` + `uv build`.

## Files

Template root — create:
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/commands.mdc`, `.cursor/rules/conventions.mdc`

Template definition — modify:
- `cookiecutter.json`: add `"use_agent_instructions": ["y", "n"]` (after `use_analytics`).
- `hooks/post_gen_project.py`: add `remove_agent_files()`, add `assert_no_unrendered_variables()`.
- `{{cookiecutter.project_slug}}/Makefile`: add `verify: check` alias, add `verify` to `.PHONY`.
- `{{cookiecutter.project_slug}}/.gitignore`: change `./python-boilerplate` → `python-boilerplate/`.
- `.github/workflows/template-ci.yml`: 4-way matrix + agent-file assertions.

Generated project — create (templated, removed when flag=n):
- `{{cookiecutter.project_slug}}/AGENTS.md`
- `{{cookiecutter.project_slug}}/CLAUDE.md`
- `{{cookiecutter.project_slug}}/.github/copilot-instructions.md`
- `{{cookiecutter.project_slug}}/.cursor/rules/commands.mdc`, `.cursor/rules/conventions.mdc`

## AGENTS.md content contract (generated)

- Title: `# {{cookiecutter.project_slug}} — Agent Instructions`
- Tech Stack: Python `{{cookiecutter.python_version}}`, uv, hatchling, pytest, ruff (list select groups), ty, pre-commit; conditional analytics line.
- Commands table: `make install/build/test/lint/type_check/check_format/coverage/verify`, `uv build`.
- Conventions: src layout `src/{{cookiecutter.pkg_name}}/` with `py.typed`, tests `tests/{{cookiecutter.pkg_name}}/test_*.py`, ruff line-length 88 / `E501` ignored, `ty check src/{{cookiecutter.pkg_name}}`, pytest `testpaths=["tests"]`.
- Boundaries: never commit `.env`/secrets, never hand-edit lockfiles, ask before DB schema/license change, run `make verify` before declaring done.
- Pattern: one `scrabble_score` import example.

## Verification

- `uvx cookiecutter --no-input -o $TMP . use_analytics=y use_agent_instructions=y` → `AGENTS.md`, `CLAUDE.md`, Copilot + Cursor files exist, `make verify` documented, no `{{` leftovers.
- Same with `=n` → agent files absent, notebooks logic unchanged.
- CI green on all 4 combos.
