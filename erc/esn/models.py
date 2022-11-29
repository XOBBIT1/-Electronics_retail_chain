from django.db import models
from erc.settings import OBJECT_CHOICES


class ObjectModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)
    contacts = models.OneToOneField(
        "contacts.Contacts",
        related_name="contacts",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.CharField(max_length=20,
                            choices=OBJECT_CHOICES,
                            default="FACTORY")
    product = models.ManyToManyField(
        "products.Product", related_name="product", null=True
    )
    employees = models.ManyToManyField(
        "employees.Employees",
        related_name="employees",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
