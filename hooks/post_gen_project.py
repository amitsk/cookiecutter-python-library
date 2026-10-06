#!/usr/bin/env python
"""Post-generation hooks for cookiecutter template."""

import shutil
import sys
from pathlib import Path


def remove_notebooks_folder():
    """Remove notebooks folder if analytics is not enabled."""
    use_analytics = "{{ cookiecutter.use_analytics }}"

    if use_analytics == "n":
        notebooks_dir = Path("notebooks")
        if notebooks_dir.exists():
            shutil.rmtree(notebooks_dir)
            print("Removed notebooks folder (use_analytics=n)")


def remove_agent_files():
    """Remove LLM agent instruction files if not enabled."""
    use_agent_instructions = "{{ cookiecutter.use_agent_instructions }}"

    if use_agent_instructions == "n":
        candidates = [
            Path("AGENTS.md"),
            Path("CLAUDE.md"),
            Path(".github/copilot-instructions.md"),
            Path(".cursor"),
        ]
        for target in candidates:
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
                print(f"Removed {target} (use_agent_instructions=n)")
            elif target.exists() or target.is_symlink():
                target.unlink()
                print(f"Removed {target} (use_agent_instructions=n)")


def assert_no_unrendered_variables():
    """Fail if any Jinja variable survived rendering."""
    # NOTE: built from chr(123) so cookiecutter's own Jinja rendering
    # of this hook file does not choke on a literal double-open-brace.
    open_braces = chr(123) * 2
    leftovers = []
    for path in Path(".").rglob("*"):
        if ".git/" in str(path) or "__pycache__" in str(path):
            continue
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if open_braces in text and "cookiecutter" in text:
                leftovers.append(str(path))
    if leftovers:
        print("Unrendered cookiecutter variables in:", file=sys.stderr)
        for item in leftovers:
            print(f"  {item}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    remove_notebooks_folder()
    remove_agent_files()
    assert_no_unrendered_variables()
