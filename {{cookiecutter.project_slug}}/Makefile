
.PHONY: build install help clean clean-test clean-pyc clean-build type_check lint test coverage check check_format fix_format format
.DEFAULT_GOAL := help

UV=uv
CODE_COVERAGE=50

build: install lint type_check test ## install, lint, type check and test

install: ## install the package and dev dependencies
	$(UV) sync --dev

help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

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
	rm -fr htmlcov/ coverage_html_report/
	rm -fr .pytest_cache

type_check: ## Check type hints with ty
	@$(UV) run ty check src/{{cookiecutter.pkg_name}}

lint: ## Check code with ruff
	@$(UV) run ruff check src/ tests/


test: ## run tests quickly with the default Python
	@$(UV) run pytest --cov src/{{cookiecutter.pkg_name}} --cov-report term-missing --cov-fail-under $(CODE_COVERAGE)  tests/ -v


coverage: ## check code coverage quickly with the default Python
	@$(UV) run pytest --cov src/{{cookiecutter.pkg_name}} --cov-report term-missing --cov-report html tests/

check: check_format lint type_check test ## run all checks without installing

check_format: ## check formatting with ruff
	$(info [*] Running ruff format checkers...)
	@$(UV) run ruff format --check src/ tests/

fix_format: ## format code with ruff
	$(info [*] Running ruff format fixers...)
	@$(UV) run ruff format src/ tests/

format: fix_format ## alias for fix_format
{%- if cookiecutter.use_analytics == "y" %}

install-analytics: ## Install analytics dependencies
	$(info [*] Installing analytics dependencies...)
	@$(UV) sync --extra analytics

jupyter: install-analytics ## Start Jupyter Lab
	$(info [*] Starting Jupyter Lab...)
	@$(UV) run --extra analytics jupyter lab

notebook: install-analytics ## Start Jupyter Notebook
	$(info [*] Starting Jupyter Notebook...)
	@$(UV) run --extra analytics jupyter notebook
{%- endif %}
