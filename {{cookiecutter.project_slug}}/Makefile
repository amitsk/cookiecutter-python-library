
.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

UV=uv
CODE_COVERAGE=50

build: install  lint type_check test

install:
	$(UV) sync --dev

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

type_check: ## Check type hints with ty
	-@$(UV) run ty check  src/{{cookiecutter.pkg_name}}

lint: ## Check code with pyflakes and mypy ( errors ignored)
	@$(UV) run ruff check src/{{cookiecutter.pkg_name}}


test: ## run tests quickly with the default Python
	@$(UV) run pytest --cov src/{{cookiecutter.pkg_name}} --cov-report term-missing --cov-fail-under $(CODE_COVERAGE)  tests/ -v


coverage: ## check code coverage quickly with the default Python
	coverage run --source src/{{cookiecutter.pkg_name}} -m pytest
	coverage report -m
	coverage html

check: check_format lint test

check_format:
	$(info [*] Running ruff format checkers...)
	@$(UV) run ruff format --check src/

fix_format:
	$(info [*] Running ruff format fixers...)
	@$(UV) run ruff format  src/
