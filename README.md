# Getting started

This project users celery , redis , postgres and django to retrieve BTC prices on an hourly basis using scheduled tasks. The app is built in a docker container using docker-compose.

## Installation

Use the git command to clone the project to your local machine.

```bash
git clone https://github.com/farrem68/alphavantage.git
```

## Usage

To start the project use the following command while in the base directory
```bash
docker-compose up 
```
You should then execute the following command in a seperate terminal to enter the docker instance hosting the django app so you can access the management scripts.
```bash
docker exec -it django_app sh
```

We need to enter the manage.py interactive shell and create a user by using the following commands

```python
python manage.py shell 
>>> Username (leave blank to use 'root'):
>>> Email address:
>>> Password:
>>> Password (again):
```

Once you have created your user, you can test the API to get the latest BTC prices targeting the folling endpoints:
* GET /api/v1/get-prices
* POST /api/v1/get-prices

## Sending Requests

Checkout the request_template.py file to get started making requests and seeing the output.

You will also need to create your own .env file with the following variables.
```bash

DJANGO_SETTINGS_MODULE=DJANGO_SETTINGS_MODULE
DB_HOST=DB_HOST
POSTGRES_DB=POSTGRES_DB
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
SECRET_KEY=SECRET_KEY
DEBUG=DEBUG
ALLOWED_HOSTS=ALLOWED_HOSTS
ALPHAVANTAGE_KEY=ALPHAVANTAGE_KEY
CELERY_BROKER_URL=CELERY_BROKER_URL
CELERY_RESULT_BACKED=CELERY_RESULT_BACKED
CELERY_TIMEZONE=CELERY_TIMEZONE

```