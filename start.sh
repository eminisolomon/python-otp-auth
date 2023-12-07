alembic revision --autogenerate -m "update table"
alembic upgrade head
uvicorn app.main:app --reload