#!/usr/bin/env python
"""Post-generation hooks for cookiecutter template."""

import shutil
from pathlib import Path


def remove_notebooks_folder():
    """Remove notebooks folder if analytics is not enabled."""
    use_analytics = "{{ cookiecutter.use_analytics }}"

    if use_analytics == "n":
        notebooks_dir = Path("notebooks")
        if notebooks_dir.exists():
            shutil.rmtree(notebooks_dir)
            print("Removed notebooks folder (use_analytics=n)")


if __name__ == "__main__":
    remove_notebooks_folder()
