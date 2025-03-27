from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)  # String field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
