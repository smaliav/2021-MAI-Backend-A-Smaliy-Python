# Main
run: build up migrate

stop:
	docker-compose down

rerun: stop run

restart: stop up migrate

# Secondary
build:
	docker-compose build

up:
	docker-compose up -d

test: up
	docker-compose exec django-app python3 /app/manage.py test

migrate: up
	docker-compose exec django-app python3 /app/thatcar/manage.py migrate
