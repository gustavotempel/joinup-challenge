# JoinUp Challenge

## How to set up the services:

### For PRODUCTION environment

#### Build and run the containers
- `docker compose -f docker-compose-prod.yaml build`
- `docker compose -f docker-compose-prod.yaml up -d`

#### Migrate models to the database
- `docker compose -p joinup-challenge exec app python manage.py migrate`

#### Run the tests
- `docker compose -p joinup-challenge exec app python manage.py test`

To find out where the messages services are running you can use the following commands to view the logs:

- `docker logs -f joinup_app`
- `docker logs -f joinup_async_worker`


#### Example of a request to register a user with synchronous message sending
```bash
curl --location 'http://localhost:8000/api/v1/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Gustavo",
    "last_name": "Tempel",
    "email": "gtempel@joinup.com",
    "phone": "1 222 333 4444",
    "hobbies": [
        "Swimming",
        "Videogames",
        "Travel"
    ]
}'
```

#### Example of a request to register a user with asynchronous message sending
```bash
curl --location 'http://localhost:8000/api/v2/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Gustavo",
    "last_name": "Tempel",
    "email": "gtempel@joinup.com",
    "phone": "1 222 333 4444",
    "hobbies": [
        "Swimming",
        "Videogames",
        "Travel"
    ]
}'
```

#### Example of a request to get user profile
```bash
curl --location 'http://localhost:8000/api/v1/profile/gtempel@joinup.com'
```

### For DEVELOPMENT environment

#### Build and run the containers
- `docker compose -f docker-compose-dev.yaml -p joinup-challenge-dev build`
- `docker compose -f docker-compose-dev.yaml -p joinup-challenge-dev up -d`

#### Migrate models to the database
- `docker compose -p joinup-challenge-dev exec app python manage.py migrate`

#### Run the tests
- `docker compose -p joinup-challenge-dev exec app python manage.py test`

To find out where the messages services are running you can use the following commands to view the logs:

- `docker logs -f joinup_app_dev`
- `docker logs -f joinup_async_worker_dev`

#### Example of a request to register a user (may use v1 or v2)
```bash
curl --location 'http://localhost:8001/api/v1/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Gustavo",
    "last_name": "Tempel",
    "email": "gtempel@joinup.com",
    "phone": "1 222 333 4444",
    "hobbies": [
        "Swimming",
        "Videogames",
        "Travel"
    ]
}'
```

#### Example of a request to get user profile
```bash
curl --location 'http://localhost:8001/api/v1/profile/gtempel@joinup.com'
```


## How to run unit tests locally:

Tests need a database to run, in this case a PostgreSQL db configured in the development docker compose:
- `docker compose -f docker-compose-dev.yaml -p joinup-challenge-dev up -d db`

Now, you can run tests locally:
- `poetry run python manage.py test`
