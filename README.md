
install dependencies:
```
poetry install
```

run migrations:
```
poetry run python manage.py migrate
```

download csv into sqlite:
```
poetry run python import_from_csv --path ./pokemon.csv
```


