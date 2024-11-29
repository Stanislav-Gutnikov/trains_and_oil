# syntax=docker/dockerfile:1
# check=skip=SecretsUsedInArgOrEnv
FROM python:3.10-slim
WORKDIR /trains_and_oil
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini ./
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
#COPY .env ./
#ENV DB_NAME=postgres
#ENV USER=postgres
#ENV PASSWORD=postgres
#ENV HOST=localhost
#ENV PORT=5432
#ENV DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost/postgres 
ENV XLSX_FILE_PATH=./app/api/get_db_data.xls

# Сделать скрипт исполняемым
RUN chmod +x /usr/local/bin/entrypoint.sh

# Установить entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]