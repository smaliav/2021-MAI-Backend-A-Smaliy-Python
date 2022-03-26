up:
	docker-compose up -d

test: up
	docker-compose exec django-app python3 /app/manage.py test

migrate: up
	docker-compose exec django-app python3 /app/thatcar/manage.py migrate
