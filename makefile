format:
  @echo "formatting..."
  poetry run ruff format

types:
    @echo "checking types..."
    poetry run mypy app

migrate:
    @echo "running migrations..."
    alembic revision --autogenerate -m 'initial migration1'