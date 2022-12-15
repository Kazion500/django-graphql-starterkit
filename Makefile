start:
	uvicorn config.asgi:application --reload --host 0.0.0.0

up: 
	docker-compose up --build --force-recreate --remove-orphans

down:
	docker-compose down

migrate:
	- python3 manage.py migrate