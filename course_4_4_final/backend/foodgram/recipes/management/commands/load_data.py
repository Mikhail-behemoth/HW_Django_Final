import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'загруза исходных даннах в БД'

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv', encoding='utf-8') as f:
            for row in csv.reader(f):
                name, measurement_unit = row
                Ingredient.objects.get_or_create(
                    name=name, measurement_unit=measurement_unit
                )
