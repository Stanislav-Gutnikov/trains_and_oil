#!/bin/sh

# Ожидание, пока база данных станет доступной
until nc -z db 5432; do
  echo "Ожидание базы данных..."
  sleep 2
done

# Выполнение миграции Alembic
alembic upgrade head

# Запуск приложения
exec "$@"

