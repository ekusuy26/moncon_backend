up:
	docker-compose up
upd:
	docker-compose up -d
build_up:
	docker-compose up --build
build_upd:
	docker-compose up -d --build
in:
	docker-compose exec app sh
down:
	docker-compose down