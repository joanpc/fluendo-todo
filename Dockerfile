#
# Django Dockerfile for development and production.
#
FROM python:3-alpine

WORKDIR /app

RUN apk add --no-cache \
    postgresql-client


# Build dependencies
RUN apk update && apk add --no-cache --virtual .build-deps \
    build-base \
    python3-dev \
    py-pip \
    jpeg-dev \
    zlib-dev \
    postgresql-dev


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Use waitress as our wsgi server.
RUN pip install --no-cache-dir waitress

# Remove build dependencies
RUN apk del --no-network .build-deps

COPY . .

# Override from Docker-compose file for development
CMD ["sh", "wait_for_postgresql.sh", "python3", "-m", "waitress", "fluendo_todo.wsgi:application"]