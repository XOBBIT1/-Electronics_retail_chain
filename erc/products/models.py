from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    product_model = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
