up:
		docker-compose -f docker-compose.prod.yaml up --build
up-dev:
		docker-compose -f docker-compose.dev.yaml up --build
down-dev:
		docker-compose -f docker-compose.dev.yaml down -v
down:
		docker-compose -f docker-compose.prod.yaml down -v