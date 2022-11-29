from django.db import models
from contacts.models import Contacts
from erc.settings import OBJECT_CHOICES

# class IndividualEntrepreneur(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False)
#     debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)
#     contacts = models.ForeignKey(
#         Contacts,
#         related_name="contacts_ie",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#     )
#     product = models.ManyToManyField(
#         "products.Product", related_name="product_ie", null=True
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     supplier = models.ForeignKey(
#         LargeRetailChain,
#         related_name="supplier_ie",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#     )
#     employees = models.CharField(max_length=50, null=False, blank=False)
#
#     class Meta:
#         verbose_name = "Индивидуальный предприниматель"


class ObjectModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)
    contacts = models.ForeignKey(
        Contacts,
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
