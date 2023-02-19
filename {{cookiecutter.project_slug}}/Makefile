
.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

PDM=pdm
CODE_COVERAGE=50

build: install test lint

install:
	$(PDM) install -d

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

mypy:
	-@$(PDM) run mypy  {{cookiecutter.project_module}}

lint: ## Check code with pyflakes and mypy ( errors ignored)
	@$(PDM) run ruff {{cookiecutter.project_module}}


test: ## run tests quickly with the default Python
	@$(PDM) run pytest --cov {{ cookiecutter.project_module }} --cov-report term-missing --cov-fail-under $(CODE_COVERAGE)  tests/ -v


coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.project_module }} -m pytest
	coverage report -m
	coverage html


