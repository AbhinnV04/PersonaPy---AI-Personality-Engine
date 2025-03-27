from django.core.management.base import BaseCommand
from app.models import Product

class Command(BaseCommand):
    help = 'Seed the database with sample products'

    def handle(self, *args, **kwargs):
        Product.objects.create(name="Laptop", price=599.99)
        Product.objects.create(name="Smartphone", price=399.99)
        Product.objects.create(name="Headphones", price=49.99)
        self.stdout.write("Sample products added to the database.")
