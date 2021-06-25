#!/bin/sh
# Wait for postgresql to be ready

set -e

until PGPASSWORD=$DJANGO_DB_PASSWORD psql -h "$DJANGO_DB_HOST" -U "$DJANGO_DB_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec "$@"

