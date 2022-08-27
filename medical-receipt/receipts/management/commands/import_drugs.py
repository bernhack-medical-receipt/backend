from django.core.management.base import BaseCommand, CommandError
import csv
from ....receipts import models as receipts_models


class Command(BaseCommand):
    help = 'parses drugs from csv'

    def handle(self, *args, **options):
        with open('drugs.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            drugs = []
            for row in csvreader:
                drug_name, license_owner, category, package, unit, active, ingredients, application = row
                drugs.append(receipts_models.Drug(
                    title=drug_name,
                    license_owner=license_owner,
                    category=category,
                    package_size=package,
                    unit=unit,
                    active_ingredients=active,
                    ingredients=ingredients,
                    application=application
                ))

            objs = receipts_models.Drug.objects.bulk_create(drugs)
            self.stdout.write(self.style.SUCCESS('Successfully created drugs "%s"' % len(objs)))

