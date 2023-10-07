import csv
from django.core.management import BaseCommand
from pokedex.models import Pokemon

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, path=None, **kwargs):
        if path is None:
            path = ""
        with open(path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for name, value in row.items():
                    if value == "":
                        row[name] = None
                Pokemon.objects.create(**row)
