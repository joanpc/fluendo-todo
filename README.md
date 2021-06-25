# My Solution

I've implemented a todo list CRUD with token authentication.


# Setup

## Using Docker

Build and start the stack.

    docker-compose -f development.yml up --build

On a new terminal update the database and create a django user.

    docker container exec -it fluendo-todo_app_1 \
    python3 manage.py migrate
    
    docker container exec -it fluendo-todo_app_1 \
    python manage.py createsuperuser --username joan --email joan@fluendo.com

Set the password to: 12345 in order to use the following examples.
    

## Using virtual env

The code can also be tested just using virtualenv and sqlite.

    python manage.py migrate
    python manage.py createsuperuser --username joan --email joan@fluendo.com


# An API User story.


## As an API user, I want to be able to authenticate with the API.


I need to provide a user and password to get a token to add to subsequents calls to the API.

    curl http://127.0.0.1:8000/api/auth_token \
    -d '{"username": "joan", "password": "12345"}' \
    -H 'Content-Type: application/json'

    # Set an env variable with the new generated token
    export TOKEN=8322c32c70ea9cde7cc114bcfc9e7fa4c96e9ce4

## As an API user, I want to create a new Todo item

    curl -X POST http://127.0.0.1:8000/api/todo/ \
    -d '{"name": "My fluendo Django test", "completed": false}' \
    -H "Authorization: Token $TOKEN" \
    -H 'Content-Type: application/json'
    

## As an API user, I want to list the Todo  List.

    curl -X GET http://127.0.0.1:8000/api/todo/ \
    -H "Authorization: Token $TOKEN"


## As an API user, I want to update a Todo item

    curl -X PUT http://127.0.0.1:8000/api/todo/1/ \
    -d '{"id":1, "name": "My fluendo Django test", "completed": true}' \
    -H "Authorization: Token $TOKEN" \
    -H 'Content-Type: application/json'

## As an API user, I want to delete a Todo item

    curl -X DELETE http://127.0.0.1:8000/api/todo/1/ \
    -H "Authorization: Token $TOKEN" \
    

# Testing

I used the django rest framework to do testing on the TODO crud.

    docker container exec -it fluendo-todo_app_1 \
    python manage.py test
