.PHONY: install test lint format

install:
	poetry install

test:
	poetry run pytest

make lint:
	poetry run ruff check .

format:
	poetry run ruff format .

hooks:
	poetry run pre-commit run --all-files