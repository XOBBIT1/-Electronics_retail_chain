from django.db.models import Avg, F
from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectType(models.TextChoices):
    FACTORY = "0", _("Factory")
    DISTRIBUTOR = "1", _("Distributor")
    LRC = "2", _("Large_retail_chain")
    DECEMBER = "3", _("December")
    IE = "4", _("Individual_entrepreneur")


class ObjectModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)
    contacts = models.OneToOneField(
        "contacts.Contacts",
        related_name="contacts",
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=20, choices=ObjectType.choices, default="FACTORY"
    )
    provider = models.OneToOneField(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    product = models.ManyToManyField("products.Product", related_name="product")
    employees = models.ManyToManyField(
        "employees.Employees",
        related_name="employees",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def calculate_average_debt():
        debt_awg = ObjectModel.objects.all().aggregate(Avg(F("debt")))
        all_data = ObjectModel.objects.all().filter(debt__gt=debt_awg["debt__avg"])
        return all_data
