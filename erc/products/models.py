from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    product_model = models.CharField(max_length=25, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Продукты"
