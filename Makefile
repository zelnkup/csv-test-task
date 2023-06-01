
set_env:
	cp .env.example .env


build:
	docker-compose build

run:
	docker-compose up


bash:
	docker-compose run --rm backend bash


pre-commit:
	pre-commit install
