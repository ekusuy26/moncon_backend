include .env

up:
	docker-compose up
upd:
	docker-compose up -d
build_up:
	docker-compose up --build
build_upd:
	docker-compose up -d --build
in:
	docker-compose exec app bash
db:
	docker-compose exec db bash
connect_db:
	docker-compose exec db mysql -u ${DB_USER} -p${DB_PASS}
down:
	docker-compose down
create_migration:
	docker-compose exec app bash -c "cd app/db && alembic revision --autogenerate -m '${FILENAME}'"
migrate:
	docker-compose exec app bash -c "cd app/db && alembic upgrade head"
rollback:
	docker-compose exec app bash -c "cd app/db && alembic downgrade base"
