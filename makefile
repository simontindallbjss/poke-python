.PHONY: install test lint format hooks coverage

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

hooks:
	poetry run pre-commit run --all-files

coverage:
	poetry run pytest --cov=poke_python --cov-report=term-missing

coverage-html:
	poetry run pytest --cov=poke_python --cov-report=html
	open htmlcov/index.html