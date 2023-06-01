
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


shell:
	docker-compose run --rm backend python manage.py shell

migrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate
