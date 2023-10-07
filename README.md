
This repository hosts the back and front in separate folders.

`django` hosts the backend django app
`vue` hosts the frontend vue app


# Django
On first download, run (from the django directory):
```
./scripts/install.sh
```

it installs the dependencies, migrates the database up to date, and downloads the csv pokemon file into the database.

then, you can run the django app with (still from the django directory)
```
poetry run python manage.py runserver
```
