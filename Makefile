run:
	uvicorn project.main:app --host 0.0.0.0 --port 8000 --forwarded-allow-ips "*" --reload


create_migration:
	alembic -c project/alembic.ini revision --autogenerate -m "$(m)"

migrate_head:
	alembic -c project/alembic.ini upgrade head

migrate_down:
	alembic -c project/alembic.ini downgrade -1

current_revision:
	alembic -c project/alembic.ini current
