import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("category_data.json", encoding="UTF8") as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open("product_data.json", encoding="UTF8") as file:
            return json.load(file)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                )
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    preview=product["fields"]["preview"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
