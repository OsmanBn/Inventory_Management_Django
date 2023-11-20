from django.db import models

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics','Electronics'),
    ('Food', 'Food'),
)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)