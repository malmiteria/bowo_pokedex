#!/bin/bash

poetry install
poetry run python manage.py migrate
poetry run python manage.py import_from_csv --path ./pokemon.csv

