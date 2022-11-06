install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

migrate:
	poetry run python -m django_boilerplate.manage migrate

migrations:
	poetry run python -m django_boilerplate.manage makemigrations

run-server:
	poetry run python -m django_boilerplate.manage runserver

superuser:
	 poetry run python -m django_boilerplate.manage createsuperuser

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.yml up --force-recreate db

update: install migrate install-pre-commit ;
