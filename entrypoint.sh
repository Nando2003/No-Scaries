#!/bin/sh
set -e

mkdir -p /django_app/staticfiles

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 2
done

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ "$DEBUG" = "1" ]; then
  echo "DEBUG MODE 🤖"
  exec python manage.py runserver 0.0.0:8000
else
  echo "PRODUCTION MODE 🚀"
  exec uvicorn core.asgi:application --host 0.0.0.0 --port 8000
fi