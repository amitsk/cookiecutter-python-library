# LLM Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generated projects bootstrap LLMs via templated AGENTS.md matrix gated by `use_agent_instructions`.

**Architecture:** Single canonical `AGENTS.md` per repo (template root + generated); `CLAUDE.md`/Copilot/Cursor files are thin pointers/condensations; Jinja renders variables; post-gen hook deletes on `n`; CI asserts 4-way matrix.

**Tech Stack:** Cookiecutter/Jinja2, Python 3.14, uv, Make, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-10-06-llm-bootstrap-design.md`

## Global Constraints

- Python floor for generated projects is the `python_version` variable (default 3.14); template repo itself uses `.mise.toml` python 3.14.
- Never commit `.env`/secrets; never hand-edit lockfiles.
- LLM entrypoint is `make verify` (= `make check`).
- No `{{` leftovers in any generated project outside `.git/`.

## Review Focus

- `use_agent_instructions=n` still leaves an agent file behind — expect zero agent files.
- Jinja variable renders literally (e.g. `{{cookiecutter.pkg_name}}` unsubstituted) — expect substituted `src/<pkg>/` paths.
- `make verify` missing from `.PHONY` or not equal to `check` — expect alias works.
- Copilot/Cursor pointer drifts from `AGENTS.md` (omits `make check`) — expect pointer contains `make check`/`make verify`.
- 4-way CI matrix not actually exercising `n/n` combo — expect all 4 generate+build.

---

### Task 1: Template definition (flag + hook + Makefile + gitignore)

**Files:**
- Modify: `cookiecutter.json`
- Modify: `hooks/post_gen_project.py`
- Modify: `{{cookiecutter.project_slug}}/Makefile`
- Modify: `{{cookiecutter.project_slug}}/.gitignore`

**Interfaces:**
- Consumes: existing `use_analytics` flag pattern, `remove_notebooks_folder()`.
- Produces: `use_agent_instructions` variable; `remove_agent_files()` + `assert_no_unrendered_variables()` called from `__main__`; `make verify` target.

- [ ] **Step 1: Add flag + hook + alias + gitignore fix**
- [ ] **Step 2: Render both combos locally and assert file presence/absence + no `{{` leftovers**
Run: `rm -rf /tmp/opencode/llm-y /tmp/opencode/llm-n && uvx cookiecutter --no-input -o /tmp/opencode/llm-y . use_agent_instructions=y && uvx cookiecutter --no-input -o /tmp/opencode/llm-n . use_agent_instructions=n && ls /tmp/opencode/llm-y/python-boilerplate/AGENTS.md && test ! -e /tmp/opencode/llm-n/python-boilerplate/AGENTS.md && ! grep -r "{{" /tmp/opencode/llm-y/python-boilerplate --exclude-dir=.git && echo OK`
Expected: OK
- [ ] **Step 3: Commit**
```bash
git add cookiecutter.json hooks/post_gen_project.py "{{cookiecutter.project_slug}}/Makefile" "{{cookiecutter.project_slug}}/.gitignore"
git commit -m "feat: gate agent instructions behind use_agent_instructions flag"
```

### Task 2: Generated-project agent files

**Files:**
- Create: `{{cookiecutter.project_slug}}/AGENTS.md`
- Create: `{{cookiecutter.project_slug}}/CLAUDE.md`
- Create: `{{cookiecutter.project_slug}}/.github/copilot-instructions.md`
- Create: `{{cookiecutter.project_slug}}/.cursor/rules/commands.mdc`
- Create: `{{cookiecutter.project_slug}}/.cursor/rules/conventions.mdc`

**Interfaces:**
- Consumes: `use_agent_instructions` flag + `verify` target from Task 1.
- Produces: 5 templated files using `{{cookiecutter.project_slug}}`, `{{cookiecutter.pkg_name}}`, `{{cookiecutter.python_version}}`, conditional analytics block.

- [ ] **Step 1: Write the 5 files per Spec content contract**
- [ ] **Step 2: Render `y` combo and verify substitution + pointers reference AGENTS.md/make check**
Run: `rm -rf /tmp/opencode/llm-y && uvx cookiecutter --no-input -o /tmp/opencode/llm-y . use_agent_instructions=y && grep -q "src/" /tmp/opencode/llm-y/python-boilerplate/AGENTS.md && grep -q "make check" /tmp/opencode/llm-y/python-boilerplate/.github/copilot-instructions.md && echo OK`
Expected: OK
- [ ] **Step 3: Commit**
```bash
git add "{{cookiecutter.project_slug}}/AGENTS.md" "{{cookiecutter.project_slug}}/CLAUDE.md" "{{cookiecutter.project_slug}}/.github/copilot-instructions.md" "{{cookiecutter.project_slug}}/.cursor/rules/"
git commit -m "feat: add templated LLM instruction files to generated project"
```

### Task 3: Template-root agent files

**Files:**
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Create: `.github/copilot-instructions.md`
- Create: `.cursor/rules/commands.mdc`, `.cursor/rules/conventions.mdc`

**Interfaces:**
- Consumes: generated-project AGENTS.md content contract (mirrors it for template-maintainer workflow).
- Produces: maintainer instructions (`uvx cookiecutter --no-input`, `make build check_format`, `uv build`).

- [ ] **Step 1: Write the 4 files**
- [ ] **Step 2: Verify no Jinja leftovers in template-root files**
Run: `! grep -r "{{" AGENTS.md CLAUDE.md .github/copilot-instructions.md .cursor/rules/ && echo OK`
Expected: OK
- [ ] **Step 3: Commit**
```bash
git add AGENTS.md CLAUDE.md .github/copilot-instructions.md .cursor/rules/
git commit -m "docs: add maintainer agent instructions for template repo"
```

### Task 4: CI 4-way matrix

**Files:**
- Modify: `.github/workflows/template-ci.yml`
- Modify: `docs/superpowers/specs/2026-10-06-llm-bootstrap-design.md` (none — spec frozen)

**Interfaces:**
- Consumes: Tasks 1–2 outputs.
- Produces: `use_analytics {y,n}` × `use_agent_instructions {y,n}` matrix with presence/absence + `{{` assertions.

- [ ] **Step 1: Extend matrix + assertion steps**
- [ ] **Step 2: Simulate CI matrix locally (4 generates; build the `y/y` one if toolchain allows)**
Run: `for a in y n; do for g in y n; do rm -rf /tmp/opencode/m-$a-$g; uvx cookiecutter --no-input -o /tmp/opencode/m-$a-$g . use_analytics=$a use_agent_instructions=$g || exit 1; d=/tmp/opencode/m-$a-$g/python-boilerplate; [ "$a" = y ] && test -d $d/notebooks || test ! -e $d/notebooks; [ "$g" = y ] && test -f $d/AGENTS.md || test ! -e $d/AGENTS.md; ! grep -r "{{" $d --exclude-dir=.git || exit 1; done; done; echo MATRIX-OK`
Expected: MATRIX-OK
- [ ] **Step 3: Commit**
```bash
git add .github/workflows/template-ci.yml docs/superpowers/specs/2026-10-06-llm-bootstrap-design.md docs/superpowers/plans/2026-10-06-llm-bootstrap.md
git commit -m "ci: cover agent-instruction flag in template matrix"
```
